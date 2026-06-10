from pathlib import Path
import matplotlib.pyplot as plt

def save_figure(fig, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path)

def blank_figure(title="Figure"):
    fig, ax = plt.subplots()
    ax.set_title(title)
    return fig
