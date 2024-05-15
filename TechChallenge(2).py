#python -m venv techchallenge
#techchallenge/Scripts/activate
#pip install -r requirements.txt
#pip install yfinance
#pip install plotly
#pip install matplotlib
#pip install statsmodels
#streamlit run TechChallenge.py
# ==============================================================================
#Origem dos dados
import yfinance as yf

# Data manipulation
# ==============================================================================
import streamlit as st
import pandas as pd
import numpy as np

from datetime import date
from datetime import timedelta

# Plots
# ==============================================================================
import plotly.graph_objs as go

import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['font.size'] = 10

#Page config
def wide_space_default():
    st.set_page_config(layout='wide')

# ==============================================================================
wide_space_default()

#Gráfico padrão
def cria_grafico( df1, df2, df3, df4, titulo, fixa_data, len_fixa_data):
    if fixa_data ==1 :
      dt_ini = df1.index[-(len_fixa_data):]
    else:
      dt_ini = df1.index[:1]

    dt_ini = dt_ini[0].strftime('%Y-%m-%d')
    List_dt_fim=[]
    List_dt_fim.append(df1.tail(1).index.values)
    if df2.shape[0] != 0 :
      List_dt_fim.append(df2.tail(1).index.values)
    if df3.shape[0] != 0 :
      List_dt_fim.append(df3.tail(1).index.values)
    if df4.shape[0] != 0 :
      List_dt_fim.append(df4.tail(1).index.values)

    df_dt_fim =pd.DataFrame(List_dt_fim)
    dt_fim = df_dt_fim.describe().loc['max'][0]
    dt_fim = pd.to_datetime(str(dt_fim))
    dt_fim.strftime('%Y-%m-%d')

    layout = go.Layout(
                    title = titulo,
                    titlefont = dict(size=20))
    fig = go.Figure(layout=layout)
    fig.add_trace(go.Scatter(x=df1.index.values, y=df1[df1.columns[0]].values,
                    mode='lines',
                    line_color = 'blue',
                    name=df1.columns[0]))
    
    if df2.shape[0] != 0 :
      fig.add_trace(go.Scatter(x=df2.index.values, y=df2[df2.columns[0]].values,
                    mode='lines',
                    line_color = 'red',
                    name=df2.columns[0]))
    
    if df3.shape[0] != 0 :
      fig.add_trace(go.Scatter(x=df3.index.values, y=df3[df3.columns[0]].values,
                    mode='lines',
                    line_color = 'green',
                    name=df3.columns[0]))
       
    if df4.shape[0] != 0 :
      fig.add_trace(go.Scatter(x=df4.index.values, y=df4[df4.columns[0]].values,
                    mode='lines',
                    line_color = 'orange',
                    name=df4.columns[0]))   

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
                        ])
            ),
        range=(dt_ini, dt_fim)
    )
    return fig

st.title('Tech Challenge - DTAT2 - Grupo 56 - Análise Petroleo Brent')
st.image('cabeçalho.jpg')
st.image('Refinaria.jpg')
st.divider()  
st.subheader('Grupo 56')
st.write(":point_right: Denise Oliveira     rm351364")
st.write(":point_right: Fabrício Carraro    rm350902")
st.write(":point_right: Luiz H. Spezzano    rm351120")
st.write(":point_right: Thayze Darnieri     rm349021")
st.divider()  
st.subheader('O Desafio')
st.write("Você foi contratado(a) para uma consultoria, e seu trabalho envolve analisar os dados de preço do petróleo brent, que pode ser encontrado no site do [ipea](http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&amp;serid=1650971490&amp;oper=view). Essa base de dados histórica envolve duas colunas: data e preço (em dólares). Um grande cliente do segmento pediu para que a consultoria desenvolvesse um dashboard interativo e que gere insights relevantes para tomada de decisão. Além disso, solicitaram que fosse desenvolvido um modelo de Machine Learning para fazer o forecasting do preço do petróleo.")

st.write("Seu objetivo é:")
st.write(":black_medium_small_square: Criar um dashboard interativo com ferramentas à sua escolha.")
st.write(":black_medium_small_square: Seu dashboard deve fazer parte de um storytelling que traga insights relevantes sobre a variação do preço do petróleo, como situações geopolíticas, crises econômicas, demanda global por energia e etc. Isso pode te ajudar com seu modelo. É obrigatório que você traga pelo menos 4 insights neste desafio.")
st.write(":black_medium_small_square: Criar um modelo de Machine Learning que faça a previsão do preço do petróleo diariamente (lembre-se de time series). Esse modelo deve estar contemplado em seu storytelling e deve conter o código que você trabalhou, analisando as performances do modelo.")
st.write(":black_medium_small_square: Criar um plano para fazer o deploy em produção do modelo, com as ferramentas que são necessárias.")
st.write(":black_medium_small_square: Faça um MVP do seu modelo em produção utilizando o Streamlit.")

st.divider()  
st.subheader('Notas Iniciais do Grupo')
st.write("Ao invés de utilizarmos o site do IPEA, conforme sugestão do desafio, optamos por utilizar a carga da biblioteca do Yahoo Finance ( https://finance.yahoo.com/ ) pois elimina a necessidade de ter que importar planilha, tornando o código mais versátil")

st.divider()  
st.subheader('Vamos falar de Petróleo!!!')
st.write("É comemorado em 29 de setembro o Dia do Petróleo!! O petróleo é um dos motores da sociedade atual, motivo de guerras e um dos principais responsáveis pelas mudanças climáticas. Todos os dias, são extraídos no mundo mais de 80 milhões de barris de petróleo. Seu nome vem do latim e significa 'óleo de pedra'.")

st.write("O líquido viscoso conhecido como “ouro negro” é uma mistura de hidrocarbonetos — compostos que contêm na sua estrutura molecular, principalmente, carbono e hidrogênio. Ele é o resultado de um processo de transformação ocorrido ao longo de milhões de anos.")

st.write(" **Origem do petróleo** ")

st.write("Há inúmeras teorias sobre o surgimento do petróleo, porém, a mais aceita é que ele surgiu através de restos orgânicos de animais e vegetais depositados no fundo de lagos e mares sofrendo transformações químicas ao longo de milhares de anos. Substância inflamável possui estado físico oleoso e com densidade menor do que a água. Sua composição química é a combinação de moléculas de carbono e hidrogênio (hidrocarbonetos).")

st.write(" **Uso e derivados** ")

