# Импортируем все из библиотеки TKinter
from tkinter import *


class ClassMenu(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.master.title("Простое меню")

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu1 = Menu(menubar)
        fileMenu1.add_command(label="Выход", command=self.onExit)
        menubar.add_cascade(label="Файл", menu=fileMenu1)
        fileMenu2 = Menu(menubar)
        menubar.add_cascade(label="Параметры конструкции", menu=fileMenu2)
        fileMenu2.add_command(label="Ввод параметров", command=self.opendata)
        fileMenu2 = Menu(menubar)
        menubar.add_cascade(label="Параметры нагрузок", menu=fileMenu2)
        fileMenu2.add_command(label="Ввод параметров", command=self.opendata1)

    def onExit(self):
        self.quit()

    def opendata(self):
        def write_File(text_File, name_file):
            file = open(name_file, "a")
            # The object text_File is a tkinter.Entry object, so we will get
            #   the user input by calling the get method on that object.
            user_Input = text_File.get(1.0, 10.20)
            # user_Input = (''.join(user_Input)).split()
            # Here we now directly write the user input to the file that has been
            #   opened, I'm not sure you were previously doing with writing the
            #   string version of the file, but this appears to achieve what you
            #   desire.
            file.write(user_Input)
            file.close()

        dataframe = Tk()
        dataframe['bg'] = '#fafafa'
        dataframe.title('ConstructionParameters')
        dataframe.geometry('300x900')
        dataframe.resizable(width=True, height=True)

        # dataframe.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], weight=1, minsize=75)
        # dataframe.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], weight=1, minsize=50)

        NRtext = Label(dataframe, text='NR=', bg='white', font=40)
        NRtext.grid(row=0, column=0, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        # NRField = Entry(dataframe, bg='white', font=30, width=3)
        # NRField.grid(row=0, column=1, padx=5, pady=10, ipadx=2, ipady=2)

        NStext = Label(dataframe, text='NS=', bg='white', font=40)
        NStext.grid(row=0, column=1, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        # NSField = Entry(dataframe, bg='white', font=30, width=3)
        # NSField.grid(row=0, column=3, padx=5, pady=10, ipadx=2, ipady=2)

        NCtext = Label(dataframe, text='NC=', bg='white', font=40)
        NCtext.grid(row=0, column=2, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        # NCField = Entry(dataframe, bg='white', font=30, width=3)
        # NCField.grid(row=0, column=5, padx=5, pady=10, ipadx=2, ipady=2)

        NMtext = Label(dataframe, text='NM=', bg='white', font=40)
        NMtext.grid(row=0, column=3, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        # NMField = Entry(dataframe, bg='white', font=30, width=3)
        # NMField.grid(row=0, column=7, padx=5, pady=10, ipadx=2, ipady=2)

        NRNC = Text(dataframe, height=1, width=24, bg='gray90')
        NRNC.grid(row=1, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(NRNC, "Construction/NR NS NC NM.txt"))
        btn.grid(row=1, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")
        # btn.bind('<Button-1>', write_File(NRField))

        XRtext = Label(dataframe, text='XR(NR,1:2)', bg='white', font=40)
        XRtext.grid(row=2, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        XYtext = Label(dataframe, text='X Y=', bg='white', font=40)
        XYtext.grid(row=3, column=0, padx=5, pady=10, ipadx=2, ipady=2)

        XYListText = Text(dataframe, height=3, width=24, bg='gray90')
        XYListText.grid(row=4, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(XYListText, "Construction/XYList.txt"))
        btn.grid(row=4, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        XStext = Label(dataframe, text='XS(NS,1:3)', bg='white', font=40)
        XStext.grid(row=8, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        IJIgtext = Label(dataframe, text='I J Ig=', bg='white', font=40)
        IJIgtext.grid(row=9, column=0, padx=5, pady=10, ipadx=2, ipady=2)

        IJIgListText = Text(dataframe, height=3, width=24, bg='gray90')
        IJIgListText.grid(row=10, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(IJIgListText, "Construction/IJIgList.txt"))
        btn.grid(row=10, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        XCtext = Label(dataframe, text='XC(NC,0:9)', bg='white', font=40)
        XCtext.grid(row=13, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        ERotext = Label(dataframe, text='E Ro At A Iz y- y+ [Sp] [Sc]=', bg='white', font=40)
        ERotext.grid(row=14, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        ERoListText = Text(dataframe, height=3, width=24, bg='gray90')
        ERoListText.grid(row=15, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(ERoListText, "Construction/E_Ro_At.txt"))
        btn.grid(row=15, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        XMtext = Label(dataframe, text='XM(NM,0:2)', bg='white', font=40)
        XMtext.grid(row=18, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        PMImtext = Label(dataframe, text='P M Im=', bg='white', font=40)
        PMImtext.grid(row=19, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2, sticky="w")

        PMImListText = Text(dataframe, height=3, width=24, bg='gray90')
        PMImListText.grid(row=20, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(ERoListText, "Construction/P_M_Im.txt"))
        btn.grid(row=20, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        dataframe.mainloop()

    def opendata1(self):
        def write_File(text_File, name_file):
            file = open(name_file, "a")
            # The object text_File is a tkinter.Entry object, so we will get
            #   the user input by calling the get method on that object.
            user_Input = text_File.get(1.0, 10.20)
            # user_Input = (''.join(user_Input)).split()
            # Here we now directly write the user input to the file that has been
            #   opened, I'm not sure you were previously doing with writing the
            #   string version of the file, but this appears to achieve what you
            #   desire.
            file.write(user_Input)
            file.close()

        dataframe = Tk()
        dataframe['bg'] = '#fafafa'
        dataframe.title('PowersParameters')
        dataframe.geometry('300x900')
        dataframe.resizable(width=True, height=True)

        # dataframe.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30], weight=1, minsize=75)
        # dataframe.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], weight=1, minsize=50)

        NAtext = Label(dataframe, text='NA=  NQR=  NQS=  NT=', bg='white', font=40)
        NAtext.grid(row=0, column=0, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        # NRField = Entry(dataframe, bg='white', font=30, width=3)
        # NRField.grid(row=0, column=1, padx=5, pady=10, ipadx=2, ipady=2)

        """NQRtext = Label(dataframe, text='NQR=', bg='white', font=40)
        NQRtext.grid(row=0, column=1, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")


        NQStext = Label(dataframe, text='NQS=', bg='white', font=40)
        NQStext.grid(row=0, column=2, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")


        NTtext = Label(dataframe, text='NT=', bg='white', font=40)
        NTtext.grid(row=0, column=3, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")"""

        NANQR = Text(dataframe, height=1, width=24, bg='gray90')
        NANQR.grid(row=1, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(NANQR, "Powers/NA NQR NQS NT.txt"))
        btn.grid(row=1, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        NBtext = Label(dataframe, text='NB(NA,0:3)', bg='white', font=40)
        NBtext.grid(row=2, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        IKKKtext = Label(dataframe, text='I K1 K2 K3=', bg='white', font=40)
        IKKKtext.grid(row=3, column=0, padx=5, pady=10, ipadx=2, ipady=2)

        IKKKListText = Text(dataframe, height=3, width=24, bg='gray90')
        IKKKListText.grid(row=4, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(IKKKListText, "Powers/IKKKList.txt"))
        btn.grid(row=4, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        QRtext = Label(dataframe, text='QR(NQR,0:3)', bg='white', font=40)
        QRtext.grid(row=8, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        IFFMtext = Label(dataframe, text='I F1 F2 M=', bg='white', font=40)
        IFFMtext.grid(row=9, column=0, padx=5, pady=10, ipadx=2, ipady=2)

        IFFMListText = Text(dataframe, height=3, width=24, bg='gray90')
        IFFMListText.grid(row=10, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(IFFMListText, "Powers/IFFMList.txt"))
        btn.grid(row=10, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        QStext = Label(dataframe, text='QS(NQC,0:3)', bg='white', font=40)
        QStext.grid(row=13, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        PxyTtext = Label(dataframe, text='P qx qy T=', bg='white', font=40)
        PxyTtext.grid(row=14, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        PxyTListText = Text(dataframe, height=3, width=24, bg='gray90')
        PxyTListText.grid(row=15, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(PxyTListText, "Powers/PxyT.txt"))
        btn.grid(row=15, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        FTtext = Label(dataframe, text='FT(NT,0:1)', bg='white', font=40)
        FTtext.grid(row=18, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2)

        tFtext = Label(dataframe, text='t F(t)=', bg='white', font=40)
        tFtext.grid(row=19, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=2, sticky="w")

        tFListText = Text(dataframe, height=3, width=24, bg='gray90')
        tFListText.grid(row=20, column=0, padx=5, pady=10, ipadx=2, ipady=2, columnspan=4)

        btn = Button(dataframe, text='Save', command=lambda: write_File(tFListText, "Powers/tF.txt"))
        btn.grid(row=20, column=4, padx=5, pady=10, ipadx=2, ipady=2, sticky="w")

        dataframe.mainloop()


def main():
    def CheckCorrect(filename):
        Result = True

        file1 = open(filename, "r")
        if not file1:
            Result = False
            print(Result)
            # print(filename)
            return (Result)

        while True:

            line = file1.readline()
            for i in line:
                if not (str(i) in "0123456789" or str(i) == chr(32) or str(i) == '\n'):
                    Result = False
                    print(filename)
            if not line:
                if Result == False:
                    # print(filename)
                    return (Result)
                    break
                return (Result)
                break

    mainframe = Tk()
    mainframe['bg'] = '#fafafa'
    mainframe.title('Препроцессор')
    mainframe.geometry('900x600')
    mainframe.resizable(width=True, height=True)

    Menu = ClassMenu()
    CheckCorrect("Construction/E_Ro_At.txt")
    CheckCorrect("Construction/IJIgList.txt")
    CheckCorrect("Construction/NR NS NC NM.txt")
    CheckCorrect("Construction/P_M_Im.txt")
    CheckCorrect("Construction/XYList.txt")
    CheckCorrect("Powers/tF.txt")
    CheckCorrect("Powers/PxyT.txt")
    CheckCorrect("Powers/NA NQR NQS NT.txt")
    CheckCorrect("Powers/IKKKList.txt")
    CheckCorrect("Powers/IFFMList.txt")
    # MenuPowers = ClassPowers()
    # self.Scrollbar(mainframe)
    # self.Scrollbar.pack(side="right", fill="y")

    # scroll_x = Scrollbar(orient=HORIZONTAL)
    # scroll_y = Scrollbar(orient=VERTICAL)
    # canvas = Canvas(width=300, height=100,
    # xscrollcommand=scroll_x.set,
    # yscrollcommand=scroll_y.set)
    # self.scroll_x.config(command=self.canvas.xview)
    # self.scroll_y.config(command=self.canvas.yview)

    # Эта функция срабатывает при нажатии на кнопку "Посмотреть погоду"
    """def get_weather():
        # Получаем данные от пользователя
        city = cityField.get()

        # данные о погоде будем брать с сайта openweathermap.org
        # ниже пропишите свой API ключ, который получите в кабинете пользователя на сайте openweathermap.org
        key = 'ВАШ КЛЮЧ'
        # ссылка, с которой мы получим все данные в формате JSON
        url = 'http://api.openweathermap.org/data/2.5/weather'
        # Дополнительные парамтеры (Ключ, город введенный пользователем и единицины измерения - metric означает Цельсий)
        params = {'APPID': key, 'q': city, 'units': 'metric'}
        # Отправляем запрос по определенному URL
        result = requests.get(url, params=params)
        # Получаем JSON ответ по этому URL
        weather = result.json()

        # Полученные данные добавляем в текстовую надпись для отображения пользователю
        info['text'] = f'{str(weather["name"])}: {weather["main"]["temp"]}'
"""

    """# Настройки главного окна



    # Создаем фрейм (область для размещения других объектов)
    # Указываем к какому окну он принадлежит, какой у него фон и какая обводка
    frame_geometry = Frame(mainframe, bg='white', bd=5)
    # Также указываем его расположение
    frame_geometry.place(relx=0.4, rely=0, relwidth=0.6, relheight=1)

    # Все то-же самое, но для второго фрейм
    frame_data = Frame(mainframe, bg='gray', bd=5)
    frame_data.place(relx=0, rely=0, relwidth=0.4, relheight=1)

    # Создаем текстовое поле для получения данных от пользователя    NR
    NRField = Entry(frame_data, bg='white', font=30, width=3)
    NRField.pack()  # Размещение этого объекта, всегда нужно прописывать
    NRField.place(x=0, y=25)
    # Создаем текстовую надпись, в которую будет выводиться информация о погоде
    NRtext = Label(frame_data, text='NR', bg='gray', font=40)
    NRtext.pack()
    NRtext.place(x=0, y=0)

    NSField = Entry(frame_data, bg='green', font=30)
    NSField.pack()
    NCField = Entry(frame_data, bg='blue', font=30)
    NCField.pack()
    # Создаем кнопку и при нажатии будет срабатывать метод "get_weather"
    btn = Button(frame_geometry, text='Посмотреть погоду')
    btn.pack()



    # Запускаем постоянный цикл, чтобы программа работала"""
    mainframe.mainloop()


if __name__ == '__main__':
    main()
