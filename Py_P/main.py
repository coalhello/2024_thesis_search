import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import research_thesis
import webbrowser

form_class = uic.loadUiType("sample.ui")[0]

class Mywindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def get_subject(self):
        num = ''
        info = self.input_line.text()

        with open("C:/Users/siri4/OneDrive/바탕 화면/Py_P/storage/subject.txt", "w+") as safe_subject:
            safe_subject.write(info)

        txt = str(research_thesis.get_max())
        self.max_label.setText("최댓값 : " + txt)
        index = txt.find("건")
        Lnum = txt[:index].split(",")
        for i in range(len(Lnum)):
            num += Lnum[i]
        self.slider.setMaximum(int(num))

    def recent_signal(self, value):
        self.recent_label.setText("현재값 : " + f'{int(value):,}' + "건")
        global recent_value
        recent_value = int(value)

    def research(self):
        L_title = []
        self.output_list.clear()
        if recent_value > 20:
            QMessageBox.information(self, "오류", "20이하로 설정해주세요")
        elif recent_value == 0:
            QMessageBox.information(self, "오류", "0보다 큰 값으로 설정해주세요")
        else:
            research_thesis.get_info(recent_value)
            with open("C:/Users/siri4/OneDrive/바탕 화면/Py_P/storage/title.txt") as title:
                for line in title:
                    L_title.append(line.strip())

            for i in range(len(L_title)):
                self.output_list.insertItem(i, str(L_title[i]))

    def making_excel(self):
        research_thesis.make_yxl()

    def selected_box(self, item):
        global user_item
        user_item = item.text()

    def join_link(self):
        url = research_thesis.move_link(user_item)
        webbrowser.open(url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Mywindow()
    myWindow.show()
    app.exec_()