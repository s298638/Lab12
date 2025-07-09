from dataclasses import dataclass
from datetime import datetime


@dataclass
class Retailer:
    cod_retailer:int
    nazione:str
    nome_retailer:str
    def __eq__(self, other):
        return self.cod_retailer == other.cod_retailer

    def __hash__(self):
        return hash(self.cod_retailer)