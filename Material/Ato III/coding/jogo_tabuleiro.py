"""
Jogo de tabuleiro 2D simples (tkinter).

Regras:
- O tabuleiro tem várias casas numeradas (0 = início, última = chegada).
- A cada turno o jogador escolhe UM entre dois dados diferentes.
- O peão anda o número de casas sorteado pelo dado escolhido.
- Vence quem parar EXATAMENTE na casa final primeiro.
- Se o resultado do dado ultrapassar a casa final, o peão "rebate": anda até
  a última casa e recua o número de casas que sobraram.
  Ex.: com 6 casas (1 a 6), peão na 5 e resultado 2 -> sobra 1 -> fica na 5.

Jogadores:
- Humano: escolhe o dado clicando em um dos botões.
- Computador: usa a classe JogadorComputador. A lógica de escolha do dado
  está em `escolher_dado` e deve ser implementada por você (ver TODO).
"""

import random
import tkinter as tk
from abc import ABC, abstractmethod
from tkinter import messagebox

# ----------------------------------------------------------------------
# Configurações do jogo (fáceis de alterar)
# ----------------------------------------------------------------------
LINHAS = 5
COLUNAS = 6
TOTAL_CASAS = LINHAS * COLUNAS      # casas de 0 até TOTAL_CASAS - 1
TAMANHO_CASA = 70                   # pixels
MARGEM = 20


# ----------------------------------------------------------------------
# Dados
# ----------------------------------------------------------------------
class Dado:
    """Um dado definido pela lista de valores de suas faces."""

    def __init__(self, nome, faces):
        self.nome = nome
        self.faces = list(faces)

    def lancar(self):
        return random.choice(self.faces)

    def descricao(self):
        return "Faces: " + ", ".join(str(f) for f in self.faces)

    def media(self):
        return sum(self.faces) / len(self.faces)

    def __repr__(self):
        return f"Dado({self.nome!r})"


# Dois dados diferentes: um "seguro" e um "arriscado" (pode não andar,
# mas também pode andar mais). Altere à vontade.
DADO_COMUM = Dado("Dado Comum", [1, 2, 3, 4, 5, 6])
DADO_ARRISCADO = Dado("Dado Arriscado", [0, 0, 2, 4, 6, 8])


# ----------------------------------------------------------------------
# Jogadores
# ----------------------------------------------------------------------
class Jogador(ABC):
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
        self.posicao = 0

    @property
    @abstractmethod
    def eh_humano(self):
        ...

    @abstractmethod
    def escolher_dado(self, jogo):
        """Retorna o Dado escolhido para a jogada atual."""
        ...


class JogadorHumano(Jogador):
    eh_humano = True

    def escolher_dado(self, jogo):
        # A escolha do humano vem dos botões da interface, não daqui.
        raise NotImplementedError("O humano escolhe o dado pela interface.")


class JogadorComputador(Jogador):
    eh_humano = False

    def escolher_dado(self, jogo):
        """
        TODO: implemente aqui a lógica do computador.

        Informações úteis disponíveis:
            jogo.dados                       -> lista com os dois dados
            self.posicao                     -> posição atual deste jogador
            jogo.meta                        -> índice da casa de chegada
            jogo.casas_restantes(self)       -> casas que faltam até a meta
            jogo.adversarios(self)           -> lista de outros jogadores
            jogo.calcular_destino(pos, val)  -> casa final (já considera o recuo)
            dado.faces / dado.media()        -> para calcular probabilidades

        Deve retornar um dos objetos presentes em `jogo.dados`.
        """
        # Lógica provisória: escolhe aleatoriamente.
        return random.choice(jogo.dados)


# ----------------------------------------------------------------------
# Lógica do jogo (sem interface gráfica)
# ----------------------------------------------------------------------
class Jogo:
    def __init__(self, jogadores, dados, total_casas=TOTAL_CASAS):
        self.jogadores = jogadores
        self.dados = dados
        self.meta = total_casas - 1
        self.indice_turno = 0
        self.vencedor = None
        self.rodadas = 0

    @property
    def jogador_atual(self):
        return self.jogadores[self.indice_turno]

    def casas_restantes(self, jogador):
        return self.meta - jogador.posicao

    def adversarios(self, jogador):
        return [j for j in self.jogadores if j is not jogador]

    def calcular_destino(self, posicao, valor):
        """
        Calcula a casa final de um peão que sai de `posicao` e anda `valor` casas.
        Se passar da meta, recua a diferença (rebate na casa final).
        Útil também para o algoritmo do computador simular jogadas.
        """
        destino = posicao + valor
        while destino > self.meta:
            destino = self.meta - (destino - self.meta)
        return max(destino, 0)

    def jogar(self, dado):
        """
        Executa a jogada do jogador atual.
        Retorna (jogador, antes, valor, recuou), onde `recuou` indica se o
        peão ultrapassou a meta e precisou voltar casas.
        """
        jogador = self.jogador_atual
        antes = jogador.posicao
        valor = dado.lancar()
        recuou = antes + valor > self.meta
        jogador.posicao = self.calcular_destino(antes, valor)

        if jogador.posicao == self.meta:
            self.vencedor = jogador
        else:
            self.indice_turno = (self.indice_turno + 1) % len(self.jogadores)
            if self.indice_turno == 0:
                self.rodadas += 1
        return jogador, antes, valor, recuou


