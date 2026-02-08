"""
Campbell's Soup Can #2109
Produced: 2026-02-08 03:34:50
Worker: Free Models Router (openrouter/free)
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

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "I hate reality. It's the worst place to live, but unfortunately it's the only one with free parking.",
            "My only goal in life is to be as happy as my dog, but without the constant need to smell everything.",
            "I believe marriage is a wonderful institution. But who wants to live in an institution?",
            "I'm not against religion. It's just that I find it hard to believe in a God who would create a world with so many tiny, unreachable itches.",
            "My psychiatrist told me I was crazy. I said I want a second opinion. He said okay, you're ugly too.",
            "I don't want to be immortal through my work. I want to be immortal by not dying. It's the only way to be sure.",
            "I'm not afraid of death. I just don't want it to happen to me."
        ]
        
        # ANSI color codes
        self.colors = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'cyan': '\033[96m',
            'yellow': '\033[93m',
            'green': '\033[92m',
            'magenta': '\033[95m',
            'red': '\033[91m',
            'blue': '\033[94m'
        }
    
    def typewriter_effect(self, text, color='\033[93m', delay=0.03):
        """Print text with typewriter effect"""
        for char in text:
            sys.stdout.write(color + char + self.colors['reset'])
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def draw_neurotic_border(self, width):
        """Draw a wobbly, neurotic border"""
        border_chars = ['-', '~', ':', ';', '=']
        border = ''
        for i in range(width):
            # Make it wobble like Woody's anxiety
            if i % 3 == 0:
                border += random.choice(['-', '~'])
            elif i % 5 == 0:
                border += random.choice([':', ';'])
            else:
                border += random.choice(['=', '-'])
        return border
    
    def create_woody_signature(self):
        """Create Woody Allen's signature in ASCII"""
        signature = [
            "  __  __           _       ___  ___  ",
            " |  \\/  | __ _  __| |     / _ \\/ __| ",
            " | |\\/| |/ _` |/ _` |    | | | \\__ \\ ",
            " | |  | | (_| | (_| |    | |_| |___/ ",
            " |_|  |_|\\__,_|\\__,_|     \\___/|____/ ",
            "                                      ",
            "         -Existential Comedian-       "
        ]
        return signature
    
    def animate_thought_bubble(self):
        """Animate a thought bubble appearing"""
        bubble = [
            "   o",
            "  o o",
            " o   o",
            "o     o",
            " o   o",
            "  o o",
            "   o"
        ]
        
        for i in range(8):
            print("\033[F" * (len(bubble) if i < len(bubble) else 1), end='')
            if i < len(bubble):
                for j in range(i+1):
                    if j < len(bubble):
                        print("\033[K" + self.colors['cyan'] + bubble[j] + self.colors['reset'])
            time.sleep(0.1)
    
    def perform(self):
        """Main performance"""
        # Clear screen
        print("\033[2J\033[H", end='')
        
        # Draw signature with wobble
        signature = self.create_woody_signature()
        for line in signature:
            colored_line = ''
            for char in line:
                if char != ' ':
                    colored_line += self.colors['magenta'] + char + self.colors['reset']
                else:
                    colored_line += char
            self.typewriter_effect(colored_line, delay=0.005)
        
        print("\n" * 2)
        
        # Animate thought bubble
        self.animate_thought_bubble()
        
        print("\n" * 2)
        
        # Select random quote
        quote = random.choice(self.quotes)
        
        # Calculate box width
        box_width = len(quote) + 8
        
        # Draw box with neurotic wobble
        print(self.colors['cyan'] + self.draw_neurotic_border(box_width) + self.colors['reset'])
        
        # Empty line
        print(self.colors['cyan'] + "|" + " " * (box_width - 2) + "|" + self.colors['reset'])
        
        # Quote line with dramatic pause
        print(self.colors['cyan'] + "|  \033[0m", end='')
        time.sleep(0.5)
        
        # Type the quote with random dramatic pauses
        words = quote.split()
        for i, word in enumerate(words):
            self.typewriter_effect(word + " ", delay=0.05 if i % 3 != 0 else 0.2)
        
        print(self.colors['cyan'] + "  |" + self.colors['reset'])
        
        # Another empty line
        print(self.colors['cyan'] + "|" + " " * (box_width - 2) + "|" + self.colors['reset'])
        
        # Bottom border
        print(self.colors['cyan'] + self.draw_neurotic_border(box_width) + self.colors['reset'])
        
        # Add neurotic footnote
        print("\n")
        footnote = "(Note: This quote may cause existential dread, which is not covered by warranty.)"
        self.typewriter_effect(footnote, self.colors['red'], delay=0.02)
        
        # Final fade effect
        print("\n")
        for i in range(5):
            print("\033[F" + " " * 80)
            time.sleep(0.1)

if __name__ == "__main__":
    try:
        woody = WoodyAllenPhilosopher()
        woody.perform()
    except KeyboardInterrupt:
        print("\n\033[91m[Interrupted mid-existential-crisis]\033[0m")
        sys.exit(0)