from collections import Counter
from openpyxl.chart import (
    PieChart,
    Reference
)
from openpyxl.chart.series import DataPoint

def create_pie_chart(sheet, numOfStocks,sectors) :
    dictSector = Counter(sectors)


    pie = PieChart()
    labels = Reference(sheet, min_col=1, min_row=2, max_row=numOfStocks + 1)
    data = Reference(sheet, min_col=5, min_row=1, max_row=numOfStocks + 1)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.title = "Percentage of Shares in Portfolio"
    pie.height = 12
    pie.width = 20

    sheet.add_chart(pie, "K1")

    pie2 = PieChart()
    labels = Reference(sheet, min_col=7, min_row=27, max_row=26 + len(dictSector))
    data = Reference(sheet, min_col=8, min_row=26, max_row= 26 + len(dictSector))
    pie2.add_data(data, titles_from_data=True)
    pie2.set_categories(labels)
    pie2.title = "Percentage of Sectors in Portfolio"
    pie2.height = 12
    pie2.width = 20

    sheet.add_chart(pie2, "K26")
