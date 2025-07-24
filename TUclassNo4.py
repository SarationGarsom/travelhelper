import requests
import tkinter as tk
Firstinput="767438ad237c8f1dd99241f4"
#Firstinput=input("https://www.exchangerate-api.com/のアカウントで取得したキーを入力")
ratesAPI=True
if ratesAPI==True:
    rates = requests.get("https://v6.exchangerate-api.com/v6/{}/latest/USD".format(Firstinput)).json()
    if rates["result"]=="error":
        ratesAPImode=0
    else:
        ratesAPImode=1
else:
    ratesAPImode=-1
if ratesAPImode==1:
    #print('1 USD =', rates['rates']['JPY'], 'JPY')
    print(rates)
    Tokyo= requests.get('http://worldtimeapi.org/api/timezone/America/New_York').json()
    #print(Tokyo['datetime'])
    #print(Tokyo)
    MainWin=tk.Tk()
    MainWin.geometry("460x620")
    MainWin.resizable(width=False,height=False)
    LabelM2=tk.Label(MainWin,text="未完成です",font=("",45))
    LabelM=tk.Label(MainWin,text='1 USD ='+str(rates['conversion_rates']['JPY'])+'JPY'+str(Tokyo['datetime']),font=("",45))
    LabelM2.pack(side=tk.TOP)
    LabelM.pack(side=tk.TOP)
    MainWin.mainloop()