import pandas as pd
import plotly.express as px
import streamlit as st

#LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#MELHORANDO O NOME DAS COLUNAS DA TABELA
df = df.rename(columns={'newDeaths': 'Novos óbitos','newCases': 'Novos casos','deaths_per_100K_inhabitants': 'óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants':'casos por 100 mil habitantes'})

#SELEÇÃO DO ESTADO
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)

#SELEÇÃO DA COLUNA
column = 'Casos por 100mil habitantes'
colunas = ['Novos óbitos','Novos casos']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#SELEÇÃO DAS LINHAS QUE  PERTENCEM AO ESTADO
df = df[df['state'] == state]

fig =px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout( xaxis_title='Data', yaxis_title=column.upper(), title = {'x':0.5})

st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação,o usuário tem a opção de escolher o estado eo tipo de informação para mostrar o gráfico. Utilize o menu lateral para alterar a montagem.')

st.plotly_chart(fig, use_container_width=True)

st.caption(' Os dados foram obtidos a partir do site : https//github.com/wCota/covide19br')
