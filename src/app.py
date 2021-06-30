import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title= "CSA Pindorama", page_icon=':seedling:')

def carrega_dados(caminho, aba, ignora_primeira_linha_coluna = False):
    if ignora_primeira_linha_coluna == True:
        dados = pd.read_excel(caminho, sheet_name = aba, skiprows = [0])
        if dados.shape[0] != 0:
            dic_mes = {'1': 'jan', '2': 'fev', '3': 'mar', '4': 'abr', '5': 'may','6': 'jun',
                   '7': 'jul', '8': 'ago', '9': 'set', '10': 'out', '11': 'nov', '12': 'dez'}
            dia = dados["Unnamed: 0"].dt.day
            mes = dados["Unnamed: 0"].dt.month
            dados["Unnamed: 0"] = dados["Unnamed: 0"].dt.day.map(str) + "/" + dados["Unnamed: 0"].dt.month.map(str).apply(lambda x: dic_mes[x])
            dados = dados.set_index("Unnamed: 0")                
    else:
        dados = pd.read_excel(caminho, sheet_name = aba)
        
    return dados


def grafico_comparativo(dados_nutricao, lista_alimentos, atributo):
    df = dados_nutricao.set_index('alimento')
    df = df.loc[lista_alimentos]
    
    figura, ax = plt.subplots()
    ax = sns.barplot(data = df, x = df.index, y = atributo)
    ax.set_title(f"{atributo} por 100g de alimento cru")
    ax.set(xlabel=None)
    
    max = 0
    for p in ax.patches:
        ax.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', fontsize=11, color='gray', xytext=(0, 10),
                    textcoords='offset points')
        
        if p.get_height() > max:
            max = p.get_height()
    _ = ax.set_ylim(0,max + 0.2*max) #To make space for the annotations
    
    return figura

def gera_tabela(df, label):
        df = df.sort_values(by='produto')
        df.index = [" "] * len(df)
        df.loc[:,'na_terra'] = " "
        df.loc[:,'na_cesta'] = " "
        df.loc[:,'novos'] = " "
        df.loc[:, ' '] = " "
        df.rename({'produto':label,'na_terra': '   ', 'na_cesta':'  ', 'novos': '   '}, axis='columns', inplace=True)
        st.table(df[[label, '   ', '  ', ' ']])   


def lista_extenso(df,label,emoji):
    st.markdown(f"<font size='5'> {label} </font>", unsafe_allow_html=True)
    for item in df['produto'].sort_values().values:
            st.markdown(f"**{emoji}** <font size='4'> {item} </font>", unsafe_allow_html=True)
        
    st.markdown("")
    st.markdown("")
    
    
def plantio_extenso(df,label):
    st.markdown(f"<font size='5'> {label} </font>", unsafe_allow_html=True)
    for item in df['produto'].values:
            st.markdown(f"**:seedling:** <font size='4'> {item} </font>", unsafe_allow_html=True)
        
    st.markdown("")
    st.markdown("")
    

        
