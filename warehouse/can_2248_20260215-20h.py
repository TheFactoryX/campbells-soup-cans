"""
Campbell's Soup Can #2248
Produced: 2026-02-15 20:44:07
Worker: Qwen: Qwen3 235B A22B Thinking 2507 (qwen/qwen3-235b-a22b-thinking-2507)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def main():
    width = 50
    inner_content_width = width - 2
    
    # ANSI escape codes
    border_color = "\033[93m"  # Bright yellow
    quote_color = "\033[96m"   # Bright cyan
    title_bg = "\033[44m"      # Blue background
    title_fg = "\033[97m"      # White text
    reset = "\033[0m"
    blink = "\033[5m"          # Blinking effect for existential dread

    # Clear screen and move cursor to top
    print("\033[2J\033[H", end='', flush=True)
    
    # Create Woody Allen style quote (neurotic and self-deprecating)
    quote_lines = [
        "I'm not afraid of death; I just don't want to be there",
        "when it happens... and frankly, the existential ",
        "dread buffet is terrible for my digestion."
    ]

    # Top border with blinking corners for anxiety
    print(blink + border_color + '+' + '-' * width + '+' + reset, flush=True)
    
    # Title with dramatic background
    title = "WOODY ALLEN'S EXISTENTIAL CRISIS HOUR"
    left_pad = (width - len(title)) // 2
    right_pad = width - len(title) - left_pad
    print(
        border_color + '|' + ' ' * left_pad + 
        title_bg + title_fg + title + reset + 
        border_color + ' ' * right_pad + '|' + reset,
        flush=True
    )
    print(border_color + '+' + '-' * width + '+' + reset, flush=True)
    
    # Empty content area with nervous energy
    for _ in range(5):
        time.sleep(0.05)
        print(border_color + '|' + ' ' * width + '|' + reset, flush=True)
    
    # Bottom border
    print(border_color + '+' + '-' * width + '+' + reset, flush=True)
    
    # Move cursor up to quote position (4 lines up from current position)
    print("\033[5A", end='', flush=True)
    
    # Position at quote area (2 columns in from left border)
    print("\033[2C", end='', flush=True)
    
    # Neurotic blinking quote with uneven typing speed
    print(quote_color, end='', flush=True)
    for i, line in enumerate(quote_lines):
        # Center each line with neurotic precision
        padding = (inner_content_width - len(line)) // 2
        print(' ' * padding, end='', flush=True)
        
        # Type with Woody's nervous rhythm (faster for mundane words, slower for existential dread)
        for j, char in enumerate(line):
            delay = 0.02 if char in " ,.;'aeiou" else 0.07
            print(char, end='', flush=True)
            time.sleep(delay)
        
        # Move to next line with anxious hesitation
        if i < len(quote_lines) - 1:
            time.sleep(0.3)
            print(f"\033[B\033[{2}C", end='', flush=True)
            time.sleep(0.5)
    
    # Add final existential sigh
    print(reset + "\n" + border_color + "  Life: 50% panic attack, 50% wondering why the" + reset, flush=True)
    print(border_color + "  cheese platter isn't enough to solve mortality." + reset + "\n", flush=True)
    
    # Blinking "The End" with resignation
    time.sleep(1)
    print(blink + border_color + "\n     The End (probably)" + reset, flush=True)
    time.sleep(1.5)

if __name__ == "__main__":
    main()