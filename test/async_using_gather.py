import asyncio
import time

async def fetch_data(id, delay):
    print("Fetching data...id:", id)
    await asyncio.sleep(delay)
    print("Data fetched...id:", id)
    return {"data": "some data", "id": id}


async def main():
    print("Start of main coroutine...")
    
    task1 = fetch_data(1,2)
    task2 = fetch_data(2,2)
    task3 = fetch_data(3,2)

    results = await asyncio.gather(task1,task2, task3)

    print(results)

if __name__=="__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time-start_time)