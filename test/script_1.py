import asyncio

async def fetch_data(delay, id):
    print("Fetching data...id:", id)
    await asyncio.sleep(delay)
    print("Data fetched...id:", id)
    return {"data": "some data", "id": id}


async def main():
    print("Start of main coroutine...")
    
    task1 = fetch_data(4,1)
    task2 = fetch_data(2,2)

    result1 = await task1 
    print(f"Result received: {result1}")

    result2 = await task2
    print(f"Result received: {result2}")

if __name__=="__main__":
    asyncio.run(main())