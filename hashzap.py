# Levantar Requisitos do sistema
    # Título do sistema: HashZap
        # Botão : iniciar chat
        # Pop - up ( Janela na  frente da tela)
        # Titulo : Bem vindo ao HashZap
        # Campo de texto : Escreva seu nome no chat - usuário se cadastra no chat
        # Botão : Entrar no chat
            # Sumir com o Título
            # Fechar Pop Up
            # Tirar botão iniciar chat 
            # Carregar o chat
                # Mensagens que já foram enviadas
                # Campo: Digite sua mensagem
                # Botão: Enviar   

# Ferramenta de desenvolvimento - Biblioteca : Flet (BackEnd/FrontEnd)
# pip install flet

# Passo a passo do flet 

# Passo 1: Importar o flet
import flet as ft 

# Passo 2: Criar função principal (main) do seu aplicativo

def main(pagina):
    # criar todas as funcionalidades
    # criar um elemento
    titulo = ft.Text("Hashzap")

    # Criar janela pop up
        # Título da janela  
    titulo_janela = ft.Text("Bem vindo (a) ao HashZap")
    campo_nome_usuario = ft.TextField(label="Nome de usuário")

    chat = ft.Column()

    def enviar_mensagem_todos(mensagem):
        texto_chat= ft.Text(mensagem)
        chat.controls.append(texto_chat)

        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_todos)

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem= f"{nome_usuario}: {texto_mensagem}"
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value=""

        pagina.update()

    
    campo_mensagem = ft.TextField(label="Digite uma mensagem",on_submit=enviar_mensagem) #Adicionar on submit
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem= f"{campo_nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(mensagem)

        pagina.update()


    def voltar_inicio(evento):
        janela.open = False

        pagina.update()

    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    botao_cancelar = ft.ElevatedButton("Cancelar", on_click=voltar_inicio)
    janela = ft.AlertDialog(title=titulo_janela,content=campo_nome_usuario, actions=[botao_entrar,botao_cancelar])

    # Passo 3: Fazer função do botão
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat )
    
    # adicionar o elemento na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Passo 3: Rodar o app
ft.app(main, view=ft.WEB_BROWSER)



