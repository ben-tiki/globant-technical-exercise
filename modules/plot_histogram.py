import base64
import io
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def plot_hist(growth_metrics_dict: dict):

    # generate plot
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    # set title and labels
    axis.set_title("Berry Growth Time")
    axis.set_xlabel("Bins")
    axis.set_ylabel("Growth Time")
    # style options
    for side in ['top', 'right', 'left', 'bottom']:
        axis.spines[side].set_visible(False)
    axis.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    axis.set_axisbelow(True)

    growth_time_list = growth_metrics_dict['growth_time_list']
    axis.hist(growth_time_list, bins=5,
              color='#bfd732', alpha=0.7, rwidth=0.85)

    # convert plot to PNG image
    pngImage = io.BytesIO()
    FigureCanvas(fig).print_png(pngImage)

    # encode PNG image to base64 string
    pngImageB64String = "data:image/png;base64,"
    pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return pngImageB64String