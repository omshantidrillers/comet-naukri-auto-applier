"""
Send prompt to Comet AI Assistant
Injects job search instructions via Perplexity UI
"""

import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_prompt_to_comet(driver):
    """
    Sends the job search prompt to Comet AI Assistant
    Reads from prompts/comet_prompt.txt and injects into Comet's input
    """
    try:
        # Read prompt from file
        prompt_file = 'prompts/comet_prompt.txt'
        if not os.path.exists(prompt_file):
            print(f"Warning: Prompt file not found: {prompt_file}")
            return False
        
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()
        
        # Wait for input field to be ready
        wait = WebDriverWait(driver, 15)
        input_field = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "[role='textbox']"))
        )
        
        # Click to focus
        input_field.click()
        time.sleep(1)
        
        # Send the prompt
        input_field.send_keys(prompt)
        time.sleep(2)
        
        # Find and click submit button
        submit_btn = driver.find_element(By.XPATH, "//button[contains(text(), 'Send') or contains(text(), 'Submit')]")
        submit_btn.click()
        
        return True
        
    except Exception as e:
        print(f"Error sending prompt to Comet: {str(e)}")
        return False
