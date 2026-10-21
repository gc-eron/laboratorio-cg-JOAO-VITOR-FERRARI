# Laboratório de Computação Gráfica

João Vitor Ferrari · RA 241072083 · Turma A  
UniFil · Computação Gráfica · 2026/4

## Executar

Instale o [uv](https://docs.astral.sh/uv/getting-started/installation/) e o Git. Na pasta do projeto:

```powershell
uv sync
uv run streamlit run app.py
```

Abra o endereço informado no terminal, normalmente http://localhost:8501.
O arquivo `.python-version` seleciona Python 3.12 e `uv.lock` registra as versões das dependências.

## Atividades

- **Atv 1:** app com identificação, controle do tamanho de 2 a 64, imagem aleatória em tons de cinza e sua matriz. A opção **Cinza 128** realiza a alteração com `np.full` proposta na aula.
- **Atv 2:** bandeira do Canadá criada com `np.zeros((32, 64, 3), dtype=np.uint8)`. Fatias de colunas desenham as faixas e uma máscara de NumPy desenha a folha de 11 pontas a partir de um polígono. `ampliar` repete os pixels 30 vezes nos dois eixos. A página também contém os quatro experimentos da aula, os seletores de cores e a referência visual.

## Cores da bandeira

| Cor | Hexadecimal | RGB | Uso |
| --- | --- | --- | --- |
| Branco | #FFFFFF | (255, 255, 255) | Centro |
| Vermelho | #FF0000 | (255, 0, 0) | Faixas e folha |
| Vermelho escuro | #C80000 | (200, 0, 0) | Contorno da releitura em pixels |

A bandeira oficial canadense usa apenas vermelho e branco. O contorno vermelho escuro é uma adaptação artística para incluir um terceiro valor RGB, como solicitado no enunciado. A caixa **Mostrar somente as duas cores da bandeira oficial** remove essa adaptação. A forma usa a proporção oficial 1:2; as curvas pequenas da folha são aproximadas por segmentos de reta na grade de pixels.

Referências: [imagem vetorial da bandeira](https://commons.wikimedia.org/wiki/File:Flag_of_Canada.svg), em domínio público; [descrição oficial do Governo do Canadá](https://www.canada.ca/en/canadian-heritage/services/flag-canada-description.html).

## Estrutura

```text
app.py
src/
  atv1.py
  atv2.py
assets/
  bandeira-canada.svg
pyproject.toml
uv.lock
.python-version
```

As cinco bibliotecas pedidas na Atividade 1 estão declaradas no projeto: Streamlit, NumPy, OpenCV headless, Matplotlib e Pillow.
