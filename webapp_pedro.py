import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from PIL import Image


cervicalgia_df1 = pd.read_feather('data/cervicalgia_df1.feather')
cervicalgia_df2 = pd.read_feather('data/cervicalgia_df2.feather')
cervicalgia_df3 = pd.read_feather('data/cervicalgia_df3.feather')
cervicalgia_df4 = pd.read_feather('data/cervicalgia_df4.feather')
cervicalgia_im01 = Image.open('data/cervicalgia_im01.png')
cervicalgia_vd = open('data/cervicalgia_vd.mp4', 'rb')

lombalgia_df1 = pd.read_feather('data/lombalgia_df1.feather')
lombalgia_df2 = pd.read_feather('data/lombalgia_df2.feather')
lombalgia_df3 = pd.read_feather('data/lombalgia_df3.feather')
lombalgia_df4 = pd.read_feather('data/lombalgia_df4.feather')
lombalgia_im01 = Image.open('data/lombalgia_im01.png')
lombalgia_vd = open('data/lombalgia_vd.mp4', 'rb')

dor_ombro_df1 = pd.read_feather('data/dor_ombro_df1.feather')
dor_ombro_df2 = pd.read_feather('data/dor_ombro_df2.feather')
dor_ombro_df3 = pd.read_feather('data/dor_ombro_df3.feather')
dor_ombro_df4 = pd.read_feather('data/dor_ombro_df4.feather')
dor_ombro_im01 = Image.open('data/dor_ombro_im01.png')
dor_ombro_vd = open('data/dor_ombro_vd.mp4', 'rb')

oa_joelho_df1 = pd.read_feather('data/oa_joelho_df1.feather')
oa_joelho_df2 = pd.read_feather('data/oa_joelho_df2.feather')
oa_joelho_df3 = pd.read_feather('data/oa_joelho_df3.feather')
oa_joelho_df4 = pd.read_feather('data/oa_joelho_df4.feather')
oa_joelho_im01 = Image.open('data/oa_joelho_im01.png')
oa_joelho_vd = open('data/oa_joelho_vd.mp4', 'rb')

dor_tornozelo_df1 = pd.read_feather('data/dor_tornozelo_df1.feather')
dor_tornozelo_df2 = pd.read_feather('data/dor_tornozelo_df2.feather')
dor_tornozelo_df3 = pd.read_feather('data/dor_tornozelo_df3.feather')
dor_tornozelo_df4 = pd.read_feather('data/dor_tornozelo_df4.feather')
dor_tornozelo_im01 = Image.open('data/dor_tornozelo_im01.png')
dor_tornozelo_vd = open('data/dor_tornozelo_vd.mp4', 'rb')

entorse_tornozelo_df1 = pd.read_feather('data/entorse_tornozelo_df1.feather')
entorse_tornozelo_df2 = pd.read_feather('data/entorse_tornozelo_df2.feather')
entorse_tornozelo_df3 = pd.read_feather('data/entorse_tornozelo_df3.feather')
entorse_tornozelo_df4 = pd.read_feather('data/entorse_tornozelo_df4.feather')
entorse_tornozelo_im01 = Image.open('data/entorse_tornozelo_im01.png')
entorse_tornozelo_vd = open('data/entorse_tornozelo_vd.mp4', 'rb')


st.title('Ci??ncia e Fisioterapia Ortop??dica')

st.subheader('An??lise quantitativa e qualitativa na base de dados PEDro')

st.write('''
         A qualidade das publica????es cient??ficas ?? um tema de crescente interesse, devido a populariza????o de uma abordagem de tratamentos 
         baseada em evid??ncia. Apesar do n??mero crescente dos artigos cient??ficos (principalmente nas ultimas 2 decadas), discute-se a 
         validade de tais estudos para sustentar as condutas terapeuticas, assim surgem debates sobre a maneira mais adequada de promover o 
         tratamento fisioterapeutico.
         
         Para investigar o n??vel de produ????o cient??fica na fisioterapia ortop??dica, em alguns temas mais relevantes, foram utilizados 
         dados da Phyisioterapy Evidence Database (PEDro), uma base de dados que re??ne, organiza e avalia a qualidade metodol??gica de 
         artigos cient??ficos de fisioterapia, abrangendo algumas d??cadas de produ????o cient??fica (mais comumente a partir da decada de 1980).
         
         Os dados apresentados foram coletados utilizando a biblioteca ***__SELENIUM__*** e ap??s a extra????o dos dados e caracter??sticas
         dos estudos os dados foram limpos, organizados e analisados utilizando bibliotecas padr??o de an??lise de dados, como ***__PANDAS__*** e
         ***__NUMPY__***. Tamb??m foi necess??rio o uso de bibliotecas de processamento de texto como ***__NLTK__*** e ***__RE(REGEX)__***. 
         Para a visualiza????o dos dados foram utilizadas as bibliotecas ***__MATPLOTLIB__***, ***__PLOTLY__***, ***__WORDCLOUD__*** e ***__BAR_CHART_RACE__***.
         ''')

