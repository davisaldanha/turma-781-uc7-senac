'''Exceções Customizadas utilizadas na API'''

class ValueErrorISBN(Exception):
    '''Exceção representativa para atributo ISBN'''
    def __init__(self, isbn):
        super().__init__(f'O isbn {isbn} não possui um tamanho válido para 13 caracteres.')

class UserNotFoundError(Exception):
    ''''Exceção representativa para usuário não encontrado'''
    def __init__(self, username):
        super().__init__(f'O usuário {username} não foi encontrado.')

class PasswordLengthError(Exception):
    '''Exceção representativa para senha com comprimento inválido'''
    def __init__(self, password):
        super().__init__(f'A senha {password} deve conter no mínimo 8 caracteres.')