class No():

    def __init__(self,elemento):
        self.elemento = elemento
        self.direita = None
        self.esquerda = None
        self.pai = None

    def __str__(self):
        return str(self.elemento)

    def get_elemento(self):
        return self.elemento

    def get_direita(self):
        return self.direita

    def get_esquerda(self):
        return self.esquerda

    def get_pai(self):
        return self.pai

class ervore():

    def __init__(self):
        self.raiz = None
    def menu(self):
        while True:
            print('1 - Adicionar')
            print('2 - Buscar')
            print('3 - Maximo')
            print('4 - Minino')
            print('5 - Mostra Arvore')
            print('6 - Niveis')
            print('7 - Remover')
            print('8 - Sucessor')
            print('9 - Altura ')
            print('10 - Retornar elemento do nivel')
            print('11 - Soma')
            print('12 - Quantidade de nós da arvore')
            print('13 - Quantidade de folhas da arvore')
            print('14 - Retornar nivel de elemento')
            print('15 - Antecessor')
            op = input('Digite uma opção: ')

            if op == '0':
                return

            elif op == '1':
                x = int(input('Digite o valor que deseja adicionar: '))
                self.add(x)

            elif op =='2':
                x = int(input('Digite o valor que deseja buscar: '))
                a = self.buscar(x)
                print(a)
            elif op =='3':
                a = self.maximo()
                print(a)

            elif op =='4':
                a = self.minimo()
                print(a)

            elif op =='5':
                a = self.imprimir(self.raiz)
                print(a)
            elif op =='6':
                a = self.niveis(self.raiz)
                print(a)

            elif op =='7':
                x = input('Digite o elemento que deseja excluir: ')
                a = self.remover(x)
                print(a)

            elif op =='8':
                x = int(input('Digite: '))
                a = self.buscar(x)
                b = self.nosucessor(a)
                print(b)

            elif op=='9':
                print(self.altura(self.raiz))


            elif op =='10':
                self.retornar_elemento()

            elif op =='11':
                self.soma_completa()

            elif op =='12':
                print(self.quantidade_de_nos(self.raiz))

            elif op =='13':
                print(self.quantidade_folhas(self.raiz))

            elif op == '14':
                elemento = int(input('Digite o elemento que deseja buscar o nivel: '))

                print(self.retornar_nivel_elemento(elemento))


            elif op =='15':
                elemento = int(input('Digite o elemento que deseja buscar o antecessor: '))
                print(self.antecessor(elemento))


    def quantidade_de_nos(self, atual):
        if atual == None:
            return 0
        else:
            return 1 + self.quantidade_de_nos(atual.esquerda) + self.quantidade_de_nos(atual.direita)

    def add(self,elemento):
        no = No(elemento)
        atual = self.raiz

        if self.raiz == None:
            self.raiz = no
        else:
            while True:
                if int(no.elemento)  > int(atual.elemento):
                    if atual.direita!=None:
                        atual = atual.direita

                    else:
                        atual.direita = no
                        break

                elif int(no.elemento) < int(atual.elemento):
                    if atual.esquerda !=None:
                        atual = atual.esquerda

                    else:
                        atual.esquerda = no
                        break

                else:
                    raise Exception('Elemento já adicionado')
        print('Adicionado com sucesso!!!')


    def buscar(self,elemento):

        atual = self.raiz
        pai = self.raiz

        if self.raiz == None:
            return "Arvore vazia primo"

        while elemento != atual.elemento:
            if elemento  > atual.elemento:
                anterior = atual
                atual = atual.direita


            else:
                atual = atual.esquerda

        print('Encontrado')
        return atual

    def minimo(self):
        x = self.raiz

        if x == None:
            return "A arvore está vazia"

        while x.esquerda is not None:
            x = x.esquerda

        return x

    def quantidade_folhas(self, atual):
        if atual == None:
            return 0
        if atual.esquerda == None and atual.direita == None:
            return 1
        return self.quantidade_de_nos(atual.esquerda) + self.quantidade_de_nos(atual.direita)

    def maximo(self):
        x = self.raiz

        if x == None:
            return "Arvore vazia"

        while x.direita is not None:
            x = x.direita

        return x

    def imprimir(self, atual):
        if atual != None:
            self.imprimir(atual.esquerda)
            print(atual.elemento)
            self.imprimir(atual.direita)

        else:
            return "Arvore vazia "
    def altura(self,atual):
        if atual == None or atual.esquerda == None and atual.direita == None:
            return  1

        else:

            if self.altura(atual.esquerda) > self.altura(atual.direita):
                return 1 + self.altura(atual.esquerda)
            else:
                return 1 + self.altura(atual.direita)


    def niveis(self, atual):

        if atual == None or atual.esquerda == None and atual.direita == None:
            return 0
        else:
            if self.niveis(atual.esquerda) > self.niveis(atual.direita):
                return 1 + self.niveis(atual.esquerda)
            else:
                return 1 + self.niveis(atual.direita)

    def retornar_nivel_elemento(self,elemento):

        nivel = 0
        atual = self.raiz

        while atual is not None and elemento!= atual.elemento:
            if elemento < atual.elemento:
                atual = atual.esquerda
                nivel += 1

            else:
                atual = atual.direita
                nivel +=1

        return print("Elemento = {} - Nivel = {} ".format(atual.elemento,nivel))



    def retornar_elemento(self):

            atual = self.raiz

            if atual is not  None and  atual.esquerda == None and atual.direita == None:
                    print(" Nivel {} Elemento  = {} ".format(self.niveis(atual), atual))

            else:
                while atual !=None or atual.esquerda!=None and atual.direita!=None:
                    if  self.niveis(atual.esquerda) == self.niveis(atual.direita):
                               return print( "Nivel {}  Elemento = {} Elemento {}".format(self.niveis(atual),(atual.esquerda),(atual.direita)))



    def soma_esquerda(self):

        atual = self.raiz
        soma = 0

        while True:
            if atual.esquerda !=None:
                atual = atual.esquerda
                soma = soma + atual.elemento

            else:
                return soma + self.raiz.elemento

    def soma_direita(self):
        soma1 = 0
        atual = self.raiz
        while True:
            if atual.direita !=None:
                atual = atual.direita
                soma1 = soma1 + atual.elemento


            else:
                return soma1

    def soma_completa(self):
        a = self.soma_direita()
        b = self.soma_esquerda()
        return print(a+b)

    def folhas(self, atual):
        if atual == None:
            return 0
        if atual.esquerda == None and atual.direita == None:
            return 1
        return self.folhas(atual.esquerda) + self.folhas(atual.direita)

    def remover(self, elemento):
        if self.raiz == None:
            return "Arvore está vazia meu querido"
        perc = self.raiz
        pai = self.raiz
        filho_esq = True

        while perc.elemento != elemento:
            pai = perc
            if elemento< perc.elemento:
                perc = perc.esquerda
                filho_esq = True
            else:
                perc = perc.direita
                filho_esq = False
            if perc == None:
                return "Arvore vazia "
        if perc.esquerda == None and perc.direita == None:
            if perc == self.raiz:
                self.raiz = None
            else:
                if filho_esq:
                    pai.esquerda = None
                else:
                    pai.direita = None
        elif perc.direita == None:
            if perc == self.raiz:
                self.raiz = perc.esquerda
            else:
                if filho_esq:
                    pai.esquerda = perc.esquerda
                else:
                    pai.direita = perc.esquerda


        elif perc.esquerda == None:
            if perc == self.raiz:
                self.raiz = perc.direita
            else:
                if filho_esq:
                    pai.esquerda = perc.direita
                else:
                    pai.direita = perc.direita
        else:
            sucessor = self.nosucessor(perc)

            if perc == self.raiz:
                self.razi = sucessor
            else:
                if filho_esq:
                    pai.esquerda = sucessor
                else:
                    pai.direita = sucessor
            sucessor.esquerda = perc.esquerda


        print('Removido com sucesso!!!')

        return True

    def nosucessor(self, remover):
        paidosucessor = remover
        sucessor = remover
        perc = remover.direita

        while perc != None:
            paidosucessor = sucessor
            sucessor = perc
            perc = perc.esquerda

        if sucessor != remover.direita:
            paidosucessor.esquerda = sucessor.direita


        return sucessor


    def antecessor(self,elemento):
        no = No(elemento)
        atual = self.raiz
        if atual ==None:
            return 'vazia'

        else:
            while no.elemento != atual.elemento :
                    #atual = atual.direita
                    #return type(atual.elemento),type(no.elemento),atual.elemento,no.elemento

                    while True:
                        if (atual.elemento) < (no.elemento):
                            atual = atual.direita
                            print(atual)
                            break

                        elif atual.elemento > no.elemento:
                            atual = atual.esquerda
                            print( atual)
                            break


                        #elif atual.elemento == no.elemento:
                            #return atual














