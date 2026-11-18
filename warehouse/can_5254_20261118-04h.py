"""
Campbell's Soup Can #5254
Produced: 2026-11-18 04:21:53
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

# Woody Allen original quote for this program
QUOTE = "I told my analyst I was having an identity crisis. He said, 'That'll be $300 — but who's asking?'"

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
GRAY = '\033[90m'

# Background colors
BG_BLACK = '\033[40m'
BG_BLUE = '\033[44m'

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=WHITE, delay=0.03, newline=True):
    """Print text with typewriter effect"""
    for char in text:
        print(f'{color}{char}{RESET}', end='', flush=True)
        time.sleep(delay + random.uniform(-0.01, 0.01))
    if newline:
        print()

def glitch_text(text, color=CYAN, iterations=3):
    """Glitch effect on text"""
    chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        print(f'\r{color}{glitched}{RESET}', end='', flush=True)
        time.sleep(0.05)
    print(f'\r{color}{text}{RESET}')

def draw_box(lines, width=70, color=CYAN, title=""):
    """Draw a fancy box around text"""
    top = f'{color}┌{"─" * (width - 2)}┐{RESET}'
    bottom = f'{color}└{"─" * (width - 2)}┘{RESET}'
    
    print(top)
    if title:
        title_line = f'{color}│{RESET} {BOLD}{YELLOW}{title.center(width - 4)}{RESET} {color}│{RESET}'
        print(title_line)
        print(f'{color}├{"─" * (width - 2)}┤{RESET}')
    
    for line in lines:
        padding = width - 4 - len(line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f'{color}│{RESET}{" " * left_pad}{line}{" " * right_pad}{color}│{RESET}')
    
    print(bottom)

def neurotic_animation():
    """A little neurotic animation before the quote"""
    thoughts = [
        "Wait, did I leave the stove on?",
        "Is this quote pretentious?",
        "Am I pretentious?",
        "Why am I talking to myself in code?",
        "Does the computer judge me?",
        "Should I have gone to law school?",
        "My mother was right about everything.",
        "Existential dread: loading... ████░░░░░░ 40%",
        "Okay, deep breaths. Just print the quote."
    ]
    
    print(f'{GRAY}{ITALIC}[Internal Monologue]{RESET}\n')
    for thought in thoughts:
        prefix = f'{GRAY}→ {RESET}'
        typewriter(f'{prefix}{thought}', GRAY, 0.015)
        time.sleep(random.uniform(0.15, 0.35))
    print()

def woody_face():
    """ASCII Woody Allen face"""
    face = f'''{YELLOW}
        ▄▄▄▄▄▄▄
       █       █
      █  ◉   ◉  █   "Neurosis is just
      █   ▿▿▿   █    advanced optimism"
      █  ▄▄▄▄▄  █
       █▀▀▀▀▀▀▀█
      ▄█       █▄
     █  █     █  █
    █   █     █   █
   █    ▀▀▀▀▀    █{RESET}'''
    return face

def main():
    hide_cursor()
    try:
        clear_screen()
        
        # Opening animation
        print(f'{BOLD}{MAGENTA}')
        print("╔" + "═" * 68 + "╗")
        print("║" + " " * 18 + "A WOODY ALLEN MOMENT" + " " * 18 + "║")
        print("╚" + "═" * 68 + "╝")
        print(f'{RESET}\n')
        
        # Show Woody
        print(woody_face())
        print()
        
        # Neurotic buildup
        neurotic_animation()
        
        # Dramatic pause
        time.sleep(0.5)
        print(f'{YELLOW}{ITALIC}▶ Delivering punchline in 3...{RESET}')
        time.sleep(0.4)
        print(f'{YELLOW}{ITALIC}▶ Delivering punchline in 2...{RESET}')
        time.sleep(0.4)
        print(f'{YELLOW}{ITALIC}▶ Delivering punchline in 1...{RESET}')
        time.sleep(0.4)
        print()
        
        # The quote - typewriter style with colors
        words = QUOTE.split()
        quote_lines = []
        current_line = ""
        
        for word in words:
            test_line = current_line + (" " if current_line else "") + word
            if len(test_line) > 56:
                quote_lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        if current_line:
            quote_lines.append(current_line)
        
        # Print quote in a fancy box with typewriter effect
        print(f'{CYAN}┌{"─" * 60}┐{RESET}')
        for line in quote_lines:
            print(f'{CYAN}│{RESET} ', end='', flush=True)
            typewriter(line, WHITE + BOLD, 0.025, newline=False)
            padding = 58 - len(line)
            print(f' {" " * padding}{CYAN}│{RESET}')
        print(f'{CYAN}└{"─" * 60}┘{RESET}')
        print()
        
        # Attribution with flair
        time.sleep(0.3)
        attribution = "— Woody Allen (probably, I mean, who knows anymore?)"
        typewriter(f'{ITALIC}{GRAY}{attribution:>70}{RESET}', GRAY, 0.02)
        print()
        print()
        
        # Final neurotic afterthought
        afterthoughts = [
            "Anyway, I have to go. My therapist says I have a fear of commitment.",
            "But I'm committed to this fear. So... progress?",
            "Goodnight. Don't let the bedbugs bite. Or do. They need to eat too.",
            "Is it too late to become a neurosurgeon? Asking for a friend.",
            "I should really call my mother. She hasn't guilt-tripped me in hours."
        ]
        chosen = random.choice(afterthoughts)
        typewriter(f'{DIM}{ITALIC}{chosen}{RESET}', GRAY, 0.02)
        print()
        print()
        
        # Little footer
        print(f'{GRAY}{"─" * 70}{RESET}')
        print(f'{GRAY}This program has been brought to you by Anxiety™ and Caffeine™{RESET}')
        print(f'{GRAY}No neurotics were harmed in the making of this quote. Mostly.{RESET}')
        
    finally:
        show_cursor()

if __name__ == '__main__':
    main()