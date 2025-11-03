"""
Campbell's Soup Can #19
Produced: 2025-11-03 03:57:55
Worker: TNG: DeepSeek R1T2 Chimera (free) (tngtech/deepseek-r1t2-chimera:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def main():
    # ANSI escape codes
    RESET = "\033[0m"
    BOLD_CYAN = "\033[1;36m"
    YELLOW = "\033[1;33m"
    WHITE_BRIGHT = "\033[1;97m"
    PINK = "\033[38;5;205m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    
    # Woody Allen-style quote
    quote_lines = [
        "I wouldn't mind the existential dread if someone could",
        "at least validate how artistic my anxiety looks when",
        "I pose dramatically with a cup of decaf."
    ]
    author = "— Woody Allen"
    
    # Calculate box dimensions
    max_line_length = max(len(line) for line in quote_lines)
    box_width = max_line_length + 8
    title = "Neurotic Wisdom"
    
    # Display
    print("\033[2J\033[H")  # Clear screen
    
    # Title with 'coffee' ASCII art
    print(f"\n{WHITE_BRIGHT}      ) )")
    print(f"     ( ({BOLD_CYAN}☕ {WHITE_BRIGHT}){BOLD_CYAN} {title.upper()}{RESET}")
    print(f"      ) ){RESET}")
    
    # Top border with bounce animation
    border = "─" * (box_width - 2)
    for i in range(0, 3):
        for pos in [0, 2, 4, 2]:  # Bounce positions
            time.sleep(0.1)
            print(f"\033[4;1H{WHITE_BRIGHT}┌{border[pos:]}┐{RESET}", end="\r")
    time.sleep(0.3)
    
    # Quote box
    print(f"\033[5;1H{WHITE_BRIGHT}│{' ' * (box_width-2)}│{RESET}")
    
    # Typewriter effect for quote
    for idx, line in enumerate(quote_lines):
        padded_line = f"  {line.center(max_line_length)}  "
        print(f"\033[{6+idx};1H{WHITE_BRIGHT}│{RESET}{YELLOW}", end="")
        for char in padded_line:
            print(char, end="", flush=True)
            time.sleep(0.04 if char not in " ." else 0.01)
        print(f"{RESET}{WHITE_BRIGHT}│{RESET}")
    
    # Bottom border
    print(f"\033[{6+len(quote_lines)};1H{WHITE_BRIGHT}└{border}┘{RESET}")
    
    # Animated author credit
    print(f"\n\n{ITALIC}{DIM}", end="")
    for char in author:
        print(char, end="", flush=True)
        time.sleep(0.1)
    print(RESET)

if __name__ == "__main__":
    main()