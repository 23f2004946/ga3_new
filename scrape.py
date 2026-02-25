from playwright.sync_api import sync_playwright
import re

urls = [

"https://sanand0.github.io/tdsdata/seed39.html",
"https://sanand0.github.io/tdsdata/seed40.html",
"https://sanand0.github.io/tdsdata/seed41.html",
"https://sanand0.github.io/tdsdata/seed42.html",
"https://sanand0.github.io/tdsdata/seed43.html",
"https://sanand0.github.io/tdsdata/seed44.html",
"https://sanand0.github.io/tdsdata/seed45.html",
"https://sanand0.github.io/tdsdata/seed46.html",
"https://sanand0.github.io/tdsdata/seed47.html",
"https://sanand0.github.io/tdsdata/seed48.html",

]


def scrape():

    total = 0

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        for url in urls:

            print("Visiting:", url)

            page.goto(url)

            # wait JS execution
            page.wait_for_load_state("networkidle")

            page.wait_for_timeout(4000)

            # get whole page text
            text = page.inner_text("body")

            # extract numbers
            numbers = re.findall(r"\d+(?:\.\d+)?", text)

            for num in numbers:

                total += float(num)

        browser.close()

    print("========== FINAL ANSWER ==========")
    print(f"TOTAL_SUM={int(total)}")
    print("=================================="))


if __name__ == "__main__":
    scrape()
