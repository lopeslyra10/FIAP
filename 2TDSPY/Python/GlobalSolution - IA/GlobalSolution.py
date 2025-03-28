

# Nome: Augusto Lopes Lyra - RM: 558209
# Nome: Lucas Barreto Consentino - RM: 557107
#----------------------------------------------------------------
# Análise Exploratória sobre a Transição Energética
# Neste notebook, vamos realizar uma análise exploratória de dados para entender os principais fatores relacionados à transição energética. A análise incluirá:

# Coleta de dados sobre eficiência energética, uso de fontes renováveis de energia e seu impacto econômico e ambiental.
# Verificação da distribuição e correlação entre as variáveis.

# Importando as bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar a base de dados
# Assumindo que o arquivo CSV já está no mesmo diretório que o Jupyter Notebook.
df = pd.read_csv('Carbon_(CO2)_Emissions_by_Country.csv')

# Exibindo as primeiras linhas dos dados
df.head()

# Resumo estatístico dos dados
df.describe()

# Verificando os tipos de dados
df.info()

# Identificando valores ausentes
df.isnull().sum()

# Selecting only numeric columns for correlation analysis
numeric_df = df.select_dtypes(include=np.number)

# Visualizando a correlação entre as variáveis
plt.figure(figsize=(10, 6))
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlação entre as variáveis')
plt.show()

# Gráfico 1: Emissões de CO2 por Região
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Kilotons of Co2', data=df, estimator=sum, ci=None)
plt.title('Emissões de CO2 por Região')
plt.xlabel('Região')
plt.ylabel('Emissões de CO2 (Kilotons)')
plt.xticks(rotation=45)
plt.show()

# Gráfico 2: Emissões de CO2 ao longo do tempo
df['Year'] = pd.to_datetime(df['Date']).dt.year
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Kilotons of Co2', data=df, estimator='mean', ci=None)
plt.title('Emissões de CO2 ao Longo do Tempo')
plt.xlabel('Ano')
plt.ylabel('Emissões de CO2 (Kilotons)')
plt.xticks(rotation=45)
plt.show()

# Gráfico 3: Top 10 países em emissões per capita
top_countries = df.groupby('Country')['Metric Tons Per Capita'].mean().nlargest(10).reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Country', y='Metric Tons Per Capita', data=top_countries)
plt.title('Top 10 Países em Emissões Per Capita')
plt.xlabel('País')
plt.ylabel('Emissões Per Capita (Metric Tons)')
plt.xticks(rotation=45)
plt.show()

# Gráfico 4: Distribuição de emissões per capita por região
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='Metric Tons Per Capita', data=df)
plt.title('Distribuição de Emissões Per Capita por Região')
plt.xlabel('Região')
plt.ylabel('Emissões Per Capita (Metric Tons)')
plt.xticks(rotation=45)
plt.show()

# Gráfico 5: Relação entre emissões totais e per capita por região
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Kilotons of Co2', y='Metric Tons Per Capita', hue='Region', data=df)
plt.title('Relação entre Emissões Totais e Per Capita por Região')
plt.xlabel('Emissões Totais (Kilotons)')
plt.ylabel('Emissões Per Capita (Metric Tons)')
plt.legend(title='Região')
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Criar variável de classificação
df['Progresso'] = ['Alto' if x > 5 else 'Baixo' for x in df['Metric Tons Per Capita']]

# Seleção de variáveis
X = df[['Kilotons of Co2']]
y = df['Progresso']

# Dividir em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Treinar o modelo de classificação
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predição
y_pred = model.predict(X_test)

# Avaliação
print(classification_report(y_test, y_pred))

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Selecionar variáveis para clusterização
features = df[['Kilotons of Co2', 'Metric Tons Per Capita']]

# Escalar os dados
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Clusterização com KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(scaled_features)

# Visualizar os clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Kilotons of Co2',
    y='Metric Tons Per Capita',
    hue='Cluster',
    palette='viridis',
    data=df
)
plt.title('Clusters de Padrões de Emissões')
plt.xlabel('Emissões Totais (Kilotons)')
plt.ylabel('Emissões Per Capita (Metric Tons)')
plt.legend(title='Cluster')
plt.show()

import joblib

# Salvar modelos
joblib.dump(model, 'class_model.pkl')
joblib.dump(kmeans, 'cluster_model.pkl')
joblib.dump(scaler, 'scaler.pkl')

from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Carregar os modelos treinados
class_model = joblib.load('class_model.pkl')  # Salve o modelo de classificação
cluster_model = joblib.load('cluster_model.pkl')  # Salve o modelo de clusterização
scaler = joblib.load('scaler.pkl')  # Salve o scaler

@app.route('/classificar', methods=['POST'])
def classificar():
    data = request.json
    if 'Kilotons of Co2' not in data:
        return jsonify({'error': 'Kilotons of Co2 é necessário'}), 400

    kilotons = [[data['Kilotons of Co2']]]
    prediction = class_model.predict(kilotons)
    return jsonify({'Progresso': prediction[0]})

@app.route('/clusterizar', methods=['POST'])
def clusterizar():
    data = request.json
    if 'Kilotons of Co2' not in data or 'Metric Tons Per Capita' not in data:
        return jsonify({'error': 'Kilotons of Co2 e Metric Tons Per Capita são necessários'}), 400

    features = [[data['Kilotons of Co2'], data['Metric Tons Per Capita']]]
    scaled_features = scaler.transform(features)
    cluster = cluster_model.predict(scaled_features)
    return jsonify({'Cluster': int(cluster[0])})

if __name__ == '__main__':
    app.run(debug=True)
