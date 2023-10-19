def cacti_number(plot_func):
    def wrapper(plot):
        if not (isinstance(plot, list)):
            raise TypeError("Input must be a list.")

        ylim = len(plot[0]) - 1
        xlim = len(plot) - 1

        x_bound = (0, xlim)
        y_bound = (0, ylim)

        rows = xlim+1
        cols = ylim+1

        count = 0

        for i in range(rows):
            for j in range(cols):
                if plot[i][j] == 0:

                    valid_slot = True  # space is valid unless...any of these

                    if not out_of_range(y_bound, j+1):
                        if plot[i][j+1] == 1:  # check below
                            valid_slot = False

                    if not out_of_range(y_bound, j-1):
                        if plot[i][j-1] == 1:  # check above
                            valid_slot = False

                    if not out_of_range(x_bound, i-1):
                        if plot[i-1][j] == 1:  # check left
                            valid_slot = False

                    if not out_of_range(x_bound, i+1):
                        if plot[i+1][j] == 1:  # check right
                            valid_slot = False

                    if valid_slot:
                        count += 1
                        plot[i][j] = 1

        return count
    return wrapper


def out_of_range(bound, move):

    if (bound[0] > move or bound[1] < move):  # bound[0] = 0, bound[1] = xlim or ylim
        return True
    else:
        return False
