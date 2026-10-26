# Distribuições Típicas de Variáveis Aleatórias Discretas

## 1. Distribuição de Bernoulli
Uma variável aleatória $X$ que toma apenas dois valores (0 e 1) com $Pr(X=1)=p$ tem a distribuição de Bernoulli com parâmetro $p$.

$$f(x;p) = \begin{cases} 
p & \text{se } x=1 \\\\ 
1-p & \text{se } x=0 
\end{cases}$$

**Exemplos:** cara ou coroa, filtro de spam, reconhecimento de objetos, diagnóstico de doença, etc.

## 2. Distribuição Uniforme sobre Inteiros
Seja $a \le b$ inteiros. Suponha que o valor de uma variável aleatória $X$ é igualmente provável ser cada um dos inteiros $a, a+1, ..., b-1, b$. Então $X$ tem uma distribuição uniforme sobre inteiros $a, a+1, ..., b-1, b$ e a função de probabilidade é dada por:

$$f(x;a,b) = \begin{cases} 
\frac{1}{b-a+1} & \text{se } x \in \{a,...,b\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

## 3. Distribuição Binomial
$x$ é a quantidade de acertos em $n$ tentativas com chance de sucesso $p$. A função de probabilidade com parâmetros $n$ e $p$ é:

$$f(x;n,p) = \begin{cases} 
\binom{n}{x}p^x(1-p)^{n-x} & \text{se } x \in \{0,1,...,n\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

## 4. Distribuição Hipergeométrica
Considere $A$ elementos de um tipo e $B$ elementos de um segundo tipo, então $x$ é a quantidade de elementos dentre os $A$ elementos, quando realizados $n$ sorteios sem reposição nos $A+B$ elementos. A função de probabilidade com parâmetros $A$, $B$ e $n$ (para $A+B \ge n$) é:

$$f(x;A,B,n) = \begin{cases} 
\frac{\binom{A}{x}\binom{B}{n-x}}{\binom{A+B}{n}} & \text{se } \max\{0,n-B\} \le x \le \min\{n,A\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

*Nota: A distribuição binomial é o limite da distribuição hipergeométrica quando $A \rightarrow \infty$, $B \rightarrow \infty$ e $\frac{A}{A+B} \rightarrow p$.*

## 5. Distribuição Geométrica
$x$ é a quantidade de tentativas até obter um sucesso, sendo que a chance de obter sucesso em uma tentativa é $p$. A função de probabilidade com parâmetro $p$ é:

$$f(x;p) = \begin{cases} 
(1-p)^{x-1}p & \text{se } x \in \{1,2,...\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

*Propriedade de Falta de Memória:* Deixe $X$ ter a distribuição geométrica com parâmetro $p$ e seja $k \ge 0$. Então para todo inteiro $t \ge 0$:
$$Pr(X=N+t \mid X>N) = Pr(X=t)$$

## 6. Distribuição Binomial Negativa
$x$ é a quantidade de tentativas até obter $k$ sucessos, sendo que a chance de obter sucesso em uma tentativa é $p$. A função de probabilidade com parâmetros $p$ e $k$ é:

$$f(x;k,p) = \begin{cases} 
\binom{x-1}{k-1}(1-p)^{x-k}p^k & \text{se } x \in \{k,k+1,...\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

## 7. Distribuição de Poisson
$x$ é a quantidade de ocorrências em um intervalo de tempo. $\lambda$ é a esperança (média) de eventos nesse intervalo. A função de probabilidade com parâmetro $\lambda$ é:

$$f(x;\lambda) = \begin{cases} 
\frac{e^{-\lambda}\lambda^x}{x!} & \text{se } x \in \{0,1,...\} \\\\ 
0 & \text{caso contrário} 
\end{cases}$$

*Propriedades:*
* Em um processo de Poisson, o número de chegadas em toda coleção de intervalos de tempo disjuntos são independentes.
* Considere $N$ variáveis aleatórias $X_i$ que seguem a distribuição de Poisson com respectivo parâmetro $\lambda_i$, então a variável aleatória $Y = \sum_{i=1}^N X_i$ também é uma distribuição de Poisson com $\lambda = \sum_{i=1}^N \lambda_i$.
* A distribuição de Poisson é o limite da distribuição binomial quando $n \rightarrow \infty$ e $pn \rightarrow \lambda$.

---

# Resumo das Distribuições

| Distribuição | Função distribuição $f(x)$ | Esperança $E[X]$ | Variância $Var[X]$ |
| :--- | :--- | :--- | :--- |
| **Uniforme** | $f(x)=\frac{1}{b-a+1}$ | $E[X]=\frac{a+b}{2}$ | $Var[X]=\frac{(b-a)(b-a+2)}{12}$ |
| **Bernoulli** | $f(x)=p^x(1-p)^{1-x}$ | $E[X]=p$ | $Var[X]=p(1-p)$ |
| **Binomial** | $f(x)=\binom{n}{x}p^x(1-p)^{n-x}$ | $E[X]=np$ | $Var[X]=np(1-p)$ |
| **Hipergeométrica** | $f(x)=\frac{\binom{A}{x}\binom{B}{n-x}}{\binom{A+B}{n}}$ | $E[X]=n\frac{A}{A+B}$ | $Var[X]=n\frac{AB}{(A+B)^2}\frac{A+B-n}{A+B-1}$ |
| **Geométrica** | $f(x)=(1-p)^{x-1}p$ | $E[X]=\frac{1}{p}$ | $Var[X]=\frac{1-p}{p^2}$ |
| **Binomial Negativa** | $f(x)=\binom{x-1}{k-1}(1-p)^{x-k}p^k$ | $E[X]=k\frac{1}{p}$ | $Var[X]=k\frac{1-p}{p^2}$ |
| **Poisson** | $f(x)=e^{-\lambda}\frac{\lambda^x}{x!}$ | $E[X]=\lambda$ | $Var[X]=\lambda$ |

# Referências & Agradecimentos

Este capítulo foi baseado no material das aulas de **Introdução a Estatística** do [Professor Doutor Valdinei Freire](https://www.each.usp.br/valdinei/) da **EACH-USP**, com sua permissão concedida diretamente.
