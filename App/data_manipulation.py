import pandas as pd
#This script just show how I transform the data, the way I wish.

# Data Manipulation ---------------
NOTA_1 = pd.read_csv('C:/Users/SAMSUNG/Downloads/Análise Descritiva dos Dados/Dados/2022_2_Notas Ciência da Computação - CC_NOTA_1.csv')
NOTA_2 = pd.read_csv('C:/Users/SAMSUNG/Downloads/Análise Descritiva dos Dados/Dados/2022_2_Notas Ciência da Computação - CC_NOTA_2.csv')
#read files will not be made available as they contain data from real students


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
NOTA.to_csv('NOTAS_CC.csv',index=False)
