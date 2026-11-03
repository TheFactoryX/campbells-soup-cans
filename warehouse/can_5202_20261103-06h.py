"""
Campbell's Soup Can #5202
Produced: 2026-11-03 06:48:37
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
BRIGHT_BLACK = '\033[90m'
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

def move_cursor(row, col):
    print(f'\033[{row};{col}H', end='')

def typewriter(text, delay=0.03, color=WHITE):
    for char in text:
        print(f"{color}{char}{RESET}", end='', flush=True)
        time.sleep(delay)
    print()

def center_text(text, width=80):
    return text.center(width)

def draw_box(content_lines, width=70, border_color=CYAN, title="", title_color=YELLOW):
    horizontal = "─" * (width - 2)
    top = f"{border_color}┌{horizontal}┐{RESET}"
    bottom = f"{border_color}└{horizontal}┘{RESET}"
    
    lines = [top]
    
    if title:
        title_line = f"{border_color}│{RESET} {title_color}{BOLD}{title.center(width - 4)}{RESET} {border_color}│{RESET}"
        lines.append(title_line)
        lines.append(f"{border_color}├{horizontal}┤{RESET}")
    
    for line in content_lines:
        padding = width - 4 - len(line.replace('\033[0m', '').replace('\033[1m', '').replace('\033[3m', ''))
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{border_color}│{RESET}{' ' * left_pad}{line}{' ' * right_pad}{border_color}│{RESET}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def woody_face():
    return f"""
{CYAN}      ┌─────────┐{RESET}
{CYAN}     │  {WHITE}@   @{CYAN}  │{RESET}   {YELLOW}"I told my psychiatrist{RESET}
{CYAN}     │  {WHITE}  ▼  {CYAN}  │{RESET}    {YELLOW}I have a fear of{RESET}
{CYAN}     │  {WHITE}\\___/{CYAN}  │{RESET}    {YELLOW}commitment. He said,{RESET}
{CYAN}      └─────────┘{RESET}    {YELLOW}'That's not a phobia,{RESET}
{CYAN}       │     │{RESET}        {YELLOW}that's just being{RESET}
{CYAN}      /       \\{RESET}       {YELLOW}my patient.'" {RESET}
{CYAN}     /         \\{RESET}
"""

def animate_thought_bubble():
    thoughts = [
        "Wait... did I leave the stove on?",
        "Is this quote too pretentious?",
        "Should I have ordered the salad?",
        "My therapist would hate this.",
        "Existence is just anxiety with better lighting.",
        "I'm not paranoid. The universe IS watching.",
        "Death is nature's way of saying 'table for one.'",
    ]
    
    for i, thought in enumerate(thoughts):
        clear_screen()
        print(woody_face())
        print()
        
        # Draw thought bubble
        bubble_width = 60
        bubble = draw_box([thought], width=bubble_width, border_color=MAGENTA, title="WOODY'S INNER MONOLOGUE")
        print(center_text(bubble.split('\n')[0]))
        for line in bubble.split('\n')[1:]:
            print(center_text(line))
        
        time.sleep(1.2)
    
    clear_screen()

def main():
    hide_cursor()
    try:
        # Opening animation
        clear_screen()
        
        # Title sequence
        title_lines = [
            f"{BRIGHT_YELLOW}{BOLD}╔══════════════════════════════════════════════════════════════╗{RESET}",
            f"{BRIGHT_YELLOW}{BOLD}║{RESET}  {MAGENTA}✦{RESET} {CYAN}A WOODY ALLEN MOMENT{RESET} {MAGENTA}✦{RESET}                              {BRIGHT_YELLOW}{BOLD}║{RESET}",
            f"{BRIGHT_YELLOW}{BOLD}╚══════════════════════════════════════════════════════════════╝{RESET}",
        ]
        for line in title_lines:
            print(center_text(line))
            time.sleep(0.15)
        
        print()
        time.sleep(0.5)
        
        # Woody face appears
        for line in woody_face().split('\n'):
            print(center_text(line))
            time.sleep(0.1)
        
        time.sleep(1)
        
        # Thought bubble animation
        animate_thought_bubble()
        
        # Final quote reveal
        quote = "I don't believe in an afterlife, but I'm bringing a change of underwear just in case."
        
        # Build up the quote dramatically
        clear_screen()
        print(woody_face())
        print()
        
        # Dramatic pause
        for dot in ["", ".", "..", "...", ""]:
            clear_screen()
            print(woody_face())
            print()
            print(center_text(f"{BRIGHT_CYAN}{dot}{RESET}"))
            time.sleep(0.4)
        
        # Typewriter effect for the quote
        clear_screen()
        print(woody_face())
        print()
        
        quote_box = draw_box(
            [f"{ITALIC}{WHITE}\"{quote}\"{RESET}"],
            width=76,
            border_color=BRIGHT_YELLOW,
            title=f"{BOLD}THE VERDICT{RESET}",
            title_color=BRIGHT_RED
        )
        
        for line in quote_box.split('\n'):
            print(center_text(line))
            time.sleep(0.08)
        
        print()
        print(center_text(f"{DIM}{BRIGHT_BLACK}— Woody Allen, probably, at 3 AM, staring at the ceiling{RESET}"))
        print()
        
        # Final flourish
        decorations = [
            f"{MAGENTA}✦{RESET} {CYAN}✦{RESET} {YELLOW}✦{RESET} {GREEN}✦{RESET} {BLUE}✦{RESET} {MAGENTA}✦{RESET}",
            f"{DIM}Existential dread never looked so well-dressed.{RESET}",
            f"{BRIGHT_BLACK}Press Ctrl+C to accept the absurdity...{RESET}"
        ]
        
        for dec in decorations:
            print(center_text(dec))
            time.sleep(0.3)
        
        # Tiny blinking cursor at end
        for _ in range(6):
            print(f"\r{center_text(f'{BLINK}{BRIGHT_GREEN}▋{RESET}')}", end='', flush=True)
            time.sleep(0.5)
            print(f"\r{center_text(' ')}", end='', flush=True)
            time.sleep(0.5)
        
        print()
        
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        print(f"\n{RESET}")

if __name__ == "__main__":
    main()