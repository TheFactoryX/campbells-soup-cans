"""
Campbell's Soup Can #2570
Produced: 2026-03-04 19:50:43
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
import os

class WoodyAllenQuote:
    def __init__(self):
        self.colors = {
            'reset': '\033[0m',
            'red': '\033[91m',
            'green': '\033[92m',
            'yellow': '\033[93m',
            'blue': '\033[94m',
            'magenta': '\033[95m',
            'cyan': '\033[96m',
            'white': '\033[97m',
            'bold': '\033[1m',
            'italics': '\033[3m',
            'underline': '\033[4m'
        }
    
    def color_text(self, text, color_name):
        return f"{self.colors[color_name]}{text}{self.colors['reset']}"
    
    def typewriter_effect(self, text, delay=0.03):
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def draw_frame(self):
        frame_width = 70
        frame_char = "─"
        corner_char = "╭" if os.name != 'nt' else "+"
        
        # Top border
        self.typewriter_effect(self.color_text(corner_char + frame_char * (frame_width - 2) + "╮", 'cyan'))
        
        # Side borders with content
        self.typewriter_effect(self.color_text("│" + " " * (frame_width - 2) + "│", 'cyan'))
        self.typewriter_effect(self.color_text("│" + " " * 16 + "WOODY ALLEN" + " " * 17 + "│", 'yellow'))
        self.typewriter_effect(self.color_text("│" + " " * (frame_width - 2) + "│", 'cyan'))
        self.typewriter_effect(self.color_text("│" + " " * (frame_width - 2) + "│", 'cyan'))
        
        # Quote
        quote = " I tried to be a philosopher once, but I kept getting "
        quote += "distracted by my own neurosis. I think I exist, therefore "
        quote += "I'm probably worried about something. "
        
        # Split quote to fit in frame
        words = quote.split()
        line = ""
        for word in words:
            if len(line + word) + 1 > frame_width - 4:
                self.typewriter_effect(self.color_text("│" + line.center(frame_width - 4) + "│", 'white'))
                line = word + " "
            else:
                line += word + " "
        self.typewriter_effect(self.color_text("│" + line.center(frame_width - 4) + "│", 'white'))
        
        # Side borders with footer
        self.typewriter_effect(self.color_text("│" + " " * (frame_width - 2) + "│", 'cyan'))
        self.typewriter_effect(self.color_text("│" + " " * 22 + "─" * 26 + " " * 22 + "│", 'cyan'))
        self.typewriter_effect(self.color_text("│" + " " * 24 + "PHILOSOPHY" + " " * 23 + "│", 'yellow'))
        self.typewriter_effect(self.color_text("╰" + frame_char * (frame_width - 2) + "╯", 'cyan'))
    
    def show_animated_quote(self):
        # Clear screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Title
        self.typewriter_effect("\n" + self.color_text("THE WOODY ALLEN PHILOSOPHY GENERATOR", 'bold', 'red'))
        time.sleep(1)
        
        # Animated frame
        self.draw_frame()
        time.sleep(1)
        
        # Neurotic footer
        footer = "\n\n"
        footer += self.color_text(" existential crisis level: ", 'magenta')
        footer += self.color_text("█" * 15 + "█" * 15, 'red')
        footer += " " + self.color_text("maximum", 'red')
        
        self.typewriter_effect(footer)
        time.sleep(0.5)
        
        # Self-deprecating signature
        self.typewriter_effect("\n\n" + self.color_text("─" * 30, 'yellow'))
        self.typewriter_effect(self.color_text("   Written by a man who", 'white'))
        self.typewriter_effect(self.color_text("   once spent an hour", 'white'))
        self.typewriter_effect(self.color_text("   worrying if his", 'white'))
        self.typewriter_effect(self.color_text("   thoughts were too", 'white'))
        self.typewriter_effect(self.color_text("   neurotic to be", 'white'))
        self.typewriter_effect(self.color_text("   considered neurotic.", 'white'))
        self.typewriter_effect(self.color_text("─" * 30, 'yellow'))
        
        # Exit prompt
        input("\n\n" + self.color_text("Press Enter to exit... (But only if you're absolutely sure. What if there's something better after this?)", 'cyan'))

if __name__ == "__main__":
    woody_quote = WoodyAllenQuote()
    woody_quote.show_animated_quote()