import asyncio
import websockets

async def chat_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Send user input to the server
        async def send_messages():
            while True:
                message = input("Client: ")
                await websocket.send(message)

        # Receive messages from the server
        async def receive_messages():
            async for message in websocket:
                print(f"\nServer: {message}")

        # Run both send and receive tasks concurrently
        await asyncio.gather(send_messages(), receive_messages())


if __name__=="__main__":
    asyncio.run(chat_client())