from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube

def baixar_video(link_do_video, caminho_destino='.'):
    try:
        video = YouTube(link_do_video)
        stream = video.streams.get_highest_resolution()
        print(f'Baixando vídeo: {video.title}')
        stream.download(output_path=caminho_destino)
        print('Download concluído!')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

def iniciar_download():
    link = link_entry.get()
    diretorio_destino = diretorio_destino_var.get()
    baixar_video(link, diretorio_destino)

# Criar a janela principal
janela = Tk()
janela.title('Download de Vídeo do YouTube')

# Variável para armazenar o diretório de destino
diretorio_destino_var = StringVar()
diretorio_destino_var.set('C:\\Users\\Lisboa\\Downloads\\h')

# Configurar as dimensões e a posição da janela
largura_janela = 800
altura_janela = 400
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x_pos = (largura_tela - largura_janela) // 2
y_pos = (altura_tela - altura_janela) // 2
janela.geometry(f'{largura_janela}x{altura_janela}+{x_pos}+{y_pos}')

# Rótulo e entrada para o link do vídeo
Label(janela, text='Link do Vídeo:').pack(pady=5)
link_entry = Entry(janela, width=40)
link_entry.pack(pady=5)

# Rótulo e entrada para o diretório de destino
Label(janela, text='Diretório de Destino:').pack(pady=5)
diretorio_entry = Entry(janela, textvariable=diretorio_destino_var, width=40)
diretorio_entry.pack(pady=5)

# Botão para iniciar o download
botao_download = Button(janela, text='Baixar Vídeo', command=iniciar_download)
botao_download.pack(pady=10)

# Centralizar e alinhar verticalmente os elementos
for widget in janela.winfo_children():
    widget.pack_configure(anchor='center')

# Iniciar o loop principal da interface gráfica
janela.mainloop()
