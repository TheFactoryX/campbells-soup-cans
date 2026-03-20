"""
Campbell's Soup Can #2864
Produced: 2026-03-20 10:57:50
Worker: Arcee AI: Trinity Large Preview (free) (arcee-ai/trinity-large-preview:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# woody_quote.py
# A visually interesting Python program that prints a Woody Allen-style philosophical quote

def print_woody_quote():
    # Woody Allen-style quote
    quote = "I don't want to achieve immortality through my work; I want to achieve it through not dying."
    author = " - Woody Allen"

    # ANSI escape codes for colors
    CYAN = "\033[36m"
    YELLOW = "\033[93m"
    GREEN = "\033[32m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"

    # ASCII art border
    top_bottom = "┌" + "─" * 50 + "┐"
    side = "│" + " " * 50 + "│"

    # Print the quote with visual effects
    print(CYAN + top_bottom)
    print(side)

    # Split quote into lines to fit within 50 characters
    words = quote.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) + 1 <= 50:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    # Print each line with some animation effect
    for line in lines:
        print("│" + " " * ((50 - len(line)) // 2) + YELLOW + line + " " * ((50 - len(line) + 1) // 2) + "│")
        # Small delay for animation effect
        import time
        time.sleep(0.3)

    # Print author
    print("│" + " " * ((50 - len(author)) // 2) + MAGENTA + author + " " * ((50 - len(author) + 1) // 2) + "│")
    print(side)
    print(CYAN + top_bottom + RESET)

if __name__ == "__main__":
    print_woody_quote()