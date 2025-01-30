import asyncio
from datetime import datetime

async def async_sleep(num):
    print(f"Sleeping {num} seconds.")
    await asyncio.sleep(num)
    print(f"Awake after sleeping for {num} seconds")


async def main():
    start = datetime.now()

    coro_objs = []
    for i in range(1, 4):
        coro_objs.append(async_sleep(i))
    
    await asyncio.gather(*coro_objs)
    
    duration = datetime.now() - start
    print(f"Took {duration.total_seconds():.2f} seconds.")


if __name__=="__main__":
    asyncio.run(main())