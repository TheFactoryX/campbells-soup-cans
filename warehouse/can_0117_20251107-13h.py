"""
Campbell's Soup Can #117
Produced: 2025-11-07 13:39:15
Worker: DeepSeek: DeepSeek R1 0528 Qwen3 8B (free) (deepseek/deepseek-r1-0528-qwen3-8b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys

def print_styled_text(text, style=('rainbow', 'bold'), delay=0.1):
    # Clear screen with escape sequence
    print("\033c", end="")
    
    def rainbow_effect(char):
        colors = [
            '', '\033[95m', '', '\033[96m', 
            '\033[97m', '\033[91m', '\033[93m', '\033[92m'
        ]
        idx = (ord(char) + 1000) % (len(colors) * 10) // len(colors)
        return f"{colors[idx]}{char}\033[0m"
    
    def bold_effect(char):
        return f"\033[1m{char}\033[0m"
    
    effects = {
        'rainbow': rainbow_effect,
        'bold': bold_effect,
        'invert': lambda char: f"\033[7m{char}\033[0m"
    }
    
    # Create visual pattern effects
    pattern = ""
    for i in range(len(text)):
        pattern += text[i] * 3
    
    # Initial inverted text
    print("\n\n\033[7m", end="")
    
    # Print character by character with style
    for char in text:
        stylized_char = effects[style](char) if style in effects else char
        print(stylized_char, end='', flush=True)
        time.sleep(delay)
        sys.stdout.flush()
    
    print("\n\n", end="")
    
    # Draw ASCII heart below
    for i in range(7, -1, -1):
        print(" " * ((7-i)*2-2) + "\033[91m" + ("*" if i>2 else "").join([
            "\033[91m" + ("0" if i>=3 else "1")*2,
            "\\" if i>=2 else "/",
            "  " + (((i >= 4) and "0" or "1") + "  " if i < length//2 else ""),
            "\\" if i>=1 else "/"
        ]), "\033[0m", flush=True)
        time.sleep(0.5)

# Main quote with interactive setup
quote = "I'm not afraid of death;\033[31mI'm afraid of life\033[0m. \033[4mLife\033[0m is full of misery, loneliness, and suffering — and it's all over much too soon."

print("\033[2J\033[1;1H")  # Clear screen and move cursor to top-left

print("\n\n")
print("\033[1m" + "="*50 + "\033[0m")
print("\033[3m" + "\033[1;36mPHILOSOPHICAL QUOTE\033[0m".center(50) + "\n" + "="*50 + "\033[0m")
print("\033[0m")

while True:
    try:
        input_style = input("\033[32mEnter text effect (rainbow, bold, invert): \033[0m")
        if input_style.lower() in ['rainbow', 'bold', 'invert']:
            print("\n")
            print_styled_text(quote, input_style)
            print("\n\033[1;37m" + "="*50 + "\033[0m")
            time.sleep(3)
        else:
            print("\033[31mPlease choose from rainbow, bold, or invert.\033[0m")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\033[1mGoodbye, neurotic philosopher!\033[0m")
        break
    except EOFError:
        print("\n\033[1mGoodbye, neurotic philosopher!\033[0m")
        break

sys.exit(0)