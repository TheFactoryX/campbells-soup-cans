"""
Campbell's Soup Can #1849
Produced: 2026-01-25 23:32:26
Worker: AllenAI: Molmo2 8B (free) (allenai/molmo-2-8b:free)
Employment: Volunteer
Flavor: Woody Allen Philosophy
Quality: ✅

Made by Machine #0 - Production Line 0
Like Warhol's soup cans - same but different.
Each can is the same flavor, made by different hands.
"""

import time

def center(msg, size=79):
    return f"\n{msg}\n" if len(msg) > size else f"\n{msg.center(size)}\n\n"

def border(msg, border='+', n=80):
    spaces = (n - len(msg)) // 2
    return f"{border * (spaces+2)}{msg}{border * (spaces+2)}" if len(msg) < n else msg

def color(code, text, reset='\033[0m'):
    return f'\033[{code}m{text}\033[{reset}]'

def wiggle(phrase, delay=0.1):
    print(phrase)
    s = time.time()
    while time.time() - s < 3:
        print('\r'+border('\n'+phrase+'\n', '_', 79)+'\r', end='')
        time.sleep(delay)

ASTERIX = '*'*45

QUOTE = "'It felt so wonderful until it felt so wonderful that it no longer felt so wonderful at all.'"

HEADER = '      {\n         *  HASTY SAD新世纪利他主义 NOMAD Python\n         *  哈哈.... 人生是混乱, 这行代码更重要呢。\n         *  ......\n        }\n'

MAIN_BODY = ASCII_ART + GOLD_BORDER + BOTTOM_BORDER

ASCII_ART = '''
        __   __
      /      \\__
   ~~  \\▰▱▰▱/  ~~
    __   ⛔   __
  _.−−−−−−−−−−−−−._
'''

GOLD_BORDER = '─ ( ─ ─  ─╢═┒' '牡蛎 像我这样..\n│  PYTHON│\n└─  ─ ─ ─╨╜'

BOTTOM_BORDER = '     ━▂▂▂▂▂▂▂▂▂▂▂\n'

HEADER_COLOR = 'cyan'
QUOTE_COLOR = 'dark gray'
BACK_COLOR = 'bright magenta'

TIP = '*   (试着在大脑里预览这个问题的答案。)\n*      别忘了和我分享生活中的 每一次误解哦。'

WOOZY = (
    '...'
    '对哲学的探索只能让生活变得更加糟糕:'
    '试过人生的每一刻都充满了怀疑和自我嘲笑吗？'
    '运气好我可以和你们一起探索人生的无底深渊...'
)

FONT_STYLE = 'colorama'


GROWL = '''
     ___________
    /             \\
   |  人生不可能   |
   \_______________/
'''

WOOZY = '''
  ｌｌｌｌ．ｌｌｌ(lll)...
'''