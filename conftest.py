# conftest.py
import os
import re
import base64
from datetime import datetime
from pathlib import Path

import pytest
import pytest_html
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page

# ---------------------------------------------------------
# PLUGIN CONFIG
# ---------------------------------------------------------
pytest_plugins = [
    "tests.steps.steps_common",
]

# ---------------------------------------------------------
# CLI OPTIONS
# ---------------------------------------------------------
def pytest_addoption(parser):
    """Register command line options"""
    # Renamed to --browsertype to avoid conflict with pytest-playwright plugin
    parser.addoption(
        "--browsertype", 
        action="store", 
        default="chromium", 
        help="Browser to run tests on: chromium, firefox, webkit"
    )

# ---------------------------------------------------------
# UI FIXTURES
# ---------------------------------------------------------
@pytest.fixture(scope="session")
def base_url():
    return "https://stratpoint.com/"

@pytest.fixture(scope="session")
def browser(request):
    """
    Launches the browser instance based on CLI option.
    Scope is session to avoid restarting browser for every test.
    """
    # Skip browser launch for API tests
    if request.node.get_closest_marker("api"):
        yield None
        return

    # Get the browser name from CLI (Updated to use browsertype)
    browser_arg = request.config.getoption("--browsertype")
    
    # Map common aliases to Playwright engines
    # Playwright engines: chromium, firefox, webkit
    browser_map = {
        "chrome": "chromium",
        "edge": "chromium", 
        "chromium": "chromium",
        "firefox": "firefox",
        "webkit": "webkit",
        "safari": "webkit"
    }
    
    browser_name = browser_map.get(browser_arg.lower(), "chromium")

    with sync_playwright() as playwright:
        if not hasattr(playwright, browser_name):
             raise ValueError(f"Browser '{browser_name}' is not supported by Playwright.")

        browser_type = getattr(playwright, browser_name)
        
        # Launch options
        launch_options = {
            "headless": False,
            "slow_mo": 1000, 
        }
        
        # If specifically asking for chrome/edge channel
        if browser_arg.lower() == "chrome":
            launch_options["channel"] = "chrome"
        elif browser_arg.lower() == "edge":
            launch_options["channel"] = "msedge"

        browser = browser_type.launch(**launch_options)
        
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page(browser, request):
    """Creates a new page context for each test function"""
    if browser is None:
        yield None
        return

    # Create directories for artifacts
    screenshots_dir = Path("reports/screenshots")
    traces_dir = Path("reports/traces")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    traces_dir.mkdir(parents=True, exist_ok=True)

    # Start context with tracing
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    yield page

    # Post-test cleanup and artifact generation
    scenario = getattr(request.node.obj, "__scenario__", None)
    scenario_name = scenario.name if scenario else request.node.name
    
    safe = lambda s: re.sub(r"[^a-zA-Z0-9_-]+", "_", s)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # If test failed, save the trace zip
    if request.node.rep_call.failed:
        trace_path = traces_dir / f"{safe(scenario_name)}__{timestamp}.zip"
        context.tracing.stop(path=str(trace_path))
    else:
        context.tracing.stop()

    page.close()
    context.close()

# ---------------------------------------------------------
# PAGE OBJECT FIXTURES
# ---------------------------------------------------------
from main.pages.page_home import HomePage
from main.pages.page_services import ServicesPage
from main.pages.page_portfolio import PortfolioPage
from main.pages.page_partners import PartnersPage
from main.pages.page_solutions import SolutionsPage
from main.pages.page_insights import InsightsPage
from main.pages.page_careers import CareersPage
from main.pages.page_about import AboutPage
from main.pages.page_contact_us import ContactUsPage

@pytest.fixture
def home_page(page): return HomePage(page)
@pytest.fixture
def services_page(page): return ServicesPage(page)
@pytest.fixture
def portfolio_page(page): return PortfolioPage(page)
@pytest.fixture
def partners_page(page): return PartnersPage(page)
@pytest.fixture
def solutions_page(page): return SolutionsPage(page)
@pytest.fixture
def insights_page(page): return InsightsPage(page)
@pytest.fixture
def careers_page(page): return CareersPage(page)
@pytest.fixture
def about_page(page): return AboutPage(page)
@pytest.fixture
def contact_us_page(page): return ContactUsPage(page)

# ---------------------------------------------------------
# REPORTING & UTILS
# ---------------------------------------------------------

