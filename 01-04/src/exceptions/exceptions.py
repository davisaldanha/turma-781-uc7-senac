'''Exceções Customizadas utilizadas na API'''

class ValueErrorISBN(Exception):
    '''Exceção representativa para atributo ISBN'''
    def __init__(self, isbn):
        super().__init__(f'O isbn {isbn} não possui um tamanho válido para 13 caracteres.')