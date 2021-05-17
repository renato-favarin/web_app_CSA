import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def carrega_dados(caminho):
    dados_nutricao = pd.read_csv(caminho, decimal=",")
    dados_nutricao = dados_nutricao.replace('t', 0)
    return dados_nutricao


def grafico_comparativo(dados_nutricao, lista_alimentos, atributo):
    df = dados_nutricao.set_index('Food')
    df = df.loc[lista_alimentos]
    #plt.figure(figsize = (8,6))
    
    figura, ax = plt.subplots()
    ax = sns.barplot(data = df, x = df.index, y = atributo)
    ax.set_title(f"Comparação de {atributo}")
    
    return figura

def main():
    
    caminho = "data/nutrients_csvfile.csv"
    dados_nutricao = carrega_dados(caminho)
    dados_nutricao = tratamento_dados(dados_nutricao)
    figura = grafico_comparativo(dados_nutricao,["Milk skim", "Fortified milk", "Ice cream"], "Protein")
    
    st.title("CSA Pindorama")
    st.markdown("Aplicação da **CSA Pindorama** :seedling:")
    #st.dataframe(dados_nutricao)
    st.pyplot(figura)
    

def tratamento_dados(dados_nutricao):    
    dados_nutricao["Protein"] = dados_nutricao["Protein"].replace("-1","0", regex=True)
    dados_nutricao["Protein"] = dados_nutricao["Protein"].astype(float)

    # dropar linhas erradas
    dados_nutricao.drop(205, inplace=True)
    dados_nutricao.drop(82, inplace=True)

    # coluna calorias (Calories)
    dados_nutricao["Calories"] = dados_nutricao["Calories"].str.replace(",",".",regex=True)
    # corrigindo as calorias das ervilhas
    dados_nutricao.loc[134, "Calories"] = '36.4'
    # considerando o máximo da faixa de calories das alcachofras
    dados_nutricao.loc[91, "Calories"] = '44'
    dados_nutricao["Calories"] = dados_nutricao["Calories"].astype(float)

    #coluna gordura (Fat)
    dados_nutricao["Fat"] = dados_nutricao["Fat"].astype(float)

    # coluna gordura saturada (Sat.Fat)
    # corrigindo a gordura saturada da carne de porco
    dados_nutricao.loc[42, "Sat.Fat"] = '18.6'
    # corrigindo a gordura saturada da beterraba
    dados_nutricao.loc[100, "Sat.Fat"] = '0'
    dados_nutricao["Sat.Fat"] = dados_nutricao["Sat.Fat"].astype(float)

    # coluna fibra (Fiber)
    # corrigindo o valor da fibra do peixe "cavalinha" 
    dados_nutricao.loc[81, "Fiber"] = '0'
    dados_nutricao["Fiber"] = dados_nutricao["Fiber"].astype(float)

    #coluna carboidrato (Carbs)
    dados_nutricao["Carbs"] = dados_nutricao["Carbs"].astype(float)

    # dropar coluna "Measure" (a coluna gramas permite uma comparação melhor)
    dados_nutricao.drop("Measure", axis = 1, inplace=True)
    
    return dados_nutricao
    
    
    
if __name__ == "__main__":
    main()
    
  

