"""
Open Comet AI Assistant locally
Launches Chrome with Comet extension
"""

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_comet_browser():
    """
    Opens Chrome browser with Comet AI Assistant
    Returns selenium webdriver instance
    """
    try:
        # Set Chrome options
        options = webdriver.ChromeOptions()
        
        # Add Comet extension (if you have the extension ID)
        extension_id = os.getenv('COMET_EXTENSION_ID')
        if extension_id:
            options.add_extension(extension_id)
        
        # Set user data directory for persistent login
        user_data_dir = os.path.expanduser('~/.comet-naukri-applier')
        options.add_argument(f'user-data-dir={user_data_dir}')
        
        # Start maximized
        options.add_argument('--start-maximized')
        
        # Initialize webdriver
        driver = webdriver.Chrome(options=options)
        
        # Navigate to Comet Perplexity
        driver.get('https://www.perplexity.ai')
        
        # Wait for Comet to load (max 30 seconds)
        try:
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "[role='textbox']"))
            )
            time.sleep(2)  # Extra wait for full load
        except:
            pass  # Continue even if element not found
        
        return driver
        
    except Exception as e:
        print(f"Error opening Comet browser: {str(e)}")
        return None

def close_browser(driver):
    """
    Closes the browser instance
    """
    try:
        driver.quit()
        return True
    except:
        return False
