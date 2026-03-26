"""
Campbell's Soup Can #2978
Produced: 2026-03-26 17:18:38
Worker: NVIDIA: Nemotron 3 Nano 30B A3B (free) (nvidia/nemotron-3-nano-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

pythonimport sys, time

# ANSI color codesC_RESET = '\033[0m'
C_CYAN  = '\033[36m'
C_GREEN = '\033[32m'

def slow_print(text, delay=0.02):
    """Print text character by character for a typing effect."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

# The Woody Allen‑style philosophical quote
quote = "I’m not afraid of death; I just don’t want to be there when it happens."

# Build a colored ASCII‑art box around the quote
box_top    = f"{C_CYAN}+----------------------------------------+{C_RESET}"
box_mid    = f"{C_CYAN}|                                        |{C_RESET}"
quote_line1= f"{C_GREEN}|   I’m not afraid of death; I just     |{C_RESET}"
quote_line2= f"{C_GREEN}|   don’t want to be there when it     |{C_RESET}"
quote_line3= f"{C_GREEN}|   happens.                              |{C_RESET}"
box_bottom = f"{C_CYAN}+----------------------------------------+{C_RESET}"

# Print each line of the box with a typing animation
for line in (box_top, box_mid, quote_line1, quote_line2, quote_line3, box_bottom):
    slow_print(line)

# Add a tiny pause before the program exits
time.sleep(0.5)