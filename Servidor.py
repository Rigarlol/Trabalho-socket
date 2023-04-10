import socket
import threading
import json

# define a porta e o endereço do servidor
HOST = '127.0.0.1'
PORT = 5000

# cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# vincula o socket à porta e ao endereço definidos
server_socket.bind((HOST, PORT))

# define o número máximo de conexões simultâneas
server_socket.listen(5)

lista_mensagens = []

# função que trata cada conexão
def handle_connection(client_socket, client_address):
    print(f"Nova conexão: {client_address}")
    
    try:
        # loop para receber as mensagens do cliente
        while True:
            # recebe a mensagem do cliente e decodifica do formato JSON
            data = client_socket.recv(1024).decode()
            if not data:
                break
            message = json.loads(data)

            # executa a operação solicitada pelo cliente
            if message["operation"] == "ENVIAR":
                mensagem = message["params"]["mensagem"]
                status = '200 OK'
                response = {"status": status}
                operation = {"operation: ENVIAR"}
                lista_mensagens.append([client_address, mensagem])
                print(f"Nova mensagem recebida: {mensagem}, {response}, {operation}")

            if message["operation"] == "ERROR_BUSCAR":
                status = '404 ERROR'
                response = {"status": status}
                print(response)    

            elif message["operation"] == "ERROR_ENVIAR":
                status = '404 ERROR'
                response = {"status": status}
                print(f"Nova mensagem recebida: {response}")
                
                
            elif message["operation"] == "BUSCAR":
                
                response = {"status": "200 OK", "mensagens": lista_mensagens}
                print(response)
            

            elif message["operation"] == "SAIR":
                print(f"Encerrando conexão: {client_address}")
                response = {"status": "OK"}
                break

            else:
                response = {"status": "ERROR", "message": "Operação desconhecida"}

            # codifica a resposta no formato JSON e envia para o cliente
            response_data = json.dumps(response).encode()
            client_socket.sendall(response_data)

    except Exception as e:
        print(f"Erro na conexão: {e}")
    finally:
        # fecha o socket do cliente
        client_socket.close()


# loop principal do servidor
print(f"Servidor iniciado em {HOST}:{PORT}")
while True:
    # aguarda por novas conexões
    client_socket, client_address = server_socket.accept()

    # cria uma nova thread para tratar a conexão
    client_thread = threading.Thread(target=handle_connection, args=(client_socket, client_address))
    client_thread.start()