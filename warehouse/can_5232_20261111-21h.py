"""
Campbell's Soup Can #5232
Produced: 2026-11-11 21:59:06
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
A single-file Python program that serves up existential dread with a side of humor.
"""

import sys
import time
import random

# ─── ANSI Color Palette ───
class C:
    RST  = '\033[0m'
    BLD  = '\033[1m'
    DIM  = '\033[2m'
    ITL  = '\033[3m'
    UL   = '\033[4m'
    BLK  = '\033[30m'
    RED  = '\033[31m'
    GRN  = '\033[32m'
    YEL  = '\033[33m'
    BLU  = '\033[34m'
    MAG  = '\033[35m'
    CYN  = '\033[36m'
    WHT  = '\033[37m'
    BG_BLK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GRN = '\033[42m'
    BG_YEL = '\033[43m'
    BG_BLU = '\033[44m'
    BG_MAG = '\033[45m'
    BG_CYN = '\033[46m'
    BG_WHT = '\033[47m'

# ─── Woody's Quote Collection ───
QUOTES = [
    ("I took a speed-reading course and read War and Peace in twenty minutes. "
     "It involves Russia."),
    ("My one regret in life is that I am not someone else."),
    ("The universe is indifferent, which is the nicest thing you can say about it. "
     "At least it's not actively hostile. Yet."),
    ("I have a metaphysical dilemma: if a tree falls in a forest and no one's "
     "around, does it make a sound? More importantly, who's cleaning it up?"),
    ("Death is just nature's way of telling you to slow down. "
     "I'm already slow. Can I get an extension?"),
    ("I don't believe in an afterlife, but I'm bringing a change of underwear "
     "just in case. And a snack. Never travel without a snack."),
    ("My therapist says I have a preoccupation with mortality. "
     "I told her, 'We all do, we just call it Tuesday.'"),
    ("Life is a sexually transmitted terminal disease. "
     "The prognosis is poor, but the bedside manner is tolerable."),
    ("I'm at two with nature. Two very large, very angry men named nature."),
    ("If only God would give me a clear sign! Like a large deposit in my name "
     "at a Swiss bank. Or a parking spot on the Upper West Side."),
    ("Eternal nothingness is fine if you're dressed for it. "
     "I'm never dressed for it. I can't even find matching socks."),
    ("The lion and the lamb shall lie down together, but the lamb won't get "
     "much sleep. Neither will I, thinking about it."),
    ("I failed to make the chess team because of my height. "
     "Also, I don't play chess. Or sports. Or go outside."),
    ("Confidence is what you have before you understand the problem. "
     "I understand all the problems. That's why I have no confidence."),
    ("I'd call him a sadistic, hippophilic necrophile, but that would be "
     "beating a dead horse. Which he'd probably enjoy."),
]

# ─── ASCII Art Frames ───
WOODY_FRAMES = [
    r"""
     ╭────────────────────────────╮
     │  (◔_◔)   ←  That's me.     │
     │   / \                      │
     │  (   )  Existential dread  │
     │   \_/   loading... ████░░  │
     ╰────────────────────────────╯
""",
    r"""
     ╭────────────────────────────╮
     │  (◔_◔)   ←  Still me.      │
     │   /|\                      │
     │  (   )  Why did I say that?│
     │   \_/   Replaying 2003...  │
     ╰────────────────────────────╯
""",
    r"""
     ╭────────────────────────────╮
     │  (◔_◔)   ←  Me, worried.   │
     │   / \                      │
     │  (   )  Did I lock the     │
     │   \_/   door? The stove?   │
     │        My soul?            │
     ╰────────────────────────────╯
""",
]

TITLE_ART = f"""{C.MAG}{C.BLD}
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║   ██╗    ██╗ ██████╗ ██████╗ ███╗   ██╗███████╗              ║
    ║   ██║    ██║██╔═══██╗██╔══██╗████╗  ██║██╔════╝              ║
    ║   ██║ █╗ ██║██║   ██║██████╔╝██╔██╗ ██║█████╗                ║
    ║   ██║███╗██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝                ║
    ║   ╚███╔███╔╝╚██████╔╝██║  ██║██║ ╚████║███████╗              ║
    ║    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝              ║
    ║                                                              ║
    ║   ██████╗ ███████╗███╗   ██╗███████╗███████╗███████╗         ║
    ║   ██╔══██╗██╔════╝████╗  ██║██╔════╝██╔════╝██╔════╝         ║
    ║   ██║  ██║█████╗  ██╔██╗ ██║█████╗  ███████╗███████╗         ║
    ║   ██║  ██║██╔══╝  ██║╚██╗██║██╔══╝  ╚════██║╚════██║         ║
    ║   ██████╔╝███████╗██║ ╚████║███████╗███████║███████║         ║
    ║   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝         ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
{C.RST}"""

