# Configuration file for Comet Naukri Auto Applier
# Update these values based on your system and preferences

# Path to Comet Browser executable
COMET_PATH = r"C:\Users\vivek\AppData\Local\Perplexity\Comet\Application\comet.exe"

# Job application prompt
PROMPT = """
Apply to exactly 5 Cloud/DevOps jobs on Naukri.
Roles: Cloud Engineer, Senior Cloud Engineer, DevOps Engineer
Experience: 3–6 years
Posted in last 24 hours
Avoid duplicate applications.
"""

# ===== TIMING CONFIGURATION (in seconds) =====
# Time to wait for Comet to fully launch
COMET_LAUNCH_WAIT = 12

# Time to wait for Comet window to focus
WINDOW_FOCUS_WAIT = 2

# Time to wait after clicking Assistant button
CLICK_WAIT = 2

# Interval between typing characters (in seconds)
TYPING_INTERVAL = 0.02

# ===== MOUSE POSITION CONFIGURATION =====
# IMPORTANT: You must calibrate these coordinates!
# To find the coordinates of the Assistant button:
# 1. Run: python -c "import pyautogui; pyautogui.displayMousePosition()"
# 2. Hover your mouse over the Assistant button in Comet
# 3. Note the x, y coordinates displayed
# 4. Update ASSISTANT_BUTTON_X and ASSISTANT_BUTTON_Y below

ASSISTANT_BUTTON_X = 1820  # ⚠️ UPDATE THIS with your screen coordinates
ASSISTANT_BUTTON_Y = 60    # ⚠️ UPDATE THIS with your screen coordinates
