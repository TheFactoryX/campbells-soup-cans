"""
Campbell's Soup Can #5264
Produced: 2026-11-21 09:56:36
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
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
ORANGE = '\033[38;5;208m'
PINK = '\033[38;5;213m'
LAVENDER = '\033[38;5;183m'
GOLD = '\033[38;5;220m'

# Backgrounds
BG_BLACK = '\033[40m'
BG_DARK = '\033[48;5;234m'
BG_BLUE = '\033[48;5;17m'
BG_PURPLE = '\033[48;5;54m'

CLEAR = '\033[2J\033[H'
CURSOR_HIDE = '\033[?25l'
CURSOR_SHOW = '\033[?25h'

WOODY_QUOTE = (
    "I took a speed-reading course and read \n"
    "'War and Peace' in twenty minutes. \n"
    "It involves Russia."
)

WOODY_LINES = [
    "I took a speed-reading course",
    "and read 'War and Peace' in twenty minutes.",
    "It involves Russia."
]

ASCII_WOODY = r"""
      ╭─────────────────────────────────────╮
      │  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   │
      │  █  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  █   │
      │  █  █     █  █     █  █     █  █   │
      │  █  █  O  █  █  O  █  █  O  █  █   │
      │  █  █     █  █     █  █     █  █   │
      │  █  ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  █   │
      │  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █   │
      │  █  █  WOODY  ALLEN  MODE  █  █   │
      │  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █   │
      │  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   │
      ╰─────────────────────────────────────╯
"""

ASCII_GLASSES = r"""
     ╭─────────────────────────╮
     │      ▄▄         ▄▄      │
     │    ▄████▄     ▄████▄    │
     │   ██▀▀████   ██▀▀████   │
     │   ██    ██   ██    ██   │
     │   ▀██▄▄██▀   ▀██▄▄██▀   │
     │      ▀▀         ▀▀      │
     ╰─────────────────────────╯
