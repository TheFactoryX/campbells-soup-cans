"""
Campbell's Soup Can #2349
Produced: 2026-02-21 07:45:28
Worker: Baidu: ERNIE 4.5 VL 28B A3B (baidu/ernie-4.5-vl-28b-a3b)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_colored(text, color_code):
    """Print text in a specified ANSI color."""
    sys.stdout.write(f"\033[{color_code}m{text}\033[0m\n")

def box_quote(quote):
    """Print a quote inside a box with decorations."""
    border = "🔷 "  # Woody might use fancy symbols!
    边框长度 = len(border)
    
    # Calculate box size based on the quote length
    quote_length = len(quote)
    box_size = max(10, quote_length + 4)  # Make sure it's not super tiny
    
    # Center the quote within the box
    left_padding = (box_size - len(quote)) // 2
    quote = " " * left_padding + quote

    print(border + " Woody Allen Quotefu 🔸 " + border)
    print(" " * (len(border) + 8) + "✨✨✨✨✨✨✨✨✨✨✨✨")
    for _ in range(3):  # Animate the box with waves
        time.sleep(0.5)
        print("")
        print(" " * (len(border) + 8) + "*" * 12)
        print(" " * (len(border) + 8) + "* " + quote.replace("\n", "\n" + " " * (len(border) + 10)) + " *")
        print(" " * (len(border) + 8) + "*" * 12)
    print("")
    print(" " * (len(border) + 8) + "✨✨✨✨✨✨✨✨✨✨✨✨")
    print(border + " End Quotefu 🔸 " + border)

def main():
    """Main function with a creative animation."""
    animate_quotes = [
        "I'm not afraid of death; I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I'll sleep well tonight.. in a graveyard. That way, if they make noise, they're just tombstones rattling."
    ]
    
    for i in range(3):  # Letter-by-letter animation for intro
        print(" " * 10, end="", flush=True)
        time.sleep(0.1)
    
    print_colored("🌌 QUOTEFU 🌠", "35")  # Magenta
    time.sleep(1)
    
    quote = animate_quote_selector(animate_quotes)  # Cycle through quotes with a slight delay
    box_quote(quote)

def animate_quote_selector(quotes):
    """Animate cycling through the list of quotes."""
    for i in range(len(quotes)):
        print_colored(f"Selecting Quote #{i+1} ... ", "33")  # Blue
        time.sleep(0.8)
        return quotes[i % len(quotes)]

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_colored("\nQuoteFU was interrupted by you! Goodnight.", "31")  # Red
        sys.exit(0)