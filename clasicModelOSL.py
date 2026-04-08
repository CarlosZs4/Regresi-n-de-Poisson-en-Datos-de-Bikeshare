import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt


df = pd.read_csv('Bikeshare.csv')

# Extraer hora de la columna datetime
df['datetime'] = pd.to_datetime(df['datetime'])
df['hr'] = df['datetime'].dt.hour

# 2. Ajustar el modelo OLS (El que tiene el fallo)
formula = "bikers ~ hr + temp + workingday + weathersit"
modelo_lineal = smf.ols(formula, data=df).fit()

# 3. Generar las predicciones
df['pred_lm'] = modelo_lineal.predict(df)

# 4. GENERAR LA GRÁFICA EXACTA
plt.figure(figsize=(10, 6))

# Dibujar la nube de puntos en naranja con transparencia
plt.scatter(df['bikers'], df['pred_lm'], alpha=0.3, color='orange', label='Predicciones OLS')

# Dibujar la línea roja punteada en el CERO (La "línea del fallo")
plt.axhline(0, color='red', linestyle='--', linewidth=2)

# Configuración de etiquetas y cuadrícula
plt.xlabel('Valores Reales (Bikers)', fontsize=12)
plt.ylabel('Valores Predichos por OLS', fontsize=12)
plt.title('Evidencia de Fallo: Predicciones por debajo de cero', fontsize=14)
plt.grid(alpha=0.2)
plt.legend()

# 5. Guardar y mostrar
plt.show()
