import asyncio
import time

async def fetch_data(id, delay):
    print("Fetching data...id:", id)
    await asyncio.sleep(delay)
    print("Data fetched...id:", id)
    return {"data": "some data", "id": id}


async def main():
    print("Start of main coroutine...")
    
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2,2,2], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # result = [task.result() for task in tasks]
    # print(result)

if __name__=="__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    print(end_time-start_time)