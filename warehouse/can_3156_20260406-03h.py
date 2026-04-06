"""
Campbell's Soup Can #3156
Produced: 2026-04-06 03:41:38
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

def slow_print(text, delay=0.03, color='\033[36m'):
    """Prints text with a typewriter effect"""
    reset = '\033[0m'
    for char in text:
        sys.stdout.write(f"{color}{char}{reset}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()

def flicker_text(text, iterations=3):
    """Makes text flicker like a broken neon sign"""
    colors = ['\033[31m', '\033[33m', '\033[37m', '\033[0m']
    for _ in range(iterations):
        for i in range(len(text)):
            sys.stdout.write('\033[F\033[K')  # Move up and clear line
            color = random.choice(colors)
            flicker = ''.join(random.choice(['', '\033[7m']) + char for char in text[:i+1])
            sys.stdout.write(f"{color}{flicker}")
            sys.stdout.flush()
            time.sleep(0.05)
    print('\n' + '\033[0m')

def main():
    # Woody Allen's existential dread meets ASCII art
    quote = "I don't want to achieve immortality through my work. " \
            "I want to achieve it through not dying. " \
            "It's my favorite way to achieve immortality."
    
    # Clear screen and create dramatic tension
    sys.stdout.write('\033[2J\033[H')
    
    # Build Woody's neurotic rabbit hole
    rabbit_hole = [
        "    ╭───────────────────────────────────────╮",
        "    │   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  │",
        "    │  █                             █   │",
        "    │ █   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█  │",
        "    │ █   █                   █   █    │",
        "    │  █   █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█   █  │",
        "    │   █   █               █   █    │",
        "    │    █   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   █  │",
        "    │     █   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    █ │",
        "    │      █   █               █   █  │",
        "    │       █   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█   █ │",
        "    │        █   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█    │",
        "    │         █   █               █   █ │",
        "    │          █   ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█    │",
        "    │           █                       █ │",
        "    │            ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀  │",
        "    │                                    │",
        "    ╰───────────────────────────────────────╯"
    ]
    
    # Animate the rabbit hole descending
    for i in range(len(rabbit_hole) + 5):
        sys.stdout.write('\033[F\033[K' * 20)  # Clear multiple lines
        for line in rabbit_hole[max(0, i-4):i]:
            print(f"\033[90m{line}\033[0m")
        time.sleep(0.08)
    
    time.sleep(0.5)
    
    # Dramatic pause before quote appears
    print("\n" + " " * 30 + "\033[33m...and then I realized...\033[0m\n")
    time.sleep(1.2)
    
    # The quote appears with neurotic typewriter effect
    slow_print(quote.rstrip(), delay=0.04, color='\033[37m')
    time.sleep(0.8)
    
    # Add Woody's signature existential sigh
    sigh = "\033[3m\033[90m(sigh)\033[0m"
    print(" " * 50 + sigh)
    time.sleep(0.5)
    
    # Flickering enlightenment
    flicker_text("EXISTENTIAL DREAD? CHECK.", iterations=2)
    time.sleep(0.3)
    
    # Final neurotic punctuation
    punctuation = random.choice(['?!', '...', '!?', '...?!'])
    print(" " * 60 + f"\033[31m{punctuation}\033[0m\n")
    
    # Add a little Woody Allen existential footer
    time.sleep(0.7)
    footer = "\033[2m\033[90m~ from the mind of someone who overthought this ~\033[0m"
    print(footer.center(80))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n\033[31m↳  I knew you'd interrupt me. Typical.\033[0m")
        sys.exit(0)