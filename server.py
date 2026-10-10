from mcp.server.fastmcp import FastMCP


# ============================================================
# MCP SERVER
# ============================================================

mcp = FastMCP("PersonalizedLetterWritingMCP")


# ============================================================
# OPTIONS THE USER CAN CHOOSE
# ============================================================

KNOWN_LANGUAGES = ["English", "Tamil", "Tanglish"]

KNOWN_TONES = [
    "Cute", "Warm", "Emotional", "Funny", "Friendly",
    "Casual", "Formal", "Respectful", "Inspirational", "Playful",
]

KNOWN_FORMATS = [
    "Plain Text Message",
    "Clean Digital Letter",
    "Formal Letter",
    "Cute Handwritten Letter",
    "Cute Scrapbook Letter",
    "Minimal & Aesthetic",
]

# Short names people may type instead of the full format name
FORMAT_ALIASES = {
    "plain": "Plain Text Message",
    "plain text": "Plain Text Message",
    "text": "Plain Text Message",
    "message": "Plain Text Message",
    "whatsapp": "Plain Text Message",
    "whatsapp message": "Plain Text Message",
    "sms": "Plain Text Message",
    "clean": "Clean Digital Letter",
    "digital": "Clean Digital Letter",
    "formal": "Formal Letter",
    "handwritten": "Cute Handwritten Letter",
    "cute handwritten": "Cute Handwritten Letter",
    "scrapbook": "Cute Scrapbook Letter",
    "cute scrapbook": "Cute Scrapbook Letter",
    "minimal": "Minimal & Aesthetic",
    "aesthetic": "Minimal & Aesthetic",
    "minimal and aesthetic": "Minimal & Aesthetic",
}


# ============================================================
# DESIGN KNOWLEDGE (colors, ready-made page templates)
# ============================================================

DEFAULT_COLORS = {
    "main": "#E8548C", "soft": "#F9C6D9", "alt": "#9C6ADE",
    "sun": "#FFD54F", "leaf": "#8FCB9B", "paper": "#FFF4EC", "ink": "#4A2F3A",
}


def _c(main, soft, alt, sun, leaf, paper, ink):
    return {"main": main, "soft": soft, "alt": alt, "sun": sun,
            "leaf": leaf, "paper": paper, "ink": ink}


# The first matching word in the user's themes decides the colors
THEME_COLORS = {
    "flower": _c("#E8548C", "#F9C6D9", "#9C6ADE", "#FFD54F", "#8FCB9B", "#FFF4EC", "#4A2F3A"),
    "garden": _c("#3E9B55", "#CDEBC5", "#E8548C", "#FFD54F", "#8FCB9B", "#F8FFF2", "#2F4A36"),
    "butterfl": _c("#8E5BD6", "#E3D4F7", "#2CA4DE", "#FFC470", "#8FCB9B", "#F7F2FF", "#3B2F57"),
    "panda": _c("#E8548C", "#F9C6D9", "#4FB286", "#FFD54F", "#8FCB9B", "#FFF6F0", "#2B2B33"),
    "cat": _c("#F28B3C", "#FFE0B8", "#7A8CC8", "#FFD54F", "#8FCB9B", "#FFF8EE", "#4A3A2E"),
    "bunn": _c("#EC6FA0", "#FAD1E2", "#7FB8E8", "#FFE082", "#9ED8A8", "#FFF8FB", "#4A3A44"),
    "heart": _c("#E8456F", "#FAC5D1", "#FF8A65", "#FFD54F", "#8FCB9B", "#FFF2F4", "#4A2A33"),
    "star": _c("#5C6BC0", "#D6DAF7", "#B07CD8", "#FFD54F", "#7FD0C0", "#F6F5FF", "#2E3354"),
    "moon": _c("#5C6BC0", "#D6DAF7", "#B07CD8", "#FFD54F", "#7FD0C0", "#F6F5FF", "#2E3354"),
    "nature": _c("#3E9B55", "#D5EBC9", "#2CA4DE", "#FFD54F", "#8FCB9B", "#FAFFF3", "#2F4A36"),
    "kawaii": _c("#F0549B", "#FFD0E6", "#35B8E0", "#FFE066", "#7FDDB0", "#FFF5FA", "#4A2F44"),
    "rainbow": _c("#EF5B77", "#FFE1B8", "#6BA8F0", "#FFD54F", "#7FD08F", "#FFFBF2", "#43374A"),
    "teddy": _c("#C27C47", "#F4DFC6", "#E8548C", "#FFD54F", "#8FCB9B", "#FFF7EC", "#4A3526"),
    "sweet": _c("#EC5D8C", "#FFD6E3", "#8D6E63", "#FFE082", "#9ED8A8", "#FFF7F3", "#4E3434"),
    "dessert": _c("#EC5D8C", "#FFD6E3", "#8D6E63", "#FFE082", "#9ED8A8", "#FFF7F3", "#4E3434"),
    "animal": _c("#F28B3C", "#FFE0B8", "#4FB286", "#FFD54F", "#8FCB9B", "#FFF8EE", "#4A3A2E"),
}


def _colors_for(themes: list) -> dict:
    """Pick page colors from the user's themes, or a happy default."""
    found = []
    for theme in themes[:3]:
        lowered = theme.lower()
        for key, colors in THEME_COLORS.items():
            if key in lowered:
                found.append(colors)
                break
    result = dict(found[0]) if found else dict(DEFAULT_COLORS)
    if len(found) > 1:
        result["alt"] = found[1]["main"]
        result["leaf"] = found[1]["leaf"]
    if len(found) > 2:
        result["sun"] = found[2]["sun"]
    return result


def _fill_colors(template: str, colors: dict) -> str:
    html = template.replace("<!--SYMS-->", SYMBOLS)
    for name, value in colors.items():
        html = html.replace("[[" + name.upper() + "]]", value)
    return html


