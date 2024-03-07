import flet as ft# Framework para site ou aplicativo

def main(pagina): 
    texto = ft.Text('Chat da Vitoria')
    
    def abrir_popup(evento):
        print('Abrir PopUp')
        
    botao_iniciar = ft.ElevatedButton('Iniciar Chat', on_click=abrir_popup) #ft. eu defino o tipo do botao
    
    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main) #Chamando o Main para app mobile, para fazer web coloca -> view=ft.WEB_BROWSER