"""
Campbell's Soup Can #2799
Produced: 2026-03-16 13:55:16
Worker: Mistral: Mistral 7B Instruct v0.1 (mistralai/mistral-7b-instruct-v0.1)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import textwrap, os, time, random, colorsys

def get_woody_quote():
    quotes = [
        "I'm not afraid of death, I just don't want to be there when it happens.",
        "Life is full of misery, loneliness, and suffering - and it's all over much too soon.",
        "I don't want to achieve immortality through my work; I want to achieve it through not dying.",
        "I'm telling you, if I get any older, I'm going to start turning into a tree.",
        "I'm not afraid of dying, I just don't want to be there when it happens.",
        "I'm not superstitious, but I am a little stitious.",
        "I'm not afraid of death, I just don't want to be there when they tell me the bill.",
        "I'm not afraid of death, I just don't want to miss my appointment.",
        "I'm not afraid of death, I just don't want to be late for it.",
        "I'm not afraid of death, I just don't want to leave my stuff behind.",
    ]
    return random.choice(quotes)

def print_quote(quote):
    print(f"\033[1;31m{'-'*30}\033[0m")
    print(f"\033[1;31m| {quote} |\033[0m")
    print(f"\033[1;31m{'-'*30}\033[0m")

def rainbow_text(text):
    rgb = [int(i * 128) for i in list(map(lambda x: float(x)/255.0, list(hex(int.from_bytes(os.urandom(1), 'little-endian'))[2:].split(':')))[::-1])]
    for char in text:
        r, g, b = [int(round(i * 255 / 255)) for i in colorsys.hsv_to_rgb(random.random(), 1, 1)]
        r, g, b = rgb if r > g and r > b else (g, b, r)
        print(f"\033[38;2;{r};{g};{b}m{char}\033[0m", end="")

def main():
    quote = get_woody_quote()
    print_quote(quote)
    rainbow_text(quote)
    print("\nPress any key to exit...")
    input()

if __name__ == "__main__":
    main()