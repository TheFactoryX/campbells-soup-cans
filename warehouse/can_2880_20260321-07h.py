"""
Campbell's Soup Can #2880
Produced: 2026-03-21 07:03:38
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI escape codes for colors and effects
RESET = "\033[0m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"

# Woody Allen's neurotic color palette
COLORS = {
    'existential_dread': '\033[38;5;124m',   # Deep red
    'neurotic': '\033[38;5;208m',           # Orange
    'self_deprecating': '\033[38;5;220m',   # Yellow
    'absurdist': '\033[38;5;45m',           # Cyan
    'intellectual': '\033[38;5;141m'        # Purple
}

def clear_screen():
    """Clear terminal screen with a dramatic effect"""
    print("\n" * 50)

def typewriter(text, color, speed=0.04, jitter=0.01):
    """Typewriter effect with Woody Allen's signature hesitation"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(speed + random.uniform(-jitter, jitter*2))
        if char in ',.!?;:':
            time.sleep(0.1)  # Pause at punctuation like he's thinking

def existential_spiral():
    """Animated existential spiral using ASCII"""
    spiral = [
        "        *",
        "      *   *",
        "    *       *",
        "  *           *",
        " *             *",
        "*               *",
        " *             *",
        "  *           *",
        "    *       *",
        "      *   *",
        "        *"
    ]
    
    for i in range(3):
        for frame in spiral:
            print(f"\r{COLORS['existential_dread']}{frame}{RESET}", end="")
            time.sleep(0.05)
        print("\r" + " " * 30, end="\r")

def philosophical_critic():
    """A pretentious critic's commentary in the margin"""
    criticisms = [
        "A tad derivative of Kierkegaard...",
        "He's really hitting his neurotic stride here...",
        "I've heard better anxiety at my dentist's...",
        "Themozart would be proud... or horrified...",
        "This quote needs more clarinet..."
    ]
    return random.choice(criticisms)

def main():
    clear_screen()
    
    # Build the philosophical presentation
    print(f"{BOLD}{COLORS['neurotic']}╔" + "═" * 68 + "╗" + RESET)
    
    # Header with Woody's signature anxiety
    header = "WOODY ALLEN'S GUIDE TO EXISTENTIAL DESPAIR"
    print(f"{BOLD}{COLORS['intellectual']}║ {header:^66} ║{RESET}")
    print(f"{BOLD}{COLORS['neurotic']}╚" + "═" * 68 + "╝" + RESET)
    print()
    
    # Animated spiral
    existential_spiral()
    print()
    
    # The actual quote (I made this up but it sounds like him)
    quote = (
        "I don't fear death. I just feel it's terribly rude to arrive "
        "unannounced, especially when I'm in the middle of something "
        "important. Like worrying. Or reorganizing my books by color "
        "instead of by subject, which is clearly more logical anyway. "
        "The universe is meaningless, but my apartment is not. Yet."
    )
    
    # Print with dramatic pauses
    typewriter(quote, COLORS['self_deprecating'])
    print("\n")
    
    # Add the critic's footnote
    time.sleep(0.5)
    critic = philosophical_critic()
    print(f"{ITALIC}{COLORS['absurdist']}    -- Anon. Existential Critic, probably overthinking this{RESET}")
    print(f"{ITALIC}{COLORS['existential_dread']}    {critic}{RESET}")
    print()
    
    # Dramatic footer
    time.sleep(1)
    footer = "Thus spoke the neurotic. Now go worry about something else."
    print(f"{BOLD}{COLORS['neurotic']}    {footer}{RESET}")
    
    # Final existential shrug
    time.sleep(2)
    shrug = "¯\\_(ツ)_/¯"
    print(f"\n{COLORS['intellectual']}{shrug:^80}{RESET}")
    
    # Keep the quote on screen until user is done being depressed
    time.sleep(3)
    print(f"\n{COLORS['existential_dread']}{ITALIC}Press Enter to continue feeling existentially unsettled...{RESET}")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{COLORS['neurotic']}Of course you'd interrupt. Typical.{RESET}")