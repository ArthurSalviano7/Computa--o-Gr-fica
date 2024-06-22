import math
import numpy as np
from PIL import Image, ImageTk
import Operacoes

# TRANSFORMAÇÕES
def negativo_da_imagem(imagem):
    # Criar uma cópia da imagem para aplicar a Transformação
    imagem_filtrada = imagem.copy()
    # Obter largura e altura da imagem
    height, width = imagem.shape
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    

    # Aplicar o filtro
    for y in range(0, height):
        for x in range(0, width):
            valor_transformado = 255 - img_array[y, x] # S = 255 - r
            
            imagem_filtrada[y, x] = valor_transformado

    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(imagem_filtrada.astype('uint8'), 'L')

    print(imagem_filtrada, "\n")

    return imagem_filtrada_convertida

def logaritmo(imagem, a):
    # Criar uma cópia da imagem para aplicar a Transformação
    imagem_filtrada = imagem.copy()
    # Obter largura e altura da imagem
    height, width = imagem.shape
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    

    # Aplicar o filtro
    for y in range(0, height):
        for x in range(0, width):
            valor_transformado = a * np.log(img_array[y, x] + 1)   # S = a * log(r + 1)
            
            imagem_filtrada[y, x] = valor_transformado

    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(imagem_filtrada.astype('uint8'), 'L')

    print(imagem_filtrada, "\n")

    return imagem_filtrada_convertida

def logaritmo(imagem, c, gamma):
    # Criar uma cópia da imagem para aplicar a Transformação
    imagem_filtrada = imagem.copy()
    # Obter largura e altura da imagem
    height, width = imagem.shape
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)

    # Aplicar o filtro
    for y in range(0, height):
        for x in range(0, width):
            # S = c * r**y
            valor_transformado = round(c * (img_array[y, x] ** gamma))
            valor_transformado = np.clip(valor_transformado, 0, 255)       
            imagem_filtrada[y, x] = valor_transformado


    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(imagem_filtrada.astype('uint8'), 'L')

    print(imagem_filtrada, "\n")

    return imagem_filtrada_convertida

def linear(imagem, a, b):
    # Criar uma cópia da imagem para aplicar a Transformação
    imagem_filtrada = imagem.copy()
    # Obter largura e altura da imagem
    height, width = imagem.shape
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)

    # Aplicar o filtro
    for y in range(0, height):
        for x in range(0, width):
            # S = a * r + b
            valor_transformado = round(a * img_array[y, x] + b)
            valor_transformado = np.clip(valor_transformado, 0, 255)       
            imagem_filtrada[y, x] = valor_transformado


    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(imagem_filtrada.astype('uint8'), 'L')

    print(imagem_filtrada, "\n")

    return imagem_filtrada_convertida

def faixa_dinamica_orig(imagem, w_target):
    # Criar uma cópia da imagem para aplicar a Transformação
    imagem_filtrada = imagem.copy()
    # Obter largura e altura da imagem
    height, width = imagem.shape
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)

    #Pegar os valores min e max da imagem (nível de cinza)
    fmin = np.min(img_array)
    fmax = np.max(img_array)

    # Aplicar o filtro
    for y in range(0, height):
        for x in range(0, width):
            # S = (f - fmin / fmax - fmin) * w_target
            valor_transformado = round(((img_array[y, x] - fmin) / (fmax - fmin)) * w_target)
            valor_transformado = np.clip(valor_transformado, 0, 255)       
            imagem_filtrada[y, x] = valor_transformado


    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(imagem_filtrada.astype('uint8'), 'L')

    print(imagem_filtrada, "\n")

    return imagem_filtrada_convertida

