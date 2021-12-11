from PyQt5.QtWidgets import *
import requests
from designer import Ui_frmMain
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon ,QKeySequence
from bs4 import BeautifulSoup
import json

class deprem(QMainWindow):

 def __init__(self):
    super().__init__()

    self.ui = Ui_frmMain()
    self.ui.setupUi(self)

    self.ui.btnExt.setToolTip("Ctrl+Q ya bas")
    self.ui.btnUpdate.setToolTip("Ctrl+U ya bas")
    self.ui.btnAll.setToolTip("Ctrl+A ya bas")
    self.ui.btnDanger.setToolTip("Ctrl+D ye bas")

    self.ui.btnDanger.clicked.connect(self.btnDangerClickedSlot)
    self.ui.btnAll.clicked.connect(self.btnAllClickedSlot)
    self.ui.btnExt.clicked.connect(self.btnExtClickedSlot)
    self.ui.lndtSehir.returnPressed.connect(self.proccesCity)
    self.ui.lndtDeger.returnPressed.connect(self.proccesValue)

 def btnAllClickedSlot(self):
     r = requests.get("https://turkiyedepremapi.herokuapp.com")
     payload = {}
     headers = {}
     responseAll = requests.request("GET",
                                     url="https://turkiyedepremapi.herokuapp.com/api",
                                     headers=headers, data=payload)
     resultAll = json.loads(responseAll.text)
     print(resultAll)

 # def btnDangerClickedSlot(self):
 #     r = requests.get("https://turkiyedepremapi.herokuapp.com")
 #     received_signalDanger = 7
 #     payload = {}
 #     headers = {}
 #     responseDanger = requests.request("GET",
 #                                       url="https://turkiyedepremapi.herokuapp.com/api?min=" + received_signalDanger + "&max=" + received_signalDanger,
 #                                       headers=headers, data=payload)
 #     resultDanger = json.loads(responseDanger.text)
 #     print("Yıkıcı Hasar Alanlar:  ")
 #
 #     # if responseDanger>=7:
 #
 #
 #     print(resultDanger)
 #
 #     # else:
 #     #     print("Yıkıcı Hasar Saptanmadı.")
 #
 #


 def proccesCity(self):

     r = requests.get("https://turkiyedepremapi.herokuapp.com")
     received_signalCity = self.ui.lndtSehir.text()
     payload = {}
     headers = {}
     responseCity = requests.request("GET", url="https://turkiyedepremapi.herokuapp.com/api?sehir=(" + received_signalCity + ")",
                                 headers=headers, data=payload)
     resultCity = json.loads(responseCity.text)
     print("İstenilen Şehir: ", received_signalCity)
     print(resultCity)



 def proccesValue(self):
    r = requests.get("https://turkiyedepremapi.herokuapp.com")
    received_signalValue = self.ui.lndtDeger.text()
    payload = {}
    headers = {}
    responseValue = requests.request("GET ",url="https://turkiyedepremapi.herokuapp.com/api?min="+received_signal+"&max="+received_signal,
                                          headers=headers, data=payload)
    resultValue = json.loads(responseValue.text)
    print("Deprem Büyüklüğü: ", received_signalValue)
    print(resultValue)





 def btnExtClickedSlot(self):
     print("Çıkılıyor")
     quit()








# def sehir():
#
#       sehir = input("Şehir Yazınız:  ")
#       r = requests.get("https://turkiyedepremapi.herokuapp.com")
#       print("Sunucu Yanıtı:  " , r.status_code)
#       if r.status_code == 200:
#           print("Durum:   Bağlantı Başarılı")
#
#
#
#       payload = {}
#       headers = {}
#       response = requests.request("GET", url="https://turkiyedepremapi.herokuapp.com/api?sehir=("+sehir+")", headers=headers, data=payload)
#       result = json.loads(response.text)
#       print(result)
#
#
# print(sehir())
#



uygulama = QApplication([])
pencere = deprem()
pencere.show()
uygulama.exec()
