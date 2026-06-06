"""
Campbell's Soup Can #3870
Produced: 2026-06-06 08:02:26
Worker: NVIDIA: Nemotron Nano 12B 2 VL (free) (nvidia/nemotron-nano-12b-v2-vl:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time
import random

def woody_quote():
    # Target for animation (underscore position)
    target = "_"
    # Define the possible characters to animate
    chars = ['-', '=', "*", "+", ">", "<", "~", "!", "@"]
    color_codes = [
        "\033[91m", "\033[93m", "\033[95m", "\033[92m", "\033[96m",
        "\033[97m", "\033[90m", "\033[94m"
    ]
    
    # The Werner Herzog Deep Dive
    quote = [
        "Life is a box of chocolates.",
        "You never know what you're gonna get.",
        "But at least the chocolate melts.",
        "And sometimes it's dark.",
        "Sometimes it's bitter.",
        "Sometimes it's full of nuts.",
        "And usually there's that weird crunchy thing that you can't quite get out.",
        "Anyway. Don't worry.",
        "We're all just cowboys in a spaghetti western.",
        "Except instead of guns, we have credit card debt.",
        "And instead of horses, we have cats.",
        "To-may-to, to-mah-to..",
        "We're all just rats in a maze.",
        "Or maybe ants.",
        "No one knows.",
        "But you gotta keep running.",
        "Unless you stop.",
        "Which might be a good idea.",
        "But then you'll never find your way back.",
        "So just keep running.",
        "But maybe towards the left.",
        "Or maybe not."
    ]
    
    # Find the underscore
    u_ert = quote.find('_')
    if u_ert == -1:
        exit()  # shouldn't happen
    
    # Pre-process the quote to split into parts
    pre = quote[:u_ert]
    post = quote[u_ert+1:]
    
    # Chosen font size (changes visual impact!)
    font_size = random.choice([90, 95, 97, 100, 105])
    
    # NEW ANIMATION SLICER CODE TOOLS!
    # For the part before the cursor
    def animate_left(text, color_code, char, target, chars):
        while 1:
            # Bonus: Throw in a real random bar for texture
            line = "".join([
                random.choice(chars) if random.random() < 0.3 else c
                for c in text
            ])
            print(f"{color_code}{line[:target]}^{char}\033[39m{line[target:]}", end="\r")
            time.sleep(0.03)
    
    # Then animate the character itself
    def animate_char(target_pos, color_code, char, chars):
        while 1:
            line = "".join([
                f"{color_code}{random.choice(chars)}\033[39m" 
                if i == target_pos 
                else c
                for i, c in enumerate(line_builder)
            ]) if line_builder else ""
            print(f"\r{line}", end="")
            time.sleep(0.03)
    
    # For the part after the cursor - simpler
    def animate_right(text, post, pos, color_code, char, chars):
        full = text + char + post
        while 1:
            line = "".join([
                f"{color_code}{c}\033[39m" if i == pos 
                else c
                for i, c in enumerate(full)
            ])
            print(f"\r{line}", end="")
            time.sleep(0.03)
    
    # Start animation pipeline
    try:
        # Left part animation
        c_idx = 0
        c = chars[c_idx] if c_idx < len(chars) else random.choice(chars)
        color_code = random.choice(color_codes)
        thread1 = threading.Thread(
            target=animate_left, 
            args=(pre, color_code, c, u_ert, chars)
        )
        thread1.daemon = True
        thread1.start()
    
        # Main character animation
        c_idx = 0
        while 1:
            c = chars[c_idx % len(chars)]
            color_code = random.choice(color_codes)
            # Combine line before + char + line after
            full_line = pre + c + post
            animate_char(u_ert, color_code, c, chars)
            
            # Advance character index
            c_idx += 1
            
    except KeyboardInterrupt:
        print("\n\n" + " "*80, end="\r")  # Invisible clear
    
    print("\n\n" + "-" * 80)
    print("\033[92mYour quote was accidentally animated!\nMaybe try Python's 'theater'\nmode next time?\033[39m")

if __name__ == "__main__":
    woody_quote()