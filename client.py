import websockets
import asyncio


# The main function that will handle connection and communication
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    client_name = "Cln-1"
    try:
        # Connect to the server
        async with websockets.connect(url) as ws:
            # Send a greeting message
            await ws.send("updated")
            # Pong confirmation
            msg = await ws.recv()
            print(f"< {msg}")
            # Stay alive forever, listening to incoming msgs
            # while True:
            #     msg = await ws.recv()
            #     print(msg)
    except Exception as e:
        print(e)

# Start the connection
asyncio.get_event_loop().run_until_complete(listen())
