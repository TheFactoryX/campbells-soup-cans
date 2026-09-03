"""
Campbell's Soup Can #4891
Produced: 2026-09-03 05:48:48
Worker: NVIDIA: Nemotron 3 Ultra (free) (nvidia/nemotron-3-ultra-550b-a55b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Quote Generator - Neurotic Wisdom Edition
A single-file Python program that delivers existential dread with style.
"""

import sys
import time
import random

# ─── ANSI Color Palette ──────────────────────────────────────────────
class C:
    RST = '\033[0m'
    BLD = '\033[1m'
    DIM = '\033[2m'
    ITL = '\033[3m'
    UL  = '\033[4m'
    BLK = '\033[30m'
    RED = '\033[31m'
    GRN = '\033[32m'
    YEL = '\033[33m'
    BLU = '\033[34m'
    MAG = '\033[35m'
    CYN = '\033[36m'
    WHT = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ─── Woody's Neurotic Quotes ─────────────────────────────────────────
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes. "
    "It involves Russia.",

    "My therapist says I have a preoccupation with death. "
    "I told him, 'Doc, at my age, it's not a preoccupation—it's a schedule.'",

    "I don't believe in an afterlife, but I'm bringing a change of underwear "
    "just in case. And a snack. You never know how long the line is.",

    "The universe is indifferent to our suffering. "
    "Which is fine, because I'm indifferent to the universe's opinion of my outfit.",

    "I'm not afraid of dying. I just don't want to be conscious for the paperwork.",

    "Life is a sexually transmitted terminal disease. "
    "The prognosis is poor, but the bedside manner could use work.",

    "I asked God for a sign. He sent me a bill for $4.95. "
    "Turns out, divine intervention has a processing fee.",

    "My analyst says I have a narcissistic personality disorder. "
    "I told him, 'That's impossible—I'm the most humble person I know.'",

    "Death is nature's way of telling you to slow down. "
    "My cholesterol is nature's way of telling you to stop eating pastrami.",

    "I have a metaphysical dilemma: if a tree falls in a forest and no one "
    "hears it, does it make a sound? More importantly, who's cleaning it up?",

    "Eternal nothingness is fine if you're dressed for it. "
    "I, however, will be wearing mismatched socks.",

    "The meaning of life? I checked the back of the cereal box. "
    "It said 'Contains 100% daily value of anxiety.' Close enough."
]

# ─── ASCII Art: Woody's Glasses ──────────────────────────────────────
GLASSES = r"""
       .--.       .--.
      /    \     /    \
     |  __  |   |  __  |
     | |  | |   | |  | |
     | |__| |   | |__| |
      \____/     \____/
"""

GLASSES_SMALL = r"  .--.   .--.  "

