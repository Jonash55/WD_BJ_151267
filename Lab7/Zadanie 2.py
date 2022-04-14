import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

df = pd.read_csv('data/pkn.txt', delimiter=',')

df_copy = df.copy()
df_copy = df_copy.astype({'<DATE>': str})
for index, row in df.iterrows():
    string = str(row['<DATE>'])
    year = string[0:4]
    month = string[4:6]
    day = string[6:8]
    date = "-".join([year, month, day])
    df_copy.at[index, '<DATE>'] = date

fig, ax = plt.subplots(figsize=(25, 10))

x = list(df_copy['<DATE>'])[0:20]
line, = ax.plot(x, list(df_copy['<CLOSE>'])[0:20])


def animate(i):
    start = 20 * i
    line.set_xdata(df_copy['<DATE>'][start:start + 20])
    line.set_ydata(df_copy['<CLOSE>'][start:start + 20])
    ax.set_xlim(df_copy['<DATE>'][start], df_copy['<DATE>'][start + 20])
    ax.set_ylim(np.min(df_copy['<CLOSE>'][start:start + 20]) - 5, np.max(df_copy['<CLOSE>'][start:start + 20]) + 5)
    return line,


ani = animation.FuncAnimation(
    fig, animate, interval=20, frames=df.shape[0]//20, blit=True, save_count=50)

plt.show()