st.write("Além de gerar a gasolina, que serve de combustível para grande parte dos automóveis que circulam no mundo, vários produtos são derivados do petróleo como, por exemplo, a parafina, gás natural, GLP, produtos asfálticos, nafta petroquímica, querosene, solventes, óleos combustíveis, óleos lubrificantes, óleo diesel e combustível de aviação.")

st.write(" **Principais características químicas e físicas do petróleo** ")

st.write(":black_medium_small_square: O petróleo é tipicamente encontrado em estado líquido à temperatura ambiente. No entanto, sua consistência pode variar de um líquido fino e volátil a uma substância espessa e viscosa.")
st.write(":black_medium_small_square: A cor do petróleo bruto pode variar de um amarelo palha claro a um preto semelhante a alcatrão, dependendo de sua composição.")
st.write(":black_medium_small_square: O petróleo é geralmente menos denso que a água, o que permite que ele flutue em superfícies aquáticas. A densidade pode variar com base na composição específica do petróleo.")
st.write(":black_medium_small_square: A viscosidade do petróleo pode variar bastante. Os mais leves são menos viscosos e fluem facilmente, enquanto os mais pesados são mais viscosos e fluem mais lentamente.")
st.write(":black_medium_small_square: Do ponto de vista químico, o petróleo é composto principalmente de hidrocarbonetos (moléculas constituídas de átomos de hidrogênio e carbono). Ele também contém quantidades variáveis de outros compostos, incluindo compostos organossulfurados, oxigenados e materiais nitrogenados.")
st.write(":black_medium_small_square: O petróleo é uma mistura de muitos hidrocarbonetos diferentes, cada um com seu próprio ponto de ebulição. Essa propriedade é explorada no processo de refino, onde a destilação fracionada separa o óleo em diferentes componentes.")
st.write(":black_medium_small_square: Ele é hidrofóbico (não solúvel em água), mas é solúvel em solventes orgânicos. Essa propriedade leva à formação de manchas de óleo em corpos d'água.")
st.write(":black_medium_small_square: Ele é altamente inflamável, tornando-o uma valiosa fonte de combustível. Ele libera energia na forma de calor quando queimado.")
st.write(":black_medium_small_square: O petróleo bruto tem um odor distinto, muitas vezes forte, que pode variar com base em sua composição e estado de degradação.")
st.write(":black_medium_small_square: O petróleo pode sofrer várias reações químicas, como oxidação e polimerização. Ele também pode reagir com certos produtos químicos, levando à formação de novos compostos.")
st.write(":black_medium_small_square: Alguns componentes do petróleo bruto, especialmente certos hidrocarbonetos aromáticos policíclicos (PAHs), podem ser tóxicos para humanos e animais selvagens.")

st.write(" **Tipos de petróleo** ")

st.write(":black_medium_small_square: **Petróleo Brent**: petróleo produzido na região do Mar do Norte, provenientes dos sistemas de exploração petrolífera de Brent e Ninian. É o petróleo na sua forma bruta (crú) sem passar pelo sistema de refino.")
st.write(":black_medium_small_square: **Petróleo Light**: petróleo leve, sem impurezas, que já passou pelo sistema de refino.")
st.write(":black_medium_small_square: **Petróleo Naftênico**: petróleo com grande quantidade de hidrocarbonetos naftênicos.")
st.write(":black_medium_small_square: **Petróleo Parafínico**: petróleo com grande concentração de hidrocarbonetos parafínicos.")
st.write(":black_medium_small_square: **Petróleo Aromático**: com grande concentração de hidrocarbonetos aromáticos.")

st.write(" **Maiores Produtores Mundiais** ")

st.write(":black_medium_small_square: Os Estados Unidos da América são reconhecidos como o maior produtor de petróleo do planeta, com mais de 16 milhões de barris extraídos por dia.")
st.write(":black_medium_small_square: Logo em seguida vem a Arábia Saudita com uma produção média diária de aproximadamente 11 milhões de barris.")
st.write(":black_medium_small_square: Em terceiro lugar, temos a Rússia com uma produção média diária de 10 milhões de barris, aproximadamente.")
st.write(":black_medium_small_square: O Brasil ocupa a 9ª na produção mundial de petróleo")
st.write(":black_medium_small_square: Juntos, USA, Arábia Saudita e Russia são responsáveis por mais de 50% da produção diária de petroleo, quando somamos a quantidade total da produção dos Top 15 produtores mundiais e por 40% do volume total da produção diária.")
st.image('graf15Produtores.png')

st.write(" **Brent – O que é, significado e definição** ")

st.write(":black_medium_small_square: Brent é uma sigla, que normalmente acompanha a cotação do petróleo e indica a origem do óleo e o mercado onde ele é negociado. O petróleo Brent foi batizado assim porque era extraído de uma base da Shell chamada Brent.")
st.write(":black_medium_small_square: Atualmente, a palavra Brent designa todo o petróleo extraído no Mar do Norte e comercializado na Bolsa de Londres.")
st.write(":black_medium_small_square: A cotação do petróleo Brent é referência para os mercados europeu e asiático.")
st.write(":black_medium_small_square: O petróleo Brent é produzido próximo ao mar, então os custos de transporte são significativamente menores.")
st.write(":black_medium_small_square: O Brent tem uma qualidade menor, mas, se tornou um padrão do petróleo e tem maior preço por causa das exportações mais confiáveis.")

st.write(" **Cotação e principais influências no preço** ")

st.write("O petróleo nada mais é do que uma commodity negociada no mercado financeiro internacional, normalmente na forma de contratos no mercado futuro. Cada um desses contratos costuma ser composto por 100 barris e negociado em dólares. Por serem derivados do preço do barril e do câmbio da moeda norte-americana, esses contratos futuros são conhecidos como derivativos.")
st.write("É importante ter em mente que o preço do petróleo é sempre expresso por barril (bbl), sendo que um barril é equivalente, a aproximadamente, 159 litros.")
st.write("Como qualquer ativo financeiro cotado em Bolsa de Valores, a cotação do barril de petróleo é submetida a flutuações que dependem essencialmente da lei da oferta e da demanda.")
st.write("A oferta do mercado de petróleo é definida pela Organização dos Países Exportadores de Petróleo (Opep), que é encarregada de determinar quantos barris serão produzidos por dia. O objetivo da Opep é regular e estabilizar o mercado.")
st.write("Contudo, dois grandes produtores, Estados Unidos e Rússia, não fazem parte da Opep. Ou seja, a Opep não controla a totalidade da produção de petróleo bruto no mundo, apenas uma parte.")
st.write("Do lado da demanda, um aumento das necessidades em energia de um país que seja grande consumidor, pode ter uma influência relevante para a cotação do barril, elevando seu preço.")
st.write("Por outro lado, em momentos de crises e recessões, como foi o período da pandemia do coronavírus, o consumo do petróleo e seus derivados, como combustíveis e lubrificantes, tende a diminuir e por consequência, reduzir as cotações.")
st.write("Mudanças climáticas também podem afetar a cotação do petróleo pela ótica da demanda, por exemplo, um inverno rigoroso aumenta o consumo dos combustíveis (calefação), como resultado, tende a elevar o preço pago pelo barril de petróleo.")
st.write("Por fim, destacamos que outro fator que pode afetar o preço do petróleo são as tensões geopolíticas nos maiores países produtores de petróleo. Qualquer fator que afete a produção desses países poderá mudar a cotação do petróleo no mercado financeiro.")
st.write("Em suma, podemos concluir que a cotação do petróleo é afetada por fatores ambientais, econômicos, políticos e sociais.")

