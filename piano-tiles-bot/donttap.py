"""
Game Automation Script - Don't Tap Game Bot
Copyright (c) 2025 WanDaiser
Licensed under Custom Software License - see LICENSE file
Contact: salihefeggl@gmail.com
"""

import pyautogui
import time
import win32api , win32con
from pyautogui import *
import keyboard

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(x=743, y=360)[0] == 0:
        click(x=743, y=360)
    if pyautogui.pixel(x=890, y=349)[0] == 0:
        click(x=890, y=349)
    if pyautogui.pixel(x=1010, y=348)[0] == 0:
        click(x=1010, y=348)
    if pyautogui.pixel(x=1165, y=338)[0] == 0:
        click(x=1165, y=338)  
    if pyautogui.pixel(x=1180, y=485)[0] == 0:
        click(x=1180, y=485)
    if pyautogui.pixel(x=1031, y=476)[0] == 0:
        click(x=1031, y=476)
    if pyautogui.pixel(x=862, y=475)[0] == 0:
        click(x=862, y=475)
    if pyautogui.pixel(x=740, y=469)[0] == 0:
        click(x=740, y=469)  
    if pyautogui.pixel(x=751, y=619)[0] == 0:
        click(x=751, y=619)
    if pyautogui.pixel(x=902, y=619)[0] == 0:
        click(x=902, y=619)
    if pyautogui.pixel(x=1048, y=617)[0] == 0:
        click(x=1048, y=617)
    if pyautogui.pixel(x=1182, y=624)[0] == 0:
        click(x=1182, y=624)   
    if pyautogui.pixel(x=1201, y=800)[0] == 0:
        click(x=1201, y=800)
    if pyautogui.pixel(x=1012, y=771)[0] == 0:
        click(x=1012, y=771)
    if pyautogui.pixel(x=875, y=768)[0] == 0:
        click(x=875, y=768)
    if pyautogui.pixel(x=730, y=766)[0] == 0:
        click(x=730, y=766)        