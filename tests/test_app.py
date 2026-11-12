import re
from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def test_three_tools_link_to_their_apps():
    at = AppTest.from_file(APP).run()
    assert not at.exception
    assert at.title[0].value == "From a requirements document to a green automation suite"
    html = " ".join(m.value for m in at.markdown)
    assert re.findall(r'class="tool-name">([^<]+)<', html) == [
        "AI Test Case Generator", "AI Automation Code Generator", "Playwright Test Fixer (MCP)"]
    assert re.findall(r'class="tool-btn" href="([^"]+)"', html) == [
        "https://apptestcasegenerator.streamlit.app/",
        "https://appautomationcodegenerator.streamlit.app/",
        "https://github.com/samramkumarqa/QA_playwrightMCP",
    ]
    assert html.count('src="data:image/webp;base64,') == 3
