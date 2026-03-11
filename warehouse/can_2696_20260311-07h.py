"""
Campbell's Soup Can #2696
Produced: 2026-03-11 07:12:01
Worker: Qwen: Qwen Plus 0728 (thinking) (qwen/qwen-plus-2025-07-28:thinking)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap
import time
import sys

GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

quote = "Existence is like a bad date – you're never quite sure why you showed up, but now you're stuck paying for it and worrying about the awkward goodbye."
attribution = "- Woody Allen (probably between appointments)"

width = 45
wrapped_quote = textwrap.wrap(quote, width=width)

# Create pulsating box borders
def draw_border(char, width, color):
    sys.stdout.write(color + char * (width + 2) + RESET + '\n')
    time.sleep(0.1)

# Print opening animation with nervous energy
print(BOLD + YELLOW + "\n=== NEUROTIC PHILOSOPHICAL OUTPUT INITIATED ===" + RESET)
time.sleep(0.8)
print(YELLOW + "Running existential diagnostics..." + RESET)
time.sleep(0.5)
print(YELLOW + "Scanning for meaning (0.7% complete)..." + RESET)
time.sleep(1.2)
print(YELLOW + "Warning: Anxiety levels exceeding operational parameters!" + RESET)
time.sleep(1.3)
print(YELLOW + "Generating emergency wisdom...\n" + RESET)
time.sleep(0.7)

# Draw shaky top border
print(GREEN + '╔' + '≋' * width + '╗' + RESET)
time.sleep(0.3)
print(GREEN + '╠' + '≋' * width + '╣' + RESET)

# Print quote with typing anxiety
for line in wrapped_quote:
    print(GREEN + '║' + RESET, end='', flush=True)
    time.sleep(0.2)
    
    for char in line:
        # Random slight hesitation for neurotic effect
        if char in ',.?!' and time.time() % 1 > 0.6:
            time.sleep(0.3)
        elif time.time() % 1 > 0.85:
            time.sleep(0.15)
            
        sys.stdout.write(CYAN + char + RESET)
        sys.stdout.flush()
        time.sleep(0.04 + (0.02 if char != ' ' else 0.005))
    
    # Center the line
    padding = ' ' * ((width - len(line)) // 2)
    sys.stdout.write(' ' * (width - len(line) - len(padding)))
    sys.stdout.write(GREEN + '║' + RESET + '\n')
    time.sleep(0.4)

# Attribution with dramatic pause
print(GREEN + '╠' + '≋' * width + '╣' + RESET)
print(GREEN + '║' + RESET, end='', flush=True)
time.sleep(1.2)

for char in attribution.center(width):
    sys.stdout.write(YELLOW + char + RESET)
    sys.stdout.flush()
    time.sleep(0.06)
print(GREEN + '║' + RESET)

# Closing border with shaky effect
print(GREEN + '╠' + '≋' * width + '╣' + RESET)
time.sleep(0.4)
print(GREEN + '╚' + '≋' * (width-3) + '  ' + '╝' + RESET)

# Final neurotic ASCII flourish
time.sleep(1.5)
print(CYAN + r"""
  (•_•)
  <)  )╯  "...and then I started worrying
   /  \     about whether worrying counts 
   ￣ ￣    as cardiovascular exercise?"
""" + RESET)
time.sleep(0.5)
print(BOLD + YELLOW + "\n[Philosophical processing complete. Please consult your therapist.]" + RESET)