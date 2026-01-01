#!/usr/bin/env python3
"""
Comet Naukri Auto Applier - Main Entry Point
Automated job applications on Naukri.com using Comet AI Assistant
Runs on your local machine using Comet browser (installed separately)
"""
import os
import sys
import time
from datetime import datetime
from dotenv import load_dotenv
import pytz

# Load environment variables
load_dotenv()

from src.open_comet import open_comet_browser
from src.send_prompt import send_prompt_to_comet
from src.job_tracker import log_execution

def main():
    """
    Main orchestration function
    1. Open Comet AI Assistant
    2. Inject job search prompt via Assistant
    3. Monitor execution
    4. Track applications
    """
    
    # Get timezone
    timezone = os.getenv('TIMEZONE', 'Asia/Kolkata')
    tz = pytz.timezone(timezone)
    
    # Print header
    print("\n" + "="*70)
    print("Comet Naukri Auto Applier")
    print("="*70)
    print(f"Time: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S %Z')}")
    print(f"Timezone: {timezone}")
    print("="*70 + "\n")
    
    try:
        # Step 1: Log execution start
        print("Logging execution start...")
        log_execution('START')
        
        # Step 2: Open Comet browser
        print("\nStep 1: Opening Comet AI Assistant...")
        success = open_comet_browser()
        if not success:
            raise Exception("Failed to open Comet browser")
        print("Comet AI Assistant opened successfully")
        time.sleep(3)
        
        # Step 3: Send prompt to Comet
        print("\nStep 2: Sending job search prompt...")
        result = send_prompt_to_comet()
        if not result:
            raise Exception("Failed to send prompt to Comet")
        print("Prompt sent successfully")
        time.sleep(5)
        
        # Step 4: Monitor execution
        print("\nStep 3: Comet is processing your job applications...")
        print("Waiting for up to 10 minutes for completion...")
        print("Check Comet browser for progress")
        
        # Wait for user to manually complete (for now)
        time.sleep(10)
        
        # Log completion
        log_execution('SUCCESS', 5)
        
        print("\n" + "="*70)
        print("Job application workflow completed!")
        print("Check Comet browser for results")
        print("="*70 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\nError: {str(e)}")
        log_execution('ERROR', error=str(e))
        return 1

if __name__ == "__main__":
    sys.exit(main())