# ----------------------------------------------------------------------
# Interface gráfica
# ----------------------------------------------------------------------
class App:
    def __init__(self, raiz, jogo):
        self.raiz = raiz
        self.jogo = jogo
        raiz.title("Jogo de Tabuleiro")
        raiz.resizable(False, False)

        self.lbl_status = tk.Label(raiz, font=("Arial", 14, "bold"), pady=6)
        self.lbl_status.pack()

        largura = COLUNAS * TAMANHO_CASA + 2 * MARGEM
        altura = LINHAS * TAMANHO_CASA + 2 * MARGEM
        self.canvas = tk.Canvas(raiz, width=largura, height=altura, bg="#f4f1ea",
                                highlightthickness=0)
        self.canvas.pack(padx=10)

        # Botões de escolha do dado
        self.frame_dados = tk.Frame(raiz, pady=8)
        self.frame_dados.pack()
        self.botoes = []
        for dado in jogo.dados:
            botao = tk.Button(
                self.frame_dados,
                text=f"{dado.nome}\n{dado.descricao()}",
                width=30, height=3,
                command=lambda d=dado: self.humano_escolheu(d),
            )
            botao.pack(side="left", padx=8)
            self.botoes.append(botao)

        # Histórico de jogadas
        self.log = tk.Text(raiz, height=7, width=70, state="disabled")
        self.log.pack(padx=10, pady=(0, 10))

        self.desenhar_tabuleiro()
        self.desenhar_pecas()
        self.iniciar_turno()

    # ---------- desenho ----------
    def centro_da_casa(self, posicao):
        """Tabuleiro em 'serpentina', começando no canto inferior esquerdo."""
        linha = posicao // COLUNAS
        coluna = posicao % COLUNAS
        if linha % 2 == 1:
            coluna = COLUNAS - 1 - coluna
        linha_tela = LINHAS - 1 - linha
        x = MARGEM + coluna * TAMANHO_CASA + TAMANHO_CASA / 2
        y = MARGEM + linha_tela * TAMANHO_CASA + TAMANHO_CASA / 2
        return x, y

    def desenhar_tabuleiro(self):
        metade = TAMANHO_CASA / 2
        for pos in range(TOTAL_CASAS):
            x, y = self.centro_da_casa(pos)
            if pos == 0:
                cor = "#b7e4c7"      # início
            elif pos == self.jogo.meta:
                cor = "#ffd166"      # chegada
            else:
                cor = "#ffffff" if pos % 2 == 0 else "#e9e4d8"
            self.canvas.create_rectangle(x - metade, y - metade, x + metade, y + metade,
                                         fill=cor, outline="#8d8878", width=2)
            texto = str(pos)
            if pos == 0:
                texto = "INÍCIO"
            elif pos == self.jogo.meta:
                texto = "CHEGADA"
            self.canvas.create_text(x - metade + 6, y - metade + 6, text=texto,
                                    anchor="nw", font=("Arial", 9, "bold"), fill="#555")

    def desenhar_pecas(self):
        self.canvas.delete("peao")
        raio = 14
        n = len(self.jogo.jogadores)
        for i, jogador in enumerate(self.jogo.jogadores):
            x, y = self.centro_da_casa(jogador.posicao)
            # desloca os peões para que não fiquem um sobre o outro
            dx = (i - (n - 1) / 2) * (2 * raio + 4)
            cx, cy = x + dx, y + 18
            self.canvas.create_oval(cx - raio, cy - raio, cx + raio, cy + raio,
                                    fill=jogador.cor, outline="black", width=2, tags="peao")
            self.canvas.create_text(cx, cy, text=jogador.nome[0], fill="white",
                                    font=("Arial", 10, "bold"), tags="peao")

    def escrever_log(self, texto):
        self.log.config(state="normal")
        self.log.insert("end", texto + "\n")
        self.log.see("end")
        self.log.config(state="disabled")

    def habilitar_botoes(self, habilitar):
        for botao in self.botoes:
            botao.config(state="normal" if habilitar else "disabled")

    # ---------- fluxo do jogo ----------
    def iniciar_turno(self):
        if self.jogo.vencedor:
            return
        jogador = self.jogo.jogador_atual
        self.lbl_status.config(text=f"Vez de: {jogador.nome}", fg=jogador.cor)

        if jogador.eh_humano:
            self.habilitar_botoes(True)
        else:
            self.habilitar_botoes(False)
            self.raiz.after(900, self.turno_computador)

    def humano_escolheu(self, dado):
        self.habilitar_botoes(False)
        self.executar_jogada(dado)

    def turno_computador(self):
        jogador = self.jogo.jogador_atual
        dado = jogador.escolher_dado(self.jogo)
        if dado not in self.jogo.dados:       # proteção contra escolha inválida
            dado = random.choice(self.jogo.dados)
        self.executar_jogada(dado)

    def executar_jogada(self, dado):
        jogador, antes, valor, recuou = self.jogo.jogar(dado)
        mensagem = (
            f"{jogador.nome} escolheu '{dado.nome}' e tirou {valor}: "
            f"casa {antes} → {jogador.posicao}"
        )
        if recuou:
            mensagem += "  (passou da chegada e recuou!)"
        self.escrever_log(mensagem)
        self.desenhar_pecas()

        if self.jogo.vencedor:
            self.finalizar()
        else:
            self.raiz.after(700, self.iniciar_turno)

    def finalizar(self):
        vencedor = self.jogo.vencedor
        self.lbl_status.config(text=f"{vencedor.nome} venceu!", fg=vencedor.cor)
        self.habilitar_botoes(False)
        messagebox.showinfo("Fim de jogo",
                            f"{vencedor.nome} chegou primeiro à casa final!")


# ----------------------------------------------------------------------
# Execução
# ----------------------------------------------------------------------
def main():
    jogadores = [
        JogadorHumano("Você", "#1d6fd1"),
        JogadorComputador("Computador", "#d1341d"),
    ]
    jogo = Jogo(jogadores, [DADO_COMUM, DADO_ARRISCADO])

    raiz = tk.Tk()
    App(raiz, jogo)
    raiz.mainloop()


if __name__ == "__main__":
    main()
