"""
Campbell's Soup Can #1393
Produced: 2026-01-04 19:27:35
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import sys
import time
from itertools import cycle

class WoodyAllenQuote:
    def __init__(self):
        # ANSI color codes
        self.colors = {
            'reset': '\033[0m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bright': '\033[1m'
        }
        
        # The quote
        self.quote = (
            "I spend so much time worrying about the meaning of life, "
            "I've forgotten to actually live it. Then again, if I lived it, "
            "I'd probably just spend that time worrying about what I did wrong."
        )
        
        # Decorative elements
        self.top_border = "╔═══════════════════════════════════════════════════════════════════════════════════════════════════╗"
        self.bottom_border = "╚═══════════════════════════════════════════════════════════════════════════════════════════════════╝"
        self.side_border = "║"
        
        # Color cycle for animation
        self.color_cycle = cycle([
            self.colors['red'],
            self.colors['green'],
            self.colors['yellow'],
            self.colors['blue'],
            self.colors['magenta'],
            self.colors['cyan']
        ])
        
    def print_colored(self, text, color):
        """Print text with specified color"""
        print(f"{color}{text}{self.colors['reset']}", end='')
        
    def print_framed_quote(self):
        """Print the quote with ASCII art frame and color animation"""
        # Print top border
        self.print_colored(self.top_border + "\n", self.colors['white'])
        
        # Print quote with animation
        words = self.quote.split()
        current_line = []
        line_length = 0
        max_line_length = 70
        
        for i, word in enumerate(words):
            # Add word to current line if it fits
            if line_length + len(word) + 1 <= max_line_length:
                current_line.append(word)
                line_length += len(word) + 1
            else:
                # Print current line
                line = " ".join(current_line)
                padding = max_line_length - len(line)
                self.print_colored(self.side_border, self.colors['white'])
                
                # Animate the line
                for char in line:
                    self.print_colored(char, next(self.color_cycle))
                    sys.stdout.flush()
                    time.sleep(0.03)
                
                self.print_colored(" " * padding + self.side_border + "\n", self.colors['white'])
                
                # Start new line with current word
                current_line = [word]
                line_length = len(word) + 1
        
        # Print last line
        if current_line:
            line = " ".join(current_line)
            padding = max_line_length - len(line)
            self.print_colored(self.side_border, self.colors['white'])
            
            # Animate the last line
            for char in line:
                self.print_colored(char, next(self.color_cycle))
                sys.stdout.flush()
                time.sleep(0.03)
            
            self.print_colored(" " * padding + self.side_border + "\n", self.colors['white'])
        
        # Print bottom border
        self.print_colored(self.bottom_border + "\n\n", self.colors['white'])
        
    def print_footer(self):
        """Print a Woody Allen style footer"""
        footer_text = " - Woody Allen (probably)"
        padding = (len(self.top_border) - len(footer_text) - 2) // 2
        
        self.print_colored(self.side_border, self.colors['yellow'])
        self.print_colored(" " * padding, self.colors['yellow'])
        self.print_colored(footer_text, self.colors['bright'] + self.colors['red'])
        self.print_colored(" " * padding, self.colors['yellow'])
        self.print_colored(self.side_border + "\n", self.colors['yellow'])
        
    def run(self):
        """Main function to run the quote display"""
        # Clear screen
        print("\033[H\033[J", end='')
        
        # Print title
        self.print_colored("\n\n", self.colors['reset'])
        self.print_colored(" ".center(80, " "), self.colors['bright'] + self.colors['cyan'])
        self.print_colored("WOODY ALLEN ON LIFE".center(80, " "), self.colors['bright'] + self.colors['cyan'])
        self.print_colored(" ".center(80, " "), self.colors['bright'] + self.colors['cyan'])
        self.print_colored("\n\n", self.colors['reset'])
        
        # Print the framed quote
        self.print_framed_quote()
        
        # Print footer
        self.print_footer()
        
        # Add a small Woody Allen style joke
        joke = "\n\nYou know, I told my therapist I was having suicidal thoughts. She told me from now on I have to pay in advance."
        self.print_colored(joke, self.colors['magenta'])

if __name__ == "__main__":
    woody_quote = WoodyAllenQuote()
    woody_quote.run()