import streamlit as st
import streamlit.components.v1 as components



st.image('https://futureoflife.org/wp-content/uploads/2017/01/artificial_intelligence_benefits_risk-1400x430.jpg')
st.title("TURBO KI: 3D-TSNE")

st.text("Eingabelayer")

HtmlFile = open('./Eingabelayer.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 1")

HtmlFile = open('./CONV_1.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 2")

HtmlFile = open('./CONV_2.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 3")

HtmlFile = open('./CONV_3.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 4")

HtmlFile = open('./CONV_4.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 5")

HtmlFile = open('./CONV_5.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("DENSE LAYER 1")

HtmlFile = open('./Dense_1.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("DENSE LAYER 2")

HtmlFile = open('./Dense_2.html', 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)
