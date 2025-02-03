import numpy as np
import pandas as pd
from .e1_modulo import plt, linea, barra
from .e1_modulo import caja, histograma

df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
df = df.cumsum()

plt.title('Histograma de columna_name')
