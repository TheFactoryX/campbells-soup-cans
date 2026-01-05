"""
Campbell's Soup Can #1414
Produced: 2026-01-05 19:31:59
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import os

# Clear screen if possible
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ANSI color codes
COLORS = {
    'red': '\033[91m',
    'orange': '\033[93m', 
    'dark_red': '\033[31m',
    'reset': '\033[0m',
    'bold': '\033[1m',
    'dim': '\033[2m',
    'purple': '\033[95m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'cyan': '\033[96m',
    'gray': '\033[90m'
}

# Woody Allen style quote
QUOTE = "I'm not afraid of death; I just don't want to be there when it happens."

def print_colored_text(text, color, bold=False, underline=False):
    color_code = COLORS.get(color, COLORS.get('bright_white'))
    bold_code = COLORS['bold'] if bold else ''
    reset = COLORS['reset']
    print(f"{color_code}{bold_code}{text}{reset}")

def print_cigarette():
    cigarette_art = """
                      @@@@@
                    @@@@@@@@@
                  @@@@@@@@@@@@@\\
                 @@@@@@@@:..@@@@@
                @@@@@@@@'  . @@@@
               @@@@@@@@'  . .@@@@
             @@@@@@@@.       .@@@@
            @@@@@@@@. .  .   @  @@@
           @@@@@@.   .   .   @@  @.
          @@@@@.   .    .    @@@@
         
    """
    
    # Print cigarette in gray tones
    lines = [s + COLORS['gray'] + line + COLORS['reset'] for line in cigarette_art.split('\\n')[:-1]]
    for line in lines:
        print(line)

def print_message_box():
    box_width = 70
    
    print(COLORS['yellow'] + "─" * box_width + COLORS['reset'])
    
    print_colored_text("┌" + "─" * (box_width - 2) + "┐", "yellow")
    
    # Prepare quote text with word wrapping
    words = QUOTE.split()
    line = ""
    
    spaces = " " * 25  # Padding inside box
    quote_lines = []
    for word in words:
        if len(line) + len(word) + 1 <= box_width - 30:
            line += word + " "
        else:
            quote_lines.append(spaces + line.center(box_width - 54))
            line = word + " "
    quote_lines.append(spaces + line.center(box_width - 54))
    
    for quote_line in quote_lines:
        print_colored_text("│" + " " * (box_width - 2) + "│", "yellow")
        print_colored_text("│" + " " * 10 + COLORS['dim'] + quote_line.center(box_width - 22) + COLORS['yellow'] + " " * (box_width - len(quote_line) - 22) + "│", "yellow")
        print_colored_text("│" + " " * (box_width - 2) + "│", "yellow")
    
    print_colored_text("└" + "─" * (box_width - 2) + "┘", "yellow")
    
    return

def print_header():
    
    header1 = "✧" + "," * 35 + "★" + "," * 34 + "✧" + "," 
    header2 = "{ Woody Allen's NeurosIs Corner }"
    header3 = "~*~*" * 25 + "~"
    
    print_colored_text("\n" + header1.center(80), "gray", bold=True)
    print_colored_text("\n" + header2.center(80).upper(), "purple", bold=True)
    print_colored_text("\n" + header3.center(80), "gray", bold=True)
    print()

def print_wavy_line():
    wavy = "≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈"
    print_colored_text(wavy, "purple", bold=True)
    print()

def print_footer():
    footer = "/)_/)  I survived another day of existence... barely.  /)_/)  " 
    corners = "◔_◔," * 5  
    print()
    print_colored_text(";" + corners.center(62) + ";", "gray", bold=True)
    print_colored_text(f"'{footer}'".center(80), "dark_red", bold=True)
    print()

def main():
    clear_screen()
    
    # Section separators
    print_header()
    
    print_wavy_line()
    
    print_colored_text(" "*20 + "Today's Dose of Existential Dread:", "red", bold=True)
    print()
    
    # Message box with quote
    print_message_box()
    
    print()
    print_colored_text(" "*15 + "** Just in case you were feeling too optimistic **", "dim")
    
    print()
    
    # Cigarette art
    print_cigarette()
    
    print_footer()
    
    print_colored_text("\n" + "✧".center(80) + "\n", "purple", bold=True)

if __name__ == "__main__":
    main()