st.divider()  
st.write("Agora que nos contextualizamos um pouco sobre o petróleo, vamos aprofundar nossa análise na cotação do Petróleo Brent (Brent Crude Oil Last Day Financ (BZ=F) ) ao longo dos anos. Definimos como Início da nossa análise o ano de 2009, para termos um cenário dos últimos 15 anos.")


#fonte dos índices e cotações:   https://finance.yahoo.com/
indice = "BZ=F"   # Brent Crude Oil Last Day Financ (BZ=F)
inicio = "2009-01-01" #Define a data de ínicio para importação dos dados
#Coleta dados históricos do índice de referência até a data corrente
dados_acao = yf.download(indice, inicio) #Quando a biblioteca é chamada sem uma data final, carrega as cotações até a data corrente
df_cotacoes = pd.DataFrame({indice: dados_acao['Close']})

st.write("Vamos verificar inicialmente o comportamento gráfico das cotações do índice no período:")

df1 = pd.DataFrame(df_cotacoes)
df1.rename(columns={indice: 'Brent Crude Oil'}, inplace = True)
df2 = pd.DataFrame(data=[])
df3 = pd.DataFrame(data=[])
df4 = pd.DataFrame(data=[])

fig = cria_grafico(df1, df2,df3,df4,'Histórico de Cotações Brent Crude Oil', 0,0 )
st.plotly_chart(fig, use_container_width=True)

st.write(" **Análises de Oscilações** ")
media_valor_brent = df_cotacoes[indice].describe().loc[['mean']].mean().round(2)
txt_analise_oscilacao = "No gráfico acima, podemos verificar algumas oscilações bruscas na cotação do Brent Crude Oil ao longo dos últimos 15 anos. Na média, as cotações ficaram na casa dos USD " + str(media_valor_brent) + ", sendo que em abril/2020 a cotação atingiu seu menor preço no período, ficando em USD 19,33 e em março/2022 atingiu o maior valor do período, ficando em USD 127,98. Abaixo vamos detalhar um pouco esta variações"
st.write(txt_analise_oscilacao)
pd.options.display.float_format = "{:.2f}".format
st.write(df_cotacoes[indice].describe().loc[['mean','min','max']])

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Crise na Libia", "Aumento da Demanda de Petróleo", "Sãnções Econômicas USA vs Irã","COVID-19","Embargo Econômico USA vs Rússia"])

with tab1:
    st.header(" **abril/2011** - Crise na Líbia")
    st.image("crise na Libia.jpg")
    st.write("A crise líbia refere-se à atual crise humanitária e instabilidade política que ocorre na Líbia iniciada com os protestos da Primavera Árabe, que resultou na Guerra Civil Líbia (2011), na intervenção militar estrangeira e na deposição e morte de Muammar Gaddafi; continuando com a instabilidade de segurança geral em todo o país e na eclosão de uma nova guerra civil em 2014. A atual crise na Líbia resultou até agora em dezenas de milhares de vítimas desde o início da violência no início de 2011. Durante as duas guerras civis, a produção da indústria de petróleo, economicamente fundamental para a Líbia, colapsou para uma pequena fracção do seu nível normal.")
    st.write("Na época, Várias companhias petrolíferas suspenderam a produção do petróleo na Líbia, entre elas a Total, da França, a Repsol, da Espanha, a austríaca OMV e a italiana ENI. A Wintershall, da Alemanha, também anunciou a suspensão de suas atividades no país norte-africano, que geravam cerca de 100 mil barris de petróleo por dia.")
    st.write("Em abril/2011 a Líbia produzia 1,6 milhões de barris de petróleo por dia e era responsável por 2% do petróleo extraído no mundo. Apenas no mercado europeu, o país era responsável por 10% do abastecimento. A Itália era sua maior compradora.")
    st.write("A atividade petrolífera é fundamental para a economia líbia, representando 95% de suas exportações e 30% de seu Produto Interno Bruto (PIB)")

with tab2:
    st.header(" **janeiro/2016** - Aumento da Demanda de Petróleo no Mercado Mundial")
    st.image("queda preço 2016.jpg")
    st.write("Desde maio/2015, o petróleo da Opep vinha registrando uma forte tendência de baixa, que o fez perder desde então quase US$ 40 por barril.")
    st.write("O baixo nível dos preços foi consequência de um excesso da oferta nos mercados, sobretudo nos Estados Unidos. A isso se acrescentou também a perspectiva de uma breve alta das exportações do produto da parte do Irã, após a retirada das sanções internacionais contra esse país no marco do acordo nuclear pactuado em julho/2015.")
    st.write("Na época, o barril de petróleo Brent ficou abaixo dos USD 30 pela primeira vez desde março de 2004, devido à inquietação dos investidores sobre a economia chinesa e também pelo excesso da oferta.")
    st.write("Os preços do petróleo acumulavam mais de um ano e meio de quedas, devido a um excesso de oferta dos mercados, que se agravou devido às preocupação com as turbulências financeiras na China na époco, segundo maior consumidor mundial da commodity.")

