# Um Exemplo a Ser Modelado

Muito foi dito até aqui a respeito de como os **Markovian Decision Processes** são estruturados conceitualmente. Aproveitamos, também, para apresentar um dos principais algoritmos para processos finitos, utilizado para encontrar a **política ótima** para cada estado.

Agora, chegou o momento de começar a visualizar problemas a serem resolvidos como exemplos a serem modelados. Com isso, estruturamos um exemplo de um jogo simples para fins educativos.


## Chegando o mais rápido possível em algum lugar

Imagine **um jogo de tabuleiro simples**, com casas (posições) e um peão que irá se deslocar através delas. Para isso, você deve escolher entre dois dados, um diferente do outro. A quantidade de casas que o peão andará será o número obtido como resultado no lançamento do dado escolhido. **O objetivo do jogo é chegar o mais rápido possível em uma casa específica pré-definida**.

Caso o valor resultante do dado faça com que **o deslocamento do peão seja superior à posição final**, **o peão deve andar "para trás" o número de casas equivalente à diferença**. Então, por exemplo, caso existam seis casas, o peão esteja na posição cinco e, ao selecionar o dado, o resultado seja dois, a localização final do peão será a casa cinco.

(Inserir imagens de um peão, alguns dados e um tabuleiro)

Com a descrição acima, é factível já começar a pensar na modelagem por conta própria. **Vamos construir um algoritmo para encontrar a política ótima para cada estado**. Recomendamos que você tente fazer isso antes de ver a nossa resolução proposta.

### Planejando

Precisamos definir o que seria, exatamente, os elementos centrais do nosso **MDP** para o problema apresentado.

Vamos começar pensando em um caso mais simples, menos genérico, para alinhar o nosso pensamento. 

Pensemos, por exemplo, em um tabuleiro com **seis posições**. A posição a qual queremos chegar o mais rápido possível é, no caso, a **sexta e última posição**. Os dados os quais podemos escolher são um **D2** e um **D3**, ambos não são viciados.

Agora, que reduzimos o escopo, vamos lá:

Inicialmente, podemos definir os **estados** como sendo cada uma das casas. Assim, vamos definir uma lista que contenha cada uma delas:

```python
estados = [0, 1, 2, 3, 4, 5]
```

Cada número representa uma das posições. Definir numericamente costuma ser mais simples de trabalhar na programação!

No nosso problema, quais seriam as ações que poderíamos tomar? Ora, a decisão que será capaz de alterar o estado em que estamos de maneira probabilística é, justamente, **a escolha de um dado para ser lançado**. Podemos definir duas variáveis:

```python
d2 = [1, 2]
d3 = [1, 2, 3]
```

Essas serão as nossas ações. Podemos, para fins de organização (ou não), enumerá-las da seguinte maneira:

```python
acoes = [0, 1]
```

Aqui, o número **zero** vai dizer respeito ao `d2`, enquanto que o **um** será referente ao `d3`. Não é muito intuitivo, mas vai servir.

É importante, também, definir as recompensas. A nossa lista de recompensas, onde cada índice diz respeito a um estado, será:

```python
recompensas_por_estado = [-1, -1, -1, -1, -1, 0]
```

No caso, as nossas recompensas são -1 em todas as posições, com exceção da última. Essa decisão visa indicar que estar em qualquer estado, que não seja o último, é igualmente ruim no que tange ao objetivo final. É um pouco estranho à primeira vista, especialmente se você levar em consideração que estar em uma posição mais próxima da sexta é melhor do que o contrário. Mas, nosso objetivo não é apenas se aproximar, e sim chegar ao destino. Logo, o nosso agente só deixará de obter prejuízos quando chegar no seu objetivo.

Até então, já definimos três elementos da nossa tupla $\langle \mathcal{S}, \mathcal{A}, T, R \rangle$. Para definir o nosso **MDP** em sua totalidade, precisamos daquilo que define **a dinâmica do problema**: a nossa **função de transição**.

Como se trata de um problema de escopo reduzido, podemos, por enquanto, usufruir de uma **matriz de transições para cada ação**.

Lembrando que, aqui, cada linha diz respeito ao **estado inicial**, enquanto que cada coluna diz respeito ao **estado final**.

