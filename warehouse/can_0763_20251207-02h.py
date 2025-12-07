"""
Campbell's Soup Can #763
Produced: 2025-12-07 02:29:28
Worker: Amazon: Nova 2 Lite (free) (amazon/nova-2-lite-v1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def colorful_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def draw_boxed_quote():
    quote = "“If the universe is infinite, I’m just a speck of dust complaining about the weather.”"
    
    border_color = "36"  # Cyan
    text_color = "33"   # Yellow
    background = "44"   # Blue background for contrast
    reset = "\033[0m"
    
    width = len(quote) + 4
    horizontal = "═" * width
    top = f"╔{horizontal}╗"
    middle = f"║ {quote} ║"
    bottom = f"╚{horizontal}╝"
    
    print(colorful_text(top, border_color))
    time.sleep(0.3)
    print(f"\033[{background}m{colorful_text(middle, text_color)}\033[0m")
    time.sleep(0.3)
    print(colorful_text(bottom, border_color))
    
    print("\n" + colorful_text("...said nobody in therapy ever.", "35"))  # Magenta for afterthought

if __name__ == "__main__":
    draw_boxed_quote()