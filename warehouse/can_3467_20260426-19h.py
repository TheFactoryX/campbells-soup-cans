"""
Campbell's Soup Can #3467
Produced: 2026-04-26 19:57:31
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

def typewriter_effect(text, delay=0.05, color="\033[37m"):
    """Prints text with a neurotic, stuttering typewriter effect."""
    full_text = f"{color}{text}\033[0m"
    for char in text:
        # Add a little 'stutter' randomness to mimic neuroticism
        if random.random() > 0.95:
            sys.stdout.write(char * 2)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(0, 0.05))
    print()

def draw_frame(quote, width=60):
    """Draws a sophisticated, slightly shaky frame around the quote."""
    top_bottom = color_text("╔" + "═" * (width - 2) + "╗", "36")
    side = color_text("║", "36")
    bottom = color_text("╚" + "═" * (width - 2) + "╝", "36")
    
    clear_screen()
    print("\n" * 3)
    print(center_text(top_bottom, width))
    
    # Split quote into lines for the box
    words = quote.split()
    lines = []
    current_line = []
    
    for word in words:
        if len(" ".join(current_line + [word])) < width - 4:
            current_line.append(word)
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
    lines.append(" ".join(current_line))

    for line in lines:
        padding = (width - 2 - len(line)) // 2
        left_pad = " " * padding
        right_pad = " " * (width - 2 - len(line) - padding)
        print(f"{side}{left_pad}{line}{right_pad}{side}")

    print(center_text(bottom, width))
    print("\n" * 2)

def center_text(text, width):
    return text.center(width)

def main():
    # The Woody Allen Style Quote
    quote = ("\"I find the concept of eternal life deeply unsettling; "
             "not because of the morality, but because of the "
             "unavoidable social obligations and the sheer amount "
             "of sequels I'd be forced to endure.\"")

    # Colors: 31=Red, 32=Green, 33=Yellow, 34=Blue, 35=Magenta, 36=Cyan
    
    # 1. Intro Animation: The Existential Panic
    clear_screen()
    panic_words = ["EXISTENCE?", "VOID?", "WHY?", "PANIC!", "COFFEE?"]
    for _ in range(10):
        word = random.choice(panic_words)
        print(center_text(color_text(word, "31"), 60))
        time.sleep(0.1)
        clear_screen()
        time.sleep(0.05)

    # 2. The Dramatic Build-up
    print("\n" * 5)
    typewriter_effect("Analyzing the human condition...", 0.08, "33")
    time.sleep(1)
    typewriter_effect("Searching for meaning in a meaningless universe...", 0.08, "33")
    time.sleep(1)
    typewriter_effect("Error: Meaning not found. Reverting to neurotic humor.", 0.04, "31")
    time.sleep(1.5)

    # 3. The Reveal
    draw_frame(quote)
    
    # Final effect: A little jitter
    for _ in range(3):
        sys.stdout.write("\r" + " " * 10)
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write("\r" + " " * 5)
        sys.stdout.flush()
        time.sleep(0.1)

    print(center_text(color_text("--- [ End of Existential Crisis ] ---", "35"), 60))
    print("\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nEven the exit is a crisis. Goodbye.")