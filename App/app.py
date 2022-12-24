import pandas as pd
import streamlit as st
import plotly.express as px

#Part 01: Data Manipulation ---------------
NOTA_1 = pd.read_csv('C:/Users/SAMSUNG/Downloads/Análise Descritiva dos Dados/Dados/2022_2_Notas Ciência da Computação - CC_NOTA_1.csv')
NOTA_2 = pd.read_csv('C:/Users/SAMSUNG/Downloads/Análise Descritiva dos Dados/Dados/2022_2_Notas Ciência da Computação - CC_NOTA_2.csv')

NOTA_1.head()
NOTA_1.info()

NOTA_2.head()
NOTA_2.info()

#Selecionando as colunas de interesse: 
NOTA_1 = NOTA_1[['Matrícula','Prova 01','Média Total(Prova 01 + Média Atvs + Extra)']]
NOTA_2 = NOTA_2[['Matrícula','PROVA 2','MEDIA 2']]

# Manipulações nos Dataframes

NOTA_1.replace({',':'.'},regex=True,inplace= True)
NOTA_1 = NOTA_1.astype({'Prova 01':'float','Média Total(Prova 01 + Média Atvs + Extra)':'float'})


NOTA_2.drop(0,inplace=True)
NOTA_2.reset_index(inplace=True)
NOTA_2.drop(columns=['index'],inplace=True)
NOTA_2.replace({',':'.'},regex=True,inplace= True)
NOTA_2 = NOTA_2.astype({'Matrícula':'int','PROVA 2':'float','MEDIA 2':'float'})

#Juntando os Dataframes em um só
NOTA = pd.merge(NOTA_1,NOTA_2,how='outer')
NOTA.rename(columns = {'Média Total(Prova 01 + Média Atvs + Extra)':'Media_1','Matrícula':'Mat','Prova 01':'Prova_1','PROVA 2':'Prova_2','MEDIA 2':'Media_2'},inplace = True)
NOTA.info()

#Criando uma Nova Coluna com a Média Final
NOTA['Media_Final'] = round((NOTA['Media_1']+ NOTA['Media_2'])/ 2,2)
NOTA.head() 


NOTA.drop(columns=['Mat'],inplace=True)
NOTA.head()

# Criando uma coluna com os resultados(Aprovado, Reprovados, Avaliação Final)
resultado = []
md_f = NOTA['Media_Final']
md_f = md_f.to_list()

for r in range(len(md_f)):
  if md_f[r] >= 7:
    resultado.append('Aprovado')
  elif md_f[r]>= 4 and md_f[r]<7:
    resultado.append('Avaliação Final')
  else:
    resultado.append('Reprovado')
   
   
NOTA['Resultado'] = resultado
NOTA.head()


#Salvando os resultados em um csv
#NOTA.to_csv('NOTAS_CC.csv',index=False)

#Part 02: Building our app---------------
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
