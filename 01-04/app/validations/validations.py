'''Funções para validações de dados'''

from app.exceptions.exceptions import *

def valid_isbn(isbn: str):
    '''
    Retorna uma exec. `ValueErrorISBN` caso o isbn não corresponder a 13 caracteres.

    Args:
        isbn (str): ISBN do livro
    '''
    if not len(isbn) == 13:
        raise ValueErrorISBN(isbn)

def valid_password(password: str):
    '''
    Retorna uma exec. `PasswordLengthError` caso a senha não contenha no mínimo 8 caracteres.

    Args:
        password (str): senha do usuário
    
    '''
    if len(password) < 8:
        raise PasswordLengthError(password)