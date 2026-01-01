#!/usr/bin/env python3
import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv
import pytz

try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
except ImportError:
    print("Selenium not installed. Install with: pip install selenium")
    sys.exit(1)

load_dotenv()
from src.job_tracker import track_applications, log_execution

def open_comet():
    try:
        print("Opening Chrome WebDriver...")
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=options)
        driver.get('http://localhost:3000')
        time.sleep(3)
        return driver
    except Exception as e:
        print(f"Error opening Chrome: {e}")
        return None

def click_assistant_and_inject(driver):
    try:
        print("Finding assistant button...")
        selectors = [
            "//button[contains(text(), 'Assistant')]",
            "//button[contains(@aria-label, 'Assistant')]",
            "//button[@class*='assistant']",
        ]
        
        button = None
        for selector in selectors:
            try:
                button = driver.find_element(By.XPATH, selector)
                break
            except:
                pass
        
        if button:
            button.click()
            print("Clicked assistant button")
            time.sleep(2)
        
        print("Finding input field...")
        input_selectors = [
            "//textarea[@placeholder='Ask anything...']",
            "//textarea",
        ]
        
        input_field = None
        for selector in input_selectors:
            try:
                input_field = driver.find_element(By.XPATH, selector)
                break
            except:
                pass
        
        if input_field:
            input_field.click()
            time.sleep(1)
            
            prompt_file = 'prompts/comet_prompt.txt'
            if not os.path.exists(prompt_file):
                raise Exception(f"Prompt file not found: {prompt_file}")
            
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt = f.read().strip()
            
            input_field.send_keys(prompt)
            time.sleep(2)
            input_field.send_keys(Keys.RETURN)
            print("Prompt sent")
            return True
        
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    timezone = os.getenv('TIMEZONE', 'Asia/Kolkata')
    tz = pytz.timezone(timezone)
    
    print("\n" + "="*70)
    print("Comet Naukri Auto Applier")
    print("="*70)
    print(f"Time: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70 + "\n")
    
    driver = None
    
    try:
        log_execution('START')
        print("Step 1: Opening Comet...")
        driver = open_comet()
        
        if not driver:
            raise Exception("Failed to open browser")
        
        print("Step 2: Injecting prompt...")
        result = click_assistant_and_inject(driver)
        
        if not result:
            print("Warning: Prompt injection may have failed")
        
        print("Step 3: Opening Naukri...")
        driver.execute_script('window.open("https://www.naukri.com/jobs");')
        time.sleep(3)
        
        print("Step 4: Monitoring applications...")
        time.sleep(30)
        
        applications = track_applications()
        print(f"Total applications: {len(applications)}/5")
        
        for app in applications:
            print(f"- {app['company']} | {app['job_title']} | {app['location']}")
        
        log_execution('SUCCESS', len(applications))
        print("\nJob application completed!\n")
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        log_execution('ERROR', error=str(e))
        return 1
    
    finally:
        print("Process complete. Browser remains open.")

if __name__ == "__main__":
    sys.exit(main())
