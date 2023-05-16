import matplotlib.pyplot as plt


class Graph:

    def view(self, data):
        plt.hist(data, bins=)
        plt.xlabel('Distance')
        plt.ylabel('Count')
        plt.show()