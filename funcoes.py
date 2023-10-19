import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import spacy

from plotly.subplots import make_subplots
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def graf_linha_tempo(df1=None, nome=None):
    fig = px.line(
        data_frame=df1, x="ano", y="quantidade", color="tipo estudo", 
        title=f'{nome} ({df1["ano"].min()} - 2022): {df1["quantidade"].sum()} estudos'
    )
    fig.update_layout(title_font=dict(size=18), xaxis_title="", 
                      yaxis_title="Quantidade", legend_title='Tipo de estudo', 
                      legend=dict(y=0.87, x=0.0775),  width=810, 
                      height=500, font=dict(size=13))
    return st.plotly_chart(fig, theme='streamlit', use_container_width=True)

def histograma(df2=None, nome=None):
    fig2 = px.histogram(
        data_frame=df2, x="escala pedro", histnorm='percent', 
        title=f'{nome} ({df2["ano"].min()} - 2022): Qualidade de {df2.shape[0]} ensaios clínicos'
    )
    fig2.update_layout(title_font=dict(size=18), 
                       xaxis_title="Pontuação na Escala PEDro",
                       yaxis_title="Porcentagem (%)", width=810, height=500, 
                       font=dict(size=13))
    return st.plotly_chart(fig2, theme='streamlit', use_container_width=True)

def bar_quali(df3=None, nome=None):
    fig3 = px.bar(df3, x='decada', y='quantidade', color='qualidade', 
                  color_discrete_sequence=["red", "blue"], 
                  title=f"{nome}: Qualidade dos ensaios clínicos")
    fig3.update_layout(title_font=dict(size=18), legend_title='', 
                       legend=dict(y=0.78, x=0.085), xaxis_title="Década", 
                       yaxis_title="Quantidade", width=810, height=500, 
                       font=dict(size=13))
    return st.plotly_chart(fig3, theme='streamlit', use_container_width=True)

def linha_quali_quant(df4=None, df1=None, nome=None):
    fig4 = make_subplots(rows=2, cols=1,
                         subplot_titles=("Quantidade por década","Nota Escala PEDro (Mediana)"))
    fig4.append_trace(go.Scatter(x=df4['decada'], y=df4['quantidade'],
                                 ), row=1, col=1)
    fig4.append_trace(go.Scatter(x=df4['decada'], y=df4['escala pedro'],
                                 ), row=2, col=1)
    fig4.update_layout(height=500, width=810, showlegend=False, 
                       title_text=f"{nome} ({df1['ano'].min()} - 2022)")
    return st.plotly_chart(fig4, theme='streamlit', use_container_width=True)

def similaridade_cosseno(modelo_spacy: spacy.load, titulo: str, 
                         titulos: list, min_ngram: int, max_ngram: int,
                         lemma: bool = True):
    """
    Calcula a similaridade de cosseno entre um título de referência 
    e uma lista de títulos.

    Args:
        modelo_spacy (spacy.load): O modelo de processamento spaCy a ser 
            aplicado aos títulos.
        titulo (str): O título de referência.
        titulos (list): Uma lista de títulos a serem comparados com o título 
            de referência.
        min_ngram (int): O tamanho mínimo do n-gram utilizado na vetorização 
            TF-IDF.
        max_ngram (int): O tamanho máximo do n-gram utilizado na vetorização 
            TF-IDF.
        lemma (bool, optional): Se True, utiliza os lemas das palavras nos 
            títulos; se False, utiliza o texto original das palavras. O 
            padrão é True.
        
    Returns:
        float: Uma lista de similaridades de cosseno entre o título 
        de referência e os títulos da lista.
    """
    titulo_lower = titulo.lower()
    doc = modelo_spacy(titulo_lower)
    
    if lemma:
        tokens = [token.lemma_ for token in doc 
                  if not token.is_stop and not token.is_punct]
    else:
        tokens = [token.text for token in doc 
                  if not token.is_stop and not token.is_punct]
    
    titulo_limpo = " ".join(tokens)

    tfidf_vec = TfidfVectorizer(ngram_range=(min_ngram, max_ngram))
    titulos_tfidf = tfidf_vec.fit_transform([titulo_limpo] + titulos)

    similaridade = cosine_similarity(titulos_tfidf)

    return similaridade[0, 1:]

