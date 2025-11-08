import datetime
import pandas as pd

def coletar_dados():
    return [
        {'data': datetime.date.today(), 'evento': 'processamento finalizado', 'status': 'ok'},
    ]

def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv('dados/relatorio.csv', index = False)
    print('Relatório salvo com sucesso')

if __name__ == '__main__':
    print('Iniciando robo...')
    dados = coletar_dados()
    salvar_relatorio(dados)
    