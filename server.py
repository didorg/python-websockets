import websockets
import asyncio

PORT = 7890

print("Server listening on Port " + str(PORT))


async def echo(ws, path):
    print("A client just connected")
    try:
        async for message in ws:
            print("Received message from client: " + message)
            await ws.send("Pong: " + message)
    except websockets.ConnectionClosed as e:
        print("A client just disconnected")

# Start the server
start_server = websockets.serve(echo, "localhost", PORT)

# Start the connection
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
