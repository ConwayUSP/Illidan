# Processos Markovianos de Decisão

Agora, com a base necessária, podemos começar a pensar no que seriam os **Processos Markovianos de Decisão (Markovian Decision Process - MDP)**.

## Algumas Noções

Estudar **MDPs** é estudar **situações e possibilidades**. Quando entendemos esses pontos a respeito do que estabelecemos como objeto de estudo, entedemos como funciona o nosso **mundo**. Quando temos em mente a **dinâmica** do nosso mundo, podemos começar a realizar os nossos planejamentos, de modo a otimizar nossos benefícios naquele contexto.

Definir uma entidade que **vivencia o mundo**, tomando **decisões sequenciais (encadeadas)** com diferentes resultados possíveis, é definir um **agente**. Esse agente pode ser uma espécie de "robô", que controla um personagem de um jogo, por exemplo.

São chamadas de **estados** as **situações** nas quais o **agente** pode acabar se encontrando. Suas decisões são **ações tomadas** deles. 

Cada ação tomada pode fazer com que o agente **transite** para um estado diferente. Cada uma dessas transições produz uma **recomensa** para o agente, a qual, dentre outras coisas, indica o quão bom é estar naquele estado.

## Definindo

Então, no fim das contas, como se define um **MDP**? Um **Processo Markoviano de Decisão** é definido por uma **tupla** é definido por uma tupla $\langle \mathcal{S}, \mathcal{A}, T, R \rangle$ onde:

  - $s \in \mathcal{S}$ são estados possíveis;
  - $a \in \mathcal{A}$ são ações possíveis;
  - $T : \mathcal{S} \times \mathcal{A} \times \mathcal{S} \to [0, 1]$ é a função de transição; e
  - $R : \mathcal{S} \times \mathcal{A} \times \mathcal{S} \to \mathbb{R}$ é a função recompensa.


## A Interface Agente-Ambiente

Durante um **processo de tomada de decisão sequencial**, por parte de um **agente**, temos a sua interação com o ambiente através da escolha de ações. Cada "momento", ou unidade de tempo, que decorre durante o processo é chamado de **episódio**.

(Colocar imagem do diagrama)

Observando a imagem acima, é possível perceber o ciclo:

1) No momento `t`, o agente no estado `St` toma a ação `At`;

2) Interagindo com o ambiente, essa ação faz com que o agente transite, no próximo episódio `t+1`, para o estado `S(t+1)`, produzindo a recompensa `R(t+1)`;

3) E, assim sucessivamente.

No caso, o agente e o ambiente interagem em cada **sequência discreta de tempo**, `t = 0, 1, 2, ...`. O MDP e o agente, juntos, formam uma **trajetória** ou uma **sequência** que começa da seguinte maneira:

`S0, A0, R1, S1, A1, R2, S2, A2, R3, ...`
