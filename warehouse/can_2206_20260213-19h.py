"""
Campbell's Soup Can #2206
Produced: 2026-02-13 19:52:47
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# ANSI escape codes for colors
RESET = "\033[0m"
ORANGE = "\033[38;5;226m"
RED = "\033[38;5;196m"
YELLOW = "\033[38;5;220m"
BLUE = "\033[38;5;11m"
BOLD = "\033[1m"
ITALIC = "\033[3m"

# Define the quote in Woody Allen's style
QUOTE = "I've been in therapy for years, but the therapist finally said: 'You're not crazy, you're just the right person for the job.' And I said: 'What job?' And he said: 'The one you're already doing.'"

# Width of the box
WIDTH = 60

# Create the ASCII art frame
def create_frame():
    top = f"{ORANGE}{BOLD}{'+'}{RESET}{ORANGE}{'-' * (WIDTH - 2)}{RESET}{ORANGE}{BOLD}+{RESET}"
    middle = f"{ORANGE}{BOLD}|{RESET}{ORANGE}{' ' * (WIDTH - 2)}{RESET}{ORANGE}{BOLD}|{RESET}"
    bottom = f"{ORANGE}{BOLD}{'+'}{RESET}{ORANGE}{'-' * (WIDTH - 2)}{RESET}{ORANGE}{BOLD}+{RESET}"
    return top, middle, bottom

# Print the thinking face animation
def print_thinking_face():
    frames = [
        f"{YELLOW}  ( •_•)  ",
        f"{YELLOW}  ( •.•)  ",
        f"{YELLOW}  (   )  ",
        f"{YELLOW}  ( •_•)  "
    ]
    for frame in frames:
        print(frame)
        time.sleep(0.3)
        # Clear the line
        print("\033[A\r", end="")

# Print the quote in the frame with visual flair
def print_quote():
    top, middle, bottom = create_frame()
    
    # Center the quote in the frame
    quote_line = QUOTE.center(WIDTH - 2)
    
    # Print the entire composition
    print(f"{BLUE}{BOLD}  WOODY ALLEN'S DAILY EXISTENTIAL CRISIS  {RESET}")
    print_thinking_face()
    print(top)
    print(middle)
    print(f"{ORANGE}{BOLD}|{RESET}{RED}{ITALIC}  {quote_line}  {RESET}{ORANGE}{BOLD}|{RESET}")
    print(middle)
    print(bottom)
    print(f"\n{YELLOW}{BOLD}   -- Your Daily Reminder That You're Not Alone   {RESET}")

# Execute
print_quote()