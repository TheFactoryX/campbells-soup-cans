"""
Campbell's Soup Can #2423
Produced: 2026-02-25 09:08:01
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

# ANSI color codes
CYAN = '\033[96m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RED = '\033[91m'
MAGENTA = '\033[95m'
BLUE = '\033[94m'
RESET = '\033[0m'
BOLD = '\033[1m'

# Woody Allen style quotes (original creations)
quotes = [
    "I'm not an existentialist. I'm just a man standing in the middle of a cosmic joke, wondering if the punchline is coming or if I'm the punchline.",
    "I spend half my life searching for meaning, and the other half looking for my keys. The universe and I have something in common: we both make me late.",
    "They say love is the answer. But what if the question is 'why is there no shampoo in my hotel room?'",
    "I'm not afraid of death; I just don't want to be there when it happens. Also, I hear the Wi-Fi is terrible in the afterlife.",
    "My therapist told me the way to achieve enlightenment is to live in the present. But my phone battery is at 3% and I need to know if anyone liked my post.",
    "I tried to find the meaning of life in a fortune cookie. It said 'You will receive a lucky break.' I'm still waiting. And I'm not even Chinese.",
    "Life is like a box of chocolates: you never know what you're gonna get, and half of it is stuff you'd never choose, and also it gives you a stomachache.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying. But since that's not an option, I'll settle for being the guy who asked too many questions at parties."
]

def typewriter(text, color=YELLOW, delay=0.03, end='\n'):
    """Print text with typewriter effect"""
    for char in text:
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.7, 1.3))
    print(end=end)

def animate_thought_bubble():
    """Animate a bouncing thought bubble"""
    bubble = [
        "   o   ",
        "  o o  ",
        " o   o ",
        "o  .  o",
        " o   o ",
        "  o o  ",
        "   o   "
    ]
    
    for _ in range(3):
        for i in range(len(bubble)):
            sys.stdout.write('\r' + CYAN + ' ' * 20 + bubble[i] + RESET)
            sys.stdout.flush()
            time.sleep(0.1)
        # Reverse
        for i in range(len(bubble)-2, -1, -1):
            sys.stdout.write('\r' + CYAN + ' ' * 20 + bubble[i] + RESET)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 30 + '\n')

def draw_woody_glasses():
    """Draw Woody Allen-style glasses"""
    glasses = [
        BLUE + "   ╭━━╮     ╭━━╮" + RESET,
        BLUE + "   ┃  ┃━━┳━┳┫  ┃" + RESET,
        BLUE + "   ┃  ┃  ┃ ┃┃  ┃" + RESET,
        BLUE + "   ╰━━╯  ╰━╯╰━━╯" + RESET
    ]
    for line in glasses:
        print(' ' * 18 + line)

def main():
    # Clear screen and move cursor
    sys.stdout.write('\033[2J\033[H')
    
    # Animate bouncing thought bubble
    animate_thought_bubble()
    
    # Draw glasses
    draw_woody_glasses()
    time.sleep(0.5)
    
    # Select random quote
    quote = random.choice(quotes)
    
    # Create decorative border
    width = 70
    border = CYAN + '╔' + '═' * (width - 2) + '╗' + RESET
    empty_line = CYAN + '║' + ' ' * (width - 2) + '║' + RESET
    bottom_border = CYAN + '╚' + '═' * (width - 2) '╝' + RESET
    
    # Print header with animation
    print('\n')
    typewriter("  WOODY ALLEN'S PHILOSOPHICAL MOMENT", CYAN, 0.05, end='\n\n')
    
    # Print border
    print(border)
    print(empty_line)
    
    # Print quote with centered formatting
    words = quote.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width - 10:
            current_line.append(word)
            current_length += len(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print each line with typewriter effect
    for line in lines:
        padding = (width - 4 - len(line)) // 2
        extra = (width - 4 - len(line)) % 2
        print(CYAN + '║ ' + RESET + ' ' * (padding + extra) + YELLOW, end='')
        typewriter(line, YELLOW, 0.02, end='')
        print(RESET + CYAN + ' ' * padding + ' ║' + RESET)
        time.sleep(0.1)
    
    # Print border again
    print(empty_line)
    print(bottom_border)
    
    # Add Woody Allen signature with animation
    time.sleep(0.5)
    print('\n' + ' ' * 20 + GREEN + BOLD, end='')
    typewriter("- Woody Allen (probably)", GREEN, 0.04)
    print(RESET)
    
    # Add playful footer
    time.sleep(1)
    print('\n' + MAGENTA + '  [This quote has been neurotically optimized for your existential dread]' + RESET)
    print(BLUE + '  [Press any key to continue feeling vaguely dissatisfied...]' + RESET)
    
    # Wait for key press
    try:
        sys.stdin.read(1)
    except KeyboardInterrupt:
        pass
    
    # Clear and exit with style
    sys.stdout.write('\033[2J\033[H')
    print(CYAN + '\n  Remember: Nothing is so serious that it can\'t be made' + RESET)
    print(CYAN + '  slightly amusing through excessive overthinking.\n' + RESET)
    print(GREEN + '  🎭 The show must go on. Probably.' + RESET)

if __name__ == "__main__":
    main()