'''Funções para validações de dados'''

from exceptions.exceptions import *

def valid_isbn(isbn: str):
    '''
    Retorna uma exec. `ValueErrorISBN` caso o isbn não corresponder a 13 caracteres.

    Args:
        isbn (str): ISBN do livro
    '''
    if not len(isbn) == 13:
        raise ValueErrorISBN(isbn)