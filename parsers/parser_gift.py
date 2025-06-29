import aiohttp
from bs4 import BeautifulSoup
from typing import List, Dict
import re

async def get_gift_offers_parser(slug: str, top: int = 5) -> List[Dict]:
    url = f"https://fragment.com/gifts/{slug}?filter=sale"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers={"User-Agent": "Mozilla/5.0"}) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    offers = []
    for item in soup.select("div.tm-grid-item-content"):
        price_tag = item.select_one("div.tm-grid-item-value")
        price_text = price_tag.text.strip() if price_tag else None

        price_text = price_tag.text.strip() if price_tag else None
        if price_text:
            cleaned = price_text.replace(" ", "").replace(",", "")
            price_match = re.search(r"\d+(\.\d+)?", cleaned)
            if price_match:
                price = float(price_match.group(0))

        parent_a = item.find_parent("a")
        url = "https://fragment.com" + parent_a['href'] if parent_a else None
        
        if price and url:
            offers.append({"price": price, "url": url})

    offers.sort(key=lambda x: x['price'])
    return offers[:top]