# Short descriptions (used by the letter://formats resource)
FORMAT_DESIGN = {
    "Plain Text Message": (
        "No page design. Return only the message, ready to paste into "
        "WhatsApp, Instagram or SMS. A few fitting emojis are fine."
    ),
    "Clean Digital Letter": (
        "Cream stationery with a double colored border, flower corners, a "
        "round portrait ring at the top, an elegant serif headline, a "
        "flower divider, a script signature and a soft P.S. box."
    ),
    "Formal Letter": (
        "White paper with a thin colored top line, serif text, the date at "
        "top right, 'Dear ...' and a plain signature. No decorations, no "
        "emojis and no portrait."
    ),
    "Cute Handwritten Letter": (
        "Pastel page: dashed frame, flower corners, a big "
        "handwritten headline, a tilted taped "
        "polaroid portrait, highlighted words, a speech-bubble "
        "sticker and a taped P.S. note."
    ),
    "Cute Scrapbook Letter": (
        "Kraft-paper scrapbook: a torn-paper sheet with washi tape, a "
        "colored title label, a tilted polaroid portrait, a "
        "taped P.S. note and a round sticker badge."
    ),
    "Minimal & Aesthetic": (
        "Airy off-white page with a large script headline, a small round "
        "portrait, thin lines, light text, a script signature and a tiny "
        "line-art branch."
    ),
}

PORTRAIT_PLACEMENT = {
    "Clean Digital Letter": "in the round ring at the top center",
    "Cute Handwritten Letter": "in the tilted taped polaroid at the top right",
    "Cute Scrapbook Letter": "in the tilted polaroid at the top right of the paper",
    "Minimal & Aesthetic": "in the small circle at the top right",
}

TEMPLATE_FOR = {
    "Clean Digital Letter": "cd",
    "Formal Letter": "fm",
    "Cute Handwritten Letter": "hw",
    "Cute Scrapbook Letter": "sb",
    "Minimal & Aesthetic": "mn",
}

PORTRAIT_PROMPT = (
    "Turn the person in the attached photo into a cute illustrated "
    "portrait for a handwritten-style letter. Style: soft watercolor and "
    "colored-pencil kawaii illustration, big sparkling eyes, rosy cheeks, "
    "gentle smile, smooth soft shading, warm pastel colors, delicate "
    "hand-drawn outlines, slightly textured paper look. Keep the person's "
    "recognizable features such as hairstyle, clothes and accessories. "
    "Plain soft background, portrait only, no text."
)

# Shared flower, heart and star shapes used by the templates
SYMBOLS = r"""<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="flower" viewBox="0 0 90 90"><ellipse class="lf" cx="20" cy="74" rx="16" ry="6" transform="rotate(-25 20 74)"/><ellipse class="lf" cx="70" cy="74" rx="16" ry="6" transform="rotate(25 70 74)"/><circle class="pt" cx="45" cy="18" r="14"/><circle class="pt" cx="66" cy="33" r="14"/><circle class="pt" cx="58" cy="58" r="14"/><circle class="pt" cx="32" cy="58" r="14"/><circle class="pt" cx="24" cy="33" r="14"/><circle class="ct" cx="45" cy="40" r="10"/></symbol>
<symbol id="heart" viewBox="0 0 20 20"><path class="pt" d="M10 18C-6 6 2-4 10 4C18-4 26 6 10 18Z"/></symbol>
<symbol id="star" viewBox="0 0 20 20"><path class="pt" d="M10 0L12.9 6.9L20 7.6L14.6 12.4L16.2 19.5L10 15.8L3.8 19.5L5.4 12.4L0 7.6L7.1 6.9Z"/></symbol>
</defs></svg>"""

