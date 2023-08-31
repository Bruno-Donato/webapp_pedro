import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image

quali_metod = '''
            Para mensurar a qualidade dos ensaios clínicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia características necessárias para que um estudo possa ser considerado metodológicamente adequado, 
            consequentemente seus resultados e conclusões são mais confiáveis.
            A escala tem pontuação máxima de 10 e mínima de 0, sendo que estudos com pontuação mais alta indicam estudos
            com melhores metodologias. 
            '''
            
crit_analisis = '''
             Nessa análise foi estipulado que ensaios clínicos com nota até 6 eram considerados de baixa qualidade 
             metodológica, e os com nota 7 ou mais foram considerados de alta qualidade metodológica.
             '''

def graf_linha_tempo(df1=None, nome=None):
    fig = px.line(data_frame=df1, x="ano", y="quantidade", color="tipo estudo", 
                    title=f'{nome} ({df1["ano"].min()} - 2022): {df1["quantidade"].sum()} estudos')
    fig.update_layout(title_font=dict(size=18), xaxis_title="", yaxis_title="Quantidade",
                      legend_title='Tipo de estudo', legend=dict(y=0.87, x=0.0775), 
                      width=810, height=500, font=dict(size=13))
    return st.plotly_chart(fig, theme='streamlit', use_container_width=True)

def histograma(df2=None, nome=None):
    fig2 = px.histogram(data_frame=df2, x="escala pedro", histnorm='percent', 
                        title=f'{nome} ({df2["ano"].min()} - 2022): Qualidade de {df2.shape[0]} ensaios clínicos')
    fig2.update_layout(title_font=dict(size=18),xaxis_title="Pontuação na Escala PEDro",
                       yaxis_title="Porcentagem (%)", width=810, height=500, font=dict(size=13))
    return st.plotly_chart(fig2, theme='streamlit', use_container_width=True)

def bar_quali(df3=None, nome=None):
    fig3 = px.bar(df3, x='decada', y='quantidade', 
                  color='qualidade' , color_discrete_sequence=["red", "blue"],
                  title=f"{nome}: Qualidade dos ensaios clínicos")
    fig3.update_layout(title_font=dict(size=18), legend_title='',
                       legend=dict(y=0.78, x=0.085), xaxis_title="",
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
    
st.title('Ciência e Fisioterapia Ortopédica')
st.subheader('Análise quantitativa e qualitativa na base de dados PEDro')
st.write('''
         A qualidade das publicações científicas é um tema de crescente interesse, devido a popularização de uma abordagem de tratamentos 
         baseada em evidência. Apesar do número crescente dos artigos científicos (principalmente nas ultimas 2 decadas), discute-se a 
         validade de tais estudos para sustentar as condutas terapeuticas, assim surgem debates sobre a maneira mais adequada de promover o 
         tratamento fisioterapeutico.
         
         Para investigar o nível de produção científica na fisioterapia ortopédica, em alguns temas mais relevantes, foram utilizados 
         dados da Phyisioterapy Evidence Database (PEDro), uma base de dados que reúne, organiza e avalia a qualidade metodológica de 
         artigos científicos de fisioterapia, abrangendo algumas décadas de produção científica (mais comumente a partir da decada de 1980).
         
         Os dados apresentados foram coletados utilizando a biblioteca ***__SELENIUM__*** e após a extração dos dados e características
         dos estudos os dados foram limpos, organizados e analisados utilizando bibliotecas padrão de análise de dados, como ***__PANDAS__*** e
         ***__NUMPY__***. Também foi necessário o uso de bibliotecas de processamento de texto como ***__NLTK__*** e ***__RE(REGEX)__***. 
         Para a visualização dos dados foram utilizadas as bibliotecas ***__MATPLOTLIB__***, ***__PLOTLY__***, ***__WORDCLOUD__*** e ***__BAR_CHART_RACE__***.
         ''')
st.subheader("TEMAS")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["__Cervicalgia__", "__Lombalgia__", "__Dor em Ombro__", "__Osteoartrose de Joelho__", 
                                              "__Dor em Tornozelo__", "__Entorse de Tornozelo__"])

