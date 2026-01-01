#!/usr/bin/env python3
import time
import subprocess
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PROMPT = """You are a job search assistant on Naukri.com.
1. Search for: Cloud Engineer, Senior Cloud Engineer, DevOps Engineer
2. Locations: Pan India, Gurugram, Remote
3. Experience: 3-6 years, Posted within: Last 24 hours
4. Apply to exactly 5 jobs that match criteria
5. Skip consultancy jobs and duplicates
6. Use message: 'I have 3+ years cloud infrastructure, automation, CI/CD, and Kubernetes experience. Looking forward to contributing.'
7. Return summary of 5 jobs applied with company name, job title, location"""

def launch_comet():
    print("Launching Comet Browser...")
    system = sys.platform
    try:
        if system == 'win32':
            paths = [r"C:\Program Files\Comet\Comet.exe", rf"C:\Users\{Path.home().name}\AppData\Local\Comet\Comet.exe"]
            for p in paths:
                if Path(p).exists():
                    subprocess.Popen(p)
                    print(f"Launched from: {p}")
                    time.sleep(4)
                    return True
        elif system == 'darwin':
            subprocess.Popen(['open', '-a', 'Comet'])
            print("Launched Comet")
            time.sleep(4)
            return True
        elif system == 'linux':
            subprocess.Popen(['comet'])
            print("Launched Comet")
            time.sleep(4)
            return True
    except Exception as e:
        print(f"Error: {e}")
    return False

def click_assistant(driver):
    try:
        wait = WebDriverWait(driver, 20)
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Assistant')] | //*[contains(text(), 'Assistant')]")))
        btn.click()
        print("Clicked Assistant button")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"Error clicking Assistant: {e}")
        return False

def type_and_submit_prompt(driver):
    try:
        wait = WebDriverWait(driver, 20)
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder*='Ask'] | //textarea[@placeholder*='Ask'] | //div[@role='textbox'] | //input[@type='text']")))
        input_box.click()
        time.sleep(1)
        input_box.send_keys(PROMPT)
        print(f"Typed prompt ({len(PROMPT)} chars)")
        time.sleep(2)
        input_box.send_keys(Keys.RETURN)
        print("Submitted prompt")
        return True
    except Exception as e:
        print(f"Error submitting prompt: {e}")
        return False

def wait_completion(driver):
    print("Waiting for Comet to apply jobs (this may take 2-5 minutes)...")
    start = time.time()
    while time.time() - start < 600:
        try:
            response_text = driver.find_element(By.XPATH, "//div[contains(@class, 'response')] | //div[contains(text(), 'Successfully')] | //div[contains(text(), 'applied')]").text
            if response_text and ('success' in response_text.lower() or 'applied' in response_text.lower()):
                print(f"Task complete: {response_text[:150]}")
                return True
        except:
            pass
        time.sleep(5)
    print("Task may still be running...")
    return False

def main():
    print("\n" + "="*70)
    print("Comet Naukri Auto Applier - Fully Automated")
    print("="*70 + "\n")
    
    driver = None
    try:
        if not launch_comet():
            print("Failed to launch Comet")
            return 1
        
        print("\nConnecting to Comet browser...")
        options = webdriver.ChromeOptions()
        options.add_argument("--remote-debugging-port=9222")
        driver = webdriver.Chrome(options=options)
        print("Connected to Comet Browser")
        
        print("\nClicking Assistant button...")
        if not click_assistant(driver):
            print("Could not click Assistant - trying direct input...")
        
        print("\nTyping and submitting prompt...")
        if not type_and_submit_prompt(driver):
            print("Error in prompt submission")
            return 1
        
        print("\nMonitoring job applications...")
        wait_completion(driver)
        
        print("\n" + "="*70)
        print("SUCCESS: Job applications process initiated!")
        print("Check your Comet window for status.")
        print("="*70 + "\n")
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    finally:
        if driver:
            try:
                time.sleep(5)
                driver.quit()
            except:
                pass

if __name__ == "__main__":
    sys.exit(main())
