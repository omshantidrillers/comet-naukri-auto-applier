import subprocess
import time
import pyautogui
import pygetwindow as gw
from config import COMET_PATH, COMET_LAUNCH_WAIT, WINDOW_FOCUS_WAIT, CLICK_WAIT, TYPING_INTERVAL, PROMPT, ASSISTANT_BUTTON_X, ASSISTANT_BUTTON_Y


def open_comet():
    """Launch Comet browser application"""
    print("Launching Comet...")
    subprocess.Popen(COMET_PATH)
    time.sleep(COMET_LAUNCH_WAIT)


def focus_comet_window():
    """Focus Comet window to bring it to foreground"""
    print("Focusing Comet window...")
    windows = gw.getWindowsWithTitle("Comet")
    if windows:
        windows[0].activate()
        time.sleep(WINDOW_FOCUS_WAIT)
    else:
        raise Exception("Comet window not found. Make sure Comet is running.")


def click_assistant_button():
    """Click the Assistant button in Comet"""
    print("Clicking Assistant button...")
    pyautogui.click(x=ASSISTANT_BUTTON_X, y=ASSISTANT_BUTTON_Y)
    time.sleep(CLICK_WAIT)


def send_prompt():
    """Send job search prompt to Comet Assistant"""
    print("Sending prompt to Comet Assistant...")
    pyautogui.typewrite(PROMPT, interval=TYPING_INTERVAL)
    pyautogui.press("enter")
