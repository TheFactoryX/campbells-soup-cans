"""
Campbell's Soup Can #46
Produced: 2025-11-04 08:45:02
Worker: Google: Gemini 2.5 Flash Lite Preview 06-17 (google/gemini-2.5-flash-lite-preview-06-17)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def animate_text(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def colorful_quote(quote):
    colors = [
        '\033[91m', '\033[92m', '\033[93m', '\033[94m',
        '\033[95m', '\033[96m', '\033[31m', '\033[32m',
        '\033[33m', '\033[34m', '\033[35m', '\033[36m'
    ]
    reset_color = '\033[0m'
    
    colored_chars = []
    for i, char in enumerate(quote):
        if char.isspace():
            colored_chars.append(char)
        else:
            color_code = random.choice(colors)
            colored_chars.append(f"{color_code}{char}{reset_color}")
    return "".join(colored_chars)

def woody_allen_esque_quote():
    quotes = [
        "If you can't find happiness in the mundane, you're probably just better off staying in bed and contemplating the futility of it all. And even then, you'll probably forget where you put your glasses.",
        "The universe is a vast, uncaring void, and our brief existence is a cosmic accident. So, you know, try not to spill your coffee. It’s a real downer.",
        "I used to think I was a bit of a hypochondriac, but then I realized I was just accurately assessing my impending doom. It's a subtle distinction, really.",
        "Love is a beautiful, terrifying thing. It's like a really good brisket – takes a lot of effort, and you're never quite sure if it's going to turn out properly, but when it does, oh boy.",
        "My therapist told me I need to embrace my problems. So I gave them a hug. They seemed a little surprised and asked if they could borrow fifty bucks. Typical."
    ]
    return random.choice(quotes)

def ascii_box(text, width=70):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    
    line_length = max(max_len, width)
    
    top_bottom_border = "╔" + "═" * (line_length + 2) + "╗"
    middle_border = "║" + "═" * (line_length + 2) + "║"
    bottom_border = "╚" + "═" * (line_length + 2) + "╝"
    
    print(top_bottom_border)
    
    for line in lines:
        padding_needed = line_length - len(line)
        print(f"║ {line}{' ' * padding_needed} ║")
    
    print(bottom_border)

def typewriter_animation(text, delay=0.03):
    for i in range(len(text) + 1):
        print(text[:i], end='\r')
        time.sleep(random.uniform(delay/2, delay*2)) 
    print()
    
if __name__ == "__main__":
    print("\n" * 2)
    print(" " * 20 + "\033[96m" + "Welcome to the existential dread simulator!" + "\033[0m")
    print("\n" * 2)
    
    quote_text = woody_allen_esque_quote()
    
    boxed_quote = []
    for word in quote_text.split():
        boxed_quote.append(colorful_quote(word))
    
    final_quote_string = " ".join(boxed_quote)
    
    line_length = 70
    wrapped_lines = []
    current_line = ""
    
    for word in final_quote_string.split():
        if len(current_line) + len(word) + 1 <= line_length:
            current_line += word + " "
        else:
            wrapped_lines.append(current_line.strip())
            current_line = word + " "
    wrapped_lines.append(current_line.strip())

    formatted_quote = "\n".join(wrapped_lines)

    print("\033[93m" + "=" * 80 + "\033[0m")
    ascii_box(formatted_quote)
    print("\033[93m" + "=" * 80 + "\033[0m")
    
    print("\n" * 2)
    fade_out_text = "Pondering... reality... it's a complex business."
    for i in range(len(fade_out_text) + 1):
        print("\033[95m" + fade_out_text[:i] + "\033[0m", end='\r')
        time.sleep(0.08)
    print("\n")