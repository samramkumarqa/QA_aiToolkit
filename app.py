"""QA AI Toolkit: one page that links the three AI tools for QA, in the order they are used."""

import streamlit as st

from flow import FLOW_SVG

TOOLS = [
    {
        "num": "01",
        "name": "AI Test Case Generator",
        "input": "BRD (PDF, Word, web page), photos or screenshots of it, or a meeting recording",
        "output": "Approved test cases in Excel, with a traceability matrix",
        "button": "Open the Test Case Generator",
        "url": "https://apptestcasegenerator.streamlit.app/",
    },
    {
        "num": "02",
        "name": "AI Automation Code Generator",
        "input": "The approved Excel and the live application",
        "output": "A Page Object Model project in Playwright (JavaScript) or Selenium (Java + TestNG)",
        "button": "Open the Automation Code Generator",
        "url": "https://appautomationcodegenerator.streamlit.app/",
    },
    {
        "num": "03",
        "name": "Playwright Test Fixer (MCP)",
        "input": "A failing Playwright test, inside IntelliJ",
        "output": "The cause and a one-line fix, applied after approval",
        "button": "Set it up from GitHub",
        "url": "https://github.com/samramkumarqa/QA_playwrightMCP",
    },
]

st.set_page_config(page_title="QA AI Toolkit", page_icon="🧰", layout="wide")

st.markdown(
    """
    <style>
    .eyebrow {font-family: "JetBrains Mono", monospace; font-size: 0.8rem; letter-spacing: .18em;
              text-transform: uppercase; color: #0b6e70; margin-bottom: -0.5rem;}
    .flow-wide {display: block; margin: .5rem 0 1.5rem;}
    .flow-tall {display: none; margin: .5rem auto 1.5rem; max-width: 380px;}
    @media (max-width: 720px) { .flow-wide {display: none;} .flow-tall {display: block;} }
    .num {font-family: "JetBrains Mono", monospace; color: #0b6e70; font-weight: 700;}
    .io {font-size: .95rem; line-height: 1.5;}
    .io b {font-family: "JetBrains Mono", monospace; font-size: .75rem; letter-spacing: .08em; opacity: .7;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="eyebrow">QA AI Toolkit</p>', unsafe_allow_html=True)
st.title("From a requirements document to a green automation suite")
st.markdown(
    "Three AI tools that cover the testing life cycle: writing test cases, scripting automation and fixing "
    "failing tests. The output of each one is the input of the next, and a QA engineer approves every step."
)
st.markdown(FLOW_SVG, unsafe_allow_html=True)

for col, t in zip(st.columns(3, gap="medium"), TOOLS):
    with col, st.container(border=True, height="stretch"):
        st.markdown(f'<span class="num">{t["num"]}</span>', unsafe_allow_html=True)
        st.subheader(t["name"], anchor=False)
        st.markdown(
            f'<div class="io"><b>IN</b>&nbsp; {t["input"]}<br><b>OUT</b>&nbsp; {t["output"]}</div>',
            unsafe_allow_html=True,
        )
        st.link_button(t["button"] + " →", t["url"], type="primary", width="stretch")
