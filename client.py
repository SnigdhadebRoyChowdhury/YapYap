import asyncio
from websockets.asyncio.client import connect


async def hello():
    async with connect("ws://localhost:8765") as websocket:
        while True:
            msg = input("Client: ")
            if msg == "exit":
                await websocket.close()
                break
            else:
                final_msg = f"{msg}"
                await websocket.send(final_msg)
                message = await websocket.recv()
                print(f"Server: {message}")


if __name__ == "__main__":
    asyncio.run(hello())