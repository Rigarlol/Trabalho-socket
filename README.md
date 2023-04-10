# Chat Cliente/Servidor

Este é um simples aplicativo de chat que permite a comunicação entre um cliente e um servidor.

## Como funciona?

O servidor é iniciado em uma máquina e aguarda a conexão do cliente. O cliente, por sua vez, se conecta ao servidor e pode enviar mensagens que serão recebidas por todos os outros clientes conectados ao mesmo servidor.

## Requisitos

- Python 3.x

## Como usar?

1. Faça o download do código fonte ou clone o repositório do GitHub:

`git clone https://github.com/seu-usuario/chat-client-server.git`

2. Abra dois terminais, um para o cliente e outro para o servidor.

3. No terminal do servidor, navegue até o diretório do código fonte e execute o seguinte comando

`python server.py`

4. No terminal do cliente, navegue até o diretório do código fonte e execute o seguinte comando:

`python cliente.py`

5. Agora você pode enviar mensagens pelo cliente e elas serão recebidas por todos os outros clientes conectados ao mesmo servidor.

## Parâmetros de configuração

Você pode configurar o endereço IP e a porta do servidor editando as constantes HOST e PORT no arquivo server.py. Por padrão, o servidor está configurado para escutar conexões na porta 5000 em todas as interfaces de rede (0.0.0.0).

Você também pode configurar o endereço IP e a porta do cliente editando as constantes HOST e PORT no arquivo client.py. Por padrão, o cliente está configurado para se conectar ao servidor na porta 5000 no endereço localhost.
