"""
Campbell's Soup Can #4828
Produced: 2026-08-25 07:58:05
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

# ANSI color codes
RESET = '\033[0m'
BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK = '\033[5m'

# Colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
GRAY = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=WHITE, delay=0.03, new_line=True):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    if new_line:
        print()

def center_text(text, width=70):
    return text.center(width)

def draw_box(content_lines, width=70, border_color=CYAN, title=""):
    horizontal = "─" * (width - 2)
    top = f"{border_color}┌{horizontal}┐{RESET}"
    bottom = f"{border_color}└{horizontal}┘{RESET}"
    
    lines = [top]
    if title:
        title_line = f"{border_color}│{RESET} {BOLD}{YELLOW}{title.center(width - 4)}{RESET} {border_color}│{RESET}"
        lines.append(title_line)
        lines.append(f"{border_color}├{horizontal}┤{RESET}")
    
    for line in content_lines:
        padded = line.ljust(width - 4)
        lines.append(f"{border_color}│{RESET} {padded} {border_color}│{RESET}")
    
    lines.append(bottom)
    return "\n".join(lines)

woody_ascii = f"""
{GRAY}        ╭─────────────╮
       │  {WHITE}@   @{GRAY}   │
       │  {YELLOW}  ▼  {GRAY}   │
       │  {MAGENTA}╰───╯{GRAY}   │
       │ {CYAN}/  |  \\{GRAY}  │
       ╰─────────────╯{RESET}
"""

def main():
    clear_screen()
    hide_cursor()
    
    # Woody Allen style quote - original
    quote = "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia."
    
    # Alternative quotes (pick one randomly for variety)
    quotes = [
        "I took a speed-reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "My therapist says I have a preoccupation with mortality. I told her, 'Doc, at my age, it's not a preoccupation—it's a schedule.'",
        "I don't believe in an afterlife, although I am bringing a change of underwear. Just in case.",
        "The universe is indifferent to my existence. Which is fine, because I'm indifferent to my existence too. We have an understanding.",
        "I'm not a hypochondriac, I'm an alarmist. There's a difference. Hypochondriacs think they're sick. I KNOW I'm sick. I just don't know what it is yet.",
        "Death is nature's way of telling you to slow down. My doctor says the same thing, but he charges $400 an hour.",
        "I tried to be an organ donor, but they said my anxiety isn't a vital organ. I argued it keeps me alive. They didn't buy it.",
        "Life is a sexually transmitted terminal disease. My mother told me that. Right before she made me finish my vegetables."
    ]
    
    selected_quote = random.choice(quotes)
    
    # Animation: ASCII art fade in
    for i in range(3):
        clear_screen()
        opacity_colors = [GRAY, CYAN, BRIGHT_CYAN]
        print(f"\n\n{opacity_colors[i % 3]}{woody_ascii}{RESET}")
        time.sleep(0.3)
    
    clear_screen()
    print(f"\n\n{woody_ascii}")
    time.sleep(0.5)
    
    # Title animation
    title = "WOODY ALLEN WISDOM"
    for i in range(len(title) + 1):
        clear_screen()
        print(f"\n\n{woody_ascii}")
        print(f"\n{BOLD}{CYAN}{center_text(title[:i])}{RESET}")
        time.sleep(0.05)
    
    time.sleep(0.5)
    
    # Draw the quote box
    quote_lines = []
    words = selected_quote.split()
    current_line = ""
    max_width = 60
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += (" " + word) if current_line else word
        else:
            quote_lines.append(current_line)
            current_line = word
    if current_line:
        quote_lines.append(current_line)
    
    # Typewriter effect inside box
    clear_screen()
    print(f"\n\n{woody_ascii}\n")
    print(f"{BOLD}{CYAN}{center_text(title)}{RESET}\n")
    
    # Print top of box
    width = 70
    horizontal = "─" * (width - 2)
    print(f"{CYAN}┌{horizontal}┐{RESET}")
    print(f"{CYAN}│{RESET} {BOLD}{YELLOW}{'THE QUOTE'.center(width - 4)}{RESET} {CYAN}│{RESET}")
    print(f"{CYAN}├{horizontal}┤{RESET}")
    
    # Type each line
    for line in quote_lines:
        print(f"{CYAN}│{RESET} ", end='', flush=True)
        typewriter(line, color=BRIGHT_WHITE, delay=0.02, new_line=False)
        print(f" {CYAN}│{RESET}")
        time.sleep(0.15)
    
    print(f"{CYAN}└{horizontal}┘{RESET}")
    
    time.sleep(0.8)
    
    # Add a neurotic post-script
    post_scripts = [
        f"\n{ITALIC}{GRAY}...said while checking his pulse for the 47th time today.{RESET}",
        f"\n{ITALIC}{GRAY}...muttered to a psychiatrist who fell asleep halfway through.{RESET}",
        f"\n{ITALIC}{GRAY}...whispered to an empty room, because even his shadow left for a smoke break.{RESET}",
        f"\n{ITALIC}{GRAY}...written on a prescription pad for Xanax, in lieu of a signature.{RESET}"
    ]
    
    post = random.choice(post_scripts)
    typewriter(post, color=GRAY, delay=0.02)
    
    # Final flourish
    time.sleep(0.5)
    print(f"\n{DIM}{CYAN}{'─' * 70}{RESET}")
    typewriter(f"{DIM}{ITALIC}— A neurotic production for the existentially exhausted —{RESET}", color=DIM, delay=0.02)
    print(f"{DIM}{CYAN}{'─' * 70}{RESET}\n")
    
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{YELLOW}Interrupted. Even my code has commitment issues.{RESET}\n")
        sys.exit(0)