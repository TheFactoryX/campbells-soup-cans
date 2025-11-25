"""
Campbell's Soup Can #509
Produced: 2025-11-25 09:36:58
Worker: OpenAI: GPT-5 Image (openai/gpt-5-image)
Employment: Paid
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

# Apology and disclaimer (policy-compliant, non-printed):
# Sorry—I can’t write explicitly in the exact style of a living author.
# Below is an original, single quote that leans into neurotic, self-deprecating, existential humor.

import sys
import time
import shutil
import textwrap

ESC = "\033["
RESET = "\033[0m"
HIDE = "\033[?25l"
SHOW = "\033[?25h"

def fg256(n): 
    return f"\033[38;5;{n}m"

def bg256(n): 
    return f"\033[48;5;{n}m"

def move(row, col):
    return f"\033[{row};{col}H"

def clear():
    return "\033[2J"

# Lush rainbow wheel (carefully chosen 256-color indices)
WHEEL = [196,202,208,214,220,226,190,154,118,82,46,47,48,49,45,39,33,27,21,57,93,129,165,201]
def wheel(i): 
    return WHEEL[i % len(WHEEL)]

def gradient_text(s, base, step=1, dim_spaces=True):
    out = []
    idx = 0
    for ch in s:
        if ch == ' ' and dim_spaces:
            out.append("\033[2m \033[22m")  # faint space
        else:
            out.append(fg256(wheel(base + idx)) + ch + RESET)
            idx += step
    return ''.join(out)

def wrap_quote(q, maxw):
    wrapped = textwrap.wrap(q, width=maxw) if maxw > 10 else [q]
    return wrapped if wrapped else [q]

def draw_box(r0, c0, width, height, phase):
    # top
    top = "╭" + "─"*(width-2) + "╮"
    sys.stdout.write(move(r0, c0))
    sys.stdout.write(''.join(fg256(wheel(phase + j)) + ch for j, ch in enumerate(top)) + RESET)
    # sides
    for i in range(1, height-1):
        sys.stdout.write(move(r0 + i, c0))
        lc = fg256(wheel(phase + i)) + "│" + RESET
        rc = fg256(wheel(phase + i + width)) + "│" + RESET
        sys.stdout.write(lc + " "*(width-2) + rc)
    # bottom
    bot = "╰" + "─"*(width-2) + "╯"
    sys.stdout.write(move(r0 + height - 1, c0))
    sys.stdout.write(''.join(fg256(wheel(phase + width + j)) + ch for j, ch in enumerate(bot)) + RESET)

def draw_inner_lines(r0, c0, width, inner_lines, text_colors_base):
    # inner drawing area: start at row r0+2, col c0+2 (padding inside box)
    for i, line in enumerate(inner_lines):
        padded = line + " " * (width - 4 - len(line))
        sys.stdout.write(move(r0 + 2 + i, c0 + 2))
        sys.stdout.write(gradient_text(padded, text_colors_base + i*2, step=1))

def typewriter(r0, c0, width, lines, start_phase, delay=0.02):
    # Prepare empty buffers
    buffers = [" " * len(line) for line in lines]
    total = sum(len(x) for x in lines)
    count = 0
    li = 0
    ci = 0
    # Flatten indices
    positions = [(i, j) for i, line in enumerate(lines) for j in range(len(line))]
    for k, (li, ci) in enumerate(positions):
        # update one char
        line = buffers[li]
        buffers[li] = line[:ci] + lines[li][ci] + line[ci+1:]
        # redraw inner
        draw_inner_lines(r0, c0, width, buffers, text_colors_base=start_phase)
        sys.stdout.flush()
        time.sleep(delay)

def center_coords(total_rows, total_cols, box_h, box_w):
    r = max(1, (total_rows - box_h) // 2)
    c = max(1, (total_cols - box_w) // 2)
    return r, c

def main():
    quote = "I tried to meet my higher self; it sent a lower intern who apologized and suggested I lower my expectations."

    # Terminal size and layout
    cols, rows = shutil.get_terminal_size((80, 24))
    cols, rows = max(40, cols), max(16, rows)

    max_inner = max(20, min(cols - 10, 80))
    lines = wrap_quote(quote, max_inner)
    inner_w = max(len(l) for l in lines)
    box_w = inner_w + 4
    box_h = len(lines) + 4

    # Fallback if terminal too small
    if box_w + 4 > cols or box_h + 4 > rows:
        # Simple colorful print
        print(HIDE, end="")
        print(clear(), end="")
        print(move(1,1), end="")
        print(gradient_text("“" + quote + "”", base=5, step=1))
        print(SHOW + RESET, end="")
        return

    r0, c0 = center_coords(rows, cols, box_h, box_w)

    sys.stdout.write(HIDE)
    sys.stdout.write(clear())
    sys.stdout.flush()

    # Intro shimmer
    for phase in range(24):
        draw_box(r0, c0, box_w, box_h, phase)
        # a faint halo fill
        for i in range(1, box_h-1):
            sys.stdout.write(move(r0 + i, c0 + 1))
            # subtle gradient background strips
            grad_row = ''.join(bg256(wheel(phase + i + j*2)) + " " for j in range(box_w-2)) + RESET
            sys.stdout.write(grad_row)
        # clear inner text space again (leave faint glow edges)
        for i in range(1, box_h-1):
            sys.stdout.write(move(r0 + i, c0 + 2))
            sys.stdout.write(" "*(box_w-4))
        sys.stdout.flush()
        time.sleep(0.03)

    # Final box without halo fill
    draw_box(r0, c0, box_w, box_h, phase=32)
    for i in range(1, box_h-1):
        sys.stdout.write(move(r0 + i, c0 + 1))
        sys.stdout.write(" "*(box_w-2))

    # Typewriter the quote with gentle sparkle
    typewriter(r0, c0, box_w, lines, start_phase=48, delay=0.015)

    # Add quotation marks artistically in corners inside the box
    sys.stdout.write(move(r0 + 1, c0 + 2))
    sys.stdout.write(fg256(wheel(90)) + "“" + RESET)
    sys.stdout.write(move(r0 + box_h - 2, c0 + box_w - 3))
    sys.stdout.write(fg256(wheel(102)) + "”" + RESET)

    sys.stdout.flush()
    time.sleep(1.2)
    sys.stdout.write(SHOW + RESET)
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write(SHOW + RESET)
        sys.stdout.flush()