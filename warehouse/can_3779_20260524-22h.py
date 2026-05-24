"""
Campbell's Soup Can #3779
Produced: 2026-05-24 22:11:15
Worker: Arcee AI: Trinity Large Thinking (free) (arcee-ai/trinity-large-thinking:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Display
Pure Python, no external dependencies, ANSI colors and animations.
"""

import time
import sys
import os

class WoodyAllenQuote:
    def __init__(self):
        self.quote = (
            "I once wanted to be a hero, but then I realized that would require me "
            "to be brave, and I'm not even brave enough to order coffee without anxiety."
        )
        self.author = "— Woody Allen (probably)"
        self.width = 60
        
    def clear_screen(self):
        """Clear terminal screen using ANSI escape."""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def typewriter_effect(self, text, color_code, delay=0.03):
        """Print text with typewriter effect and color."""
        for char in text:
            sys.stdout.write(color_code + char + '\033[0m')
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def draw_box(self, text_lines, color_border, color_text):
        """Draw a decorative box around text."""
        border_top = color_border + '╔' + '═' * (self.width - 2) + '╗' + '\033[0m'
        border_bottom = color_border + '╚' + '═' * (self.width - 2) + '╝' + '\033[0m'
        border_vertical = color_border + '║' + '\033[0m'
        
        print(border_top)
        
        for line in text_lines:
            padding = (self.width - 2 - len(line)) // 2
            formatted_line = f"{border_vertical}{' ' * padding}{color_text}{line}{' ' * (padding + (self.width - 2 - len(line) - 2*padding))}{border_vertical}"
            print(formatted_line)
        
        print(border_bottom)
    
    def animate_appearance(self):
        """Animate the quote appearing with a glitch effect."""
        colors = ['\033[36m', '\033[33m', '\033[35m', '\033[32m']
        
        for i in range(3):
            self.clear_screen()
            print(random.choice(colors) + self.quote + '\033[0m')
            time.sleep(0.1)
            self.clear_screen()
            time.sleep(0.1)
        
        self.clear_screen()
    
    def display(self):
        """Main display method."""
        self.clear_screen()
        
        # Header
        print('\033[93m' + '=' * 50)
        print(' ' * 16 + 'PHILOSOPHICAL CRISIS')
        print('=' * 50 + '\033[0m')
        print()
        
        time.sleep(0.5)
        
        # Draw initial empty box
        self.draw_box([], '\033[36m', '\033[33m')
        time.sleep(0.5)
        
        # Typewriter effect for quote
        self.clear_screen()
        print('\033[93m' + '=' * 50)
        print(' ' * 16 + 'PHILOSOPHICAL CRISIS')
        print('=' * 50 + '\033[0m')
        print()
        
        # Split quote into lines
        words = self.quote.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line + word) + 1 <= self.width - 4:
                current_line += word + " "
            else:
                lines.append(current_line.strip())
                current_line = word + " "
        if current_line:
            lines.append(current_line.strip())
        
        # Animate each line
        for i, line in enumerate(lines):
            self.draw_box([line], '\033[36m', '\033[33m')
            time.sleep(0.8)
            if i < len(lines) - 1:
                self.clear_screen()
                print('\033[93m' + '=' * 50)
                print(' ' * 16 + 'PHILOSOPHICAL CRISIS')
                print('=' * 50 + '\033[0m')
                print()
                # Keep previous lines visible by redrawing them
                for j in range(i + 1):
                    padding = (self.width - 2 - len(lines[j])) // 2
                    border_vertical = '\033[36m' + '║' + '\033[0m'
                    formatted_line = f"{border_vertical}{' ' * padding}\033[33m{lines[j]}{' ' * (padding + (self.width - 2 - len(lines[j]) - 2*padding))}{border_vertical}"
                    print(formatted_line)
        
        print()
        time.sleep(0.5)
        
        # Author with typewriter effect
        print()
        self.typewriter_effect(self.author, '\033[90m', 0.05)
        
        # Footer
        print()
        print('\033[91m' + 'Existence is pain. Just kidding. Or am I?' + '\033[0m')
        print()

def main():
    quote = WoodyAllenQuote()
    quote.display()
    
    # Keep screen open
    try:
        input("\nPress Enter to return to your existential dread...")
    except KeyboardInterrupt:
        print("\n\nFine, leave. See if the universe cares.")
        sys.exit(0)

if __name__ == "__main__":
    main()