"""
Campbell's Soup Can #2140
Produced: 2026-02-09 19:40:57
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
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
import shutil

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    YELLOW = "\033[33m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    GREEN = "\033[32m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    WHITE = "\033[97m"
    BG_BLUE = "\033[44m"

def clear_screen():
    """Clear the terminal screen."""
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def get_terminal_size():
    """Get current terminal size."""
    return shutil.get_terminal_size()

def typewriter(text, color=Colors.WHITE, delay=0.03):
    """Print text with typewriter effect."""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.01, 0.01))
    print()

def draw_woody():
    """Draw a simple Woody Allen ASCII portrait."""
    woody = [
        "        .--.",
        "       |o_o |",
        "       |:_/ |",
        "      //   \\ \\",
        "     (|     | )",
        "    /'\\_   _/`\\",
        "    \\___)=(___/"
    ]
    for line in woody:
        print(Colors.BG_BLUE + Colors.WHITE + line + Colors.RESET)

def spinning_loader(seconds=2):
    """Display a spinning loader."""
    spinner = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    end_time = time.time() + seconds
    while time.time() < end_time:
        for char in spinner:
            sys.stdout.write('\r' + Colors.CYAN + f"Contemplating existence... {char}" + Colors.RESET)
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write('\r' + ' ' * 40 + '\r')
    sys.stdout.flush()

def main():
    clear_screen()
    
    # Get terminal dimensions
    term_width, term_height = get_terminal_size()
    
    # Center everything
    padding_x = max(0, (term_width - 60) // 2)
    padding_y = max(0, (term_height - 15) // 2)
    
    # Add vertical padding
    print("\n" * padding_y, end='')
    
    # Add horizontal padding
    print(" " * padding_x, end='')
    
    # Draw Woody
    draw_woody()
    print()
    
    # Add some dramatic pause
    spinning_loader(1.5)
    
    # Print the quote in a fancy box
    quote = [
        "I'm not afraid of death; I just don't want to",
        "be there when it happens. It's like going to",
        "the dentist: you know it's coming, but you",
        "keep hoping you can reschedule. And if you",
        "do die, what's the worst that can happen?",
        "You find out there's no afterlife, which",
        "would be a relief - finally, some peace and",
        "quiet. But what if there IS an afterlife?",
        "Then you have to spend eternity with all",
        "the people you tried to avoid in life.",
        "It's a lose-lose situation, really.",
        "",
        "Unless, of course, you get a really good",
        "book to read."
    ]
    
    author = "- A Neurotic Thought"
    
    # Calculate box dimensions
    max_len = max(len(line) for line in quote + [author])
    box_width = max_len + 8
    box_height = len(quote) + 4
    
    # Print top border
    print(" " * padding_x + Colors.YELLOW + "╔" + "═" * (box_width - 2) + "╗" + Colors.RESET)
    
    # Print quote with alternating colors
    for i, line in enumerate(quote):
        if line:  # Skip empty lines
            color = Colors.CYAN if i % 2 == 0 else Colors.GREEN
            padded_line = line.center(max_len)
            print(" " * padding_x + Colors.YELLOW + "║" + Colors.RESET + 
                  color + padded_line.center(box_width - 2) + Colors.RESET + 
                  Colors.YELLOW + "║" + Colors.RESET)
    
    # Empty line
    print(" " * padding_x + Colors.YELLOW + "║" + " " * (box_width - 2) + "║" + Colors.RESET)
    
    # Print author
    author_line = author.rjust(max_len)
    print(" " * padding_x + Colors.YELLOW + "║" + Colors.RESET + 
          Colors.MAGENTA + author_line.center(box_width - 2) + Colors.RESET + 
          Colors.YELLOW + "║" + Colors.RESET)
    
    # Print bottom border
    print(" " * padding_x + Colors.YELLOW + "╚" + "═" * (box_width - 2) + "╝" + Colors.RESET)
    
    # Add philosophical footer
    time.sleep(1)
    print("\n" + " " * padding_x + Colors.RED + 
          "「 The unexamined life is not worth living, " + 
          "but the over-examined life is exhausting. 」" + 
          Colors.RESET)
    
    # Add blinking cursor effect at the end
    for _ in range(3):
        sys.stdout.write('\r' + " " * padding_x + Colors.WHITE + "_" + Colors.RESET)
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\r' + " " * padding_x + " ")
        sys.stdout.flush()
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Colors.YELLOW + "Even interruption is a philosophical choice." + Colors.RESET)
        sys.exit(0)