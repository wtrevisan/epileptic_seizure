# ************************************* Machine Learning Library For Data Science (Versão 01) *************************************
# Neste arquivo estão definidas algumas funções de "Machine Learning" para serem utilizadas em Data Science.
#

# ************************************* Importando Pacotes e/ou Funções *************************************
#
# Importa o pacote "NumPy":
import numpy as np
# Importa o pacote "Pandas":
import pandas as pd

# Importa o pacote "os" (Operation System with its Packages and Functions)
import os

# O pacote "sys" permite manipulações com o sistema operacional:
import sys

# Imports para "Avaliação do Modelo":
from sklearn.metrics import roc_auc_score, precision_score, recall_score, accuracy_score, f1_score

# Path: onde estão armazenadas as classes e funções que serão utilizadas neste módulo:
LIB_PATH = os.path.join(".")

# Adicionando o diretório ao 'path' do Sistema, para podermos importar classes e funções que serão
# utilizadas neste módulo:
sys.path.append(LIB_PATH)

# ************************************* Definindo Funções *************************************
#
# ***** Função para mostrar os resultados das pontuações (Scores) da validação cruzada (Cross Validation).
#
def display_scores(scores, decimals=4):
    '''
    Input:
        "scores": pontuações (scores) calculados de um processo de validação cruzada.
        "decimals": número de dígitos decimais para apresentação dos resultados.

    Output: None
    '''
    # Código da função:

    print("Scores:", len(scores))
    print(np.round(scores, decimals=decimals))
    print("Mean:", np.round(scores.mean(), decimals=decimals)) 
    print("Standard deviation:", np.round(scores.std(), decimals=decimals))

# ***** Fução para mostrar os melhores resultados encontrados para os hiperparâmetros do modelo:
#
def best_results_report (estimator, title):
    '''
    Input:
        "estimator": modelo de machine learning que já foi treinado (fit).
        "title": título do relatório.

    Output: None
    '''
    # Código da função:

    # Mostra o título do relatório:
    print(title)
    
    # Mostra a melhor seleção de hiperparâmetros:
    print('Best params:', estimator.best_params_)

    # Mostra o melhor estimador:
    print('Best estimator:', estimator.best_estimator_)

    # Mostra o melhor score:
    print('Best score:', np.round(estimator.best_score_, decimals=4))

# ***** Função para calcularmos as métricas de classificação de um modelo de "Machine Learning":
#
def binary_classif_metrics (y_actual, y_pred, threshold=0.5):
    '''
    Input:
        "y_actual": dados "reais" da nossa variável target.
        "y_pred": dados "previstos" da nossa variável target.
        "threshold": valor limite (default = 0.5) para rotular uma amostra prevista como positiva.

    Output: retorna um objeto (dict) com os valores calculados de cada métrica.
    '''
    # Código da função:

    # Criando um objeto (dicionário) vazio para armazenar as métricas:
    metrics = dict()

    # Calculando o AUC (Area Under Curve):
    metrics['auc'] = np.round(roc_auc_score(y_actual, y_pred), decimals=4)

    # Calculando a acurácia:
    metrics['accuracy'] = np.round(accuracy_score(y_actual, (y_pred > threshold)), decimals=4)
    
    # Calculando a precisão:
    metrics['precision'] = np.round(precision_score(y_actual, (y_pred > threshold)), decimals=4)
    
    # Calculando a revocação:
    metrics['recall'] = np.round(recall_score(y_actual, (y_pred > threshold)), decimals=4)

    # Calculando a pontuação F1:
    metrics['f1_score'] = np.round(f1_score(y_actual, (y_pred > threshold)), decimals=4)
    
    # Print dos resultados:
    print ("AUC      : {}".format(metrics['auc']))
    print ("Accuracy : {}".format(metrics['accuracy']))
    print ("Precision: {}".format(metrics['precision']))
    print ("Recall   : {}".format(metrics['recall']))
    print ("f1-score : {}".format(metrics['f1_score']))
    
    # Retorna as métricas calculadas:
    return metrics

# Função para treinar e avalidar um modelo preditivo de classificação binária:
#
def train_validate_binary_clf_model(classifier, X_train, y_train, X_valid, y_valid, threshold=0.5):
    '''
    Input:
        "classifier": algoritmo de machine learning (classificação binária) que será treinado;
        "X_train": variáveis preditoras para treinamento do modelo de classificação binária;
        "y_train": variável target para treinamento do modelo de classificação binária;
        "X_valid": variáveis preditoras para avaliação do modelo de classificação binária;
        "y_valid": variável target para avaliação do modelo de classificação binária;
        "threshold": valor limite (default = 0.5) para rotular uma amostra prevista como positiva.

    Output:
        "model": retorna o modelo de classificação binária treinado;
        "train_metrics": retorna um objeto (dict) com os valores calculados de cada métrica nos dados de treino;
        "valid_metrics": retorna um objeto (dict) com os valores calculados de cada métrica nos dados de avaliação.
    '''
    # Código da função:
    
    # Criando uma instância do classificador:
    model = classifier

    # Treina (Fit) o modelo com os dados de treino:
    model.fit(X_train, y_train)

    # Utilizando o modelo treinado para fazer as previsões:
    # Dados de treino: obtendo as probabilidades da classe positiva (1):
    y_train_preds = model.predict_proba(X_train)[:,1]

    # Dados de avaliação: obtendo as probabilidades da classe positiva (1):
    y_valid_preds = model.predict_proba(X_valid)[:,1]
    
    # Calculando as métricas nos dados de treino:
    print("\nTraining Metrics:")
    train_metrics = binary_classif_metrics(y_actual=y_train, y_pred=y_train_preds, threshold=threshold)
    
    # Calculando as métricas nos dados de avaliação:
    print("\nValidation Metrics:")
    valid_metrics = binary_classif_metrics(y_actual=y_valid, y_pred=y_valid_preds, threshold=threshold)
    
    # Retorna o modelo treinado (fit) e as métricas de treino e avaliação:
    return (model, train_metrics, valid_metrics)
