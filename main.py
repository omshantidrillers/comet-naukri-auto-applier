#!/usr/bin/env python3
import subprocess
import time
import pyautogui
import pygetwindow as gw
from config import COMET_PATH, PROMPT, COMET_LAUNCH_WAIT, WINDOW_FOCUS_WAIT, CLICK_WAIT, TYPING_INTERVAL
from src.automation import open_comet, focus_comet_window, click_assistant_button, send_prompt
from src.job_tracker import log_automation_start, log_automation_end, log_error


if __name__ == "__main__":
    try:
        log_automation_start()
        
        print("\n" + "="*70)
        print("Comet Naukri Auto Applier - PyAutoGUI Approach")
        print("="*70 + "\n")
        
        open_comet()
        focus_comet_window()
        click_assistant_button()
        send_prompt()
        
        print("\n" + "="*70)
        print("SUCCESS: Job applications automation completed!")
        print("Check your Comet window for application status.")
        print("="*70 + "\n")
        
        log_automation_end(True, "Successfully applied to jobs")
        
    except Exception as e:
        print(f"\nERROR: {e}")
        log_error(str(e))
        log_automation_end(False, str(e))