def faixa_dinamica(imagem, w_target):
    # Converter imagem para matriz numpy
    img_array = np.array(imagem, dtype=np.float64)

    # Pegar os valores min e max da imagem (nível de cinza)
    fmin = np.min(img_array)
    fmax = np.max(img_array)

    # Aplicar a transformação para ajustar a faixa dinâmica
    img_array = ((img_array - fmin) / (fmax - fmin)) * (w_target - 1)
    
    # Arredondar para os valores inteiros mais próximos
    img_array = np.round(img_array).astype(np.uint8)

    # Converter a matriz filtrada de volta para imagem PIL
    imagem_filtrada_convertida = Image.fromarray(img_array, 'L')

    return imagem_filtrada_convertida

# TRANSFORMAÇÕES GEOMÉTRICAS
def zoom_in(imagem):
    altura_original, largura_original = imagem.shape
    largura_nova = largura_original * 2
    altura_nova = altura_original * 2
    
    print("Imagem Original:")
    print(largura_original, " x ", altura_original)
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Criar nova matriz para a imagem ampliada
    img_ampliada = np.zeros((altura_nova, largura_nova), dtype=np.uint8)
    
    # Ampliar a imagem duplicando os pixels
    for y in range(altura_original):
        for x in range(largura_original):
            img_ampliada[2*y, 2*x] = img_array[y, x]  # Preencher o pixel original
            img_ampliada[2*y+1, 2*x] = img_array[y, x]  # Repetir na direção X
            img_ampliada[2*y, 2*x+1] = img_array[y, x]  # Repetir na direção Y
            img_ampliada[2*y+1, 2*x+1] = img_array[y, x]  # Repetir na direção X e Y
    
    
    # Converter matriz de volta para imagem PIL
    imagem_ampliada = Image.fromarray(img_ampliada)
    print("Imagem Transformada:")
    print(imagem_ampliada)
    
    return imagem_ampliada

def zoom_out(imagem):
    altura_original, largura_original  = imagem.shape
    largura_nova = largura_original // 2
    altura_nova = altura_original // 2
    
    print("Imagem original: ")
    print(largura_original, " x ", altura_original)

    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Criar nova matriz para a imagem reduzida
    img_reduzida = np.zeros((altura_nova, largura_nova), dtype=np.uint8)
    
    # Reduzir a imagem calculando a média dos blocos de 2x2 pixels
    for y in range(altura_nova):
        for x in range(largura_nova):
            # Calcular a média dos quatro pixels na imagem original
            pixel1 = np.uint16(img_array[2*y, 2*x])
            pixel2 = np.uint16(img_array[2*y+1, 2*x])
            pixel3 = np.uint16(img_array[2*y, 2*x+1])
            pixel4 = np.uint16(img_array[2*y+1, 2*x+1])
            pixel_medio = (pixel1 + pixel2 + pixel3 + pixel4) // 4
            img_reduzida[y, x] = np.uint8(pixel_medio)
    
    # Converter matriz de volta para imagem PIL
    imagem_reduzida = Image.fromarray(img_reduzida)
    print("Imagem reduzida: ", imagem_reduzida)

    return imagem_reduzida

def rotacionar_imagem(imagem, angulo):
    altura_original, largura_original = imagem.shape
    
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Converter ângulo para radianos
    angulo_rad = math.radians(angulo)
    
    # Calcular as dimensões da imagem rotacionada
    largura_rotacionada = int(abs(largura_original * math.cos(angulo_rad)) + abs(altura_original * math.sin(angulo_rad)))
    altura_rotacionada = int(abs(altura_original * math.cos(angulo_rad)) + abs(largura_original * math.sin(angulo_rad)))
    
    # Criar matriz para a imagem rotacionada
    img_rotacionada = np.zeros((altura_rotacionada, largura_rotacionada), dtype=np.uint8)
    
    # Calcular centro da imagem original
    centro_x = largura_original // 2
    centro_y = altura_original // 2
    
    # Calcular centro da imagem rotacionada
    centro_x_rot = largura_rotacionada // 2
    centro_y_rot = altura_rotacionada // 2
    
    # Rotação da imagem
    for y in range(altura_original):
        for x in range(largura_original):
            # Calcular coordenadas rotacionadas
            x_rot = int((x - centro_x) * math.cos(angulo_rad) - (y - centro_y) * math.sin(angulo_rad) + centro_x_rot)
            y_rot = int((x - centro_x) * math.sin(angulo_rad) + (y - centro_y) * math.cos(angulo_rad) + centro_y_rot)
            
            # Verificar limites
            if 0 <= x_rot < largura_rotacionada and 0 <= y_rot < altura_rotacionada:
                img_rotacionada[y_rot, x_rot] = img_array[y, x]
    
    # Converter matriz de volta para imagem PIL
    imagem_rotacionada = Image.fromarray(img_rotacionada)
    
    return imagem_rotacionada


