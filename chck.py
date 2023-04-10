from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(
        "https://www.addisonatswiftcreek.com/floorplans/wellesley-with-fenced-in-yard"
    )

    try:
        expect(page.locator("#challenge-running")).to_have_count(
            0,
            timeout=2000,
        )
    except AssertionError:
        try:
            page.frame_locator("iframe").locator(".mark").click(timeout=10000)
        except TimeoutError as e:
            page.screenshot(path="debug-init.png")
            raise e

    expect(page.locator("#challenge-running")).to_have_count(0, timeout=2000)

    avail_container = page.locator("#available-units-container")
    expect(avail_container).to_have_count(1, timeout=1000)

    try:
        expect(avail_container.locator("#no-matches-container")).to_have_count(
            0, timeout=1000
        )
        page.screenshot(path="debug-match.png")
        raise RuntimeError("Match found! Send text message!")
    except AssertionError:
        print("No matches found")
        page.screenshot(path="debug-no-match.png")
