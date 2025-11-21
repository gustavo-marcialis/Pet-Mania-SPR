
from playwright.sync_api import sync_playwright

def verify_pet_shop():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8000/index.html")

        # Wait for fonts to load (approximate)
        page.wait_for_timeout(1000)

        # Screenshot Hero Section
        page.locator(".pt-20").screenshot(path="verification/hero_after.png")

        # Screenshot Products Section
        page.locator("#produtos").screenshot(path="verification/products_after.png")

        browser.close()

if __name__ == "__main__":
    verify_pet_shop()
