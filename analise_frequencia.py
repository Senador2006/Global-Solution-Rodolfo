# analise_frequencia.py
import pandas as pd


def carregar_dados():
    try:
        # Configurações para arquivos do INMET
        dados = pd.read_csv(
            r'C:\Users\thisa\Downloads\INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2024_A_31-12-2024.CSV',
            delimiter=';',
            decimal=',',
            encoding='ISO-8859-1',
            skiprows=8,  # Pula metadados iniciais
            on_bad_lines='warn'  # Ignora linhas com formato irregular
        )

        # Renomeia colunas para facilitar manipulação
        dados.columns = dados.columns.str.strip().str.upper()
        return dados

    except Exception as e:
        print(f"Erro ao carregar dados: {str(e)}")
        return None


def analise_discreta(df):
    try:
        # Variável discreta: Dias com chuva (0 ou 1)
        df['CHUVA'] = df['PRECIPITAÇÃO TOTAL, HORÁRIO (mm)'].apply(
            lambda x: 1 if float(x) >= 1 else 0
        )

        freq_discreta = df['CHUVA'].value_counts().reset_index()
        freq_discreta.columns = ['CHUVA', 'FREQUÊNCIA']
        return freq_discreta

    except KeyError:
        print("Erro: Coluna de precipitação não encontrada. Verifique os nomes das colunas:")
        print(df.columns.tolist())
        return None


def analise_continua(df):
    try:
        # Variável contínua: Temperatura em intervalos de 5°C
        temp_col = 'TEMPERATURA MÁXIMA NA HORA ANT. (AUT) (°C)'
        intervalos = range(10, 45, 5)

        df['FAIXA_TÉRMICA'] = pd.cut(
            df[temp_col].astype(float),
            bins=intervalos,
            labels=[f"{i}-{i + 5}°C" for i in intervalos[:-1]],
            include_lowest=True
        )

        freq_continua = df['FAIXA_TÉRMICA'].value_counts().sort_index().reset_index()
        freq_continua.columns = ['FAIXA TÉRMICA', 'FREQUÊNCIA']
        return freq_continua

    except KeyError:
        print("Erro: Coluna de temperatura não encontrada. Colunas disponíveis:")
        print(df.columns.tolist())
        return None


# Execução principal
if __name__ == "__main__":
    dados = carregar_dados()

    if dados is not None:
        print("\nPrimeiras linhas dos dados:")
        print(dados.head())

        print("\nAnálise Discreta:")
        print(analise_discreta(dados))

        print("\nAnálise Contínua:")
        print(analise_continua(dados))
