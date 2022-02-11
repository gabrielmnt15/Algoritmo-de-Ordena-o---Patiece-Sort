# Algoritmo-de-Ordenação - Patience-Sort
Um algoritmo de ordenação simples feito como um desafio pra um trabalho de faculdade, implementado em Python.

## Funcionamento
<p>Ele recebe esse nome por seguir uma lógica semelhante a resolução de um jogo de paciência, sendo que trata cada elemento da de um array 
como uma carta e faz a ordenação se utilizando de pilhas.</p>
<p>O algoritmo recebe um array desordenado e retira um elemento de cada vez os organizando em pilhas segundo as seguintes regras:</p>
<o> 
  <li>Cada elemento só pode ser colocado sobre um elemento maior.</li>
  <li>Caso não haja nenhuma pilha que satisfaça a condição anterior, então cria-se uma nova pilha.</li>
  <li>Repete-se o processo até que todos os elementos estejam ordenados nas pilhas e então se checa o topo de cada pilha buscando o menor elemento assim se faz a ordenação.</li>
</o>
