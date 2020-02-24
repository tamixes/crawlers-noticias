
from datetime import datetime
import re


def string_to_date_processor(string):
    """Converte uma string no formato Y-M-DTH:M:S para um datetime"""

    if type(string) == list:
        string = string[0]
    string = string.replace('T', ' ')
    string = string.replace('+00:00', '')
    date = datetime.strptime(string, '%Y-%m-%d %H:%M:%S')

    return date


def clean_termos(termos):
    """Limpa termos que começam e/ou terminam com espaço"""

    if type(termos) == list:
        clean_termos = []
        for termo in termos:
            termo = find_termo(r'\w+', termo)
            clean_termos.append(termo)
        return clean_termos
    else:
        return find_termo(r'\w+', termos)


def find_termo(pattern, string, flags=0):
    """Retorna o termo limpo de acordo com o regex passado"""

    termo = re.findall(pattern, string, flags=flags)

    return ' '.join(termo)
