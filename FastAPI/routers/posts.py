'''

Fetch data from public API (weather, currency, posts)

Cache result for 10 seconds

Use async + httpx
'''

from fastapi import APIRouter, Depends, HTTPException, status
import httpx
from datetime import datetime

router = APIRouter()

cached_posts = {}

url = "https://jsonplaceholder.typicode.com/posts"

@router.get("/posts")
async def get_posts():
    if cached_posts:
        time = cached_posts["cached"]["time"]
        delta = datetime.now()-time
        delta = delta.total_seconds()
        if delta<10:
            return cached_posts["cached"]["data"]
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()
            cached_posts["cached"] = {"data":response.json(),
                                      "time":datetime.now()
                                    }
            print(cached_posts)
            return response.json()
        except httpx.HTTPStatusError as ex:
            raise HTTPException(status_code=ex.response.status_code)
        except httpx.RequestError as ex:
            raise HTTPException(status_code=500)