def get_feature_steps(item):
    """Extract feature file steps and data tables for BDD tests HTML report"""
    try:
        if hasattr(item, 'obj') and hasattr(item.obj, '__scenario__'):
            scenario = item.obj.__scenario__
            feature = scenario.feature

            feature_html = f'''
            <div style="background-color:#f8f9fa; padding:15px; border-radius:5px; margin:10px 0; border-left:4px solid #0d6efd;">
                <h4 style="margin:0 0 10px 0; color:#0d6efd;">📋 Feature: {feature.name}</h4>
                <p style="margin:5px 0; color:#6c757d; font-style:italic;">{feature.description or ''}</p>
                <h5 style="margin:15px 0 10px 0; color:#198754;">🎯 Scenario: {scenario.name}</h5>
                <ol style="margin:10px 0; padding-left:20px;">
            '''

            for step in scenario.steps:
                step_color = {
                    'given': '#6f42c1',
                    'when': '#fd7e14',
                    'then': '#20c997'
                }.get(step.keyword.lower().strip(), '#212529')

                feature_html += f'<li style="margin:5px 0;"><strong style="color:{step_color};">{step.keyword}</strong> {step.name}'

                if hasattr(step, 'datatable') and step.datatable:
                    try:
                        if hasattr(step.datatable, 'rows') and step.datatable.rows:
                            feature_html += '''
                            <table style="margin:10px 0 10px 20px; border-collapse:collapse; font-size:0.9em; width:90%; background-color:#fff; box-shadow:0 1px 3px rgba(0,0,0,0.1);">
                                <thead style="background-color:#e9ecef;"><tr>
                            '''
                            header_row = step.datatable.rows[0]
                            for cell in header_row.cells:
                                feature_html += f'<th style="border:1px solid #dee2e6; padding:8px; text-align:left; font-weight:600; color:#212529;">{cell.value}</th>'
                            feature_html += '</tr></thead><tbody>'
                            for row in step.datatable.rows[1:]:
                                feature_html += '<tr style="background-color:#fff;">'
                                for cell in row.cells:
                                    feature_html += f'<td style="border:1px solid #dee2e6; padding:8px; color:#495057;">{cell.value}</td>'
                                feature_html += '</tr>'
                            feature_html += '</tbody></table>'
                    except Exception:
                        pass
                feature_html += '</li>'
            feature_html += '</ol></div>'
            return feature_html
    except Exception:
        return None
    return None

def resolve_page(item):
    """Helper to find the Playwright Page object in fixtures"""
    funcargs = item.funcargs
    if "page" in funcargs and isinstance(funcargs["page"], Page):
        return funcargs["page"]

    # Search in fixtures for Page objects
    for fixture_value in funcargs.values():
        if isinstance(fixture_value, Page):
            return fixture_value
        if hasattr(fixture_value, "page") and isinstance(fixture_value.page, Page):
            return fixture_value.page

    request = funcargs.get("request")
    if request:
        for candidate in ["page", "home_page"]:
            try:
                fixture_instance = request.getfixturevalue(candidate)
                if isinstance(fixture_instance, Page): return fixture_instance
                if hasattr(fixture_instance, "page") and isinstance(fixture_instance.page, Page):
                    return fixture_instance.page
            except Exception:
                pass
    return None

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    """Hook to capture screenshots on test failure/completion"""
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

    if report.when != "call":
        return

    page = resolve_page(item)
    if not page:
        return

    screenshots_dir = Path("reports/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
  
    scenario = getattr(item.obj, "__scenario__", None)
    feature_name = scenario.feature.name if scenario else "N/A"
    scenario_name = scenario.name if scenario else item.name

    safe = lambda s: re.sub(r"[^a-zA-Z0-9_-]+", "_", s)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    screenshot_path = (
        screenshots_dir
        / f"{safe(feature_name)}__{safe(scenario_name)}__{timestamp}.png"
    )
    
    try:
        page.screenshot(path=str(screenshot_path))
    except Exception:
        print("Failed to capture screenshot: Page might be closed")
        return

    extras = getattr(report, "extras", [])

    feature_html = get_feature_steps(item)
    if feature_html:
        extras.append(pytest_html.extras.html(feature_html))
    
    print(f"\n📄 SS Path: {screenshot_path}\n")

    if screenshot_path.exists():
        with open(screenshot_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()

        # UPDATED: Use the new browsertype option key
        browser_opt = item.config.getoption("--browsertype")
        browser_name = browser_opt if browser_opt else "chromium"
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        extras.append(
            pytest_html.extras.html(
                f"""
                <details style="margin-top:12px;">
                    <summary style="cursor:pointer; font-weight:600;">
                        📸 Screenshot
                        <span style="color:#6c757d; font-size:0.9em;">
                            ({browser_name} · {time_str})
                        </span>
                    </summary>
                    <div style="margin-top:10px;">
                        <img src="data:image/png;base64,{b64}"
                             style="max-width:900px; border:1px solid #ccc; border-radius:4px;" />
                    </div>
                </details>
                """
            )
        )

    report.extras = extras

def pytest_sessionfinish(session, exitstatus):
    report = os.path.abspath("report.html")
    if os.path.exists(report):
        print(f"\n📄 HTML report generated: file://{report}\n")