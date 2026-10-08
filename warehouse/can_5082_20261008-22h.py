"""
Campbell's Soup Can #5082
Produced: 2026-10-08 22:04:26
Worker: Dots Studio: Dots3-Note Preview (free) (dots-studio/dots-3-note-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import os
import sys

# ANSI color codes
class Colors:
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_typing_effect(text, delay=0.03, color=Colors.YELLOW):
    """Print text with a typing effect"""
    for char in text:
        sys.stdout.write(color + char + Colors.RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def create_ascii_head():
    """Create a simple ASCII art head"""
    head = f"""
    {Colors.PURPLE}    , - ~ ' - , {Colors.RESET}
    {Colors.PURPLE}  '  _   _   '  {Colors.RESET}
    {Colors.PURPLE} (  ( ) ( ) ( ) {Colors.RESET}
    {Colors.PURPLE}  '  \___/   '  {Colors.RESET}
    {Colors.PURPLE}     |   |     {Colors.RESET}
    {Colors.PURPLE}    ===|===    {Colors.RESET}
    """
    return head

def create_border(text, border_color=Colors.BLUE):
    """Create a bordered box around text"""
    lines = text.split('\n')
    max_width = max(len(line) for line in lines)
    
    border_top = border_color + "┌" + "─" * (max_width + 2) + "┐" + Colors.RESET
    border_bottom = border_color + "└" + "─" * (max_width + 2) + "┘" + Colors.RESET
    
    result = [border_top]
    for line in lines:
        result.append(border_color + "│ " + Colors.RESET + line + 
                     " " * (max_width - len(line)) + 
                     border_color + " │" + Colors.RESET)
    result.append(border_bottom)
    
    return '\n'.join(result)

def main():
    # Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens.\n\n" + \
            "The problem with life is that there's no instruction manual.\n\n" + \
            "And the therapist says I have to stop thinking of myself as a victim.\n\n" + \
            "But how can you not be a victim when life keeps punching you in the face?"
    
    # Clear screen for dramatic effect
    clear_screen()
    
    # Print ASCII head
    print(create_ascii_head())
    time.sleep(1)
    
    # Print intro
    print(f"\n{Colors.CYAN}{Colors.BOLD}A philosophical musing by Woody Allen...{Colors.RESET}\n")
    time.sleep(1.5)
    
    # Print the quote with typing effect
    print_typing_effect(quote, delay=0.04, color=Colors.YELLOW)
    
    # Add some visual flair
    time.sleep(0.5)
    print(f"\n{Colors.RED}*{Colors.RESET} {Colors.PURPLE}Existential dread level: Maximum{Colors.RESET} {Colors.RED}*{Colors.RESET}")
    
    # Create bordered version
    time.sleep(1)
    clear_screen()
    
    print(f"{Colors.BLUE}{Colors.BOLD}=== THE FINAL THOUGHT ==={Colors.RESET}\n")
    print(create_border(quote))
    
    # Final message
    time.sleep(0.5)
    print(f"\n{Colors.GREEN}{Colors.BOLD}Remember: Life is short, but therapy is longer.{Colors.RESET}")
    
    # Keep window open for a moment
    time.sleep(3)

if __name__ == "__main__":
    main()