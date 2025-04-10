import socket
import time
def iniciar_cliente():
    
    HOST = '127.0.0.1' #IPv4 (4 blocos de 8 bits)
    PORT = 65432
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        print("Solicitando Entrada...")
        
        S.sendall(b"entrar")
        data = S.recv(1024)
        print("entrou")
        time.sleep(10)
        
        if data.decode() == "numero":
            print("Enviando numero do processo...")
            Numero = b"5"
            S.sendall(Numero)
            data = S.recv(1024)
            print(f"Resposta do servidor: {data.decode()}")

if __name__ == "__main__":
    iniciar_cliente()