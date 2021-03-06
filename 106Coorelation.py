from statistics import correlation
import plotly_express as px
import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days = []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_file:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))

    return {"x": marks, "y": days}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation of Student's Marks and Days Present is: \n", correlation[0,1])

def main():
    data_path = "markspresentdata3.csv"
    datasource = getDataSource(data_path)

    findCorrelation(datasource)

main()