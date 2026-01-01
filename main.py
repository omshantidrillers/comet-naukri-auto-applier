#!/usr/bin/env python3
import os
import pyperclip
from dotenv import load_dotenv

load_dotenv()

print("\n" + "="*70)
print("Comet Naukri Auto Applier")
print("="*70)
print()

try:
    prompt_file = 'prompts/comet_prompt.txt'
    if not os.path.exists(prompt_file):
        print(f"Error: {prompt_file} not found")
        exit(1)
    
    with open(prompt_file, 'r', encoding='utf-8') as f:
        prompt = f.read().strip()
    
    print(f"Prompt loaded ({len(prompt)} characters)")
    print()
    print("Copying prompt to clipboard...")
    pyperclip.copy(prompt)
    print("Done! Prompt is in your clipboard.")
    print()
    print("Instructions:")
    print("1. Go to Comet Browser (already running)")
    print("2. Click the Assistant button (top right)")
    print("3. Paste the prompt (Ctrl+V)")
    print("4. Press Enter to submit")
    print("5. Apply to 5 jobs in Comet")
    print()
    print("="*70)
    
except Exception as e:
    print(f"Error: {e}")
    exit(1)
