"""
Campbell's Soup Can #4535
Produced: 2026-08-11 13:42:42
Worker: inclusionAI: Ling 3.0 Tiny (free) (inclusionai/ling-3.0-tiny:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
🧠 Woody Allen Philosophical Quote Generator 🧠
A beautifully animated, colorful Python display of a classic
Woody Allen-style existential thought.

"Life is short. Live it."
"""

import time
import sys
import random

# ─── ANSI Colors ─────────────────────────────────────────────
class C:
    RESET   = '\033[0m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    ITALIC  = '\033[3m'
    RED     = '\033[91m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    BLUE    = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN    = '\033[96m'
    WHITE   = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED  = '\033[41m'
    BG_GREEN= '\033[42m'

# ─── Animated Frame ───────────────────────────────────────────
def frame(title, subtitle=""):
    w = 52
    print()
    print(" " + "█" * w)
    print(" " + "█" + "█" * (w - 2) + "█")
    for i in range(3):
        prefix = " " if i == 0 else " " * (w // 2 - 1)
        print(prefix + f"  {title.center(w)}  ")
        print(prefix + "  " + "█" * w + "  ")
        print(prefix + "  " + "█" + "█" * (w - 2) + "█")
        print(prefix + "  " + "█" * w + "  ")
    print()
    if subtitle:
        print(" " + " " * (w // 2 - 1) + subtitle.center(w) + " ")
    print(" " + "█" * w)
    print(" " + "█" + "█" * (w - 2) + "█")
    print()

# ─── Typing Effect ────────────────────────────────────────────
def typewriter(text, delay=0.04, color=None):
    if color is None:
        color = C.CYAN
    for i, char in enumerate(text):
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(color + C.RESET)

# ─── The Quote ────────────────────────────────────────────────
def the_quote():
    # A real Woody Allen quote with the right flavor
    quotes = [
        "I'm not afraid of death — I just don't want to be there",
        "Life is short. There's no business in it.",
        "I don't think I'm crazy. But I'm sure you would call me " + C.BOLD + C.RED + "crazy" + C.RESET +
        " if you did.",
        "I like my women like I like my hats — " + C.ITALIC + "a little too tight." + C.RESET +
        " Life is about a lot of things.",
        "I've been to hell, but I've never been to the moon.",
        "It's a beautiful morning. I'm going to love my life. I'm going to love my life. " + C.ITALIC +
        "It is not for the weak. The weak don't want to love their life." + C.RESET,
        "I was going to be a great philosopher. I was going to be a great thinker. " + C.ITALIC +
        "I just wanted to be happy." + C.RESET +
        " You know, I don't know what life is. I don't know why there is life. " + C.ITALIC +
        "But I know there must be a life. " + C.RESET,
        "I think I am the greatest lover I know. I'm a little nervous. " + C.ITALIC +
        "I like my women like I like my hats.",
        "There are only two types of people in the world: those who get scared " + C.RED + "when they're alone" +
        " and those who don't." + C.RESET,
        "I love my life. I love my life. My mother gave me my life. My mother gave me my life. " + C.ITALIC +
        "I like my life. I have never been sick. I have not been tired. I have not been hungry. " + C.RESET,
        "I'm not going to stop. I'll stop for the record. " + C.ITALIC +
        "I think the world is a great place. I love the world." + C.RESET,
    ]
    return random.choice(quotes)

# ─── ASCII Art ─────────────────────────────────────────────────
def art():
    lines = [
        "    .••  ••.   •   •.•   .•  ••.   •  ••.•  •  •.",
        "   /  |   |   |   |   |  |   |   |   |   |   |  /",
        "  //  |   |   |   |   |   |   |   |   |   |   \\",
        "  //   |   |   |   |   |   |   |   |   |   |   \\",
        "  |   |   |   |   |   |   |   |   |   |   |   |",
        "  |   |   |   |   |   |   |   |   |   |   |   |",
        "  |   |   |   |   |   |   |   |   |   |   |   |",
        "   \\  |   |   |   |   |   |   |   |   |   |  /",
        "    \\ |   |   |   |   |   |   |   |   |   |  /",
        "   . •   •  •  •  ••  •  •   •  • •  • ••   .",
        "  ██████████████████████████████████████████████",
        "  ██████████████████████████████████████████████",
        "  ██████████████████████████████████████████████",
        "  ██████████████████████████████████████████████",
        "  ██████████████████████████████████████████████",
    ]
    for line in lines:
        print(line)

# ─── Decorative Stars ──────────────────────────────────────────
def stars(count=30):
    for _ in range(count):
        x = random.randint(0, 79)
        y = random.randint(0, 18)
        if random.random() > 0.4:
            print(f"{'★':{x}^1}")
    print()

# ─── Animated Closing ─────────────────────────────────────────
def closing():
    time.sleep(0.3)
    print(f"{C.MAGENTA}{C.BOLD}"
          f"  ╔═══╗ {C.RESET}{C.BOLD}"
          f"  ║  ♦ ║  {C.RESET}"
          f"  ╠═══╣ {C.RESET}{C.BOLD}"
          f"  ║  ♦ ║  {C.RESET}"
          f"  ╚═══╝ {C.RESET}{C.BOLD}"
          f"  {C.YELLOW}✧  {C.RESET}  {C.BOLD}{C.RED}\"I'm not afraid of dying — "
          f"{C.RESET}I just don't want to be there when it happens.\"  "
          f"{C.MAGENTA}{C.BOLD}✧")
    time.sleep(0.5)
    print()
    print(f"  {C.GREEN}  *  {C.RESET}")
    print(f"  {C.GREEN}   ♦   {C.RESET}")
    print(f"  {C.GREEN}    ───   {C.RESET}")
    print()
    print(f"  {C.YELLOW}   ~ The end. Or perhaps not. ~{C.RESET}")
    print(f"  {C.GREEN}  Written by a {C.BOLD}lover of {C.ITALIC}life.{C.RESET}")
    print()

# ─── Main ──────────────────────────────────────────────────────
def main():
    # Art
    art()

    # Frame
    frame("💫 Woody Allen Philosophical Quote 💫", "A moment of existential beauty")

    # Quote with typewriter animation
    print(f"{C.BOLD}{C.GREEN}  Let me think about this for a moment.{C.RESET}")
    time.sleep(0.3)

    quote = the_quote()
    print(f"{C.BOLD}{C.YELLOW}  Quote: {C.RESET}{C.ITALIC}{quote}")
    print()

    # Extended explanation
    print(f"  {C.CYAN}  ── {C.RESET}")
    typewriter("The world is full of " + C.ITALIC + "beautiful, sad, and confusing" + C.RESET +
               " things. " + C.ITALIC + "You have to be happy.", delay=0.03, color=C.GREEN)
    print()
    print(f"  {C.MAGENTA}  Maybe the quote is: " + C.ITALIC + "I like my women like I like my hats — "
          "a little too tight." + C.RESET)
    print()
    print(f"  {C.YELLOW}  \"Life is not like a box of chocolates. "
          "It's like a box of sorrows, and you just have to deal with them one by one.\"{C.RESET}")

    # Stars
    stars(20)

    # Closing
    closing()

if __name__ == "__main__":
    main()