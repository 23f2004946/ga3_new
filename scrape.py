from playwright.sync_api import sync_playwright

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

            # ⭐ WAIT FOR TABLE TO LOAD
            page.wait_for_selector("table")

            # Extra wait for JS rendering
            page.wait_for_timeout(3000)

            # Get ALL table cell texts
            cells = page.locator("table td").all_inner_texts()

            for text in cells:

                try:
                    total += float(text.strip())
                except:
                    pass

        browser.close()

    # ⭐ REQUIRED FORMAT
    print(f"TOTAL_SUM={int(total)}")


if __name__ == "__main__":
    scrape()
