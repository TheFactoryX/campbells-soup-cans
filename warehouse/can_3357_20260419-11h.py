"""
Campbell's Soup Can #3357
Produced: 2026-04-19 11:00:22
Worker: Elephant (openrouter/elephant-alpha)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def draw_woody_head():
    # Simple ASCII Woody Allen face
    head = r"""
       .-^^---....,,--.
    .'|               '---.
    |.    ,-._   _..-._   '.
    |'  \\'-. | / // // /,  '
    |  \\  \\||/ // / //   ,'
     \\ \\ \\ \\|// |/  /   /
      \\ \\ \\ \\/'  |  /   /
       \\ \\ \\    ,'  /   /
        \\ \\ \\_,'\_ /   /
         \\ \\         /   /
          \\ \\        /   /
           \\ \\      /   /
            \\ \\    /   /
             \\ \\  /   /
              \\ \\/   /
               \\    /
                '..'
"""
    return head

def main():
    clear()
    
    # Woody Allen style quote
    quote = (
        "I'm not afraid of death; I just don't want to be there "
        "when it happens... probably because I'll have to stand "
        "in line and the line is always too long and the coffee "
        "is terrible and I forgot my reading glasses."
    )
    
    # Color codes
    BOLD = "\033[1m"
    RESET = "\033[0m"
    FOREST_GREEN = "\033[38;5;46m"
    LIGHT_CYAN = "\033[38;5;157m"
    WARM_YELLOW = "\033[38;5;226m"
    SOFT_PURPLE = "\033[38;5;147m"
    DARK_GRAY = "\033[38;5;240m"
    
    # Header
    header = f"{BOLD}{FOREST_GREEN}═══════════════════════════════════════{RESET}"
    title = f"{BOLD}{LIGHT_CYAN}      WOODY ALLEN'S EXISTENTIAL ADVICE   {RESET}"
    divider = f"{BOLD}{FOREST_GREEN}═══════════════════════════════════════{RESET}"
    
    print(header)
    print(title)
    print(divider)
    time.sleep(1)
    
    # ASCII art with color
    woody_head = draw_woody_head()
    for line in woody_head.split('\n'):
        if line.strip():
            print(f"{SOFT_PURPLE}{line}{RESET}")
        else:
            print()
        time.sleep(0.05)
    
    time.sleep(1)
    
    # Quote box
    padding = "    "
    max_width = 70
    
    # Top border
    print(f"\n{DARK_GRAY}┌{'─' * max_width}┐{RESET}")
    time.sleep(0.05)
    
    # Quote lines with wrapping and padding
    words = quote.split()
    current_line = ""
    
    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        if len(test_line) > max_width - 4:  # Account for padding and borders
            print(f"{DARK_GRAY}│{RESET}{padding}{WARM_YELLOW}{current_line}{RESET}{padding:<{max_width - len(current_line) - len(padding) - 4}}│{RESET}")
            time.sleep(0.05)
            current_line = word
        else:
            current_line = test_line
    
    # Last line
    if current_line:
        remaining = max_width - len(current_line) - len(padding) - len(padding) - 4
        if remaining < 0:
            remaining = 0
        print(f"{DARK_GRAY}│{RESET}{padding}{WARM_YELLOW}{current_line}{RESET}{padding:<{remaining}}│{RESET}")
    time.sleep(0.05)
    
    # Bottom border
    print(f"{DARK_GRAY}└{'─' * max_width}┘{RESET}")
    time.sleep(0.5)
    
    # Footer with author
    footer = f"{BOLD}{LIGHT_CYAN}           - Woody Allen (probably) -{RESET}"
    print(f"\n{footer}")
    
    # Final flourish
    time.sleep(0.5)
    print(f"\n{DARK_GRAY}   {'⌛' * 10}  {'💭' * 10}  {'🎬' * 10}  {'🤔' * 10}{RESET}")

if __name__ == "__main__":
    main()