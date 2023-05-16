import matplotlib.pyplot as plt


class Graph:

    def view(self, data):
        plt.hist(data, bins=25)
        plt.xlabel('Distance')
        plt.ylabel('Count')
        plt.show()