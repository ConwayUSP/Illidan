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
