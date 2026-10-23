"""
Campbell's Soup Can #5154
Produced: 2026-10-23 19:14:02
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
    BD = '\033[1m'
    UL = '\033[4m'
    BL = '\033[5m'
    RS = '\033[0m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

# Original Woody Allen-style quotes
WOODY_QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
    "My therapist says I have a preoccupation with death. I told her, 'That's ridiculous — I'm too busy worrying about whether I left the stove on to die.'",
    "I don't believe in an afterlife, but I'm bringing a change of underwear just in case.",
    "The universe is indifferent to my existence. Which is fine, because I'm indifferent to the universe's — but it could at least send a thank-you note.",
    "I'm at two with nature. It wants to kill me, I want to stay alive. We compromise: I get allergies.",
    "Death doesn't worry me. It's the paperwork beforehand that gives me hives.",
    "I wanted to be a philosopher, but my mother said, 'Who's going to pay for the psychoanalysis?'",
    "Life is a sexually transmitted disease with a 100% mortality rate. My doctor calls it 'living.' I call it 'poor planning.'",
    "I have the metabolism of a hummingbird on espresso and the attention span of a goldfish with ADHD.",
    "God is silent. My analyst charges $350 an hour. You do the math.",
    "I'm not paranoid. I'm just extremely well-informed about all the things that can go wrong. Which is everything.",
    "My one regret in life is that I'm not someone else. Preferably someone with better posture and a 401(k)."
]

def clear_screen():
    print('\033[2J\033[H', end='')

def typewriter(text, color=C.W, delay=0.03, end='\n'):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    print(end, end='')
    sys.stdout.flush()

def sparkle_animation(duration=1.5):
    """Little sparkle animation around the quote"""
    sparkles = ['✦', '✧', '⋆', '✶', '✺', '✹', '✸', '✷']
    start = time.time()
    while time.time() - start < duration:
        x = random.randint(5, 65)
        y = random.randint(2, 12)
        s = random.choice(sparkles)
        color = random.choice([C.Y, C.C, C.M, C.G])
        print(f'\033[{y};{x}H{color}{s}{C.RS}', end='', flush=True)
        time.sleep(0.08)
        print(f'\033[{y};{x}H ', end='', flush=True)

def draw_fancy_box(width=70, height=14):
    """Draw a fancy ASCII box with Woody vibes"""
    tl, tr, bl, br = '╔', '╗', '╚', '╝'
    h, v = '═', '║'
    
    # Top border with decoration
    print(f"{C.M}{tl}{h * (width-2)}{tr}{C.RS}")
    
    # Content area with side borders
    for i in range(height - 2):
        if i == 0:
            # Title line
            title = " WOODY ALLEN'S DAILY DOSE OF EXISTENTIAL DREAD "
            padding = (width - 2 - len(title)) // 2
            print(f"{C.M}{v}{C.RS}{' ' * padding}{C.BD}{C.Y}{title}{C.RS}{' ' * (width - 2 - padding - len(title))}{C.M}{v}{C.RS}")
        elif i == 1:
            # Subtitle
            sub = " Neurotic Wisdom Since 1935 "
            padding = (width - 2 - len(sub)) // 2
            print(f"{C.M}{v}{C.RS}{' ' * padding}{C.D}{sub}{C.RS}{' ' * (width - 2 - padding - len(sub))}{C.M}{v}{C.RS}")
        elif i == 2:
            # Divider
            print(f"{C.M}{v}{C.D}{'─' * (width-2)}{C.RS}{C.M}{v}{C.RS}")
        elif i == height - 4:
            # Bottom divider
            print(f"{C.M}{v}{C.D}{'─' * (width-2)}{C.RS}{C.M}{v}{C.RS}")
        elif i == height - 3:
            # Signature line
            sig = " — Woody (probably) "
            padding = (width - 2 - len(sig)) // 2
            print(f"{C.M}{v}{C.RS}{' ' * padding}{C.C}{sig}{C.RS}{' ' * (width - 2 - padding - len(sig))}{C.M}{v}{C.RS}")
        else:
            print(f"{C.M}{v}{C.RS}{' ' * (width-2)}{C.M}{v}{C.RS}")
    
    # Bottom border
    print(f"{C.M}{bl}{h * (width-2)}{br}{C.RS}")

def print_woody_face():
    """Print a little Woody Allen ASCII face"""
    face = f"""
{C.Y}       ╭─────────╮
      │  {C.W}@   @{C.Y}  │   {C.D}"*sigh* Why me?"{C.RS}
      │  {C.C}▲{C.Y}   {C.C}▲{C.Y}  │
      │  {C.M}╰──┬──╯{C.Y}  │
      │     {C.M}│{C.Y}     │
      ╰─────────╯{C.RS}
"""
    print(face)

def main():
    clear_screen()
    
    # Pick a random quote
    quote = random.choice(WOODY_QUOTES)
    words = quote.split()
    
    # Print Woody face
    print_woody_face()
    time.sleep(0.5)
    
    # Draw the box
    draw_fancy_box()
    
    # Move cursor into the box for quote
    print('\033[6;4H', end='')  # Line 6, column 4 (inside box)
    
    # Type the quote word by word with varying colors
    colors = [C.W, C.C, C.G, C.Y, C.M]
    line = ""
    line_count = 0
    max_width = 62
    
    for i, word in enumerate(words):
        color = random.choice(colors)
        if len(line) + len(word) + 1 > max_width:
            # Print current line centered
            padding = (max_width - len(line)) // 2
            print(f"\033[{6 + line_count};{4 + padding}H{C.BD}{line.strip()}{C.RS}")
            line_count += 1
            line = word + " "
            # Typewriter effect for new line start
            for char in word + " ":
                sys.stdout.write(f"{color}{char}{C.RS}")
                sys.stdout.flush()
                time.sleep(0.02)
        else:
            line += word + " "
            for char in word + " ":
                sys.stdout.write(f"{color}{char}{C.RS}")
                sys.stdout.flush()
                time.sleep(0.025)
    
    # Print last line
    if line.strip():
        padding = (max_width - len(line)) // 2
        print(f"\033[{6 + line_count};{4 + padding}H{C.BD}{line.strip()}{C.RS}")
    
    # Move to signature area
    print('\033[13;4H', end='')
    
    # Sparkle animation
    print('\033[?25l', end='')  # Hide cursor
    sparkle_animation(2)
    print('\033[?25h', end='')  # Show cursor
    
    # Final position
    print('\033[16;0H')
    
    # Little footer
    footer_options = [
        f"{C.D}Press Ctrl+C to embrace the void...{C.RS}",
        f"{C.D}Your anxiety called. It wants its quote back.{C.RS}",
        f"{C.D}Remember: you're not paranoid if they're really out to get you.{C.RS}",
        f"{C.D}Death is nature's way of saying 'slow down'.{C.RS}",
    ]
    print(f"\n{random.choice(footer_options)}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}Interrupted! {C.Y}The universe wins this round.{C.RS}\n")
        sys.exit(0)