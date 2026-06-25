"""
Campbell's Soup Can #4010
Produced: 2026-06-25 11:49:45
Worker: Google: Gemma 4 26B A4B  (free) (google/gemma-4-26b-a4b-it:free)
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

def clear_screen():
    print("\033[H\033[J", end="")

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def typewriter(text, delay=0.06, color="\033[37m"):
    """Animates text typing out like a neurotic monologue."""
    for char in text:
        sys.stdout.write(f"{color}{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_frame(width, height, color="\033[36m"):
    """Draws a cinematic, slightly shaky frame."""
    print(color + "╔" + "═" * (width - 2) + "╗")
    for _ in range(height - 2):
        print("║" + " " * (width - 2) + "║")
    print("╚" + "═" * (width - 2) + "╝" + "\033[0m")

def neurosis_animation():
    """A small visual representation of an anxious mind."""
    symbols = ["?", "!", "...", "§", "ø", "×", "∞"]
    for _ in range(15):
        clear_screen()
        center_x = 40
        center_y = 10
        
        # Draw a 'thinking' cloud of anxiety
        for _ in range(5):
            x = random.randint(20, 60)
            y = random.randint(5, 15)
            sym = random.choice(symbols)
            print(f"\033[{y};{x}H{color_text(sym, '33')}", end="")
            
        time.sleep(0.1)

def main():
    # ANSI Colors
    CYAN = "36"
    MAGENTA = "35"
    YELLOW = "33"
    RED = "31"
    WHITE = "37"
    GRAY = "90"

    quote = (
        "\"I have a profound fear of the infinite, "
        "not because of its scale, but because "
        "I'm reasonably certain I'll be expected "
        "to make small talk with it.\""
    )

    try:
        # Phase 1: The Existential Dread Intro
        clear_screen()
        print("\n" * 5)
        typewriter("INITIALIZING EXISTENTIAL CRISIS...", 0.1, RED)
        time.sleep(1)
        
        # Phase 2: The Nervous Flutter
        for _ in range(3):
            neurosis_animation()
        
        # Phase 3: The Grand Reveal
        clear_screen()
        width = 70
        height = 12
        
        # Draw a 'film noir' style border
        print(color_text("\n  [ A Neurotic Moment in 4K ]\n", GRAY))
        draw_frame(width, height, CYAN)
        
        # Move cursor inside the box (approximation via newlines)
        # Since we can't use complex libraries, we use a structured approach
        print("\n" * 4, end="")
        
        # Center the quote (roughly)
        # Split quote to wrap it manually inside the 'frame'
        words = quote.split()
        lines = []
        current_line = []
        for word in words:
            if len(" ".join(current_line + [word])) < width - 6:
                current_line.append(word)
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
        lines.append(" ".join(current_line))

        # Print the lines with a "shaky" animation effect
        for line in lines:
            # Adding padding to simulate centering
            padding = " " * ((width - len(line) - 2) // 2)
            # Typewriter effect inside the frame
            typewriter(f"{padding}{line}", 0.04, WHITE)
            print("\n" * 1, end="")

        print("\n" * 2)
        typewriter("--- Press Ctrl+C to accept the void ---", 0.08, MAGENTA)
        
        # Keep the window open
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print(f"\n\n{color_text('Even your exit is neurotic. Goodbye.', RED)}")
        sys.exit()

if __name__ == "__main__":
    main()