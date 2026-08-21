"""
Campbell's Soup Can #4751
Produced: 2026-08-21 20:41:18
Worker: Poolside: Laguna XS 2.1 (free) (poolside/laguna-xs-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time

def main():
    # Woody Allen style quote with visual flair
    lines = [
        "The secret to life is accepting it's all terrible, then pretending to care.",
        "That way, when you die, you can say you gave it your best shot—and technically, you were right!"
    ]

    # Calculate maximum line width for display
    max_len = max(len(line) for line in lines)

    # Color palette for animated text (red, green, yellow, blue, magenta, cyan)
    colors = [
        '\033[31m',  # Red
        '\033[32m',  # Green
        '\033[33m',  # Yellow
        '\33[34m',   # Blue
        '\033[35m',  # Magenta
        '\033[36m'   # Cyan
    ]

    # Color for box borders (bright cyan)
    border_color = '\033[1;36m'  # Bold cyan
    reset_color = '\033[0m'

    # Print top border with animation
    top = border_color + '+' + '-' * (max_len + 2) + '+' + reset_color
    print(top)

    # Animate each line inside the box
    for line in lines:
        # Left border
        sys.stdout.write(border_color + '|' + reset_color + ' ')
        sys.stdout.flush()
        
        # Animate characters with color cycling
        for i, char in enumerate(line):
            color = colors[i % len(colors)]
            sys.stdout.write(color + char + reset_color)
            sys.stdout.flush()
            time.sleep(0.02)  # Typewriter delay
        
        # Fill remaining space to max length
        padding = ' ' * (max_len - len(line))
        sys.stdout.write(padding + ' ' + border_color + '|' + reset_color + '\n')
        sys.stdout.flush()
        time.sleep(0.3)  # Pause between lines

    # Print bottom border
    print(border_color + '+' + '-' * (max_len + 2) + '+' + reset_color)

    # Extra flair - ASCII art ending
    time.sleep(0.5)
    print("\n" + '\033[1;31m' + 
          "  ╔════════════════════════════════╗\n" +
          "  ║  Life is a bitch, then you die.  ║\n" +
          "  ╚════════════════════════════════╝" + 
          '\033[0m')
    time.sleep(1.5)  # Dramatic pause

if __name__ == "__main__":
    main()