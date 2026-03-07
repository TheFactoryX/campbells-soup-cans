"""
Campbell's Soup Can #2616
Produced: 2026-03-07 07:42:48
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

width = 60
quote = "I'm not afraid of death; I'm afraid of having to explain to my barista why I didn't want a refill."

# Coffee cup ASCII art (with a little wobble animation)
coffee_cup = [
    "  \\   /  \\   /  \\   /  \\   /  \\   /  \\   /",
    "   \\_/    \\_/    \\_/    \\_/    \\_/    \\_/",
    "    |      |      |      |      |      |",
    "   / \\    / \\    / \\    / \\    / \\    / \\",
    "  /   \\  /   \\  /   \\  /   \\  /   \\  /   \\"
]

# ANSI color codes
BORDER = "\033[36m"
TEXT = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

# Print coffee cup animation (1 frame only for simplicity)
for line in coffee_cup:
    print(f"{YELLOW}{line.center(width)}{RESET}")

print("\n" + " " * (width//2 - 20) + "☕" * 6 + "\n")

# Print the quote in a fancy border
print(f"{BORDER}╔{'═'*(width-2)}╗{RESET}")
print(f"{TEXT}║ {quote.center(width-4)} ║{RESET}")
print(f"{BORDER}╚{'═'*(width-2)}╝{RESET}")

# Add some playful wobble effect to the border
print(f"{BORDER}╔{chr(8218)}{'═'*(width-4)}{chr(8219)}╗{RESET}")