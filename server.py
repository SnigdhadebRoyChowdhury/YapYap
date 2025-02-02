import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    async for message in websocket:
        print(f"Client: {message}")
        response = input("Server: ")
        await websocket.send(response)


async def main():
    async with serve(echo, "localhost", 8765, close_timeout=120) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())