# Ready-made, tested page designs. The text can never overlap the
# decorations because every item has its own space in the layout.
TEMPLATES = {
    "hw": r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;700&display=swap" rel="stylesheet">
<style>
:root{--main:[[MAIN]];--soft:[[SOFT]];--alt:[[ALT]];--sun:[[SUN]];--leaf:[[LEAF]];--paper:[[PAPER]];--ink:[[INK]];--rule:color-mix(in srgb,var(--main) 22%,transparent)}
*{box-sizing:border-box}
html,body{margin:0}
body{background:#EFE3DA;display:flex;justify-content:center;font-family:'Caveat','Comic Sans MS',cursive;color:var(--ink)}
.page{position:relative;width:794px;min-height:1123px;padding:84px;background:var(--paper);display:flex;flex-direction:column;gap:28px;overflow:hidden}
.page>.head,.page>.letter,.page>.foot{position:relative;z-index:1}
.frame{position:absolute;inset:18px;border:3px dashed var(--main);border-radius:26px;pointer-events:none}
.deco{position:absolute;pointer-events:none}
.pt{fill:currentColor}.ct{fill:var(--sun)}.lf{fill:var(--leaf)}
.c1{left:6px;top:6px;width:72px;color:var(--main)}
.c2{right:6px;top:6px;width:72px;color:var(--alt)}
.c3{left:6px;bottom:6px;width:72px;color:var(--alt)}
.c4{right:6px;bottom:6px;width:72px;color:var(--main)}
.s1{left:30px;top:380px;width:26px;color:var(--sun)}
.s2{right:30px;top:520px;width:24px;color:var(--main)}
.s3{left:30px;top:760px;width:24px;color:var(--alt)}
.s4{right:28px;top:900px;width:26px;color:var(--sun)}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:28px}
.titlebox{flex:1;min-width:0;padding-top:16px}
.kicker{font-size:30px;line-height:1.1;color:var(--alt);font-weight:700}
h1{margin:4px 0 8px;font-size:80px;line-height:.98;font-weight:700;color:var(--main);overflow-wrap:anywhere}
.polaroid{flex:none;position:relative;width:206px;margin-top:6px;padding:12px 12px 8px;background:#fff;box-shadow:0 6px 16px rgba(0,0,0,.18);transform:rotate(3deg)}
.pic{width:182px;height:196px;background:var(--soft);overflow:hidden}
.pic img,.pic svg{width:100%;height:100%;object-fit:cover;display:block}
.cap{text-align:center;font-size:26px;line-height:34px}
.tape{position:absolute;width:74px;height:24px;opacity:.9}
.t1{top:-12px;left:-16px;background:var(--soft);transform:rotate(-12deg)}
.t2{top:-12px;right:-16px;background:var(--leaf);transform:rotate(10deg)}
.letter{--lh:40px;flex:1;font-size:27px;line-height:var(--lh)}
.letter.m{--lh:36px;font-size:24px}
.letter.s{--lh:30px;font-size:20px}
.letter p{margin:0 0 var(--lh)}
.letter p:last-child{margin-bottom:0}
.hl{background:var(--sun);padding:0 6px;border-radius:6px}
.hl2{background:var(--soft);padding:0 6px;border-radius:6px}
.foot{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.sign{flex:1;min-width:0;font-size:30px;line-height:1.15}
.name{display:block;font-size:76px;line-height:1.05;font-weight:700;color:var(--main)}
.notes{width:270px;flex:none;display:flex;flex-direction:column;gap:22px}
.sticker{align-self:flex-start;background:var(--soft);padding:10px 20px;border-radius:24px 24px 24px 4px;font-size:28px;line-height:1.1;transform:rotate(-3deg)}
.ps{position:relative;background:#FFF59D;padding:18px 16px 12px;font-size:24px;line-height:1.2;transform:rotate(2deg);box-shadow:0 3px 8px rgba(0,0,0,.16)}
.ps:before{content:"";position:absolute;top:-10px;left:50%;margin-left:-32px;width:64px;height:20px;background:var(--alt);opacity:.85;transform:rotate(-4deg)}
@page{size:A4;margin:0}
@media print{body{background:none}}
</style>
</head>
<body>
<!--SYMS-->
<div class="page">
<div class="frame"></div>
<svg class="deco c1" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c2" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c3" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c4" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco s1" viewBox="0 0 20 20"><use href="#star"/></svg>
<svg class="deco s2" viewBox="0 0 20 20"><use href="#heart"/></svg>
<svg class="deco s3" viewBox="0 0 20 20"><use href="#heart"/></svg>
<svg class="deco s4" viewBox="0 0 20 20"><use href="#star"/></svg>
<div class="head">
<div class="titlebox">
<div class="kicker">[[KICKER]]</div>
<h1>[[TITLE]]</h1>
</div>
<div class="polaroid">
<div class="tape t1"></div><div class="tape t2"></div>
<div class="pic">[[PORTRAIT]]</div>
<div class="cap">[[CAPTION]]</div>
</div>
</div>
<div class="letter">
[[BODY]]
</div>
<div class="foot">
<div class="sign">[[SIGNOFF]]<span class="name">[[NAME]]</span></div>
<div class="notes">
<div class="sticker">[[STICKER]]</div>
<div class="ps">[[PS]]</div>
</div>
</div>
</div>
</body>
</html>
""",
    "sb": r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<link href="https://fonts.googleapis.com/css2?family=Patrick+Hand&family=Caveat:wght@700&display=swap" rel="stylesheet">
<style>
:root{--main:[[MAIN]];--soft:[[SOFT]];--alt:[[ALT]];--sun:[[SUN]];--leaf:[[LEAF]];--paper:[[PAPER]];--ink:[[INK]];--rule:rgba(90,130,190,.28)}
*{box-sizing:border-box}
html,body{margin:0}
body{background:#B99B72;display:flex;justify-content:center;font-family:'Patrick Hand','Caveat','Comic Sans MS',cursive;color:var(--ink)}
.page{position:relative;width:794px;min-height:1123px;padding:76px 66px 100px;background-color:#D8B98C;background-image:radial-gradient(rgba(255,255,255,.3) 1.6px,transparent 1.9px);background-size:22px 22px;display:flex;flex-direction:column;overflow:hidden}
.page>.sheet,.page>.under{position:relative}
.deco{position:absolute;pointer-events:none}
.pt{fill:currentColor}.ct{fill:var(--sun)}.lf{fill:var(--leaf)}
.c1{left:4px;top:4px;width:62px;color:var(--main)}
.c2{right:4px;top:4px;width:62px;color:var(--alt)}
.c3{left:4px;bottom:4px;width:62px;color:var(--alt)}
.c4{right:4px;bottom:4px;width:62px;color:var(--main)}
.s1{left:22px;top:400px;width:24px;color:var(--paper)}
.s2{right:22px;top:560px;width:24px;color:var(--main)}
.s3{left:22px;top:760px;width:24px;color:var(--soft)}
.s4{right:22px;top:880px;width:24px;color:var(--paper)}
.sheet{flex:1;display:flex;z-index:1;filter:drop-shadow(0 8px 10px rgba(70,40,10,.32));transform:rotate(-.6deg)}
.paper{flex:1;display:flex;flex-direction:column;gap:26px;padding:60px 46px 88px;background:#FFFDF6;clip-path:polygon(0% 8px,4% 2px,8% 8px,12% 2px,16% 8px,20% 2px,24% 8px,28% 2px,32% 8px,36% 2px,40% 8px,44% 2px,48% 8px,52% 2px,56% 8px,60% 2px,64% 8px,68% 2px,72% 8px,76% 2px,80% 8px,84% 2px,88% 8px,92% 2px,96% 8px,100% 2px,100% calc(100% - 2px),96% calc(100% - 8px),92% calc(100% - 2px),88% calc(100% - 8px),84% calc(100% - 2px),80% calc(100% - 8px),76% calc(100% - 2px),72% calc(100% - 8px),68% calc(100% - 2px),64% calc(100% - 8px),60% calc(100% - 2px),56% calc(100% - 8px),52% calc(100% - 2px),48% calc(100% - 8px),44% calc(100% - 2px),40% calc(100% - 8px),36% calc(100% - 2px),32% calc(100% - 8px),28% calc(100% - 2px),24% calc(100% - 8px),20% calc(100% - 2px),16% calc(100% - 8px),12% calc(100% - 2px),8% calc(100% - 8px),4% calc(100% - 2px),0% calc(100% - 8px))}
.tp{position:absolute;z-index:3;width:100px;height:28px;opacity:.88;top:-14px}
.tp1{left:56px;background:var(--soft);transform:rotate(-6deg)}
.tp2{right:56px;background:var(--leaf);transform:rotate(7deg)}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:22px}
.titlebox{flex:1;min-width:0;padding-top:8px}
.label{display:inline-block;max-width:100%;background:var(--soft);padding:8px 26px 12px;transform:rotate(-2deg);box-shadow:0 2px 5px rgba(0,0,0,.16)}
h1{margin:0;font-family:'Caveat','Patrick Hand',cursive;font-size:60px;line-height:1;font-weight:700;color:var(--main);overflow-wrap:anywhere}
.kicker{margin-top:18px;font-size:26px;line-height:1.2}
.polaroid{flex:none;position:relative;width:200px;padding:12px 12px 8px;background:#fff;box-shadow:0 5px 14px rgba(0,0,0,.2);transform:rotate(-4deg)}
.pic{width:176px;height:190px;background:var(--soft);overflow:hidden}
.pic img,.pic svg{width:100%;height:100%;object-fit:cover;display:block}
.cap{text-align:center;font-size:24px;line-height:32px}
.pt1{position:absolute;top:-12px;left:50%;margin-left:-38px;width:76px;height:24px;background:var(--alt);opacity:.88;transform:rotate(3deg)}
.letter{--lh:36px;flex:1;font-size:25px;line-height:var(--lh)}
.letter.m{--lh:32px;font-size:22px}
.letter.s{--lh:28px;font-size:19px}
.letter p{margin:0 0 var(--lh)}
.letter p:last-child{margin-bottom:0}
.hl{background:var(--sun);padding:0 5px;border-radius:5px}
.hl2{background:var(--soft);padding:0 5px;border-radius:5px}
.sign{font-size:28px;line-height:1.15}
.name{display:block;font-family:'Caveat','Patrick Hand',cursive;font-size:64px;line-height:1.05;font-weight:700;color:var(--main)}
.under{z-index:2;display:flex;justify-content:space-between;align-items:flex-start;gap:20px;margin-top:-56px;padding:0 26px}
.ps{position:relative;width:310px;background:#FFF59D;padding:20px 18px 14px;font-size:24px;line-height:1.2;transform:rotate(2.5deg);box-shadow:0 4px 10px rgba(0,0,0,.22)}
.ps:before{content:"";position:absolute;top:-11px;left:50%;margin-left:-34px;width:68px;height:22px;background:var(--alt);opacity:.88;transform:rotate(-4deg)}
.badge{flex:none;width:176px;height:176px;border-radius:50%;background:var(--soft);border:4px dashed var(--main);display:flex;align-items:center;justify-content:center;text-align:center;padding:20px;font-size:27px;line-height:1.1;transform:rotate(8deg);box-shadow:0 4px 10px rgba(0,0,0,.2)}
@page{size:A4;margin:0}
@media print{body{background:none}}
</style>
</head>
<body>
<!--SYMS-->
<div class="page">
<svg class="deco c1" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c2" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c3" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c4" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco s1" viewBox="0 0 20 20"><use href="#star"/></svg>
<svg class="deco s2" viewBox="0 0 20 20"><use href="#heart"/></svg>
<svg class="deco s3" viewBox="0 0 20 20"><use href="#heart"/></svg>
<svg class="deco s4" viewBox="0 0 20 20"><use href="#star"/></svg>
<div class="sheet">
<div class="tp tp1"></div><div class="tp tp2"></div>
<div class="paper">
<div class="head">
<div class="titlebox">
<div class="label"><h1>[[TITLE]]</h1></div>
<div class="kicker">[[KICKER]]</div>
</div>
<div class="polaroid">
<div class="pt1"></div>
<div class="pic">[[PORTRAIT]]</div>
<div class="cap">[[CAPTION]]</div>
</div>
</div>
<div class="letter">
[[BODY]]
</div>
<div class="sign">[[SIGNOFF]]<span class="name">[[NAME]]</span></div>
</div>
</div>
<div class="under">
<div class="ps">[[PS]]</div>
<div class="badge">[[STICKER]]</div>
</div>
</div>
</body>
</html>
""",
    "cd": r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;1,400&family=Playfair+Display:ital,wght@1,500&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
:root{--main:[[MAIN]];--soft:[[SOFT]];--alt:[[ALT]];--sun:[[SUN]];--leaf:[[LEAF]];--paper:[[PAPER]];--ink:[[INK]]}
*{box-sizing:border-box}
html,body{margin:0}
body{background:#E9E2D8;display:flex;justify-content:center;font-family:'Lora',Georgia,serif;color:var(--ink)}
.page{position:relative;width:794px;min-height:1123px;padding:100px 104px 96px;background:var(--paper);display:flex;flex-direction:column;align-items:center;gap:22px;overflow:hidden}
.page>.top,.page>.letter,.page>.close{position:relative;z-index:1}
.b1{position:absolute;inset:20px;border:2px solid var(--main);pointer-events:none}
.b2{position:absolute;inset:30px;border:1px solid var(--soft);pointer-events:none}
.deco{position:absolute;pointer-events:none}
.pt{fill:currentColor}.ct{fill:var(--sun)}.lf{fill:var(--leaf)}
.c1{left:12px;top:12px;width:64px;color:var(--main)}
.c2{right:12px;top:12px;width:64px;color:var(--alt)}
.c3{left:12px;bottom:12px;width:64px;color:var(--alt)}
.c4{right:12px;bottom:12px;width:64px;color:var(--main)}
.top{width:100%;display:flex;flex-direction:column;align-items:center;gap:16px}
.date{align-self:flex-end;font-size:14px;font-style:italic;color:var(--main)}
.ring{width:128px;height:128px;border-radius:50%;padding:5px;background:var(--main)}
.pic{width:100%;height:100%;border-radius:50%;overflow:hidden;background:var(--soft);border:3px solid var(--paper)}
.pic img,.pic svg{width:100%;height:100%;object-fit:cover;display:block}
h1{margin:6px 0 0;font-family:'Playfair Display',Georgia,serif;font-style:italic;font-weight:500;font-size:46px;line-height:1.1;text-align:center;color:var(--main);overflow-wrap:anywhere}
.kicker{font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:var(--alt);text-align:center}
.divider{display:flex;align-items:center;gap:14px;width:70%}
.divider i{flex:1;height:1px;background:var(--soft)}
.divider svg{width:34px;color:var(--main)}
.letter{--fs:19px;width:100%;flex:1;font-size:var(--fs);line-height:1.85}
.letter.m{--fs:17px}.letter.s{--fs:15px}
.letter p{margin:0 0 1em}
.hl{background:color-mix(in srgb,var(--sun) 55%,transparent);padding:0 4px}
.close{width:100%;text-align:center}
.sign{font-style:italic;font-size:17px}
.name{display:block;margin-top:2px;font-family:'Great Vibes',cursive;font-size:56px;line-height:1.1;color:var(--main)}
.ps{margin:16px auto 0;max-width:420px;padding:12px 20px;background:color-mix(in srgb,var(--soft) 40%,white);border-radius:12px;font-size:15px;font-style:italic}
@page{size:A4;margin:0}
@media print{body{background:none}}
</style>
</head>
<body>
<!--SYMS-->
<div class="page">
<div class="b1"></div><div class="b2"></div>
<svg class="deco c1" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c2" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c3" viewBox="0 0 90 90"><use href="#flower"/></svg>
<svg class="deco c4" viewBox="0 0 90 90"><use href="#flower"/></svg>
<div class="top">
<div class="date">[[DATE]]</div>
<div class="ring"><div class="pic">[[PORTRAIT]]</div></div>
<div class="kicker">[[KICKER]]</div>
<h1>[[TITLE]]</h1>
<div class="divider"><i></i><svg viewBox="0 0 90 90"><use href="#flower"/></svg><i></i></div>
</div>
<div class="letter">
[[BODY]]
</div>
<div class="close">
<div class="sign">[[SIGNOFF]]<span class="name">[[NAME]]</span></div>
<div class="ps">[[PS]]</div>
</div>
</div>
</body>
</html>
""",
    "mn": r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@300;400&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
:root{--main:[[MAIN]];--soft:[[SOFT]];--alt:[[ALT]];--sun:[[SUN]];--leaf:[[LEAF]];--paper:[[PAPER]];--ink:[[INK]]}
*{box-sizing:border-box}
html,body{margin:0}
body{background:#E7E2DB;display:flex;justify-content:center;font-family:'Jost','Helvetica Neue',Arial,sans-serif;font-weight:300;color:var(--ink)}
.page{width:794px;min-height:1123px;padding:104px 100px 90px;background:var(--paper);display:flex;flex-direction:column;gap:44px}
.head{display:flex;justify-content:space-between;align-items:flex-start;gap:30px}
.date{font-size:13px;letter-spacing:.22em;text-transform:uppercase;color:var(--main);font-weight:400}
h1{margin:10px 0 0;font-family:'Great Vibes','Brush Script MT',cursive;font-weight:400;font-size:84px;line-height:1.05;color:var(--ink);overflow-wrap:anywhere}
.kicker{margin-top:6px;font-size:15px;letter-spacing:.08em;color:var(--alt)}
.pic{flex:none;width:96px;height:96px;border-radius:50%;overflow:hidden;background:var(--soft)}
.pic img,.pic svg{width:100%;height:100%;object-fit:cover;display:block}
.hr{height:1px;background:var(--soft)}
.letter{--fs:17px;flex:1;font-size:var(--fs);line-height:2}
.letter.m{--fs:15.5px}.letter.s{--fs:14px}
.letter p{margin:0 0 1.1em}
.hl{box-shadow:inset 0 -.5em 0 color-mix(in srgb,var(--sun) 60%,transparent)}
.sign{font-size:15px;letter-spacing:.04em}
.name{display:block;margin-top:2px;font-family:'Great Vibes',cursive;font-size:54px;line-height:1.1;color:var(--main)}
.ps{margin-top:18px;font-size:14px;color:var(--alt)}
.leaf{display:block;margin:6px auto 0;width:150px;height:60px;fill:none;stroke:var(--main);stroke-width:1.4;stroke-linecap:round}
@page{size:A4;margin:0}
@media print{body{background:none}}
</style>
</head>
<body>
<div class="page">
<div class="head">
<div>
<div class="date">[[DATE]]</div>
<h1>[[TITLE]]</h1>
<div class="kicker">[[KICKER]]</div>
</div>
<div class="pic">[[PORTRAIT]]</div>
</div>
<div class="hr"></div>
<div class="letter">
[[BODY]]
</div>
<div class="close">
<div class="sign">[[SIGNOFF]]<span class="name">[[NAME]]</span></div>
<div class="ps">[[PS]]</div>
</div>
<svg class="leaf" viewBox="0 0 150 60"><path d="M10 50C50 40 100 40 140 20"/><path d="M45 44C40 30 52 22 62 24C62 36 56 42 45 44Z"/><path d="M80 38C78 24 90 16 100 18C100 30 94 36 80 38Z"/><path d="M112 30C112 18 122 12 130 14C128 24 122 29 112 30Z"/></svg>
</div>
</body>
</html>
""",
    "fm": r"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>[[TITLE]]</title>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">
<style>
:root{--main:[[MAIN]];--ink:#222222}
*{box-sizing:border-box}
html,body{margin:0}
body{background:#E7E7E7;display:flex;justify-content:center;font-family:'Lora',Georgia,'Times New Roman',serif;color:var(--ink)}
.page{width:794px;min-height:1123px;padding:96px 110px 90px;background:#fff;border-top:8px solid var(--main);display:flex;flex-direction:column;gap:30px}
.date{text-align:right;font-size:16px}
.greeting{font-size:19px;font-weight:600}
.letter{--fs:18px;flex:none;font-size:var(--fs);line-height:1.8}
.letter.m{--fs:16.5px}.letter.s{--fs:15px}
.letter p{margin:0 0 1em}
.sign{font-size:18px}
.name{display:block;margin-top:42px;font-weight:600}
@page{size:A4;margin:0}
@media print{body{background:none}}
</style>
</head>
<body>
<div class="page">
<div class="date">[[DATE]]</div>
<div class="greeting">[[TITLE]]</div>
<div class="letter">
[[BODY]]
</div>
<div class="sign">[[SIGNOFF]]<span class="name">[[NAME]]</span></div>
</div>
</body>
</html>
""",
}


# ============================================================
# RESOURCE 1: GENERAL LETTER WRITING GUIDELINES
# ============================================================

@mcp.resource("letter://guidelines")
def letter_guidelines() -> str:
    """General guidelines for creating personalized letters."""

    return """
PERSONALIZED LETTER WRITING GUIDELINES
======================================

Purpose
-------
Create natural, meaningful and personalized letters from the user's
original thoughts, situations or rough messages.

The user does NOT need to specify a letter type. Infer the purpose
(birthday, thank you, apology, farewell, love, encouragement, pregnancy,
graduation, professional, or anything else) from the message. If the
purpose is unclear, preserve the user's intention instead of inventing one.

CORE RULES
----------
1. Understand the user's intention before writing.
2. Preserve the meaning and emotional intention of the message.
3. Preserve important personal details given by the user.
4. Never invent memories, relationships, events, achievements,
   experiences or facts about the recipient.
5. Do not assume a relationship the user did not mention.
6. Do not translate word for word.
7. Sound natural and human; avoid robotic phrases and cliches.
8. Do not use birthday phrases when the letter is not about a birthday.
9. Do not make every letter follow the same structure.
10. Match the emotional intensity of the original message.
11. Do not mention AI or the writing process unless asked.

PERSONALIZATION
---------------
Use the user's details naturally. Do not copy every detail; pick the ones
that make the letter feel personal and sincere.

LENGTH
------
Do not stretch a short message into a long letter, and do not make an
important emotional letter too short.
"""


# ============================================================
# RESOURCE 2: TONE GUIDELINES
# ============================================================

@mcp.resource("letter://tones")
def tone_guidelines() -> str:
    """Definitions and writing rules for supported tones."""

    return """
LETTER TONE GUIDELINES
======================

Cute          Sweet, playful, affectionate and light-hearted.
Warm          Sincere, comforting, caring and gentle.
Emotional     Heartfelt, meaningful and sincere.
Funny         Light-hearted and humorous without being insensitive.
Friendly      Natural, comfortable and conversational.
Casual        Relaxed and informal, like everyday chat.
Formal        Respectful, polished and professional.
Respectful    Courteous and considerate, still natural.
Inspirational Positive, encouraging and motivating.
Playful       Energetic, cheerful and slightly mischievous.

TONE RULES
----------
1. Follow the selected tone, but do not exaggerate it.
2. If the message is emotional, do not make it unnecessarily funny.
3. If several tones are given, blend them naturally.
4. For a custom tone (for example "sarcastic but sweet"), interpret it
   sensibly and keep the emotional intention.
"""


# ============================================================
# RESOURCE 3: OUTPUT FORMAT GUIDELINES
# ============================================================

@mcp.resource("letter://formats")
def format_guidelines() -> str:
    """Design rules for each supported output format."""

    lines = ["LETTER OUTPUT FORMAT GUIDELINES", "=" * 31, ""]
    for number, name in enumerate(KNOWN_FORMATS, start=1):
        lines.append(f"{number}. {name.upper()}")
        lines.append(FORMAT_DESIGN[name])
        if name in PORTRAIT_PLACEMENT:
            lines.append("Portrait: " + PORTRAIT_PLACEMENT[name] + ".")
        lines.append("")

    lines.append(
        "PORTRAIT RULE\n"
        "-------------\n"
        "A portrait is optional. If the user attaches one, place it "
        "automatically using the placement above. Never ask the user "
        "where it should go. Never claim this MCP generated an image."
    )
    return "\n".join(lines)


# ============================================================
# RESOURCE 4: LANGUAGE GUIDELINES
# ============================================================

@mcp.resource("letter://languages")
def language_guidelines() -> str:
    """Language handling rules for English, Tamil and Tanglish."""

    return """
LETTER LANGUAGE GUIDELINES
==========================

Supported input languages:  English, Tamil, Tanglish (or a mix)
Supported output languages: English, Tamil, Tanglish

ENGLISH
-------
Use natural English. Avoid complicated vocabulary unless the tone needs it.

TAMIL
-----
Write natural Tamil. Do not translate word for word from English.
Keep the emotional meaning and conversational flow.

TANGLISH
--------
Tamil written in English letters, mixed naturally with English.
Example: "Unakku romba happy birthday da! Nee eppavume ipdi happy ah
irukkanum."
Do not convert Tanglish into formal Tamil unless Tamil output is requested.

MIXED INPUT
-----------
1. Understand the full meaning.
2. Identify the emotional intention.
3. Produce the requested output language consistently.
Do not copy the mixed-language structure unless Tanglish was requested.
"""


# ============================================================
# RESOURCE 5: VISUAL THEME GUIDELINES
# ============================================================

@mcp.resource("letter://themes")
def theme_guidelines() -> str:
    """Supported visual themes, colors and combination rules."""

    lines = [
        "LETTER VISUAL THEME GUIDELINES",
        "==============================",
        "",
        "Suggested themes: Flowers, Butterflies, Panda, Cute Cats, Bunnies,",
        "Hearts, Stars & Moon, Nature, Kawaii, Rainbow, Teddy Bears, Garden,",
        "Sweet/Dessert, Cute Animals. Custom themes are allowed.",
        "",
        "RULES",
        "-----",
        "1. Up to three themes. If more are given, use the first three.",
        "2. Theme 1 = main visual, Theme 2 = supporting, Theme 3 = small accent.",
        "3. Themes shape the design; do not keep repeating them in the text.",
        "4. Be colorful, but never crowded.",
        "",
        "DEFAULT COLORS",
        "--------------",
        ", ".join(f"{k} {v}" for k, v in DEFAULT_COLORS.items()),
        "",
        "COLORS PER THEME",
        "----------------",
    ]
    for key, c in THEME_COLORS.items():
        lines.append(f"{key}: main {c['main']}, soft {c['soft']}, alt {c['alt']}")
    return "\n".join(lines)


# ============================================================
# HELPERS
# ============================================================

def _match(value: str, options: list, aliases: dict = None) -> tuple:
    """Return (clean_value, is_known). Ignores capital letters."""
    cleaned = value.strip()
    lowered = cleaned.lower()

    for option in options:
        if option.lower() == lowered:
            return option, True

    if aliases and lowered in aliases:
        return aliases[lowered], True

    return cleaned, False


def _has_portrait(portrait: str) -> bool:
    return portrait.strip().lower() in {"yes", "true", "y", "1", "attached"}


def _build_request(
    message: str,
    input_language: str = "",
    output_language: str = "",
    tone: str = "",
    output_format: str = "",
    themes: str = "",
    portrait: str = "",
) -> str:
    """Check the choices and build the full instructions for Claude."""

    # ---- Nothing to write about ----
    if not message.strip():
        return (
            "MISSING INFORMATION. Do not write anything yet. "
            "Ask the user what they want to say in the letter "
            "(who it is for and what the situation is)."
        )

    # ---- Find what is missing (only the three real choices) ----
    missing = []
    if not output_language.strip():
        missing.append(f"Output language ({', '.join(KNOWN_LANGUAGES)})")
    if not tone.strip():
        missing.append(f"Tone (for example: {', '.join(KNOWN_TONES)})")
    if not output_format.strip():
        missing.append(f"Format ({', '.join(KNOWN_FORMATS)})")

    if missing:
        return (
            "MISSING INFORMATION. Do not write the letter yet.\n"
            "Ask the user ONE short, friendly message that lists only these "
            "missing choices:\n- " + "\n- ".join(missing) + "\n"
            "Also mention, as optional extras: up to 3 themes (for example "
            "Panda, Flowers) and a portrait image they can attach.\n"
            "If the user says 'you choose' or 'anything', pick sensible "
            "choices yourself, then call this tool again with them."
        )

    # ---- Clean the values (never reject, always adapt) ----
    input_language = input_language.strip() or "Auto-detect from the message"
    if input_language != "Auto-detect from the message":
        input_language, _ = _match(input_language, KNOWN_LANGUAGES)

    output_language, lang_known = _match(output_language, KNOWN_LANGUAGES)
    tone, tone_known = _match(tone, KNOWN_TONES)
    output_format, format_known = _match(
        output_format, KNOWN_FORMATS, FORMAT_ALIASES
    )

    selected_themes = [
        t.strip()
        for t in themes.replace("+", ",").replace("&", ",").split(",")
        if t.strip() and t.strip().lower() != "none"
    ]

    notes = []
    if not lang_known:
        notes.append(
            f"'{output_language}' is not a built-in language. "
            "Write in it as naturally as you can."
        )
    if not tone_known:
        notes.append(
            f"'{tone}' is a custom tone. Interpret it sensibly and keep "
            "the emotional intention of the message."
        )
    if not format_known:
        notes.append(
            f"'{output_format}' is a custom format. Follow it as closely as "
            "you can; if unclear, use the Clean Digital Letter design."
        )
    if len(selected_themes) > 3:
        notes.append(
            "More than 3 themes were given. Use the first 3 and do not "
            "overcrowd the design."
        )
    notes_text = "\n".join(f"- {n}" for n in notes) or "- None"

    used_themes = selected_themes[:3]
    themes_text = ", ".join(used_themes) if used_themes else "None"
    colors = _colors_for(used_themes)
    portrait_given = _has_portrait(portrait)

    # ---- Plain text: no design at all ----
    if output_format == "Plain Text Message":
        delivery = (
            "DELIVERY\n"
            "- Return only the finished message.\n"
            "- No page design, no portrait, no image prompt."
        )
    else:
        layout = (
            output_format if output_format in TEMPLATE_FOR
            else "Clean Digital Letter"
        )
        template = _fill_colors(TEMPLATES[TEMPLATE_FOR[layout]], colors)

        if layout == "Formal Letter":
            portrait_rule = "This format has no portrait. Ignore this token."
        elif portrait_given:
            portrait_rule = (
                "The user attached a portrait. Put it here as an <img> tag "
                "(src as a base64 data URI of the image). The frame is "
                "already placed and sized, so never ask the user where it "
                "goes. If you cannot read the image file, draw a simple "
                "themed SVG mascot here instead and tell the user in one "
                "short line that the portrait could not be embedded."
            )
        else:
            portrait_rule = (
                "No portrait was attached. Draw a simple themed SVG mascot "
                "(for example a panda) or a small flower bouquet here, as "
                'inline <svg viewBox="0 0 100 100">.'
            )

        delivery = f"""DELIVERY
1. Write the finished letter in the requested language as short paragraphs.
2. Deliver ONE self-contained HTML page (an artifact or a file) by filling
   in the TEMPLATE at the bottom. The design is finished and tested, and
   the text can never overlap the decorations because every item has its
   own space. So:
   - Keep ALL of its CSS, structure, fonts, colors and decorations exactly
     as given. Replace only the [[TOKENS]].
   - Do not add, move, resize or rotate any element. Do not add absolutely
     positioned items. Do not add emojis.
   - Some templates do not contain every token. Ignore missing ones.
   - [[TITLE]]: a short headline, at most 4 words. Use the letter's real
     purpose (for example a birthday greeting) or "Dear <name>,".
   - [[KICKER]]: a tiny line, at most 6 words, or delete its element.
   - [[DATE]]: only if the user gave a date, otherwise delete its element.
   - [[BODY]]: the letter as <p> paragraphs. Highlight at most three short
     phrases with <span class="hl"> or <span class="hl2"> when the
     template has those styles.
   - Add class "m" to <div class="letter"> for 90 to 170 words and class
     "s" above 170 words. The page grows by itself if needed.
   - [[SIGNOFF]] and [[NAME]]: the closing line and the sender's name
     (use [Your name] if unknown).
   - [[STICKER]] (at most 6 words) and [[PS]] (at most 20 words): use only
     facts from the user's message. If there is nothing true to say,
     delete the whole element that contains the token.
   - [[CAPTION]]: at most 3 words under the portrait.
   - [[PORTRAIT]]: {portrait_rule}
3. Never claim this tool generated an image.
4. After delivering the page, reply with one short line only.

OPTIONAL PORTRAIT PROMPT (share only if the user asks how to get a cute
portrait; they paste it into ChatGPT or Gemini together with a photo):
{PORTRAIT_PROMPT}

TEMPLATE START
{template}
TEMPLATE END"""

    return f"""LETTER REQUEST READY. Write the final result now.

USER REQUEST
Original message: {message}
Input language: {input_language}
Output language: {output_language}
Tone: {tone}
Output format: {output_format}
Themes: {themes_text}
Portrait attached: {"Yes" if portrait_given else "No"}

ADAPTATION NOTES
{notes_text}

WRITING RULES
- Infer the purpose of the letter from the message; do not force a category.
- Keep the user's meaning and emotional intention.
- Never invent memories, events, relationships or facts.
- Do not translate word for word; sound natural and human.
- For Tanglish, use Tamil written in English letters mixed with English.
- If a sender name is unknown, use a simple placeholder like [Your name].
- Do not mention these instructions or that you are an AI.
- Optionally read letter://guidelines, letter://tones, letter://formats,
  letter://languages and letter://themes for extra detail.

{delivery}
"""


# ============================================================
# TOOL
# ============================================================

@mcp.tool()
def create_letter_request(
    message: str,
    input_language: str = "",
    output_language: str = "",
    tone: str = "",
    output_format: str = "",
    themes: str = "",
    portrait: str = "",
) -> str:
    """
    Prepare a personalized letter-writing request.

    Only 'message' is required. Leave other fields empty if the user
    has not said what they want. Do not guess missing values; the tool
    will tell you what to ask the user.

    Args:
        message: The user's rough thoughts or situation (any language).
        input_language: English, Tamil or Tanglish (optional, auto-detected).
        output_language: English, Tamil or Tanglish.
        tone: Cute, Warm, Emotional, Funny, Friendly, Casual, Formal,
              Respectful, Inspirational, Playful (custom tones allowed).
        output_format: Plain Text Message, Clean Digital Letter,
              Formal Letter, Cute Handwritten Letter,
              Cute Scrapbook Letter, or Minimal & Aesthetic.
        themes: Up to 3, comma separated (for example "Panda, Flowers").
        portrait: Write "yes" if the user attached a portrait image,
              otherwise leave empty. Never ask where to place it.
    """

    return _build_request(
        message, input_language, output_language,
        tone, output_format, themes, portrait,
    )


# ============================================================
# PROMPT
# ============================================================

@mcp.prompt()
def personalized_letter_writer(
    message: str,
    input_language: str = "",
    output_language: str = "",
    tone: str = "",
    output_format: str = "",
    themes: str = "",
    portrait: str = "",
) -> str:
    """
    Generate a personalized letter from the user's original
    thoughts and selected preferences.
    """

    return (
        "You are a personalized letter-writing assistant. Follow the "
        "instructions below exactly.\n\n"
        + _build_request(
            message, input_language, output_language,
            tone, output_format, themes, portrait,
        )
    )


# ============================================================
# SERVER ENTRY POINT
# ============================================================

if __name__ == "__main__":
    mcp.run(transport="stdio")