def flip_horizontal(imagem):
    altura_original, largura_original  = imagem.shape
    
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Criar matriz transposta
    img_transposta = np.zeros((largura_original, altura_original), dtype=img_array.dtype)
    
    for y in range(altura_original):
        for x in range(largura_original):
            img_transposta[x, y] = img_array[y, x]
    
    # Criar matriz para a imagem rotacionada 90 graus no sentido anti-horário
    img_rotacionada = np.zeros((altura_original, largura_original), dtype=img_array.dtype)
    
    for y in range(largura_original):
        for x in range(altura_original):
            img_rotacionada[altura_original - x - 1, y] = img_transposta[y, x]
    
    # Converter matriz de volta para imagem PIL
    imagem_flipada = Image.fromarray(img_rotacionada)
    
    return imagem_flipada

def flip_vertical(imagem):
    altura_original, largura_original  = imagem.shape
    
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Criar matriz transposta
    img_transposta = np.zeros((largura_original, altura_original), dtype=img_array.dtype)
    
    for y in range(altura_original):
        for x in range(largura_original):
            img_transposta[x, y] = img_array[y, x]
    
    # Criar matriz para a imagem rotacionada 90 graus no sentido horário
    img_rotacionada = np.zeros((altura_original, largura_original), dtype=img_array.dtype)
    
    for y in range(largura_original):
        for x in range(altura_original):
            img_rotacionada[x, largura_original - y - 1] = img_transposta[y, x]
    
    # Converter matriz de volta para imagem PIL
    imagem_flipada = Image.fromarray(img_rotacionada)
    
    return imagem_flipada

def warp_losango(imagem):
    altura_original, largura_original  = imagem.shape
    
    # Converter imagem para matriz numpy
    img_array = np.array(imagem)
    
    # Calcular a dimensão da nova imagem para garantir que caiba o losango
    largura_nova = int(np.sqrt((largura_original**2 + altura_original**2) / 2) * 2)
    altura_nova = largura_nova
    img_warping = np.zeros((altura_nova, largura_nova), dtype=img_array.dtype)
    
    # Coeficientes para a transformação afim (definidos para criar um losango)
    a, b, c = 1, 0.5, 0
    d, e, f = 0.5, 1, 0
    i, j = 0, 0
    
    # Centro da imagem original
    centro_x = largura_original // 2
    centro_y = altura_original // 2
    
    # Centro da nova imagem
    centro_x_nova = largura_nova // 2
    centro_y_nova = altura_nova // 2
    
    for y in range(altura_nova):
        for x in range(largura_nova):
            # Calcular as coordenadas originais usando a transformação inversa
            denom = i * (x - centro_x_nova) + j * (y - centro_y_nova) + 1
            if denom == 0:
                continue
            
            x_original = (a * (x - centro_x_nova) + b * (y - centro_y_nova) + c) / denom
            y_original = (d * (x - centro_x_nova) + e * (y - centro_y_nova) + f) / denom
            
            x_original = int(x_original + centro_x)
            y_original = int(y_original + centro_y)
            
            # Verificar se as coordenadas originais estão dentro dos limites da imagem original
            if 0 <= x_original < largura_original and 0 <= y_original < altura_original:
                img_warping[y, x] = img_array[y_original, x_original]
    
    # Converter matriz de volta para imagem PIL
    imagem_warping = Image.fromarray(img_warping)
    
    return imagem_warping