"""
Comet Naukri Auto Applier
Automated job applications on Naukri.com using Comet AI Assistant

Version: 1.0.0
Author: Job Application Automation
License: MIT
"""

__version__ = "1.0.0"
__author__ = "Automation System"
__license__ = "MIT"

from .open_comet import open_comet_browser, close_browser
from .send_prompt import send_prompt_to_comet
from .job_tracker import track_applications, log_application, log_execution

__all__ = [
    'open_comet_browser',
    'close_browser',
    'send_prompt_to_comet',
    'track_applications',
    'log_application',
    'log_execution'
]
