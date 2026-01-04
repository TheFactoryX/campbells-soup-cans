"""
Campbell's Soup Can #1390
Produced: 2026-01-04 16:40:34
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
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"
    FRAME_WIDTH = 60
    
    quote_part1 = "The universe is vast and meaningless,"
    quote_part2 = "but at least the coffee in my hand is real."
    quote_part3 = "Is it too much to ask for both existential certitude"
    quote_part4 = "and a decent bagel?"

    frame_top =    f"/{'¯' * (FRAME_WIDTH-2)}\\_"
    frame_bottom = f"\\{'_' * (FRAME_WIDTH-2)}/"
    
    def print_line(text, color=YELLOW, delay=0.08):
        padded = text.center(FRAME_WIDTH - 4)
        print(f"| {color}{BOLD}{padded}{RESET} |")
        time.sleep(delay)
    
    # Animation
    print("\n" * 2)
    time.sleep(0.5)
    print(f"{' ' * 10}{YELLOW}{BOLD}🤔 Contemplating existence...{RESET}\n")
    time.sleep(1.5)
    
    print(f"{' ' * 8}{frame_top}")
    print_line("", delay=0)
    print_line(quote_part1)
    print_line(quote_part2, RED)
    print_line("", delay=0.3)
    print_line(quote_part3)
    print_line(quote_part4, RED)
    print_line("", delay=0)
    print(f"{' ' * 8}{frame_bottom}")
    
    # Woody Allen signature
    time.sleep(0.8)
    print(f"\n{' ' * (FRAME_WIDTH-20)}{YELLOW}— Woody Allen's inner monologue{RESET}\n")

if __name__ == "__main__":
    main()