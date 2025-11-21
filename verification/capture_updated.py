from playwright.sync_api import sync_playwright

def capture_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # Navigate to local server
        page.goto("http://localhost:8080")

        # Wait for fonts to load
        page.wait_for_timeout(2000)

        # Capture full page
        page.screenshot(path="verification/updated_state.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    capture_page()
