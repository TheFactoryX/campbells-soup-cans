"""
Campbell's Soup Can #5072
Produced: 2026-10-06 10:19:10
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import os
import time
import random

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_width():
    """Get terminal width for centering"""
    try:
        return os.get_terminal_size().columns
    except:
        return 80

def type_text(text, delay=0.03, color=""):
    """Type text out character by character with optional color"""
    reset = "\033[0m"
    for char in text:
        print(f"{color}{char}{reset}", end="", flush=True)
        time.sleep(delay)
    print()

def print_border(char="═", width=60, color="\033[36m"):
    """Print a decorative border"""
    reset = "\033[0m"
    print(f"{color}{char * width}{reset}")

def animate_ellipsis(seconds=2):
    """Animate ellipsis dots"""
    dots = ["", ".", "..", "..."]
    start = time.time()
    while time.time() - start < seconds:
        for dot in dots:
            print(f"\r{dot}", end="", flush=True)
            time.sleep(0.3)

def woody_allen_quote():
    """Display a Woody Allen style quote with neurotic flair"""
    clear_screen()
    
    # Colors
    cyan = "\033[36m"
    yellow = "\033[33m"
    magenta = "\033[35m"
    red = "\033[31m"
    blue = "\033[34m"
    bold = "\033[1m"
    italic = "\033[3m"
    reset = "\033[0m"
    
    # Get terminal width for responsive design
    width = min(get_terminal_width(), 70)
    
    # Animated intro
    print(f"\n{cyan}{' ' * 10}{'█' * 40}{reset}\n")
    time.sleep(0.5)
    
    # Title with anxiety
    title = "A THOUGHT ON EXISTENCE"
    padding = (width - len(title)) // 2
    print(f"{' ' * padding}{yellow}{bold}{title}{reset}")
    time.sleep(0.8)
    
    print_border("━", width, cyan)
    print()
    
    # The quote - typed out with hesitation
    quote_lines = [
        f"{italic}I{reset} don't know why we're here,",
        f"{italic}but I{reset}'m sure it's not to enjoy ourselves.",
        f"{italic}The whole thing{reset} feels like a badly written joke",
        f"{italic}with a punchline{reset} that never quite lands.",
        f"{italic}And the worst part?{reset} I think I{italic} wrote{reset} it myself.",
        f"{italic}Somewhere between my{reset} anxiety{italic} and my{reset} existential dread.",
        f"{italic}The audience is laughing{reset}... or maybe they're just",
        f"{italic} uncomfortable{reset} and shifting in their seats.",
        f"{italic}Either way{reset}, I{italic} apologize{reset} for the performance.",
        f"{italic}This life{reset}... it's{italic} like a bad Woody Allen film{reset},",
        f"{italic}but with even more neurosis{reset} and{italic} worse cinematography{reset}."
    ]
    
    for line in quote_lines:
        # Random hesitation before each line
        time.sleep(random.uniform(0.1, 0.5))
        # Add occasional stutter effect
        if random.random() < 0.3:  # 30% chance of stutter
            words = line.split()
            if len(words) > 2:
                stutter_word = random.choice(words[1:-1])
                line = line.replace(stutter_word, f"{stutter_word}-{stutter_word.lower()}", 1)
        
        # Type the line with varying speed (anxious typing)
        typing_speed = random.uniform(0.02, 0.08)
        type_text(line, delay=typing_speed, color=yellow)
    
    # Animated ellipsis for dramatic pause
    print(f"\n{magenta}Thinking about it{reset}")
    animate_ellipsis(1.5)
    
    # Signature with self-deprecation
    print(f"\n{red}— Someone who probably shouldn't have written this{reset}")
    time.sleep(1)
    
    # Footer with existential warning
    print_border("━", width, cyan)
    warning = f"{blue}WARNING: This quote may cause existential dread, spontaneous weeping, and an overwhelming desire to call your therapist.{reset}"
    padding = (width - len("WARNING: This quote may cause existential dread...")) // 2
    print(f"{' ' * padding}{warning}")
    
    # Final touch - blinking cursor effect
    print(f"\n{green}Press any key to continue your meaningless existence...{reset}", end="", flush=True)
    try:
        input()
    except:
        pass

if __name__ == "__main__":
    try:
        woody_allen_quote()
    except KeyboardInterrupt:
        print(f"\n\n{red}Well, I guess even existence can be interrupted...{reset}")
    except Exception as e:
        print(f"\n{red}Even my existential crisis encountered an error: {e}{reset}")