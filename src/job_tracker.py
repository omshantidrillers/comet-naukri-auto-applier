"""
Job application tracking module
Logs all successfully applied jobs to a local file
"""

import os
from datetime import datetime
import pytz
from selenium.webdriver.common.by import By
import time

def track_applications(driver):
    """
    Monitors Naukri.com for applied jobs
    Extracts job details and logs them
    Returns list of applied job details
    """
    applications = []
    try:
        # Switch to Naukri tab if needed
        driver.get('https://www.naukri.com/my-jobs/applications')
        time.sleep(3)
        
        # Find applied jobs (simplified - adapt selectors to actual Naukri HTML)
        job_elements = driver.find_elements(By.CLASS_NAME, 'job-item')
        
        for i, job_elem in enumerate(job_elements[:5]):
            try:
                company = job_elem.find_element(By.CLASS_NAME, 'company-name').text
                title = job_elem.find_element(By.CLASS_NAME, 'job-title').text
                location = job_elem.find_element(By.CLASS_NAME, 'job-location').text
                
                app_data = {
                    'company': company,
                    'job_title': title,
                    'location': location,
                    'timestamp': datetime.now(pytz.timezone('Asia/Kolkata')).isoformat()
                }
                applications.append(app_data)
                log_application(app_data)
                
            except Exception as e:
                continue
        
        return applications
        
    except Exception as e:
        print(f"Error tracking applications: {str(e)}")
        return applications

def log_application(app_data):
    """
    Logs a single application to file
    """
    log_file = os.getenv('LOG_FILE_PATH', 'logs/naukri_applications.log')
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"{timestamp} | {app_data.get('company', 'N/A')} | {app_data.get('job_title', 'N/A')} | {app_data.get('location', 'N/A')}\n"
    
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    except Exception as e:
        print(f"Error logging application: {str(e)}")

def log_execution(status, count=0, error=None):
    """
    Logs execution summary
    """
    log_file = os.getenv('LOG_FILE_PATH', 'logs/naukri_applications.log')
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    timestamp = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    
    if status == 'START':
        entry = f"\n{'='*70}\n{timestamp} - Execution Started\n{'='*70}\n"
    elif status == 'SUCCESS':
        entry = f"{timestamp} - Execution Completed Successfully | Applications: {count}\n"
    elif status == 'ERROR':
        entry = f"{timestamp} - Execution Error: {error}\n"
    else:
        return
    
    try:
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(entry)
    except Exception as e:
        print(f"Error logging execution: {str(e)}")
