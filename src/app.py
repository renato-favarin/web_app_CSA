import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache
def carrega_dados(caminho):
    dados_nutricao = pd.read_excel(caminho)
    return dados_nutricao


def grafico_comparativo(dados_nutricao, lista_alimentos, atributo):
    df = dados_nutricao.set_index('Alimento')
    df = df.loc[lista_alimentos]
    #plt.figure(figsize = (8,6))
    
    figura, ax = plt.subplots()
    ax = sns.barplot(data = df, x = df.index, y = atributo)
    ax.set_title(f"Comparação de {atributo}")
    
    return figura

def gera_tabela(df, label):
        df.index = [" "] * len(df)
        df['na_terra'] = " "
        df['na_cesta'] = " "
        df['  '] =  " "
        df.rename({'produto':label,'na_terra': '   ', 'na_cesta':' '}, axis='columns', inplace=True)
        st.table(df[[label, '   ', '  ',' ']])

def main():
    
    caminho_base_nutricao = "data/informacao_nutricional.xls"
    
    # por enquanto, não vou usar o google drive
    #url_dados_csa = ' https://drive.google.com/file/d/1ZYFIPGIbQ52g1lKYHGhIGIBhT9ZMzB71/view?usp=sharing'
    #caminho_dados_csa = 'https://drive.google.com/uc?export=download&id='+url_dados_csa.split('/')[-2]
    #dados_csa = pd.read_excel(caminho_dados_csa, engine='openpyxl')
    caminho_dados_csa = "data/csa_pindorama.xlsx"
    
    dados_csa = carrega_dados(caminho_dados_csa)
    dados_nutricao = carrega_dados(caminho_base_nutricao)
    
    info_nutricional = dados_nutricao.columns[2:]
    info_alimento = dados_nutricao["Alimento"].values 
    
    st.title("CSA Pindorama")

    st.image("src/logo.jpg", use_column_width=True)
    
    st.markdown("Aplicativo da **CSA Pindorama** :seedling:")
    
    if st.checkbox("Na terra", value=False):
        st.image("src/na_terra.jpg",use_column_width=True)

            
        na_terra = dados_csa.query("na_terra == 'x'")
        gera_tabela(na_terra, '--produtos em cultivo--')
        
    #no futuro, pegar a data no próprio df    
    data = "22/05"
    if st.checkbox(f"Na cesta em {data}",value=False):
        st.image("src/na_cesta.jpg",use_column_width=True)
        na_cesta = dados_csa.query("na_cesta == 'x'")
        gera_tabela(na_cesta, f'--produtos na cesta em {data}--')
        

    st.write("-------------------------------------------")
    st.write("Informação nutricional dos alimentos da CSA.       \n           Obs.: em construção - aberto a sugestões!")
    opcao_info_nutricional = st.selectbox("Escolha a informação nutricional",info_nutricional)
    
    opcao_alimento_1 = st.selectbox("Escolha um alimento",info_alimento, index = 2)
    opcao_alimento_2 = st.selectbox(" Escolha um alimento",info_alimento, index = 18)
    
    
    
    figura = grafico_comparativo(dados_nutricao,[ opcao_alimento_1, opcao_alimento_2], opcao_info_nutricional)
    st.pyplot(figura)
    
if __name__ == "__main__":
    main()
    
  

