import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Gerando dados fictícios
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# 2. Dividindo em treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# 3. Criando e treinando o modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 4. Fazendo previsões
y_pred = modelo.predict(X_test)

# 5. Avaliação do modelo
print("\nResultados da Regressão Linear:")
print(f"Coeficiente angular (β1): {modelo.coef_[0][0]:.2f}")
print(f"Intercepto (β0): {modelo.intercept_[0]:.2f}")
print(f"R²: {r2_score(y_test, y_pred):.2f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.2f}")

# 6. Visualização (opcional)
plt.figure(figsize=(10,6))
plt.scatter(X_test, y_test, color='blue', alpha=0.7, label='Dados reais')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regressão Linear')
plt.xlabel('Variável Independente (X)', fontsize=12)
plt.ylabel('Variável Dependente (y)', fontsize=12)
plt.title('Modelo de Regressão Linear Simples', fontsize=14)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
