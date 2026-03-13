"""
Campbell's Soup Can #2742
Produced: 2026-03-13 13:33:58
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

# ──────────────────────────────────────────────────────────────────────────────
# Woody Allen's Existential Neurosis Generator 3000™
# ──────────────────────────────────────────────────────────────────────────────

class WoodyAllenPhilosopher:
    def __init__(self):
        self.quotes = [
            "I'm not afraid of death; I just don't want to be there when it happens.",
            "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
            "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
            "What an absurd world we live in. I'm already planning my next therapist appointment... for next year.",
            "I'm not anti-social. I'm just not user-friendly.",
            "I think crime pays. The only problem is that it doesn't pay enough to cover my analyst's fees.",
            "I wouldn't say I'm neurotic, but I do tend to obsess about whether I'm being neurotic enough.",
            "MyonebankbalanceissolowIthinkit'sdevelopingitsownpersonality.Andit'snotanicepersonality.",
            "Eternityisalongtime,especiallytowardstheend.IjusthopeIdon'tgetbored.",
            "IaskedmytherapistifIwasparanoid.Shesaid,'Whotoldyouthat?'"
        ]
        self.colors = [
            '\033[38;5;208m',  # Saffron (neurotic orange)
            '\033[38;5;45m',   # Cyan (existential blue)
            '\033[38;5;129m',  # Magenta (anxious purple)
            '\033[38;5;178m',  # Yellow (worried yellow)
            '\033[38;5;123m'   # Pink (self-deprecating pink)
        ]
        self.reset = '\033[0m'
        
    def typewriter(self, text, delay=0.03, color=None):
        """Simulate nervous typing with optional color"""
        if color:
            sys.stdout.write(color)
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay + random.uniform(-0.01, 0.01))
        if color:
            sys.stdout.write(self.reset)
        print()
    
    def draw_box(self, width=60):
        """Draw a wobbly neurotic box"""
        corners = ['┌', '┐', '└', '┘']
        hlines = ['─', '╱', '╲', '┄', '┈']
        vlines = ['│', '╎', '┆', '┊']
        
        # Randomly choose characters for this rendering
        h = random.choice(hlines)
        v = random.choice(vlines)
        tl = random.choice(['┌', '╔'])
        tr = random.choice(['┐', '╗'])
        bl = random.choice(['└', '╚'])
        br = random.choice(['┘', '╝'])
        
        # Top border with slight wobble
        sys.stdout.write(f"{self.colors[0]}{tl}")
        for i in range(width-2):
            if random.random() < 0.1:  # 10% chance of wobble
                sys.stdout.write(random.choice(['╱', '╲']))
            else:
                sys.stdout.write(h)
        print(f"{tr}{self.reset}")
        
        return v, width-2  # Return vertical line character and inner width
    
    def get_quote(self):
        """Get a Woody Allen style quote (ours or his)"""
        return random.choice(self.quotes)
    
    def animate_thought_bubble(self):
        """Animate a thinking bubble"""
        bubble = [
            "  ╭────╮  ",
            "  │ 🤔 │  ",
            "  ╰────╯  "
        ]
        for line in bubble:
            print(f"\033[38;5;240m{line}\033[0m")
            time.sleep(0.1)
        time.sleep(0.5)
        # Clear bubble with backspaces (simplified)
        print("\033[F\033[F\033[F\033[F", end='')
    
    def render(self):
        """Main rendering function"""
        # Clear screen and hide cursor
        print("\033[2J\033[?25l", end='')
        
        # Random position on screen (within bounds)
        term_height = 24  # Approximate
        term_width = 80   # Approximate
        
        # Random vertical position (leave room for box)
        top_margin = random.randint(2, term_height - 15)
        print(f"\033[{top_margin};0H", end='')
        
        # Select random color for this rendering
        accent_color = random.choice(self.colors)
        
        # Pre-thought animation
        self.animate_thought_bubble()
        
        # Draw the box
        vline, inner_width = self.draw_box(58)
        
        # Get and format the quote
        quote = self.get_quote()
        
        # Break quote into lines
        words = quote.split()
        lines = []
        current_line = []
        current_len = 0
        
        for word in words:
            if current_len + len(word) + len(current_line) <= inner_width:
                current_line.append(word)
                current_len += len(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_len = len(word)
        if current_line:
            lines.append(' '.join(current_line))
        
        # Print each line with neurotic typo effect
        for i, line in enumerate(lines):
            # Left border
            sys.stdout.write(f"{accent_color}{vline}\033[0m ")
            
            # Sometimes add a stutter effect (repeat first letter)
            if random.random() < 0.2 and i > 0:
                sys.stdout.write(line[0])
                time.sleep(0.1)
                sys.stdout.write(line[0])
            
            # Type the line
            self.typewriter(line, delay=0.02 if i == 0 else 0.015, color=accent_color)
            
            # Right border alignment (pad if needed)
            padding = inner_width - len(line)
            if padding > 0:
                print(f"{' ' * padding} {accent_color}{vline}\033[0m")
            else:
                print(f" {accent_color}{vline}\033[0m")
            
            time.sleep(0.1 if i < len(lines)-1 else 0.3)
        
        # Bottom border (drawn separately)
        print(f"{accent_color}└{'─' * (inner_width)}┘\033[0m")
        
        # Post-quote existential pause
        time.sleep(1.5)
        print(f"\033[38;5;240m[Exhales audibly]\033[0m")
        
        # Show cursor again
        print("\033[?25h", end='')

def main():
    philosopher = WoodyAllenPhilosopher()
    
    # Run multiple times with different presentations
    for i in range(3):
        philosopher.render()
        time.sleep(2)
        if i < 2:
            print("\n" * 3)  # Space between quotes
    
    # Final self-deprecating note
    print("\n\033[38;5;240m")
    print("─" * 60)
    print("(This program acknowledges that even its own existential")
    print("dread is probably not as profound as it thinks it is.)")
    print("─" * 60)
    print("\033[0m")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[?25h\033[0m")  # Show cursor and reset on Ctrl+C
        sys.exit(0)