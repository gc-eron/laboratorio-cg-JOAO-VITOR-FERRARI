import numpy as np
import streamlit as st


def ampliar(imagem, k=30):
    return imagem.repeat(k, axis=0).repeat(k, axis=1)


st.title("Bandeira do Canadá")
st.write("João Vitor Ferrari")

vermelho = (255, 0, 0)
branco = (255, 255, 255)
vermelho_escuro = (200, 0, 0)

bandeira = np.zeros((24, 48, 3), dtype=np.uint8)
bandeira[:] = branco
bandeira[:, :12] = vermelho
bandeira[:, 36:] = vermelho

bandeira[4:8, 23:25] = vermelho
bandeira[7:15, 20:28] = vermelho
bandeira[9:12, 16:19] = vermelho
bandeira[9:12, 29:32] = vermelho
bandeira[11:14, 17:31] = vermelho
bandeira[14:16, 19:29] = vermelho
bandeira[16:18, 21:27] = vermelho
bandeira[18:21, 23:25] = vermelho_escuro

st.image(ampliar(bandeira))
st.write("RGB: vermelho (255, 0, 0), branco (255, 255, 255) e vermelho escuro (200, 0, 0).")
st.caption("O caule usa vermelho escuro para incluir a terceira cor pedida na atividade.")
st.color_picker("Conferir cores", "#FF0000")
