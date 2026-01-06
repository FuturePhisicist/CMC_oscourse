import socket
import threading
import sys

# ===== CONFIG =====
IP = "192.168.123.2"
PORT = 80
# ==================

def recv_loop(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("\n[Connection closed by remote host]")
                break
            print(f"\nReceived: {data.decode(errors='replace')}")
            print("> ", end="", flush=True)
    except:
        pass

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(f"Connecting to {IP}:{PORT} ...")
    sock.connect((IP, PORT))
    print("Connected. Ctrl+C to exit.\n")

    # Start receiver thread
    threading.Thread(target=recv_loop, args=(sock,), daemon=True).start()

    try:
        while True:
            msg = input("> ")
            if not msg:
                continue
            sock.sendall(msg.encode())
            print(f"Sent: {msg}")

    except KeyboardInterrupt:
        print("\nCtrl+C pressed. Closing...")

    finally:
        try:
            sock.shutdown(socket.SHUT_RDWR)
        except:
            pass
        sock.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()

