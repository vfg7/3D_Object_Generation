import torch
import numpy as np
import torch.nn as nn
from torchvision import models, transforms

def gpu_check():

    if torch.cuda.is_available():
        print(f"GPU disponível: {torch.cuda.get_device_name(0)}")
        return torch.device("cuda")
    else:
        print("GPU não disponível. Usando CPU.")
        return torch.device("cpu")

def carregar_modelo(pretreinado=True, size=1024):
    modelo = models.resnet50(pretrained=pretreinado)
    modelo.fc = torch.nn.Linear(modelo.fc.in_features, size * 3)  # Ajustando para 1024 vértices 3D
    modelo.eval()
    return modelo

#pré-processamento das imagens
def preprocessar_imagens(imagens):
    transformacao = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    imagens_processadas = []

    for imagem in imagens:
      if imagem.mode != 'RGB':
        imagem = transformacao(imagem.convert('RGB'))
      else:
        imagem = transformacao(imagem)

      imagens_processadas.append(imagem)

    return torch.stack(imagens_processadas)

def malha3d(modelo, imagens_processadas):

    with torch.no_grad():
        # Inferência do modelo para obter os vértices
        saidas = modelo(imagens_processadas)
        print(saidas.shape, type(saidas))
        if saidas.ndimension() == 3:  # Formato (batch, 1024, 3)
          vertices = saidas.view(-1, 3).numpy()  # Concatena os lotes
        else:  # Caso tenha apenas uma entrada
          vertices = saidas.view(-1, 3).numpy()

    lado = int(np.sqrt(len(vertices)//3))  # grid quadrado

    faces = []
    for i in range(lado - 1):
        for j in range(lado - 1):
            idx = i * lado + j
            # triângulos
            faces.append([idx, idx + 1, idx + lado])
            faces.append([idx + 1, idx + lado + 1, idx + lado])
    faces = np.array(faces)

    return vertices, faces