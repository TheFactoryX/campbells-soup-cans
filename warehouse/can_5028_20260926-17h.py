"""
Campbell's Soup Can #5028
Produced: 2026-09-26 17:11:32
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen-style Philosophical Quote Generator
A neurotic little program about existence and the absurdity of it all.
"""

import sys
import time
import shutil

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def clear_screen():
    """Clear the screen in a neurotic way."""
    print("\033[2J\033[H", end="")

def get_centered_text(text, width):
    """Center text within a given width, worrying about alignment constantly."""
    return text.center(width)

def animate_dots(text, duration=2.0):
    """Animate dots appearing after text, like anxious thoughts."""
    sys.stdout.write(text)
    sys.stdout.flush()
    
    start_time = time.time()
    dots = 0
    
    while time.time() - start_time < duration:
        if dots < 3:
            sys.stdout.write('.')
            sys.stdout.flush()
            dots += 1
        else:
            # Erase the dots
            for _ in range(3):
                sys.stdout.write('\b \b')
                sys.stdout.flush()
            dots = 0
        time.sleep(0.4)
    
    # Final cleanup
    sys.stdout.write('   ')
    sys.stdout.flush()
    print()

def print_with_delay(text, delay=0.03):
    """Print text character by character, very slowly and deliberately."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def type_writer_effect(text, delay=0.05):
    """Simulate typing with a typewriter, occasionally stuttering."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        
        # Occasional hesitant pause
        if char in '.!?':
            time.sleep(delay * 10)
        elif char == ',':
            time.sleep(delay * 5)
        elif ord(char) % 7 == 0:  # Random-ish hesitation
            time.sleep(delay * 3)
        else:
            time.sleep(delay)
    
    print()

def draw_woody_frame(width=60, height=15):
    """Draw a neurotic frame around the content."""
    print(f"{Colors.MAGENTA}{Colors.BOLD}", end="")
    
    # Top border with little worries
    top_border = "╔" + "═" * width + "╗"
    print(get_centered_text(top_border, shutil.get_terminal_size().columns))
    
    # Content area with existential dread
    for i in range(height):
        if i == 1:
            content = f"║{Colors.YELLOW}{' ' * 5}🌙 A Woody Allen Production 🌙"
            content += f"{Colors.MAGENTA}{' ' * max(1, width - 25)}" + "║"
            print(get_centered_text(content, shutil.get_terminal_size().columns))
        elif i == height // 2 - 1:
            quote = 'I believe that only thing that is really certain'
            quote2 = 'in life is that we are all going to die'
            quote3 = 'and I am not even sure about that.'
            inner_width = width - 4
            print(get_centered_text(f"║{Colors.CYAN}{' ' * max(1, (inner_width - len(quote))//2)}{quote}", shutil.get_terminal_size().columns))
            print(get_centered_text(f"{Colors.CYAN}{' ' * max(1, (inner_width - len(quote2))//2)}{quote2}", shutil.get_terminal_size().columns))
            print(get_centered_text(f"{Colors.CYAN}{' ' * max(1, (inner_width - len(quote3))//2)}{quote3}", shutil.get_terminal_size().columns))
        elif i == height - 2:
            content = f"║{Colors.YELLOW}{' ' * 5}🎭 Mortality Comedy Division 🎭"
            content += f"{Colors.MAGENTA}{' ' * max(1, width - 28)}" + "║"
            print(get_centered_text(content, shutil.get_terminal_size().columns))
        else:
            empty_line = "║" + " " * width + "║"
            print(get_centered_text(empty_line, shutil.get_terminal_size().columns))
    
    # Bottom border
    bottom_border = "╚" + "═" * width + "╝"
    print(get_centered_text(bottom_border, shutil.get_terminal_size().columns))
    
    print(f"{Colors.RESET}", end="")

def main():
    """Main function that contemplates its own existence."""
    
    # Start with existential crisis
    clear_screen()
    
    # Animated title sequence
    print(f"\n{Colors.CYAN}")
    print_with_delay("  ⚡️ Loading existential dread...", 0.04)
    
    print(f"\n{Colors.MAGENTA}")
    animate_dots("  Initializing anxiety levels", 1.5)
    
    print(f"\n{Colors.RED}")
    print_with_delay("  Calibrating pessimism settings...", 0.03)
    time.sleep(0.8)
    
    # Clear and prepare for the main presentation
    time.sleep(1)
    clear_screen()
    
    # Present the quote with theatrical flair
    print()
    
    # Dramatic quote presentation
    quote_lines = [
        "    ┌─────────────────────────────────────────────┐",
        "    │                                             │",
        "    │   I took a speed-reading course and          │",
        "    │   read 500 books in one day.                 │",
        "    │   Of course, I was reading                   │",
        "    │   them in the phone book.                    │",
        "    │                                             │",
        "    │   - Woody Allen (probably)                   │",
        "    │                                             │",
        "    └─────────────────────────────────────────────┘"
    ]
    
    # Print with color cycling effect
    colors = [Colors.YELLOW, Colors.CYAN, Colors.MAGENTA, Colors.RED, Colors.GREEN]
    
    for i, line in enumerate(quote_lines):
        color = colors[i % len(colors)]
        print(f"{color}{line}")
        time.sleep(0.2)
    
    print(f"{Colors.RESET}")
    
    # Final existential thought
    print()
    print(f"{Colors.MAGENTA}{'=' * 50}")
    print(f"{Colors.YELLOW}  Afterthought: This program will eventually crash,")
    print(f"{Colors.YELLOW}  just like everything else in the universe. But hey,")
    print(f"{Colors.YELLOW}  at least it's consistent about its impermanence.")
    print(f"{Colors.MAGENTA}{'=' * 50}")
    print(f"{Colors.RESET}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}Interrupted! Just like my therapy sessions.{Colors.RESET}")
        sys.exit(1)