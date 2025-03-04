import sys
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtWidgets
#import test as test
import gui as gui  # импортируем самописные модули
import ZMQ_read as socket
import parser as parser
import plotter as plotter


# port = "37000"

plot_data = []

if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

if len(sys.argv) > 2:
    port1 = sys.argv[2]
    int(port1)

port = gui.ask_port()
print(port)
#test()

while True:
    input_data = socket.zmq_read(port)
    print(input_data)
    plot_data, event_header = parser.parse(input_data)
    print(plot_data)
    plot_figure = plotter.histogrammer(plot_data)