Considerando a **Ação 0**, o nosso **D2**, como ficaria a primeira linha da matriz?

1) Não é possível transitarmos da posição zero para ela mesma, logo, a probabilidade na **linha 0** e na **coluna 0** será **zero**;
2) No lançamento do dado, a probabilidade de obtermos 1 ou 2 será igual. Assim, poderemos transitar tanto para o **Estado 1** quanto para o **Estado 2** com chances iguais, que será **1/2**;
3) Os demais estados não poderão ser alcançados a partir de um único lançamento.

Teremos, então, a seguinte linha referente ao **Estado de Partida sendo o Estado 0**:

```python
transicao_d2 = [
    [0, 1/2, 1/2, 0, 0, 0]
]
```

Para a segunda, terceira e quarta linha, teremos **basicamente a mesma lógica aplicada acima**. O estado de onde partiremos não poderá ser alcançado a partir de um único lançamento e poderemos alcançar as duas posições seguintes com iguais probabilidades! Assim, nossas linhas ficarão:

```python
transicao_d2 = [
    [0, 1 / 2, 1 / 2,   0,     0,     0],
    [0,   0,   1 / 2, 1 / 2,   0,     0],
    [0,   0,     0,   1 / 2, 1 / 2,   0],
    [0,   0,     0,     0,   1 / 2, 1 / 2],
]
```

Agora, para as linhas seguintes, teremos algumas diferenças. Lembre-se que o nosso peão pode acabar voltando para casas anteriores caso o valor obtido a partir do lançamento faça com que **a posição final dele exceda a última casa**.

Logo, caso o peão esteja na posição cinco e o resultado do lançamento do dado seja 2, **ele poderá retornar para a própria posição 5**. Além disso, ele pode transitar com igual probabilidade para a casa 6. Logo, teremos:

```python
transicao_d2 = [
    [0, 1 / 2, 1 / 2,   0,     0,     0],
    [0,   0,   1 / 2, 1 / 2,   0,     0],
    [0,   0,     0,   1 / 2, 1 / 2,   0],
    [0,   0,     0,     0,   1 / 2, 1 / 2],
    [0,   0,     0,     0,   1 / 2, 1 / 2],
]
```

E se o peão estiver na casa 6? O jogo já terá terminado! Representamos isso ao colocar 1 na casa 6:

```python
transicao_d2 = [
    [0, 1 / 2, 1 / 2,   0,     0,     0],
    [0,   0,   1 / 2, 1 / 2,   0,     0],
    [0,   0,     0,   1 / 2, 1 / 2,   0],
    [0,   0,     0,     0,   1 / 2, 1 / 2],
    [0,   0,     0,     0,   1 / 2, 1 / 2],
    [0,   0,     0,     0,     0,     1],
]
```

Então, já temos em mãos **a matriz de transição para a ação 0**!

No que diz respeito à matriz para a ação 0, sua construção passo a passo fica como exercício para o leitor. A sua forma final será:

```python
transicao_d3 = [
    [0, 1 / 3, 1 / 3, 1 / 3,   0,     0],
    [0,   0,   1 / 3, 1 / 3, 1 / 3,   0],
    [0,   0,     0,   1 / 3, 1 / 3, 1 / 3],
    [0,   0,     0,     0,   2 / 3, 1 / 3],
    [0,   0,     0,   1 / 3, 1 / 3, 1 / 3],
    [0,   0,     0,     0,     0,     1],
]
```

Temos, enfim, a definição do nosso **MDP**. Podemos utilizar, então, o `Value Iteration` para encontrar a política ótima em cada estado.

Podemos definir a nossa lista `trans_func_per_action` apenas como sendo uma lista com cada uma das matrizes:

```python
trans_func_per_action = [transicao_d2, transicao_d3]
```

Como construímos a versão de `value_iteration` pensando na utilização das matrizes de transição, isso será suficiente para obtermos uma lista com a política ótima para cada estado. Vamos chamar a função:

(Colocar chamada de função, atribuições e print)

Assim, teremos como resultado final:

```sh
[1, 1, 1, 0, 0, 1]
```
