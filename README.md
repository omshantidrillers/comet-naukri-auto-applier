# Comet Naukri Auto Applier

Automated daily job applications on **Naukri.com** using **Comet AI Assistant**. Runs locally on your laptop at **5:00 AM IST every morning**.

## 🎯 Overview

This project automates the job application process on Naukri by:
- Launching Comet AI Assistant on your local machine
- Injecting a pre-configured prompt to search for jobs
- Applying to exactly 5 relevant jobs matching your profile
- Tracking all applications locally

**System Reality**: Code is hosted on GitHub, but execution happens on your personal laptop via local scheduling.

---

## ✨ Features

✅ **Local Execution** - Runs on your personal laptop (not cloud-based)  
✅ **Scheduled Automation** - Runs daily at 5:00 AM IST via cron/Task Scheduler  
✅ **Comet Integration** - Launches Comet browser assistant locally  
✅ **Smart Job Filtering** - Searches for Cloud Engineer, Senior Cloud Engineer, DevOps Engineer  
✅ **Quality Control** - Filters for 3-6 years experience, posted within 24 hours  
✅ **Duplicate Prevention** - Avoids applying to same jobs twice  
✅ **Application Tracking** - Logs all applications locally with timestamps  
✅ **Easy Setup** - Simple configuration with environment variables  
✅ **Zero Manual Intervention** - Fully automated once scheduled  

---

## 📋 Prerequisites

- **Python 3.8+** installed on your laptop
- **Git** installed on your laptop
- **Comet Chrome Extension** installed and logged in
- **Chrome/Chromium browser** installed
- **Internet connection** available at 5:00 AM IST
- **Laptop must be ON** at scheduled time

---

## 📁 Project Structure

```
comet-naukri-auto-applier/
│
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── .env.example                       # Environment variables template
├── .gitignore                         # Python gitignore
│
├── prompts/
│   └── comet_prompt.txt               # Prompt injected into Comet
│
├── src/
│   ├── __init__.py
│   ├── open_comet.py                  # Launch Comet locally
│   ├── send_prompt.py                 # Send prompt to Comet
│   └── job_tracker.py                 # Track applications
│
├── scheduler/
│   ├── local_schedule.md              # Setup instructions
│   ├── windows_task_scheduler.md      # Windows setup guide
│   └── linux_macos_cron.md            # Linux/macOS setup guide
│
└── main.py                            # Entry point
```

---

## 🚀 Quick Start

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/comet-naukri-auto-applier.git
cd comet-naukri-auto-applier
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Configure Environment

```bash
cp .env.example .env
# Edit .env with your details (optional)
```

### Step 4: Test Manually (Optional)

```bash
python main.py
```

This will:
1. Launch Comet AI Assistant
2. Open Naukri.com
3. Inject the job search prompt
4. Monitor the process

### Step 5: Setup Automated Scheduling

**For Windows:**
- Follow the guide in `scheduler/windows_task_scheduler.md`
- Creates a Task Scheduler task for 5:00 AM daily

**For Linux/macOS:**
- Follow the guide in `scheduler/linux_macos_cron.md`
- Creates a cron job for 5:00 AM IST daily

---

## ⚙️ Configuration

### Environment Variables (.env)

```bash
# Naukri Profile
NAUKRI_EMAIL=your-email@example.com
NAUKRI_SEARCH_KEYWORDS=Cloud Engineer,Senior Cloud Engineer,DevOps Engineer

# Job Filters
EXPERIENCE_RANGE=3-6
LOCATION=Pan India,Gurugram,Remote
POST_AGE_HOURS=24

# Application Settings
APPLY_COUNT=5
LOG_FILE_PATH=./logs/naukri_applications.log

# Timezone
TIMEZONE=Asia/Kolkata
```

---

## 📝 How It Works

### Execution Flow

1. **Scheduler Triggers** (5:00 AM IST)
   - Windows Task Scheduler or Linux cron executes `python main.py`

2. **Open Comet** (`src/open_comet.py`)
   - Launches Chrome with Comet extension
   - Navigates to Comet dashboard
   - Verifies login status

3. **Send Prompt** (`src/send_prompt.py`)
   - Reads `prompts/comet_prompt.txt`
   - Injects prompt into Comet's input field
   - Submits the prompt

4. **Monitor Execution**
   - Waits for Comet to process
   - Monitors Naukri.com activity
   - Collects job details from applied positions

5. **Track Applications** (`src/job_tracker.py`)
   - Logs company name, job title, location
   - Adds timestamp
   - Stores in `logs/naukri_applications.log`

6. **Stop After 5 Applications**
   - Terminates Comet once 5 jobs applied
   - Returns execution summary

### Comet Prompt

The prompt stored in `prompts/comet_prompt.txt` instructs Comet to:

```
Log in to Naukri.com
Search for: Cloud Engineer OR Senior Cloud Engineer OR DevOps Engineer
Filter by:
  - Experience: 3-6 years
  - Posted in last 24 hours
  - Location: Pan India, Gurugram, Remote
Apply to exactly 5 jobs that match the profile
Avoid duplicate applications
Return applied job details
```

