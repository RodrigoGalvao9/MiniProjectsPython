from PIL import Image
import requests
from io import BytesIO
import os

# Lista de URLs das imagens
image_urls = [
    'https://image.tmdb.org/t/p/original/d4Lj2wp7Qd5dIgybVqyhySNvsmq.jpg',
    'https://image.tmdb.org/t/p/original/513P9B1qIrLIDjH785PiaOdZqBz.jpg',
    'https://image.tmdb.org/t/p/original/flShWk2HFy4FfjJEMRnIbDQFP7W.jpg'
]

# Define a resolução alvo para o fundo de tela
target_resolution = (1920, 1080)

# Lista para armazenar os caminhos de saída
output_paths = []
for url in image_urls:
    # Fazer o download da imagem
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    
    # Redimensionar a imagem mantendo a proporção
    img_resized = img.resize(target_resolution, Image.LANCZOS)
    
    # Extrair o nome do arquivo da URL sem a extensão
    filename = os.path.splitext(os.path.basename(url))[0]
    output_path = f'Teste_pratico/conversor_img/img/{filename}.png'
    
    # Salvar a imagem convertida em PNG
    img_resized.save(output_path, format='PNG')
    output_paths.append(output_path)

output_paths