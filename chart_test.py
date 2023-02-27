import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QColor, QPen

class WinLoseCircleGraph:
    def __init__(self, win_rate, lose_rate):
        self.win_rate = win_rate
        self.lose_rate = lose_rate
        self.app = QApplication([])
        self.win = QMainWindow()
        self.plot_widget = pg.PlotWidget()
        self.initUI()

    def initUI(self):
        # Create the circle graph
        angle = 0
        items = []
        # for win, lose in zip(self.win_rate, self.lose_rate):
        # Calculate the size of the win sector
        win_size = int(self.win_rate * 360)

        self.plot_widget.hideAxis('left')
        self.plot_widget.hideAxis('bottom')

        # Create a win sector item
        win_sector_item = QGraphicsEllipseItem(-50, -50, 100, 100)
        win_sector_item.setStartAngle(angle * 16)
        win_sector_item.setSpanAngle(win_size * 16)
        win_sector_item.setBrush(QBrush(QColor(round(self.win_rate * 255), round((1-self.win_rate) * 255), 0)))  # Set the color of the win sector
        win_sector_item.setPen(QPen(QColor(255, 255, 255)))  # Set the color of the border
        items.append(win_sector_item)

        # Calculate the size of the lose sector
        lose_size = int(self.lose_rate * 360)

        # Create a lose sector item
        lose_sector_item = QGraphicsEllipseItem(-50, -50, 100, 100)
        lose_sector_item.setStartAngle((angle + win_size) * 16)
        lose_sector_item.setSpanAngle(lose_size * 16)
        lose_sector_item.setBrush(QBrush(QColor(255, 0, round(self.lose_rate * 255))))  # Set the color of the lose sector
        lose_sector_item.setPen(QPen(QColor(255, 255, 255)))  # Set the color of the border
        items.append(lose_sector_item)

        # Update the angle for the next sector
        angle += win_size + lose_size

        # Create a group item to hold all the sector items
        group_item = pg.QtWidgets.QGraphicsItemGroup()
        for item in items:
            group_item.addToGroup(item)

        # Add the group item to the plot widget
        self.plot_widget.addItem(group_item)

        # Add the plot widget to the main window and show it
        self.win.setCentralWidget(self.plot_widget)
        self.win.show()

    def run(self):
        self.app.exec_()

if __name__ == "__main__":
    win_rates = 0.5
    lose_rate = 0.5
    graph = WinLoseCircleGraph(win_rates, lose_rate)
    graph.run()