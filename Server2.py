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
                if not semaphore.acquire(blocking=False):
                    resposta = "negado"
                    conn.sendall(resposta.encode())
                    break
                else:
                    try:
                        print(f"[ENTROU] {addr} | Pessoas na sala: {5 - semaphore._value}")
                        resposta = "permitido"
                        conn.sendall(resposta.encode())

                        data = conn.recv(1024) 
                        print(f"[SAIU] {addr} | Pessoas restantes: {5 - (semaphore._value + 1)}")
                    finally:
                        semaphore.release()
                        break


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
