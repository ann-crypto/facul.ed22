#arvore pos ordem
class No:

    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def obtervalor(self):
        return self.valor

    def setesquerda(self, esquerda):
        self.esquerda = esquerda

    def setdireita(self, direita):
        self.direita = direita

    def obteresquerda(self):
        return self.esquerda

    def obterdireita(self):
        return self.direita


class ArvoreBinariaBusca:

    def __init__(self):
        self.raiz = None

    def obterraiz(self):
        return self.raiz

    def insere(self, valor):
        no = No(valor)
        if self.raiz == None:
            self.raiz = no
        else:
            no_pai = None
            no_atual = self.raiz
            while True:
                if no_atual != None:
                    no_pai = no_atual
                    if no.obtervalor() < no_atual.obtervalor():
                        no_atual = no_atual.obteresquerda()
                    else:
                        no_atual = no_atual.obterdireita()
                else:
                    if no.obtervalor() < no_pai.obtervalor():
                        no_pai.setesquerda(no)
                    else:
                        no_pai.setdireita(no)
                    break

    def mostraarvore(self, no_atual):
        if no_atual != None:
            self.mostraarvore(no_atual.obteresquerda())
            self.mostraarvore(no_atual.obterdireita())
            print(f'{no_atual.obtervalor()}', end=' ')



t = ArvoreBinariaBusca()

t.insere(7)
t.insere(2)
t.insere(5)
t.insere(9)
t.insere(13)
t.insere(0)
t.insere(6)
t.insere(12)
t.insere(3)

t.mostraarvore(t.obterraiz())


