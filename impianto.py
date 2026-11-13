from pannello import PannelloFotovoltaico
class ImpiantoSolare:
    __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None
        self.codice = codice
        self.modello = modello
        self.localita = localita
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        if potenza_massima_kw <= 0
            raise ValueError
    list[PannelloFotovoltaico] pannelli = []
    def aggiungi_pannello(self, PannelloFotovoltaico):
        self.pannelli.Append(PannelloFotovoltaico)
    def potenza_pannelli(self)
        self.somma = 0
        for pannello in pannelli
            somma = somma + pannello
   def rimuovi_pannello(self, codice:str)
       pannelli.remove(codice)
       

    