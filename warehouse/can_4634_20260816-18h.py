"""
Campbell's Soup Can #4634
Produced: 2026-08-16 18:47:00
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
    R = '\033[91m'
    G = '\033[92m'
    Y = '\033[93m'
    B = '\033[94m'
    M = '\033[95m'
    C = '\033[96m'
    W = '\033[97m'
    D = '\033[90m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDER = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'
    CLEAR = '\033[2J\033[H'

# Woody Allen quotes
QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering — and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "The talent for being happy is appreciating and liking what you have, instead of what you don't have.",
    "Eternal nothingness is fine if you happen to be dressed for it.",
    "I have bad reflexes. I was once run over by a car being pushed by two guys.",
    "Confidence is what you have before you understand the problem.",
    "More than any other time in history, mankind faces a crossroads. One path leads to despair and utter hopelessness. The other, to total extinction. Let us pray we have the wisdom to choose correctly.",
    "I'm astounded by people who want to 'know' the universe when it's hard enough to find your way around Chinatown.",
    "My one regret in life is that I am not someone else.",
    "If you want to make God laugh, tell him about your plans.",
    "The only time my prayers are answered is when I pray for something bad to happen and it does."
]

# ASCII art frames for Woody
WOODY_FRAMES = [
    r"""
      \   /
       \ /
      (o o)
       \_/
      /   \
    """,
    r"""
      \   /
       \ /
      (- -)
       \_/
      /   \
    """,
    r"""
      \   /
       \ /
      (o o)
       \_/
      /   \
    """,
    r"""
      \   /
       \ /
      (O O)
       \_/
      /   \
    """
]

GLASSES = r"""
      .--.   .--.
     /    \ /    \
    |  __   __  |
    | |  | |  | |
    | |__| |__| |
     \____/ \____/
