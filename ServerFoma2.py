import socket
from datetime import datetime
import threading
import time

HOST = '127.0.0.1'
PORT = 65432
semaphore = threading.Semaphore(5)  


def lidar_com_cliente(conn, addr):
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break

            msg = data.decode().strip().lower()

            if msg == "entrar":
                if (threading.active_count() - 2 >= 5):
                    resposta = "negado"
                    conn.sendall(resposta.encode())
                    break
                else:
                    print(f"[ENTROU] {addr} | Pessoas na sala: {threading.active_count() - 1}")
                    resposta = "permitido"
                    conn.sendall(resposta.encode())
                        
                    while True:
                        data = conn.recv(1024)
                        break
                    print(f"[SAIU] {addr} | Pessoas restantes: {threading.active_count() - 2}")


def iniciar_servidor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT))
        S.listen()
        print(f"Servidor ouvindo em {HOST}:{PORT}")

        while True:
            conn, addr = S.accept()
            thread = threading.Thread(target=lidar_com_cliente, args=(conn, addr))
            thread.start()


if __name__ == "__main__":
    iniciar_servidor()
