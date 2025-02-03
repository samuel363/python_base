import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

# df = pd.DataFrame(np.random.randn(100, 5), columns=list('ABCDE'))
# df = df.cumsum()
#
# plt.title('Histograma de columna_name')

""" Lineas """
def linea(df):
    df.plot()
    plt.show()

""" Barras """
def barra(df):
    df.plot.bar(stacked=True)
    plt.show()

""" Cajas """
def caja(df):
    df.plot.box()
    plt.show()

""" Histograma """
def histograma(data):
    data.hist(grid=False)
    plt.show()