st.subheader("TEMAS")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["__Cervicalgia__", "__Lombalgia__", "__Dor em Ombro__", "__Osteoartrose de Joelho__", 
                                              "__Dor em Tornozelo__", "__Entorse de Tornozelo__"])


with tab1:
    st.header('__CERVICALGIA__')
    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=cervicalgia_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'CERVICALGIA ({cervicalgia_df1["ano"].min()} - 2022): {cervicalgia_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=cervicalgia_df2, x="escala pedro", histnorm='percent', 
                        title=f'CERVICALGIA ({cervicalgia_df2["ano"].min()} - 2022): Qualidade de {cervicalgia_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    
    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')

    fig3 = px.bar(cervicalgia_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"CERVICALGIA: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=cervicalgia_df4['decada'],
        y=cervicalgia_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=cervicalgia_df4['decada'],
        y=cervicalgia_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"CERVICALGIA ({cervicalgia_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({cervicalgia_df1["ano"].min()}-2022)')
    st.image(cervicalgia_im01)

    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1990-2022)')
    st.video(cervicalgia_vd)



with tab2:
    st.header('__LOMBALGIA__')
    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=lombalgia_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'LOMBALGIA ({lombalgia_df1["ano"].min()} - 2022): {lombalgia_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=lombalgia_df2, x="escala pedro", histnorm='percent', 
                        title=f'LOMBALGIA ({lombalgia_df2["ano"].min()} - 2022): Qualidade de {lombalgia_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)


    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')

    fig3 = px.bar(lombalgia_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"LOMBALGIA: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=lombalgia_df4['decada'],
        y=lombalgia_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=lombalgia_df4['decada'],
        y=lombalgia_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"LOMBALGIA ({lombalgia_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({lombalgia_df1["ano"].min()}-2022)')
    st.image(lombalgia_im01)


    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1980-2022)')
    st.video(lombalgia_vd)


with tab3:
    st.header('__DOR EM OMBRO__')
    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=dor_ombro_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'DOR OMBRO ({dor_ombro_df1["ano"].min()} - 2022): {dor_ombro_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=dor_ombro_df2, x="escala pedro", histnorm='percent', 
                        title=f'DOR OMBRO ({dor_ombro_df2["ano"].min()} - 2022): Qualidade de {dor_ombro_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    
    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')
    
    fig3 = px.bar(dor_ombro_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"DOR OMBRO: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=dor_ombro_df4['decada'],
        y=dor_ombro_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=dor_ombro_df4['decada'],
        y=dor_ombro_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"DOR OMBRO ({dor_ombro_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({dor_ombro_df1["ano"].min()}-2022)')
    st.image(dor_ombro_im01)


    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1990-2022)')
    st.video(dor_ombro_vd)
    
    
with tab4:
    st.header('__OA JOELHO__')
    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=oa_joelho_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'OA JOELHO ({oa_joelho_df1["ano"].min()} - 2022): {oa_joelho_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=oa_joelho_df2, x="escala pedro", histnorm='percent', 
                        title=f'OA JOELHO ({oa_joelho_df2["ano"].min()} - 2022): Qualidade de {oa_joelho_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    
    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')

    fig3 = px.bar(oa_joelho_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"OA JOELHO: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=oa_joelho_df4['decada'],
        y=oa_joelho_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=oa_joelho_df4['decada'],
        y=oa_joelho_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"OA JOELHO ({oa_joelho_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({oa_joelho_df1["ano"].min()}-2022)')
    st.image(oa_joelho_im01)

    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1990-2022)')
    st.video(oa_joelho_vd)