def main():
    
    caminho_dados_csa = "data/csa_pindorama.xlsx"
    dados_csa = carrega_dados(caminho_dados_csa, 'produtos') 
    
    st.title("CSA Pindorama :seedling:")
    #st.subheader("Da cultura do preço para a cultura do apreço")

    st.image("src/logo.jpg", use_column_width=True)
    
    st.markdown("**Aplicativo da CSA Pindorama** :sunrise: :green_salad:")
    
    if st.checkbox("Na terra", value=False):
        st.image("src/na_terra.jpg",use_column_width=True)

            
        na_terra = dados_csa.query("na_terra == 'x'")
        gera_tabela(na_terra, '--produtos em cultivo--')
         

    dados_busca_cesta = carrega_dados(caminho_dados_csa, 'busca_cesta', ignora_primeira_linha_coluna = True)
    # capturar o primeiro índice da aba "busca_cesta", que no caso é a próxima data para buscar cesta
    data = dados_busca_cesta.index[0]
    
    if st.checkbox(f"Na cesta em {data}",value=False):
        st.image("src/na_cesta.jpg",use_column_width=True)
        na_cesta = dados_csa.query("na_cesta == 'x'")
        if na_cesta.shape[0] == 0:
            st.markdown("**:leaves:** <font size='5'> Informações disponíveis até 5ª-feira </font>", unsafe_allow_html=True)
            st.markdown("")
            st.markdown("")
            
        else:
            #gera_tabela(na_cesta, f'--provável cesta em {data} (sujeito à adições)--')
            lista_extenso(na_cesta, f'-- provável cesta em {data} (sujeito à adições) --', ':arrow_forward:')
    
    if st.checkbox(f"Plantios da semana",value=False):
        st.image("src/plantando.jpg",use_column_width=True)
        novos = dados_csa.query("novos == 'x'")
        if novos.shape[0] == 0:
            st.markdown("**:leaves:** <font size='4' color='blue'> Não houve novos plantios nessa semana </font>", unsafe_allow_html=True)
        else:
            #gera_tabela(novos, f'--plantios da semana--')
            lista_extenso(novos, f'--plantios da semana--', ":seedling:")
        
        
        

    st.write("-------------------------------------------")
    
    st.markdown("**Agenda e avisos:** :car: :herb: :newspaper:")
    if st.checkbox("Busca cesta", value=False):
        dados_busca_cesta = carrega_dados(caminho_dados_csa, 'busca_cesta', ignora_primeira_linha_coluna = True)
        st.table(dados_busca_cesta)
    
    if st.checkbox("Mutirões", value=False):
        
        dados_mutiroes = carrega_dados(caminho_dados_csa, 'mutiroes', ignora_primeira_linha_coluna = True)
        if dados_mutiroes.shape[0] == 0:
            st.markdown("**:leaves:** <font size='4'> Não há mutirões agendados </font>", unsafe_allow_html=True)
        else:
            st.table(dados_mutiroes)
            st.markdown("**Atenção:** uso obrigatório de máscara e álcool gel/70% durante todo o mutirão. :mask: ")
        
    if st.checkbox("Avisos", value=False):
        st.markdown("**:heavy_check_mark:** <font size='4'> Cada coagricultor leva o máximo de sacolas possíveis no primeiro sábado, correspondente ao mês todo </font>", unsafe_allow_html=True)
        st.markdown("**:heavy_check_mark:** <font size='4'> Previsão de chegada no sítio para montagem das cestas às 8h30 </font>", unsafe_allow_html=True)
        st.markdown("**:heavy_check_mark:** <font size='4'> Previsão de entrega das cestas na praça Sinésio Martins às 11h </font>", unsafe_allow_html=True)
        st.markdown("**:heavy_check_mark:** <font size='4'> Em caso de mais de 20 cestas, em carro pequeno, solicitar outro coagricultor com carro disponível para ajudar a trazer </font>", unsafe_allow_html=True)
        st.markdown("**:heavy_check_mark:** <font size='4'> Manter a comunicação no dia da distribuição com o grupo do ciclo 2 </font>", unsafe_allow_html=True)
        

    
    st.write("-------------------------------------------")
    
    st.markdown("**Extra:** :books: :telephone:")
    if st.checkbox("Informações nutricionais dos alimentos da CSA", value=False):
        dados_nutricao = carrega_dados(caminho_dados_csa, 'info_nutricional')
        info_alimento = dados_nutricao["alimento"].values
        info_nutricional = dados_nutricao.columns[1:]

        opcao_info_nutricional = st.radio("informação nutricional (a cada 100g de alimento cru):",info_nutricional)
        
        lugar_grafico = st.empty()
        
        opcao_alimento_1 = st.selectbox("alimento:",info_alimento, index = 0)
        opcao_alimento_2 = st.selectbox("  alimento:",info_alimento, index = 3)
        opcao_alimento_3 = st.selectbox("  alimento: ",info_alimento, index = 6)
        opcao_alimento_4 = st.selectbox("   alimento:",info_alimento, index = 10)
        
        figura = grafico_comparativo(dados_nutricao,[opcao_alimento_1, 
                                                     opcao_alimento_2,
                                                     opcao_alimento_3, 
                                                     opcao_alimento_4], opcao_info_nutricional)
        lugar_grafico.pyplot(figura) 
        
        st.markdown("Fonte principal dos dados: [Escola Paulista de Medicina](http://tabnut.dis.epm.br/) :school:")
        
    if st.checkbox("Contatos", value=False):
        st.markdown("[Instagram](https://www.instagram.com/csa_pindorama/) :sunflower:")
        st.markdown("[Facebook](https://www.facebook.com/stnossasenhora/) :hibiscus:")
        st.markdown("[WhatsApp - (12) 99658-1433](https://wa.me/5512996581433) :tulip:")

    
if __name__ == "__main__":
    main()
    

# melhorias
# ajustar fonte dos gráficos (aumentar)
# organizar o notebook
# uma vez com o notebook organizado, criar uma seção para escrever no histórico (cestas e mutirões)
#       para facilitar, criar uma função para escrever o histórico de cestas (copia a aba mutirões e o deixa intacto)
#       e outra função para escrever o histórico de mutirões (copia a aba cesta e a deixa intacta)
