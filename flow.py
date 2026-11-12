"""The pipeline picture: what goes in, each tool, what comes out. One wide version, one tall for phones."""

TEAL, NAVY, MUTED, SOFT, HUMAN_BG, HUMAN_FG, CARD = (
    "#0b6e70", "#14213d", "#4a5668", "#e3f1ef", "#fce3cf", "#7a3410", "#fffffe")
FONT = "font-family=\"'Source Sans Pro', 'Segoe UI', Arial, sans-serif\""
MONO = "font-family=\"'JetBrains Mono', Consolas, monospace\""


def _icon(kind: str, cx: float, cy: float) -> str:
    """A 96px round badge with a simple drawing of the hand-off."""
    out = [f'<circle cx="{cx}" cy="{cy}" r="48" fill="{SOFT}" stroke="{TEAL}" stroke-width="2"/>']
    if kind == "doc":
        x, y = cx - 18, cy - 24
        out += [f'<path d="M{x} {y} h26 l10 10 v38 h-36 z" fill="{CARD}" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>',
                f'<path d="M{x + 26} {y} v10 h10" fill="none" stroke="{NAVY}" stroke-width="2.5" stroke-linejoin="round"/>']
        out += [f'<line x1="{x + 7}" y1="{y + 20 + i * 8}" x2="{x + 29}" y2="{y + 20 + i * 8}" stroke="{TEAL}" stroke-width="2.5" stroke-linecap="round"/>' for i in range(3)]
    elif kind == "sheet":
        x, y = cx - 22, cy - 20
        out.append(f'<rect x="{x}" y="{y}" width="44" height="40" rx="3" fill="{CARD}" stroke="{NAVY}" stroke-width="2.5"/>')
        out.append(f'<rect x="{x}" y="{y}" width="44" height="10" rx="2" fill="{TEAL}"/>')
        out += [f'<line x1="{x}" y1="{y + 10 + i * 10}" x2="{x + 44}" y2="{y + 10 + i * 10}" stroke="{NAVY}" stroke-width="1.5"/>' for i in (1, 2)]
        out += [f'<line x1="{x + 15 + i * 14}" y1="{y + 10}" x2="{x + 15 + i * 14}" y2="{y + 40}" stroke="{NAVY}" stroke-width="1.5"/>' for i in (0, 1)]
    elif kind == "code":
        out.append(f'<text x="{cx}" y="{cy + 11}" text-anchor="middle" font-size="32" font-weight="700" fill="{NAVY}" {MONO}>&lt;/&gt;</text>')
    elif kind == "pass":
        out += [f'<circle cx="{cx}" cy="{cy}" r="24" fill="{TEAL}"/>',
                f'<path d="M{cx - 11} {cy} l7 8 l15 -16" fill="none" stroke="{CARD}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>']
    return "".join(out)


STAGES = [("doc", "Requirements", "BRD · recording · images"),
          ("sheet", "Test cases", "approved, in Excel"),
          ("code", "Automation project", "Playwright or Selenium"),
          ("pass", "Tests passing", "fixed after approval")]
TOOLS = [("01", "Test Case Generator", "you approve each case"),
         ("02", "Automation Code Generator", "you review the code"),
         ("03", "Test Fixer (MCP)", "you approve each fix")]


def _arrow_h(x1, x2, y):
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 10}" y2="{y}" stroke="{TEAL}" stroke-width="3"/>'
            f'<path d="M{x2 - 12} {y - 8} L{x2} {y} L{x2 - 12} {y + 8} z" fill="{TEAL}"/>')


def _arrow_v(x, y1, y2):
    return (f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 10}" stroke="{TEAL}" stroke-width="3"/>'
            f'<path d="M{x - 8} {y2 - 12} L{x} {y2} L{x + 8} {y2 - 12} z" fill="{TEAL}"/>')


def _pill(cx, cy, text, w):
    return (f'<rect x="{cx - w / 2}" y="{cy - 13}" width="{w}" height="26" rx="13" fill="{HUMAN_BG}"/>'
            f'<text x="{cx}" y="{cy + 5}" text-anchor="middle" font-size="14" fill="{HUMAN_FG}" {FONT}>{text}</text>')


def wide() -> str:
    xs = [110, 470, 830, 1190]
    cy = 80
    parts = []
    for (num, name, human), x1, x2 in zip(TOOLS, xs, xs[1:]):
        mid = (x1 + x2) / 2
        parts.append(_arrow_h(x1 + 62, x2 - 62, cy))
        parts.append(f'<text x="{mid}" y="{cy - 16}" text-anchor="middle" font-size="16" font-weight="600" fill="{NAVY}" {FONT}>'
                     f'<tspan fill="{TEAL}" {MONO}>{num}</tspan> {name}</text>')
        parts.append(_pill(mid, cy + 26, human, 168))
    for (kind, title, sub), x in zip(STAGES, xs):
        parts.append(_icon(kind, x, cy))
        parts.append(f'<text x="{x}" y="{cy + 80}" text-anchor="middle" font-size="18" font-weight="600" fill="{NAVY}" {FONT}>{title}</text>')
        parts.append(f'<text x="{x}" y="{cy + 102}" text-anchor="middle" font-size="15" fill="{MUTED}" {FONT}>{sub}</text>')
    return (f'<svg class="flow-wide" viewBox="0 0 1300 200" width="100%" role="img" '
            f'aria-label="Requirements go through the Test Case Generator to test cases, through the Automation Code '
            f'Generator to an automation project, and through the Test Fixer to passing tests.">{"".join(parts)}</svg>')


def tall() -> str:
    x = 70
    ys = [70, 250, 430, 610]
    parts = []
    for (num, name, human), y1, y2 in zip(TOOLS, ys, ys[1:]):
        mid = (y1 + y2) / 2
        parts.append(_arrow_v(x, y1 + 56, y2 - 56))
        parts.append(f'<text x="{x + 34}" y="{mid - 4}" font-size="16" font-weight="600" fill="{NAVY}" {FONT}>'
                     f'<tspan fill="{TEAL}" {MONO}>{num}</tspan> {name}</text>')
        parts.append(_pill(x + 34 + 84, mid + 20, human, 168))
    for (kind, title, sub), y in zip(STAGES, ys):
        parts.append(_icon(kind, x, y))
        parts.append(f'<text x="{x + 66}" y="{y - 2}" font-size="18" font-weight="600" fill="{NAVY}" {FONT}>{title}</text>')
        parts.append(f'<text x="{x + 66}" y="{y + 20}" font-size="15" fill="{MUTED}" {FONT}>{sub}</text>')
    return (f'<svg class="flow-tall" viewBox="0 0 360 680" width="100%" role="img" '
            f'aria-label="Requirements, then test cases, then an automation project, then passing tests.">{"".join(parts)}</svg>')


FLOW_SVG = f"<div>{wide()}{tall()}</div>"
