import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

matplotlib.style.use('ggplot')
df_rand = pd.Series(np.random.randn(2000))
df_rand_sum = df_rand.cumsum()
df_rand_sum.plot()
plt.show()

fig, ax = 