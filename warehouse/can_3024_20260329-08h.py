"""
Campbell's Soup Can #3024
Produced: 2026-03-29 08:59:10
Worker: LiquidAI: LFM2.5-1.2B-Instruct (free) (liquid/lfm-2.5-1.2b-instruct:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ❌ (broken)

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import sys

def draw_kawaii_text(quote, color='#00FFFF', size=80, border=None):
    """
    Draws a kawaii-style animated quote using ANSI colors and borders.
    """
    # Create a colorful background
    background = "#EFEFEF" + '# ' * (10*size + 4)
    text = quote.
                   .format(color=color)
                   .rjust(size)
                   .center(size)
    
    # Draw box around the text
    text_color = color + " "\n" * (size - 2)
    for i in range(size):
        text = text + ' ' * (size-i*2) + text_color
        background += "|---" + text + "|---" + text_color + "|"
    
    # Apply animation
    if border:
        # Simple bouncing effect by swapping background colors
        border_box = "#FFFFEEE" + "#A5EACC" * len(text)  # border color
        overlap = text_box_center = ' ' * size
        if background != text:
            for i in range(int(size)):
                background += background[background.index(text) - 1] + f"  {text}"
                background += text + background.center(opacity=10)
    
    # Display result
    print(f"\n🎬 [ANIMATED] {text}\n")
    sys.stdout.write(f"COLOR: {text_color}\n" + "="*30 + "\n")
    sys.stdout.flush()

# Choose a quote from Woody Allen's style
quotes = [
    "You must be the change you wish to see in the world.",
    "In today's world, we need more people who don't know what to do with themselves.",
    "Life is like a pie, and you never see what's under the crust.",
    "The only thing we have to fear is fear itself.",
    "Why don't scientists trust atoms? Because they make up everything."
]

# Picker 'the one' with some flair
picked = quotes[int(len(quotes)*0.3)]
print(picked)
draw_kawaii_text(picked, color='#0000CC', size=120)