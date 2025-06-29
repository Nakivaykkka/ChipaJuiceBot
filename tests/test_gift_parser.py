import pytest
from parsers.parser_gift import get_gift_offers_parser

@pytest.mark.asyncio
async def test_get_gift_offers_parser():
    
    offers = await get_gift_offers_parser("berrybox", top=3)
    assert isinstance(offers, list)
    assert offers
