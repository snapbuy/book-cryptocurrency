import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/chart.ui", self)

        self.priceData = QLineSeries()
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()
        self.priceChart.createDefaultAxes()
        self.priceView.setChart(self.priceChart)

        # ----------------- 추 가 ------------------
        self.dataLimit = 60
        self.viewLimit = 30
        # ------------------------------------------

    def updateData(self, idx, price):
        # ----------------- 추 가 ------------------
        if len(self.priceData) == self.dataLimit :
            self.priceData.remove(0)
        # ------------------------------------------
        self.priceData.append(idx, price)
        self.__updateAxis()


    def __updateAxis(self):
        # ----------------- 수 정 ------------------
        minValX = sys.maxsize
        maxValX = 0
        minValY = sys.maxsize
        maxValY = 0
        for p in self.priceData.pointsVector()[-self.viewLimit:]:
            minValX = min(minValX, p.x())
            maxValX = max(maxValX, p.x())
            minValY = min(minValY, p.y())
            maxValY = max(maxValY, p.y())
        padding = (maxValY - minValY) / 10

        ax = self.priceChart.axisX(self.priceData)
        ax.setRange(minValX, maxValX)
        ay = self.priceChart.axisY(self.priceData)
        ay.setRange(minValY - padding, maxValY + padding)
        ay.setLabelFormat("%d")
        # ------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    # ----------------- 추 가 ------------------
    for i in range(100):
        cw.updateData(i, i)
    # ------------------------------------------
    cw.show()
    exit(app.exec_())
