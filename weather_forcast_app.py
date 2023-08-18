import requests
from bs4 import BeautifulSoup
from tkinter import Label
from tkinter import Tk
from PIL import ImageTk, Image

url = "https://weather.com/en-IN/weather/today/l/d2127eb893261f5c537714fdcc4bf073db5ad330d0c26ed760f72eb6490b1b5d"

master = Tk()
master.title("Weather App")
master.config(bg="white")

img = Image.open("C:\\Users\hp\OneDrive\Desktop\weather.png.png")
img = img.resize((150,150))
img = ImageTk.PhotoImage(img)

def getWeather():
    page = requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    location = soup.find('h1',class_="CurrentConditions--location--1YWj_").text
    temperature = soup.find('span',class_="CurrentConditions--tempValue--MHmYY").text
    weatherPrediction = soup.find('div',class_="CurrentConditions--phraseValue--mZC_p").text
    
    locationLabel.config(text=location)
    TempretureLabel.config(text=temperature)
    weatherPredictionLabel.config(text=weatherPrediction)
    
    TempretureLabel.after(6000,getWeather)
    master.update()

locationLabel = Label(master,font=("Calibri bold",20),bg="white")
locationLabel.grid(row=0,sticky="N",padx =100)
TempretureLabel = Label(master,font=("Calibri bold",70),bg="white")
TempretureLabel.grid(row=1,sticky="W",padx =40)
Label(master,image=img,bg="white").grid(row=1,sticky="E")
weatherPredictionLabel = Label(master,font=("Calibri bold",15),bg="white")
weatherPredictionLabel.grid(row=2,sticky="W",padx=40)
getWeather()
master.mainloop()