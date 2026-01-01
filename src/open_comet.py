#!/usr/bin/env python3
"""
Open Comet AI Assistant locally
Launches Comet browser (installed separately)
Uses pyautogui for automation
"""
import os
import time
import subprocess
import pyautogui
import pygetwindow as gw

def open_comet_browser():
    """
    Opens Comet browser (installed on system)
    Returns True if successful, False otherwise
    """
    try:
        print("Opening Comet browser...")
        
        # Launch Comet browser via command line
        # Adjust the path based on your installation
        comet_path = os.path.expanduser('~/.comet/comet.exe')
        
        # If not found in user path, try common installation paths
        if not os.path.exists(comet_path):
            comet_path = 'C:\\Program Files\\Comet\\comet.exe'
        
        if not os.path.exists(comet_path):
            comet_path = 'comet'  # Try system PATH
        
        # Open Comet browser
        subprocess.Popen(comet_path)
        
        # Wait for Comet to start
        time.sleep(5)
        
        # Try to find and focus the Comet window
        try:
            comet_windows = gw.getWindowsWithTitle('Comet')
            if comet_windows:
                comet_window = comet_windows[0]
                comet_window.activate()
                time.sleep(2)
                print("Comet browser opened and focused")
                return True
        except:
            print("Comet browser opened (could not activate window)")
            return True
        
        return True
        
    except Exception as e:
        print(f"Error opening Comet browser: {str(e)}")
        return False

def focus_comet_browser():
    """
    Focuses on the Comet browser window if it's already open
    """
    try:
        comet_windows = gw.getWindowsWithTitle('Comet')
        if comet_windows:
            comet_window = comet_windows[0]
            comet_window.activate()
            time.sleep(1)
            return True
    except:
        pass
    return False
