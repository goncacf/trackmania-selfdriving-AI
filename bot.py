import ctypes
import cv2 as cv
import time
import numpy as np 
import pyautogui
from win32gui import FindWindow, GetWindowRect, SetForegroundWindow, ShowWindow


SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


#ACTUAL CODE

window_handle = FindWindow(None, "Trackmania")

ShowWindow(window_handle,5)
SetForegroundWindow(window_handle)

window_rect = GetWindowRect(window_handle)

time.sleep(0.1)

x = window_rect[0] + 10
y = window_rect[1] + 30
w = window_rect[2] - x -10
h = window_rect[3] - y -10

w_2=w/2
h_2=h/2

print("1...")

time.sleep(1)

print("2...")

time.sleep(1)

print("3...")


PressKey(0x2b)
time.sleep(1)
ReleaseKey(0x2b)
time.sleep(1)


t=0
print("start")
while(t<300):

    t+=1
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    
    xtrack = 0

    for ytrack in range(60,h - 100,2):
        r,g,b=screenshot.getpixel((w_2,y))

        if ((ytrack< 80) and (r > 30)):
            ReleaseKey(0x1f)
            PressKey(0x11)
          
        if ((ytrack < 80) and (r < 30)):   
            ReleaseKey(0x11)
            PressKey(0x1f)
            print(r)

        if ((xtrack < w_2)and (y<h-100)) :
            xtrack+=1
            rd,gd,dl=screenshot.getpixel((w_2 + xtrack,y))
            rl,gl,dl=screenshot.getpixel((w_2 - xtrack,y))
            if ((rd<30) and (rl>30)):
                 ReleaseKey(0x20)
                 PressKey(0x1e)
            if ((rd>30) and (rl<30)):
                 ReleaseKey(0x1e)
                 PressKey(0x20)

        
ReleaseKey(0x11)  


#while(True):

    #screenshot = pyautogui.screenshot(region=(x, y, w, h))
   # screenshot = np.array(screenshot)
    #screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)

    #cv.imshow('computer Vision', screenshot)

    #if cv.waitKey(1) == ord('q'):
    #    cv.destroyAllWindows()
     #   break

   # window_rect = GetWindowRect(window_handle)
    #x = window_rect[0] + 10
   # y = window_rect[1] + 30
   # w = window_rect[2] - x -10
   # h = window_rect[3] - y -10

print('done')