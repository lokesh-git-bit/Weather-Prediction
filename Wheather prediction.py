import tkinter as tk
from tkinter import Label
import requests as req
import json

def clear():
    label1.delete(0,'end')
def submit():
    header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
    url='https://api.weatherapi.com/v1/current.json?key=701cdf6feb704b5dab860250212008&q='
    y='&aqi=no'
    citynm=city.get()
    url=url+citynm+y
    res=req.get(url,headers=header)
    data=json.loads(res.text)
    temp=data['current']['temp_c']
    wpredict=data['current']['condition']['text']
    disp1_1=tk.Label(window, text="Today's temprature of",bg='PaleTurquoise1').place(x=100,y=260)
    disp1_2=tk.Label(window, text=citynm).place(x=250,y=260)
    disp1_3=tk.Label(window, text=" is: ",bg='PaleTurquoise1').place(x=310,y=260)
    disp1_4=tk.Label(window, text=temp).place(x=350,y=260)
    disp2_1=tk.Label(window, text="Weather prediction: ",bg='PaleTurquoise1').place(x=110,y=280)
    disp2_2=tk.Label(window, text=wpredict,).place(x=240,y=280)

    if temp>25:
        disp3=tk.Label(window, text="Production is POSSIBLE in today's weather").place(x=100,y=300)
        
    else:
        disp3=tk.Label(window, text="Production is NOT POSSIBLE in today's weather").place(x=100,y=300)
       

window=tk.Tk()
window.geometry('700x500')
window.title("Weather Report")
window.configure(bg='PaleTurquoise1')

label=tk.Label(window, text="Welcome to Weather Check!", font=('Cooper Black',30,'bold'),bg='PaleTurquoise1')
label.pack(pady=50)
label=tk.Label(window, text="City name:",bg='PaleTurquoise1',font=('Algerian',10,'bold'))
label.place(x=250,y=150)

city=tk.StringVar()

label1=tk.Entry(window, textvariable=city)
label1.place(x=350,y=150)
clr_btn=tk.Button(window, text='   clear   ',width=10,height=2,command=clear).place(x=300,y=195)
clr_btn=tk.Button(window, text='submit',width=10,height=2,command=submit).place(x=400,y=195)

window.mainloop()
