"""
Campbell's Soup Can #5208
Produced: 2026-11-04 23:40:08
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
    RST = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'

# Woody Allen quotes (original, in his style)
QUOTES = [
    "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
    "The universe is merely a fleeting idea in God's mind—a pretty uncomfortable thought, especially if you've just paid for a parking ticket.",
    "I don't believe in an afterlife, although I am bringing a change of underwear, just in case.",
    "My one regret in life is that I am not someone else. Preferably someone with better posture and a trust fund.",
    "Death doesn't worry me. It's the pre-show— the waiting room with the outdated magazines—that terrifies me.",
    "I'm at two with nature. Which is one better than most people, but still leaves me arguing with a squirrel over a bagel.",
    "If only God would give me some clear sign! Like making a large deposit in my name at a Swiss bank.",
    "Life is divided into the horrible and the miserable. The horrible are terminal cases. The miserable is everyone else. I'm miserable. You're miserable. Let's get coffee.",
    "I have a gnawing feeling that the universe is indifferent to my existence. Which is fine, really. I'm indifferent to most of its movies.",
    "My analyst says I have a preoccupation with mortality. I told him, 'Doc, at my age, mortality has a preoccupation with ME.'",
]

# ASCII Art - Woody-style glasses
GLASSES = [
    "    .--.       .--.    ",
    "   /    \\     /    \\   ",
    "  |  __  |   |  __  |  ",
    "  | |  | |   | |  | |  ",
    "  | |__| |   | |__| |  ",
    "   \\____/     \\____/   ",
]

# Neurotic face
FACES = [
    [
        "     .--.       .--.     ",
        "    / .. \\     / .. \\    ",
        "   |  __  |   |  __  |   ",
        "    \\ \\/ /     \\ \\/ /    ",
        "     '--'       '--'     ",
        "        \\  __  /         ",
        "         \\/  \\/          ",
    ],
    [
        "     .--.       .--.     ",
        "    / :: \\     / :: \\    ",
        "   |  __  |   |  __  |   ",
        "    \\ \\/ /     \\ \\/ /    ",
        "     '--'       '--'     ",
        "        \\    /           ",
        "         \\  /            ",
    ],
    [
        "     .--.       .--.     ",
        "    / @@ \\     / @@ \\    ",
        "   |  __  |   |  __  |   ",
        "    \\ \\/ /     \\ \\/ /    ",
        "     '--'       '--'     ",
        "        \\ __ /           ",
        "         \\/\\/            ",
    ],
]

def clear_screen():
    print('\033[2J\033[H', end='')

def hide_cursor():
    print('\033[?25l', end='')

def show_cursor():
    print('\033[?25h', end='')

def typewriter(text, color=C.WHITE, delay=0.03, newline=True):
    for char in text:
        print(f"{color}{char}{C.RST}", end='', flush=True)
        time.sleep(delay)
    if newline:
        print()

def animate_glasses():
    for i in range(3):
        clear_screen()
        print(f"\n{C.CYAN}{C.BOLD}")
        for line in GLASSES:
            print(f"        {line}")
        print(f"{C.RST}")
        time.sleep(0.3)
        clear_screen()
        time.sleep(0.15)

def animate_face():
    for _ in range(2):
        for face in FACES:
            clear_screen()
            print(f"\n{C.YELLOW}{C.BOLD}")
            for line in face:
                print(f"        {line}")
            print(f"{C.RST}")
            time.sleep(0.4)

def draw_box(text, width=70, color=C.MAGENTA, bg=C.BG_BLACK):
    lines = text.split('\n')
    inner_width = width - 4
    print(f"{color}{bg}")
    print("╔" + "═" * (width - 2) + "╗")
    for line in lines:
        padded = line.center(inner_width)
        print(f"║ {padded} ║")
    print("╚" + "═" * (width - 2) + "╝")
    print(f"{C.RST}")

def sparkle_animation(duration=2.0):
    chars = ['✦', '✧', '★', '☆', '✨', '⋆', '✺', '✷']
    start = time.time()
    while time.time() - start < duration:
        x = random.randint(5, 75)
        y = random.randint(2, 15)
        char = random.choice(chars)
        color = random.choice([C.YELLOW, C.CYAN, C.MAGENTA, C.GREEN])
        print(f"\033[{y};{x}H{color}{char}{C.RST}", end='', flush=True)
        time.sleep(0.05)

def main():
    hide_cursor()
    clear_screen()
    
    # Pick a quote
    quote = random.choice(QUOTES)
    
    # Opening animation
    print(f"\n{C.DIM}{C.CYAN}")
    print(" " * 20 + "┌" + "─" * 40 + "┐")
    print(" " * 20 + "│" + " " * 10 + "A WOODY ALLEN MOMENT" + " " * 8 + "│")
    print(" " * 20 + "└" + "─" * 40 + "┘")
    print(f"{C.RST}\n")
    time.sleep(0.8)
    
    # Animate glasses appearing
    animate_glasses()
    
    # Type the quote with neurotic pauses
    clear_screen()
    print(f"\n{C.YELLOW}{C.BOLD}")
    for line in FACES[0]:
        print(f"        {line}")
    print(f"{C.RST}\n")
    
    # Typewriter effect for the quote
    print(f"  {C.GREEN}│ {C.RST}", end='', flush=True)
    
    # Split into neurotic chunks
    words = quote.split(' ')
    for i, word in enumerate(words):
        color = C.WHITE if i % 2 == 0 else C.CYAN
        for char in word:
            print(f"{color}{char}{C.RST}", end='', flush=True)
            time.sleep(random.uniform(0.02, 0.06))
        print(" ", end='', flush=True)
        # Neurotic pauses at commas and periods
        if ',' in word or '.' in word:
            time.sleep(random.uniform(0.3, 0.6))
            print(f"{C.DIM}...{C.RST}", end='', flush=True)
            time.sleep(0.2)
    
    print(f"\n  {C.GREEN}│{C.RST}\n")
    time.sleep(1)
    
    # Final presentation in a nice box
    clear_screen()
    print()
    draw_box(f"\"{quote}\"", width=76, color=C.MAGENTA, bg=C.BG_BLACK)
    print()
    
    # Signature
    print(f"  {C.DIM}{C.CYAN}─ — —  {C.BOLD}Woody Allen{C.RST}{C.DIM}{C.CYAN}  (probably) — — ─{C.RST}")
    print()
    
    # Sparkle finale
    sparkle_animation(1.5)
    print("\n\n")
    
    show_cursor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        show_cursor()
        clear_screen()
        print(f"\n{C.RED}Interrupted. Typical. Even my exit strategy has anxiety.{C.RST}\n")
    except Exception as e:
        show_cursor()
        print(f"\n{C.RED}Something went wrong. Story of my life: {e}{C.RST}\n")