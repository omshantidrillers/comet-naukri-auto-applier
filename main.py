#!/usr/bin/env python3
"""
Comet Naukri Auto Applier - Main Entry Point
Automated job applications on Naukri.com using Comet AI Assistant
Runs daily at 5:00 AM IST on your local machine
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
from src.job_tracker import track_applications, log_execution

def main():
    """
    Main orchestration function
    1. Load configuration
    2. Open Comet AI Assistant
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
    
    try:
        # Step 1: Log execution start
        print("📝 Logging execution start...")
        log_execution('START')
        
        # Step 2: Open Comet browser
        print("\n🌐 Step 1: Opening Comet AI Assistant...")
        browser = open_comet_browser()
        if not browser:
            raise Exception("Failed to open Comet browser")
        print("   ✅ Comet AI Assistant opened successfully")
        time.sleep(3)
        
        # Step 3: Send prompt to Comet
        print("\n📨 Step 2: Sending job search prompt...")
        result = send_prompt_to_comet(browser)
        if not result:
            raise Exception("Failed to send prompt to Comet")
        print("   ✅ Prompt sent successfully")
        time.sleep(5)
        
        # Step 4: Monitor execution
        print("\n⏳ Step 3: Monitoring job application process...")
        print("   Waiting for Comet to process (max 10 minutes)...")
        
        # Track applications from browser
        applications = track_applications(browser)
        
        # Step 5: Report results
        print(f"\n✅ Step 4: Job application complete!")
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
        # Close browser
        try:
            if 'browser' in locals():
                browser.quit()
                print("\n🔚 Browser closed.")
        except:
            pass

if __name__ == "__main__":
    sys.exit(main())
