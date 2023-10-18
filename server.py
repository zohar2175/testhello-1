import socket
import sqlite3

#שומר את ההודעות שהלקוח שולח
def save_message(client_address, message):
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO messages (client_address, message) VALUES (?, ?)
    ''', (client_address, message))
    conn.commit()
    conn.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #יוצר חיבור לכל כתובות הוייפי על פורמט 12345
    server_socket.bind(('0.0.0.0', 12345))
    #האזנה לחיבורים נכנסים (יש תור של עד 5 אנשים)
    server_socket.listen(5)
    print("Echo server is running and listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")

            # שמירת ההודעה במסד הנתונים
            save_message(str(client_address), message)

            # שליחת ההודעה בחזרה לקליינט (Echo)
            client_socket.sendall(data)

        client_socket.close()
        print(f"Connection from {client_address} closed")

if __name__ == "__main__":
    start_server()