with tab3:
    st.header(" **agosto a outubro/2018** - Sanções Econômicas dos Estados Unidos Contra o Irã")
    st.image("sanção dos Estados Unidos Irã.jpg")
    st.write("Em agosto/2018 entrou em vigor uma série de sanções econômicas impostas pelos Estados Unidos ao Irã, que alegavam que regime de Teerã não cumpria os termos do acordo nuclear assinado em 2015.")
    st.write("Os USA já havia anunciado em maio/2018 a saída do acordo e o restabelecimento das sanções contra o Irã e as empresas internacionais que faziam negócios com o país.")
    st.write("Acertado em 2015 depois de dois anos de negociações entre o Irã, Estados Unidos, China, Reino Unido, França e Alemanha, este pacto permitiu remover uma na parte das sanções contra Teerã e conseguir o compromisso do regime islâmico iraniano de não ter bomba nuclear.")
    st.write("Segundo o Organismo Internacional de Energia Atômica (OIEA), o Irã respeitou as condições do acordo. Mas os EUA diziam que isso não era verdade, e o governo de Israel dizia ter documentos mostrando que o Irã seguia enriquecendo urânio.")
    st.write("Depois de sua saída unilateral, Washington indicou que as sanções seriam efetivadas de maneira imediata para os novos contratos e deu um prazo de 90 a 180 dias para que as multinacionais abandonassem suas atividades no Irã.")
    st.write("Em outubro/2018 os preços do petróleo tiveram um salto, avançando para níveis não vistos desde de novembro de 2014, devidoo ao temor do mercado de as exportações de óleo do terceiro maior produtor da Organização dos Países Exportadores de Petróleo (Opep) serem reduzidas.")

with tab4:
    st.header(" **abril/2020** - Paralisação da Economia Global devido à COVID-19")
    st.image("quedaPreçoCOVID19.jpg")
    st.write("Com a economia global paralisada devido à pandemia de coronavírus, a demanda por petróleo caiu e faltou espaço para armazenar os superestoques. Os preços do petróleo já vinham caindo drasticamente desde meados de março/2020 devido à crise do novo coronavírus. Também houve um desacordo entre o cartel da Organização dos Países Exportadores de Petróleo (Opep) e outros países produtores dessa matéria-prima. A gota d'água agora foi que certos contratos de entrega de petróleo estavam prestes a vencer, mas os armazéns estão cheios, pois há poucos compradores. E isso empurrou o preço do petróleo WTI (West Texas Intermediate) para um valor negativo na noite de segunda-feira 20/04/2020 – ou seja, os operadores estavam pagando para que outros investidores assumissem os contratos.")
    st.write(" O petróleo WTI tem a propriedade de ser armazenado de forma bastante unidimensional, porque os oleodutos terminam no estado de Oklahoma, onde se localiza a maior instalação de armazenamento de petróleo do mundo e onde as entregas são feitas. Na cidade de Cushing, no entanto, os reservatórios já estavam bem cheios. Os tanques que sobraram cobravam cerca de 10 dólares para armazenar cada barril. O petróleo Brent, produzido no Mar do Norte, na Europa, tem mais alternativas de entrega e por isso não sofreu uma baixa tão significativa quanto o WTI, porém atingiu o menor valor de cotação dos últimos 18 anos!!")

with tab5:
    st.header(" **março/2022** - Embargo Econômico dos USA contra a Russia")
    st.image("gerraUcrania.jpg")
    st.write("A Rússia é a segunda maior exportadora de petróleo no mundo, responsável por aproximadamente 11% da produção mundial. Porém, países como EUA e Reino Unido se negaram a importar combustível russo como forma de retaliar as ações do Kremlin na Ucrânia. Devido a isso, aproximadamente 7 milhões de barris deixaram de ser comercializados diariamente. Como defesa contra o embargo econômico, Putin decretou a proibição de importação e exportação de matérias-primas, o que afetou as atividades econômicas em diversos países, como o próprio EUA e a Alemanha.")
    st.write("Desde que o mercado notou a intenção da invasão russa no dia 21/02/2022, o preço do barril Brent já vinha valorizando. No dia 08/03/2022 O preço do barril de Brent, petróleo de referência na Europa, subiu mais de 5%, e atingiu o maior valor da série histórica, cotado a USD 127,98.")
    st.write("Na contra-mão deste movimento, os Emirados Árabes Unidos entraram com um pedido à Opep (Organização dos Países Exportadores de Petróleo) para elevar o nível de produção de petróleo dos países membros. O objetivo era aumentar a oferta e controlar os preços dos barris. A medida foi um aceno positivo ao mercado e no dia 10 de março de 2022, o barril já era cotado em USD 112,37, uma queda de 13% em relação ao dia anterior.")


st.divider()  
st.subheader('Modelos de Predição')
st.write("Não explicaremos a base e conceitos de cada modelo utilizado nesta análise, apenas apresentaremos um comparativo entre eles")

#Modelos e Validadores
from statsmodels.tsa.stattools import adfuller # importar o teste ADF
from statsmodels.tsa.stattools import acf, pacf
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.seasonal import seasonal_decompose
from prophet import Prophet
from keras.models import Sequential
from keras.layers import LSTM,Dense,Dropout
from tensorflow.keras.preprocessing.sequence import TimeseriesGenerator
from tensorflow.keras.optimizers import Adam
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error,  mean_absolute_percentage_error, r2_score



#Define Constantes para todos os  Modelo
steps = 120  #Tamanho da base de testes. Optamos por treinar com todo o histórico e testar com ultimos x dias definidos na variável
du = 10       #dias úteis para previsão futura
Lista_indicadores = ['Erro Médio Absoluto - MAE','Erro Quadrático Médio - MSE','Raiz Quadrada do Erro Médio - RMSE','Média Percentual Absoluta do Erro - MAPE','Coeficiente de Determinação(R²)']

tab1MP, tab2MP, tab3MP, tab4MP = st.tabs(["ARIMA", "PROPHET", "LSTM","LSTM Suavizado"])

