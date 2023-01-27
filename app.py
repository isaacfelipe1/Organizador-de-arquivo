import os
#pega os nome dos arquivos
#pega a extensão para determinar o tipo
# criar as pastas :imagens, audios, documentos, videos, outros
#mover os arquivos para pastas correspondentes
#find ('.') vai encontrar o indice a partir da esquerda
#
audios_ext=['.mp3','.wav']
videos_ext=['.mp4','.mov','.avi']
imagens_ext=['.jpg','.jpeg','.png']
documentos_ext=['.txt', '.log','.pdf']

def pegar_extensao(nome):
    index=nome.rfind('.')
    return nome[index:]

def organizar(diretorio):
    AUDIO_DIR=os.path.join(diretorio,"audios")
    IMAGENS_DIR=os.path.join(diretorio,"imagens")
    DOCS_DIR=os.path.join(diretorio,"documentos")
    VIDEOS_DIR=os.path.join(diretorio,"videos")
    OUTROS_DIR=os.path.join(diretorio,"outros")
    if not os.path.isdir(AUDIO_DIR):
        os.makedirs(AUDIO_DIR)
    if not os.path.isdir(IMAGENS_DIR):
        os.makedirs(IMAGENS_DIR)
    if not os.path.isdir(DOCS_DIR):
        os.makedirs(DOCS_DIR)
    if not os.path.isdir(VIDEOS_DIR):
        os.makedirs(VIDEOS_DIR)
    if not os.path.isdir(OUTROS_DIR):
        os.makedirs(OUTROS_DIR)
    nomes_arquivos=os.listdir(diretorio)
    nova_pasta=''
    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretorio,arquivo)):
            #extensão dos arquivos em minúsculas
            extensao=str.lower(pegar_extensao(arquivo))
            if extensao in audios_ext:
                nova_pasta= AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta=VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta=IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta=DOCS_DIR
            else:
                nova_pasta=OUTROS_DIR
            
            velho=os.path.join(diretorio, arquivo)
            novo= os.path.join(nova_pasta,arquivo)
            os.rename(velho,novo)
            print("Moveu: ", velho, "->", novo )
            
            
if __name__=='__main__':
    organizar('Downloads')
