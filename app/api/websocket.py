from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

router = APIRouter()

# Store active connections
active_connections = {}

@router.websocket("/notifications/{user_id}")
async def websocket_notifications(websocket: WebSocket, user_id: int):
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        while True:
            # Wait for any message from client
            data = await websocket.receive_text()
            # You can process the message here if needed
            await websocket.send_text(f"Message received: {data}")
    except WebSocketDisconnect:
        # Remove connection when client disconnects
        if user_id in active_connections:
            del active_connections[user_id]

# Function to send notifications to specific user
async def send_notification_to_user(user_id: int, message: str):
    if user_id in active_connections:
        await active_connections[user_id].send_text(json.dumps({"message": message}))