with tab1MP:
    st.header("ARIMA")
    st.write("O modelo Arima (AutoRegressive Integrated Moving Average) é amplamente utilizado para previsão de séries temporais. Ele combina componentes de regressão autoregressiva, média móvel e diferenciação para capturar os padrões presentes nos dados. É mandatorio que a série temporal seja estacionária para que este modelo seja aplicado.")

    #Define um valor para as janelas
    janela = 7
    #Cria um novo DataFrame para armazenar apenas a Data e a cotação de fechamento do índice (Close)
    df_arima = pd.DataFrame({indice: dados_acao['Close']})
    df_arima = df_arima.reset_index('Date')
    df_arima['Date'] = pd.to_datetime(df_arima['Date']) #realizando a conversão da data para formato datetime
    df_arima.set_index('Date', inplace = True)

    X = df_arima[indice].values

    # aplicar ADF e imprimir o resultado
    result = adfuller(X)
    ma = df_arima.rolling(janela).mean()
    df_log = np.log(df_arima)
    ma_log = df_log.rolling(janela).mean()
    #subtrair média do log dos dados
    df_sub = (df_log - ma_log).dropna()
    ma_sub = df_sub.rolling(janela).mean()
    #desvio padrão
    std_sub = df_sub.rolling(janela).std()
    #repetir o ADF
    X_sub = df_sub[indice].values

    # aplicar ADF
    result_sub = adfuller(X_sub)
    #Diferenciação
    #aplicar diferenciação
    df_diff = df_sub.diff(1)
    ma_diff = df_diff.rolling(janela).mean()
    #desvio padrão
    std_diff = df_diff.rolling(janela).std()
    #extrair apenas os valores e retirar os valores NA
    X = df_diff[indice].dropna().values

    # aplicar ADF e imprimir o resultado
    result_diff = adfuller(X)

    lag_acf = acf(df_diff.dropna(), nlags=janela)
    lag_pacf = pacf(df_diff.dropna(), nlags=janela)
    #Treinando o modelo
    #ARIMA(p,d,q)
    p = 1
    d = 1
    q = 1

    #Treina o modelo
    model = ARIMA(df_log, order=(p,d,q))
    result_AR = model.fit( )
    #Cria um dataframe para acompanhar os ultimos x dias da base de teste com as predições
    df_teste_arima  = pd.DataFrame(data=df_log[-steps:], columns=[indice])
    df_i = df_teste_arima.head(1)
    df_i.reset_index(inplace = True)
    di = df_i['Date'].astype(str)

    df_e = df_teste_arima.tail(1)
    df_e.reset_index(inplace = True)
    de = df_e['Date'].astype(str)

    #Cria um dataframes com os ultimos x dias da previsão do Arima
    forecast =  result_AR.predict(start=di.values[0], end=de.values[0])
    df_forecast =  pd.DataFrame(data= forecast.values, columns=[indice], index = df_teste_arima.index)
    # Plota um gráfico para comparar o realizado com o periodo testado + previsões
    df1 = pd.DataFrame(df_log)
    df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
    df2 = pd.DataFrame(df_forecast)
    df2.rename(columns={indice: 'Predições'}, inplace = True)
    df3 = pd.DataFrame(data=[])
    df4 = pd.DataFrame(data=[])
    
    figArima = cria_grafico(df1, df2,df3,df4,'Predições com Modelo Arima', 1,steps+1 )
    st.plotly_chart(figArima, use_container_width=True)

    #Retorna o df do ARIMA para os valores antes da diferenciação para a plotagem no gráfico comparativo
    df_original= df_arima[-steps:]
    cols = df_original.columns
    x = []
    for col in cols:
        diff_results = df_original[col] + df_forecast[col].shift(-1)
        x.append(diff_results)
    diff_df_inverted = pd.concat(x, axis=1)
    #calcula as métricas de avaliação de desempenho do modelo
    MAE_ARIMA = mean_absolute_error(df_teste_arima[indice].values, df_forecast[indice].values)
    MSE_ARIMA = mean_squared_error(df_teste_arima[indice].values, df_forecast[indice].values, squared=True)
    RMSE_ARIMA = mean_squared_error(df_teste_arima[indice].values, df_forecast[indice].values, squared=False)
    MAPE_ARIMA = mean_absolute_percentage_error(df_teste_arima[indice].values, df_forecast[indice].values)
    r2_ARIMA = r2_score(df_teste_arima[indice].values, df_forecast[indice].values)
    dados_arima = {
    'Indicador': Lista_indicadores,
    'Resultado': [MAE_ARIMA, MSE_ARIMA,RMSE_ARIMA,MAPE_ARIMA,r2_ARIMA]
    }
    df_result_arima = pd.DataFrame(data = dados_arima['Resultado'], index=dados_arima['Indicador'], columns =['Resultado'])
    st.write(df_result_arima)

with tab2MP:
    st.header("PROPHET")
    st.write("Prophet é uma biblioteca de predição da Meta(Facebook) , que segue o modelo da API sklearn")
    #Cria um novo DataFrame para armazenar apenas a Data e a cotação de fechamento do índice (Close
    df_prophet = pd.DataFrame({indice: dados_acao['Close']})

    df_prophet = df_prophet.reset_index('Date')
    df_prophet[['ds','y']] = df_prophet[['Date',indice]]
    #separando os dados em Treinamento e Teste
    train_pp = df_prophet.sample(frac=0.8, random_state=0)
    train_pp.drop(['Date',indice], axis=1, inplace = True)
    test_pp = df_prophet.drop(train_pp.index)
    #Treinando o modelo
    modelo_pp = Prophet(daily_seasonality='auto')
    modelo_pp.fit(df_prophet)
    dataFramefuture_pp = modelo_pp.make_future_dataframe(periods=du)
    previsao_pp = modelo_pp.predict(dataFramefuture_pp)
    # Extrair as colunas relevantes dos DataFrames
    previsao_cols = ['ds', 'yhat']
    valores_reais_cols = ['ds', 'y']

    previsao_pp = previsao_pp[previsao_cols]
    valores_reais = train_pp[valores_reais_cols]

    # Mesclar os DataFrames nas colunas 'ds' para comparar previsões e valores reais
    resultados_pp = pd.merge(previsao_pp, valores_reais, on='ds', how='inner')
    # Plota um gráfico para comparar o realizado com o periodo testado + previsões
    df1 = pd.DataFrame(data= resultados_pp['y'].values, index=resultados_pp['ds'], columns=['Dados Históricos'] )
    #df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
    df2 = pd.DataFrame(data= resultados_pp[-steps:]['yhat'].values, index=resultados_pp[-steps:]['ds'].values, columns=['Predições'] )
    #df2.rename(columns={indice: 'Predições'}, inplace = True)
    df3 = pd.DataFrame(data=[])
    df4 = pd.DataFrame(data=[])
    
    figProphet = cria_grafico(df1, df2,df3,df4,'Predições com Modelo Prophet', 1,steps+1 )
    st.plotly_chart(figProphet, use_container_width=True)

    #calcula as métricas de avaliação de desempenho do modelo
    MAE_pp = mean_absolute_error(resultados_pp[-steps:]['y'].values, resultados_pp[-steps:]['yhat'].values)
    MSE_pp = mean_squared_error(resultados_pp[-steps:]['y'].values, resultados_pp[-steps:]['yhat'].values, squared=True)
    RMSE_pp = mean_squared_error(resultados_pp[-steps:]['y'].values, resultados_pp[-steps:]['yhat'].values, squared=False)
    MAPE_pp = mean_absolute_percentage_error(resultados_pp[-steps:]['y'].values, resultados_pp[-steps:]['yhat'].values)
    r2_pp = r2_score(resultados_pp[-steps:]['y'].values, resultados_pp[-steps:]['yhat'].values)    
    dados_prophet = {
    'Indicador': Lista_indicadores,
    'Resultado': [MAE_pp, MSE_pp,RMSE_pp,MAPE_pp,r2_pp]
    }
    df_result_prophet = pd.DataFrame(data = dados_prophet['Resultado'], index=dados_prophet['Indicador'], columns =['Resultado'])
    st.write(df_result_prophet)
