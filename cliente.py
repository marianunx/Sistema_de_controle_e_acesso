import socket
import time

def iniciar_cliente():
    HOST = '127.0.0.1'
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        print("Solicitando entrada na sala...")

        S.sendall(b"entrar")
        data = S.recv(1024)
        msg = data.decode().strip().lower()

        if msg == "permitido":
            print("\nEntrada permitida! Você está na sala.")
            input("Pressione ENTER para sair da sala.")
            S.sendall(b"sair")
            print("\nVocê saiu da sala. Conexão encerrada.")
        else:
            print("\nSala cheia. Tente novamente mais tarde.")

if __name__ == "__main__":
    iniciar_cliente()
