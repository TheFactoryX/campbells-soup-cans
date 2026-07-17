"""
Campbell's Soup Can #4231
Produced: 2026-07-17 17:30:57
Worker: Free Models Router (openrouter/free)
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
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    BLINK = '\033[5m'
    UNDERLINE = '\033[4m'
    CLEAR = '\033[2J\033[H'

# Original Woody Allen-esque quote
QUOTE = "I told my therapist I have an inferiority complex. He said, 'Don't worry, it's not a very good one.'"

FRAMES = [
    f"""
{C.C}  ╔═══════════════════════════════════════════════════════════════╗
  ║  {C.Y}☕  WOODY'S WISDOM CORNER  ☕{C.C}                              ║
  ╠═══════════════════════════════════════════════════════════════╣
  ║                                                               ║
  ║  {C.W}{C.BOLD}\"{QUOTE}\"{C.RESET}{C.C}                         ║
  ║                                                               ║
  ║  {C.M}~ spoken into a tape recorder at 3am ~{C.C}                  ║
  ╚═══════════════════════════════════════════════════════════════╝{C.RESET}
""",
    f"""
{C.M}  ╔═══════════════════════════════════════════════════════════════╗
  ║  {C.Y}🧠  EXISTENTIAL CRISIS HOTLINE  🧠{C.M}                          ║
  ╠═══════════════════════════════════════════════════════════════╣
  ║                                                               ║
  ║  {C.W}{C.BOLD}\"{QUOTE}\"{C.RESET}{C.M}                         ║
  ║                                                               ║
  ║  {C.C}~ transcribed from muttered ramblings ~{C.M}                   ║
  ╚═══════════════════════════════════════════════════════════════╝{C.RESET}
""",
]

WOODY_ART = [
    f"""
{C.Y}       ▄▄▄▄▄▄▄
      █ {C.W}● {C.Y}█ {C.W}● {C.Y}█
      █{C.M}▄▄▄▄▄▄▄▄▄{C.Y}█
      █ {C.C}NEUROTIC{C.Y} █
      █{C.G}▀▀▀▀▀▀▀▀▀{C.Y}█
       ▀▀▀▀▀▀▀
{C.RESET}""",
    f"""
{C.C}       ▄▄▄▄▄▄▄
      █ {C.W}◉ {C.C}█ {C.W}◉ {C.C}█
      █{C.Y}▄▄▄▄▄▄▄▄▄{C.C}█
      █ {C.M}ANXIOUS{C.C} █
      █{C.G}▀▀▀▀▀▀▀▀▀{C.C}█
       ▀▀▀▀▀▀▀
{C.RESET}""",
]

def typewriter(text, delay=0.02, color=C.W):
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def animate_entrance():
    print(C.CLEAR)
    # Falling lines effect
    lines = [
        f"{C.DIM}Initializing neurosis...{C.RESET}",
        f"{C.DIM}Loading existential dread...{C.RESET}",
        f"{C.DIM}Calibrating hypochondria...{C.RESET}",
        f"{C.DIM}Fetching therapist's number...{C.RESET}",
        f"{C.G}{C.BOLD}Ready. Proceeding to overthink.{C.RESET}\n",
    ]
    for line in lines:
        print(line)
        time.sleep(0.3)

def pulse_quote():
    colors = [C.Y, C.G, C.C, C.M, C.B]
    for _ in range(3):
        for color in colors:
            print(C.CLEAR)
            frame = random.choice(FRAMES)
            # Colorize the quote part
            colored_frame = frame.replace(QUOTE, f"{color}{C.BOLD}{QUOTE}{C.RESET}")
            print(colored_frame)
            print(random.choice(WOODY_ART))
            time.sleep(0.5)

def final_display():
    print(C.CLEAR)
    frame = FRAMES[0]
    # Rainbow-ify the quote
    words = QUOTE.split()
    rainbow_words = []
    colors = [C.R, C.Y, C.G, C.C, C.B, C.M]
    for i, word in enumerate(words):
        rainbow_words.append(f"{colors[i % len(colors)]}{C.BOLD}{word}{C.RESET}")
    rainbow_quote = " ".join(rainbow_words)
    final = frame.replace(QUOTE, rainbow_quote)
    print(final)
    print(WOODY_ART[0])
    
    # Final typewriter sign-off
    print(f"\n{C.DIM}— Woody, probably, while ordering a pastrami on rye{C.RESET}\n")

def main():
    animate_entrance()
    pulse_quote()
    final_display()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.R}Interrupted. My mother would say 'I told you so.'{C.RESET}")