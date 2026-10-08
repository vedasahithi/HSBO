import PySimpleGUI as sg
import matplotlib.pyplot as plt
import RUN
import numpy as np
sg.change_look_and_feel('LightBrown13')
# sg.change_look_and_feel('DarkRed4')
import warnings
warnings.filterwarnings("ignore")


# Designing layout
layout = [[sg.Text("\n")],
          [sg.Text("\t\t"), sg.Text("\tTraining Samples(%)\t"), sg.Combo(["60", "70", "80", "90"], size=(14, 2)), sg.Text("   "), sg.Text("\n")],
          [sg.Text("\t\t\t\t\t\t    "), sg.Button("START", size=(14, 1)), sg.Text("\n")],

          [sg.Text("\n")], [sg.Text("\t\t CybS-CC-SACGAN-COA\tRF-RBFNN\t\tFEFS-DLM\tIMFL-IDSCS\t  Proposed HSBOA_QRNN")],
          [sg.Text('\tAccuracy'), sg.In(key='11', size=(18, 18)), sg.In(key='12', size=(18, 18)), sg.In(key='13', size=(18, 18)),
           sg.In(key='14', size=(18, 18)), sg.In(key='15', size=(18, 18))],

          [sg.Text('\tTPR\t'), sg.In(key='21', size=(18, 18)), sg.In(key='22', size=(18, 18)), sg.In(key='23', size=(18, 18)),
           sg.In(key='24', size=(18, 18)), sg.In(key='25', size=(18, 18))],

          [sg.Text('\tTNR\t'), sg.In(key='31', size=(18, 18)), sg.In(key='32', size=(18, 18)), sg.In(key='33', size=(18, 18)),
           sg.In(key='34', size=(18, 18)), sg.In(key='35', size=(18, 18))],

          [sg.Text('\n\t\t\t\t\t\t\t\t\t\t\t    '), sg.Button('Run Graph'), sg.Text(" "), sg.Button('Close')]]


# to plot graph
def plot_graph(result_1, result_2, result_3):

    loc, result = [], []
    result.append(result_1)  # appending the result
    result.append(result_2)
    result.append(result_3)
    result = np.transpose(result)

    # labels for bars
    labels = ['CybS-CC-SACGAN-COA', 'RF-RBFNN', 'FEFS-DLM', 'IMFL-IDSCS', "Proposed HSBOA_QRNN"]         # x-axis labels
    tick_labels = ['Accuracy', 'TPR', 'TNR']                           # metrics
    bar_width, s = 0.12, 0                                                      # bar width, space between bars

    for i in range(len(result)):                                                # allocating location for bars
        if i == 0:                                                              # initial location - 1st result
            tem = []
            for j in range(len(tick_labels)):
                tem.append(j + 1)
            loc.append(tem)
        else:                                                                    # location from 2nd result
            tem = []
            for j in range(len(loc[i - 1])):
                tem.append(loc[i - 1][j] + s + bar_width)
            loc.append(tem)

    # plotting a bar chart
    for i in range(len(result)):
        plt.bar(loc[i], result[i], label=labels[i], tick_label=tick_labels, width=bar_width)
    plt.legend(loc="lower right",
               prop={'weight': 'bold', 'size': '15'})                # show a legend on the plot
    plt.show()                                                                    # to show the plot


# Create the Window layout
window = sg.Window('GUI', layout)

# event loop
while True:
    event, values = window.read()                                                   # displays the window
    if event == "START":
        tr = int(values[0]) / 100

        ACC, TPR, TNR = RUN.call_main(tr)
        print("\nCode Execution Done!")
        window.Element('11').Update(ACC[0])
        window.Element('12').Update(ACC[1])
        window.Element('13').Update(ACC[2])
        window.Element('14').Update(ACC[3])
        window.Element('15').Update(ACC[4])
        
        window.Element('21').Update(TPR[0])
        window.Element('22').Update(TPR[1])
        window.Element('23').Update(TPR[2])
        window.Element('24').Update(TPR[3])
        window.Element('25').Update(TPR[4])
        
        window.Element('31').Update(TNR[0])
        window.Element('32').Update(TNR[1])
        window.Element('33').Update(TNR[2])
        window.Element('34').Update(TNR[3])
        window.Element('35').Update(TNR[4])

    if event == 'Run Graph':
        plot_graph(ACC, TPR, TNR)
    if event == 'Close':
        window.close()
        break

window.close()
