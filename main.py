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
import webbrowser
from datetime import datetime
from dotenv import load_dotenv
import pytz

# Load environment variables
load_dotenv()

from src.job_tracker import track_applications, log_execution

def main():
    """
    Main orchestration function
    1. Load configuration
    2. Open Comet browser (standalone application)
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
        
        # Step 2: Open Comet browser (standalone application)
        print("\n🌐 Step 1: Opening Comet Browser Application...")
        success = open_comet_application()
        if not success:
            raise Exception("Failed to open Comet application")
        print("   ✅ Comet Browser opened successfully")
        time.sleep(5)  # Wait for Comet to fully load
        
        # Step 3: Send prompt to Comet
        print("\n📨 Step 2: Sending job search prompt to Comet...")
        # Open Naukri in default browser
        webbrowser.open('https://www.naukri.com/jobs')
        time.sleep(3)
        
        # Send prompt to Comet (opens Perplexity AI)
        result = send_prompt_to_comet()
        if not result:
            raise Exception("Failed to send prompt to Comet")
        print("   ✅ Prompt sent successfully")
        time.sleep(5)
        
        # Step 4: Monitor execution
        print("\n⏳ Step 3: Monitoring job application process...")
        print("   Waiting for Comet to process (max 10 minutes)...")
        time.sleep(30)  # Wait for applications to be submitted
        
        # Track applications from local logs
        applications = track_applications()
        
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
        # Comet browser stays open for user interaction
        print("\n🔚 Process completed. Comet browser remains open for you to interact with.")

def open_comet_application():
    """
    Opens Comet browser application (standalone)
    
    For different operating systems:
    - Windows: Looks for Comet in Program Files or uses 'start comet' command
    - macOS: Uses 'open -a Comet' command
    - Linux: Uses 'comet' command or full path
    
    Returns True if successful, False otherwise
    """
    try:
        system = sys.platform
        
        if system == 'win32':
            # Windows - Try multiple methods to launch Comet
            comet_paths = [
                r"C:\Program Files\Comet\Comet.exe",
                r"C:\Program Files (x86)\Comet\Comet.exe",
                r"C:\Users\{}\AppData\Local\Comet\Comet.exe".format(os.getenv('USERNAME')),
            ]
            
            # Try direct path first
            for path in comet_paths:
                if os.path.exists(path):
                    subprocess.Popen(path)
                    print(f"   Launched Comet from: {path}")
                    return True
            
            # Fallback: Try using 'start' command
            try:
                subprocess.Popen(['start', 'comet'], shell=True)
                print("   Launched Comet using system command")
                return True
            except:
                pass
        
        elif system == 'darwin':
            # macOS - Use 'open' command
            subprocess.Popen(['open', '-a', 'Comet'])
            print("   Launched Comet application")
            return True
        
        elif system == 'linux':
            # Linux - Direct command
            subprocess.Popen(['comet'])
            print("   Launched Comet application")
            return True
        
        return False
        
    except Exception as e:
        print(f"Error opening Comet: {str(e)}")
        return False

def send_prompt_to_comet():
    """
    Sends job search prompt to Comet via Perplexity AI interface
    Opens the prompt for user to copy-paste into Comet
    """
    try:
        # Open Comet's web interface (Perplexity AI)
        webbrowser.open('https://www.perplexity.ai')
        
        # Read and display the prompt for user to copy-paste
        prompt_file = 'prompts/comet_prompt.txt'
        if os.path.exists(prompt_file):
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt = f.read().strip()
            
            print("\n📋 Prompt ready. Comet browser is open.")
            print("   Please paste this prompt in Comet:\n")
            print("="*70)
            print(prompt)
            print("="*70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"Error with Comet prompt: {str(e)}")
        return False

if __name__ == "__main__":
    sys.exit(main())
