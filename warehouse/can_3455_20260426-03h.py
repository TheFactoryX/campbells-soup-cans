"""
Campbell's Soup Can #3455
Produced: 2026-04-26 03:55:57
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys
import time
import random

def typewriter(text, delay=0.02, color_code="\033[93m"):
    sys.stdout.write(color_code)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    sys.stdout.write("\033[0m")

def sparkle():
    sparkles = ["✨", "🌟", "💫", "⭐", "✦", "❂"]
    return random.choice(sparkles)

def nervous_pulse():
    colors = ["\033[91m", "\033[93m", "\033[95m", "\033[96m"]
    return random.choice(colors)

def main():
    # Clear screen
    sys.stdout.write("\033[2J\033[H")
    
    # ASCII brain
    brain = [
        "       .--.",
        "      |o_o |",
        "      |:_/ |",
        "     //   \\ \\",
        "    (|     | )",
        "   /'\\_   _/`\\",
        "   \\___)=(___/",
        "   🤯⚡🧠💭"
    ]
    
    # Title box
    width = 58
    title = " WOODY'S EXISTENTIAL CRISIS (TM) "
    padding = (width - len(title)) // 2
    
    print("\033[95m" + "╔" + "═" * (width - 2) + "╗")
    print("║" + " " * padding + "\033[96m" + title + "\033[95m" + " " * (width - padding - len(title)) + "║")
    print("╠" + "─" * (width - 2) + "╣")
    
    # Nervous brain animation
    for line in brain:
        color = nervous_pulse()
        spaces = " " * ((width - len(line) - 4) // 2)
        print(f"║{spaces}{color}{line}\033[95m{spaces}║")
        sys.stdout.flush()
        time.sleep(0.08)
    
    print("╠" + "─" * (width - 2) + "╣")
    
    # The quote
    quote = "I've been having such vivid nightmares about my own death that I woke up crying — only to realize I was still alive, which frankly was even more depressing."
    
    wrapped = []
    words = quote.split()
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= width - 6:
            line += word + " "
        else:
            wrapped.append(line)
            line = word + " "
    if line:
        wrapped.append(line)
    
    for i, qline in enumerate(wrapped):
        spaces = (width - len(qline) - 4)
        left = spaces // 2
        right = spaces - left
        sparkle_color = ["\033[93m", "\033[91m", "\033[96m"][i % 3]
        print(f"║  {sparkle_color}“\033[0m{qline}{sparkle_color}”\033[95m{' ' * (right - 2)}║")
    
    print("╚" + "═" * (width - 2) + "╝")
    
    # Footer with animated signatures
    signatures = [
        "   — Woody (probably)",
        "   — Allen (maybe?)",
        "   — A Neurotic Mind",
        "   — Someone Who Overthinks Toast"
    ]
    
    print()
    for sig in signatures:
        color = random.choice(["\033[90m", "\033[37m", "\033[92m"])
        sys.stdout.write(color + sig + "\033[0m")
        time.sleep(0.3)
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.2)
        print()
    
    # Confetti burst
    print()
    confetti = ["🎭", "🎪", "🎪", "🎪", "🎭", "🍿", "🎬", "🎥", "🎞️", "🎟️"]
    for i in range(20):
        color = random.choice(["\033[91m", "\033[93m", "\033[92m", "\033[95m", "\033[96m"])
        sys.stdout.write(color + random.choice(confetti) + " \033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print()
    print("\n\033[90m\"Existence is 99% panic and 1% wondering why you're panicking.\"\033[0m\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[93mAh, escape! The only truly successful human endeavor...\033[0m\n")