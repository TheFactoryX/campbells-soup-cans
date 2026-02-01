"""
Campbell's Soup Can #1983
Produced: 2026-02-01 11:38:48
Worker: NVIDIA: Nemotron Nano 9B V2 (free) (nvidia/nemotron-nano-9b-v2:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

bold = "\033[1m"
green = "\033[92m"
reset = "\033[0m"
yellow = "\033[93m"
red = "\033[91m"

ascii_box = f"""
{green}▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  {reset}
{green}▓▓▓▓▓▓▓  ▓▓▓▓▓▓  ▓▓▓▓▓▓  {reset}
{green}▓ 😵‍💫 'Exist...' ▓▓▓▓▓  {reset}
{green}▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓  ▓▓▓▓▓▓  {reset}
{green}▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄  {reset}
"""

quote = f"{yellow}Why did I learn to write Python?\n{red}Same reason Descartes doubted his existence:\n{green}Maybe the universe is just a glitch in my shampoo bottle.{reset}"

final_quote = f"""
{green}▄▄▄▄▄▄▄▄  ▄▄▄▄  ▄▄▄▄▄▄  {reset}
{green}▓ {bold}{yellow}[WOODY'S MIND] {reset}{green} ▓{reset}
{green}▓ {bold}{green}{quote}{reset} ▓{reset}
{green}▓ {bold}{yellow}[END OF EXISTENCE] {reset}{green} ▓{reset}
{green}▄▄▄▄▄▄▄▄  ▄▄▄▄  ▄▄▄▄▄▄  {reset}
"""

print(ascii_box)
print("\n" + final_quote + "\n")

# Playful ASCII Woody
print(red + "\n   (    🧠  )   \n     'I THOUGHT I SEEN A MOUSE'\n")