with tab1:
    cervicalgia_df1 = pd.read_feather('data/cervicalgia_df1.feather')
    cervicalgia_df2 = pd.read_feather('data/cervicalgia_df2.feather')
    cervicalgia_df3 = pd.read_feather('data/cervicalgia_df3.feather')
    cervicalgia_df4 = pd.read_feather('data/cervicalgia_df4.feather')
    cervicalgia_im01 = Image.open('data/cervicalgia_im01.png')
    cervicalgia_vd = open('data/cervicalgia_vd.mp4', 'rb')
    st.header('__CERVICALGIA__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=cervicalgia_df1, nome='Cervicalgia')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=cervicalgia_df2, nome='Cervicalgia')
    st.write(crit_analisis)
    bar_quali(df3=cervicalgia_df3, nome='Cervicalgia')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=cervicalgia_df4, df1=cervicalgia_df1, nome='Cervicalgia')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({cervicalgia_df1["ano"].min()}-2022)')
    st.image(cervicalgia_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(cervicalgia_vd)

with tab2:
    lombalgia_df1 = pd.read_feather('data/lombalgia_df1.feather')
    lombalgia_df2 = pd.read_feather('data/lombalgia_df2.feather')
    lombalgia_df3 = pd.read_feather('data/lombalgia_df3.feather')
    lombalgia_df4 = pd.read_feather('data/lombalgia_df4.feather')
    lombalgia_im01 = Image.open('data/lombalgia_im01.png')
    lombalgia_vd = open('data/lombalgia_vd.mp4', 'rb')
    st.header('__LOMBALGIA__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=lombalgia_df1, nome='Lombalgia')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=lombalgia_df2, nome='Lombalgia')
    st.write(crit_analisis)
    bar_quali(df3=lombalgia_df3, nome='Lombalgia')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=lombalgia_df4, df1=lombalgia_df1, nome='Lombalgia')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({lombalgia_df1["ano"].min()}-2022)')
    st.image(lombalgia_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1980-2022)')
    st.video(lombalgia_vd)

with tab3:
    dor_ombro_df1 = pd.read_feather('data/dor_ombro_df1.feather')
    dor_ombro_df2 = pd.read_feather('data/dor_ombro_df2.feather')
    dor_ombro_df3 = pd.read_feather('data/dor_ombro_df3.feather')
    dor_ombro_df4 = pd.read_feather('data/dor_ombro_df4.feather')
    dor_ombro_im01 = Image.open('data/dor_ombro_im01.png')
    dor_ombro_vd = open('data/dor_ombro_vd.mp4', 'rb')
    st.header('__DOR EM OMBRO__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=dor_ombro_df1, nome='Dor Ombro')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=dor_ombro_df2, nome='Dor Ombro')
    st.write(crit_analisis)
    bar_quali(df3=dor_ombro_df3, nome='Dor Ombro')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=dor_ombro_df4, df1=dor_ombro_df1, nome='Dor Ombro')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({dor_ombro_df1["ano"].min()}-2022)')
    st.image(dor_ombro_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(dor_ombro_vd)
    
with tab4:
    oa_joelho_df1 = pd.read_feather('data/oa_joelho_df1.feather')
    oa_joelho_df2 = pd.read_feather('data/oa_joelho_df2.feather')
    oa_joelho_df3 = pd.read_feather('data/oa_joelho_df3.feather')
    oa_joelho_df4 = pd.read_feather('data/oa_joelho_df4.feather')
    oa_joelho_im01 = Image.open('data/oa_joelho_im01.png')
    oa_joelho_vd = open('data/oa_joelho_vd.mp4', 'rb')
    st.header('__OA JOELHO__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=oa_joelho_df1, nome='OA Joelho')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=oa_joelho_df2, nome='OA Joelho')
    st.write(crit_analisis)
    bar_quali(df3=oa_joelho_df3, nome='OA Joelho')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=oa_joelho_df4, df1=oa_joelho_df1, nome='OA Joelho')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({oa_joelho_df1["ano"].min()}-2022)')
    st.image(oa_joelho_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(oa_joelho_vd)

with tab5:   
    dor_tornozelo_df1 = pd.read_feather('data/dor_tornozelo_df1.feather')
    dor_tornozelo_df2 = pd.read_feather('data/dor_tornozelo_df2.feather')
    dor_tornozelo_df3 = pd.read_feather('data/dor_tornozelo_df3.feather')
    dor_tornozelo_df4 = pd.read_feather('data/dor_tornozelo_df4.feather')
    dor_tornozelo_im01 = Image.open('data/dor_tornozelo_im01.png')
    dor_tornozelo_vd = open('data/dor_tornozelo_vd.mp4', 'rb')
    st.header('__DOR TORNOZELO__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=dor_tornozelo_df1, nome='Dor Tornozelo')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=dor_tornozelo_df2, nome='Dor Tornozelo')
    st.write(crit_analisis)
    bar_quali(df3=dor_tornozelo_df3, nome='Dor Tornozelo')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=dor_tornozelo_df4, df1=dor_tornozelo_df1, nome='Dor Tornozelo')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({dor_tornozelo_df1["ano"].min()}-2022)')
    st.image(dor_tornozelo_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(dor_tornozelo_vd)
    
with tab6:   
    entorse_tornozelo_df1 = pd.read_feather('data/entorse_tornozelo_df1.feather')
    entorse_tornozelo_df2 = pd.read_feather('data/entorse_tornozelo_df2.feather')
    entorse_tornozelo_df3 = pd.read_feather('data/entorse_tornozelo_df3.feather')
    entorse_tornozelo_df4 = pd.read_feather('data/entorse_tornozelo_df4.feather')
    entorse_tornozelo_im01 = Image.open('data/entorse_tornozelo_im01.png')
    entorse_tornozelo_vd = open('data/entorse_tornozelo_vd.mp4', 'rb')
    st.header('__ENTORSE TORNOZELO__')
    st.subheader('Quantidade de estudos')
    graf_linha_tempo(df1=entorse_tornozelo_df1, nome='Entorse Tornozelo')
    st.subheader('Qualidade Metodológica dos Ensaios Clínicos')
    st.write(quali_metod)
    histograma(df2=entorse_tornozelo_df2, nome='Entorse Tornozelo')
    st.write(crit_analisis)
    bar_quali(df3=entorse_tornozelo_df3, nome='Entorse Tornozelo')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=entorse_tornozelo_df4, df1=entorse_tornozelo_df1,nome='Entorse Tornozelo')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({entorse_tornozelo_df1["ano"].min()}-2022)')
    st.image(entorse_tornozelo_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(entorse_tornozelo_vd)