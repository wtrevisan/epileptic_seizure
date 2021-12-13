# ************************************* Data Science Library *************************************
# Neste arquivo estão definidas algumas funções (uso geral) para serem utilizadas neste projeto.
#

# ************************************* Importando Pacotes ou Funções *************************************
#
# Importa o pacote "os" Operation System (Packages and Functions):
import os

# Importa o pacote  "numpy":
import numpy as np

# Importa o pacote  "pandas":
import pandas as pd

# Importa o pacote "pickle" para salvar/carregar objetos:
import pickle as pck

# Importa o pacote "time":
import time

# ************************************* Definindo Classes *************************************
#
#  ***** Classe para calcular o tempo decorrido de um processo/atividade qualquer:
#
class ElapsedTime():
    
    # Este método vai inicializar cada objeto criado a partir desta classe
    # O nome deste método é __init__, e ele é chamado de "Construtor", porque é ele que inicializa os objetos desta classe.
    # (self) é uma referência a cada atributo de um objeto criado a partir desta classe
    def __init__(self, builder_msg=True, display=True):
        
        # Atributos de cada objeto criado a partir desta classe. 
        # O self indica que estes são atributos dos objetos.
        self.display = display # Define se queremos mostrar a mensagem do tempo decorrido.
        self.start_time = 0 # Começa a contagem do tempo.
        self.end_time = 0 # Termina a contagem do tempo.
        self.elapsed_time = 0 # Calcula o tempo decorrido.
        if (builder_msg):
            print("Builder called to create an object of class ElapsedTime!")
        
    # Métodos são funções, que recebem como parâmetro atributos do objeto criado.
    # Método para iniciar a contagem do tempo:
    def start (self, msg=None):
        if (msg != None):
            print(msg) # Print message!
        
        self.start_time = time.perf_counter()

    # Método para terminar a contagem do tempo e imprimir o tempo decorrido se for desejado:
    def end (self, msg=None):
        # Calcula o tempo decorrido:
        self.end_time = time.perf_counter()
        self.elapsed_time = np.round((self.end_time - self.start_time), decimals=2)

        if (msg != None):
            msg_str = msg
        else:
            msg_str = "Elapsed time:"
                
        if (self.display == True):
            if (self.elapsed_time == 1):
                print("%s 1 second." % (msg_str))
            elif (self.elapsed_time == 60):
                print("%s 1 minute." % (msg_str))
            elif (self.elapsed_time == 60*60):
                print("%s 1 hour." % (msg_str))
            elif (self.elapsed_time == 60*60*24):
                print("%s 1 day." % (msg_str))
            elif (self.elapsed_time < 60):
                print("%s %.2f seconds." % (msg_str, self.elapsed_time))
            elif (self.elapsed_time < 60*60):
                print("%s %.2f minutes." % (msg_str, self.elapsed_time/60))
            elif (self.elapsed_time < 60*60*24):
                print("%s %.2f hours." % (msg_str, self.elapsed_time/(60*60)))
            else:
                print("%s %.2f days." % (msg_str, self.elapsed_time/(60*60*24)))

    # Método para obter a contagem do tempo:
    def get (self):
        return self.elapsed_time

# ************************************* Definindo Funções *************************************
#
# ***** Função para carregar (load) um objeto python qualquer, armazenado em um arquivo "pickle":
#
def pickle_object_load (path=".", file="None", msg=None):
    '''
    Input:
        "path": diretório (path) do arquivo que será carregado.
        "file": nome do arquivo que será carregado.
        "msg": mensagem que será impressa na tela (default é None, ou seja,
               não será impressa uma mensagem).

    Output:
        "obj": retorna os dados do "objeto" armazenado no arquivo.
    '''
    # Código da função:

    # Prepara o nome completo do arquivo piclke que será carregado (load):
    object_file = os.path.join(path, file)
    
    try:
        # Abre o arquivo para o modo leitura (read):
        pickle_in = open(object_file,"rb")
        
        # Faz a leitura do arquivo e carrega os dados no objeto ("obj"):
        obj = pck.load(pickle_in)

        # Fecha o arquivo "pickle":
        pickle_in.close()

        # Verifica se existe uma mensagem para ser impressa na tela:
        if (msg != None):
            # Imprime na tela a mensagem:
            print(msg)

        # Retorna os dados carregados:
        return obj
    
    except FileNotFoundError as error:
        # Erro encontrado na abertura do arquivo:
        print(error)
        # Retorna um valor nulo (None):
        return None

    except ValueError:
        # Erro encontrado na leitura do arquivo:
        print("I can not upload the '{}' file".format(file))
        
        # Fecha o arquivo "pickle":
        pickle_in.close()
        
        # Retorna um valor nulo (None):
        return None

