# 3D_object_generation

# Geração de Malha 3D a partir de Imagens 2D

Este projeto utiliza redes neurais e técnicas de reconstrução 3D para gerar malhas 3D a partir de imagens 2D. O modelo pré-treinado **ResNet50** é utilizado para processar as imagens e gerar os vértices 3D, enquanto a malha é construída utilizando o pacote **Trimesh**.

## Requisitos

- Python 3.x
- PyTorch
- Trimesh
Instalação das dependências:

```bash
pip install torch torchvision trimesh
```

## Estrutura do Projeto

- `generate3D.py`: Script para gerar a malha 3D a partir das imagens 2D.
- **samples/**: Pasta para armazenar as imagens 2D utilizadas na reconstrução e onde as malhas 3D geradas serão salvas (no formato .glb).

## Como Usar

### 1. Preparar as Imagens

Coloque as imagens 2D que você deseja usar para gerar a malha na pasta `samples/`.

### 2. Executar o Script de Geração

Execute o script `generate3D.py` para gerar a malha 3D. O código irá carregar as imagens da pasta `samples/`, processá-las utilizando o modelo ResNet50 e gerar a malha 3D.

```bash
python src/generate3D.py
```

### 3. Visualizar a Malha

Você pode visualizar a malha gerada usando softwares como 3D viewer ou Blender, utilizando o formato `.glb` exportado.
## Estrutura de Geração da Malha 3D

1. **ResNet50**: Utiliza um modelo pré-treinado para extrair características das imagens 2D.
2. **Reconstrução de Vértices**: O modelo gera uma saída que é interpretada como um conjunto de vértices 3D.
3. **Construção das Faces**: As faces são geradas com base nos vértices, usando métodos pré-definidos.
4. **Exportação**: A malha 3D é exportada em formato `.glb` usando o Trimesh.

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou correções, fique à vontade para abrir um pull request.

## Licença

Este projeto é licenciado sob a Licença para mais detalhes.
