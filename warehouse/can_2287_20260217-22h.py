"""
Campbell's Soup Can #2287
Produced: 2026-02-17 22:51:10
Worker: StepFun: Step 3.5 Flash (free) (stepfun/step-3.5-flash:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random
import sys

def neurotic_typewriter(text, delay=0.05, color='\033[93m'):
    """Print text with Woody Allen's signature anxious pacing"""
    for char in text:
        sys.stdout.write(color + char + '\033[0m')
        sys.stdout.flush()
        time.sleep(delay * random.uniform(0.5, 1.5))
    print()

def existential_box():
    """Create a visually neurotic presentation"""
    # Woody's existential dread palette
    NEUROTIC_YELLOW = '\033[93m'
    ANXIETY_BLUE = '\033[94m'
    DARK_THOUGHT = '\033[90m'
    RESET = '\033[0m'
    
    # The quote - freshly minted existential neurosis
    quote = (
        "I don't want to achieve immortality through my work; "
        "I want to achieve it through not dying. "
        "But then I thought: what if immortality is exhausting? "
        "Imagine having to attend your own birthday parties for eternity. "
        "I'd rather have a nice nap and be done with the whole thing."
    )
    
    # Woody's signature trembling border
    border = NEUROTIC_YELLOW + "┌" + "─" * 68 + "┐" + RESET
    middle = NEUROTIC_YELLOW + "│" + RESET
    bottom = NEUROTIC_YELLOW + "└" + "─" * 68 + "┘" + RESET
    
    # Opening with philosophical preamble
    print(DARK_THOUGHT + "「 Deep Thought Module Loading... 」" + RESET)
    time.sleep(0.8)
    print(ANXIETY_BLUE + "「 Processing mortality algorithms... 」" + RESET)
    time.sleep(1.2)
    print(NEUROTIC_YELLOW + "「 Found something disturbing! 」" + RESET)
    time.sleep(0.5)
    print()
    
    # The dramatic box
    print(border)
    
    # Type the quote with neurotic pacing
    sys.stdout.write(middle + " ")
    neurotic_typewriter(quote, delay=0.03)
    
    # The devastating realization at the end
    print(middle + " " + DARK_THOUGHT + "∴ Conclusion: Existence is overrated." + RESET + " " + middle)
    print(bottom)
    
    # Woody's signature self-deprecating footnote
    time.sleep(1.5)
    print()
    print(ANXIETY_BLUE + "      - Woody Allen (probably while waiting for the dentist)" + RESET)
    print(DARK_THOUGHT + "      [This quote brought to you by insomnia and a questionable past]" + RESET)

if __name__ == "__main__":
    try:
        existential_box()
    except KeyboardInterrupt:
        print("\n\033[90mSee? Even the universe interrupts my suffering.\033[0m")
        sys.exit(0)