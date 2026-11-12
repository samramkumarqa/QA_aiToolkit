"""QA AI Toolkit: one page that links the three AI tools for QA, in the order they are used."""

import base64
from pathlib import Path

import streamlit as st

from flow import FLOW_SVG

ASSETS = Path(__file__).parent / "assets"

TOOLS = [
    {
        "num": "01",
        "name": "AI Test Case Generator",
        "image": "test-case-generator.webp",
        "alt": "Review table of generated test cases with 18 approved and 100% coverage",
        "input": "BRD (PDF, Word, web page), photos or screenshots of it, or a meeting recording",
        "output": "Approved test cases in Excel, with a traceability matrix",
        "button": "Open the Test Case Generator",
        "url": "https://apptestcasegenerator.streamlit.app/",
    },
    {
        "num": "02",
        "name": "AI Automation Code Generator",
        "image": "automation-code-generator.webp",
        "alt": "Playwright test report of the generated project: 5 passed, 1 skipped",
        "input": "The approved Excel and the live application",
        "output": "A Page Object Model project in Playwright (JavaScript) or Selenium (Java + TestNG)",
        "button": "Open the Automation Code Generator",
        "url": "https://appautomationcodegenerator.streamlit.app/",
    },
    {
        "num": "03",
        "name": "Playwright Test Fixer (MCP)",
        "image": "test-fixer.webp",
        "alt": "IntelliJ with the AI chat reporting that the fix was applied and the test passes",
        "input": "A failing Playwright test, inside IntelliJ",
        "output": "The cause and a one-line fix, applied after approval",
        "button": "Set it up from GitHub",
        "url": "https://github.com/samramkumarqa/QA_playwrightMCP",
    },
]

CSS = """
<style>
h1 {text-wrap: balance;}
.eyebrow {font-family: "JetBrains Mono", monospace; font-size: 0.8rem; letter-spacing: .18em;
          text-transform: uppercase; color: #0b6e70; margin-bottom: -0.5rem;}
.flow-wide {display: block; margin: .5rem 0 1.75rem;}
.flow-tall {display: none; margin: .5rem auto 1.75rem; max-width: 380px;}
@media (max-width: 720px) { .flow-wide {display: none;} .flow-tall {display: block;} }

.tools {display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; align-items: stretch;}
@media (max-width: 960px) { .tools {grid-template-columns: 1fr;} }
.tool {display: flex; flex-direction: column; background: #fffffe; border: 1px solid #d8ddd6;
       border-radius: 14px; overflow: hidden; min-width: 0;}
.shot {aspect-ratio: 16 / 10; width: 100%; object-fit: cover; object-position: left top; display: block;
       border-bottom: 1px solid #d8ddd6; background: #eef0ec;}
.tool-body {display: flex; flex-direction: column; gap: 12px; padding: 20px 22px 22px; flex: 1;}
.tool-num {font-family: "JetBrains Mono", monospace; color: #0b6e70; font-weight: 700; font-size: .9rem;}
.tool-name {font-size: 1.35rem; font-weight: 700; line-height: 1.25; color: #14213d; margin: 0;
            min-height: 2.5em; display: flex; align-items: flex-start;}
.io {display: grid; grid-template-columns: 3.2em 1fr; row-gap: 8px; font-size: .95rem; line-height: 1.45;
     color: #14213d; margin: 0;}
.io dt {font-family: "JetBrains Mono", monospace; font-size: .72rem; letter-spacing: .08em; color: #4a5668;
        padding-top: .2em;}
.io dd {margin: 0;}
a.tool-btn, a.tool-btn:visited {margin-top: auto; display: block; text-align: center; background: #0b6e70;
       color: #ffffff !important; text-decoration: none; font-weight: 600; padding: 11px 14px; border-radius: 8px;}
a.tool-btn:hover {background: #095a5c;}
a.tool-btn:focus-visible {outline: 3px solid #14213d; outline-offset: 2px;}
.tool:has(a.tool-btn:hover) {border-color: #0b6e70;}
</style>
"""


def _img(name: str) -> str:
    return "data:image/webp;base64," + base64.b64encode((ASSETS / name).read_bytes()).decode()


def card(t: dict) -> str:
    return (
        f'<div class="tool">'
        f'<img class="shot" src="{_img(t["image"])}" alt="{t["alt"]}">'
        f'<div class="tool-body">'
        f'<span class="tool-num">{t["num"]}</span>'
        f'<div class="tool-name">{t["name"]}</div>'
        f'<dl class="io"><dt>IN</dt><dd>{t["input"]}</dd><dt>OUT</dt><dd>{t["output"]}</dd></dl>'
        f'<a class="tool-btn" href="{t["url"]}" target="_blank" rel="noopener">{t["button"]} →</a>'
        f"</div></div>"
    )


st.set_page_config(page_title="QA AI Toolkit", page_icon="🧰", layout="wide")
st.markdown(CSS, unsafe_allow_html=True)

st.markdown('<p class="eyebrow">QA AI Toolkit</p>', unsafe_allow_html=True)
st.title("From a requirements document to a green automation suite", anchor=False)
st.markdown(
    "Three AI tools that cover the testing life cycle: writing test cases, scripting automation and fixing "
    "failing tests. The output of each one is the input of the next, and a QA engineer approves every step."
)
st.markdown(FLOW_SVG, unsafe_allow_html=True)
st.markdown('<div class="tools">' + "".join(card(t) for t in TOOLS) + "</div>", unsafe_allow_html=True)
