"""
Campbell's Soup Can #1212
Produced: 2025-12-27 11:27:51
Worker: Nex AGI: DeepSeek V3.1 Nex N1 (free) (nex-agi/deepseek-v3.1-nex-n1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def clear():
    print("\033[H\033[J", end="")

def move_cursor(y, x):
    print(f"\033[{y};{x}H", end="")

def set_color(r, g, b, background=False):
    code = 48 if background else 38
    print(f"\033[{code};2;{r};{g};{b}m", end="")

def reset_color():
    print("\033[0m", end="")

def draw_pixel_art():
    # Woody Allen caricature-inspired text art
    print("      \\_/")
    print("     (o.o)")
    print("      |=|")
    print("     /   \\")
    print("    /     \\")
    print("   /       \\")
    print("  |  •   •  |")
    print("  |    ∆    |")
    print("   \\  ___  /")
    print("    \\_____/")

def draw_box(text, padding=2):
    lines = text.split('\n')
    max_len = max(len(line) for line in lines)
    width = max_len + padding * 2
    
    # Top border
    set_color(139, 69, 19)
    print("╔" + "═" * (width + 2) + "╗")
    reset_color()
    
    # Empty line
    set_color(255, 248, 220, True)
    set_color(139, 69, 19)
    print("║" + " " * (width + 2) + "║")
    reset_color()
    
    # Text lines
    for line in lines:
        set_color(255, 248, 220, True)
        set_color(139, 69, 19)
        print("║ ", end="")
        set_color(0, 0, 0)
        print(line.center(max_len), end="")
        set_color(139, 69, 19)
        print(" ║")
        reset_color()
    
    # Empty line
    set_color(255, 248, 220, True)
    set_color(139, 69, 19)
    print("║" + " " * (width + 2) + "║")
    reset_color()
    
    # Bottom border
    set_color(139, 69, 19)
    print("╚" + "═" * (width + 2) + "╝")
    reset_color()

def type_text(text, delay=0.08):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def draw_notes():
    set_color(218, 165, 32)
    print("    ♪ ♫ ♪ ♫ ♪ ♫ ♪ ♫ ♪")
    reset_color()

def animate_thoughts():
    thoughts = [
        "thinking neurotically...",
        "pondering existence...",
        "worrying about mortality...",
        "questioning everything...",
        "overanalyzing life..."
    ]
    
    for i in range(10):
        thought = random.choice(thoughts)
        set_color(100 + i*15, 100 + i*10, 100 + i*5)
        print(f"({thought})", end="\r", flush=True)
        time.sleep(0.3)
    print(" " * 50, end="\r")

def main():
    clear()
    
    # Set background color
    print("\033[48;2;245;245;220m")
    
    print("\n\n")
    
    # Title
    move_cursor(3, 30)
    set_color(139, 0, 0)
    print("𝑾𝒐𝒐𝒅𝒚 𝑨𝒍𝒍𝒆𝒏'𝒔")
    move_cursor(4, 35)
    print("𝑷𝒉𝒊𝒍𝒐𝒔𝒐𝒑𝒉𝒊𝒄𝒂𝒍 𝑰𝒏𝒔𝒊𝒈𝒉𝒕")
    
    print("\n\n")
    
    # Draw Woody Allen caricature
    set_color(0, 0, 0)
    draw_pixel_art()
    
    print("\n")
    
    # Animate thinking process
    set_color(255, 140, 0)
    animate_thoughts()
    
    print("\n\n")
    draw_notes()
    print("\n")
    
    # The quote
    quote = """Life is essentially a cosmic joke with a punchline
I'm not sure anyone really understands,
but I'm pretty sure the joke is on me,
and the punchline involves death,
which statistically, happens to everyone eventually,
except maybe Keanu Reeves, who I suspect
is actually immortal and just humoring us all."""""""
    
    draw_box(quote)
    
    print("\n\n\n")
    
    # Attribution
    set_color(139, 0, 0)
    type_text("~ Woody Allen (probably)", 0.1)
    
    print("\n\n")
    set_color(218, 165, 32)
    print("   ✨ Existential wisdom delivered with neurotic charm ✨")
    
    reset_color()
    print("\033[0m")

if __name__ == "__main__":
    try:
        main()
    except:
        # Fallback if terminal doesn't support ANSI codes
        print("\n")
        print("╔" + "═" * 60 + "╗")
        print("║" + " " * 60 + "║")
        print("║" + "  Life is essentially a cosmic joke with a".center(60) + "║")
        print("║" + "  punchline I'm not sure anyone really".center(60) + "║") 
        print("║" + "  understands, but I'm pretty sure the".center(60) + "║")
        print("║" + "  joke is on me, and the punchline involves".center(60) + "║")
        print("║" + "  death, which statistically, happens to".center(60) + "║")
        print("║" + "  everyone eventually, except maybe Keanu".center(60) + "║")
        print("║" + "  Reeves, who I suspect is actually immortal".center(60) + "║")
        print("║" + "  and just humoring us all.".center(60) + "║")
        print("║" + " " * 60 + "║")
        print("╚" + "═" * 60 + "╝")
        print("\n                 ~ Woody Allen (probably)")