with tab3MP:
    st.header("LSTM")   
    st.write("Vamos agora utilizar uma Rede LSTM (Long Short-Term Memory)")

    df_LSTM = pd.DataFrame({indice: dados_acao['Close']})
    df_LSTM.reset_index(inplace=True)
    #Aplicando suavização exponencial
    alpha = 0.15   # Fator de suavização
    # O parâmetro alpha na suavização exponencial controla a taxa de decaimento dos pesos atribuídos às observações passadas.
    # Determina o quão rapidamente o impacto das observações antigas diminui à medida que você avança no tempo.

    df_LSTM['Smoothed_Close'] = df_LSTM[indice].ewm(alpha=alpha, adjust=False).mean()
    close_data = df_LSTM[indice].values #fechamento não suavizado
    close_data = close_data.reshape(-1,1) #transformar em array
 
    #Agora aplicamos a normalização dos dados para não termos ruído
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler = scaler.fit(close_data)
    close_data_escalado = scaler.transform(close_data)
 
    #Separando as bases em treino e teste
    look_back = 10
    close_train_lstm = close_data_escalado[:-steps]
    close_test_lstm = close_data_escalado[-(steps):]

    date_train_lstm = df_LSTM['Date'][:-steps]
    date_test_lstm = df_LSTM['Date'][-steps:]

    # Gerar sequências temporais para treinamento e teste em um modelo de aprendizado de máquina
    train_generator = TimeseriesGenerator(close_train_lstm, close_train_lstm, length=look_back, batch_size=20)
    test_generator = TimeseriesGenerator(close_test_lstm, close_test_lstm, length=look_back, batch_size=1)
    #Aplica o modelo
    np.random.seed(7)
    model = Sequential()
    model.add(LSTM(100, activation='relu', input_shape=(look_back,1)))
    model.add(Dense(1)),
    model.compile(optimizer='adam', loss='mean_squared_error')
    num_epochs = 20
    retornomodelo = model.fit(train_generator, epochs=num_epochs, verbose=1)
    # 1. Fazer previsões usando o conjunto de teste
    test_predictions_lstm = model.predict(test_generator)
    prediction_lstm = test_predictions_lstm.reshape((-1))
    close_data_g = close_data_escalado.reshape((-1))

    # Plota um gráfico para comparar o realizado com o periodo testado + previsões
    df1 = pd.DataFrame(data= close_data_g, index=df_LSTM['Date'].values, columns=['Dados Históricos'] )
    #df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
    df2 = pd.DataFrame(data= prediction_lstm, index=date_test_lstm[-prediction_lstm.size:], columns=['Predições'] )
    #df2.rename(columns={indice: 'Predições'}, inplace = True)
    df3 = pd.DataFrame(data=[])
    df4 = pd.DataFrame(data=[])
    
    figLSTM = cria_grafico(df1, df2,df3,df4,'Predições com Modelo LSTM', 1,steps+1 )
    st.plotly_chart(figLSTM, use_container_width=True)
    #calcula as métricas de avaliação de desempenho do modelo
    MAE_LSTM = mean_absolute_error(close_data_g[-prediction_lstm.size:], prediction_lstm)
    MSE_LSTM = mean_squared_error(close_data_g[-prediction_lstm.size:], prediction_lstm, squared=True)
    RMSE_LSTM = mean_squared_error(close_data_g[-prediction_lstm.size:], prediction_lstm, squared=False)
    MAPE_LSTM = mean_absolute_percentage_error(close_data_g[-prediction_lstm.size:], prediction_lstm)
    r2_LSTM = r2_score(close_data_g[-prediction_lstm.size:], prediction_lstm) 
    dados_LSTM = {
    'Indicador': Lista_indicadores,
    'Resultado': [MAE_LSTM, MSE_LSTM,RMSE_LSTM,MAPE_LSTM,r2_LSTM]
    }
    df_result_LSTM = pd.DataFrame(data = dados_LSTM['Resultado'], index=dados_LSTM['Indicador'], columns =['Resultado'])
    st.write(df_result_LSTM)

    predictions_LSTM_inv = scaler.inverse_transform(prediction_lstm.reshape(-1, 1))
    df_LSTM_pred_g = pd.DataFrame(data=predictions_LSTM_inv, columns = [indice], index= df_LSTM[-predictions_LSTM_inv.size:]['Date'])

