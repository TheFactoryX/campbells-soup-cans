"""
Campbell's Soup Can #4179
Produced: 2026-07-13 00:10:51
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

# Backgrounds
BG_BLACK = '\033[40m'
BG_DARK = '\033[100m'

WOODY_QUOTE = (
    "I took a speed-reading course and read 'War and Peace' in twenty minutes. "
    "It involves Russia."
)

WOODY_LINES = [
    "I took a speed-reading course",
    "and read 'War and Peace' in twenty minutes.",
    "It involves Russia."
]

WOODY_ASCII = r"""
      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
     █                                                                      █
     █   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   █
     █   █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █   █
     █   █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █   █
     █   █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █   █
     █   █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █   █
     █   █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █   █
     █   █  █  █  █  █  █                                      █  █  █  █  █  █   █
     █   █  █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █  █   █
     █   █  █  █  █  █  █  █  █  WOODY ALLEN SIMULATOR v1.0  █  █  █  █  █  █  █  █   █
     █   █  █  █  █  █  █  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  █  █  █  █  █   █
     █   █  █  █  █  █  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  █  █  █  █   █
     █   █  █  █  █  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  █  █  █   █
     █   █  █  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  █  █   █
     █   █  █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █  █   █
     █   █  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  █   █
     █   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀   █
     █                                                                      █
      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
"""

GLASSES = r"""
    ╔════════════════════════════════════════════════════════════════════╗
    ║  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ║
    ║  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  ║
    ║  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  ║
    ║  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  ║
    ║  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  ║
    ║  █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ║
    ║  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ║
    ║  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ║
    ╚════════════════════════════════════════════════════════════════════╝
"""

NEUROTIC_THOUGHTS = [
    "Wait, did I leave the stove on?",
    "Is that a lump? It feels like a lump.",
    "Everyone's judging me. Even the cat.",
    "I should have said 'you too' to the waiter.",
    "What if this simulation crashes?",
    "My therapist would call this 'avoidance behavior'.",
    "Death is just life's way of saying 'time's up'.",
    "I'm not paranoid. They really ARE out to get me.",
]

def typewriter_print(text, delay=0.03, color=WHITE, end='\n'):
    for char in text:
        sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def animate_glasses():
    frames = [
        "    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ",
        "    █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  ",
        "    █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  ",
        "    █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  ",
        "    █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  ",
        "    █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █  ",
        "    █  █  █  █  █  █  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  █  █  █  █  █  █  ",
        "    █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ",
        "    █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ",
        "    █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ",
        "    █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ",
        "    █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  █  ",
        "    ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  ",
    ]
    for i, frame in enumerate(frames):
        color = [CYAN, BLUE, MAGENTA, YELLOW, GREEN, RED][i % 6]
        sys.stdout.write(f"\r{color}{frame}{RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
    sys.stdout.write("\n")

def print_with_glitch(text, color=WHITE):
    glitch_chars = "!@#$%^&*()_+-=[]{}|;':\",./<>?`~"
    for i, char in enumerate(text):
        if random.random() < 0.03 and char != ' ':
            sys.stdout.write(f"{RED}{random.choice(glitch_chars)}{RESET}")
            sys.stdout.flush()
            time.sleep(0.01)
            sys.stdout.write(f"\r{color}{text[:i+1]}{RESET}")
        else:
            sys.stdout.write(f"{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.02)
    sys.stdout.write("\n")

def main():
    # Clear screen
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()
    
    # Print the recursive frame
    print(f"{CYAN}{WOODY_ASCII}{RESET}")
    time.sleep(0.5)
    
    # Animate glasses
    print(f"\n{MAGENTA}Initializing neurotic subsystem...{RESET}\n")
    animate_glasses()
    
    # Random neurotic thought
    thought = random.choice(NEUROTIC_THOUGHTS)
    print(f"{YELLOW}[Inner Monologue: {ITALIC}{thought}{RESET}{YELLOW}]{RESET}\n")
    time.sleep(0.8)
    
    # Print quote with typewriter effect
    print(f"{BOLD}{CYAN}┌{'─' * 70}┐{RESET}")
    print(f"{BOLD}{CYAN}│{RESET} {BOLD}{WHITE}WOODY ALLEN QUOTE GENERATOR v3.14159{RESET} {' ' * 31}{BOLD}{CYAN}│{RESET}")
    print(f"{BOLD}{CYAN}├{'─' * 70}┤{RESET}")
    
    for i, line in enumerate(WOODY_LINES):
        color = [YELLOW, GREEN, CYAN][i % 3]
        prefix = f"{BOLD}{CYAN}│{RESET} {color}»{RESET} "
        sys.stdout.write(prefix)
        sys.stdout.flush()
        typewriter_print(line, delay=0.04, color=color, end='')
        padding = ' ' * (68 - len(prefix) - len(line))
        print(f"{padding}{BOLD}{CYAN}│{RESET}")
        time.sleep(0.3)
    
    print(f"{BOLD}{CYAN}└{'─' * 70}┘{RESET}\n")
    
    # Existential footer
    time.sleep(0.5)
    footers = [
        f"{GRAY}* Quote generated while worrying about mortality {RESET}",
        f"{GRAY}* No neurons were harmed in the making of this output {RESET}",
        f"{GRAY}* If you're reading this, you're not dead yet. Congratulations. {RESET}",
    ]
    for footer in footers:
        typewriter_print(footer, delay=0.015, color=GRAY)
        time.sleep(0.2)
    
    # Final neurotic sign-off
    print()
    signoffs = [
        "Anyway, I have a 3 PM appointment with my analyst. And a 4 PM existential crisis.",
        "I'd stay and chat, but I think I left the iron on. Or was it the oven? Both?",
        "Excuse me, I need to go check if the front door is locked. For the 17th time.",
    ]
    signoff = random.choice(signoffs)
    typewriter_print(f"{ITALIC}{MAGENTA}{signoff}{RESET}", delay=0.025)
    
    # Blinking cursor effect at end
    for _ in range(6):
        sys.stdout.write(f"{BLINK}{GRAY}_ {RESET}")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f"\r{RESET}  ")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Interrupted. Just like my therapy sessions.{RESET}")
        sys.exit(0)