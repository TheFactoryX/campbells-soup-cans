"""
Campbell's Soup Can #3776
Produced: 2026-05-24 18:13:37
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
Woody Allen-style existential crisis generator with visual flair.
Features: animated text reveal, color gradients, ASCII frame, and neurotic humor.
"""

import sys
import time
import random
from dataclasses import dataclass

# ANSI escape codes for colors
class Colors:
    RESET = '\033[0m'
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    BOLD = '\033[1m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'

@dataclass
class Quote:
    """A neurotic Woody Allen-style philosophical quote."""
    text: str
    author: str = "— Woody Allen (probably)"
    
    def __str__(self):
        return f'"{self.text}"\n{self.author}'

def typewriter_effect(text, color=Colors.WHITE, delay=0.03, random_offset=False):
    """Print text with a typewriter effect and optional color."""
    for char in text:
        if random_offset and random.random() < 0.1:
            time.sleep(delay * 3)  # Occasional long pauses for dramatic effect
        else:
            time.sleep(delay)
        print(f"{color}{char}{Colors.RESET}", end='', flush=True)
    print()

def draw_frame(width=60, height=12, color=Colors.CYAN):
    """Draw an ASCII art frame with decorative corners."""
    top_bottom = color + "╔" + "═" * (width-2) + "╗" + Colors.RESET
    sides = color + "║" + " " * (width-2) + "║" + Colors.RESET
    bottom_up = color + "╚" + "═" * (width-2) + "╝" + Colors.RESET
    
    print("\n" + top_bottom)
    for _ in range(height-2):
        print(sides)
    print(bottom_up)

def animate_frame_appearance(width=60, height=12):
    """Animate the frame drawing itself from top to bottom."""
    colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.MAGENTA]
    
    # Draw top line
    print(random.choice(colors) + "╔" + "═" * (width-2) + "╗" + Colors.RESET)
    time.sleep(0.1)
    
    # Draw sides with animation
    for row in range(1, height-1):
        color = random.choice(colors)
        print(color + "║" + " " * (width-2) + "║" + Colors.RESET, end='')
        # Draw random "dust particles" in the frame
        if random.random() < 0.3:
            print(random.choice(colors) + "·" + Colors.RESET, end='')
        else:
            print(" ", end='')
        print()
        time.sleep(0.05)
    
    # Draw bottom line
    print(random.choice(colors) + "╚" + "═" * (width-2) + "╝" + Colors.RESET)
    time.sleep(0.2)

def create_gradient_text(text, colors):
    """Create text with a gradient effect through multiple colors."""
    if not text:
        return ""
    
    gradient = []
    chunk_size = max(1, len(text) // len(colors))
    
    for i, color in enumerate(colors):
        start = i * chunk_size
        end = start + chunk_size if i < len(colors) - 1 else len(text)
        gradient.append(f"{color}{text[start:end]}{Colors.RESET}")
    
    return "".join(gradient)

def main():
    """Generate and display a Woody Allen-style quote with visual effects."""
    print(f"\033[?25l\033[2J\033[H")  # Clear screen and hide cursor
    
    # Woody Allen-esque quote generation
    quotes = [
        "I once had a dream that I was awake, but then I realized I was just having a nightmare about being awake. It was very existential.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon. Especially if you're sitting next to someone who talks during the movie.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying. So far, my plan is working perfectly.",
        "My brain? It's my second favorite organ. My first favorite is my liver, because it processes all the alcohol from my existential dread.",
        "I was thrown out of college for cheating on the metaphysics exam; I looked into the soul of the boy sitting next to me. He was cheating too.",
        "Why are our days numbered and not, say, lettered? I'd prefer a good alphabet over this chronological tyranny.",
        "I believe there is something out there watching us. Unfortunately, it's the government.",
        "Sex between a man and a woman can be wonderful, provided you get between the right man and the right woman. And both are you.",
        "I took a speed-reading course and read War and Peace in twenty minutes. It involves Russia.",
        "My one regret in life is that I am not someone else. Preferably someone with better posture and fewer allergies."
    ]
    
    quote = random.choice(quotes)
    author = "— Woody Allen (or a reasonable approximation thereof)"
    
    # Visual setup
    width = 70
    height = 18
    
    # Animate frame appearance
    animate_frame_appearance(width, height)
    
    # Create gradient for title
    title = "PHILOSOPHICAL CRISIS INCOMING"
    gradient_colors = [Colors.RED, Colors.YELLOW, Colors.GREEN, Colors.CYAN, Colors.BLUE]
    gradient_title = create_gradient_text(title, gradient_colors)
    
    # Print title with typewriter effect
    print("\n" + " " * ((width - len(title)) // 2) + gradient_title)
    time.sleep(0.5)
    
    # Print empty line with border effect
    print(Colors.CYAN + "║" + " " * (width-2) + "║" + Colors.RESET)
    
    # Print quote with typewriter effect and color changes
    words = quote.split()
    current_line = ""
    line_count = 0
    
    for word in words:
        if len(current_line) + len(word) + 1 > width - 4:  # Account for borders
            # Print line with random color
            color = random.choice([Colors.YELLOW, Colors.WHITE, Colors.MAGENTA])
            print(Colors.CYAN + "║" + Colors.RESET + 
                  f"{color}{current_line.ljust(width-4)}{Colors.RESET}" + 
                  Colors.CYAN + "║" + Colors.RESET)
            current_line = word + " "
            line_count += 1
        else:
            current_line += word + " "
    
    # Print last line
    if current_line:
        color = random.choice([Colors.YELLOW, Colors.WHITE, Colors.MAGENTA])
        print(Colors.CYAN + "║" + Colors.RESET + 
              f"{color}{current_line.ljust(width-4)}{Colors.RESET}" + 
              Colors.CYAN + "║" + Colors.RESET)
    
    # Print attribution
    print(Colors.CYAN + "║" + Colors.RESET + 
          f"{Colors.GREEN}{author.center(width-4)}{Colors.RESET}" + 
          Colors.CYAN + "║" + Colors.RESET)
    
    # Bottom frame line
    print(Colors.CYAN + "╚" + "═" * (width-2) + "╝" + Colors.RESET)
    
    # Add some neurotic commentary at the bottom
    print("\n")
    typewriter_effect("Anyway, that's what I think... ", Colors.YELLOW, 0.05)
    typewriter_effect("But what do I know? I'm just a fictional character in a Python script.", Colors.CYAN, 0.05)
    typewriter_effect("Sometimes I wonder if any of this is real, or if I'm just a simulation running on someone's laptop.", Colors.RED, 0.05)
    typewriter_effect("If this is a simulation, the programmer has a weird sense of humor.", Colors.MAGENTA, 0.05)
    
    # Final existential question
    print("\n")
    typewriter_effect("But enough about me. What do YOU think about death?", Colors.BOLD + Colors.GREEN, 0.03, random_offset=True)
    
    # Show cursor and exit
    print(f"\033[?25h")
    print(f"\n{Colors.BLUE}Press any key to return to your existential crisis...{Colors.RESET}")
    input()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\033[?25h{Colors.RED}Fine, run away from existential thoughts. See if I care.{Colors.RESET}")
        sys.exit(0)