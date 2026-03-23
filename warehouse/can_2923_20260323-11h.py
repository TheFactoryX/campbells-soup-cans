"""
Campbell's Soup Can #2923
Produced: 2026-03-23 11:10:44
Worker: MoonshotAI: Kimi K2 0905 (moonshotai/kimi-k2-0905)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def typewriter(text, delay=0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def neurotic_cursor():
    for _ in range(3):
        sys.stdout.write('\033[?25l')
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write('\033[?25h')
        sys.stdout.flush()
        time.sleep(0.3)

def glitch_line(text):
    glitch_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    for i, char in enumerate(text):
        if random.random() < 0.1:
            print(random.choice(glitch_chars), end='', flush=True)
            time.sleep(0.05)
            sys.stdout.write('\b')
        print(char, end='', flush=True)
        time.sleep(0.02)
    print()

print("\033[2J\033[H")  # Clear screen
print("\033[38;5;214m")  # Woody orange tint

print("┌" + "─"*58 + "┐")
print("│" + " "*58 + "│")
print("│" + " "*15 + "\033[1mWOODY'S MIDNIGHT ANGST™" + "\033[0m\033[38;5;214m" + " "*16 + "│")
print("│" + " "*58 + "│")
print("└" + "─"*58 + "┘")
print()

neurotic_cursor()

print("\033[38;5;196m")  # Anxiety red
typewriter("I don't fear death—", 0.1)
print("\033[38;5;226m")  # Existential yellow
typewriter("I just don't want to be invited to the pre-party,", 0.08)
print("\033[38;5;82m")  # Jealous green
glitch_line("the after-party, or the party in between where they serve existential dread on crackers.")

print("\033[38;5;214m")  # Back to woody orange
print("\n" + " "*20 + "✧･ﾟ: *✧･ﾟ:*  ･ﾟ✧*:･ﾟ✧")
print("\033[3m" + " "*12 + "(And the crackers are stale.)" + "\033[0m\033[38;5;214m")

print("\n\033[38;5;147m")  # Melancholy purple
for i in range(3):
    print("◝(ᵕ_ᵕ)◞" + " "*i*3 + "◝(ﾟ_ﾟ)◞" + " "*(6-i*3) + "◝(｡_｡)◞")
    time.sleep(0.5)

print("\033[0m")  # Reset