# ─── Animation Helpers ───
def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, delay=0.015, color=C.WHT, end='\n'):
    for char in text:
        print(f'{color}{char}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print(end, end='', flush=True)

def fade_in(text, color=C.WHT, steps=10):
    for i in range(steps + 1):
        intensity = i / steps
        # Simulate fade by printing with increasing visibility
        print(f'\r{color}{text}{C.RST}', end='', flush=True)
        time.sleep(0.03)
    print()

def scroll_text(text, width=60, color=C.CYN, delay=0.05):
    padded = ' ' * width + text + ' ' * width
    for i in range(len(padded) - width + 1):
        print(f'\r{color}{padded[i:i+width]}{C.RST}', end='', flush=True)
        time.sleep(delay)
    print()

# ─── Visual Effects ───
def neurotic_loader():
    """A little anxiety animation."""
    frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    thoughts = [
        "Overthinking...",
        "Replaying conversation from 2007...",
        "Checking if stove is off...",
        "Wondering if existence is a simulation...",
        "Calculating probability of catastrophe...",
        "Breathing... manually...",
        "Is that a symptom?...",
        "Why did I say 'you too' to the waiter?...",
    ]
    for _ in range(30):
        frame = random.choice(frames)
        thought = random.choice(thoughts)
        print(f'\r{C.YEL}{frame} {C.ITL}{thought}{C.RST}', end='', flush=True)
        time.sleep(0.08)
    print('\r' + ' ' * 60 + '\r', end='')

def quote_box(quote, color=C.CYN):
    """Draw a fancy box around the quote."""
    lines = []
    words = quote.split(' ')
    current_line = []
    max_width = 58
    
    for word in words:
        test_line = ' '.join(current_line + [word])
        if len(test_line) <= max_width:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Box drawing
    top = f'{color}╭{"─" * (max_width + 2)}╮{C.RST}'
    bottom = f'{color}╰{"─" * (max_width + 2)}╯{C.RST}'
    
    print(top)
    for line in lines:
        padding = max_width - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{color}│{C.RST}{" " * left_pad}{C.WHT}{C.ITL}{line}{C.RST}{" " * right_pad}{color}│{C.RST}')
    print(bottom)

def glasses_animation():
    """Woody's iconic glasses appear."""
    frames = [
        "       ▄▄       ▄▄      ",
        "      ████     ████     ",
        "     ██████   ██████    ",
        "    ████████ ████████   ",
        "   ██████████████████  ",
        "  ████████████████████ ",
        " ██████████████████████",
    ]
    for frame in frames:
        print(f'\r{C.BLU}{frame}{C.RST}', end='', flush=True)
        time.sleep(0.06)
    print()

# ─── Main Program ───
def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Title sequence
        print(TITLE_ART)
        time.sleep(0.5)
        
        # Neurotic loading
        print(f'\n{C.DIM}Initializing neurotic subsystem...{C.RST}\n')
        neurotic_loader()
        
        # Glasses appear
        print(f'\n{C.CYN}Adjusting glasses...{C.RST}')
        glasses_animation()
        
        # Pick a quote
        quote = random.choice(QUOTES)
        
        # Dramatic pause
        print(f'\n{C.MAG}{C.BLD}━━━ A Thought Occurs ━━━{C.RST}\n')
        time.sleep(0.4)
        
        # Typewriter the quote
        typewriter('"', delay=0.03, color=C.YEL, end='')
        typewriter(quote, delay=0.012, color=C.WHT, end='')
        typewriter('"', delay=0.03, color=C.YEL)
        
        print()
        
        # Show it in a nice box too
        time.sleep(0.3)
        print()
        quote_box(quote, C.MAG)
        
        # Random Woody frame
        print()
        frame = random.choice(WOODY_FRAMES)
        print(f'{C.CYN}{frame}{C.RST}')
        
        # Final neurotic sign-off
        signoffs = [
            "Anyway, I have a doctor's appointment. And a dentist. And a lawyer.",
            "I should go. My hypochondria is acting up. Or is it just Tuesday?",
            "Excuse me, I need to check if I unplugged the toaster. In 1994.",
            "My analyst says I should practice mindfulness. I'm mindful of everything that can go wrong.",
            "I'd stay and chat, but my separation anxiety is kicking in. From myself.",
        ]
        print(f'\n{C.DIM}{C.ITl}{random.choice(signoffs)}{C.RST}\n')
        
        # Credits scroll
        print(f'{C.DIM}', end='')
        scroll_text(
            "  Quote generated by the Woody Allen Quote-O-Matic 3000™  |  "
            "No neuroses were harmed in the making of this program  |  "
            "Side effects may include: existential dread, sudden urge to see a therapist, "
            "checking the stove 47 times  ",
            width=70, color=C.DIM, delay=0.02
        )
        print(f'{C.RST}')
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()