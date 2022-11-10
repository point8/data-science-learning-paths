import html

import jupyterthemes
import seaborn

from . import datasets, mlp, mlts

p8_colors = [
    "#15985C",
    "#DD841E",
    "#2A4958",
    "#2C6048",
    "#8B683F",
    "#4598C0",
    "#41C78A",
    "#ECA34E",
    "#19668C",
    "#62A1C0",
    "#60C798",
    "#ECB473",
]
p8_palette = seaborn.color_palette(p8_colors)


def setup_plot_style(dark=False):
    if dark:
        theme = "monokai"
    else:
        theme = None  # TODO: select favorite light theme
    seaborn.set_style("ticks")
    jupyterthemes.jtplot.style(theme=theme, grid=True, figsize=(20, 5))
    seaborn.set_palette(p8_palette)


def show_command(cmd):
    """
    Display a terminal command with HTML layour
    """
    from IPython.display import HTML, display

    return HTML(
        f"<div style='margin:0 0 5px; overflow:hidden; padding:10px; background-color:DimGray; border:1px solid DimGray; -webkit-border-radius: 5px;border-radius: 5px;'><tt>{html.escape(cmd)}</tt></p>"
    )