with tab5:
    st.header('__DOR TORNOZELO__')

    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=dor_tornozelo_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'DOR TORNOZELO ({dor_tornozelo_df1["ano"].min()} - 2022): {dor_tornozelo_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=dor_tornozelo_df2, x="escala pedro", histnorm='percent', 
                        title=f'DOR TORNOZELO ({dor_tornozelo_df2["ano"].min()} - 2022): Qualidade de {dor_tornozelo_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    
    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')

    fig3 = px.bar(dor_tornozelo_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"DOR TORNOZELO: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=dor_tornozelo_df4['decada'],
        y=dor_tornozelo_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=dor_tornozelo_df4['decada'],
        y=dor_tornozelo_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"DOR TORNOZELO ({dor_tornozelo_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({dor_tornozelo_df1["ano"].min()}-2022)')
    st.image(dor_tornozelo_im01)


    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1990-2022)')
    st.video(dor_tornozelo_vd)
    

with tab6:
    st.header('__ENTORSE TORNOZELO__')
    st.subheader('Quantidade de estudos')

    fig = px.line(data_frame=entorse_tornozelo_df1, x="ano", y="quantidade", color="tipo estudo", 
                title=f'ENTORSE TORNOZELO ({entorse_tornozelo_df1["ano"].min()} - 2022): {entorse_tornozelo_df1["quantidade"].sum()} estudos')

    fig.update_layout(
        title_font=dict(size=18),
        xaxis_title="",
        yaxis_title="Quantidade",
        legend_title='Tipo de estudo',
        legend=dict(y=0.87, x=0.0775),
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade Metodol??gica dos Ensaios Cl??nicos')
    st.write('''
            Para mensurar a qualidade dos ensaios cl??nicos foi proposta a ***__Escala PEDro__***, um instrumento
            que avalia caracter??sticas necess??rias para que um estudo possa ser considerado metodol??gicamente adequado, 
            consequentemente seus resultados e conclus??es s??o mais confi??veis.
            A escala tem pontua????o m??xima de 10 e m??nima de 0, sendo que estudos com pontua????o mais alta indicam estudos
            com melhores metodologias. 
            ''')

    fig2 = px.histogram(data_frame=entorse_tornozelo_df2, x="escala pedro", histnorm='percent', 
                        title=f'ENTORSE TORNOZELO ({entorse_tornozelo_df2["ano"].min()} - 2022): Qualidade de {entorse_tornozelo_df2.shape[0]} ensaios cl??nicos')

    fig2.update_layout(
        title_font=dict(size=18),
        xaxis_title="Pontua????o na Escala PEDro",
        yaxis_title="Porcentagem (%)",
        width=810, height=500,
        font=dict(size=13))

    st.plotly_chart(fig2, theme='streamlit', use_container_width=True)
    
    
    st.write('''
             Nessa an??lise foi estipulado que ensaios cl??nicos com nota at?? 6 eram considerados de baixa qualidade 
             metodol??gica, e os com nota 7 ou mais foram considerados de alta qualidade metodol??gica.
             ''')

    fig3 = px.bar(entorse_tornozelo_df3, x='decada', y='quantidade', 
                color='qualidade' , color_discrete_sequence=["red", "blue"],
                title=f"ENTORSE TORNOZELO: Qualidade dos ensaios cl??nicos")

    fig3.update_layout(
        title_font=dict(size=18),
        legend_title='',
        legend=dict(y=0.78, x=0.085),
        xaxis_title="",
        yaxis_title="Quantidade",
        width=810, height=500,
        font=dict(size=13)
        )

    st.plotly_chart(fig3, theme='streamlit', use_container_width=True)


    st.subheader('Qualidade vs Quantidade (Ensaios Cl??nicos)')

    fig4 = make_subplots(rows=2, cols=1,
                        subplot_titles=("Quantidade por d??cada","Nota Escala PEDro (Mediana)"))

    fig4.append_trace(go.Scatter(
        x=entorse_tornozelo_df4['decada'],
        y=entorse_tornozelo_df4['quantidade'],
    ), row=1, col=1)

    fig4.append_trace(go.Scatter(
        x=entorse_tornozelo_df4['decada'],
        y=entorse_tornozelo_df4['escala pedro'],
    ), row=2, col=1)

    fig4.update_layout(height=500, width=810, showlegend=False, 
                    title_text=f"ENTORSE TORNOZELO ({entorse_tornozelo_df1['ano'].min()} - 2022)")

    st.plotly_chart(fig4, theme='streamlit', use_container_width=True)


    st.header('Temas e termos mais frequentes nos t??tulos')
    st.subheader(f'Ensaios Cl??nicos ({entorse_tornozelo_df1["ano"].min()}-2022)')
    st.image(entorse_tornozelo_im01)


    st.text("")
    st.header('Temas e termos de interesse de pesquisa')
    st.subheader('Ensaios Cl??nicos (1990-2022)')
    st.video(entorse_tornozelo_vd)