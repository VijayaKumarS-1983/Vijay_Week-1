import pyautogui
import subprocess
import time

# Open Chrome
subprocess.Popen(r"C:\Program Files\Google\Chrome\Application\chrome.exe")

# Wait for Chrome to launch
time.sleep(5)

# Open a new tab
pyautogui.hotkey('ctrl', 't')
time.sleep(1)

# Navigate to Google
pyautogui.write('https://www.google.com', interval=0.05)
pyautogui.press('enter')

time.sleep(3)

# Open another new tab
# Go to Gmail login page in the SAME tab
pyautogui.hotkey("ctrl", "l")  # Focus address bar
time.sleep(1)

pyautogui.write("https://accounts.google.com/signin", interval=0.05)
pyautogui.press("enter")