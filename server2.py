import asyncio
from websockets.asyncio.server import serve


async def echo(websocket):
    message = await websocket.recv()
    print(f"CLient: {message}")

    reply = input("Server:")
    await websocket.send(reply)


async def main():
    async with serve(echo, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())