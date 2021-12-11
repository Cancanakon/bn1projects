from PyQt5.QtWidgets import *
import requests
from designer import Ui_frmMain
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon ,QKeySequence
from bs4 import BeautifulSoup
import json
from PyQt5.QtGui import QIntValidator


class depremler(QMainWindow):

    r = requests.get("https://turkiyedepremapi.herokuapp.com")


    def __init__(self):
        super().__init__()

        self.ui = Ui_frmMain()
        self.ui.setupUi(self)


        #Mesaj Kutusu Tanımlıyoruz.


        QMessageBox.about(self,"DEPREM APP HAKKINDA","<font size = 5> Bu uygulama<b> Blacknight</b> görevi içindir."
                                "<br><br>"
                                 "<b>İletişim İçin</>"
                                  "<br>"
                                   "<a href=\"https://www.instagram.com/blacknight_tek\">BLACKNIGHT</a>"
                                "</font>")


        #Kısayol atamalarımız için yazı(üstüne gelince)
        self.ui.btnExt.setToolTip("Ctrl+Q ya bas")
        self.ui.btnUpdate.setToolTip("Ctrl+U ya bas")
        self.ui.btnAll.setToolTip("Ctrl+A ya bas")
        self.ui.btnDanger.setToolTip("Ctrl+D ye bas")
        self.ui.lndtSehir.setToolTip("Aramak için ENTER a bas")
        self.ui.lndtDeger.setToolTip("Aramak için ENTER a bas")

        #EditText Arama Bağlantılarımız
        self.ui.lndtSehir.returnPressed.connect(self.proccesCities)
        self.ui.lndtDeger.returnPressed.connect(self.proccesValues)
        self.ui.lndtDeger.setValidator(QIntValidator(0,20,self))

        #Butonlarımızın Bağlantıları
        self.ui.btnExt.clicked.connect(self.btnExtClickedSlot)
        self.ui.btnAll.clicked.connect(self.btnAllClickedSlot)
        self.ui.btnDanger.clicked.connect(self.btnDangerClickedSlot)
        self.ui.btnUpdate.clicked.connect(self.btnUpdateClickedSlot)


        #Combobox İşlemlerimizin Bağlantıları
        self.ui.comboSehir.addItems(["Seçiniz","ADANA","ADIYAMAN","AFYON","AGRI","AMASYA","ANKARA","ANTALYA",
        "ARTVIN","AYDIN","BALIKESIR","BILECIK","BINGOL","BITLIS","BOLU","BURDUR","BURSA","CANAKKALE","CANKIRI","CORUM",
         "DENIZLI","DIYARBAKIR","EDIRNE","ELAZIG","ERZINCAN","ERZURUM","ESKISEHIR","GAZIANTEP","GIRESUN","GUMUSHANE"
          "HAKKARI","HATAY","ISPARTA","MERSIN","ISTANBUL","IZMIR","KARS","KASTAMONU","KAYSERI","KIRKLARELI","KIRSEHIR",
           "KOCAELI","KONYA","KUTAHYA","MALATYA","MANISA","KAHRAMANMARAS","MARDIN","MUGLA","MUŞ","NEVSEHIR","NIGDE","ORDU"
             "RIZE","SAKARYA","SAMSUN","SIIRT","SINOP","SIVAS","TEKIRDAG","TOKAT","TRABZON","TUNCELI","SANLIURFA","USAK","VAN",
               "YOZGAT","ZONGULDAK","AKSARAY","BAYBURT","KARAMAN","KIRIKKALE","BATMAN","SIRNAK","BARTIN","ARDAHAN","IGDIR",
                 "YALOVA","KARABUK","KILIS","OSMANIYE","DUZCE"])
        self.ui.comboSehir.currentIndexChanged['QString'].connect(self.comboChanged)


    #Fonksiyonlarımızı Atıyoruz.

    def comboChanged(self, akımDegisim):
     if (akımDegisim!="Seçiniz"):
        print("Seçilen Şehir: ",akımDegisim)
        payloadComboCities = {}
        headersComboCities = {}
        responseComboCity = requests.request("GET",url="https://turkiyedepremapi.herokuapp.com/api?sehir=(" + akımDegisim + ")",
                                        headers=headersComboCities,
                                        data=payloadComboCities)
        resultComboCity = json.loads(responseComboCity.text)
        print(resultComboCity)

    def proccesCities(self):

        answer_signalCity = self.ui.lndtSehir.text()
        payloadCities = {}
        headersCities = {}
        responseCity = requests.request("GET",url="https://turkiyedepremapi.herokuapp.com/api?sehir=(" + answer_signalCity + ")",
                                        headers=headersCities,
                                        data=payloadCities)
        resultCity = json.loads(responseCity.text)
        print("İstenilen Şehir:  ",answer_signalCity)
        print(resultCity)
        # self.ui.txtBrowser.setText("İstenilen Şehir:"+ resultCity )


    def proccesValues(self):

        answer_signalValues = self.ui.lndtDeger.text()
        answer_signalValuesMax = str(answer_signalValues+".9")#Verilen değerde aralık oluşturdum. Örneğin 5-5.9
        payloadValues={}
        headersValues={}
        responseValues = requests.request("GET",
                                        url="https://turkiyedepremapi.herokuapp.com/api?min="+answer_signalValues+"&max="+answer_signalValuesMax,
                                        headers=headersValues,
                                        data=payloadValues)
        resultValues = json.loads(responseValues.text)
        print(answer_signalValues,"büyüklüğünde depremler:")
        print(resultValues)

    def btnExtClickedSlot(self):

        print("Çıkılıyor")
        quit()

    def btnAllClickedSlot(self):

        print("Bütün Depremler Gösteriliyor.")
        payloadAll={}
        headersAll={}
        responseAll =requests.request("GET",url="https://turkiyedepremapi.herokuapp.com/api",
                                        headers=headersAll,
                                        data=payloadAll)
        resultAll = json.loads(responseAll.text)
        print(resultAll)

    def btnDangerClickedSlot(self):

        print("Yıkıcı Boyuttaki Depremler Gösteriliyor....")
        payloadDanger={}
        headersDanger={}
        responseDanger =requests.request("GET",url="https://turkiyedepremapi.herokuapp.com/api?min=7.1&max=19.9",
                                        headers=headersDanger,
                                        data=payloadDanger)
        resultDanger = json.loads(responseDanger.text)
        print(resultDanger)



    def btnUpdateClickedSlot(self):
        depremler()
        print("Güncelleniyor")











uygulama = QApplication([])
penceremiz = depremler()
penceremiz.show()
uygulama.exec()
