import socket
import time
def iniciar_cliente():
    
    HOST = '127.0.0.1'
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        print("Solicitando Entrada...")
        
        S.sendall(b"entrar")
        data = S.recv(1024)
        msg = data.decode().strip().lower()
        if msg == "permitido":
            print("entrou")
            mensage=input("precione enter para sair para sair").encode('utf-8')
            S.sendall(mensage)
        else:
            print("\nSala cheia\n")

if __name__ == "__main__":
    iniciar_cliente()