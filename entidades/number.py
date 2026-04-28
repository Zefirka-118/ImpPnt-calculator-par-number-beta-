"""Definiremos un comparador TRUE/FALSE"""

class Number:
    
    def __init__(self, valor):
        self.valor = valor

    def es_par(self) -> bool:
        return self.valor % 2 == 0