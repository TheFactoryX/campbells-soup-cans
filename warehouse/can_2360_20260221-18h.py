"""
Campbell's Soup Can #2360
Produced: 2026-02-21 18:54:09
Worker: Qwen: Qwen3 VL 30B A3B Thinking (qwen/qwen3-vl-30b-a3b-thinking)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'

quote = "I'm not afraid of death; I'm just afraid of being a failure before I die. But then again, I'm afraid of being a failure after death. So I'm stuck in a kind of existential panic that's more like a mild inconvenience."

max_width = 40

# Split the quote into lines that fit in max_width-2 characters
words = quote.split()
lines = []
current_line = ""
for word in words:
    if current_line == "":
        current_line = word
    else:
        # Check if adding next word would exceed max_width-2
        if len(current_line) + 1 + len(word) <= max_width - 2:
            current_line += " " + word
        else:
            lines.append(current_line)
            current_line = word
if current_line:
    lines.append(current_line)

# Build colorful borders
top = RED + '+' + ('-' * (max_width - 2)) + '+' + RESET
bottom = BLUE + '+' + ('-' * (max_width - 2)) + '+' + RESET

# Print the framed quote
print(top)
for line in lines:
    centered = line.center(max_width - 2)
    print(f"{GREEN}|{YELLOW}{centered}{RESET}{GREEN}|{RESET}")
print(bottom)

# Add some whimsical animation
for i in range(3):
    print(f"{YELLOW}  (•_•) {RESET}{GREEN}  (•_•) {RESET}{BLUE}  (•_•) {RESET}", end='\r')
    import time
    time.sleep(0.3)
    print(f"{YELLOW}  (•_•) {RESET}{GREEN}  (•_•) {RESET}{BLUE}  (•_•) {RESET}  ", end='\r')
    time.sleep(0.3)
print("\n" + YELLOW + "Woody Allen would approve." + RESET)