"""

TYPEWRITER_SPEED = 0.03
GLITCH_CHARS = "!@#$%^&*()_+-=[]{}|;':\",./<>?"

def clear_screen():
    sys.stdout.write(C.CLEAR)
    sys.stdout.flush()

def typewriter(text, color=C.W, delay=TYPEWRITER_SPEED, newline=True):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(C.RESET)
    if newline:
        print()

def glitch_text(text, color=C.R, iterations=3):
    for _ in range(iterations):
        glitched = ''.join(random.choice(GLITCH_CHARS) if random.random() < 0.1 else c for c in text)
        sys.stdout.write(f'\r{color}{glitched}{C.RESET}')
        sys.stdout.flush()
        time.sleep(0.05)
    sys.stdout.write(f'\r{color}{text}{C.RESET}')
    sys.stdout.flush()

def animate_woody(frames, cycles=3):
    for _ in range(cycles):
        for frame in frames:
            clear_screen()
            print(f"{C.Y}{frame}{C.RESET}")
            time.sleep(0.3)

def draw_box(text_lines, border_color=C.C, title="", title_color=C.M):
    width = max(len(line) for line in text_lines) + 4
    top = f"{border_color}╔{'═' * (width - 2)}╗{C.RESET}"
    bottom = f"{border_color}╚{'═' * (width - 2)}╝{C.RESET}"
    
    lines = [top]
    if title:
        title_line = f"{border_color}║{C.RESET} {title_color}{title}{C.RESET}{' ' * (width - len(title) - 3)}{border_color}║{C.RESET}"
        lines.append(title_line)
        lines.append(f"{border_color}╠{'═' * (width - 2)}╣{C.RESET}")
    
    for line in text_lines:
        padding = width - len(line) - 4
        lines.append(f"{border_color}║{C.RESET} {line}{' ' * padding} {border_color}║{C.RESET}")
    
    lines.append(bottom)
    return '\n'.join(lines)

def sparkle_animation(duration=2):
    sparkles = ['✦', '✧', '⋆', '✵', '✸', '✹', '✺', '✻', '✼']
    start = time.time()
    while time.time() - start < duration:
        x = random.randint(5, 70)
        y = random.randint(2, 15)
        sparkle = random.choice(sparkles)
        color = random.choice([C.R, C.G, C.Y, C.B, C.M, C.C])
        sys.stdout.write(f'\033[{y};{x}H{color}{sparkle}{C.RESET}')
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    clear_screen()
    
    # Pick a random quote
    quote = random.choice(QUOTES)
    
    # Opening animation - Woody appears
    print(f"{C.BOLD}{C.Y}Loading neurotic existentialism...{C.RESET}\n")
    time.sleep(0.5)
    
    # Animated glasses
    for i in range(3):
        clear_screen()
        offset = " " * i
        print(f"{C.C}{offset}{GLASSES}{C.RESET}")
        print(f"{C.DIM}{offset}   Adjusting prescription...{C.RESET}")
        time.sleep(0.4)
    
    clear_screen()
    
    # Show Woody face with blinking animation
    print(f"{C.C}{GLASSES}{C.RESET}")
    animate_woody(WOODY_FRAMES, cycles=2)
    
    clear_screen()
    
    # Type the quote with dramatic effect
    print(f"\n{C.BOLD}{C.M}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}")
    print(f"{C.BOLD}{C.Y}  A Thought from the Neurotic Void:{C.RESET}")
    print(f"{C.BOLD}{C.M}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}\n")
    
    # Split quote into sentences for dramatic pausing
    sentences = quote.replace('—', '.').replace(';', '.').split('. ')
    
    for i, sentence in enumerate(sentences):
        if i > 0:
            sentence = '. ' + sentence
        if not sentence.endswith('.'):
            sentence += '.'
        
        # Type each sentence
        typewriter(f"{C.W}{C.ITALIC}\"{C.RESET}", delay=0.01, newline=False)
        typewriter(f"{C.W}{C.ITALIC}{sentence}{C.RESET}", delay=0.02, newline=False)
        typewriter(f"{C.W}{C.ITALIC}\"{C.RESET}", delay=0.01, newline=True)
        
        # Dramatic pause between sentences
        if i < len(sentences) - 1:
            time.sleep(0.8)
            # Add a neurotic interjection
            interjections = [
                f"{C.D}*adjusts glasses nervously*{C.RESET}",
                f"{C.D}*checks pulse*{C.RESET}",
                f"{C.D}*wonders if stove is on*{C.RESET}",
                f"{C.D}*existential dread intensifies*{C.RESET}",
            ]
            print(f"  {random.choice(interjections)}")
            time.sleep(0.5)
    
    print()
    print(f"{C.BOLD}{C.M}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}")
    
    # Final Woody sign-off
    time.sleep(0.5)
    signoffs = [
        "Anyway, I have a dentist appointment. Or was it a funeral? Same difference.",
        "I'm going to go lie down now. My hypochondria is acting up.",
        "If you need me, I'll be worrying about things that haven't happened yet.",
        "My therapist says I have a preoccupation with death. I told him, 'We all do, Doc. We all do.'",
    ]
    signoff = random.choice(signoffs)
    
    typewriter(f"\n{C.Y}{C.DIM}— {signoff}{C.RESET}", delay=0.02)
    
    # Final sparkle
    print(f"\n{C.DIM}Press Ctrl+C to escape the void...{C.RESET}")
    
    # Keep the quote visible with subtle animation
    try:
        while True:
            time.sleep(2)
            # Subtle blink of the quote
            sys.stdout.write(f'\033[10;5H{C.BLINK}{C.W}{C.ITALIC}"{quote}"{C.RESET}')
            sys.stdout.flush()
            time.sleep(0.5)
            sys.stdout.write(f'\033[10;5H{C.W}{C.ITALIC}"{quote}"{C.RESET}')
            sys.stdout.flush()
    except KeyboardInterrupt:
        clear_screen()
        print(f"\n{C.G}The void thanks you for your visit. Remember: death is just nature's way of telling you to slow down.{C.RESET}\n")

if __name__ == "__main__":
    main()