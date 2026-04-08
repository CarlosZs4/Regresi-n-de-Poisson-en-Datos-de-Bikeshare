import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

# 1. Carga de datos y preparación
df = pd.read_csv('Bikeshare.csv')
df['datetime'] = pd.to_datetime(df['datetime'])
df['hr'] = df['datetime'].dt.hour

# 2. Ajuste del Modelo de Poisson (GLM)
# Definimos la fórmula según los requerimientos del proyecto
formula = "bikers ~ hr + temp + workingday + weathersit"
modelo_poisson = smf.glm(formula, data=df, family=sm.families.Poisson()).fit()

# Generamos la tasa esperada (lambda) predicha por el modelo
df['lambda_pred'] = modelo_poisson.predict(df)

# 3. Generación de la Gráfica de Poisson
plt.figure(figsize=(10, 6))

# Dibujamos la dispersión de los datos
# Eje X: Valores Reales del CSV
# Eje Y: Valores que el modelo predijo (siempre positivos)
plt.scatter(df['bikers'], df['lambda_pred'], alpha=0.3, color='#2a9d8f', label='Predicciones Poisson ($\hat{\lambda}$)')

# Línea de identidad (Referencia de "Modelo Perfecto")
# Si el modelo fuera 100% exacto, todos los puntos estarían sobre esta línea
max_val = max(df['bikers'].max(), df['lambda_pred'].max())
plt.plot([0, max_val], [0, max_val], color='#e76f51', linestyle='--', linewidth=2, label='Ajuste Ideal')

# Estética y etiquetas técnicas
plt.xlabel('Alquileres Reales (Bikers)', fontsize=12)
plt.ylabel('Tasa Esperada Predicha ($\lambda$)', fontsize=12)
plt.title('Regresión de Poisson: Validación de Predicciones vs Realidad', fontsize=14)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)


plt.show()
