from PIL import Image
import os

# Caminhos das imagens de entrada
image_paths = [
    'Teste_pratico\conversor_img\img\barcoRoma.webp',
    'Teste_pratico\conversor_img\img\os2.webp',
    'Teste_pratico\conversor_img\img\tropa.webp'
]

# Define a resolução alvo para o fundo de tela
target_resolution = (1920, 1080)

# Lista para armazenar os caminhos de saída
output_paths = []
for path in image_paths:
    # Abrir a imagem
    img = Image.open(path)
    # Redimensionar a imagem mantendo a proporção
    img_resized = img.resize(target_resolution, Image.LANCZOS)
    # Extrair o nome do arquivo sem a extensão e definir o caminho de saída
    filename = os.path.splitext(os.path.basename(path))[0]
    output_path = f'Teste_pratico/conversor_img/img/{filename}.png'
    # Salvar a imagem convertida em PNG
    img_resized.save(output_path, format='PNG')
    output_paths.append(output_path)

output_paths