"""

NEUROTIC_THOUGHTS = [
    "Wait, is that a tumor? No, just a headache.",
    "Did I leave the stove on? The iron? My will to live?",
    "Everyone's judging me. Even the cat.",
    "What if I'm just a brain in a jar?",
    "My therapist says I have a preoccupation with death. \n       He's right. I'm preoccupied with not dying.",
    "I'm not a hypochondriac. I'm an alarmist. \n       There's a difference. Ask my doctor. \n       Actually, don't. He's part of the conspiracy.",
    "Anxiety is just my body's way of \n       preparing for disasters that won't happen.",
    "I have two moods: \n       'Something's wrong' and 'Everything's wrong.'",
]

def typewriter(text, color=WHITE, delay=0.02, end='\n'):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def typewriter_line(line, color=WHITE, delay=0.03):
    for char in line:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')
    sys.stdout.flush()

def glitch_text(text, color=RED, iterations=3):
    chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        sys.stdout.write(f'\r{color}{glitched}{RESET}')
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f'\r{color}{text}{RESET}\n')
    sys.stdout.flush()

def pulse_color(text, colors, cycles=3):
    for _ in range(cycles):
        for c in colors:
            sys.stdout.write(f'\r{c}{BOLD}{text}{RESET}')
            sys.stdout.flush()
            time.sleep(0.15)
    sys.stdout.write(f'\n')

def draw_box(lines, border_color=CYAN, title="", title_color=YELLOW):
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    
    top = f"{border_color}╭{'─' * (width - 2)}╮{RESET}"
    bottom = f"{border_color}╰{'─' * (width - 2)}╯{RESET}"
    
    print(top)
    if title:
        padding = (width - 2 - len(title)) // 2
        title_line = f"{border_color}│{RESET}{' ' * padding}{title_color}{BOLD}{title}{RESET}{' ' * (width - 2 - padding - len(title))}{border_color}│{RESET}"
        print(title_line)
        print(f"{border_color}├{'─' * (width - 2)}┤{RESET}")
    
    for line in lines:
        padding = width - 2 - len(line)
        print(f"{border_color}│{RESET} {line}{' ' * padding} {border_color}│{RESET}")
    
    print(bottom)

def animate_entrance():
    print(CLEAR + CURSOR_HIDE)
    
    # ASCII art entrance
    for line in ASCII_WOODY.split('\n'):
        print(f"{LAVENDER}{line}{RESET}")
        time.sleep(0.08)
    
    time.sleep(0.5)
    
    # Glasses appear
    print(f"\n{CYAN}Initializing neurotic subsystem...{RESET}")
    time.sleep(0.3)
    
    for line in ASCII_GLASSES.split('\n'):
        print(f"{MAGENTA}{line}{RESET}")
        time.sleep(0.06)
    
    time.sleep(0.5)
    print(CLEAR)

def show_neurotic_interlude():
    print(f"\n{DIM}{ITALIC}[Internal monologue...]{RESET}\n")
    time.sleep(0.5)
    
    thought = random.choice(NEUROTIC_THOUGHTS)
    for line in thought.split('\n'):
        typewriter(f"  {YELLOW}⚡{RESET} {line}", color=WHITE, delay=0.015)
        time.sleep(0.1)
    
    time.sleep(0.8)
    print(CLEAR)

def main():
    try:
        animate_entrance()
        
        # Show the Woody title card
        print(f"{BG_DARK}{' ' * 60}{RESET}")
        print(f"{BG_DARK}{PINK}{BOLD}{'WOODY ALLEN WISDOM GENERATOR v1.0':^60}{RESET}")
        print(f"{BG_DARK}{' ' * 60}{RESET}")
        print()
        
        # Neurotic interlude
        show_neurotic_interlude()
        
        # The quote reveal
        print(f"{CYAN}{'=' * 55}{RESET}")
        print(f"{GOLD}{BOLD}  \"{RESET}")
        time.sleep(0.3)
        
        # Type each line with dramatic timing
        colors_per_line = [WHITE, YELLOW, MAGENTA]
        for i, line in enumerate(WOODY_LINES):
            typewriter_line(f"  {line}", color=colors_per_line[i], delay=0.04)
            time.sleep(0.4)
        
        print(f"{GOLD}{BOLD}  \"{RESET}")
        print(f"{CYAN}{'=' * 55}{RESET}")
        
        time.sleep(0.5)
        
        # Philosophical commentary box
        commentary = [
            "Analysis: The joke works on three levels.",
            "1. Speed reading War & Peace is absurd.",
            "2. 'It involves Russia' - the ultimate reduction.",
            "3. Tolstoy would hate this. So would my analyst.",
            "",
            "Conclusion: Life is meaningless. \n         But at least we have literature. \n         And anxiety. Mostly anxiety."
        ]
        
        print()
        draw_box(commentary, border_color=LAVENDER, title="EXISTENTIAL FOOTNOTES", title_color=PINK)
        
        time.sleep(1)
        
        # Final neurotic sign-off
        print(f"\n{DIM}{ITALIC}Now if you'll excuse me, I need to check \nif my left eyebrow is higher than my right...{RESET}\n")
        
        # Pulsing final message
        pulse_color("  *existential dread continues in background*", [RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, MAGENTA], cycles=2)
        
        print(f"\n{CYAN}╭{'─' * 53}╮{RESET}")
        print(f"{CYAN}│{RESET} {WHITE}Thank you for your attention. I'd stay, but{RESET} {CYAN}│{RESET}")
        print(f"{CYAN}│{RESET} {WHITE}my separation anxiety is kicking in.        {RESET} {CYAN}│{RESET}")
        print(f"{CYAN}╰{'─' * 53}╯{RESET}\n")
        
    except KeyboardInterrupt:
        print(f"\n{RED}Interrupted. Just like my therapy sessions.{RESET}\n")
    finally:
        print(CURSOR_SHOW)

if __name__ == "__main__":
    main()