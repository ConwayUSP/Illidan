# Políticas e Funções de Valor

Dinâmica do ambiente (probabilidade de transição de estado e recompensa):

$$
p(s', r \mid s, a) \doteq \Pr\{S_t=s', R_t=r \mid S_{t-1}=s, A_{t-1}=a\},
$$

---

A soma das probabilidades de transição deve ser igual a 1:

$$
\sum_{s' \in \mathcal{S}} \sum_{r \in \mathcal{R}} p(s', r \mid s, a) = 1, \quad \text{for all } s \in \mathcal{S}, a \in \mathcal{A}(s).
$$

---

Função de valor de estado $v_\pi(s)$:

$$
v_\pi(s) \doteq \mathbb{E}_\pi[G_t \mid S_t=s] = \mathbb{E}_\pi\left[\sum_{k=0}^\infty \gamma^k R_{t+k+1} \mid S_t=s\right], \quad \text{for all } s \in \mathcal{S},
$$

---

Equação de Bellman para $v_\pi(s)$:

$$
\begin{aligned}
v_\pi(s) &\doteq \mathbb{E}_\pi[G_t \mid S_t=s] \\
&= \mathbb{E}_\pi[R_{t+1} + \gamma G_{t+1} \mid S_t=s] \\
&= \sum_a \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma \mathbb{E}_\pi[G_{t+1} \mid S_{t+1}=s'] \right] \\
&= \sum_a \pi(a \mid s) \sum_{s', r} p(s', r \mid s, a) [r + \gamma v_\pi(s')], \quad \text{for all } s \in \mathcal{S},
\end{aligned}
$$

---

Equação de otimalidade de Bellman para $v_{*}(s)$:

$$
\begin{aligned}
v_{*}(s) &= \max_{a \in \mathcal{A}(s)} q_{\pi_{*}}(s, a) \\
&= \max_a \mathbb{E}_{\pi_{*}}[G_t \mid S_t=s, A_t=a] \\
&= \max_a \mathbb{E}_{\pi_{*}}[R_{t+1} + \gamma G_{t+1} \mid S_t=s, A_t=a] \\
&= \max_a \mathbb{E}[R_{t+1} + \gamma v_{*}(S_{t+1}) \mid S_t=s, A_t=a] \\
&= \max_a \sum_{s', r} p(s', r \mid s, a) [r + \gamma v_{*}(s')].
\end{aligned}
$$

---

Função de valor de ação $q_\pi(s, a)$:

$$
q_\pi(s, a) \doteq \mathbb{E}_\pi[G_t \mid S_t=s, A_t=a] = \mathbb{E}_\pi\left[\sum_{k=0}^\infty \gamma^k R_{t+k+1} \mid S_t=s, A_t=a\right].
$$

---

Equação de otimalidade de Bellman para $q_{*}(s, a)$:

$$
\begin{aligned}
q_{*}(s, a) &= \mathbb{E} \left[ R_{t+1} + \gamma \max_{a'} q_{*}(S_{t+1}, a') \mid S_t=s, A_t=a \right] \\
&= \sum_{s', r} p(s', r \mid s, a) \left[ r + \gamma \max_{a'} q_{*}(s', a') \right].
\end{aligned}
$$
