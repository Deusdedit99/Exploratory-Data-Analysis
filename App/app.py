import pandas as pd
import streamlit as st
import plotly.express as px

NOTA = pd.read_csv('https://github.com/Deusdedit99/Exploratory-Data-Analysis/blob/main/Dados/NOTAS_CC.csv')
# Building our app---------------
st.set_page_config('Análise Descritiva dos Dados',page_icon='📈',layout='wide')


with open('C:/Users/SAMSUNG/Downloads/Análise Descritiva dos Dados/App/style.css') as f:
   st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.title('Análise Descritiva dos Dados :')
st.header('Desepenho dos Alunos de Ciência da Computação em 2022.2 em Probabilidade e Estatística')
st.markdown('---')



st.markdown('#### 1) Objetivo:')
st.markdown(''' - ##### Apresentar ao leitor um panorama rápido do desempenho da turma de Ciência da Computação 2022.2 em probabilidade e estatística;
- ##### Mostrar resumos númericos importantes para um rápido entendimento;
- ##### Trazer vizualizações para melhor entendimento, entre eles : Histograma e Boxplot.
''')


 
st.markdown("---")
st.markdown('#### 2) Análise Descritiva')
st.markdown('- ##### Após carregar os dados, temos as seguintes classificações :')
st.latex(r'''\text{Tipos de variáveis presente no DataFrame:}\begin{cases}
\text{Qualitativa}\begin{cases}Nome(String)\end{cases}\\
\text{Quantitativa}\begin{cases} \text{Matrícula(Integer)}\\ \text{Nota da Prova 01 e Prova 02(Float)} \\ \text{Média da Parte 01 e 02(Float)}\\ \text{Nota Final(Float)}  \end{cases} \end{cases}''')
st.caption('Obs : Os dados Matrícula e Nome foram ocultados de forma a respeitar a privacidade dos alunos, portanto, cada linha do Dataframe representa um aluno.')
 



st.markdown('- ##### Dados  :')
st.dataframe(NOTA.head(8),use_container_width=True)
st.caption('No semestre 2022.2 teve 2 provas, a primeira ( Prova_1 ) é a parte voltada para a Estatística Descritiva e a segunda ( Prova_2 ) é Probabilidade e Inferência.')
st.caption('Média 1 é referente a média do aluno na parte 1 da disciplina ( Estatística Descritiva ) e Média 2 é a média do aluno na parte 2 da disciplina ( Probabilidade e Inferência ).')
st.caption('A Média Final é uma média entre a média 1 e média 2.')


st.markdown('- ##### Como funciona a Média da Disciplina?')
st.latex(r'''
\text{Média Final} = \frac{Parte_1+ Parte_2}{2}  \\
\text{Onde a Parte 1 ou Parte 2 é composta por:}
\\ Parte_i = \frac{Média_{atvs}+ Prova_i}{2}  
         ''')

st.markdown('- ##### Como saber se fui Aprovado(a), Reprovado(a) ou de Avaliação Final?')
st.latex(r''' 
\begin{cases}
   Aprovado, &\text{Se } Média final \ge 7 \\
   \text{Avaliação Final}, &\text{Se } 4 \le Média final \lt 7 \\
   Reprovado, &\text{Se } Média final \lt 4
\end{cases}    
         ''')
st.caption('Veremos no tópico 4 a situação da turma.')

st.markdown('---')
st.markdown('#### 3) Métricas importantes : ')

col1, col2, col3 = st.columns(3)
col1.metric("Média", "3.64")
col2.metric("Mediana","3.17")
col3.metric("Desvio Padrão", "3.07")


st.markdown('---')
st.markdown('#### 4) Vizualizações : ')
st.markdown('- ##### Para a coluna de *Média Final* temos as seguintes visualizações: ')

col4,col5 = st.columns(2)

fig1 = px.histogram(NOTA,x=NOTA['Media_Final'],title='Histograma das Notas',opacity=0.65,nbins= 9,color_discrete_sequence=px.colors.qualitative.Bold)
col4.plotly_chart(fig1,use_container_width=True)

fig2 = px.box(NOTA,y=NOTA['Media_Final'],title='Boxplot',points='all',color_discrete_sequence=px.colors.qualitative.Bold)
col5.plotly_chart(fig2,use_container_width=True)


st.markdown('- ##### Para a coluna de *Resultado* temos a seguinte visualização: ')
fig3 = px.bar(NOTA,x=NOTA['Resultado'],color=NOTA['Resultado'],title='Gráfico de Barras',opacity=0.7)
st.plotly_chart(fig3,use_container_width=True)


st.markdown('#### Análise e Construção do Relatório desenvolvida por Serena Moonlight 💜')
