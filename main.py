from playwright.sync_api import sync_playwright # for browser automation
import argparse
from download import downloadVideo

def getVideoUrl(item, page):
    #hover upon the video to show up the options button
    item.locator("//div[@id='content']").hover()

    #click on the options button
    item.locator("//button[@id='button']").click()

    #get all the options in option bar
    optionsXpath = "//tp-yt-paper-listbox[@id='items']/ytd-menu-service-item-renderer"
    options = page.locator(optionsXpath).all()

    #click the last option as it is the 'share' option
    options[-1].click()
    page.wait_for_timeout(1000)

    #select the url of video from popup window after clicking share
    popup = page.locator("//tp-yt-paper-dialog")
    url = popup.locator("//input[@id='share-url']").input_value()

    #close the popup window
    closeButton = "//button[@id='button'][@aria-label='Cancel']"
    popup.locator(closeButton).click()
    return url


def main():
    with sync_playwright() as p:
        #open the chromium browser
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        #search for the playlist in the browser
        page.goto(search_for, timeout=60000)
        page.wait_for_timeout(5000)

        #select all the videos in the playlist
        videoXpath = "//div[@id='contents']/ytd-playlist-video-list-renderer/div[@id='contents']/ytd-playlist-video-renderer"
        contents = page.locator(videoXpath).all()

        global total
        global start
        if total < 0:
            total = len(contents)
        print(f"total number of videos to be downloaded : {total - (start-1)}")


        for index,item in enumerate(contents[start-1:total]):
            url = getVideoUrl(item, page)
            #download the video
            downloadVideo(url, index+start)
            page.wait_for_timeout(2000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str , required=True)
    parser.add_argument('-F','-f', '--From', type=int, required=False, default=1)
    parser.add_argument('-t', '--total', type=int, required=False)
    args = parser.parse_args()
    if args.url:
        search_for = args.url; 
    if args.total:
        start = args.From
        total = args.total
    else:
        start = args.From
        total = -1
    main()