# ***** Função para salvar (save) um objeto python qualquer em um arquivo "pickle":
#
def pickle_object_save (path=".", file="None", object_name=None, msg=None):
    '''
    Input:
        "path": diretório (path) onde o arquivo será criado.
        "file": nome do arquivo que será armazenado (salvo) o objeto python.
        "object_name": nome do objeto python que será armazenado (salvo) no arquivo.
        "msg": mensagem que será impressa na tela (default é None, ou seja,
               não será impressa uma mensagem).

    Output: None
    '''
    # Código da função:

    # Prepara o nome completo do arquivo piclke que será criado:
    object_file = os.path.join(path, file)
    
    try:
        # Abre o arquivo para o modo escrita (write):
        pickle_out = open(object_file,"wb")
        
        # Faz o 'dump' do objeto ("object_name") e salva os dados no arquivo ("file"):
        pck.dump(object_name, pickle_out)

        # Fecha o arquivo "pickle":
        pickle_out.close()

        # Verifica se existe uma mensagem para ser impressa na tela:
        if (msg != None):
            # Imprime na tela a mensagem:
            print(msg)

    except FileNotFoundError as error:
        # Erro encontrado na abertura do arquivo:
        print(error)

    except:
        # Erro encontrado ao fazer o "dump" do objeto:
        print("I can not save the '{}' object".format(object_name))
        
        # Fecha o arquivo "pickle":
        pickle_out.close()

# ***** Função para calcular os "missing values" em um DataFrame:
#
def missing_values(df):
    '''
    Input:
        "df": Data Frame.

    Output:
        Objeto do tipo "Dataframe" do Pandas.
    '''
    # Código da função:

    # Calcula o total de missing values para cada atributo (feature) do DataFrame "df":
    total = df.isnull().sum().sort_values(ascending=False)
    
    # Calcula a porcentagem de missing values para cada atributo (feature) do DataFrame "df":
    percent = (df.isnull().sum()/df.isnull().count()).sort_values(ascending=False)
    
    # Retorna um dataframe com os resultados:
    return (pd.concat([total, percent], axis=1, names='Attributes (Columns)', keys=['Total', 'Percent']))

# ***** Função para calcular a proporção dos valores atribuidos para uma variável qualquer em um DataFrame:
#
def percent_count_feature(df, feature, lines_drop=False):

    '''
    Entrada:
        "df": Data Frame;
        "feature": atributo (variável) do Dataframe.
        "lines_drop":
            "True": eliminar as linhas cujo "Total" seja igual a zero ("0").
            "False": não eliminar as linhas cujo "Total" seja igual a zero ("0"). Este é o valor default.

    Saída:
        temp_df: Objeto do tipo "Dataframe" do Pandas, com os resultados calculados.
    '''
    # Código da função:

    # Cria um DataFrame temporário calculando a contagem de cada valor atribuido a variável desejada ('feature'):
    temp_df = pd.DataFrame(df[feature].groupby(df[feature]).count())
    temp_df.rename(columns={feature:'Total'}, inplace=True)
    temp_df.sort_values(by='Total', ascending=False, inplace=True)

    # Verifica se devemos eliminar as linhas cujo "Total" seja igual a zero ("0"), ou seja, "lines_drop=True":
    if(lines_drop):
        # Eliminando as linhas:
        lines = list(temp_df[temp_df['Total'] == 0].index) # Retorna uma lista com os índices das linhas.
        temp_df.drop(list(lines), inplace=True) # Elimina do DataFrame as linhas selecionadas.
    
    # Calcula a soma total (geral) dos valore para o atributo (feature) do DataFrame "df":
    TotalGeral = temp_df.Total.sum()
    
    # Cria uma nova coluna ('Percent'), calculando a porcentagem de cada valor do atributo (feature) do DataFrame "df":
    temp_df['Percent'] = round(number=temp_df.Total / TotalGeral, ndigits=4)

    # Retorna um dataframe com os resultados:
    return (temp_df)

