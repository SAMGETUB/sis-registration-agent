from playwright.sync_api import sync_playwright
from seat_checker import check_seats

with sync_playwright() as p:
    browser = p.chromium.launch_persistent_context(
        user_data_dir="/Users/samuel/Library/Application Support/Google/Chrome/Default",
        channel="chrome",
        headless=False
    )
    page = browser.pages[0] if browser.pages else browser.new_page()
    page.goto("https://www.uml.edu/NOW")
    page.click("text=Sign In")
    page.wait_for_load_state("networkidle")
    page.click("text= Continue signing in")
    page.wait_for_load_state("networkidle")
    page.goto("https://uml.edu/student-dashboard#class-search/filters")
    page.wait_for_load_state("networkidle")

    # check_seats(page)

    # input("Press Enter to close the browser...")

    try:
        check_seats(page)
    except Exception as e:
        print(f"An error occurred: {e}")    

    input("Press Enter to close the browser...")    