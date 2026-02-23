import cv2
import numpy as np
import pyautogui
from PIL import ImageGrab
import os
import time

TEMPLATE_DIR = 'templates'
SCREEN_REGION = (0, 129, 1657, 658)

def load_templates():
    templates = []
    for digit in range(10):
        digit_path = os.path.join(TEMPLATE_DIR, str(digit))
        if not os.path.exists(digit_path):
            print(f"[ERROR] Directory does not exist: {digit_path}")
            continue
        
        for fname in os.listdir(digit_path):
            path = os.path.join(digit_path, fname)
            print(f"[DEBUG] Loading template: {path}")
            if not os.path.isfile(path):
                print(f"[ERROR] Not a file: {path}")
                continue
            
            img = cv2.imread(path)
            if img is None:
                print(f"[ERROR] Failed to load image: {path}")
                continue
            
            # Görüntüyü griye çevir ve uint8 formatında tut
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = img.astype(np.uint8)
            
            print(f"[DEBUG] Template digit {digit}: shape={img.shape}, dtype={img.dtype}")
            templates.append((digit, img))
    
    return templates

def non_max_suppression(detections, min_distance=15):
    """
    Smart NMS: Filters only truly overlapping digits
    """
    if len(detections) == 0:
        return []
    
    detections = sorted(detections, key=lambda x: x[0])
    
    keep = []
    
    for i, (x, digit, pt, confidence, w, h) in enumerate(detections):
        should_keep = True
        
        for kept_detection in keep:
            kept_x, kept_digit, kept_pt, kept_conf, kept_w, kept_h = kept_detection
            
            x_distance = abs(x - kept_x)
            y_distance = abs(pt[1] - kept_pt[1])
            
            if x_distance < min_distance and y_distance < 10:
                if confidence > kept_conf:
                    keep.remove(kept_detection)
                    print(f"[DEBUG] NMS: Replaced digit {kept_digit} (conf: {kept_conf:.3f}) with digit {digit} (conf: {confidence:.3f})")
                else:
                    should_keep = False
                    print(f"[DEBUG] NMS: Rejected digit {digit} (conf: {confidence:.3f}) in favor of digit {kept_digit} (conf: {kept_conf:.3f})")
                break
        
        if should_keep:
            keep.append((x, digit, pt, confidence, w, h))
    
    print(f"[DEBUG] NMS: Kept {len(keep)} out of {len(detections)} detections")
    
    keep = sorted(keep, key=lambda x: x[0])
    return keep

def match_digits(image, templates):
    detected = []
    
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)
    
    print(f"[DEBUG] Screenshot shape: {image.shape}, dtype: {image.dtype}")
    
    for digit, template in templates:
        if template is None:
            print(f"[ERROR] Template for digit {digit} failed to load.")
            continue
        
        if template.dtype != np.uint8:
            template = template.astype(np.uint8)
        
        print(f"[DEBUG] Processing digit {digit}: template shape={template.shape}, dtype={template.dtype}")
        
        try:
            result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
        except cv2.error as e:
            print(f"[ERROR] Template matching failed for digit {digit}: {e}")
            continue
        
        threshold = 0.65
        loc = np.where(result >= threshold)
        
        w, h = template.shape[1], template.shape[0]
        
        for pt in zip(*loc[::-1]):
            confidence = result[pt[1], pt[0]]
            detected.append((pt[0], digit, pt, confidence, w, h))
            print(f"[DEBUG] Digit {digit} found at ({pt[0]}, {pt[1]}) with confidence {confidence:.3f}")
    
    print(f"[DEBUG] Total detections before NMS: {len(detected)}")
    for i, (x, digit, pt, conf, w, h) in enumerate(detected):
        print(f"[DEBUG] Detection {i}: Digit {digit} at ({x}, {pt[1]}) with confidence {conf:.3f}")
    
    detected = non_max_suppression(detected)
    print(f"[DEBUG] Total detections after NMS: {len(detected)}")
    
    detected = sorted(detected, key=lambda x: x[0])
    
    return [(x, digit, pt) for x, digit, pt, _, _, _ in detected]

def main():
    print("Starting in 2 seconds...")
    time.sleep(2)
    
    pyautogui.click(x=837, y=544)
    time.sleep(0.5)
    
    screenshot = ImageGrab.grab(bbox=SCREEN_REGION)
    
    screenshot_np = np.array(screenshot)
    print(f"[DEBUG] Original screenshot shape: {screenshot_np.shape}, dtype: {screenshot_np.dtype}")
    
    screenshot_cv = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    
    templates = load_templates()
    if not templates:
        print("[ERROR] No templates loaded!")
        return
    
    screenshot_gray = cv2.cvtColor(screenshot_cv, cv2.COLOR_BGR2GRAY)
    screenshot_gray = screenshot_gray.astype(np.uint8)
    
    print(f"[DEBUG] Final gray image shape: {screenshot_gray.shape}, dtype: {screenshot_gray.dtype}")
    
    digits = match_digits(screenshot_gray, templates)
    
    if digits:
        number_str = ''.join(str(d[1]) for d in digits)
        print(f'Detected number: {number_str}')
        print(f'Total digits: {len(digits)}')
        
        while True:
            if pyautogui.pixel(568,402)==(34,108,187):
                pyautogui.click(x=834, y=404)
            
                pyautogui.write(number_str)
            
                pyautogui.click(x=818, y=484)
                break
        
        
        print("Process completed!")
    else:
        print("NO DIGITS DETECTED")
        print("Possible reasons:")
        print("- Template files missing or in wrong location")
        print("- Threshold value too high (0.65)")
        print("- Screen resolution or coordinates mismatch")

if __name__ == "__main__":
    for i in range(50):    
        main()
        