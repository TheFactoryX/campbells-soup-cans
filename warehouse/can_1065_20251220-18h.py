"""
Campbell's Soup Can #1065
Produced: 2025-12-20 18:41:04
Worker: Tongyi DeepResearch 30B A3B (free) (alibaba/tongyi-deepresearch-30b-a3b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import textwrap
import os
import platform

def ansi_cursor_up(n):
    """Move cursor up n lines."""
    sys.stdout.write(f"\033[{n}A")

def ansi_cursor_down(n):
    """Move cursor down n lines."""
    sys.stdout.write(f"\033[{n}B")

def ansi_clear_line():
    """Clear current line."""
    sys.stdout.write("\033[2K\r")

def ansi_set_color(r, g, b):
    """Set text color using RGB."""
    return f"\033[38;2;{r};{g};{b}m"

def print_ascii_box(text, box_char='ₑ', theme="default"):
    """Print text inside an ASCII art box with optional theme coloring."""
    colors = {
        "woody": ["#2c3e50", "#3498db"],  # Dark blue gradient
        "neurotic": ["#e74c3c", "#c0392b"],  # Red for neuroticism
        "default": ["#16a085", "#1abc9c"]   # Green for default
    }
    
    foreground = colors[theme][0]
    background = colors[theme][1]
    
    lines = text.strip().split('\n')
    max_width = max(len(line) for line in lines)
    decoration = box_char * (max_width + 4)
    
    styled_box = (
        ansi_set_color(*[int(h) for h in foreground.lstrip('#').replace('x', '0')]) if foreground.startswith('#') else foreground + "m"
    )
    styled_bg = (
        ansi_set_color(*[int(h) for h in background.lstrip('#').replace('x', '0')]) if background.startswith('#') else background + "m"
    )
    
    sys.stdout.write(f"{styled_box}┌{decoration}┐\n")
    for line in lines:
        sys.stdout.write(f"│ {line.center(max_width)} │\n")
    sys.stdout.write(f"└{decoration}┘{ansi_set_color(0,0,0)}")
    sys.stdout.flush()

def slow_print(text, speed=0.02, end='\n'):
    """Print text slowly with decorative animation."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(end)
    sys.stdout.flush()

def clear_screen():
    """Clear the terminal screen."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def print_loading_animation(duration=2.0):
    """Print a fun loading animation."""
    spinner = "|/-\\"
    start = time.time()
    
    # Go to a fixed position
    sys.stdout.write("\033[3A")  # Move up 3 lines
    
    while time.time() - start < duration:
        for symbol in spinner:
            ansi_clear_line()
            sys.stdout.write(f"  Loading Woody Allen Wisdom... {symbol}  ")
            sys.stdout.flush()
            time.sleep(0.1)
    
    # Move cursor back to original position
    ansi_cursor_down(3)

def main():
    # Clear the screen first
    clear_screen()
    
    # Print initial ASCII art
    print("""
          ██╗██████╗ ███████╗ █████╗ ██╗   ██╗██████╗  █████╗ ██████╗ 
          ██║██╔══██╗██╔════╝██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗
          ██║██████╔╝███████╗███████║██║   ██║██████╔╝███████║██████╔╝
          ██║██╔═══╝ ╚════██║██╔══██║██║   ██║██╔══██╗██╔══██║██╔══██╗
          ██║██║       █████╔╝██║  ██║╚██████╔╝██║  ██║██║  ██║██║  ██║
          ╚═╝╚═╝       ╚════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
                                 Version 1.0
    """)
    
    # Game loading animation
    print_loading_animation()
    time.sleep(0.5)
    
    # Create a fancy box for the title
    title = "WOODY ALLEN QUOTE GENERATOR"
    print_ascii_box(f"{title}\n", theme="woody")
    
    # Generate and display the cool looping effect
    print("\n"*2)
    slow_print("...", 0.5)
    print()
    
    # Woody Allen style neurotic, existential quote
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. "
        "[technically more logical but doubly depressing]\n\n"
        "Maybe that's the trick: the more ridiculous life seems, the closer you are to truth. "
        "I tried meditation, but discovered I could only focus on whether I was doing it right. "
        "Being an actor is like masturbation: both do you good, but ultimately they don't get you anywhere. "
        "If you live long enough, you'll die. Kids: try and enjoy the journey before that happens."
    )
    
    # Wrap the quote to fit in the terminal
    wrapper = textwrap.TextWrapper(width=80)
    wrapped_lines = wrapper.wrap(quote)
    
    # Print the quote slowly line by line
    for line in wrapped_lines:
        slow_print(f"  {line.strip()}", 0.01)
        time.sleep(0.5)
    
    print()
    
    # ASCII art representing Woody's signature
    print_ascii_box("Signature: W.A\nHe/Him\nFOU")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nWoody Allen will finish his quote when he's good and ready...")
        sys.exit(0)