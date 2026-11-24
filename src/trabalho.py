import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)

st.header("1. Saturação")
col1, col2 = st.columns(2)
fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = np.clip(s * fator, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(img, caption="Original")
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Saturação")

st.header("2. Brilho")
col1, col2 = st.columns(2)
brilho = col1.slider("Brilho", 0.0, 2.0, 1.2)
v = hsv[:, :, 2].astype(float)
v = np.clip(v * brilho, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
col1.image(img, caption="Original")
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Brilho")

st.header("3. Matiz girada")
col1, col2 = st.columns(2)
giro = col1.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = (h + giro // 2) % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
col1.image(img, caption="Original")
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="Matiz girada")

st.header("8. Negativo")
col1, col2 = st.columns(2)
col1.image(img, caption="Original")
col2.image(255 - img, caption="Negativo")

st.header("11. Espelhamento")
col1, col2 = st.columns(2)
col1.image(img[:, ::-1], caption="Horizontal")
col2.image(img[::-1, :], caption="Vertical")
