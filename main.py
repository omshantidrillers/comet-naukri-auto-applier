#!/usr/bin/env python3
"""
Comet Naukri Auto Applier - Main Entry Point
Automated job applications on Naukri.com using Comet AI Assistant
Runs daily at 5:00 AM IST on your local machine
"""

import os
import sys
import time
import subprocess
from datetime import datetime
from dotenv import load_dotenv
import pytz

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.keys import Keys
except ImportError:
    print("Selenium not installed. Install with: pip install selenium")
    sys.exit(1)

# Load environment variables
load_dotenv()

from src.job_tracker import track_applications, log_execution

def main():
    """
    Main orchestration function
    1. Open Comet browser
    2. Click assistant button on top right
    3. Inject job search prompt
    4. Monitor execution
    5. Track applications
    """
    
    # Get timezone
    timezone = os.getenv('TIMEZONE', 'Asia/Kolkata')
    tz = pytz.timezone(timezone)
    
    # Print header
    print("\n" + "="*70)
    print("🚀 Comet Naukri Auto Applier")
    print("="*70)
    print(f"Time: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Timezone: {timezone}")
    print("="*70 + "\n")
    
    driver = None
    
    try:
        # Step 1: Log execution start
        print("📝 Logging execution start...")
        log_execution('START')
        
        # Step 2: Open Comet browser
        print("\n🌐 Step 1: Opening Comet Browser...")
        driver = open_comet_with_selenium()
        if not driver:
            raise Exception("Failed to open Comet with Selenium")
        print("   ✅ Comet Browser opened successfully")
        time.sleep(5)  # Wait for Comet to fully load
        
        # Step 3: Navigate to Comet and interact with assistant
        print("\n📨 Step 2: Clicking Assistant Button and Sending Prompt...")
        result = inject_prompt_to_comet(driver)
        if not result:
            raise Exception("Failed to inject prompt to Comet")
        print("   ✅ Prompt injected successfully")
        time.sleep(5)
        
        # Step 4: Open Naukri in a new tab for job search
        print("\n🌐 Step 3: Opening Naukri.com in browser...")
        driver.execute_script('window.open("https://www.naukri.com/jobs");')
        time.sleep(3)
        
        # Step 5: Monitor execution
        print("\n⏳ Step 4: Monitoring job application process...")
        print("   Waiting for Comet to process (max 10 minutes)...")
        time.sleep(30)  # Wait for applications to be submitted
        
        # Track applications from local logs
        applications = track_applications()
        
        # Step 6: Report results
        print(f"\n✅ Step 5: Job application complete!")
        print(f"   Total applications: {len(applications)}/5")
        print(f"\n   Applied to:")
        for app in applications:
            print(f"   - {app['company']} | {app['job_title']} | {app['location']}")
        
        # Log completion
        log_execution('SUCCESS', len(applications))
        
        print("\n" + "="*70)
        print("🎉 Daily job application completed successfully!")
        print("="*70 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        log_execution('ERROR', error=str(e))
        return 1
    
    finally:
        # Keep browser open for monitoring
        if driver:
            try:
                print("\n🔚 Keeping Comet browser open for monitoring...")
                print("   You can manually monitor the process and close when done.")
                # Don't close - keep browser open
                # driver.quit()
            except:
                pass

def open_comet_with_selenium():
    """
    Opens Comet browser and returns Selenium WebDriver instance
    Comet runs on localhost (usually http://localhost:3000)
    """
    try:
        print("   Initializing Chrome WebDriver for Comet...")
        
        # Chrome options
        options = webdriver.ChromeOptions()
        
        # Try to add Comet extension
        try:
            comet_extension = os.getenv('COMET_EXTENSION_PATH')
            if comet_extension and os.path.exists(comet_extension):
                options.add_extension(comet_extension)
        except:
            pass
        
        options.add_argument('--start-maximized')
        
        # Initialize Chrome driver
        driver = webdriver.Chrome(options=options)
        
        # Navigate to Comet (usually localhost:3000 or perplexity.ai)
        print("   Navigating to Comet...")
        driver.get('http://localhost:3000')
        
        # Wait for page to load
        time.sleep(3)
        
        return driver
        
    except Exception as e:
        print(f"   Error opening Chrome: {str(e)}")
        print("   Trying alternative method...")
        
        # Fallback: Try opening via subprocess
        try:
            subprocess.Popen('start chrome http://localhost:3000', shell=True)
            time.sleep(3)
            return webdriver.Chrome()
        except:
            return None

def inject_prompt_to_comet(driver):
    """
    Finds and clicks the assistant button on top right
    Then types the job search prompt in the input field
    """
    try:
        wait = WebDriverWait(driver, 10)
        
        # Step 1: Click assistant button (usually on top right)
        print("   Searching for assistant button...")
        
        # Try multiple selectors for assistant button
        assistant_selectors = [
            "//button[contains(@aria-label, 'assistant')]",
            "//button[contains(@aria-label, 'Assistant')]",
            "//div[@class='copilot-button']",
            "//button[contains(text(), 'Assistant')]",
            "//button[contains(@class, 'assistant')]",
        ]
        
        assistant_button = None
        for selector in assistant_selectors:
            try:
                assistant_button = driver.find_element(By.XPATH, selector)
                if assistant_button:
                    print(f"   Found assistant button")
                    break
            except:
                continue
        
        if assistant_button:
            assistant_button.click()
            print("   Clicked assistant button")
            time.sleep(2)
        
        # Step 2: Find and click on the input field
        print("   Searching for input field...")
        
        input_selectors = [
            "//textarea[@placeholder='Ask anything...']" ,
            "//textarea[@placeholder='Ask a follow-up']",
            "//div[@role='textbox']",
            "//input[@placeholder*='Ask']",
            "//textarea[@class*='input']",
        ]
        
        input_field = None
        for selector in input_selectors:
            try:
                input_field = driver.find_element(By.XPATH, selector)
                if input_field:
                    print(f"   Found input field")
                    break
            except:
                continue
        
        if not input_field:
            # Last resort - find any textarea
            input_field = driver.find_element(By.TAG_NAME, 'textarea')
        
        # Click the input field
        input_field.click()
        time.sleep(1)
        
        # Step 3: Clear any existing text
        input_field.send_keys(Keys.CONTROL + 'a')
        input_field.send_keys(Keys.DELETE)
        time.sleep(0.5)
        
        # Step 4: Read and type the prompt
        print("   Reading prompt from file...")
        prompt_file = 'prompts/comet_prompt.txt'
        if not os.path.exists(prompt_file):
            raise Exception(f"Prompt file not found: {prompt_file}")
        
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()
        
        # Type the prompt
        print("   Typing prompt into input field...")
        input_field.send_keys(prompt)
        time.sleep(2)
        
        # Step 5: Find and click submit button
        print("   Searching for submit button...")
        
        submit_selectors = [
            "//button[contains(@aria-label, 'Submit')]",
            "//button[contains(@aria-label, 'Send')]",
            "//button[contains(text(), 'Submit')]",
            "//button[contains(text(), 'Send')]",
            "//button[@type='submit']",
        ]
        
        submit_button = None
        for selector in submit_selectors:
            try:
                submit_button = driver.find_element(By.XPATH, selector)
                if submit_button and submit_button.is_displayed():
                    print(f"   Found submit button")
                    break
            except:
                continue
        
        if submit_button:
            submit_button.click()
            print("   Clicked submit button")
            time.sleep(2)
        else:
            # Try pressing Enter
            print("   Pressing Enter to submit...")
            input_field.send_keys(Keys.RETURN)
            time.sleep(2)
        
        return True
        
    except Exception as e:
        print(f"   Error injecting prompt: {str(e)}")
        return False

if __name__ == "__main__":
    sys.exit(main())
