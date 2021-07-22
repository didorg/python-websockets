import websockets
import asyncio

# Server data
PORT = 7890
print("Server listening on Port " + str(PORT))
# A set of connected ws clients
connected = set()


async def echo(ws, path):
    print("A client just connected")
    # Store a copy of the connected client
    connected.add(ws)
    # Handle incoming messages
    try:
        async for msg in ws:
            print("Received message from client: " + msg)
            # Send a response to all connected clients except sender
            for conn in connected:
                if conn != ws:
                    await conn.send("Someone said: " + msg)
    # Handle disconnecting clients 
    except websockets.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(ws)


# Start the server
start_server = websockets.serve(echo, "localhost", PORT)

# Start the connection
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()