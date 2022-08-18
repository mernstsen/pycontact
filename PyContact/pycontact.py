""" Authors: Maximilian Scheurer, Peter Rodenkirch
    Date created: May 2016
"""

import warnings
import sys

from PyQt6.QtWidgets import QApplication

from .gui.MainWindow import MainWindow

warnings.filterwarnings("ignore")


def main():
    """Pycontact main function."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
