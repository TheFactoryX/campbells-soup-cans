"""
Campbell's Soup Can #2724
Produced: 2026-03-12 16:15:46
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen's Existential Doodles
A neurotic philosophical experience in 4K (not really)
"""

import time
import sys
import random
import os

# Clear screen and hide cursor
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.write("\033[?25l")

# ANSI color palettes
NEUROTIC = {
    'anxiety': '\033[38;5;226m',     # Nervous yellow
    'existential': '\033[38;5;147m', # Pale existential blue
    'self_deprecating': '\033[38;5;173m', # Self-deprecating pink
    'reset': '\033[0m',
    'bold': '\033[1m',
    'blink': '\033[5m'
}

# Woody Allen's brain under stress
def existential_doodle():
    quotes = [
        "I don't want to achieve immortality through my work. I want to achieve it through not dying.",
        "I'm not afraid of death; I just don't want to be there when it happens. It's not that I'm cowardly, I just find the whole process messy and poorly organized.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. But on the plus side, the appetizers are decent.",
        "I'm not an optimist. I'm a realist. And reality is mostly bad. But I'm not a pessimist either. I'm a neurotic. I worry about everything, including the fact that I'm not worrying enough.",
        "What if nothing exists and we're all just figments of someone's imagination? And what if that someone is me? Then I'm really in trouble because I can't even manage my own life, let alone everybody else's.",
        "Eternal nothingness is fine with me. I just don't want to be present when it happens. It's the ultimate 'I told you so' moment, and I'm not ready for that level of vindication.",
        "I don't believe in the afterlife, but I'm taking a change of underwear just in case. You can never be too careful about the cosmic dry cleaning.",
    ]
    
    return random.choice(quotes)

# ASCII art of Woody's face in crisis
def woody_with_issues():
    return r"""
         _____
        /     \
       |  O O  |
       |   ∆   |
       |  ~~~  |
        \_____/
         |   |
         |   |
        /____\
    """

# Typewriter effect with neurotic jitters
def type_with_anxiety(text, color, speed=0.03, jitter=0.01):
    for i, char in enumerate(text):
        if char == ' ':
            sys.stdout.write(char)
        else:
            sys.stdout.write(color + char + NEUROTIC['reset'])
            sys.stdout.flush()
            # Random pauses like Woody's nervous tics
            time.sleep(speed + random.uniform(-jitter, jitter*2))
            # Occasionally overthink a comma
            if char in ['.', ',', ';'] and random.random() < 0.3:
                time.sleep(0.1)

# Create a wobbly box
def neurotic_border(width):
    border = ""
    for i in range(width):
        if i == 0 or i == width-1:
            border += "+"
        elif random.random() < 0.2:  # Hand tremor effect
            border += "-~"[random.randint(0,1)]
        else:
            border += "-"
    return border

# Main performance
def main():
    quote = existential_doodle()
    
    # Print Woody's troubled face
    print(NEUROTIC['existential'] + woody_with_issues() + NEUROTIC['reset'])
    time.sleep(0.5)
    
    # Calculate box dimensions
    max_width = min(80, os.get_terminal_size().columns - 4)
    lines = []
    current_line = ""
    
    # Word wrap with existential dread
    for word in quote.split():
        if len(current_line) + len(word) + 1 <= max_width - 4:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    lines.append(current_line.strip())
    
    box_width = max(len(line) for line in lines) + 4
    
    # Print with trembling precision
    print()
    time.sleep(0.3)
    
    # Top border (slightly crooked)
    top = neurotic_border(box_width)
    print(NEUROTIC['anxiety'] + top + NEUROTIC['reset'])
    time.sleep(0.2)
    
    # Quote lines with self-deprecating colors
    for i, line in enumerate(lines):
        padding = (box_width - 2 - len(line)) // 2
        extra = (box_width - 2 - len(line)) % 2
        
        sys.stdout.write(NEUROTIC['self_deprecating'] + "|" + NEUROTIC['reset'])
        sys.stdout.write(" " * (padding + (0 if i % 2 == 0 else 1)))
        
        # Alternate colors for each line (mood swings)
        line_color = NEUROTIC['anxiety'] if i % 2 == 0 else NEUROTIC['existential']
        type_with_anxiety(line, line_color)
        
        sys.stdout.write(" " * (padding + (1 if i % 2 == 0 else 0)))
        print(NEUROTIC['self_deprecating'] + "|" + NEUROTIC['reset'])
        time.sleep(0.1)
    
    # Bottom border (giving up halfway)
    bottom = neurotic_border(box_width)
    print(NEUROTIC['anxiety'] + bottom + NEUROTIC['reset'])
    
    #Signature existential footnote
    time.sleep(0.5)
    footnote = "— Probably not helpful, but there it is."
    sys.stdout.write("\n" + " " * ((box_width - len(footnote)) // 2))
    type_with_anxiety(footnote, NEUROTIC['existential'], 0.02)
    print("\n")
    
    # Restore cursor
    sys.stdout.write("\033[?25h")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h\n")
        print("\nSee? I knew you'd leave me. It's fine. Really.")
        sys.exit(0)