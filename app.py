"""QA AI Toolkit: one page that links the three AI tools for QA, in the order they are used."""

import streamlit as st

TOOLS = [
    {
        "num": "01",
        "name": "AI Test Case Generator",
        "input": "BRD (PDF, Word, web page), photos or screenshots of it, or a meeting recording",
        "output": "Approved test cases in Excel, with a traceability matrix",
        "about": "Lists every requirement with its own ID and source sentence, then writes positive, "
                 "negative and boundary test cases for each.",
        "human": "You approve each test case",
        "button": "Open the Test Case Generator",
        "url": "https://apptestcasegenerator.streamlit.app/",
        "code": "https://github.com/samramkumarqa/GenerativeAI",
    },
    {
        "num": "02",
        "name": "AI Automation Code Generator",
        "input": "The approved Excel and the live application",
        "output": "A Page Object Model project in Playwright (JavaScript) or Selenium (Java + TestNG)",
        "about": "Explores the app in a real browser, records a unique locator for every element and maps "
                 "each manual step to a real element. Steps it can't map are skipped and flagged.",
        "human": "You review the code",
        "button": "Open the Automation Code Generator",
        "url": "https://appautomationcodegenerator.streamlit.app/",
        "code": "https://github.com/samramkumarqa/QA_generateAutomationcodes",
    },
    {
        "num": "03",
        "name": "Playwright Test Fixer (MCP)",
        "input": "A failing Playwright test, inside IntelliJ",
        "output": "The cause and a one-line fix, applied after approval",
        "about": "An MCP server that gives the AI assistant in your IDE safe tools: run tests, read the error, "
                 "inspect the live page, propose a fix and apply it with a backup. It runs in the IDE, "
                 "so it is set up from GitHub.",
        "human": "You approve every change",
        "button": "Set it up from GitHub",
        "url": "https://github.com/samramkumarqa/QA_playwrightMCP",
        "code": "https://github.com/samramkumarqa/QA_playwrightMCP",
    },
]

FLOW = ["BRD · recording · images", "test_cases.xlsx", "pom-project.zip", "tests passing"]

st.set_page_config(page_title="QA AI Toolkit", page_icon="🧰", layout="wide")

st.markdown(
    """
    <style>
    .eyebrow {font-family: "JetBrains Mono", monospace; font-size: 0.8rem; letter-spacing: .18em;
              text-transform: uppercase; color: #0b6e70; margin-bottom: -0.5rem;}
    .flow {display: flex; flex-wrap: wrap; align-items: center; gap: .5rem; margin: .5rem 0 1rem;}
    .flow code {font-size: .85rem;}
    .flow .arrow {color: #0b6e70; font-weight: 700;}
    .num {font-family: "JetBrains Mono", monospace; color: #0b6e70; font-weight: 700;}
    .human {display: inline-block; background: #fce3cf; color: #7a3410; border-radius: 999px;
            padding: .15rem .75rem; font-size: .85rem; margin: .25rem 0 .5rem;}
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
st.markdown(
    '<div class="flow">'
    + ' <span class="arrow">→</span> '.join(f"<code>{x}</code>" for x in FLOW)
    + "</div>",
    unsafe_allow_html=True,
)

for col, t in zip(st.columns(3, gap="medium"), TOOLS):
    with col, st.container(border=True, height="stretch"):
        st.markdown(f'<span class="num">{t["num"]}</span>', unsafe_allow_html=True)
        st.subheader(t["name"], anchor=False)
        st.markdown(
            f'<div class="io"><b>IN</b>&nbsp; {t["input"]}<br><b>OUT</b>&nbsp; {t["output"]}</div>',
            unsafe_allow_html=True,
        )
        st.caption(t["about"])
        st.markdown(f'<span class="human">{t["human"]}</span>', unsafe_allow_html=True)
        st.link_button(t["button"] + " →", t["url"], type="primary", width="stretch")
        st.markdown(f"[Source code]({t['code']})")

st.divider()
a, b, c = st.columns(3)
a.info("**First open can be slow.** The apps sleep when nobody uses them. If you see *Wake up this app*, "
       "click it and wait about 30 seconds.", icon="⏱️")
b.info("**Try it with the samples.** Each app has a sample built in: a fictional grocery-checkout BRD, "
       "and the public Swag Labs practice shop.", icon="🧪")
c.warning("**Public demos.** Use sample or public documents only. Don't upload confidential requirements, "
          "customer data or passwords.", icon="🔒")

st.caption("Built by Ramkumar · Python · Groq · Playwright · Selenium · MCP · Streamlit")
