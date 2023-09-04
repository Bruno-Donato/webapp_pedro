# Investigação da qualidade da evidência cientifica na fisioterapia ortopédica
![Pedro Logo](https://github.com/Bruno-Donato/webapp_pedro/blob/main/data/pedro_logo.png)

## Visão Geral
Nesse projeto, vamos analisar a produção das evidências científicas sobre as principais condições e patologias na especialidade de ortopedia. As publicações analisadas estão disponíveis na [PEDro - Physioterapy Evidence Database](https://pedro.org.au/).

Confira o dashboard interativo com os resultados no link abaixo:
## >>> [Webapp dos Resultados](https://bruno-donato-artigosfisio-pedro.streamlit.app/)

## Problema e Solução
Na área da saúde a prática baseada em evidência (PBE) é uma abordagem que tem como objetivo entregar os melhores resultados para os pacientes de maneira eficaz e segura, e se sustenta por 3 pilares igualmente importantes, sendo eles: 
- Melhor evidência disponível
- Expertise do profissional
- Preferencias do paciente<br>
<br>
Para que a PBE seja viável os profissionais da área precisam encontrar e colocar em prática as publicações científicas sobre os temas referentes á sua área de atuação.
Para os profissionais da fisiotrapia a busca e identificação dessas publicações podem ser feitas em diversos repositórios e bases de dados, mas esse trabalho se tornou mais fácil com a idealização da Physioterapy Evidence Database (PEDro), um repositório especializado reunindo somente artigos de fisioterapia.<br>
<br>
Porém muito se discute sobre a qualidade das publicações e se elas são confiáveis para fundamentar as condutas terapeuticas utilizadas no tratamento dos pacientes.
Nesse projeto analisaremos a quantidade e a qualidade de produções científicas na fisioterapia sobre as principais condições ortopédicas, para responder às seguintes perguntas:<br>
<br>
1.Como se deu a quantidade da produção científica ao longo das décadas?<br>
2.As evidências científicas são confiáveis?<br>
3.Quais os temas de interesse de pesquisa ao longo das décadas?
<br>

## Processo
A linguagem de programação Python e o software VSCode foram utilizados para executar todos os códigos. A primeira etapa consistiu em extrair os dados do site da base de dados PEDro com a tecnica de webscraping utilizando a biblioteca Selenium. Após a aquisição dos dados foi feita análise exploratória com bibliotecas Pandas, Numpy e a partir dos resultados encontrados foram elaboradas visualizações com bibliotecas Matplotlib, Plotly, WordCloud e Bar_Chart_Race para expor os achados de maneira adequada.
Também foram utilizadas as bibliotecas NLTK e RE para processamento de linguagem natural dos títulos dos artigos selecionados. 

## Resultados
As produções científicas apresentam uma grande variação em relação ao número e qualidade de publicações. Isso provavelmente é resultado da relevância do tema e também a disponibilidade de recursos para viabilizar as pesquisas.

* A quantidade de artigos aumentam de maneira relevante a partir da década de 2000 em todas as condições avaliadas, tendo queda abrupta no período da pandemia e Covid.

* A qualidade metodológica das publicações aumenta com o passar das décadas, porém se mantem baixa. 

* O interesse de pesquisa em todas as condições em geral se inicia com foco em intervenções passivas e no decorrer das décadas muda para abordagens ativas. 

* No geral menos de 40% das publicações apresentam alta qualidade metodológica.

## Conclusões
Essa análise se torna importante pois mostra que apesar de o número de evidências científicas na fisioterapia ortopédica apresentar aumento nas últimas décadas infelizmente a qualidade metodólógica se mantém baixa. Dessa forma é evidente a necessidade de um melhor preparo por parte dos alunos em formação e profissionais, com foco em desenvolver maior senso crítico e habilidades necessárias para consumir trabalhos e produções científicas na área da ortopedia. Isso permitiria melhor fundamentação de tratamentos alinhados as melhores evidências científicas para entregar resultados eficazes e seguros para seus pacientes.