---

## 🪟 Windows Setup

See `scheduler/windows_task_scheduler.md` for detailed instructions.

**Quick Steps:**

1. Open Task Scheduler (Win + R → `taskschd.msc`)
2. Create Basic Task → "Naukri Auto Applier"
3. Set Trigger: Daily at 5:00 AM
4. Set Action: Start program `python.exe`
5. Arguments: `C:\path\to\main.py`
6. Enable: "Run whether user is logged in or not"

---

## 🐧 Linux / macOS Setup

See `scheduler/linux_macos_cron.md` for detailed instructions.

**Quick Steps:**

```bash
# Edit crontab
crontab -e

# Add this line (5:00 AM IST = 11:30 PM UTC previous day)
30 23 * * * cd /path/to/comet-naukri-auto-applier && python main.py

# Save and exit (Ctrl+X, then Y)
```

---

## 📊 Application Tracking

All applications are logged in `logs/naukri_applications.log`:

```
2025-01-02 05:00:15 | TechCorp | Senior Cloud Engineer | Gurugram
2025-01-02 05:03:42 | CloudSys | DevOps Engineer | Remote
2025-01-02 05:06:19 | InfraCo | Cloud Engineer | Pan India
2025-01-02 05:09:53 | DevOpsPlus | Senior Cloud Engineer | Gurugram
2025-01-02 05:12:30 | SkyCorp | Cloud Engineer | Remote
```

---

## 🔒 Security Precautions

### ✅ DO:
- ✅ Use `.env` file for sensitive data (not committed to GitHub)
- ✅ Review the Comet prompt before first run
- ✅ Keep Comet extension updated
- ✅ Monitor application logs regularly
- ✅ Test manually before scheduling

### ❌ DON'T:
- ❌ Commit `.env` file to GitHub
- ❌ Share your laptop credentials
- ❌ Modify Naukri website directly
- ❌ Apply to jobs you're not qualified for
- ❌ Disable laptop security features

---

## 🛠️ Troubleshooting

### Comet Not Launching
```bash
# Ensure Comet extension is installed
# Try launching Chrome manually first
python src/open_comet.py
```

### Prompt Not Being Injected
```bash
# Check Comet's active tab
# Verify prompt file exists and is readable
cat prompts/comet_prompt.txt
```

### Task Scheduler Not Running (Windows)
```bash
# Check event logs
# Verify Python path is correct
python --version  # Get the path
```

### Cron Not Running (Linux/macOS)
```bash
# Check cron logs
sudo log stream --predicate 'eventMessage contains[cd] "cron"'

# Test cron manually
*/1 * * * * /path/to/test.sh
```

### Laptop Sleeping at 5:00 AM
```bash
# Windows: Settings → System → Power & Sleep → Never
# macOS: System Preferences → Energy Saver → Never
# Linux: Check power management settings
```

---

## 📋 Application Requirements

Your profile must match:

- **Roles**: Cloud Engineer, Senior Cloud Engineer, DevOps Engineer
- **Experience**: 3-6 years
- **Skills**: Azure, AWS, Kubernetes, Terraform, Ansible, CI/CD
- **Location**: Pan India, Gurugram, Remote
- **Availability**: Full-time

---

## 📚 File Descriptions

### `main.py`
Entry point. Orchestrates the entire process.

### `src/open_comet.py`
Launches Comet AI Assistant locally using Chrome.

### `src/send_prompt.py`
Sends the job search prompt to Comet's input.

### `src/job_tracker.py`
Tracks and logs all successful applications.

### `prompts/comet_prompt.txt`
The instruction prompt sent to Comet.

### `scheduler/local_schedule.md`
General scheduling concepts.

### `scheduler/windows_task_scheduler.md`
Detailed Windows setup guide.

### `scheduler/linux_macos_cron.md`
Detailed Linux/macOS setup guide.

---

## ⚡ Important Notes

1. **Laptop Must Be ON**: The scheduled time won't help if your laptop is sleeping or turned off.
2. **Internet Required**: Ensure internet is available at 5:00 AM IST.
3. **Comet Must Be Logged In**: Keep your Comet session active; logout resets authentication.
4. **No GitHub-Based Runners**: Execution is local only; no cloud/CI infrastructure.
5. **Manual Override**: You can run `python main.py` anytime to apply immediately.
6. **Testing**: Always test manually before scheduling for production use.

---

## 🤝 Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review scheduler setup guides
3. Test `python main.py` manually
4. Check `logs/naukri_applications.log` for details

---

## 📄 License

MIT License - See LICENSE file for details.

---

## 🎉 Ready?

1. Clone the repo
2. Install dependencies
3. Configure environment
4. Test with `python main.py`
5. Schedule for 5:00 AM IST
6. Let automation run daily!

Happy job hunting! 🚀
