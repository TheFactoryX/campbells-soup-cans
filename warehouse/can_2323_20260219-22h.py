"""
Campbell's Soup Can #2323
Produced: 2026-02-19 22:51:15
Worker: Qwen: Qwen3 VL 235B A22B Thinking (qwen/qwen3-vl-235b-a22b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

# ANSI color codes
BLUE = '\033[94m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Neurotic Woody Allen style quote
quote = (
    "I don't fear death; I'm just terrified that when I die, "
    "the afterlife's HR department will reject my application "
    "for 'insufficient achievement' and make me reapply... "
    "with references from people who actually succeeded at something."
)

# Create a dynamic typing effect with visual flair
def print_witty_box():
    max_width = 55
    lines = []
    current = ""
    
    # Simple text wrapping (no external dependencies)
    for word in quote.split():
        if len(current) + len(word) + 1 <= max_width - 4:
            current += (" " + word) if current else word
        else:
            lines.append(current)
            current = word
    if current: 
        lines.append(current)
    
    # Top border with animated pulse
    border = BLUE + '+' + '-' * max_width + '+'
    for _ in range(2):
        sys.stdout.write(BLUE + border + '\n')
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write('\033[A' + ' ' * (max_width + 2) + '\n')
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(BLUE + border + '\n')
    sys.stdout.flush()
    
    # Print content with typing effect and neurotic cursor
    for line in lines:
        # Left border
        sys.stdout.write(BLUE + '| ')
        sys.stdout.flush()
        
        # Typing animation with random "backspace" errors (neurotic touch)
        text = line
        i = 0
        while i < len(text):
            sys.stdout.write(YELLOW + text[i])
            sys.stdout.flush()
            time.sleep(0.02)
            
            # 15% chance of "neurotic backspace"
            if i > 5 and not text[i].isspace() and text[i-1].isspace() and i < len(text)-10:
                if i > 0 and text[i] != ' ':
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
                    time.sleep(0.05)
                    i -= 1  # Re-type the character
            i += 1
        
        # Right border
        sys.stdout.write(BLUE + ' |' + '\n')
        sys.stdout.flush()
    
    # Bottom border with "sigh" animation
    sys.stdout.write(BLUE + '|' + '-' * max_width + '|\n')
    sys.stdout.flush()
    
    # Neurotic footer
    footer = "— *Sighs, adjusts imaginary glasses, mutters about existential paperwork*"
    sys.stdout.write(BLUE + '| ')
    for i, char in enumerate(footer):
        sys.stdout.write(GREEN if i > len(footer)-30 else YELLOW)
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    sys.stdout.write(BLUE + ' |\n')
    sys.stdout.flush()
    
    # Final border and reset
    sys.stdout.write(BLUE + '+' + '-' * max_width + '+\n' + RESET)
    sys.stdout.flush()

# Add dramatic pause and title
print(f"{BOLD}{GREEN}{'='*25} WOODY ALLEN'S NEUROTIC WISDOM {'='*25}{RESET}")
time.sleep(0.8)
print_witty_box()
print(f"{BOLD}{GREEN}{'='*65}{RESET}")