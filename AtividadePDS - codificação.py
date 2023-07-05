#Classe Artigo (título, Autor)
class Artigo:
    def __init__ (self,titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def GetArtigo(self):
        return "Título: " + str(self.titulo) + " ; " + "Autor: " + str(self.autor)



#Classe Edição (NúmeroDeEdição, VolumeDaEdição, DataDaEdição)
class Edicao:
    def __init__ (self, numeroDeEdicao, volumeDaEdicao, dataDaEdicao):
        self.numeroDeEdicao = nunumeroDeEdicaomero
        self.volumeDaEdicao = volumeDaEdicao
        self.dataDaEdicao = dataDaEdicao
        self.artigos = [] #ligação entre Edicao e Artigo

    def addNovoArtigo (self,artigo):
        self.artigos.append(artigo)

    def GetEdicao(self):
        return "Edição: " + str(self.numero) + " ; " + "Volume: " + str(self.volume) + " ; " + "Data: " + str(self.data)

    def showArtigos(self):
        for artigo in self.artigos:
            print(artigo.exibirArtigo()) 

    def exibirNumeroDeArtigo(self):
        return len(self.artigos)
    
    def excluirArtigo(self,titulo):
        for artigo in self.artigos:
            if artigo.titulo == titulo:
                self.artigos.remove(artigo) #função adicional



#Classe Revista (Título, ISSN, Periodicidade)
class Revista:
    def __init__ (self, titulo, issn, periodicidade):
        self.titulo =  titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = [ ] #Ligação entre revista e edição
        
    def addNovaEdicao(self, edicao):
        num_artigos = edicao.contarNumeroDeArtigo()
        if (num_artigos>=10 and num_artigos <=15):
            self.edicoes.append(edicao)
            return f"Edição lançada com sucesso!!!"
        else:
            return f"Necessita de no mínimo 10, e no máximo 15 artigos, para lançar uma nova edição!"

    def ShowEdicoes(self): #exibir
        for edicao in self.edicoes:
            print(edicao.exibirEdicao())
