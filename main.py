import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QVBoxLayout, QPushButton, QFormLayout
import variables
import fonts
import countries
import weatherData


def clearForm(data_layout):
    while data_layout.rowCount() > 0:
        for role in [QFormLayout.LabelRole, QFormLayout.FieldRole]:
            item = data_layout.itemAt(0,role)
            if item is not None:
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        data_layout.removeRow(0)


def main():
    global dataContainerContainsData
    dataContainerContainsData = False


    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("Weather Information: ")
    window.setGeometry(100, 100, variables._screenWidth, variables._screenHeight)

    main_layout = QVBoxLayout()
    content = QWidget()
    content_layout = QVBoxLayout()
    DataContainer = QWidget()
    dataLayout = QFormLayout()

    #title of the window
    titleLabel = QLabel("Weather Information", window)
    titleLabel.setFont(fonts._titleFont)
    

    #drop down menu
    capitalCity = QComboBox()
    capitalCity.addItems(countries.capital_cities)
    content_layout.addWidget(capitalCity)


    #button 
    getWeatherInformation = QPushButton("Get Weather Information")
    getWeatherInformation.setFont(fonts._buttonfonts)
    content_layout.addWidget(getWeatherInformation)

    def onButtonClicked():
        global dataContainerContainsData
        if(dataContainerContainsData == True):
            clearForm(dataLayout)
            dataContainerContainsData = False
        else:
            dataContainerContainsData = True
        selectedcity = capitalCity.currentText()
        data = weatherData.getData(selectedcity)
        if(data["Code"] == 200):
            for key,value in data.items():
                if(key != "Code"):
                    dataLayout.addRow(QLabel(key + ':') , QLabel(str(value)))

        DataContainer.setLayout(dataLayout)
        main_layout.addWidget(DataContainer)
    
    content.setLayout(content_layout)
    main_layout.addWidget(titleLabel)
    main_layout.addWidget(content)
    window.setLayout(main_layout)


    getWeatherInformation.clicked.connect(onButtonClicked)
    window.show()

    sys.exit(app.exec_())


if(__name__ == "__main__"):
    main()