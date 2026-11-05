import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)

st.header("1. HSV")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
col1.image(img, caption="img")
so_h = hsv.copy()
so_h[:, :, 1] = 255
so_h[:, :, 2] = 255
col2.image(cv2.cvtColor(so_h, cv2.COLOR_HSV2RGB), caption="H")

st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)
fator = col1.slider("Saturação", 0.0, 2.0, 1.5)
s = hsv[:, :, 1].astype(float)
s = np.clip(s * fator, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 1] = s
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="saturação")

brilho = col1.slider("Brilho", 0.0, 2.0, 1.2)
v = hsv[:, :, 2].astype(float)
v = np.clip(v * brilho, 0, 255)
hsv2 = hsv.copy()
hsv2[:, :, 2] = v
col1.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="brilho")

giro = col2.slider("Giro (graus)", 0, 360, 120)
h = hsv[:, :, 0].astype(int)
h = (h + giro // 2) % 180
hsv2 = hsv.copy()
hsv2[:, :, 0] = h
col2.image(cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB), caption="matiz girada")

st.header("3. Faixa na escala")
col1, col2 = st.columns(2)
escala = np.zeros((1, 12, 3), dtype=np.uint8)
escala[0, :, 0] = np.arange(0, 180, 15)
escala[0, :, 1] = 255
escala[0, :, 2] = 255
rgb = cv2.cvtColor(escala, cv2.COLOR_HSV2RGB)
col1.image(rgb.repeat(40, axis=0).repeat(40, axis=1), caption="escala")
h_min, h_max = col1.slider("Faixa de H na escala", 0, 179, (90, 130))
mascara = cv2.inRange(escala, (h_min, 0, 0), (h_max, 255, 255))
col2.image(mascara.repeat(40, axis=0).repeat(40, axis=1), caption="máscara")

st.header("4. Máscara de cor")
col1, col2 = st.columns(2)
h_min, h_max = col1.slider("Faixa de H", 0, 179, (10, 20))
mascara = cv2.inRange(hsv, (h_min, 60, 40), (h_max, 255, 255))
col1.image(mascara, caption="máscara de cor")
so_cor = img.copy()
so_cor[mascara == 0] = 0
col2.image(so_cor, caption="só a cor escolhida")

st.header("5. Recorte")
col1, col2 = st.columns(2)
altura, largura = img.shape[0], img.shape[1]
y = col1.slider("y", 0, altura - 1, altura // 4)
x = col1.slider("x", 0, largura - 1, largura // 4)
t = col1.slider("tamanho", 10, largura, largura // 3)
recorte = img[y:y + t, x:x + t]
col1.image(recorte, caption="recorte")
nova = img.copy()
nova[y:y + t, x:x + t] = 255 - nova[y:y + t, x:x + t]
col2.image(nova, caption="negativo no recorte")

st.header("6. Espelhamento")
col1, col2 = st.columns(2)
col1.image(img[:, ::-1], caption="horizontal")
col2.image(img[::-1, :], caption="vertical")
