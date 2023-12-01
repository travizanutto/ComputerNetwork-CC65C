import socket


if __name__ == "__main__":
    server_address = ('localhost', 8080)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect(server_address)
            print(f"[INFO] Connected to {server_address[0]}:{server_address[1]}")

            print('Numero de redes e a quantidade de máquinas de cada rede: ')
            buf = input()
            client_socket.sendall(buf.encode())

            data = client_socket.recv(1024)

        except Exception as e:
            print(f"[ERROR] {e}")

        finally:
            client_socket.close()