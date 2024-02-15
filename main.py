from playwright.sync_api import sync_playwright # for browser automation
import argparse
from download import downloadVideo


def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(search_for, timeout=60000)
        page.wait_for_timeout(5000)

        videoXpath = "//div[@id='contents']/ytd-playlist-video-list-renderer/div[@id='contents']/ytd-playlist-video-renderer"
        contents = page.locator(videoXpath).all()
        for item in contents[:total]:
            item.locator("//div[@id='content']").hover()
            item.locator("//button[@id='button']").click()
            options = page.locator("//tp-yt-paper-listbox[@id='items']/ytd-menu-service-item-renderer").all()
            options[-1].click()
            page.wait_for_timeout(1000)
            popup = page.locator("//tp-yt-paper-dialog")
            url = popup.locator("//input[@id='share-url']").input_value()
            popup.locator("//button[@id='button'][@aria-label='Cancel']").click()
            downloadVideo(url)
            page.wait_for_timeout(2000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str , required=True)
    parser.add_argument('-t', '--total', type=int, required=False)
    args = parser.parse_args()
    if args.url:
        search_for = args.url; 
    if args.total:
        total = args.total
    main()