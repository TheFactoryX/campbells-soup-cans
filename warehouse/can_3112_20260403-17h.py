"""
Campbell's Soup Can #3112
Produced: 2026-04-03 17:52:16
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

# Woody Allen style quote
quote = [
    "I don't want to achieve immortality through my work;",
    "I want to achieve it through not dying.",
    "- Woody Allen"
]

# ANSI escape codes for colors and formatting
colors = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "cyan": "\033[36m",
    "yellow": "\033[93m",
    "red": "\033[91m",
    "green": "\033[92m"
}

def print_colored(text, color):
    """Print text in specified color"""
    print(f"{color}{text}{colors['reset']}")

def typewriter(text, color=colors['cyan'], delay=0.05):
    """Print text with typewriter effect"""
    for char in text:
        print_colored(char, color, end='', flush=True)
        time.sleep(delay)

def print_boxed(text_lines, border_color=colors['yellow']):
    """Print text inside a decorative box"""
    max_len = max(len(line) for line in text_lines)
    border = "═" * (max_len + 4)
    
    print_colored(f"╔{border}╗", border_color)
    for line in text_lines:
        padding = " " * (max_len - len(line))
        print_colored(f"║ {line}{padding} ║", border_color)
    print_colored(f"╚{border}╝", border_color)

def animate_fade_in(text, color=colors['cyan']):
    """Animate text fading in"""
    for i in range(1, 30):
        opacity = i / 30
        dimmed_text = "".join([char if char == " " else char for char in text])
        print_colored(dimmed_text, color)
        time.sleep(0.02)
        print("\033[F" * len(text.split("\n")), end="")

def main():
    print("\n" * 2)
    
    # Title animation
    title = "WOODY ALLEN PHILOSOPHY"
    print_colored("\n" + " " * 10 + title, colors['red'])
    time.sleep(0.8)
    
    # Divider
    print_colored("\n" + "─" * 50, colors['yellow'])
    
    # Animate quote appearance
    print("\n" * 2)
    for line in quote:
        typewriter(line, colors['cyan'])
        print()
        time.sleep(0.3)
    
    print("\n")
    
    # Boxed attribution
    print_boxed([quote[-1]], colors['green'])
    
    print("\n")
    
    # Existential crisis animation
    crisis_phrases = [
        "Existence is pain...",
        "Why are we here?",
        "Is this all there is?",
        "I should've stayed in bed..."
    ]
    
    print_colored("Thoughts racing through Woody's mind:", colors['yellow'])
    for phrase in crisis_phrases:
        print_colored("•", colors['red'], end=" ")
        typewriter(phrase, colors['red'], 0.02)
        print("\n")
        time.sleep(0.5)

if __name__ == "__main__":
    main()