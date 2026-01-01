#!/usr/bin/env python3
"""
Send prompt to Comet AI Assistant
Uses pyautogui to click assistant button and type prompt
"""
import time
import os
import pyautogui

def send_prompt_to_comet():
    """
    Sends the job search prompt to Comet AI Assistant
    1. Clicks the Assistant button (top right)
    2. Reads prompt from prompts/comet_prompt.txt
    3. Types the prompt into the assistant
    4. Sends it
    """
    try:
        # Wait for Comet to fully load
        time.sleep(2)
        
        # Step 1: Click the Assistant button (top right of Comet)
        # Adjust coordinates based on your screen resolution
        ASSISTANT_BUTTON_X = 1820
        ASSISTANT_BUTTON_Y = 60
        
        print(f"Clicking Assistant button at ({ASSISTANT_BUTTON_X}, {ASSISTANT_BUTTON_Y})...")
        pyautogui.click(ASSISTANT_BUTTON_X, ASSISTANT_BUTTON_Y)
        time.sleep(2)
        
        # Step 2: Read the prompt from file
        prompt_file = 'prompts/comet_prompt.txt'
        if not os.path.exists(prompt_file):
            print(f"Error: Prompt file not found: {prompt_file}")
            return False
        
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()
        
        print(f"Prompt loaded: {len(prompt)} characters")
        
        # Step 3: Click in the prompt text area
        # The text input area in assistant should appear
        time.sleep(1)
        pyautogui.click(900, 500)  # Click in the middle area to focus on input
        time.sleep(1)
        
        # Step 4: Type the prompt
        print("Typing prompt...")
        pyautogui.typewrite(prompt, interval=0.01)  # Slow typing to avoid issues
        time.sleep(2)
        
        # Step 5: Send the prompt (press Enter)
        print("Sending prompt...")
        pyautogui.press('return')
        time.sleep(3)
        
        print("Prompt sent successfully")
        return True
        
    except Exception as e:
        print(f"Error sending prompt to Comet: {str(e)}")
        return False
