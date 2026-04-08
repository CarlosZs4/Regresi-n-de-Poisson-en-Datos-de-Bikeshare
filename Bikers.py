import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Cargar los datos
df = pd.read_csv('Bikeshare.csv')

# 2. Configurar el estilo visual
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Crear el Histograma de la variable 'bikers'
# 'kde=True' añade la línea de densidad que ayuda a ver la forma de la distribución
sns.histplot(df['bikers'], kde=True, color='teal', bins=50)

# 4. Personalizar etiquetas según la terminología del proyecto
plt.title('Análisis Exploratorio: Distribución de la Variable Bikers', fontsize=14)
plt.xlabel('Número de Alquileres por Hora (Valores de la Variable Aleatoria $Y$)', fontsize=12)
plt.ylabel('Frecuencia (Número de horas en el dataset)', fontsize=12)

# Añadir una nota explicativa en la gráfica (opcional)
plt.text(600, 1500, 'Sesgo positivo:\nMuchos registros cerca de 0\n(Poisson con $\lambda$ pequeño)', 
         bbox=dict(facecolor='white', alpha=0.5))


# 6. Mostrar gráfica
plt.show()
