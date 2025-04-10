# Servidor (data e hora)

import socket
from datetime import datetime
import threading


def iniciar_servidor():
    
    HOST = '127.0.0.1' #IPv4 (4 blocos de 8 bits)
    PORT = 65432
    
    # Criando o socket TCP/IP
    semaphore = threading.Semaphore(5)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT)) # Vincular o socket ao endereço e porta
        S.listen()
        print(f"Servidor ouvindo em {HOST}:{PORT}")
        
        while True:
            with semaphore:
                print(threading.active_count())
                #nova threafing 
                #thread = thersdfsikfs
                conn, addr = S.accept()
                with conn:
                    print(f"Conectado por {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                    
                        if data.decode().strip().lower() == "entrar":
                            resposta = "Entrou na sala"
                            conn.sendall(resposta.encode())
                            
                            
                        else:
                            conn.sendall("Mensagem inválida")

if __name__ == "__main__":
    iniciar_servidor()
                    
                    