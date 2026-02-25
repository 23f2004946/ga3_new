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

        browser = p.chromium.launch()

        page = browser.new_page()

        for url in urls:

            print("Visiting:", url)

            page.goto(url)

            page.wait_for_load_state("networkidle")

            cells = page.locator("table td")

            count = cells.count()

            for i in range(count):

                text = cells.nth(i).inner_text().strip()

                try:
                    total += float(text)
                except:
                    pass

        browser.close()

    # ⭐ IMPORTANT PRINT FORMAT
    print(f"TOTAL_SUM={int(total)}")


if __name__ == "__main__":
    scrape()
