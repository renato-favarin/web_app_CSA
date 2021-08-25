<img src="/img/csa_logo.png" alt="CSA Pindorama logo" title="CSA" align="right" height="180" class="center"/>

# Aplicativo web CSA
O aplicativo em produção: http://tiny.cc/csaPindorama

## Contexto

O aplicativo foi desenvolvido para facilitar a programação de compras e unificar um local para a disposição das informações relevantes da CSA (Comunidade que Sustenta a Agricultura) que faço parte. <br>
Pode ser facilmente adaptada para qualquer outra CSA.

## Demonstração do aplicativo

<ADD GIF>

## Fonte de informações

Todas as informações utilizadas pelo aplicativo estão presentes em um único arquivo Excel, dividido em diversas abas:

### produtos
<pre>Lista dos produtos disponíveis 'na_terra', 'na_cesta' e 'novos'. <br>
'na_terra': produtos atualmente em cultivo
'na_cesta': produtos na próxima cesta
'novos': produto no último lote de plantio realizado <br>
basta marcar com um 'x' para instruir o app sobre determinado item <br>

obs.: quando ainda não há nenhum produto previsto na cesta (por ainda estar longe o dia da 
distribuição), basta remover todos os 'x' da coluna 'na_cesta' que um aviso será emitido 
pelo aplicativo.

<p align="center">
  <img src="/img/produtos.png">
</p>

</pre>



### busca_cesta
<pre>Agenda dos coprodutores que buscarão a cesta nos próximos dias.
Conforme os coprodutores vão se planejando, eles informam em algum canal oficial do grupo 
(WhatsApp, Telegram) e é feita a atualização da agenda nesta aba, adicionando os seus nomes.

<p align="center">
  <img src="/img/busca_cesta.png">
</p>

A implementar: flexibilizar a quantidade de carros que irão buscar os itens. 
Por enquanto está fixo em 2 carros por semana, conforme necessidade atual da CSA Pindorama. 
</pre>

### mutiroes
<pre>Futuros mutirões planejadas com identificação do objetivo e participantes. 

<p align="center">
  <img src="/img/mutiroes.png">
</p>

</pre>

### hist_cestas
<pre>Identificação dos itens presentes nas cestas em suas respectivas datas, para controle de histórico.
<p align="center">
  <img src="/img/hist_cestas.png">
</p>
</pre>

### qtde_cestas
<pre>Quantidade de cestas entregues, para controle de histórico. 
<p align="center">
  <img src="/img/qtde_cestas.png">
</p>
</pre>

### info_nutricional
<pre>Informação nutricional obtida de fonte confiável (http://tabnut.dis.epm.br/) dos 
itens em cultivo pela CSA. 
<p align="center">
  <img src="/img/info_nutricional.png">
</p>
</pre>

### hist_plantios
<pre>Identificação dos itens plantados em suas respectivas datas, para controle de histórico. 
<p align="center">
  <img src="/img/hist_plantios.png">
</p>
</pre>

### hist_mutiroes
<pre>Identificação dos mutiróes realizados em suas respectivas datas, para controle de histórico. 
<p align="center">
  <img src="/img/hist_mutiroes.png">
</p>
</pre>

## Futuras melhorias
- avisos: cada app poderá ter a quantidade e os avisos que desejarem; a fonte de informação será uma nova aba
- contatos: cada app poderá ter a quantidade de contatos que quiser; a fonte de informação também será uma nova aba
