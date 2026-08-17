"""
Campbell's Soup Can #4641
Produced: 2026-08-17 03:12:48
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

# ANSI Color Codes
class C:
    R = '\033[0m'      # Reset
    B = '\033[1m'      # Bold
    D = '\033[2m'      # Dim
    I = '\033[3m'      # Italic
    U = '\033[4m'      # Underline
    
    # Foreground
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
    
    # Background
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody Allen's glasses ASCII
GLASSES = f"""
{C.CYAN}      ╔══════════════════════════════════════════╗
      ║  {C.YELLOW}███{C.CYAN}                    {C.YELLOW}███{C.CYAN}  ║
      ║  {C.YELLOW}███{C.CYAN}   {C.WHITE}◉{C.GRAY}────────────{C.WHITE}◉{C.CYAN}   {C.YELLOW}███{C.CYAN}  ║
      ║  {C.YELLOW}███{C.CYAN}                    {C.YELLOW}███{C.CYAN}  ║
      ╚══════════════════════════════════════════╝{C.R}
"""

# The quote - original Woody Allen style
QUOTE = (
    "I took a course in speed-waiting. "
    "Now I can wait an hour in just ten minutes."
)

QUOTE_2 = (
    "My analyst says I have a preoccupation with death. "
    "I told him that's absurd — I'm much too busy "
    "worrying about whether I left the stove on "
    "in my previous life."
)

QUOTE_3 = (
    "The universe is indifferent. "
    "My landlord, however, is very opinionated "
    "about the rent."
)

QUOTE_4 = (
    "I don't believe in an afterlife, "
    "but I'm bringing a change of underwear "
    "just in case."
)

QUOTES = [QUOTE, QUOTE_2, QUOTE_3, QUOTE_4]

# Decorative elements
STARS = "✦ ✧ ★ ✰ ⋆ ❋ ✵ ✸ ✹ ✺ ✻ ✼ ❂ ❃ ❄ ❅ ❆ ❇ ❈ ❉ ❊ ❋"

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def move_cursor(y, x):
    print(f'\033[{y};{x}H', end='')

def typewriter(text, color=C.WHITE, delay=0.02, newline=True):
    for char in text:
        print(f"{color}{char}{C.R}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def fade_in_text(text, color=C.WHITE, steps=10):
    for i in range(steps + 1):
        alpha = i / steps
        # Simulate fade with dim/bold
        if alpha < 0.3:
            style = C.D
        elif alpha < 0.7:
            style = C.R
        else:
            style = C.B
        print(f'\r{style}{color}{text}{C.R}', end='', flush=True)
        time.sleep(0.05)
    print()

def draw_box(content_lines, width=60, border_color=C.CYAN, title=""):
    top = f"{border_color}╔{'═' * (width - 2)}╗{C.R}"
    bottom = f"{border_color}╚{'═' * (width - 2)}╝{C.R}"
    
    lines = [top]
    if title:
        title_line = f" {title} "
        padding = width - 2 - len(title_line)
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{border_color}║{C.R}{' ' * left_pad}{C.B}{C.YELLOW}{title_line}{C.R}{' ' * right_pad}{border_color}║{C.R}")
        lines.append(f"{border_color}║{' ' * (width - 2)}║{C.R}")
    
    for line in content_lines:
        visible_len = len(line.replace('\033[', '').replace('m', ''))  # rough
        # Better: strip ANSI
        import re
        clean = re.sub(r'\033\[[0-9;]*m', '', line)
        padding = width - 2 - len(clean)
        lines.append(f"{border_color}║{C.R} {line}{' ' * padding} {border_color}║{C.R}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def sparkle_animation(duration=2):
    """Little sparkle animation around the quote"""
    colors = [C.YELLOW, C.CYAN, C.MAGENTA, C.GREEN, C.BRIGHT_YELLOW, C.BRIGHT_CYAN]
    sparkles = ['✦', '✧', '★', '✰', '⋆', '❋', '✵', '✸']
    end_time = time.time() + duration
    
    while time.time() < end_time:
        x = random.randint(5, 70)
        y = random.randint(5, 15)
        color = random.choice(colors)
        sparkle = random.choice(sparkles)
        move_cursor(y, x)
        print(f"{color}{sparkle}{C.R}", end='', flush=True)
        time.sleep(0.05)
        move_cursor(y, x)
        print(" ", end='', flush=True)

def main():
    hide_cursor()
    clear_screen()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # Title animation
    print(f"\n{C.CYAN}{C.B}")
    print("    ╔══════════════════════════════════════════════════════════════╗")
    print("    ║                                                               ║")
    print("    ║     W O O D Y   A L L E N ' S   D A I L Y   N E U R O S I S  ║")
    print("    ║                                                               ║")
    print("    ╚══════════════════════════════════════════════════════════════╝")
    print(f"{C.R}\n")
    
    # Glasses
    print(GLASSES)
    
    # Typing the quote with typewriter effect
    print(f"{C.YELLOW}{C.B}  \"{C.R}", end='', flush=True)
    time.sleep(0.3)
    
    # Split quote into sentences for dramatic effect
    sentences = quote.split('. ')
    for i, sent in enumerate(sentences):
        if i > 0:
            print(f"{C.YELLOW}. {C.R}", end='', flush=True)
            time.sleep(0.4)
        typewriter(sent, color=C.WHITE, delay=0.03, newline=False)
    
    print(f"{C.YELLOW}\"{C.R}")
    print()
    
    # Attribution with style
    time.sleep(0.5)
    print(f"  {C.D}{C.GRAY}— Woody Allen, probably{C.R}")
    print(f"  {C.D}{C.GRAY}(as channeled by a Python script having an existential crisis){C.R}\n")
    
    # Decorative footer box
    footer_lines = [
        f"{C.CYAN}Philosophical Advisory:{C.R} This quote contains traces of neurosis,",
        f"existential dread, and {C.YELLOW}zero{C.R} nutritional value.",
        f"",
        f"{C.MAGENTA}Side effects{C.R} may include: questioning reality,",
        f"checking if the stove is off, and sudden urge to",
        f"see a therapist who falls asleep during sessions.",
    ]
    
    print(draw_box(footer_lines, width=64, border_color=C.MAGENTA, title=" ⚠ WARNING "))
    
    # Final sparkle
    print(f"\n{C.GRAY}{C.D}  Press Ctrl+C to exit this simulation...{C.R}\n")
    
    # Subtle breathing animation on the quote
    try:
        breath_chars = ['▓', '▒', '░', '▒']
        idx = 0
        while True:
            # Just a subtle pulster on the glasses
            time.sleep(1.5)
            idx = (idx + 1) % len(breath_chars)
    except KeyboardInterrupt:
        pass
    finally:
        show_cursor()
        clear_screen()
        print(f"{C.CYAN}Thanks for the neurosis. Remember: {C.YELLOW}the universe doesn't care, {C.CYAN}but your landlord does.{C.R}\n")

if __name__ == "__main__":
    main()