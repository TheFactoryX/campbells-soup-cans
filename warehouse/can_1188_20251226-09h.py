"""
Campbell's Soup Can #1188
Produced: 2025-12-26 09:35:19
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
Woody Allen Style Philosophical Quote Generator
A neurotic, existential, and visually entertaining quote display
"""

import time
import random
import sys
import shutil

def clear_console():
    """Clear the console screen"""
    print("\033c", end="")

def get_terminal_width():
    """Get the current terminal width"""
    return shutil.get_terminal_size().columns

def slow_print(text, delay=0.06):
    """Print text with a typewriter effect"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def animate_border(width, duration=1.0):
    """Animate a decorative border"""
    steps = 10
    for i in range(steps):
        border_char = "█" if i % 2 == 0 else "▓"
        border = border_char * width
        print(f"\033[35m{border}\033[0m")
        time.sleep(duration / steps)
        if i < steps - 1:
            print("\033[1A", end="")  # Move cursor up

class NeuroticColors:
    """ANSI color codes for our neurotic display"""
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

def draw_thinker_ascii():
    """Draw an ASCII art thinker (but make it look worried)"""
    thinker = [
        "      " + NeuroticColors.BOLD + NeuroticColors.PURPLE + "__" + NeuroticColors.RESET,
        "     " + NeuroticColors.BOLD + NeuroticColors.PURPLE + "/" + NeuroticColors.DIM + "o o" + NeuroticColors.RESET + NeuroticColors.BOLD + NeuroticColors.PURPLE + "\\" + NeuroticColors.RESET,
        "     " + NeuroticColors.BOLD + "(" + NeuroticColors.CYAN + "  ╯" + NeuroticColors.BOLD + " )" + NeuroticColors.RESET,
        "      " + NeuroticColors.BOLD + ">" + NeuroticColors.YELLOW + "~" + NeuroticColors.BOLD + "<" + NeuroticColors.RESET,
    ]
    return '\n'.join(thinker)

def create_speech_bubble(text, max_width=50):
    """Create a speech bubble around the text"""
    words = text.split()
    lines = []
    current_line = ""
    
    for word in words:
        if len(current_line) + len(word) + 1 <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    
    # Find the longest line
    max_line_length = max(len(line) for line in lines) if lines else 0
    width = min(max_line_length + 4, max_width + 4)
    
    bubble = []
    bubble.append(" " + "▔" * (width - 2))
    for line in lines:
        bubble.append(f"  {line.ljust(width - 4)}  ")
    bubble.append(" " + "▁" * (width - 2))
    bubble.append("   \\")
    bubble.append("    \\")
    
    return '\n'.join(bubble)

def generate_quote():
    """Generate a Woody Allen style quote"""
    quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "The universe is merely a fleeting idea in God's mind - a pretty uncomfortable thought, particularly if you've just made a down payment on a house.",
        "I'm plagued by doubts. What if everything is an illusion and nothing exists? In that case, I definitely overpaid for my carpet.",
        "Time is nature's way of keeping everything from happening at once. Unfortunately, it doesn't work very well in my anxiety attacks.",
        "If God exists, I hope he has a good excuse.",
        "Eternal nothingness is fine if you happen to be dressed for it.",
        "I took a speed reading course and read 'War and Peace' in twenty minutes. It involves Russia.",
        "I'm not a quitter. I've been fired from jobs I've never even started."
    ]
    
    return random.choice(quotes)

def main():
    """Main program execution"""
    try:
        clear_console()
        width = get_terminal_width()
        
        # Animate border
        print("\n")
        animate_border(width, 0.8)
        
        # Display title
        title = NeuroticColors.BOLD + NeuroticColors.GREEN + "✨ Woody Allen's Neurotic Corner ✨" + NeuroticColors.RESET
        padding = (width - len("✨ Woody Allen's Neurotic Corner ✨")) // 2
        print(" " * padding + title)
        print()
        
        # Pick a quote
        quote = generate_quote()
        
        # Display thinker with speech bubble
        print(NeuroticColors.DIM + " " * (padding - 15) + draw_thinker_ascii() + NeuroticColors.RESET)
        
        # Slow print the speech bubble
        speech_bubble = create_speech_bubble(quote, width // 2)
        print(NeuroticColors.CYAN + speech_bubble + NeuroticColors.RESET)
        
        # Slow print the actual quote
        print()
        time.sleep(0.5)
        slow_print(NeuroticColors.BOLD + NeuroticColors.YELLOW + '"' + quote + '"' + NeuroticColors.RESET, 0.04)
        
        # Add signature
        print()
        padding = (width - 20) // 2
        time.sleep(0.3)
        slow_print(" " * padding + NeuroticColors.DIM + "— some neurotic guy from Manhattan" + NeuroticColors.RESET, 0.02)
        
        # Final animation
        print("\n")
        animate_border(width, 0.6)
        
        # Wait a bit before clearing
        time.sleep(3)
        clear_console()
        
        # Final message
        print("\n" * 2)
        slow_print(NeuroticColors.BOLD + "Thanks for visiting my existential crisis corner!" + NeuroticColors.RESET)
        slow_print(NeuroticColors.DIM + "(Don't worry, I'm seeing my analyst about it...)" + NeuroticColors.RESET)
        print("\n" * 2)
        
    except KeyboardInterrupt:
        clear_console()
        print("\n" + NeuroticColors.RED + "Alright, alright, I'll stop... sheesh." + NeuroticColors.RESET + "\n")
        sys.exit(0)
    except Exception as e:
        clear_console()
        print(f"\n{NeuroticColors.RED}Well, this is embarrassing. My existential crisis just crashed: {e}{NeuroticColors.RESET}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()