# ─── Animation Helpers ───────────────────────────────────────────────
def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.02, color=C.WHT, end='\n'):
    """Print text with a typewriter effect."""
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def glitch_text(text, iterations=3, delay=0.05):
    """Glitch effect for neurotic emphasis."""
    chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for _ in range(iterations):
        glitched = ''.join(
            random.choice(chars) if random.random() < 0.1 else c
            for c in text
        )
        print(f'\r{C.RED}{glitched}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print(f'\r{C.YEL}{text}{C.RST}', end='', flush=True)
    time.sleep(0.3)

def pulse_color(text, colors, cycles=2, delay=0.15):
    """Pulse through colors."""
    for _ in range(cycles):
        for color in colors:
            print(f'\r{color}{text}{C.RST}', end='', flush=True)
            time.sleep(delay)

# ─── Visual Components ───────────────────────────────────────────────
def draw_box(content_lines, width=70, border_color=C.CYN, title=None):
    """Draw a fancy box around content."""
    inner_width = width - 4
    top = f'{border_color}╔{"═" * (width - 2)}╗{C.RST}'
    bot = f'{border_color}╚{"═" * (width - 2)}╝{C.RST}'
    
    lines = [top]
    
    if title:
        title_line = f' {title} '
        pad = (inner_width - len(title_line)) // 2
        lines.append(f'{border_color}║{C.RST}{" " * pad}{C.BLD}{C.YEL}{title_line}{C.RST}{" " * (inner_width - pad - len(title_line))}{border_color}║{C.RST}')
        lines.append(f'{border_color}╠{"═" * (width - 2)}╣{C.RST}')
    
    for line in content_lines:
        visible_len = len(line)
        # Strip ANSI for length calculation
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = inner_width - len(clean)
        lines.append(f'{border_color}║{C.RST} {line}{" " * padding}{border_color}║{C.RST}')
    
    lines.append(bot)
    return '\n'.join(lines)

def spinning_loader(message, duration=1.5):
    """Show a spinning loader with neurotic messages."""
    spinner = '⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏'
    neurotic_messages = [
        "Consulting my analyst...",
        "Checking if the universe noticed me...",
        "Replaying every awkward moment since 1987...",
        "Calculating probability of existential dread...",
        "Adjusting glasses nervously...",
        "Wondering if I left the stove on in a past life...",
    ]
    start = time.time()
    i = 0
    msg_idx = 0
    while time.time() - start < duration:
        spin = spinner[i % len(spinner)]
        msg = neurotic_messages[msg_idx % len(neurotic_messages)]
        print(f'\r{C.MAG}{spin} {C.ITL}{msg}{C.RST}', end='', flush=True)
        time.sleep(0.08)
        i += 1
        if i % 20 == 0:
            msg_idx += 1
    print('\r' + ' ' * 60 + '\r', end='', flush=True)

# ─── Main Sequence ───────────────────────────────────────────────────
def main():
    # Setup
    hide_cursor()
    clear_screen()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # ─── Opening: Glasses appear ─────────────────────────────────────
    print(f'{C.CYN}{C.BLD}')
    for line in GLASSES.strip().split('\n'):
        print(f'        {line}')
        time.sleep(0.08)
    print(f'{C.RST}')
    
    time.sleep(0.3)
    
    # ─── Neurotic loader ─────────────────────────────────────────────
    spinning_loader("Initializing neurotic episode...", 1.2)
    
    # ─── Quote reveal with typewriter ────────────────────────────────
    print()
    print(f'{C.DIM}────────────────────────────────────────────────────────────{C.RST}')
    print()
    
    # Split quote into sentences for dramatic effect
    sentences = quote.split('. ')
    for i, sent in enumerate(sentences):
        if i > 0:
            sent = '. ' + sent
        if i == len(sentences) - 1 and not sent.endswith('.'):
            sent += '.'
        
        # Choose color based on sentence
        colors = [C.YEL, C.CYN, C.MAG, C.GRN, C.WHT]
        color = colors[i % len(colors)]
        
        typewriter(sent, delay=0.015, color=color, end='')
        time.sleep(0.4)  # Pause between sentences
    
    print()
    print()
    print(f'{C.DIM}────────────────────────────────────────────────────────────{C.RST}')
    print()
    
    # ─── Woody's signature ───────────────────────────────────────────
    sig_lines = [
        f'{C.ITL}— Woody Allen (probably, or maybe just my analyst){C.RST}',
        f'{C.DIM}   "I told my psychiatrist I got suicidal tendencies. '
        f'He said from now on I have to pay in advance."{C.RST}'
    ]
    
    for line in sig_lines:
        typewriter(line, delay=0.01, color=C.WHT)
        time.sleep(0.2)
    
    print()
    print()
    
    # ─── Final box with the quote ────────────────────────────────────
    # Wrap quote for box
    words = quote.split()
    wrapped_lines = []
    current = ""
    for word in words:
        if len(current) + len(word) + 1 > 60:
            wrapped_lines.append(current)
            current = word
        else:
            current = current + " " + word if current else word
    if current:
        wrapped_lines.append(current)
    
    box = draw_box(wrapped_lines, width=74, border_color=C.MAG, 
                   title=f'{C.BLD}WOODY\'S WISDOM{C.RST}{C.MAG}')
    print(box)
    
    print()
    
    # ─── Closing animation: glasses fade ─────────────────────────────
    time.sleep(0.5)
    for _ in range(3):
        print(f'\r{C.CYN}{GLASSES_SMALL}{C.RST}     ', end='', flush=True)
        time.sleep(0.2)
        print(f'\r{C.DIM}{GLASSES_SMALL}{C.RST}     ', end='', flush=True)
        time.sleep(0.2)
    print(f'\r{C.CYN}{GLASSES_SMALL}{C.RST}     ')
    print()
    
    # ─── Final neurotic thought ──────────────────────────────────────
    final_thoughts = [
        "Anyway, I have to go. My mother called. She wants to know why I'm not married to a nice Jewish doctor.",
        "I should really go. I left my hypochondria appointment early.",
        "Existential crisis complete. Time for a bagel and more therapy.",
        "If you need me, I'll be worrying about things that haven't happened yet.",
    ]
    
    thought = random.choice(final_thoughts)
    typewriter(f'{C.ITL}{C.DIM}{thought}{C.RST}', delay=0.015)
    print()
    print()
    
    show_cursor()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        print(f'\n{C.RED}Interrupted. Just like my therapy sessions.{C.RST}')
        sys.exit(0)
    except Exception as e:
        show_cursor()
        print(f'\n{C.RED}Error: {e}{C.RST}')
        print(f'{C.DIM}Even my code has anxiety.{C.RST}')
        sys.exit(1)