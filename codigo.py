import flet as ft# Framework para site ou aplicativo

def main(pagina): 
    texto = ft.Text('Chat da Vitoria')
    
    def entrar_chat(evento):
        print('Entrar no Chat')
        
    titulo_popup = ft.Text('Bem-Vindo ao Chat da Vitoria')
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