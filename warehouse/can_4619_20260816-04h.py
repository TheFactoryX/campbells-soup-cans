"""
Campbell's Soup Can #4619
Produced: 2026-08-16 04:00:37
Worker: Poolside: Laguna S 2.1 (free) (poolside/laguna-s-2.1:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

#!/usr/bin/env python3
"""
A neurotic existential crisis... served with a side of visual flair.
"""

import sys
import time
import os
import random

# ===== ANSI Color Magic =====
class C:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    GREY = "\033[90m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_type(text, delay=0.03, end='\n'):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write(end)
    sys.stdout.flush()

def glitch_text(text, iterations=3):
    """A nervous little glitch effect"""
    for _ in range(iterations):
        glitched = ""
        for char in text:
            if random.random() < 0.3:
                glitched += chr(random.randint(33, 126))
            else:
                glitched += char
        print(f"\r{glitched}" + " " * 10, end='\r')
        time.sleep(0.08)
    print(text)

def rainbow_print(text, delay=0.02):
    """Print text with a cycling rainbow effect"""
    colors = [C.RED, C.YELLOW, C.GREEN, C.CYAN, C.BLUE, C.MAGENTA]
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print(C.RESET)

def print_with_box(text_lines, padding=2, border_color=C.CYAN, inner_color=C.YELLOW):
    """Print text inside a decorative box"""
    max_width = max(len(line) for line in text_lines)
    box_width = max_width + (padding * 2)
    
    # Top border
    print(border_color + "┌" + "─" * box_width + "┐")
    
    # Empty line at top
    print("│" + " " * box_width + "│")
    
    # Content lines
    for line in text_lines:
        spaces = " " * (max_width - len(line))
        content = " " * padding + line + spaces + " " * padding
        print("│" + inner_color + content + C.RESET + border_color + "│")
    
    # Empty line at bottom
    print("│" + " " * box_width + "│")
    
    # Bottom border
    print("└" + "─" * box_width + "┘" + C.RESET)

def draw_thinking_bubble():
    """Draw a cartoon thinking bubble"""
    bubble = [
        "  ┌─────────────────────────┐",
        "  │  Well... I guess I      │",
        "  │  should probably        │",
        "  │  contemplate this       │",
        "  │  whole mortality        │",
        "  │  situation, but first   │",
        "  │  let me check my        │",
        "  │  therapist's            │",
        "  │  availability...        │",
        "  └─────────────────────────┘",
        "        ░░░░░       ",
        "      ░░░░░░░░░     ",
        "    ░░░░░░░░░░░░░   ",
        "  ░░░░░░░░░░░░░░░░░ ",
        "░░░░░░░░░░░░░░░░░░░░",
    ]
    for line in bubble:
        print(C.MAGENTA + line + C.RESET)
        time.sleep(0.05)

def draw_neurotic_man():
    """ASCII art of a worried philosopher"""
    figure = [
        f"    {C.YELLOW}┌──────┐",
        f"   {C.YELLOW}│  😰  │  {C.GREY}(existential dread)",
        f"    {C.YELLOW}└─┬─┬──┘",
        f"   {C.CYAN}   │ │  {C.RESET}    ╱",
        f"   {C.CYAN}  ╱     {C.RESET}  ╱",
        f"  {C.CYAN}  │  {C.MAGENTA}_{C.RESET}{C.CYAN}\\  {C.RESET}│",
        f" {C.CYAN}   │  {C.MAGENTA}_{C.RESET}{C.CYAN} |{C.RESET} │",
        f" {C.CYAN}  ╱ \\{C.RESET}    │  {C.GREEN}☕{C.RESET}",
        f"{C.CYAN}  ╱   \\{C.RESET}  ╱ \\"
    ]
    for line in figure:
        print(line)
        time.sleep(0.1)

def main():
    clear_screen()
    
    # Opening animation
    print("\n" + C.GREY + " " * 20 + "A Production of")
    time.sleep(0.5)
    rainbow_print(" " * 18 + "NEUROTIC PHILOSOPHY™")
    time.sleep(0.5)
    
    # Draw the character
    print()
    draw_neurotic_man()
    time.sleep(0.5)
    
    # Draw thinking process
    print()
    draw_thinking_bubble()
    time.sleep(0.5)
    
    # Random "thinking" pauses
    thinking_msgs = [
        f"{C.GREY}Hmm... let me think about this...{C.RESET}",
        f"{C.DIM}Actually, first, a word from our sponsor: Anxiety.{C.RESET}",
        f"{C.GREY}Wait, what was the question again?{C.RESET}",
    ]
    print()
    slow_type(random.choice(thinking_msgs) + "\n", 0.05)
    time.sleep(0.3)
    
    # The main quote - delivered with flair
    quote_lines = [
        "I was walking down the street the other day",
        "and I thought, 'That's it, I'm done.'",
        "Not done with what, exactly?",
        "Well, done with the whole",
        "existence thing. It seemed so simple!",
        "",
        "But then I realized - if I'm done with",
        "existence, who's going to worry about",
        "whether they're worrying about me?",
        "",
        "So I decided to continue existing,",
        "but only on a probationary basis.",
        "Death and I have an understanding:",
        "It'll wait until I've finished my coffee,",
        "and preferably until after dessert.",
        "",
        "Because honestly, eternity sounds",
        "like a very long time to be bored,",
        "and I'm already bored at parties",
        "that last two hours.",
        "",
        "I once asked a monk about",
        "achieving enlightenment. He said,",
        "'You must let go of attachment.'",
        "I said, 'I can't let go, I'm too ",
        "neurotic!' And he said, 'Perfect,'",
        "and charged me double."
    ]
    
    # Display the quote
    print()
    print(C.GREEN + "════════════════════════════════════════════")
    print("  THE QUOTE (FINALLY)                        ")
    print("════════════════════════════════════════════" + C.RESET)
    time.sleep(0.5)
    
    for line in quote_lines:
        if line == "":
            print()
            time.sleep(0.3)
        else:
            # Sometimes glitch, sometimes rainbow, sometimes normal
            choice = random.randint(1, 10)
            if choice == 1:
                glitch_text(C.YELLOW + line + C.RESET)
            elif choice == 2:
                rainbow_print(line, 0.01)
            else:
                slow_type(C.YELLOW + line + C.RESET, 0.02)
            time.sleep(0.1)
    
    # Final punchline in a box
    print()
    punchline = [
        "    Summary:",
        "    I'm not afraid of death.",
        "    I'm afraid of missing my",
        "    dentist appointment",
        "    with whatever comes after.",
    ]
    print_with_box(punchline, border_color=C.RED + C.BOLD, inner_color=C.YELLOW)
    
    time.sleep(1)
    
    # Signature
    print()
    slow_type(C.GREY + "— Someone who definitely should be", 0.04)
    slow_type(C.GREY + "   in therapy right now" + C.RESET + "\n", 0.04)
    
    # Final flourish
    print()
    for _ in range(5):
        print(C.DIM + "  ." * 30 + C.RESET)
        time.sleep(0.2)
    
    print(C.GREEN + f"\n  ({len(quote_lines) + len(punchline)} words of wisdom)" + C.RESET)

if __name__ == "__main__":
    main()