with tab4MP:
    st.header("LSTM Suavizado")   
    cs_data =  df_LSTM['Smoothed_Close'].values #fechamento  suavizado
    cs_data = cs_data.reshape(-1,1) #transformar em array
    cs_data_escalado = scaler.transform(cs_data)
    #Separando as bases em treino e teste
    cs_train_lstm = cs_data_escalado[:-steps]
    cs_test_lstm = cs_data_escalado[-steps:]
    # Gerar sequências temporais para treinamento e teste em um modelo de aprendizado de máquina
    look_back_cs = 5
    train_generator_cs = TimeseriesGenerator(cs_train_lstm, cs_train_lstm, length=look_back_cs, batch_size=20)
    test_generator_cs = TimeseriesGenerator(cs_test_lstm, cs_test_lstm, length=look_back_cs, batch_size=1)
    #Aplica o modelo
    np.random.seed(7)
    model_cs = Sequential()
    model_cs.add(LSTM(100, activation='relu', input_shape=(look_back_cs,1)))
    model_cs.add(Dense(1)),
    model_cs.compile(optimizer='adam', loss='mean_squared_error')
    num_epochs = 20
    model_cs.fit(train_generator_cs, epochs=num_epochs, verbose=1)
    # 1. Fazer previsões usando o conjunto de teste
    test_predictions_cs_lstm = model_cs.predict(test_generator_cs)
    prediction_lstm_cs = test_predictions_cs_lstm.reshape((-1))
    # Plota um gráfico para comparar o realizado com o periodo testado + previsões
    df1 = pd.DataFrame(data= close_data_g, index=df_LSTM['Date'].values, columns=['Dados Históricos'] )
    #df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
    df2 = pd.DataFrame(data= prediction_lstm_cs, index=date_test_lstm[-prediction_lstm_cs.size:], columns=['Predições'] )
    #df2.rename(columns={indice: 'Predições'}, inplace = True)
    df3 = pd.DataFrame(data=[])
    df4 = pd.DataFrame(data=[])
    
    figLSTMCS = cria_grafico(df1, df2,df3,df4,'Predições com Modelo LSTM - Curva Suavizada', 1,steps+1 )
    st.plotly_chart(figLSTMCS, use_container_width=True)
    
    #calcula as métricas de avaliação de desempenho do modelo
    MAE_CS = mean_absolute_error(close_data_g[-prediction_lstm_cs.size:], prediction_lstm_cs)
    MSE_CS = mean_squared_error(close_data_g[-prediction_lstm_cs.size:], prediction_lstm_cs, squared=True)
    RMSE_CS = mean_squared_error(close_data_g[-prediction_lstm_cs.size:], prediction_lstm_cs, squared=False)
    MAPE_CS = mean_absolute_percentage_error(close_data_g[-prediction_lstm_cs.size:], prediction_lstm_cs)
    r2_CS = r2_score(close_data_g[-prediction_lstm_cs.size:], prediction_lstm_cs)

    dados_LSTM_CS = {
    'Indicador': Lista_indicadores,
    'Resultado': [MAE_CS, MSE_CS,RMSE_LSTM,MAPE_CS,r2_CS]
    }
    df_result_LSTM_CS = pd.DataFrame(data = dados_LSTM_CS['Resultado'], index=dados_LSTM_CS['Indicador'], columns =['Resultado'])
    st.write(df_result_LSTM_CS)

    predictions_LSTM_cs_inv = scaler.inverse_transform(prediction_lstm_cs.reshape(-1, 1))
    df_LSTM_pred_cs_g = pd.DataFrame(data=predictions_LSTM_cs_inv, columns = [indice], index= df_LSTM[-predictions_LSTM_cs_inv.size:]['Date'])
 
    
st.divider()  
st.subheader('Resumo dos Resultados ')
st.write("Agora que já testamos diversos modelos clássicos de sérias temporais, como escolher um? Para medir um modelo (seja ele qual for), vamos tentar medir e analisar os erros que ele apresenta, ou seja, vamos comparar Y e Ŷ (Y real e Y previsto, respectivamente) e dar atenção à esses resíduos.")
st.write("Sendo assim, a seguir, vamos comparar 5 técnicas diferentes para aferir o melhor modelo de previsão para séries temporais:")


dados_consolidados = {
    'Indicador': Lista_indicadores,
    'ARIMA': [MAE_ARIMA, MSE_ARIMA,RMSE_ARIMA,MAPE_ARIMA,r2_ARIMA],
    'PROPHET': [MAE_pp, MSE_pp,RMSE_pp,MAPE_pp,r2_pp],
    'LSTM': [MAE_LSTM, MSE_LSTM,RMSE_LSTM,MAPE_LSTM,r2_LSTM],
    'LSTM Curva Suavizada': [MAE_CS, MSE_CS,RMSE_LSTM,MAPE_CS,r2_CS]
    }

df_result_consolidado = pd.DataFrame(data = dados_consolidados, index=dados_consolidados['Indicador'], columns =['ARIMA','PROPHET','LSTM','LSTM Curva Suavizada'])
st.write(df_result_consolidado)

st.write("Comparando a tabela acima, tanto o ARIMA quanto o LSTM alcaçaram bons resultados. Vamos compará-los graficamente para não restar dúvidas:")
# Plota um gráfico para comparar todos os modelos
df1 = pd.DataFrame(df_cotacoes)
df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
df2 = pd.DataFrame(diff_df_inverted)
df2.rename(columns={indice: 'ARIMA'}, inplace = True)
df3 = pd.DataFrame(df_LSTM_pred_g)
df3.rename(columns={indice: 'LSTM'}, inplace = True)
df4 = pd.DataFrame(data=[])

figConsolidado = cria_grafico(df1, df2,df3,df4,'Comparativo de Predições dos Modelos - ARIMA vs LSTM', 1,steps+1 )
st.plotly_chart(figConsolidado, use_container_width=True)

st.write("Na análise visual, o modelo ARIMA acompanhou melhor o comportamento do Índice BRENT, acertando o movimento (valorização ou desvalorização) enquanto o modelo LSTM ficou mais perto dos valores, porém com os valores com tendencias de subida, sem acompanhar o movimento diário. Vamos ver na prática como foram estes resultados pelo percentual de acertos do movimento:")


#Monta um DF para armazenar os dados de previsão das ações
x = 0
prev_ini = date.today() + timedelta(days = 1)
na = [prev_ini]

while (len(na)+1) <= du :
  prev_fim_d = prev_ini + timedelta(days = x+1)
  x=x+1
  if (prev_fim_d.weekday() not in (5,6)):
    prev_fim = prev_fim_d
    na.append(prev_fim)

df_dt_futura = pd.DataFrame({"Date":na})
df_dt_futura = df_dt_futura.set_index(pd.DatetimeIndex(df_dt_futura['Date']))

#Cria um segundo DF para unir as cotações correntes e as previsões das ações
df_cotacao_futura = pd.DataFrame({"Date":df_cotacoes.index.values})
df_cotacao_futura = pd.concat([df_cotacao_futura, df_dt_futura])
df_cotacao_futura['Date'] = pd.to_datetime(df_cotacao_futura['Date'])
#Monta os dataframes. A ideia é testar com os últimos <steps> dias e treinar com os dias anteriores
df_treina = df_cotacoes[:-steps]
df_teste  = df_cotacoes[-steps:]
df_prev   = df_cotacao_futura[-(steps+du):]
df_teste_g = pd.DataFrame(df_teste.index)
df_teste_g["teste"] = df_teste[indice].values


#ARIMA
df_compara_arima = pd.DataFrame(data=df_teste_arima[indice].values, index=df_teste_arima.index.values, columns=["Close"])
df_compara_arima["predicoes"] = df_forecast[indice].values
comp_real_arima = np.where(df_compara_arima['Close'].shift(1) < df_compara_arima['Close'], 1, 0)
comp_predito_arima = np.where(df_compara_arima['predicoes'].shift(1) < df_compara_arima['predicoes'], 1, 0)

