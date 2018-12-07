import asyncio


async def scroll_page(page):
    cur_dist = 0
    height = await page.evaluate("() => document.body.scrollHeight")
    while True:
        if cur_dist < height:
            await page.evaluate("window.scrollBy(0, 500);")
            await asyncio.sleep(0.1)
            cur_dist += 500
        else:
            break
