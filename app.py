import numpy as np
import streamlit as st

st.title("Computação Gráfica")
st.write("Meu nome é João Vitor Ferrari.")

n = st.slider("Tamanho", 2, 64, 8)
tipo = st.radio("Imagem", ["Aleatória", "Cinza 128"], horizontal=True)
if tipo == "Cinza 128":
    img = np.full((n, n), 128, dtype=np.uint8)
else:
    img = np.random.randint(0, 256, (n, n), dtype=np.uint8)

st.image(img, caption=f"Imagem {n}x{n}", width=300)
st.write(img)
