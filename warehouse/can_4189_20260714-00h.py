"""
Campbell's Soup Can #4189
Produced: 2026-07-14 00:08:46
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
class C:
    R = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Woody Allen quotes (original, in his voice)
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
    "The talent for being happy is appreciating what you have, not what you don't have. Which explains why I'm miserable.",
    "I don't believe in an afterlife, although I am bringing a change of underwear.",
    "Life doesn't imitate art, it imitates bad television.",
    "I'm not afraid of death. I just don't want to be there when it happens. Or the waiting room beforehand. Or the paperwork.",
    "My therapist says I have a preoccupation with mortality. I told him, 'Doc, at my age, it's not a preoccupation. It's a schedule.'",
    "I don't want to achieve immortality through my work. I want to achieve it through not dying. Or at least a really good moisturizer.",
    "The universe is indifferent. My landlord, however, is very opinionated.",
    "I have a fear of commitment. And intimacy. And elevators. And tuna fish. Mostly tuna fish.",
    "You can live to be a hundred if you give up all the things that make you want to live to be a hundred. So I'll die at forty-two, but happy.",
]

WOODY_ASCII = r"""
       \   /
        \ /
     .--( )--.
    /  _\ /_  \
   |  (o) (o)  |
   |    __     |
    \  \__/  /
     '.____.'
      |    |
     _'    '_
"""

NEUROTIC_ASCII = r"""
    🧠  THOUGHTS.RUNNING...  🧠
   ╔══════════════════════════╗
   ║  ████████░░░░  87%      ║
   ║  [████████░░] ANXIETY   ║
   ║  [██████░░░░] DOUBT     ║
   ║  [██████████] REGRET    ║
   ║  [██░░░░░░░░] HOPE      ║
   ╚══════════════════════════╝
"""

def typewriter(text, delay=0.02, color=C.WHITE):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.R}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def fade_in(text, color=C.CYAN, steps=10):
    """Fade in text"""
    for i in range(steps + 1):
        intensity = i / steps
        sys.stdout.write(f"\r{color}{text}{C.R}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def glitch_text(text, color=C.MAGENTA, iterations=3):
    """Glitch effect"""
    chars = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`"
    for _ in range(iterations):
        glitched = ''.join(random.choice(chars) if random.random() < 0.1 else c for c in text)
        sys.stdout.write(f"\r{color}{glitched}{C.R}")
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f"\r{color}{text}{C.R}\n")
    sys.stdout.flush()

def draw_box(content_lines, title="", color=C.CYAN, width=60):
    """Draw a fancy box around content"""
    inner_width = width - 4
    top = f"{color}╔{'═' * (width - 2)}╗{C.R}"
    bottom = f"{color}╚{'═' * (width - 2)}╝{C.R}"
    
    lines = [top]
    
    if title:
        title_line = f" {title.center(inner_width)} "
        lines.append(f"{color}║{C.BOLD}{title_line}{C.R}{color}║{C.R}")
        lines.append(f"{color}╠{'═' * (width - 2)}╣{C.R}")
    
    for line in content_lines:
        # Handle ANSI codes in length calculation
        visible_len = len(line)
        for code in [C.R, C.BOLD, C.DIM, C.RED, C.GREEN, C.YELLOW, C.BLUE, C.MAGENTA, C.CYAN, C.WHITE]:
            visible_len -= line.count(code) * len(code)
        padding = inner_width - visible_len
        left_pad = padding // 2
        right_pad = padding - left_pad
        lines.append(f"{color}║{' ' * left_pad}{line}{' ' * right_pad}{color}║{C.R}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def spinning_loader(message, duration=1.5):
    """Spinning loader animation"""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f"\r{C.CYAN}{spinner[i % len(spinner)]} {message}{C.R}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write(f"\r{' ' * (len(message) + 4)}\r")
    sys.stdout.flush()

def main():
    # Clear screen
    print('\033[2J\033[H', end='')
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # Intro animation
    print(f"{C.MAGENTA}{C.BOLD}")
    print("    ╭─────────────────────────────────────────────╮")
    print("    │                                             │")
    print("    │     W O O D Y   A L L E N   M O D E         │")
    print("    │     Neurotic Philosophy Generator v1.0      │")
    print("    │                                             │")
    print("    ╰─────────────────────────────────────────────╯")
    print(f"{C.R}")
    
    time.sleep(0.5)
    
    # Show Woody ASCII
    print(f"{C.YELLOW}{WOODY_ASCII}{C.R}")
    time.sleep(0.3)
    
    # Loading thoughts
    spinning_loader("Consulting therapist...", 1.2)
    spinning_loader("Checking for symptoms...", 1.0)
    spinning_loader("Overthinking existence...", 1.5)
    
    print()
    
    # Show neurotic brain
    print(f"{C.CYAN}{NEUROTIC_ASCII}{C.R}")
    print()
    
    time.sleep(0.5)
    
    # The reveal
    print(f"{C.GREEN}{C.BOLD}    ⟫  AHA! A THOUGHT EMERGES FROM THE ABYSS  ⟪{C.R}")
    print()
    time.sleep(0.5)
    
    # Typewriter the quote in a fancy box
    quote_lines = []
    words = quote.split(' ')
    current_line = ""
    max_width = 50
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += (" " if current_line else "") + word
        else:
            quote_lines.append(current_line)
            current_line = word
    if current_line:
        quote_lines.append(current_line)
    
    # Build the box with typewriter effect
    box_top = f"{C.MAGENTA}╔{'═' * 56}╗{C.R}"
    box_bottom = f"{C.MAGENTA}╚{'═' * 56}╝{C.R}"
    
    print(box_top)
    print(f"{C.MAGENTA}║{' ' * 56}║{C.R}")
    
    for line in quote_lines:
        # Typewriter each line inside the box
        sys.stdout.write(f"{C.MAGENTA}║ {C.BOLD}{C.YELLOW}")
        sys.stdout.flush()
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.025)
        # Padding
        padding = 54 - len(line)
        sys.stdout.write(f"{' ' * padding}{C.R}{C.MAGENTA}║{C.R}")
        print()
        time.sleep(0.15)
    
    print(f"{C.MAGENTA}║{' ' * 56}║{C.R}")
    print(box_bottom)
    
    print()
    time.sleep(0.3)
    
    # Attribution with flair
    attribution = "— Woody Allen (probably, in an alternate universe where he writes Python)"
    glitch_text(f"    {attribution}", C.DIM + C.CYAN, 2)
    
    print()
    print()
    
    # Final neurotic touch
    final_thoughts = [
        "    (adjusts glasses nervously)",
        "    (checks pulse)",
        "    (wonders if the quote was too long)",
        "    (worries the universe is judging)",
        "    (exits stage left, tripping over own shadow)"
    ]
    
    for thought in final_thoughts:
        print(f"{C.DIM}{C.BLUE}{thought}{C.R}")
        time.sleep(0.25)
    
    print()
    print(f"{C.MAGENTA}    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.R}")
    print(f"{C.MAGENTA}    ░  Thank you for your anxiety. Come again soon.       ░{C.R}")
    print(f"{C.MAGENTA}    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░{C.R}")
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.RED}\n    (exits abruptly, muttering about mortality){C.R}")
        sys.exit(0)