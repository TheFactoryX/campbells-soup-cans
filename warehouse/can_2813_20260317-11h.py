"""
Campbell's Soup Can #2813
Produced: 2026-03-17 11:08:47
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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

def typewriter(text, color_code=97, delay=0.03):
    """Print text with typewriter effect in specified color."""
    for char in text:
        sys.stdout.write(f"\033[{color_code}m{char}\033[0m")
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def clear_screen():
    """Clear terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def print_woody_quote():
    clear_screen()
    
    # Woody Allen style quote (original!)
    quote = (
        "I'm not afraid of death; I just don't want to be there when it happens. "
        "Actually, I'd prefer to be somewhere else entirely - perhaps a nice diner "
        "where the coffee is weak but the existential dread is complimentary."
    )
    
    # Random colors for artistic effect
    colors = [91, 92, 93, 94, 95, 96]  # Bright colors
    border_color = 33  # Yellow
    
    # Create decorative border
    width = min(80, len(quote) + 20)
    top_border = f"\033[{border_color}m╔{'═' * (width-2)}╗\033[0m"
    bottom_border = f"\033[{border_color}m╚{'═' * (width-2)}╝\033[0m"
    side_border = f"\033[{border_color}m║\033[0m"
    
    # Print with animation
    print("\n" * 3)
    print(top_border.center(width + 20))
    print()
    
    # Center the quote with random colors per word
    words = quote.split()
    current_line = []
    line_length = 0
    max_line = width - 10
    
    for word in words:
        if line_length + len(word) + 1 <= max_line:
            current_line.append(word)
            line_length += len(word) + 1
        else:
            # Print current line with random colors per word
            print(side_border + " " * 4, end="")
            for w in current_line:
                color = random.choice(colors)
                typewriter(w + " ", color, 0.01)
            print(" " * (max_line - line_length + 4) + side_border)
            current_line = [word]
            line_length = len(word)
    
    # Print last line
    if current_line:
        print(side_border + " " * 4, end="")
        for w in current_line:
            color = random.choice(colors)
            typewriter(w + " ", color, 0.01)
        print(" " * (max_line - line_length + 4) + side_border)
    
    print()
    print(bottom_border.center(width + 20))
    
    # Add philosophical footer
    print("\n")
    footer = "─ Philosopher-in-Residence at the Diner of Despair ─"
    print(f"\033[90m{footer.center(width + 30)}\033[0m")
    
    # Final dramatic pause
    time.sleep(0.5)
    print("\n\033[3m\033[90m(Please disregard the meaning of life. It's on backorder.)\033[0m\n")

if __name__ == "__main__":
    try:
        print_woody_quote()
    except KeyboardInterrupt:
        print("\n\n\033[91m↳ Cancelled. Just like my therapist's appointment.\033[0m")
        sys.exit(0)