from playwright.sync_api import sync_playwright # for browser automation
import argparse

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(search_for, timeout=60000)
        page.wait_for_timeout(5000)

        contents = page.locator("//div[@class='contents']")



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--link', type=str , required=True)
    args = parser.parse_args()
    if args.link:
        search_for = args.link; 
    main()