"""
Campbell's Soup Can #1332
Produced: 2026-01-01 23:32:12
Worker: Z.AI: GLM 4.5 Air (free) (z-ai/glm-4.5-air:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
import time
import sys
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write('\n')

def color_text(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def box_border(text, width=70):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    border = '+' + '-' * (max_len + 2) + '+'
    
    result = [border]
    for line in lines:
        result.append('| ' + line.ljust(max_len) + ' |')
    result.append(border)
    return '\n'.join(result)

def main():
    # ASCII art of Woody Allen's glasses
    glasses = """
    .-.
    |o|
    '`
    """
    
    # Quote with different colors for different parts
    quote = f"""
{color_text(glasses, '33')}  {color_text("I've always wanted to be someone,", '36')}
    {color_text("but I think I should have been more specific.", '37')}

    {color_text("The existential dread is overwhelming,", '35')}
    {color_text("at least when I remember to be anxious about it.", '36')}

    {color_text("I suppose I could find meaning in the universe,", '37')}
    {color_text("but I'm still looking for my keys.", '35')}
    """
    
    # Frame the quote
    framed_quote = box_border(quote.strip())
    
    # Add title
    title = color_text("\nWOODY ALLEN ON EXISTENTIAL CRISES", '31;1')
    
    # Animation sequence
    clear_screen()
    typewriter(title, 0.05)
    time.sleep(1)
    
    for i in range(3):
        print(color_text(".", '33'), end='')
        sys.stdout.flush()
        time.sleep(0.3)
    print()
    
    # Display the quote with a typewriter effect
    clear_screen()
    typewriter(title, 0.03)
    time.sleep(0.5)
    
    lines = framed_quote.split('\n')
    for line in lines:
        typewriter(line, 0.01)
    
    # Add a final thought
    time.sleep(1)
    final_thought = color_text("\n\nPS - If you're not neurotic, you're not paying attention.\n", '32;3')
    typewriter(final_thought, 0.05)
    
    # Blinking cursor effect
    for _ in range(3):
        print(color_text("█", '32'), end='')
        sys.stdout.flush()
        time.sleep(0.3)
        print(color_text(" ", '32'), end='')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

if __name__ == "__main__":
    main()