df_compara_arima["comportamento_real"]= comp_real_arima
df_compara_arima["comportamento_predito"]= comp_predito_arima
acertou_arima = np.where(df_compara_arima['comportamento_real'] == df_compara_arima['comportamento_predito'], 1, 0)
df_compara_arima['acertou_o_lado'] = acertou_arima

#calcular media de acertos
df_compara_arima['var_percent_acao'] = df_compara_arima['Close'].pct_change()
df_compara_arima['var_percent_modelo'] = df_compara_arima['predicoes'].pct_change()
df_compara_arima['dif_var_percent']= (df_compara_arima['var_percent_acao'] - df_compara_arima['var_percent_modelo'])

acertou_lado_arima = df_compara_arima['acertou_o_lado'].sum()/len(df_compara_arima['acertou_o_lado'])
acertos_arima = acertou_lado_arima * 100

#LSTM
df_compara_LSTM = pd.DataFrame(data=df_teste_g[-df_LSTM_pred_g[indice].values.size:]["teste"].values, index=df_LSTM_pred_g.index, columns=["Close"])
df_compara_LSTM["predicoes"] = df_LSTM_pred_g[indice].values

comp_real_LSTM = np.where(df_compara_LSTM['Close'].shift(1) < df_compara_LSTM['Close'], 1, 0)
comp_predito_LSTM = np.where(df_compara_LSTM['predicoes'].shift(1) < df_compara_LSTM['predicoes'], 1, 0)

df_compara_LSTM["comportamento_real"]= comp_real_LSTM
df_compara_LSTM["comportamento_predito"]= comp_predito_LSTM
acertou_LSTM = np.where(df_compara_LSTM['comportamento_real'] == df_compara_LSTM['comportamento_predito'], 1, 0)
df_compara_LSTM['acertou_o_lado'] = acertou_LSTM

#calcular media de acertos
df_compara_LSTM['var_percent_acao'] = df_compara_LSTM['Close'].pct_change()
df_compara_LSTM['var_percent_modelo'] = df_compara_LSTM['predicoes'].pct_change()
df_compara_LSTM['dif_var_percent']= (df_compara_LSTM['var_percent_acao'] - df_compara_LSTM['var_percent_modelo'])

acertou_lado_LSTM = df_compara_LSTM['acertou_o_lado'].sum()/len(df_compara_LSTM['acertou_o_lado'])
acertos_LSTM = acertou_lado_LSTM * 100


dados_compararativos = {
    'Modelo': ['ARIMA','LSTM'],
    '% Acertos': [acertos_arima.round(2),acertos_LSTM.round(2)]
    }

df_comparativo = pd.DataFrame(data = dados_compararativos, index=dados_compararativos['Modelo'], columns =['% Acertos'])
st.write(df_comparativo)

st.write("Como ambos os modelos estão com performance similar em todos os comparativos, iremos realizar o forecast com ambos!")

#Gera as previsões
close_prev_lstm = close_data_escalado[-(steps+du+look_back):]
data_prev_lstm = df_cotacao_futura[-(steps+du):]
prev_generator = TimeseriesGenerator(close_prev_lstm, close_prev_lstm, length=look_back, batch_size=1)
previsions_lstm = model.predict(prev_generator)
prev_lstm = previsions_lstm.reshape((-1))

prev_lstm_inv = scaler.inverse_transform(prev_lstm.reshape(-1, 1))
df_LSTM_prev_g = pd.DataFrame(data=prev_lstm_inv, columns = [indice], index= df_cotacao_futura[-prev_lstm_inv.size:]['Date'])

df1 = pd.DataFrame(df_cotacoes)
df1.rename(columns={indice: 'Dados Históricos'}, inplace = True)
df2 = pd.DataFrame(df_LSTM_pred_g)
df2.rename(columns={indice: 'Predição - LSTM'}, inplace = True)
df3 = pd.DataFrame(data= df_LSTM_prev_g[indice][-df_dt_futura.size:].values, index=df_dt_futura.index.values, columns=['Previsão'] )
df4 = pd.DataFrame(data=[])

figPrev = cria_grafico(df1, df2,df3,df4,'Previsões - Petróleo Brent - Próximos 10 dias', 1,steps+du+look_back )
st.plotly_chart(figPrev, use_container_width=True)

st.write("Listando as Previsões:")
st.write(df3)


st.divider()  
st.subheader('Fontes:')
st.write(" https://www.suapesquisa.com/geografia/petroleo/ ")
st.write(" https://www.suno.com.br/artigos/cotacao-do-petroleo/")
st.write(" https://www.bbc.com/portuguese/articles/cnk0e0yydelo")
st.write(" https://www.wilsonsons.com.br/pt-br/blog/maiores-produtores-de-petroleo-do-mundo/")
st.write(" https://investnews.com.br/infograficos/industria-do-petroleo-quem-produz-quem-compra-e-maiores-reservas/")
st.write(" https://www.bbc.com/portuguese/noticias/2011/02/110224_libia_petroleo_precos_fn")
st.write(" https://pt.wikipedia.org/wiki/Crise_L%C3%ADbia_(2011%E2%80%93presente)#:~:text=A%20atual%20crise%20na%20L%C3%ADbia,frac%C3%A7%C3%A3o%20do%20seu%20n%C3%ADvel%20normal.")
st.write(" https://www.bbc.com/portuguese/noticias/2011/02/110216_libia_petroleo_jf")
st.write(" https://g1.globo.com/economia/noticia/2016/01/barril-de-petroleo-da-opep-cai-para-us-25-o-menor-preco-em-12-anos.html")
st.write(" https://g1.globo.com/economia/noticia/2018/10/01/precos-do-petroleo-sobem-para-maximas-desde-2014-com-acordo-sobre-nafta-e-sancoes-contra-ira.ghtml")
st.write(" https://noticias.uol.com.br/ultimas-noticias/afp/2018/08/07/eua-impoem-sancoes-ao-ira-6-pontos-para-entender-a-crise.htm")
st.write(" https://noticias.uol.com.br/ultimas-noticias/deutschewelle/2020/04/21/por-que-o-preco-do-petroleo-despencou.htm")
st.write(" https://www1.folha.uol.com.br/mercado/2020/03/com-coronavirus-petroleo-brent-cai-ao-menor-patamar-em-17-anos.shtml ")
st.write(" https://noticias.uol.com.br/ultimas-noticias/afp/2022/03/08/petroleo-sobe-545-na-europa-alavancada-por-proximas-sancoes-dos-eua-a-russia.htm ")
st.write(" https://www.zuldigital.com.br/blog/guerra-ucrania-preco-combustivel-brasil/ ")


