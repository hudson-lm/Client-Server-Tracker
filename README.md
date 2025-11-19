# Client-Server-Tracker
This project implements a client for a TCP-based TODO tracker server. It supports ADD, LIST, REMOVE, and MARK commands to manage tasks with unique IDs and statuses. The client formats requests, handles multi-line input, and processes server responses.
How to Compile and Run the Code
Prerequisites: Ensure both TrackerClient.py and TrackerServer.py are in your VS Code workspace.

Start the Server:

Open TrackerServer.py and click the "Run" (play) button in the top right, or manually open a terminal and run:

bash
python3 TrackerServer.py
You should see the message: "Server listening on port 18222..."

Start the Client:

Open a New Terminal (this is essential to keep the server running in the background).

In the new terminal, run the client by opening TrackerClient.py and clicking the "Run" button, or by typing:

bash
python3 TrackerClient.py
Upon a successful connection, you will see: "Connected to TodoTracker Server"

Use the Application: You can now execute commands (ADD, LIST, REMOVE, MARK, QUIT) from the client terminal to interact with the server.
