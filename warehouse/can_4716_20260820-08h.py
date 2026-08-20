"""
Campbell's Soup Can #4716
Produced: 2026-08-20 08:56:10
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
    R = '\033[91m'      # Red
    G = '\033[92m'      # Green
    Y = '\033[93m'      # Yellow
    B = '\033[94m'      # Blue
    M = '\033[95m'      # Magenta
    C = '\033[96m'      # Cyan
    W = '\033[97m'      # White
    BD = '\033[1m'      # Bold
    DM = '\033[2m'      # Dim
    UL = '\033[4m'      # Underline
    BL = '\033[5m'      # Blink
    RS = '\033[0m'      # Reset
    BG_B = '\033[44m'   # Blue background
    BG_R = '\033[41m'   # Red background
    BG_Y = '\033[43m'   # Yellow background

# Woody Allen quotes (original, in his style)
WOODY_QUOTES = [
    "I took a speed-reading course and read 'War and Peace' in twenty minutes.\nIt involves Russia.",
    
    "My one regret in life is that I'm not someone else.\nPreferably someone with better posture and a 401(k).",
    
    "The universe is indifferent. So is my dentist.\nAt least the universe doesn't lecture me about flossing.",
    
    "I don't believe in an afterlife, although I'm bringing a change of underwear\njust in case there's a mix-up at the pearly gates.",
    
    "My therapist says I have a preoccupation with death.\nI told him that's ridiculous — I'm preoccupied with not dying.\nThere's a nuance. A subtle, expensive nuance.",
    
    "I was thrown out of college for cheating on the metaphysics exam.\nI looked into the soul of the boy sitting next to me.\nTurns out, he didn't have one either. Just student loans.",
    
    "Life is divided into the horrible and the miserable.\nThe horrible are terminal diseases and people who talk during movies.\nThe miserable is everyone else. Including me. Especially me.",
    
    "I'm at two with nature.\nNature wants to kill me, and I want to order takeout.\nWe've reached a tense stalemate.",
    
    "Eternal nothingness is fine if you're dressed for it.\nBut who wants to spend infinity in a polyester blend?",
    
    "I don't want to achieve immortality through my work.\nI want to achieve it through my accountant finding a loophole.\nSo far, the IRS is winning. They're very persistent. Like death, but with better stationery."
]

# Woody Allen ASCII art (glasses + face)
WOODY_ART = [
    "        ╔═══════════════════════╗",
    "        ║  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ║",
    "        ║ █ ▀▀▀ █ █ ▀▀▀ █ ║",
    "        ║ █ ▄▄▄ █ █ ▄▄▄ █ ║  ←  The Glasses",
    "        ║ █ ▀▀▀ █ █ ▀▀▀ █ ║",
    "        ║  ▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀  ║",
    "        ╚═══════════════════════╝",
    "                │     │",
    "                ▼     ▼",
    "           ┌───────────┐",
    "           │  (o) (o)  │  ←  Neurotic gaze",
    "           │     △     │",
    "           │  \\_____/  │  ←  Signature frown",
    "           └───────────┘",
]

# Decorative elements
DIVIDER = "━" * 60
STARS = "✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦ ✧ ✦"

def typewriter(text, color=C.W, delay=0.02, newline=True):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(f"{color}{char}{C.RS}")
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def fade_in(text, color=C.W, steps=10):
    """Fade in text by gradually increasing brightness"""
    for i in range(steps):
        brightness = int(30 + (225 * i / steps))
        sys.stdout.write(f"\r\033[38;5;{brightness}m{text}{C.RS}")
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def print_boxed_quote(quote, color=C.Y, border_color=C.C):
    """Print quote in a fancy box"""
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + 4
    
    print(f"\n{border_color}┌{'─' * width}┐{C.RS}")
    for line in lines:
        padding = width - len(line) - 2
        left_pad = padding // 2
        right_pad = padding - left_pad
        print(f"{border_color}│{C.RS}{' ' * left_pad}{color}{line}{C.RS}{' ' * right_pad}{border_color}│{C.RS}")
    print(f"{border_color}└{'─' * width}┘{C.RS}\n")

def animate_thought_bubble():
    """Show a little thinking animation"""
    thoughts = [
        "Hmm...", "Wait...", "But what if...", "Oh no.", 
        "That's terrifying.", "I need a sandwich.", "Existential dread: 100%"
    ]
    for thought in thoughts:
        sys.stdout.write(f"\r{C.DM}{C.C}[{thought}]{C.RS}   ")
        sys.stdout.flush()
        time.sleep(0.4)
    sys.stdout.write("\r" + " " * 40 + "\r")
    sys.stdout.flush()

def main():
    # Clear screen
    print("\033[2J\033[H", end="")
    
    # Title animation
    print(f"\n{C.BD}{C.M}{'='*60}{C.RS}")
    typewriter(f"{C.BD}{C.Y}   W O O D Y   A L L E N   Q U O T E   G E N E R A T O R{C.RS}", C.Y, 0.01)
    print(f"{C.BD}{C.M}{'='*60}{C.RS}\n")
    
    # Print Woody ASCII art with colors
    print(f"{C.C}")
    for i, line in enumerate(WOODY_ART):
        if i < 7:
            print(f"{C.B}{line}{C.RS}")
        else:
            print(f"{C.Y}{line}{C.RS}")
        time.sleep(0.08)
    print(f"{C.RS}")
    
    # Thinking animation
    print(f"{C.DM}Contemplating the void...{C.RS}")
    animate_thought_bubble()
    
    # Select random quote
    quote = random.choice(WOODY_QUOTES)
    
    # Dramatic pause
    time.sleep(0.5)
    
    # Print decorative separator
    print(f"\n{C.M}{STARS}{C.RS}\n")
    
    # Print the quote with typewriter effect, line by line
    print(f"{C.BD}{C.G}Woody muses:{C.RS}\n")
    for line in quote.split('\n'):
        typewriter(f"  {line}", C.W, 0.015)
        time.sleep(0.15)
    
    # Decorative separator
    print(f"\n{C.M}{STARS}{C.RS}")
    
    # Final philosophical footer
    footers = [
        f"{C.DM}— Now if you'll excuse me, I have an appointment with my analyst.{C.RS}",
        f"{C.DM}— I'd explain further, but my neurosis has a 3 PM.{C.RS}",
        f"{C.DM}— This quote brought to you by anxiety and rye bread.{C.RS}",
    ]
    print(f"\n{random.choice(footers)}")
    
    # Final flourish
    print(f"\n{C.C}{C.DM}Press Ctrl+C to exit... or don't. The void doesn't care either way.{C.RS}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.R}{C.BD}Interrupted! {C.RS}{C.Y}Even the program has commitment issues.{C.RS}\n")
        sys.exit(0)