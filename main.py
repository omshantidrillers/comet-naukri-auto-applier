21:0
def launch_comet_browser():
    """Launches Comet Browser application"""
    system = sys.platform
    
    if system == 'win32':
        comet_paths = [
            r"C:\Program Files\Comet\Comet.exe",
            r"C:\Program Files (x86)\Comet\Comet.exe",
            rf"C:\Users\{Path.home().name}\AppData\Local\Comet\Comet.exe",
        ]
        for path in comet_paths:
            if Path(path).exists():
                subprocess.Popen(path)
                print(f"Launched from: {path}")
                time.sleep(3)
                return
        subprocess.Popen(['start', 'comet'], shell=True)
        print("Launched via system command")
        time.sleep(3)
    
    elif system == 'darwin':
        subprocess.Popen(['open', '-a', 'Comet'])
        print("Launched Comet application")
        time.sleep(3)
    
    elif system == 'linux':
        subprocess.Popen(['comet'])
        print("Launched Comet application")
        time.sleep(3)            paths = [r"C:\Program Files\Comet\Comet.exe", rf"C:\Users\{Path.home().name}\AppData\Local\Comet\Comet.exe"]
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

49

def click_assistant(driver):
    try:
        wait = WebDriverWait(driver, 20)
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class*='Assistant'] | //span[contains(text(), 'Assistant')]/ancestor::button | //*[@aria-label='Assistant'] | //button[.//span[contains(text(), 'Assistant')]] | //*[contains(text(), 'Assistant') and (@role='button' or self::button)]")))
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
        launch_comet_browser()
        time.sleep(2)
        
        print("\nConnecting to Comet browser...")
try:
            driver = webdriver.Chrome()  # Connect to Comet via debugging port
            print("Connected to Comet Browser")
        except Exception as e:
            print(f"Error connecting to Comet: {e}")
            print("Make sure Comet is running on port 9222")
            return 1
        print("Connected to Comet Browser")
        
        print("\nClicking Assistant button...")
        click_assistant(driver)
        
        print("\nTyping and submitting prompt...")
        if not type_and_submit_prompt(driver):
            print("Error in prompt submission")
            return 1
        
        print("\nMonitoring job applications...")
        wait_completion(driver)            print("Could not click Assistant - trying direct input...")
        
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
21
