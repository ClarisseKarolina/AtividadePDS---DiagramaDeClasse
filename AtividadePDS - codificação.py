#Classe Artigo (título, Autor)
class Artigo:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def getArtigo(self):
        return "Titulo:" + self.titulo + " | " + "Autor:" + self.autor



#Classe Edição (NúmeroDeEdição, VolumeDaEdição, DataDaEdição)
class Edicao:
    def __init__ (self, numeroDeEdicao, volumeDaEdicao, dataDaEdicao):
        self.numeroDeEdicao = nunumeroDeEdicaomero
        self.volumeDaEdicao = volumeDaEdicao
        self.dataDaEdicao = dataDaEdicao
        self.artigos = []

    def addNovoArtigo(self, artigo):
        self.artigos.append(artigo)

    def getEdicao(self):
        return "Edição número:" + str(self.numero) + " | " + "Volume:" + str(self.volume) + " | " + "Data:" + str(self.data)

    def showArtigos(self):
        for artigo in self.artigos:
            print(artigo.getArtigo())

    def getNumeroDeArtigo(self):
        return len(self.artigos)



#Classe Revista (Título, ISSN, Periodicidade)
class Revista:
    def __init__(self, titulo, issn, periodicidade):
        self.titulo = titulo
        self.issn = issn
        self.periodicidade = periodicidade
        self.edicoes = []

#Revista >> Adicionar Nova Edição (especificar quantidade de artigos necessários para uma edição )
    def addNovaEdicao(self, edicao):
        num_artigos = edicao.getNumeroDeArtigo()
           if(num_artigos >= 10 and num_artigos <= 15):
            self.edicoes.append(edicao)
            print("Edição Lançada com Sucesso!")

           else:
            print(" É necessário no mínimo 10 e no máximo 15 artigos para uma edição")

#Mostrar
    def showEdicoes(self):
        for edicao in self.edicoes:
        print(edicao.getEdicao())