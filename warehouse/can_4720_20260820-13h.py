"""
Campbell's Soup Can #4720
Produced: 2026-08-20 13:11:10
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
    print_whimsical_quote()

def print_whimsical_quote():
    quote = "I'm not afraid of death, I just don't want to be there when it happens - unless it's a really good movie."
    words = quote.split()
    
    colors = [
        '\x1b[31m',  # Red
        '\x1b[33m',  # Yellow
        '\x1b[32m',  # Green
        '\x1b[34m',  # Blue
        '\x1b[35m',  # Magenta
        '\x1b[36m'   # Cyan
    ]
    reset = '\x1b[0m'
    
    colored_words = []
    for idx, word in enumerate(words):
        color = colors[idx % len(colors)]
        colored_words.append(f"{color}{word}{reset}")
    
    colored_line = ' '.join(colored_words)
    quote_line = ' '.join(words)
    border_line = '+' + '-'*len(quote_line) + '+'
    
    def animate_line(line):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
    
    # Animate top border
    animate_line(border_line)
    print()
    
    # Animate content
    content_line = f"|{colored_line}|"
    animate_line(content_line)
    print()
    
    # Animate bottom border
    animate_line(border_line)
    print()

if __name__ == "__main__":
    main()