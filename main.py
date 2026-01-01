#!/usr/bin/env python3
import os
import sys
import time
import requests
from datetime import datetime
from dotenv import load_dotenv
import pytz
import webbrowser

load_dotenv()
from src.job_tracker import track_applications, log_execution

def send_prompt_to_comet():
    try:
        print("Connecting to Comet at http://localhost:3000...")
        
        prompt_file = 'prompts/comet_prompt.txt'
        if not os.path.exists(prompt_file):
            raise Exception(f"Prompt file not found: {prompt_file}")
        
        with open(prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read().strip()
        
        print(f"Prompt loaded ({len(prompt)} chars)")
        print("Opening Comet in browser...")
        webbrowser.open('http://localhost:3000')
        
        time.sleep(3)
        print("Please paste this prompt into Comet's input field:")
        print("\n" + "="*70)
        print(prompt)
        print("="*70)
        print("\nWaiting for you to paste and submit the prompt...")
        print("\nPress Enter once you've applied for jobs in Comet...")
        input()
        
        return True
        
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
    
    try:
        log_execution('START')
        print("Step 1: Opening Comet Assistant...")
        result = send_prompt_to_comet()
        
        if not result:
            print("Warning: Comet connection may have failed")
        
        print("\nStep 2: Opening Naukri.com...")
        webbrowser.open('https://www.naukri.com/jobs')
        time.sleep(3)
        
        print("Step 3: Monitoring applications...")
        time.sleep(10)
        
        applications = track_applications()
        print(f"Total applications tracked: {len(applications)}/5")
        
        for app in applications:
            print(f"- {app['company']} | {app['job_title']} | {app['location']}")
        
        log_execution('SUCCESS', len(applications))
        print("\nJob application process completed!\n")
        return 0
    
    except Exception as e:
        print(f"Error: {e}")
        log_execution('ERROR', error=str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main())
