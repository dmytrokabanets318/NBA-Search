from lab.visualizer import Visualizer
import csv

class CSVBuilder(Visualizer):

    def __init__(self, file):
        super().__init__()
        self.csv = file

    # This function is to build a pie chart of the labels
    # in current csv file and load into plot
    def build_pie(self):
        labels = []
        weights = []

        with self.csv as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = ',')
            for row in csv_reader:
                if len(row) > 0:
                    label = row[len(row) - 1]

                    if label in labels:
                        weights[labels.index(label)] += 1
                    else:
                        labels.append(row[len(row) - 1])
                        weights.append(1)

        fig1, pie_chart = self.plt.subplots()
        pie_chart.pie(weights, labels = labels, autopct = '%1.2f%%', startangle = 90)
        pie_chart.axis('equal')
