# Illidan

O objetivo deste projeto é construir um material teórico, didático e com exemplos de código que abordem Processos Markovianos de Decisão (PMD ou MDPs) em ambientes interativos gráficos, como jogos/simulações.

## Ementa

A ementa a respeito deste projeto contém as seguintes seções:

1. Resumo acerca de pré-requisitos em Probabilidade e Estatística;

2. Resumo acerca das ferramentas utilizadas;

3. Principais pontos a respeito de formalismos de Processos Markovianos de Decisão e Aprendizado por Reforço;

4. Implementações básicas de algoritmos fundamentais de programação dinâmica;

5. API entre C++ e Python, criando wrappers;

6. Aplicabilidade em jogos e simulações.

## APIs e Tecnologias

### [Gymnasium](https://gymnasium.farama.org/): "An API standard for reinforcement learning with a diverse collection of reference environments."

### [Matplotlib](https://matplotlib.org/): "Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python."

### [Cython](https://cython.org/): "Cython is an optimising static compiler for both the Python programming language and the extended Cython programming language (based on Pyrex). It makes writing C extensions for Python as easy as Python itself."

### [Eigen](https://libeigen.gitlab.io/): "Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms."

### [<Random>](https://cplusplus.com/reference/random/?kw=random): "This header introduces random number generation facilities."

## Bibliografia

A base teórica a respeito de MDPs terá como principal referência:

### _Reinforcement Learning, An Introduction. Second Edition - Sutton & Barto_

Revisões para Probabilidade e Estatística:

### _DEGROOT, M.H., SCHERVISH, M.J. Probability and Statistics, Addison Wesley, 4th edition (2011)._

Estudos a respeito da modularização e interface C++/Python:

### _Cython: A Guide for Python Programmers, Kurt W. Smith._

## Divertissement: "você não está preparado!"

Illidan Stormrage é um personagem do universo de Warcraft. Conhecido por sua força e habilidade, ele é um dos personagens mais icônicos do jogo, além de ser muito estiloso e popular.

<img src="/assets/Illidan.jpg" width=400>

### O Agente Não Treinado

A frase mais icônica do Illidan encaixa como uma luva na definição de um agente de Aprendizado por Reforço no "Episódio 0". Quando um modelo de RL é instanciado em um ambiente, ele não sabe absolutamente nada sobre as regras do jogo, não sabe o que é bom ou ruim. Ele literalmente **não está preparado**. É através de milhares de tentativas, erros e punições que ele aprende a dominar o ambiente.

### Visão Espectral e a Representação de Estado (MDP)

Illidan sacrificou seus olhos normais e ganhou a "Visão Espectral", permitindo que ele visse a magia e a energia bruta do mundo em vez do mundo físico. Em MDPs, o nosso agente de IA também é "cego" para os gráficos do jogo. Ele não vê as texturas ou a iluminação; ele enxerga apenas a matriz de estados, os valores numéricos, as recompensas e as probabilidades de transição. Ele tem a própria visão espectral.

### Sacrifício pelo Objetivo Maior (Maximização de Recompensa a Longo Prazo)

A história do Illidan é marcada por tomar decisões moralmente duvidosas e aceitar perdas no curto prazo (punições imediatas) com o objetivo de derrotar a Legião Ardente no futuro (a grande recompensa final). Esse é o coração do Aprendizado por Reforço: encontrar uma Política Ótima que maximize a recompensa cumulativa a longo prazo, mesmo que isso signifique perder alguns pontos no presente para ganhar o jogo no final.

## Autor

- [Lucas Neves Souza](https://github.com/fatorarpolinomio)
