# Um Exemplo a Ser Modelado

Muito foi dito até aqui a respeito de como os **Markovian Decision Processes** são estruturados conceitualmente. Aproveitamos, também, para apresentar um dos principais algoritmos para processos finitos, utilizado para encontrar a **política ótima** para cada estado.

Agora, chegou o momento de começar a visualizar problemas a serem resolvidos como exemplos a serem modelados. Com isso, estruturamos um exemplo de um jogo simples para fins educativos.


## Chegando o mais rápido possível em algum lugar

Imagine um jogo de tabuleiro simples, com casas (posições) e um peão que irá se deslocar através delas. Para isso, você deve escolher entre dois dados, um diferente do outro. A quantidade de casas que o peão andará será o número obtido como resultado no lançamento do dado escolhido. O objetivo do jogo é chegar o mais rápido possível em uma casa específica pré-definida.

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

Aqui, o número **zero** vai dizer respeito ao `d2`, enquanto que o **um** será referente ao `d3`.
