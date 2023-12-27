from tkinter import Tk, Label, Button, StringVar, Entry, filedialog
from moviepy.editor import VideoFileClip
from pydub import AudioSegment
from pytube import YouTube

def converter_video_para_audio(caminho_video, caminho_saida_audio):
    try:
        # Carregar o vídeo
        video_clip = VideoFileClip(caminho_video)

        # Extrair o áudio do vídeo
        audio_clip = video_clip.audio

        # Salvar o áudio em um arquivo
        audio_clip.write_audiofile(caminho_saida_audio, codec='mp3')

        # Fechar os objetos de vídeo e áudio
        video_clip.close()
        audio_clip.close()

        mensagem_status.set('Conversão concluída com sucesso!')

    except Exception as e:
        mensagem_status.set(f'Ocorreu um erro: {e}')

def baixar_video():
    try:
        link_video = entrada_link_video.get()
        video = YouTube(link_video)
        stream = video.streams.get_highest_resolution()
        caminho_video = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[('Arquivos de Vídeo', '*.mp4')])
        stream.download(output_path=caminho_video)
        entrada_caminho_video.delete(0, 'end')
        entrada_caminho_video.insert(0, caminho_video)

        mensagem_status.set('Download de vídeo concluído com sucesso!')

    except Exception as e:
        mensagem_status.set(f'Ocorreu um erro durante o download do vídeo: {e}')

def escolher_arquivo():
    caminho_video = filedialog.askopenfilename(title='Escolher Vídeo', filetypes=[('Arquivos de Vídeo', '*.mp4;*.avi')])
    entrada_caminho_video.delete(0, 'end')
    entrada_caminho_video.insert(0, caminho_video)

def escolher_saida():
    caminho_saida_audio = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[('Arquivos de Áudio', '*.mp3')])
    entrada_caminho_saida.delete(0, 'end')
    entrada_caminho_saida.insert(0, caminho_saida_audio)

# Criar a janela principal
janela = Tk()
janela.title('WILL -- TUBE')

# icone da interface grafica
icon_path = 'icone.ico'
janela.iconbitmap(default=icon_path)

mensagem_status = StringVar()
mensagem_status.set('')

# Rótulo e entrada para o link do vídeo
Label(janela, text='Link do Vídeo:').grid(row=0, column=0, pady=5)
entrada_link_video = Entry(janela, width=40)
entrada_link_video.grid(row=0, column=1, pady=5)

# Botão para baixar o vídeo
Button(janela, text='Baixar Vídeo', command=baixar_video).grid(row=0, column=2, pady=5)

# Rótulo e entrada para o caminho do vídeo
Label(janela, text='Caminho do Vídeo:').grid(row=1, column=0, pady=5)
entrada_caminho_video = Entry(janela, width=40)
entrada_caminho_video.grid(row=1, column=1, pady=5)

# Botão para escolher o arquivo de vídeo
Button(janela, text='Escolher Vídeo', command=escolher_arquivo).grid(row=1, column=2, pady=5)

# Rótulo e entrada para o caminho de saída
Label(janela, text='Caminho de Saída:').grid(row=2, column=0, pady=5)
entrada_caminho_saida = Entry(janela, width=40)
entrada_caminho_saida.grid(row=2, column=1, pady=5)

# Botão para escolher o local de saída
Button(janela, text='Escolher Saída', command=escolher_saida).grid(row=2, column=2, pady=5)

# Botão para iniciar a conversão
Button(janela, text='Converter para Áudio', command=lambda: converter_video_para_audio(entrada_caminho_video.get(), entrada_caminho_saida.get())).grid(row=3, column=0, columnspan=3, pady=10)

# Rótulo para exibir a mensagem de status
Label(janela, textvariable=mensagem_status).grid(row=4, column=0, columnspan=3)

# Iniciar o loop principal da interface gráfica
janela.mainloop()
