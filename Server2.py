import socket
from datetime import datetime
import threading


HOST = '127.0.0.1'
PORT = 65432
semaphore = threading.Semaphore(5)  


def lidar_com_cliente(conn, addr):
    with semaphore:  
        print(f"[ENTROU] {addr} | Pessoas na sala: {threading.active_count() - 1}")
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                msg = data.decode().strip().lower()

                if msg == "entrar":
                    resposta = "Entrou na sala"
                elif msg == "sair":
                    resposta = "Saiu da sala"
                    conn.sendall(resposta.encode())
                    break  
                else:
                    resposta = "Mensagem inválida"

                conn.sendall(resposta.encode())

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
