from pathlib import Path
import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    """Repete cada pixel nas linhas e nas colunas, formando blocos."""
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Imagem como matriz")
st.write("João Vitor Ferrari · RA 241072083 · Turma A")
st.subheader("Bandeira do Canadá em pixels")
st.write("Matriz RGB de 32 linhas por 64 colunas, na proporção 1:2. As faixas vermelhas ocupam 16 colunas de cada lado; o centro branco é um quadrado.")

branco = (255, 255, 255)
vermelho = (255, 0, 0)
vermelho_escuro = (200, 0, 0)
oficial = st.checkbox("Mostrar somente as duas cores da bandeira oficial")
st.caption("A bandeira oficial tem vermelho e branco. Nesta releitura em pixels, o contorno vermelho escuro da folha acrescenta o terceiro RGB pedido na atividade.")

bandeira = np.zeros((32, 64, 3), dtype=np.uint8)
bandeira[:] = branco
bandeira[:, :16] = vermelho
bandeira[:, 48:] = vermelho

# Folha de 11 pontas baseada no SVG de referência. As pequenas curvas
# são aproximadas pelos seus extremos; as coordenadas são reduzidas para pixels.
pontos = np.array([
    [4890, 4430], [4845, 3567], [4956, 3469], [5815, 3620],
    [5699, 3300], [5719, 3227], [6660, 2465], [6448, 2366],
    [6414, 2287], [6600, 1715], [6058, 1830], [5985, 1792],
    [5880, 1545], [5457, 1999], [5346, 1942], [5550, 890],
    [5223, 1079], [5132, 1052], [4800, 400], [4468, 1052],
    [4377, 1079], [4050, 890], [4254, 1942], [4143, 1999],
    [3720, 1545], [3615, 1792], [3542, 1830], [3000, 1715],
    [3186, 2287], [3152, 2366], [2940, 2465], [3881, 3227],
    [3901, 3300], [3785, 3620], [4644, 3469], [4755, 3567],
    [4710, 4430],
], dtype=float) / 150

# Cada cruzamento de uma aresta inverte a máscara. Testamos o centro
# de cada pixel (coluna + 0.5, linha + 0.5) para descobrir o interior da folha.
linhas, colunas = np.indices((32, 64))
x, y = colunas + 0.5, linhas + 0.5
folha = np.zeros((32, 64), dtype=bool)
for i in range(len(pontos)):
    x1, y1 = pontos[i - 1]
    x2, y2 = pontos[i]
    if y1 != y2:
        cruza = ((y1 > y) != (y2 > y)) & (x < (x2 - x1) * (y - y1) / (y2 - y1) + x1)
        folha ^= cruza
bandeira[folha] = vermelho

# O interior tem quatro vizinhos que também pertencem à folha.
interior = folha.copy()
interior[1:, :] &= folha[:-1, :]
interior[:-1, :] &= folha[1:, :]
interior[:, 1:] &= folha[:, :-1]
interior[:, :-1] &= folha[:, 1:]
contorno = folha & ~interior
if not oficial:
    bandeira[contorno] = vermelho_escuro

st.image(ampliar(bandeira), caption="Canadá · 32 × 64 pixels · ampliação de 30 vezes")
st.table([
    {"Cor": "Branco", "RGB": str(branco), "Hexadecimal": "#FFFFFF", "Uso": "Centro"},
    {"Cor": "Vermelho", "RGB": str(vermelho), "Hexadecimal": "#FF0000", "Uso": "Faixas e folha"},
    {"Cor": "Vermelho escuro", "RGB": str(vermelho_escuro), "Hexadecimal": "#C80000", "Uso": "Contorno da releitura"},
])
st.caption("NumPy usa [linha, coluna]. O tipo uint8 guarda cada canal entre 0 e 255.")

with st.expander("Referência e seletores de cores"):
    referencia = Path(__file__).resolve().parents[1] / "assets" / "bandeira-canada.svg"
    st.image(str(referencia), width=400, caption="Referência com as duas cores oficiais")
    st.markdown("[Descrição oficial](https://www.canada.ca/en/canadian-heritage/services/flag-canada-description.html) · [SVG de referência](https://commons.wikimedia.org/wiki/File:Flag_of_Canada.svg)")
    st.write("Seletores para conferir os valores RGB usados na imagem:")
    for nome, hexadecimal in [("Branco", "#FFFFFF"), ("Vermelho", "#FF0000"), ("Vermelho escuro", "#C80000")]:
        cor = st.color_picker(nome, hexadecimal, key=f"cor_{nome}")
        rgb = tuple(int(cor[i:i + 2], 16) for i in (1, 3, 5))
        st.write(f"{nome}: {cor.upper()} → RGB {rgb}")

with st.expander("Experimentos da aula"):
    st.subheader("1 · Imagem preta de 8 × 8")
    imagem = np.zeros((8, 8), dtype=np.uint8)
    st.image(ampliar(imagem))
    st.write(imagem)
    st.subheader("2 · Pixel branco na linha 2, coluna 5")
    imagem[2, 5] = 255
    st.image(ampliar(imagem))
    st.write(imagem)
    st.subheader("3 · Metade inferior cinza")
    imagem[4:, :] = 128
    st.image(ampliar(imagem))
    st.write(imagem)
    st.subheader("4 · Três faixas coloridas")
    faixas = np.zeros((6, 9, 3), dtype=np.uint8)
    faixas[:2, :] = (110, 50, 150)
    faixas[2:4, :] = (240, 190, 40)
    faixas[4:, :] = (30, 160, 150)
    st.image(ampliar(faixas))
