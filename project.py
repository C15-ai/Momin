from abc import ABC,abstractmethod
class Teatr(ABC):
    def __init__(self,nomi,kod,janr):
        self.nomi = nomi
        self.kod = kod
        self.janr = janr
    @abstractmethod
    def locate(self):
        pass
    def __str__(self):
        return f"Teatr nomi {self.nomi} Kodi {self.kod} Janri {self.janr}"
class Movie(Teatr):
    def __init__(self,nomi,kod,janr,direktor,davomiylik):
        super().__init__(nomi,kod,janr)
        self.direktor = direktor
        self.davomiylik = davomiylik
    def locate(self):
        return f"Filmlar bolimi {self.kod}"
    def __str__(self):
        return f"Film nomi {self.nomi} - Rejisyor {self.direktor} - Davomiylik {self.davomiylik} minut"
class Series(Teatr):
    def __init__(self,nomi,kod,janr,season,epizode):
        super().__init__(nomi,kod,janr)
        self.season = season
        self.epizode = epizode
    def locate(self):
        return f"Seriallar bolimi {self.kod}"
    def __str__(self):
        return f"Serial nomi {self.nomi} - Epizod qismlari {self.epizode} - Mavsumlari {self.season}"
class Spektakl(Teatr):
    def __init__(self,nomi,kod,janr,actors):
        super().__init__(nomi,kod,janr)
        self.actors = actors
    def locate(self):
        return f"Spektakl bolimi {self.kod}"
    def __str__(self):
        return f"Nomi {self.nomi} - Aktyorlari {self.actors}"
class Consert(Teatr):
    def __init__(self,nomi,kod,janr,artist):
        super().__init__(nomi,kod,janr)
        self.artist = artist
    def locate(self):
        return f"Konsertlar {self.kod}"
    def __str__(self):
        return f"Konsert Nomi {self.nomi} - Artist {self.artist}"
class Catalog:
      pass



