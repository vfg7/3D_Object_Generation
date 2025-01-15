import os
from PIL import Image

def carregar_imagens(diretorio):

    imagens = []
    formatos_suportados = (".jpg", ".jpeg", ".png", ".bmp", ".tiff")

    if not os.path.isdir(diretorio):
        raise FileNotFoundError(f"O diretório {diretorio} não existe.")

    for arquivo in os.listdir(diretorio):
        if arquivo.lower().endswith(formatos_suportados):
            caminho_completo = os.path.join(diretorio, arquivo)
            try:
                imagem = Image.open(caminho_completo)
                imagens.append(imagem)
            except Exception as e:
                print(f"Erro ao carregar a imagem {arquivo}: {e}")

    if not imagens:
        raise ValueError("Nenhuma imagem válida encontrada no diretório.")

    print(f"{len(imagens)} imagens carregadas com sucesso.")
    return imagens