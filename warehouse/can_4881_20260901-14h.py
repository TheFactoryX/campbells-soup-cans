"""
Campbell's Soup Can #4881
Produced: 2026-09-01 14:54:22
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

# ANSI color codes
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, delay=0.03, color=Colors.YELLOW):
    """Type out text character by character with a delay"""
    for char in text:
        print(color + char + Colors.RESET, end='', flush=True)
        time.sleep(delay)
    print()

def create_ascii_head():
    """Create a simple ASCII art head"""
    head = f"""
    {Colors.BOLD}{Colors.MAGENTA}
        ┌─────┐
        │  o  o │
        │   ^   │
        │  ─── │
        └─────┘
    {Colors.RESET}
    """
    return head

def create_anxiety_meter():
    """Create a visual anxiety meter"""
    meter = f"""
    {Colors.RED}Anxiety Level: {Colors.BOLD}████████░░{Colors.RESET}
    {Colors.YELLOW}Existential Dread: {Colors.BOLD}██████████{Colors.RESET}
    {Colors.CYAN}Self-Awareness: {Colors.BOLD}█████░░░░░{Colors.RESET}
    """
    return meter

def main():
    # The Woody Allen style quote
    quote = "I'm not afraid of death; I just don't want to be there when it happens. \
Actually, I'm terrified of death, but I'm even more terrified of living in a world \
where I have to keep going to those terrible dinner parties with people who talk \
about their investments and their hernias. The universe is cold and indifferent, \
and yet I still have to show up for my therapy appointments. Life is just a series \
of increasingly disappointing birthday parties, and I'm the only one who remembers \
that it's all meaningless. But hey, at least I'm consistent in my misery."

    # Clear screen for dramatic effect
    clear_screen()
    
    # Print ASCII head
    print(create_ascii_head())
    time.sleep(0.5)
    
    # Print a neurotic introduction
    print(f"\n{Colors.BOLD}{Colors.CYAN}Well, let me think about this...{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.YELLOW}Hmm, this is a difficult philosophical question...{Colors.RESET}")
    time.sleep(1.5)
    print(f"{Colors.RED}Actually, I'm having a panic attack just thinking about it.{Colors.RESET}")
    time.sleep(1)
    
    # Print anxiety meter
    print(f"\n{create_anxiety_meter()}")
    time.sleep(1)
    
    # Print the quote with dramatic typing effect
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}Here's what I really think:{Colors.RESET}\n")
    
    # Split quote into sentences for dramatic pauses
    sentences = quote.split('. ')
    for i, sentence in enumerate(sentences):
        if i < len(sentences) - 1:
            sentence += '.'
        
        # Random color for each sentence to show emotional instability
        colors = [Colors.RED, Colors.YELLOW, Colors.BLUE, Colors.MAGENTA, Colors.CYAN]
        color = random.choice(colors)
        
        type_text(sentence, delay=0.04, color=color)
        time.sleep(0.3)
    
    # Neurotic ending
    print(f"\n{Colors.YELLOW}...Or maybe I'm just being paranoid. What do I know?{Colors.RESET}")
    time.sleep(1)
    print(f"{Colors.RED}Why am I even talking about this? I should be home watching television.{Colors.RESET}")
    time.sleep(1)
    
    # Final dramatic flourish
    print(f"\n{Colors.BOLD}{Colors.MAGENTA}The End. (Or is it?){Colors.RESET}")
    
    # Blinking text for extra anxiety
    for _ in range(3):
        print(f"{Colors.BLINK}{Colors.RED}Please don't leave me alone with my thoughts...{Colors.RESET}")
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.3)

if __name__ == "__main__":
    main()