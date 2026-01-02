"""
Campbell's Soup Can #1345
Produced: 2026-01-02 14:36:31
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time, os, sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def set_color(color_code):
    print(f"\033[{color_code}m", end='')

class TerminalColor:
    BLACK = '30'
    RED = '31'  
    GREEN = '32'
    YELLOW = '33'
    BLUE = '34'
    PURPLE = '35'
    CYAN = '36'
    WHITE = '37'
    RESET = '0'
    BOLD = '1'
    DIM = '2'

def print_colored(text, color=TerminalColor.GREEN):
    set_color(color)
    print(text)
    set_color(TerminalColor.RESET)

def draw_woody():
    print()
    print_colored("        ╔════════════════════════════════════════╗", TerminalColor.GREEN)
    print_colored("        ║     WOODY ALLEN'S EXISTENTIAL         ║", TerminalColor.GREEN)
    print_colored("        ║        OBSERVATION CORNER             ║", TerminalColor.GREEN)
    print_colored("        ╚════════════════════════════════════════╝", TerminalColor.GREEN)
    print_colored("", TerminalColor.RESET)
    time.sleep(0.5)
    print()

def animate_text():
    clear_screen()
    
    set_color(TerminalColor.RESET)
    print_colored("", TerminalColor.RESET)
    
    draw_woody()
    
    set_color(TerminalColor.GREEN | TerminalColor.BOLD)
    print_colored("🎬", TerminalColor.PURPLE) 
    slow_print("     Woody Allen is typing...", 0.2)
   
    time.sleep(1.5)
    clear_screen()
    draw_woody()
    
    slow_print("✨", 0.3)
    slow_print("✨ ✨", 0.25)
    slow_print("✨ ✨ ✨", 0.2)
    slow_print("✨ ✨ ✨ ✨", 0.15)
    slow_print("", 0.1)
    
    print_colored("✨", TerminalColor.PURPLE)
    set_color(TerminalColor.PURPLE | TerminalColor.BOLD)
    
    time.sleep(1)
    clear_screen()
    draw_woody()
    
    time.sleep(0.5)
    quote_lines = [
        "  \"",
        "  I'm plagued by existential dread",  
        "  and the terrifying realization that",
        "  we're all hurtling toward oblivion...", 
        "",
        "  But frankly, my biggest worry is",
        "  what if there's an afterlife and",
        "  I still have to pay taxes there?",
        "\""
    ]
    
    for line in quote_lines:
        if line.strip():
            print_colored(line, TerminalColor.CYAN)
        else:
            print(line)
        time.sleep(0.4)
    print()
    
    time.sleep(0.5)
    
    frame_parts = ["╭", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","─","╮"]
    print_colored("".join(frame_parts), TerminalColor.YELLOW)
    
    time.sleep(0.2)
    
    border_line = ["│"] + [" "] * 78 + ["│"]
    for i in range(74):
        time.sleep(0.01)
        border_line[i+1] = "╍"
        print_colored("│", TerminalColor.YELLOW, end="")
        for j in range(78):
            if j <= i:
                print_colored("╍", TerminalColor.YELLOW, end="")
            else:
                print(" ", end="")
        print_colored("│", TerminalColor.YELLOW)
        print("\r", end="")
    print()
    
    line_parts = ["╰", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─", "─"] 
    for i in range(35):
        line_parts.append("─")
    line_parts.append("╯")
    slow_print("".join(line_parts), 0.01)
    time.sleep(0.2)
    
    time.sleep(2)
    print_colored("", TerminalColor.RESET)
    print()
    
if __name__ == "__main__":
    animate_text()