# ***** Função para obter os "percentis" das features de um dataset qualquer.
#

def get_features_percentiles(data, features, percent_range):
    '''
    Input:
        "data": Data Frame com os dados.
        "features": Features do Data Frame que desejamos calcular os "Percentis".
        "percet_range": Lista dos percentis que desejamos calcular, no formto de 0 a 100.
    
    Output:
        "df": Data Frame com os percentis calculados para cada variável.
    '''
    # Código da função:

    # Cria um array dos "percentis" desejados:
    percentiles = np.array(percent_range)
    
    # Cria um data frame onde serão armazenados os percentis de cada feature:
    percentiles_str = [str(v)+'%' for v in percentiles] # prepara os índices do data frame.
    
    # Cria o dataframe:
    df = pd.DataFrame(index=percentiles_str)
    df.index.name = 'Percentile' # nomeia o índice do data frame.
    
    # Verifica se temos apenas "1" variável em "features":
    if (type(features) == str):
        # Calcula os percentis:
        result = np.percentile(a=data[features], q=percentiles)
        # Armazena os resultados no data frame:
        df[features] = result
    else:
        # Neste caso, "features" representa uma lista de variáveis.
        # Loop para calcular os percentis de cada variável em 'features':
        for feat in features:
            # Calcula os percentis:
            result = np.percentile(a=data[feat], q=percentiles)
            # Armazena os resultados no data frame:
            df[feat] = result
    
    # Retorna o resultado:
    return df

# ***** Função para calcular algumas medidas estatísticas de tendência central (moda, média e mediana),
# de dispersão (desvio padrão), de forma (assimetria e curtose), e também o coeficiente de variação (CV).
#
def statistical_measures(df, feature, decimals=3):

    '''
    Entrada:
        "df": Data Frame que contém os atributos (features);
        "feature": atributos (variáveis) do Dataframe.

    Saída:
        results_df: Objeto do tipo "Dataframe" do Pandas, com os resultados calculados.
    '''
    # Código da função:

    # Cria um dicionário, calculando as medidas estatísticas para cada atributo (feature) do DataFrame (df):
    measures = {'mean': df[feature].mean(), # média
                'median': df[feature].median(), # mediana
                'mode': df[feature].mode(axis=0).iloc[0], # moda
                'var': df[feature].var(), # variância.
                'std': df[feature].std(), # desvio padrão.
                'var_coff': (df[feature].std()/df[feature].mean())*100, # CV = (std/mean)*100
                'skewness': df[feature].skew(axis=0), # Assimetria
                'kurtosis': df[feature].kurtosis(axis=0) # Curtose
               }
    
    # Criando um DataFrame para armazenar os resultados:
    results_df = pd.DataFrame(data=measures).T

    # Verifica se os resultados serão arredondados:
    if (decimals != None):
        # Retorna o resultado com arredondamento dos resultados:
        return results_df.round(decimals=decimals)
    else:
        # Retorna os resultados sem arredondamento:
        return (results_df)

# ***** Função para realizar algumas transformações (feature engineering) nos dados.
#
def feature_engineering(df):
    '''
    Entrada:
        "df": Data Frame que contém os atributos (features);

    Saída:
        df_new: "novo" Data Frame do Pandas, com as features transformadas.
    '''

    # Código da função:
    
    # Removendo a variável "Unnamed: 0":
    df_new = df.drop(columns=['Unnamed: 0'], axis=1, inplace=False)
    
    # Criando a variável "target" com 2 categorias:
    # Colocando "True" onde o valor de "y" for igual a "1" e "False" onde o valor for diferente:
    df_new["target"] = (df_new.y == 1)
    # Convertendo os valores booleanos "True" e "False" para números inteiros "1" e "0" respectivamente:
    df_new["target"] = df_new["target"].astype(int)
    
    # Retorna o data frame transformado:
    return df_new
