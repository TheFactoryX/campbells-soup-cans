"""
Campbell's Soup Can #3549
Produced: 2026-05-03 13:49:44
Worker: inclusionAI: Ling-2.6-1T (free) (inclusionai/ling-2.6-1t:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import sys
import random

def typewriter(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay + random.uniform(-0.005, 0.01))
    sys.stdout.write('\n')

def color(text, code):
    return f"\033[{code}m{text}\033[0m"

def box(text, width=60):
    lines = text.split('\n')
    padded = [f"  {line.center(width - 4)}  " for line in lines]
    top = '╭' + '─' * (width - 2) + '╮'
    bottom = '╰' + '─' * (width - 2) + '╯'
    return '\n'.join([top] + [f"│{line}│" for line in padded] + [bottom])

def sparkle(text):
    sparkles = ['✨', '⭐', '💫', '🌟', '🔮', '🪐']
    result = ""
    for char in text:
        result += char
        if random.random() > 0.85:
            result += color(random.choice(sparkles), "93")
    return result

def main():
    quote = (
        "I've been having the most terrible anxiety about the nature of existence.\n"
        "You see, I realized that if nothing matters, then my anxiety doesn't\n"
        "matter either — which only makes me more anxious because now I'm anxious\n"
        "about not being anxious enough. It's very zen, really. Or maybe it's just\n"
        "gas. I tend to confuse enlightenment with lactose intolerance."
    )
    
    colors = ["95", "96", "93", "91", "92"]
    frames = 0
    
    sys.stdout.write("\033[2J\033[H")
    
    for i in range(15):
        sys.stdout.write("\033[2J\033[H")
        c = colors[frames % len(colors)]
        stars = '·' * (15 - abs(i - 7) * 2)
        sys.stdout.write(color(stars.center(60), "90") + "\n\n")
        
        if i == 14:
            b = box(color(sparkle(quote), c), 62)
            typewriter(b, 0.01)
        elif i > 7:
            partial = quote.split('\n')[:i-7]
            if partial:
                b = box(color('\n'.join(partial), c), 62)
                print(b)
        
        frames += 1
        time.sleep(0.15)
        sys.stdout.write("\033[2J\033[H")
    
    # Final sparkle burst
    sys.stdout.write("\033[2J\033[H")
    for _ in range(20):
        c = colors[random.randint(0, len(colors)-1)]
        star = random.choice(['✦', '❂', '✧', '❈', '✴', '🌀'])
        x = random.randint(5, 55)
        y = random.randint(2, 20)
        sys.stdout.write(f"\033[{y};{x}H{color(star, c)}")
        sys.stdout.flush()
        time.sleep(0.05)
    
    time.sleep(0.5)
    sys.stdout.write("\033[23;15H" + color("— Woody Allen (probably)", "90"))
    sys.stdout.write("\033[25;25H" + color("☕", "93"))
    sys.stdout.write("\n\n")
    sys.stdout.write(color("  (tap any key to fade into existential dread...)\n", "90"))
    
    # Keep it alive
    sys.stdout.flush()
    time.sleep(0.5)
    
    # Gentle fade
    for i in range(10, 0, -1):
        sys.stdout.write(f"\033[{i}J")
        time.sleep(0.08)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\033[0m\n")