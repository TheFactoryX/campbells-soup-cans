"""
Campbell's Soup Can #2668
Produced: 2026-03-09 19:52:27
Worker: StepFun: Step 3.5 Flash (stepfun/step-3.5-flash)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

# ANSI color codes
COLORS = {
    'reset': '\033[0m',
    'bold': '\033[1m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bg_black': '\033[40m',
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue': '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan': '\033[46m',
    'bg_white': '\033[47m',
}

# Woody Allen style quotes collection (original ones!)
WOODY_QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "I took a test in Existentialism. I left all the answers blank and got a 100.",
    "I'm not against religion, but I think it's a crutch for people who are afraid of the dark.",
    "My one regret in life is that I'm not a twin. I could have had a spare me.",
    "I don't believe in the after life, but I'm going to take a change of underwear just in case.",
    "What a world. Here I am suffering for my art, and nobody even cares.",
    "I'm not neurotic, I'm just a sensitive person with a very active imagination.",
    "If my film makes one person feel less alone, then it's a success. If it makes two people feel less alone, then it's a blockbuster."
]

def slow_print(text, color='white', delay=0.03, end='\n'):
    """Print text with typing animation"""
    sys.stdout.write(COLORS[color])
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    sys.stdout.write(COLORS['reset'] + end)
    sys.stdout.flush()

def draw_wave(rows=5, width=50):
    """Draw a simple ASCII wave"""
    wave = []
    for i in range(rows):
        line = []
        for j in range(width):
            # Create wave pattern
            if abs((j + i * 4) % 20 - 10) < 3:
                line.append('~')
            else:
                line.append(' ')
        wave.append(''.join(line))
    return wave

def main():
    # Clear screen and move cursor home
    print('\033[2J\033[H', end='')
    
    # Draw colorful header
    header = "  WOODY ALLEN PHILOSOPHY DIVISION  ".center(60, '≡')
    slow_print(header, 'cyan', 0.01)
    time.sleep(0.5)
    
    # Draw wavy separator
    for line in draw_wave(3, 60):
        slow_print(line, 'blue', 0.002)
    
    # Select random quote
    quote = random.choice(WOODY_QUOTES)
    
    # Create decorative box
    box_width = 58
    horizontal = '━'
    vertical = '┃'
    corners = ['┏', '┓', '┗', '┛']
    
    # Animate box drawing
    slow_print(corners[0] + horizontal * (box_width-2) + corners[1], 'yellow', 0.005)
    time.sleep(0.2)
    
    # Split quote into lines (simple wrapping)
    words = quote.split()
    lines = []
    current_line = []
    for word in words:
        if sum(len(w) for w in current_line) + len(word) + len(current_line) <= box_width - 6:
            current_line.append(word)
        else:
            lines.append(' '.join(current_line))
            current_line = [word]
    if current_line:
        lines.append(' '.join(current_line))
    
    # Print quote with alternating colors
    colors = ['white', 'green', 'magenta', 'cyan']
    for i, line in enumerate(lines):
        colored_line = f"{vertical} {line.center(box_width-4)} {vertical}"
        slow_print(colored_line, colors[i % len(colors)], 0.02)
        time.sleep(0.1)
    
    time.sleep(0.3)
    
    # Print signature
    sig = f"{vertical}{'─' * (box_width-2)}{vertical}"
    slow_print(sig, 'yellow', 0.01)
    slow_print(corners[2] + horizontal * (box_width-2) + corners[3], 'yellow', 0.005)
    
    # Animated signature
    slow_print("\n   - Woody Allen (probably)", 'red', 0.05)
    time.sleep(0.5)
    
    # Final wave animation
    for line in draw_wave(4, 60):
        slow_print(line, 'blue', 0.002)
    
    # Blinking cursor effect
    for _ in range(3):
        sys.stdout.write('\033[?25l')  # Hide cursor
        slow_print("\n" + " " * 30 + "💡", 'yellow', 0.1)
        time.sleep(0.3)
        sys.stdout.write('\033[K')  # Clear line
        time.sleep(0.1)
    
    sys.stdout.write('\033[?25h')  # Show cursor
    print("\n" + "=" * 60)
    slow_print("Remember: Existential dread is just anxiety with a better vocabulary.", 'magenta', 0.03)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + COLORS['red'] + "Philosophy interrupted. How very Zen of you." + COLORS['reset'])
        sys.exit(0)