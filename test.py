import streamlit as st
import streamlit.components.v1 as components

Dateipfad_Versuch3 = "./"
Dateipfad_Versuch4 = "./200/"

perplexity_list = [30, 200]

st.image('https://futureoflife.org/wp-content/uploads/2017/01/artificial_intelligence_benefits_risk-1400x430.jpg')
st.title("TURBO KI: 3D-TSNE")

st.sidebar.header('Auswahl der Perplexity')
selected_perplexity = st.sidebar.selectbox('Perplexity', perplexity_list)

if selected_perplexity == 30:

    st.markdown(
        'Dargestellt sind die Ergebnisse der 3D Tsne Dimensionsreduktion der einzelnen Layer mit einer Perplexity von **30**: ')
    st.text("Eingabelayer")

    HtmlFile = open(Dateipfad_Versuch3 + 'Eingabelayer.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 1")

    HtmlFile = open(Dateipfad_Versuch3 + 'CONV_1.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 2")

    HtmlFile = open(Dateipfad_Versuch3 + 'CONV_2.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 3")

    HtmlFile = open(Dateipfad_Versuch3 + 'CONV_3.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 4")

    HtmlFile = open(Dateipfad_Versuch3 + 'CONV_4.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 5")

    HtmlFile = open(Dateipfad_Versuch3 + 'CONV_5.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("DENSE LAYER 1")

    HtmlFile = open(Dateipfad_Versuch3 + 'Dense_1.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("DENSE LAYER 2")

    HtmlFile = open(Dateipfad_Versuch3 + 'Dense_2.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

else:

    st.markdown(
        'Dargestellt sind die Ergebnisse der 3D Tsne Dimensionsreduktion der einzelnen Layer mit einer Perplexity von **200**: ')
    st.text("Eingabelayer")

    HtmlFile = open(Dateipfad_Versuch4 + 'Eingabelayer.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 1")

    HtmlFile = open(Dateipfad_Versuch4 + 'CONV_1.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 2")

    HtmlFile = open(Dateipfad_Versuch4 + 'CONV_2.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 3")

    HtmlFile = open(Dateipfad_Versuch4 + 'CONV_3.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 4")

    HtmlFile = open(Dateipfad_Versuch4 + 'CONV_4.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("CONVOLUTIONAL LAYER 5")

    HtmlFile = open(Dateipfad_Versuch4 + 'CONV_5.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("DENSE LAYER 1")

    HtmlFile = open(Dateipfad_Versuch4 + 'Dense_1.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)

    st.text("DENSE LAYER 2")

    HtmlFile = open(Dateipfad_Versuch4 + 'Dense_2.html', 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    print(source_code)
    components.html(source_code, height=500)
