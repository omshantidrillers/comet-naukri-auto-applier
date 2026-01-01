# Local Scheduling Setup

## Overview
This script is designed to run locally on your laptop and execute job applications every morning at 5:00 AM IST.

## Windows Setup (Task Scheduler)

### Step 1: Open Task Scheduler
1. Press `Win + R` to open Run dialog
2. Type `taskschd.msc` and press Enter

### Step 2: Create a New Task
1. Click on "Create Basic Task" in the right panel
2. Name: "Naukri Auto Job Applier"
3. Click "Next"

### Step 3: Set Trigger
1. Choose "Daily"
2. Set time to 5:00 AM
3. Click "Next"

### Step 4: Set Action
1. Select "Start a program"
2. Program/script: python or full path to Python executable
3. Add arguments: path to main.py
4. Start in: path to comet-naukri-auto-applier directory
5. Click "Next"

### Step 5: Finish
1. Check "Open the Properties dialog for this task when I click Finish"
2. Click "Finish"
3. In Properties, go to "General" tab
4. Check "Run with highest privileges" if needed

## macOS Setup (LaunchAgent)

1. Create a plist file in ~/Library/LaunchAgents/
2. Use LaunchAgent to schedule the Python script
3. Set StartCalendarInterval for 5:00 AM

## Linux Setup (Cron)

1. Open terminal
2. Type: crontab -e
3. Add: 0 5 * * * /usr/bin/python3 /path/to/main.py

## Prerequisites
- Python 3.6+ installed
- Comet Browser installed on your laptop
- Dependencies installed: pip install -r requirements.txt

## Testing
1. Run manually first: python main.py
2. Verify script works without errors
3. Check that Comet opens and displays Assistant button
4. Only then configure the scheduler

## Logs
- Add logging to main.py to track execution
- Check system logs for failures
- Monitor Comet Assistant for completed applications
