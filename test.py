import streamlit as st
import streamlit.components.v1 as components



st.image('https://futureoflife.org/wp-content/uploads/2017/01/artificial_intelligence_benefits_risk-1400x430.jpg')
st.title("TURBO KI: 3D-TSNE")

st.text("CONVOLUTIONAL LAYER 1")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\CONV_1.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 2")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\CONV_2.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 3")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\CONV_3.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 4")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\CONV_4.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("CONVOLUTIONAL LAYER 5")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\CONV_5.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("DENSE LAYER 1")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\Dense_1.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)

st.text("DENSE LAYER 2")

HtmlFile = open(r"C:\Users\Sebastian\Dropbox\10_FEP\04_Gruppe_KI\50_TSNE\TSNE_Daten_02_11\Versuch_3\Dense_2.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
print(source_code)
components.html(source_code, height = 500)