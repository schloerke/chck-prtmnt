from playwright.sync_api import Page, expect


def test_output_ui_kitchen(page: Page) -> None:
    page.goto(
        "https://www.addisonatswiftcreek.com/floorplans/wellesley-with-fenced-in-yard"
    )

    try:
        expect(page.locator("#challenge-running")).to_have_count(0)
    except AssertionError:
        try:
            page.frame_locator("iframe").locator(".mark").click(timeout=10000)
        except TimeoutError:
            page.screenshot(path="shivon.png")

    expect(page.locator("#challenge-running")).to_have_count(0)

    avail_container = page.locator("#available-units-container")
    expect(avail_container).to_have_count(1)

    try:
        expect(avail_container.locator("#no-matches-container")).to_have_count(0)
    except AssertionError:
        print("No matches found")
        page.screenshot(path="shivon-pass.png")
        return

    raise RuntimeError("Match found! Send text message!")
