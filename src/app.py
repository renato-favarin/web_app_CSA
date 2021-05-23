import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title= "CSA Pindorama", page_icon=':seedling:')

def carrega_dados(caminho, aba):
    dados_nutricao = pd.read_excel(caminho, sheet_name = aba)
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
    
    # por enquanto, não vou usar o google drive
    #url_dados_csa = ' https://drive.google.com/file/d/1ZYFIPGIbQ52g1lKYHGhIGIBhT9ZMzB71/view?usp=sharing'
    #caminho_dados_csa = 'https://drive.google.com/uc?export=download&id='+url_dados_csa.split('/')[-2]
    #dados_csa = pd.read_excel(caminho_dados_csa, engine='openpyxl')
    caminho_dados_csa = "data/csa_pindorama.xlsx"
    
    dados_csa = carrega_dados(caminho_dados_csa, 'produtos') 
    
    st.title("CSA Pindorama :seedling:")
    #st.subheader("Da cultura do preço para a cultura do apreço")

    st.image("src/logo.jpg", use_column_width=True)
    
    st.markdown("**Aplicativo da CSA Pindorama** :sunrise:")
    
    if st.checkbox("Na terra", value=False):
        st.image("src/na_terra.jpg",use_column_width=True)

            
        na_terra = dados_csa.query("na_terra == 'x'")
        gera_tabela(na_terra, '--produtos em cultivo--')
        
    #no futuro, pegar a data no próprio df    
    
    data = "29/mai"
    if st.checkbox(f"Na cesta em {data}",value=False):
        st.image("src/na_cesta.jpg",use_column_width=True)
        na_cesta = dados_csa.query("na_cesta == 'x'")
        gera_tabela(na_cesta, f'--provável cesta em {data} (sujeito à adições)--')
        

    st.write("-------------------------------------------")
    
    st.markdown("**Agenda:** :book: :herb:")
    if st.checkbox("Busca cesta", value=False):
        dados_busca_cesta = carrega_dados(caminho_dados_csa, 'busca_cesta')
        dados_busca_cesta.index = ["carro_1", "carro_2"]
        st.table(dados_busca_cesta)
    
    if st.checkbox("Mutirões", value=False):
        dados_mutiroes = carrega_dados(caminho_dados_csa, 'mutiroes')
        dados_mutiroes.index = ["objetivo", "presença_confirmada"]
        st.table(dados_mutiroes)
    
    
    st.write("-------------------------------------------")
    
    st.markdown("**Extra:** :books: :telephone:")
    if st.checkbox("Informações nutricionais dos alimentos da CSA (em construção)", value=False):
        dados_nutricao = carrega_dados(caminho_dados_csa, 'info_nutricional')
        info_alimento = dados_nutricao["Alimento"].values
        info_nutricional = dados_nutricao.columns[2:]

        opcao_info_nutricional = st.selectbox("informação nutricional",info_nutricional)

        opcao_alimento_1 = st.selectbox("alimento",info_alimento, index = 1)
        opcao_alimento_2 = st.selectbox("  alimento",info_alimento, index = 3)
        opcao_alimento_3 = st.selectbox("  alimento ",info_alimento, index = 5)
        opcao_alimento_4 = st.selectbox("   alimento",info_alimento, index = 13)
        

        figura = grafico_comparativo(dados_nutricao,[opcao_alimento_1, 
                                                     opcao_alimento_2,
                                                     opcao_alimento_3, 
                                                     opcao_alimento_4], opcao_info_nutricional)
        st.pyplot(figura)
        
    if st.checkbox("Contatos", value=False):
        st.markdown("[Instagram](https://www.instagram.com/csa_pindorama/) :sunflower:")
        st.markdown("[Facebook](https://www.facebook.com/stnossasenhora/) :hibiscus:")
    
if __name__ == "__main__":
    main()
    
  

