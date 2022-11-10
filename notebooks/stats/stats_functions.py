import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches

def likelihood(model, data, x_limits, dim=1, y_limits=(None, None), grid_res=(100, 100), n_ticks=3, x_label='', y_label='', x_y_ref_point=(None, None), fixed_params=None):
    # set limits for x and y axes
    x_min, x_max = x_limits
    y_min, y_max = y_limits
    
    # set grid resolution
    xn, yn = grid_res
    
    # create equally spaced x and y axis points
    xs = np.linspace(x_min, x_max, xn)
    ys = np.linspace(y_min, y_max, yn)
    
    # create x and y coordinate grids
    xv, yv = np.meshgrid(xs, ys)

    # create [x, y] coordinare pairs for every point in the grid
    stack = np.dstack((yv, xv)).reshape((len(xv) * len(yv), 2))

    if fixed_params is not None:
        stack = np.array([np.append(a, fixed_params) for a in stack])

    # calculate the negative log likelihood for each point in the grid, then reshape to fit original dimensions
    im = np.array([model.nnlf(xy, data) for xy in stack]).reshape((len(xv), len(yv)))
    im = im - im.min()
    
    if dim == 2:
        # plotting
        plt.figure(figsize=(10, 10))

        plt.imshow(im)
        cset = plt.contour(im, [-30, -20, -10, 0, 0.5, 1, 2, 4, 8, 16, 32, 64], linewidths=3)
        plt.clabel(cset, inline=True, fmt='%1.1f', fontsize=12)
        
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        
        # Create t + 2 ticks, ignore first and last one
        # TODO: why shift by 0.5?
        x_ticks = (np.linspace(0, xn, n_ticks + 2) - 0.5)[1:-1]
        y_ticks = (np.linspace(0, yn, n_ticks + 2) - 0.5)[1:-1]
        
        # Create n_ticks + 2 labels, ignore first and last one
        x_tick_labels = [f'{label:.2f}' for label in np.linspace(x_min, x_max , n_ticks + 2)][1:-1]
        y_tick_labels = [f'{label:.2f}' for label in np.linspace(y_min, y_max , n_ticks + 2)][1:-1]
        
        plt.xticks(x_ticks, x_tick_labels)
        plt.yticks(y_ticks, y_tick_labels)
        
        if all(x_y_ref_point):
            plt.scatter((x_min - x_y_ref_point[0]) / (x_min - x_max) * (xn - 1), (y_min - x_y_ref_point[1]) / (y_min - y_max) * (yn - 1), marker='x', s=100, color='red', label = 'Fit parameters')
            plt.legend()
    elif dim == 1:
        # plot mean
        plt.plot(np.linspace(y_min, y_max, len(im)), im.mean(axis=0) / im.mean(axis=0).min() - 1, color = 'dodgerblue', label='1D-Liklihood function')
        plt.xlabel(y_label)
        if all(x_y_ref_point):
            plt.axvline(x_y_ref_point[1], color='red', linestyle='dashed', linewidth=2, label='Fitted mean')
        plt.legend()
        plt.show()
        # plot width
        plt.plot(np.linspace(x_min, x_max, len(im)), im.mean(axis=0) / im.mean(axis=0).min() - 1, color = 'dodgerblue', label='1D-Liklihood function')
        plt.xlabel(x_label)
        if all(x_y_ref_point):
            plt.axvline(x_y_ref_point[0], color='red', linestyle='dashed', linewidth=2, label='Fitted width')
        plt.legend()
        plt.show()



def pullpdf(model, params, y, nbins=20):
    plt.figure()

    gs1 = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
    gs1.update(wspace=0.025, hspace=0.00)

    ax1 = plt.subplot(gs1[0])
    vals = plt.hist(y, bins=nbins, color='dodgerblue')

    bins = vals[1]
    width = (max(bins) - min(bins))/(len(bins) - 1)
    bin_centers = (bins[1:] + bins[:-1]) / 2
    size=len(y)

    model_data = model.pdf(bin_centers, *params) * size * width
    plt.plot(np.linspace(bin_centers[0], bin_centers[-1], nbins), model_data, color='red')

    plt.setp(ax1.get_xticklabels(), visible=False)

    residuen = vals[0] - model_data
    pulls = residuen / np.sqrt(vals[0] + 0.00000000001)

    ax2 = plt.subplot(gs1[1], sharex=ax1)
    plt.errorbar(bin_centers, pulls, xerr=width / 2, yerr=1, fmt='.')
    plt.ylim(-7,7)
    plt.setp(ax2.get_xticklabels(), visible=True)

    xmin = bins[0]
    xmax = bins[-1]
    width = xmax - xmin

    plt.xlim(xmin,xmax)
    ax2.add_patch(
        patches.Rectangle(
            (xmin, -1),   # (x,y)
            width,          # width
            2,          # height
            color = 'green', alpha = 0.2))
    ax2.add_patch(
        patches.Rectangle(
            (xmin, -7),   # (x,y)
            width,          # width
            4,          # height
            color = 'orange', alpha = 0.2)
        )
    ax2.add_patch(
        patches.Rectangle(
            (xmin, 3),   # (x,y)
            width,          # width
            4,          # height
            color = 'orange', alpha = 0.2)
        )