from bs4 import BeautifulSoup
import requests
import pandas as pd
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import pyqtSlot
class Game(QMainWindow):
    def __init__(self):
        super().__init__()
                
        self.combo = QComboBox(self)
        self.combo.addItem("PowerBall")
        self.combo.addItem("Mega Millions")
        self.combo.addItem("Classic Lotto")

        self.combo.move(150,100)

        self.qlabel = QLabel(self)
        self.qlabel.move(100,50)
        
        self.combo_1 = QComboBox(self)
        
        self.combo_1.addItem("2022")
        self.combo_1.addItem("2021")
        self.combo_1.addItem("2020")
        self.combo_1.addItem("2019")
        self.combo_1.addItem("2018")
        self.combo_1.addItem("2017")
        self.combo_1.addItem("2016")

        self.combo_1.move(150, 150)

        self.qlabel = QLabel(self)
        self.qlabel.move(50,16)


        self.button = QPushButton('Download', self)
        self.button.move(250,250)
        
        self.button.clicked.connect(self.run)
        self.label = QLabel(self)
  
        # setting geometry of the label
        self.label.setGeometry(200, 200, 200, 30)
        
        self.setGeometry(50,50,500,400)
        self.setWindowTitle("Web Mining Program")
        self.show()

        
    @pyqtSlot()
    def run(self):
        content_game = self.combo.currentText()
        content_date = self.combo_1.currentText()
        # self.label.setText("Content Game : " + content_game + "Content Date : " + content_date)
        if content_game == "PowerBall":
            url = f"https://lottery.com/previous-results/us/powerball/{content_date}/"
            self.powerball(url)
        elif content_game == "Mega Millions":
            url = f"https://lottery.com/previous-results/us/megamillions/{content_date}/"
            self.mega_millions(url)
        else:
            url = f"https://lottery.com/previous-results/oh/classiclottooh/{content_date}/"
            self.classic_lotto(url)
            # print(run.classic_lotto(url,date))
            
    def powerball(self,url):
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content,'html.parser')
        
        table = soup.find('table',class_ = 'lottery-table')
        
        df = pd.DataFrame(columns = ['Date','Numbers','Sum of Numbers'])
        
        for row in table.tbody.find_all('tr'):
            columns = row.find_all('td')
            
            if columns != []:
                date = columns[1].text.strip()
                numbers = columns[3].text.strip()
                
                df = df.append({'Date':date,'Numbers':numbers},ignore_index = True)
        sum_of_numbers_list = list()
        number = ""
        for i in range(len(df['Numbers'])):
            # df['Numbers'][i] = df['Numbers'][i][-15:-30] 
            number = df['Numbers'][i]
            sum_of_numbers_list.append(number.split('-'))
            sum_of_numbers_list[i][-1] = sum_of_numbers_list[-1][0]
        new_numbers_list = list()
        for i in df['Numbers']:
            new_numbers_list.append(i[0:-15:1])
        
        numbers = list()
        summ = len(sum_of_numbers_list)
        for i in range(summ):
            sum = 0
            for j in range(6): 
                sum = sum + int(sum_of_numbers_list[i][j])
            numbers.append(sum)
        series = pd.Series(numbers)
        numbers_series = pd.Series(new_numbers_list)
        df['Sum of Numbers'] = series.values
        df['Numbers'] = numbers_series.values
        df.to_excel('powerball.xlsx')
        return True
    
    def mega_millions(self,url):
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content,'html.parser')
        
        table = soup.find('table',class_ = 'lottery-table')
        
        df = pd.DataFrame(columns = ['Date','Numbers','Sum of Numbers'])
        
        for row in table.tbody.find_all('tr'):
            columns = row.find_all('td')
            
            if columns != []:
                date = columns[1].text.strip()
                numbers = columns[3].text.strip()
                
                df = df.append({'Date':date,'Numbers':numbers},ignore_index = True)
        sum_of_numbers_list = list()
        number = ""
        for i in range(len(df['Numbers'])):
            # df['Numbers'][i] = df['Numbers'][i][-15:-30] 
            number = df['Numbers'][i]
            sum_of_numbers_list.append(number.split('-'))
            sum_of_numbers_list[i][-1] = sum_of_numbers_list[-1][:2]
        new_numbers_list = list()
        for i in df['Numbers']:
            new_numbers_list.append(i[0:-15:1])
        
        numbers = list()
        summ = len(sum_of_numbers_list)
        for i in range(summ):
            sum = 0
            for j in range(6): 
                sum = sum + int(sum_of_numbers_list[i][j])
            numbers.append(sum)
        series = pd.Series(numbers)
        numbers_series = pd.Series(new_numbers_list)
        df['Sum of Numbers'] = series.values
        df['Numbers'] = numbers_series.values
        df.to_excel('mega_millions.xlsx')
        return True
    
    def classic_lotto(self,url):
        response = requests.get(url)
        
        soup = BeautifulSoup(response.content,'html.parser')
        
        table = soup.find('table',class_ = 'lottery-table')
        
        df = pd.DataFrame(columns = ['Date','Numbers','Sum of Numbers'])
        
        for row in table.tbody.find_all('tr'):
            columns = row.find_all('td')
            
            if columns != []:
                date = columns[1].text.strip()
                numbers = columns[3].text.strip()
                
                df = df.append({'Date':date,'Numbers':numbers},ignore_index = True)
        sum_of_numbers_list = list()
        number = ""
        for i in range(len(df['Numbers'])):
            # df['Numbers'][i] = df['Numbers'][i][-15:-30] 
            number = df['Numbers'][i]
            sum_of_numbers_list.append(number.split('-'))
            sum_of_numbers_list[i][-1] = sum_of_numbers_list[-1][0]
        new_numbers_list = list()
        for i in df['Numbers']:
            new_numbers_list.append(i[0:-15:1])
        
        numbers = list()
        summ = len(sum_of_numbers_list)
        for i in range(summ):
            sum = 0
            for j in range(6): 
                sum = sum + int(sum_of_numbers_list[i][j])
            numbers.append(sum)
        series = pd.Series(numbers)
        numbers_series = pd.Series(new_numbers_list)
        df['Sum of Numbers'] = series.values
        df['Numbers'] = numbers_series.values
        df.to_excel('classic_lotto.xlsx')
        return True
    
    
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MAIN = Game()
    sys.exit(app.exec_())
