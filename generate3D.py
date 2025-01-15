import trimesh
import numpy as np
from model import *
from carregar_imagens import *

def salvar_em_obj(vertices, faces, caminho):
  try:
   # Ensure vertices are float64
    vertices = vertices.astype(np.float64)
    # Ensure faces are int64 or int32 depending on platform
    faces = faces.astype(np.int64 if np.intp().nbytes == 8 else np.int32)

    malha = trimesh.Trimesh(vertices, faces)
    malha.export(caminho)
    print(f"Modelo salvo em {caminho}.")
  except:
    # print("covert error")
    raise

def salvar_em_glb(vertices, faces, caminho):

    malha = trimesh.Trimesh(vertices, faces)
    malha.export(caminho, file_type="glb")
    print(f"Modelo salvo em {caminho}.")


#main

def reconstruir_e_salvar(diretorio_imagens, caminho, tipo="glb"):

  imagens = carregar_imagens(diretorio_imagens)
  modelo = carregar_modelo()
  imagens_processadas = preprocessar_imagens(imagens)

  # Geração da malha 3D
  vertices, faces = malha3d(modelo, imagens_processadas)

  if tipo == "obj":
    # Salvar a malha 3D em formato .obj
    salvar_em_obj(vertices, faces, diretorio_imagens)
  elif tipo == "glb":
    # Salvar a malha 3D em formato .obj
    salvar_em_glb(vertices, faces, caminho)
  else:
    print('escreveu tipo errado')

def main(diretorio_imagens, caminho, tipo="glb"):
  reconstruir_e_salvar(diretorio_imagens, caminho, tipo)

if __name__ == "__main__":

  diretorio_imagens = './samples'
  caminho = './samples/pikachu_15.glb' #content
  main(diretorio_imagens, caminho, tipo="glb")
