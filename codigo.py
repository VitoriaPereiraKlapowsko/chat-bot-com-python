import flet as ft# Framework para site ou aplicativo

def main(pagina): 
    texto = ft.Text('Chat da Vitoria')
    
    chat = ft.Column() #Para as mensagens aparecerem uma a baixo da outra, se eu quiser diferente coloco como linha por exemplo
    
    def enviar_mensagem(evento):
        print('Enviar Mensagem')
        
        texto_mensagem = ft.Text(campo_mensagem.value)
        chat.controls.append(texto_mensagem)
        
        campo_mensagem.value = ''
        pagina.update()
    
    campo_mensagem = ft.TextField(label='Digite a sua mensagem')
    botao_enviar = ft.ElevatedButton('Enviar', on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar]) #colocando um do lado do outro
    def entrar_chat(evento):
        print('Entrar no Chat')
        #Aqui estou tirando o PopUp antigo, botão e texto que estava antes na tela
        popup.open = False
        pagina.remove(botao_iniciar)
        pagina.remove(texto)
        #Adicionando o chat na página
        pagina.add(chat)
        texto_entrada = ft.Text(f'{nome_usuario.value} Entrou no chat')
        chat.controls.append(texto_entrada)#Adicionando o nome do usuário
        pagina.add(linha_enviar)
        #Só atualizando
        pagina.update()
        
    titulo_popup = ft.Text('fBem-Vindo ao Chat da Vitoria')
    nome_usuario = ft.TextField(label='Escreva seu nome no Chat')
    botao_entrar = ft.ElevatedButton('Entrar no Chat', on_click=entrar_chat)
    popup = ft.AlertDialog(
        open=False, #Fazendo ele esperar para abrir, não é obrigatório mas é bom colocar
        modal=True, #Colocando ele no meio da tela 
        title=titulo_popup, #Inserindo o titulo 
        content=nome_usuario, #Textinho que fica na caixinha label para poder escrever
        actions=[botao_entrar] #A ação é regra estar em uma lista []
    )
    
    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update() #Não preciso apertar f5 para atualizar ele atualiza sozinho
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup) #ft. eu defino o tipo do botão
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main) #Chamando o Main para app mobile, para fazer web coloca -> view=ft.WEB_BROWSER