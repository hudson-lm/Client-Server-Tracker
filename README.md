# Client-Server-Tracker
This project implements a client for a TCP-based tracker server. It supports ADD, LIST, REMOVE, and MARK commands to manage tasks with unique IDs and statuses. The client formats requests, handles multi-line input, and processes server responses.

## How to Run

### Prerequisites
*   Ensure both `TrackerClient.py` and `TrackerServer.py` are in your VS Code workspace.
*   Python 3 must be installed.

### 1. Start the Server
*   Open `TrackerServer.py` and click the **"Run" (play)** button in the top right.
*   Alternatively, open a terminal and run:
    ```bash
    python3 TrackerServer.py
    ```
*   You should see the message: `"Server listening on port 18222..."`

### 2. Start the Client
*   **Open a New Terminal** (this is essential to keep the server running in the background).
*   In the new terminal, run the client by opening `TrackerClient.py` and clicking the **"Run"** button, or by typing:
    ```bash
    python3 TrackerClient.py
    ```
*   Upon a successful connection, you will see: `"Connected to Tracker Server"`

### 3. Use the Application
You can now execute commands (`ADD`, `LIST`, `REMOVE`, `MARK`, `QUIT`) from the client terminal to interact with the server.

Use the Application: You can now execute commands (ADD, LIST, REMOVE, MARK, QUIT) from the client terminal to interact with the server.
