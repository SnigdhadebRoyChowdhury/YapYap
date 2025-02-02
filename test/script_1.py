import asyncio
import time

async def fetch_data(id, delay):
    print("Fetching data...id:", id)
    await asyncio.sleep(delay)
    print("Data fetched...id:", id)
    return {"data": "some data", "id": id}


async def main():
    print("Start of main coroutine...")
    
    # Create tasks for running coroutines concurrently
    task1 = asyncio.create_task(fetch_data(1,2))
    task2 = asyncio.create_task(fetch_data(2,2))
    task3 = asyncio.create_task(fetch_data(3,2))

    result1 = await task1 
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)

if __name__=="__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time-start_time)