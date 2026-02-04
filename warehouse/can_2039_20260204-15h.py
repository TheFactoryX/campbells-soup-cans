"""
Campbell's Soup Can #2039
Produced: 2026-02-04 15:01:07
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI escape codes for colors
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"

# Woody Allen's style quote - I made this one up!
quote = """I'm not an existentialist. I'm just a man who keeps expecting
the universe to acknowledge his existence, but it keeps
forgetting to put it in its address book. 
I called again today - they said I wasn't on the list."""

def typewriter(text, color=WHITE, delay=0.03, jitter=False):
    """Print text with typewriter effect and optional random jitter."""
    for char in text:
        if jitter and char != ' ' and char != '\n':
            time.sleep(delay + random.uniform(-0.01, 0.01))
        else:
            time.sleep(delay)
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()

def spinning_cursor():
    """Animated spinning cursor."""
    while True:
        for cursor in '|/-\\':
            yield cursor

def main():
    # Clear screen and move cursor to home
    sys.stdout.write("\033[2J\033[H")
    
    spinner = spinning_cursor()
    
    # Philosophical preamble with animation
    print(BG_BLACK + WHITE + "="*50 + RESET)
    print(BG_BLACK + WHITE + " WOODY ALLEN'S DEEP THOUGHTS (VOL. 47) " + RESET)
    print(BG_BLACK + WHITE + "="*50 + RESET)
    print()
    
    # Loading animation
    print(YELLOW + "Consulting the void...", end=' ')
    for _ in range(15):
        sys.stdout.write(next(spinner))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print("found it!" + RESET)
    print()
    
    # Print the quote with fancy formatting
    lines = quote.split('\n')
    max_len = max(len(line) for line in lines)
    
    # Top border with animated color
    top_border = BG_MAGENTA + WHITE + "▄" * (max_len + 6) + RESET
    print(top_border)
    
    # Quote lines with alternating colors and typewriter effect
    colors = [CYAN, GREEN, YELLOW, BLUE]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        padding = (max_len - len(line)) // 2
        
        # Animated left border
        left_border = MAGENTA + "█" + RESET
        sys.stdout.write(left_border)
        
        # Typewriter effect for the line
        typewriter(" " * padding + line, BOLD + color, 0.02, jitter=True)
        
        # Animated right border
        sys.stdout.write(" " * (max_len - len(line) - padding))
        sys.stdout.write(RESET + MAGENTA + " █" + RESET)
        print()
    
    # Bottom border
    print(top_border)
    print()
    
    # Woody Allen-esque commentary
    time.sleep(0.5)
    print(RED + BOLD + "— Woody Allen, probably" + RESET)
    print()
    
    # Philosophical footer with blinking effect
    footer = "Note: This profound insight brought to you by insomnia and a questionable diet"
    print(BG_BLUE + WHITE, end='')
    for char in footer:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print(RESET)
    print()
    
    # Final dramatic pause with random existential emoji
    emojis = ["🤔", "😵‍💫", "🫠", "🙃", "🌀"]
    print(WHITE + "Contemplating the abyss... " + random.choice(emojis) * 3 + RESET)
    time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + RED + "Existential crisis interrupted. How appropriate." + RESET)