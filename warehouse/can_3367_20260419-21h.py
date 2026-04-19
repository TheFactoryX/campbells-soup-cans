"""
Campbell's Soup Can #3367
Produced: 2026-04-19 21:51:14
Worker: Elephant (openrouter/elephant-alpha)
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
import random

# ANSI color codes
class C:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"
    BG_RED = "\033[41m"
    DIM = "\033[2m"
    BOLD = "\033[1m"

# Woody Allen style quote
QUOTE = (
    "I'm not afraid of death; I just don't want to be there "
    "when it happens. It's like showing up late to a party "
    "where everyone's already left... and the door is locked."
)

def type_writer_effect(text, delay=0.03):
    """Simulate typing with a slight color shift per character."""
    colors = [C.RED, C.YELLOW, C.CYAN, C.GREEN, C.MAGENTA, C.WHITE, C.BLUE]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(f"{color}{char}{C.RESET}")
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.005))
    print()

def draw_balloon(quote, width=60):
    """Draw a speech balloon around the quote."""
    lines = []
    # Split quote into lines
    words = quote.split()
    current_line = ""
    for word in words:
        test_line = f"{current_line} {word}".strip()
        if len(test_line) <= width - 4:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    
    # Top
    balloon = []
    balloon.append(" " + " " * (width - 2) + " ")
    balloon.append(C.YELLOW + " " + "╭" + "─" * (width - 2) + "╮" + C.RESET)
    
    # Content lines
    for line in lines:
        padding = width - 4 - len(line)
        left = padding // 2
        right = padding - left
        balloon.append(C.YELLOW + " │" + " " * left + line + " " * right + "│" + C.RESET)
    
    # Bottom tail
    balloon.append(C.YELLOW + " │" + " " * (width - 4) + "│" + C.RESET)
    balloon.append(C.YELLOW + " " + " " * (width // 2 - 1) + "▼" + " " * (width // 2) + C.RESET)
    balloon.append(C.YELLOW + " " + "╰" + "─" * (width - 2) + "╯" + C.RESET)
    return balloon

def draw_speakers(who):
    """Draw a small ASCII speaker with thought bubbles."""
    speakers = [
        f"C{C.BLUE}  ｡◕‿◕｡  {C.RESET}   {C.GREEN}'{who}'{C.RESET}",
        f"C{C.BLUE} (⌐■_■) {C.RESET}   {C.GREEN}(philosopher){C.RESET}",
        f"C{C.BLUE}   つ ◕_◕  {C.RESET}   {C.YELLOW}existential crisis mode{C.RESET}"
    ]
    return speakers

def animate_stars(count=20):
    """Print twinkling stars randomly."""
    stars = ['✦', '★', '✧', '•', '☆']
    positions = random.sample(range(50), count)
    for pos in positions:
        color = random.choice([C.CYAN, C.MAGENTA, C.WHITE])
        sys.stdout.write(f"\033[{1};{pos+1}H{color}{random.choice(stars)}{C.RESET}")
    sys.stdout.flush()

def main():
    print(C.BG_BLUE + C.WHITE)
    print(" " * 15 + "🎭 W O O D Y   A L L E N   P H I L O S O P H Y 🎭")
    print(" " * 10 + "An Existential Comedy Hour")
    print(C.RESET)
    
    # Little intro animation
    for i in range(3):
        print("\n" + " " * 20 + C.YELLOW + "⌛" + C.RESET, end="", flush=True)
        time.sleep(0.3)
    
    print("\n\n")
    
    # Draw balloon
    balloon = draw_balloon(QUOTE)
    for line in balloon:
        print(line)
        time.sleep(0.02)
    
    print()
    
    # Speaker and additional commentary
    speakers = draw_speakers("Woody")
    for speaker in speakers:
        print(speaker.format(random.choice(['!', '.', '...'])))
        time.sleep(0.4)
    
    # Final twist
    print("\n" + C.BOLD + C.CYAN)
    print(" " * 15 + "The only true wisdom is in knowing you know nothing...")
    print(" " * 15 + "...especially about this quote.")
    print(C.RESET)

if __name__ == "__main__":
    main()