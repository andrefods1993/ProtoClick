import dropbox
import webbrowser
import urllib.parse
import uuid
import os

# Define as credenciais do aplicativo do Dropbox
ACCESS_TOKEN = 'sl.ByFFGyTY5qasl1ZYqfcdQgiWQVx354UqnQW3T95oNssRxumQC4kiPwRCVFaFQmj8_DooQIjpHEo29K1hxky6qg0qKYmkCjMlwxuXoDcGPYBwNDLR0p5IgP7qm43cmP_EqGdpziB-TZDYUqY'

# Caminho do arquivo que será enviado para o Dropbox
caminho_arquivo = 'config/Protocolo.pdf'

def upload_arquivo_dropbox(caminho_arquivo):
    # Autenticação no Dropbox
    dbx = dropbox.Dropbox(ACCESS_TOKEN)

    # Gerar um identificador único para o nome do arquivo
    arquivo_uuid = str(uuid.uuid4())
    nome_arquivo = f'{arquivo_uuid}_{os.path.basename(caminho_arquivo)}'

    # Realiza o upload do arquivo para o Dropbox
    with open(caminho_arquivo, 'rb') as file:
        response = dbx.files_upload(file.read(), f'/ProtoClick/{nome_arquivo}')

    # Cria um link compartilhado para o arquivo
    shared_link = dbx.sharing_create_shared_link(response.path_display)

    # Retorna o link compartilhado do Dropbox
    return shared_link.url

def enviar_whatsapp_arquivo(numero, link_arquivo):

    numero = f'+{numero[0]}'
  
    # Decodificar o link do arquivo para evitar duplicação da codificação
    link_arquivo_decodificado = urllib.parse.unquote(link_arquivo)
    
    # Criar a mensagem com o link do arquivo
    mensagem = f'Olá, estou enviando o link do protocolo de atendimento para você: {link_arquivo_decodificado}'
    
    # Codificar a mensagem para o formato de URL
    mensagem_url = urllib.parse.quote(mensagem)
    
    # Montar a URL do WhatsApp com a mensagem
    url_whatsapp = f'https://wa.me/{numero}?text={mensagem_url}'
    print(url_whatsapp)
    # Abrir o navegador padrão com a URL do WhatsApp
    webbrowser.open(url_whatsapp)


def upload_arquivo_e_enviar_whatsapp(numero, caminho_arquivo):
    # Faz o upload do arquivo para o Dropbox e obtém o link compartilhado
    link_arquivo = upload_arquivo_dropbox(caminho_arquivo)
    
    # Envia o link do arquivo pelo WhatsApp
    enviar_whatsapp_arquivo(numero, link_arquivo)
