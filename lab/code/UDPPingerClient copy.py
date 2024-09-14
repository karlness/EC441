import sys
import time
from socket import *

# Server address and port number is passed as arguments
server_address = sys.argv[1]
server_port = int(sys.argv[2])
client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.settimeout(1)  # Timeout of 1 second

# Statistics variables
packets_sent = 0
packets_received = 0
rtt_list = []

for sequence_number in range(1, 11):  # 10 pings
    send_time = time.time()
    message = f"Ping {sequence_number} {send_time}"
    client_socket.sendto(message.encode(), (server_address, server_port))
    packets_sent += 1
    
    try:
        response, _ = client_socket.recvfrom(1024)
        received_time = time.time()
        rtt = received_time - send_time
        rtt_list.append(rtt)
        packets_received += 1
        print(f"{response.decode()} RTT: {rtt:.6f} seconds")
    except timeout:
        print("Request timed out.")

# Close socket
client_socket.close()

# Print statistics
if rtt_list:
    print(f"Minimum RTT: {min(rtt_list):.6f}")
    print(f"Maximum RTT: {max(rtt_list):.6f}")
    print(f"Average RTT: {sum(rtt_list)/len(rtt_list):.6f}")
print(f"Packets Sent: {packets_sent}")
print(f"Packets Received: {packets_received}")
print(f"Packet Loss Percentage: {((packets_sent - packets_received) / packets_sent) * 100:.2f}%")


