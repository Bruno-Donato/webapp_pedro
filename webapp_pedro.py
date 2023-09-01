import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from PIL import Image
from plotly.subplots import make_subplots

quali_metod = '''
            Para mensurar a qualidade dos ensaios clínicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia características necessárias para que um estudo possa ser considerado metodológicamente adequado, 
            consequentemente seus resultados e conclusões são mais confiáveis.
            
            A escala tem pontuação máxima de 10 e mínima de 0, sendo que estudos com pontuação mais alta indicam estudos
            com melhores metodologias.
            
            Nessa análise foi estipulado que ensaios clínicos com nota até 6 eram considerados de baixa qualidade metodológica, 
            e os com nota 7 ou mais foram considerados de alta qualidade metodológica.
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
    fig3 = px.bar(df3, x='decada', y='quantidade', color='qualidade', 
                  color_discrete_sequence=["red", "blue"], title=f"{nome}: Qualidade dos ensaios clínicos")
    fig3.update_layout(title_font=dict(size=18), legend_title='', legend=dict(y=0.78, x=0.085), 
                       xaxis_title="", yaxis_title="Quantidade", width=810, height=500, font=dict(size=13))
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
    st.header('Principais Achados')
    st.write('''
             Apesar de publicações sobre cervicalgias serem feitas desde a década de 1960 (mais de 50 anos) o número de  produções apresentou 
             um salto significativo a partir da década de 2000 com uma queda abrupta por volta de 2020, explicada pela pandemia de Covid.
             
             Tanto a qualidade metodológica quanto o número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir da década 
             de 2020. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica a maior parte dos ensaios clínicos ainda 
             apresentaram baixa qualidade metodológica.
                          
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de cervicalgias e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, tendo terapias 
             e recursos passivos, como acupuntura, quiropraxia e terapia manual em maior número de publicações na década de 1990 passando para 
             abordagens baseadas em exercícios e treinamento a partir da década de 2000.
             
             As cervicalgias crônicas se mantiveram objeto de estudo por todo o período mas por volta da década de 2010 os estudos nas cervigalgias 
             definidas como "não específicas" ganharam força e espaço na pesquisa.
             
             No total menos de 40% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de cervicalgias. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.           
             ''')

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
    st.header('Principais Achados')
    st.write('''
             As publicações abordando lombalgias existem há mais de 50 anos e apresentou aumento do número de produções a partir da década de 
             2000 com uma queda abrupta por volta de 2020, explicada pela pandemia de Covid.
             
             Tanto a qualidade metodológica quanto o número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir 
             da década de 2000. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica a maior parte dos 
             ensaios clínicos ainda apresentaram baixa qualidade metodológica.
             
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de lombalgias e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, tendo terapias 
             e recursos passivos, como estimulação elétrica, acupuntura, quiropraxia e terapia manual em maior número de publicações na década de 
             1980 juntamente as escolas de exercício e abordagens baseadas em exercícios a partir da década de 1990. Na década de 2000 a acupuntura 
             retorna ao cenário dividindo espaço com abordagens baseadas em exercícios e treinamento e há o aparecimento das abordagens com educação. 
             Já na década de 2010 o tema estabilização e core se mostram presentes e a partir daí o exercício parece ser o recurso mais abordado.  
             
             As lombalgias crônicas se mantiveram objeto de estudo por todo o período e por volta da década de 2000 os estudos nas lombalgias 
             agudas ganham força. As lombalgias definidas como "não específicas" foram foco de pesquisas também nesse período ganhando espaço 
             a partir de 2010.
             
             No total menos de 30% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de lombalgias. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.          
             ''')

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
    st.header('Principais Achados')
    st.write('''
             As publicações abordando dor em ombro são mais recentes, a partir de 1974, e apresentou aumento do número de produções 
             a partir da década de 2000 com uma queda abrupta por volta de 2020, explicada pela pandemia de Covid.
             
             Tanto a qualidade metodológica quanto o número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir 
             da década de 2000. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica a maior parte dos 
             ensaios clínicos ainda apresentaram baixa qualidade metodológica.
                          
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de dores no ombro e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, tendo terapias 
             e recursos passivos, como estimulação elétrica e bloqueios em maior número de publicações no início da década de 1990 mudando para 
             exercício, estimulação e cirurgia na segunda metade da década. A acupuntura e exercício são foco principal no início da década de 2000
             e o exercício se mantém principal tema de estudo desde então. A partir da década de 2010 há uma abordagem de patologias e condições 
             como sindrome de dor subacromial e do impacto.
             
             Dores em ombro com origem cervical parecem apresentar maior interesse de estudo até os anos 2000 e a partir daí o foco das pesquisas 
             parece focar nos estudos de condições e definições mais pontuais na própria região e estruturas da articulação do ombro.             
             
             No total por volta de 35% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de dor no ombro. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.
             ''')
    
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
    st.header('Principais Achados')
    st.write('''
             As publicações abordando OA de joelho existem há mais de 50 anos e apresentou aumento do número de produções a partir da década de 
             2000 com uma queda abrupta por volta de 2020, explicada pela pandemia de Covid.
             
             O número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir da década de 2000 enquanto que a qualidade metodológica 
             teve queda nas decadas 1970/80 com posterior aumento. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica 
             a partir da década de 2000 a maior parte dos ensaios clínicos ainda apresentaram baixa qualidade metodológica.
                          
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de OA de joelho e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, tendo terapias 
             e recursos passivos, como estimulação elétrica e a artroplastia no início da década de 1990 mudando rapidamente na segunda metade da decada 
             para exercício que se manteve dali em diante. A acupuntura ganhou espaço no início dos anos 2000 porém as abordagens focadas em fortalecimento 
             e exercício foram o principal tema de estudo.
             
             No total por volta de 35% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de OA de joelho. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.            
             ''')

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
    st.header('Principais Achados')
    st.write('''
             As publicações abordando dor em tornozelo apresentou flutuação no número de trabalhos porém com tendência de aumento a partir da 
             década de 1990 e posteior diminuição, principalmente por volta de 2020, explicada pela pandemia de Covid.
             
             Tanto a qualidade metodológica quanto o número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir 
             da década de 2000. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica a partir da década de 
             2000 a maior parte dos ensaios clínicos ainda apresentaram baixa qualidade metodológica.
                          
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de entorse de tornozelo e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, lesões ligamentares 
             agudas e tratamento com bandagens como foco de pesquisa no início da decada de 1990 e na segunda metade da década o interesse em fraturas esteve 
             presente. Já no início da década de 2000 patologias crônicas e condições relacionadas ao tendão de aquiles juntamente com abordagens com exercícios 
             e acupuntura ganham espaço e após esse período os entorses são foco de estudo. A partir da década de 2010 os estudos investigando a fasciite plantar 
             e abordagens com exercício e funcionalidade são o foco de estudo.
             
             No total por volta de 30% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de dores no tornozelo. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.
             ''')
    
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
    bar_quali(df3=entorse_tornozelo_df3, nome='Entorse Tornozelo')
    st.subheader('Qualidade vs Quantidade (Ensaios Clínicos)')
    linha_quali_quant(df4=entorse_tornozelo_df4, df1=entorse_tornozelo_df1, nome='Entorse Tornozelo')
    st.header('Temas e termos mais frequentes nos títulos')
    st.subheader(f'Ensaios Clínicos ({entorse_tornozelo_df1["ano"].min()}-2022)')
    st.image(entorse_tornozelo_im01)
    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Clínicos (1990-2022)')
    st.video(entorse_tornozelo_vd)
    st.header('Principais Achados')
    st.write('''
             As publicações abordando entorse de tornozelo apresentam menor número e demonstram flutuação no número de trabalhos a partir da década 
             de 2000 com pico de produção na segunda metade de 2000 e posteior diminuição e flutuação, principalmente por volta de 2020, explicada 
             pela pandemia de Covid.
             
             Tanto a qualidade metodológica quanto o número de ensaios clínicos apresentou aumento contínuo por década, tendo maior pico a partir da década 
             de 2000. Apesar de haver um aumento relevante do número de publicações com alta qualidade metodológica a partir da década de 2000 a 
             maior parte dos ensaios clínicos ainda apresentaram baixa qualidade metodológica.
                          
             Visualizando os termos nos títulos das publicações pela nuvem de palavras é possível identificar os temas mais estudados para 
             tratamento de entorse de tornozelo e com o vídeo podemos ver uma mudança no paradigma de pesquisa com o passar das décadas, tendo terapias 
             e recursos passivos, bandagens e imobilizações em maior número de publicações no início da década de 1990, e a acupuntura aparecendo 
             na segunda metade da década tendo grande visibilidade até a primeira metade da década de 2000. A partir daí as dores agudas e foco na 
             abordagem ativa com exercícios de equilíbrio e fortalecimento começam a aparecer e as condições de instabilidade crônicas também foram 
             interesse de pesquisa.
             
             No total menos de 25% dos ensaios clínicos apresentaram alta qualidade metodológica, mostrando que a maior parte das evidências 
             produzidas não são adequadas para fundamentar condutas terapêuticas para tratamento de entorse no tornozelo. 
             
             Dessa forma é evidente a necessidade de um preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico 
             e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos 
             alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.
             ''')