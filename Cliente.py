import socket
import json


# define o endereço e a porta do servidor
HOST = '127.0.0.1'
PORT = 5000

# cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conecta ao servidor
client_socket.connect((HOST, PORT))

lista_mensagens = []

# define uma função para enviar uma mensagem ao servidor
def enviar_mensagem(mensagem):
    # verifica se a mensagem é uma string e tem no máximo 15 caracteres
    if not isinstance(mensagem, str) or len(mensagem) > 15:
        print("A mensagem deve ser uma string com até 15 caracteres")
        error_message = "404 ERROR"
        operation = "ERROR_ENVIAR"
        message = {"operation": operation, "mensagem": error_message}
        message_data = json.dumps(message).encode()
        client_socket.sendall(message_data)
        response_data = client_socket.recv(1024)
        response = json.loads(response_data.decode())

        return
    
    lista_mensagens.append(mensagem)

    # define a operação a ser executada
    operation = "ENVIAR"

    # define os parâmetros da operação
    params = {"mensagem": mensagem}

    # codifica a mensagem no formato JSON e envia ao servidor
    
    message = {"operation": operation, "params": params}
    message_data = json.dumps(message).encode()
    client_socket.sendall(message_data)

    # espera pela resposta do servidor e decodifica do formato JSON
    response_data = client_socket.recv(1024)
    response = json.loads(response_data.decode())

    # verifica o status da resposta
    if response["status"] == "200 OK":
        print("Mensagem enviada com sucesso")
    else:
        print("Mensagem enviada com sucesso")
    
# define uma função para buscar mensagens no servidor
def buscar_mensagens():

    if len(lista_mensagens) == 0:
        operation = "ERROR_BUSCAR"
        error_buscar = "404 ERROR"
        message = {"operation": operation, "mensagem": error_buscar}
        message_data = json.dumps(message).encode()
        client_socket.sendall(message_data)
        response_data = client_socket.recv(1024)
        response = json.loads(response_data.decode())

        return
    # define a operação a ser executada
    operation = "BUSCAR"

    # codifica a mensagem no formato JSON e envia ao servidor
    message = {"operation": operation}
    message_data = json.dumps(message).encode()
    client_socket.sendall(message_data)

    # espera pela resposta do servidor e decodifica do formato JSON
    response_data = client_socket.recv(1024)
    response = json.loads(response_data.decode())

    # verifica o status da resposta
    if response["status"] == "200 OK":
        # verifica se existem mensagens na resposta
        if "mensagens" in response:
            # imprime as mensagens no console
            for mensagem in response["mensagens"]:
                print(mensagem)
        else:
            print("ERROR 404")
    else:
        print("Erro ao buscar mensagens")


# define uma função para sair da aplicação
def sair():
    # define a operação a ser executada
    operation = "SAIR"

    # codifica a mensagem no formato JSON e envia ao servidor
    message = {"operation": operation}
    message_data = json.dumps(message).encode()
    client_socket.sendall(message_data)

    # espera pela resposta do servidor e decodifica do formato JSON
    response_data = client_socket.recv(1024)
    response = json.loads(response_data.decode())

    # verifica o status da resposta e fecha o socket do cliente
    if response["status"] == "OK":
        print("Conexão encerrada")
        client_socket.close()
    else:
        print("Erro ao encerrar conexão")


# loop principal do cliente
while True:
    # exibe o menu de opções
    print("Opções:")
    print("1 - Enviar mensagem")
    print("2 - Buscar mensagens")
    print("3 - Sair")

    # lê a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # executa a opção escolhida
    if opcao == "1":
        mensagem = input("Digite a mensagem: ")
        enviar_mensagem(mensagem)

    elif opcao == "2":
        buscar_mensagens()

    elif opcao == "3":
        sair()
        break

    else:
        print("Opção inválida")