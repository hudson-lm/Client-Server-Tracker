# MARCUS Hudson Lois
from socket import *

def read_line(sock):
    line = b''
    while True:
        chunk = sock.recv(1)
        if not chunk:
                raise ConnectionError("Connection closed unexpectedly")
        line += chunk
        if chunk.endswith(b'\n'):
            break
    return line.decode('utf-8').strip()

def read_until_hash(sock):
    lines = []
    while True:
        line = read_line(sock)
        if line == '#': # the one to terminate the command, e.g. the one in "ADD"
            break
        lines.append(line)
    return lines

def send_command(sock, command):
    sock.send((command + '\n').encode('utf-8'))
    
def send_multiline_data(sock, lines):
    for line in lines: 
        sock.send((line + '\n').encode('utf-8'))
    sock.send(b'#\n')
    
def add_task(sock):
    send_command(sock,'ADD') #sending 'ADD' to the server
    
    content_lines = [] # for the multiple lines of "ADD" content 
    while True:
        line = input("client: ")
        if(line == '#'):
            break
        content_lines.append(line) #add every content's line to the 'content_lines' list except '#'
    
    send_multiline_data(sock,content_lines)
    
    server_response = read_line(sock)
    print(f"server: {server_response}") # catch and print server's response
        
def list_tasks(sock):
    send_command(sock,"LIST") #sending 'LIST' to the server
    
    response_lines = read_until_hash(sock)
    for line in response_lines:
        print(f"server: {line}") # will print each line of server's response
        
def mark_tasks(sock):
    send_command(sock,"MARK") #sending 'MARK' to the server
    
    content_ids = [] # to store task id's until "#" is reached
    while True:
        line = input("client: ")
        if(line == '#'):
            break
        content_ids.append(line)
    send_multiline_data(sock,content_ids)
    
    server_response = read_line(sock)
    print(f"server: {server_response}") # catch and print server's response (print OK)
  
def remove_tasks(sock):
    send_command(sock,"REMOVE") # #sending 'REMOVE' to the server
    
    content_ids = []
    while True:
        line = input("client: ")
        if(line == "#"):
            break
        content_ids.append(line)
    send_multiline_data(sock,content_ids)
    
    server_response = read_line(sock)
    print(f"server: {server_response}") #print OK
    
def quit_conn(sock):
    send_command(sock,"QUIT")
    
    server_response = read_line(sock)
    print(f"server: {server_response}") #print OK
    sock.shutdown(SHUT_RDWR) # shutdown the socket
    sock.close() #close the socket
    
def error_handling(sock, command):
    send_command(sock,command)
    
    server_response = read_line(sock) 
    print(f"server: {server_response}") # error handling from server's response --> ERROR - Command not understood
    

def main():
    serverName = '127.0.0.1' # using the IP address of the local host
    serverPort = 18222 # using the port number stated in TrackerServer.py

    clientSocket = socket(AF_INET, SOCK_STREAM) #create socket
    clientSocket.connect((serverName,serverPort)) # connect to the server
    print("Connected to Tracker Server")
    
    while True:
        command = input("client: ").strip().upper() # get command from client
        
        if command == "ADD":
            add_task(clientSocket)
        elif command == "LIST":
            list_tasks(clientSocket)
        elif command == "REMOVE":
            remove_tasks(clientSocket)
        elif command == "MARK": 
            mark_tasks(clientSocket)
        elif command == "QUIT":
            quit_conn(clientSocket)
            break # if i don't put 'break' here, it won't break the while loop, although the socket connection has been stopped 
        else:
            error_handling(clientSocket, command) #error handling if COMMAND is not one of those 4 above
            ''' 
                I was also curious to try make the command like this , e.g.:
                    "MARK 0001"
                    "REMOVE 0001"
                    "ADD Buy Groceries"
                This is an error, because command not understood --> not separated by 'new line', handled on this else statement. So it works the same like the *.exe demo
            '''
            
            
if __name__ == "__main__":
    main() #automatic running right after file execution