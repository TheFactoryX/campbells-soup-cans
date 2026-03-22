"""
Campbell's Soup Can #2906
Produced: 2026-03-22 13:14:11
Worker: Free Models Router (openrouter/free)
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

# Woody Allen style quotes
WOODY_QUOTES = [
    "I'm not afraid of death; I just don't want to be there when it happens.",
    "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
    "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
    "What a wonderful world. It's so beautiful. If they gave me a choice between immortality and a cheese sandwich, I'd probably take the cheese sandwich.",
    "I don't believe in an afterlife, but I'm going to take some underwear with me, just in case.",
    "My problem is that I'm more interested in the present than the future. The future doesn't exist. The present is all we have. That's why I'm always late.",
    "I'm not against the police. I'm just afraid of them.",
    "I think crime pays. There's no government program that pays as well.",
    "I'm at the age where I want to be with people I really like, and I'm running out of people I really like."
]

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quote = random.choice(WOODY_QUOTES)
        self.colors = {
            'cyan': '\033[96m',
            'yellow': '\033[93m',
            'green': '\033[92m',
            'red': '\033[91m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'bold': '\033[1m',
            'dim': '\033[2m',
            'reset': '\033[0m'
        }
    
    def clear_screen(self):
        """Clear the terminal screen."""
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
    
    def print_animated(self, text, delay=0.03, color='cyan'):
        """Print text with typewriter effect."""
        colored_text = self.colors[color] + text + self.colors['reset']
        for char in colored_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write('\n')
        sys.stdout.flush()
    
    def print_boxed(self, text, width=60, border_color='cyan', text_color='yellow'):
        """Print text in a fancy box."""
        lines = []
        words = text.split()
        current_line = []
        
        # Wrap text
        for word in words:
            if sum(len(w) for w in current_line) + len(current_line) + len(word) <= width - 4:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))
        
        # Print box
        top_bottom = border_color + '╔' + '═' * (width - 2) + '╗' + self.colors['reset']
        middle = border_color + '║' + self.colors['reset'] + ' {} ' + border_color + '║' + self.colors['reset']
        empty = border_color + '║' + ' ' * (width - 2) + '║' + self.colors['reset']
        
        print(top_bottom)
        print(empty)
        
        for line in lines:
            padded_line = line.ljust(width - 4)
            print(middle.format(self.colors[text_color] + padded_line + self.colors['reset']))
        
        print(empty)
        print(border_color + '╚' + '═' * (width - 2) + '╝' + self.colors['reset'])
    
    def print_neurotic_disclaimer(self):
        """Print a funny disclaimer in Woody Allen style."""
        disclaimer = [
            "DISCLAIMER: This quote is presented with",
            "neurotic precision and existential dread.",
            "No philosophers were harmed in the making",
            "of this display, though several may have",
            "contemplated suicide upon reading it.",
            "Results may vary. Void where prohibited.",
            "Consult your existential therapist before",
            "applying to daily life."
        ]
        
        print()
        for line in disclaimer:
            self.print_animated(line, delay=0.01, color='dim')
            time.sleep(0.1)
        print()
    
    def draw_woody_face(self):
        """Draw a simple ASCII Woody Allen face."""
        face = [
            "          .--.",
            "         |o_o |",
            "         |:_/ |",
            "        //   \\ \\",
            "       (|     | )",
            "      /'\\_   _/`\\",
            "     \\___)=(___/"
        ]
        
        for line in face:
            print(self.colors['magenta'] + line + self.colors['reset'])
    
    def perform(self):
        """Main performance."""
        self.clear_screen()
        
        # Draw Woody's face
        self.draw_woody_face()
        print()
        
        # Dramatic pause
        time.sleep(1)
        
        # Print setup
        self.print_animated("And now, a moment of philosophical clarity...", delay=0.05, color='dim')
        time.sleep(0.5)
        
        # Print the actual quote in a box
        self.print_boxed(self.quote, width=70, border_color='cyan', text_color='yellow')
        print()
        
        # Print disclaimer
        self.print_neurotic_disclaimer()
        
        # Final touch
        time.sleep(0.5)
        self.print_animated("Remember: existence is pain, but at least it's *your* pain.", 
                           delay=0.04, color='green')
        print()
        time.sleep(0.3)
        self.print_animated("Now go forth and be mildly anxious about everything!", 
                           delay=0.03, color='red')

if __name__ == "__main__":
    philosopher = WoodyAllenPhilosopher()
    philosopher.perform()