from pathlib import Path

from streamlit.testing.v1 import AppTest

APP = str(Path(__file__).resolve().parent.parent / "app.py")


def test_three_tools_link_to_their_apps():
    at = AppTest.from_file(APP).run()
    assert not at.exception
    assert at.title[0].value == "From a requirements document to a green automation suite"
    assert [s.value for s in at.subheader] == [
        "AI Test Case Generator", "AI Automation Code Generator", "Playwright Test Fixer (MCP)"]
    assert [b.proto.url for b in at.get("link_button")] == [
        "https://apptestcasegenerator.streamlit.app/",
        "https://appautomationcodegenerator.streamlit.app/",
        "https://github.com/samramkumarqa/QA_playwrightMCP",
    ]
