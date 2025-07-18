import pandas as pd
import plotly.express as px
import streamlit as st

# LENDO O DATASET
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

# MELHORANDO O NOME DAS COLUNAS
df = df.rename(columns={
    'newDeaths': 'Novos óbitos',
    'newCases': 'Novos casos',
    'deaths_per_100K_inhabitants': 'Óbitos por 100 mil habitantes',
    'totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'
})

# SELEÇÃO DO ESTADO
estados = sorted(df['state'].unique())
state = st.sidebar.selectbox('Qual estado?', estados)

# SELEÇÃO DO TIPO DE DADO
colunas = ['Novos óbitos', 'Novos casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

# FILTRANDO O DATAFRAME
df_estado = df[df['state'] == state]

# PLOTANDO O GRÁFICO
fig = px.line(df_estado, x='date', y=column, title=f'{column} - {state}')
fig.update_layout(xaxis_title='Data', yaxis_title=column.upper(), title={'x': 0.5})

# TÍTULO E DESCRIÇÃO
st.title('📊 Dados COVID-19 no Brasil')
st.write('Use o menu lateral para selecionar o estado e o tipo de dado. O gráfico abaixo será atualizado automaticamente.')

st.plotly_chart(fig, use_container_width=True)

st.caption('Fonte dos dados: https://github.com/wcota/covid19br')
