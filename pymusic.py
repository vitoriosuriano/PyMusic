from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

# Nome do arquivo que contém os links das músicas
arquivo_links = 'linkmusicas.txt'

# Diretório onde você deseja salvar as músicas
diretorio_destino = r'C:\Users\Valid\Desktop\Musicas'
# Diretório onde você deseja salvar as músicas mp4 de auxiliar
diretorio_destino_mp4 = r'C:\Users\Valid\Desktop\Musicas\bin'

# Função para baixar e converter a música
def baixar_e_converter_musica(link):
    try:
        yt = YouTube(link)

        # Baixe o vídeo
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        stream.download(output_path=diretorio_destino_mp4)
        print(f'{yt.title} baixada com sucesso em formato MP4!')

        # Converta o arquivo MP4 em MP3
        caminho_arquivo_mp4 = os.path.join(diretorio_destino_mp4, f'{yt.title}.mp4')
        caminho_arquivo_mp3 = os.path.join(diretorio_destino, f'{yt.title}.mp3')
        video_clip = VideoFileClip(caminho_arquivo_mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(caminho_arquivo_mp3)
        video_clip.close()
        audio_clip.close()
        print(f'{yt.title} convertida para MP3 com sucesso!')

        # Exclua o arquivo MP4
        os.remove(caminho_arquivo_mp4)
        print(f'Arquivo MP4 excluído: {caminho_arquivo_mp4}')

    except Exception as e:
        print(f'Erro ao baixar/converter {link}: {str(e)}')

# Lê os links do arquivo
with open(arquivo_links, 'r') as file:
    links = file.read().splitlines()

# Baixa e converte cada música da lista!
for link in links:
    baixar_e_converter_musica(link)