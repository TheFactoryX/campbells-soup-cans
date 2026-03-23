"""
Campbell's Soup Can #2919
Produced: 2026-03-23 05:47:13
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import random

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[31m',
    'green': '\033[32m',
    'yellow': '\033[33m',
    'blue': '\033[34m',
    'magenta': '\033[35m',
    'cyan': '\033[36m',
    'white': '\033[37m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def neurotic_pause(duration=0.1):
    """Simulate Woody Allen's neurotic pauses."""
    time.sleep(duration)

def typewriter(text, color='white', delay=0.03, end='\n'):
    """Print text with typewriter effect and color."""
    sys.stdout.write(COLORS[color])
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    sys.stdout.write(COLORS['reset'] + end)
    sys.stdout.flush()

def draw_woody_allen():
    """Draw a simple Woody Allen ASCII portrait."""
    portrait = [
        "          .-'''-.        ",
        "         /       \\       ",
        "        |         |      ",
        "        |   O O   |      ",
        "        |    ^    |      ",
        "         \\  '''  /       ",
        "          '-___-'        ",
        "           |   |         ",
        "           |   |         ",
        "          /     \\        ",
        "         /       \\       ",
        "        /         \\      ",
        "       /           \\     ",
        "      /             \\    ",
        "     /               \\   ",
        "    /                 \\  ",
        "   /                   \\ ",
        "  /                     \\",
    ]
    for line in portrait:
        print(COLORS['bg_black'] + COLORS['white'] + line + COLORS['reset'])

def existential_crisis_animation():
    """Animate existential crisis with floating questions."""
    questions = ["Why?", "What if?", "But what does it MEAN?", "Seriously, why?"]
    for _ in range(10):
        for q in questions:
            sys.stdout.write('\033[2K\033[G')  # Clear line and move to start
            sys.stdout.write(COLORS['magenta'] + q + COLORS['reset'])
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\033[2K\033[G')  # Clear final question

def main():
    clear_screen()
    
    # Animate existential crisis
    existential_crisis_animation()
    print()
    neurotic_pause(0.5)
    
    # Draw Woody Allen
    draw_woody_allen()
    print()
    neurotic_pause(0.5)
    
    # Print the philosophical quote with dramatic formatting
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens.\n"
        "Life is like a box of chocolates - except the chocolates are all\n"
        "bitter, the box is empty, and someone keeps moving the furniture."
    )
    
    # Create fancy border
    border = COLORS['cyan'] + "═" * 60 + COLORS['reset']
    print(border)
    print(COLORS['yellow'] + "║" + COLORS['reset'] + quote.center(58) + COLORS['yellow'] + "║" + COLORS['reset'])
    print(border)
    print()
    neurotic_pause(0.8)
    
    # Typewriter effect with color changes
    typewriter("Woody Allen's", color='magenta', delay=0.08)
    typewriter("Philosophical", color='red', delay=0.08)
    typewriter("Insights™", color='green', delay=0.08)
    print()
    neurotic_pause(0.5)
    
    # Print the main quote with dramatic pauses
    sentences = [
        "I'm not afraid of death;",
        "I just don't want to be there when it happens.",
        "",
        "The universe is infinite and meaningless,",
        "which I would find comforting",
        "if I weren't so afraid of the dark.",
        "",
        "And my therapist says I have",
        "a fear of commitment...",
        "to anything other than anxiety."
    ]
    
    for i, sentence in enumerate(sentences):
        if sentence == "":
            print()
            neurotic_pause(0.3)
        else:
            # Alternate colors for dramatic effect
            color = 'white' if i % 3 == 0 else 'yellow' if i % 3 == 1 else 'cyan'
            typewriter("  " + sentence, color=color, delay=0.04)
            neurotic_pause(0.2)
    
    print()
    neurotic_pause(0.5)
    
    # Final dramatic flourish
    print(COLORS['bg_red'] + COLORS['white'] + " ⚠️  ZEN MASTER? MORE LIKE ZEN DISASTER!  ⚠️ " + COLORS['reset'])
    print()
    
    # Rolling credits
    credits = [
        "Written by: Woody Allen's Anxiety",
        "Directed by: Overthinking Productions",
        "Starring: Existential Dread (as himself)",
        "Special Thanks: My Mother (for the guilt)",
        "                                     ",
        "No philosophers were harmed in the making of this quote,",
        "though several are now in therapy because of it."
    ]
    
    print(COLORS['blue'] + "─" * 60 + COLORS['reset'])
    for credit in credits:
        print(COLORS['dim'] + credit.center(60) + COLORS['reset'])
        time.sleep(0.1)
    print(COLORS['blue'] + "─" * 60 + COLORS['reset'])
    
    neurotic_pause(1)
    typewriter("\nRemember: The unexamined life is not worth living,",
               color='green', delay=0.03)
    typewriter("but the over-examined life is exhausting and probably",
               color='green', delay=0.03)
    typewriter("won't get you a table at that trendy restaurant.",
               color='green', delay=0.03)
    print()
    neurotic_pause(0.5)
    typewriter("Now go ponder your existence. Or take a nap. Nap sounds good.",
               color='magenta', delay=0.02)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + COLORS['red'] + "Fine! Be that way! I wasn't going to say anything profound anyway!" + COLORS['reset'])
        sys.exit(0)