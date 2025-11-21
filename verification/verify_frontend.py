
from playwright.sync_api import Page, expect, sync_playwright
import os
import re

def verify_hero_layout(page: Page):
    # 1. Arrange: Go to the local homepage.
    page.goto("http://localhost:8080")

    # 2. Act & Assert:
    # Check for Hero Section text (should be visible)
    disk_racao = page.get_by_text("Disk Ração")
    expect(disk_racao).to_be_visible()

    # Check styling indirectly via screenshot or inspecting computed styles if needed
    # But for this task, we rely on screenshot primarily.

    # 3. Screenshot: Capture the full page
    # Ensure directory exists
    os.makedirs("/home/jules/verification", exist_ok=True)
    page.screenshot(path="/home/jules/verification/hero_update_verification.png", full_page=True)
    print("Screenshot saved to /home/jules/verification/hero_update_verification.png")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})
        try:
            verify_hero_layout(page)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            browser.close()
