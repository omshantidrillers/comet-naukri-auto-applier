#!/usr/bin/env python3
import pyperclip
import time
import subprocess
import sys
from pathlib import Path

PROMPT = """You are a job search assistant. Your task is to help me apply for jobs on Naukri.com.

Please follow these instructions carefully:

1. LOGIN & NAVIGATION:
   - Go to https://www.naukri.com
   - Log in with my credentials if needed
   - Navigate to the jobs search page

2. JOB SEARCH CRITERIA:
   - Search for these job roles (any of these):
     * Cloud Engineer
     * Senior Cloud Engineer
     * DevOps Engineer
   - Locations: Pan India, Gurugram, Remote (all acceptable)
   - Experience: 3-6 years
   - Posted within: Last 24 hours only

3. APPLY TO JOBS:
   - Find jobs matching the above criteria
   - Apply to exactly 5 jobs that best match the requirements
   - For each job, verify:
     * Role matches my target positions
     * Location is acceptable
     * Experience requirement matches (3-6 years)
   - Skip jobs that are:
     * From recruitment consultancies/staffing
     * Duplicate applications (already applied)
     * Outside my skill set

4. APPLICATION DETAILS:
   - When applying, use my existing resume
   - If a note/message is required, use:
     "I have 3+ years of experience in cloud infrastructure, automation, CI/CD, and Kubernetes. Looking forward to contributing to your team."
   - Don't modify this message

5. RETURN INFORMATION:
   - Apply to exactly 5 jobs
   - Return a summary of the 5 jobs you applied to
   - Include company name, job title, and location for each
   - Confirm successful completion

My Skills & Experience:
- Cloud Platforms: Azure, AWS basics, VMware
- Automation: Ansible, Terraform, PowerShell
- Kubernetes & Container Orchestration
- Linux & Windows Server Administration
- CI/CD: GitLab pipelines
- Total Experience: 3-4 years in Cloud Infrastructure & DevOps

IMPORTANT: Only apply to 5 jobs. Do not apply to more than 5. Do not apply to jobs that are not in the target roles or locations."""

def main():
    print("\n" + "="*70)
    print("Comet Naukri Auto Applier")
    print("="*70)
    print()
    
    try:
        print("Step 1: Launching Comet Browser...")
        launch_comet_browser()
        
        print("\nStep 2: Opening Naukri.com in default browser...")
        import webbrowser
        webbrowser.open('https://www.naukri.com/jobs')
        
        print("\nStep 3: Preparing prompt for Comet Assistant...")
        print(f"Copying prompt to clipboard ({len(PROMPT)} characters)...")
        pyperclip.copy(PROMPT)
        
        print("\n" + "="*70)
        print("INSTRUCTIONS:")
        print("="*70)
        print()
        print("1. Comet Browser should now be open")
        print("2. Click the 'Assistant' button on top right")
        print("3. The prompt has been copied to your clipboard")
        print("4. Paste the prompt (Ctrl+V) into the Assistant input field")
        print("5. Press Enter to submit")
        print("6. Comet will apply to 5 jobs on Naukri")
        print()
        print("="*70)
        print()
        
        print("Waiting for you to complete the task...")
        print("Press Enter when done applying to 5 jobs in Comet")
        input()
        
        print("\n✓ Task completed!")
        print("="*70 + "\n")
        return 0
        
    except Exception as e:
        print(f"\nError: {e}")
        return 1

def launch_comet_browser():
    """
    Launches Comet Browser application
    """
    system = sys.platform
    
    if system == 'win32':
        # Windows
        comet_paths = [
            r"C:\Program Files\Comet\Comet.exe",
            r"C:\Program Files (x86)\Comet\Comet.exe",
            rf"C:\Users\{Path.home().name}\AppData\Local\Comet\Comet.exe",
        ]
        
        for path in comet_paths:
            if Path(path).exists():
                subprocess.Popen(path)
                print(f"   Launched from: {path}")
                time.sleep(3)
                return
        
        subprocess.Popen(['start', 'comet'], shell=True)
        print("   Launched via system command")
        time.sleep(3)
    
    elif system == 'darwin':
        # macOS
        subprocess.Popen(['open', '-a', 'Comet'])
        print("   Launched Comet application")
        time.sleep(3)
    
    elif system == 'linux':
        # Linux
        subprocess.Popen(['comet'])
        print("   Launched Comet application")
        time.sleep(3)

if __name__ == "__main__":
    sys.exit(main())
