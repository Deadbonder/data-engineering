import matplotlib
matplotlib.use('Agg')  # save to file, no window needed
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

df = load_wine(as_frame=True).frame

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

ax[0].hist(df['alcohol'], bins=15)
ax[0].set(title='Alcohol distribution', xlabel='alcohol', ylabel='count')

for t in sorted(df['target'].unique()):
    part = df[df['target'] == t]
    ax[1].scatter(part['alcohol'], part['color_intensity'], label=f'cultivar {t}')
ax[1].set(title='Alcohol vs colour intensity', xlabel='alcohol', ylabel='color_intensity')
ax[1].legend()

df['target'].value_counts().sort_index().plot.bar(ax=ax[2])
ax[2].set(title='Wines per cultivar', xlabel='cultivar', ylabel='count')

fig.tight_layout()
fig.savefig('matplotlib_practice/wine_plots.png', dpi=120)
