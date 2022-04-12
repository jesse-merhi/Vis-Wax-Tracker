# VIS WAX TRACKER V1.0
# Improvements for 1.1:
# - Aesthetic.
# - Allow for different first and second runes
# - Second (3) rune selection. 
# - Attempts
# - Optimization
# - Third Rune Alphabetical
# - 

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
from time import sleep
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk,Image 
from functools import partial
window = tk.Tk()
window.geometry("750x500")
window.resizable(False, False)
title = """
-----WELCOME TO THE VIS WAX TRACKER-----
--------------VERSION:1.0---------------
--------CODED AND MAINTAINED BY:--------
-------------JESSE MERHI----------------
"""
def search_vis():
    URL = "https://runescape.wiki/w/Vis_wax"
    page = requests.get(URL)
    quantity = visentry.get()
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all('span', {"class":"infobox-quantity-replace"})
    price = int(str(prices[0]).replace('<span class="infobox-quantity-replace">',"").replace("</span>","").replace(",",""))
    total_rune_price = int(price * int(quantity))
    currency ="{:,}gp".format(total_rune_price) 

    pricing_string = f"Vis wax x{quantity} = {currency}"
    
    vis_pricing_frame = tk.Frame(screen_frame)
    vis_pricing_frame.grid(row = 3, column = 1)

    

    total_price = 0
    choice = v.get()
    total_price = runes_pricing[0] + runes_pricing[int(choice)+1 ]
    third_rune_deets = search_rune("<<ComboboxSelected>>")
    total_price += third_rune_deets["price"]
    total_profit = total_rune_price - total_price
    total_price = "{:,}gp".format(total_price)
    total_profit = "{:,}gp".format(total_profit)
    first_rune_currency = "{:,}gp".format(runes_pricing[0])
    first_rune_price = tk.Label(vis_pricing_frame, text = f"First Rune: {given_runes[0]} x{runes[given_runes[0]]} = {first_rune_currency}")
    first_rune_price.grid(column = 1, row = 1)

    chosen_rune_currency = "{:,}gp".format(runes_pricing[int(choice)+1])
    chosen_rune_price = tk.Label(vis_pricing_frame, text = f"Chosen Rune: {given_runes[int(choice)+1 ]} x{runes[given_runes[int(choice)+1 ]]} = {chosen_rune_currency}")
    chosen_rune_price.grid(column = 1, row = 2)

    third_rune_currency = "{:,}gp".format(third_rune_deets["price"])
    third_rune_name = third_rune_deets["name"]
    third_rune_amount  =third_rune_deets["amount"]
    third_rune_price = tk.Label(vis_pricing_frame, text = f"Third Rune: {third_rune_name} x{third_rune_amount} = {third_rune_currency}")
    third_rune_price.grid(column = 1, row = 3)

    vis_pricing = tk.Label(vis_pricing_frame, text = pricing_string, width = 20)
    vis_pricing.grid(column = 1, row = 4)

    total_cost_runes = tk.Label(vis_pricing_frame, text = f"Total Cost of Runes: {total_price}", width = 25)
    total_cost_runes.grid(column = 1, row = 5)


    total_cost_runes = tk.Label(vis_pricing_frame, text = f"Total Profit: {total_profit}", width = 25)
    total_cost_runes.grid(column = 1, row = 6)
def validate(user_input): 
    # check if the input is numeric
    if  user_input.isdigit(): 
        # Fetching minimum and maximum value of the spinbox 
        minval = int(0) 
        maxval = int(101) 
  
        # check if the number is within the range 
        if int(user_input) not in range(minval, maxval): 
            return False
  
        # Printing the user input to the console 
        return True
  
    # if input is blank string 
    elif user_input == "": 
        return True 
    else: 
        return False

    
def search_rune(event):
    third_rune = combo_box.get()
    choice = v.get()
    print(choice)
    print("images/"+third_rune+".png")
    third_rune_image_frame = tk.Frame(screen_frame)
    third_rune_image_frame.grid( row = 3)
    image = Image.open("images/"+third_rune+".png")
    image = image.resize((100, 100), Image.ANTIALIAS)
    ThirdRuneImage = ImageTk.PhotoImage(image)
    third_rune_label = tk.Label(third_rune_image_frame, image = ThirdRuneImage)
    third_rune_label.image = ThirdRuneImage
    third_rune_label.pack(pady = 20)



    URL = "https://runescape.wiki/w/"+third_rune
    page = requests.get(URL)
    quantity = runes[third_rune]
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all('span', {"class":"infobox-quantity-replace"})
    price = int(str(prices[0]).replace('<span class="infobox-quantity-replace">',"").replace("</span>",""))
    total_rune_price = int(price * quantity)
    currency ="{:,}gp".format(total_rune_price) 

    pricing_string = f"Third rune: {third_rune} x{quantity} = {currency}"

    third_rune_pricing_frame = tk.Frame(screen_frame)
    third_rune_pricing_frame.grid( row = 4)
    for widget in third_rune_pricing_frame.winfo_children():
        print(widget)
    third_rune_pricing = tk.Label(third_rune_pricing_frame, text = pricing_string, width = 32)
    third_rune_pricing.pack()
    return {
        "name": third_rune,
        "price": total_rune_price,
        "amount": quantity
    }

runeslist = [
    "Air_Rune",
    "Mind_Rune",
    "Water_Rune",
    "Earth_Rune",
    "Fire_Rune",
    "Body_Rune",
    "Cosmic_Rune",
    "Chaos_Rune",
    "Nature_Rune",
    "Law_Rune",
    "Death_Rune",
    "Dust_Rune",
    "Smoke_Rune",
    "Mist_Rune",
    "Lava_Rune",
    "Steam_Rune",
    "Blood_Rune",
    "Soul_Rune",
    "Astral_Rune",
    "Mud_Rune",
]

screen_frame = tk.Frame(master = window)
first_rune_frame = tk.Frame(master = screen_frame, width = 350)
second_rune_frame = tk.Frame(master = screen_frame,width = 350)
screen_frame.pack(side = tk.TOP)


first_rune_frame.grid( column = 1,row = 0)
second_rune_frame.grid( column = 1, row  = 1)

print(title)

titleimg = ImageTk.PhotoImage(Image.open("images/Vis Tracker.png"))
titlelabel = tk.Label(screen_frame, image = titleimg)
titlelabel.grid(column = 0, row = 0)

URL = "https://warbandtracker.com/goldberg/"
print("\n\n")
print("TALKING TO WIZARD TOWER WIZARDS...")

page = requests.get(URL)
print("TRANSLATING ANCIENT LANGUAGE...")
soup = BeautifulSoup(page.content, 'html.parser')
print("FETCHING RUNE DATA...")
print("\n\n")
results = soup.find_all('b')

runes = {
    "Air_Rune":  1000,
    "Mind_Rune": 2000,
    "Water_Rune": 1000,
    "Earth_Rune": 1000,
    "Fire_Rune": 1000,
    "Body_Rune": 2000,
    "Cosmic_Rune": 400,
    "Chaos_Rune": 500,
    "Nature_Rune": 350,
    "Law_Rune": 300,
    "Death_Rune": 400,
    "Dust_Rune": 500,
    "Smoke_Rune": 500,
    "Mist_Rune": 500,
    "Lava_Rune": 500,
    "Steam_Rune": 500,
    "Blood_Rune": 350,
    "Soul_Rune": 300,
    "Astral_Rune": 300,
    "Mud_Rune": 300,
}


total = 0
i = 1
v = tk.StringVar(window, "1")
given_runes = []
runes_pricing = []
for x in results[0:3]:
    rune = (str(x).replace("<b>","").replace("</b>","").replace(" ","_"))
    URL = "https://runescape.wiki/w/"+rune
    page = requests.get(URL)
    quantity = runes[rune]
    soup = BeautifulSoup(page.content, 'html.parser')
    prices = soup.find_all('span', {"class":"infobox-quantity-replace"})
    price = int(str(prices[0]).replace('<span class="infobox-quantity-replace">',"").replace("</span>",""))
    total_rune_price = int(price * quantity)
    currency ="{:,}gp".format(total_rune_price) 
    if( i == 1):
        string = "First Rune"
        given_runes.append(rune)
        print(f"{string}: {rune} x{quantity} = {currency}")
        greeting = tk.Label(text = f"{string}: {rune} x{quantity} = {currency}", master = first_rune_frame, width = 40)
        img1 = ImageTk.PhotoImage(Image.open("images/"+rune+".png"))
        panel1 = tk.Label(first_rune_frame, image = img1)
        panel1.grid(row = 0, column = 0)
        greeting.grid(row = 0, column = 1)
        runes_pricing.append(total_rune_price)

    elif(i == 2):
        string = "Second Rune (1)"
        given_runes.append(rune)
        print(f"{string}: {rune} x{quantity} = {currency}")
        greeting = tk.Label(text = f"{string}: {rune} x{quantity} = {currency}", master = first_rune_frame, width = 40)
        img2 = ImageTk.PhotoImage(Image.open("images/"+rune+".png"))
        panel2 = tk.Label(first_rune_frame, image = img2)
        panel2.grid(row = 1, column = 0)
        panel3 = tk.Radiobutton(first_rune_frame, variable = v, value = "0", command = lambda: search_rune("<<ComboboxSelected>>"))
        panel3.grid(row = 1, column = 2)
        greeting.grid(row = 1, column = 1)
        runes_pricing.append(total_rune_price)

    else:   
        string = "Second Rune (2)"
        given_runes.append(rune)

        print(f"{string}: {rune} x{quantity} = {currency}")
        greeting = tk.Label(text = f"{string}: {rune} x{quantity} = {currency}", master = first_rune_frame, width = 40)
        img3 = ImageTk.PhotoImage(Image.open("images/"+rune+".png"))
        panel4 = tk.Label(first_rune_frame, image = img3)
        panel4.grid(row = 3, column = 0)
        panel5 = tk.Radiobutton(first_rune_frame, variable = v, value = "1", command = lambda: search_rune("<<ComboboxSelected>>"))
        panel5.grid(row = 3, column = 2)
        greeting.grid(row = 3, column = 1)
        runes_pricing.append(total_rune_price)
    print(runes_pricing)
    
    if(i == 2):
        greet = tk.Label(text = "OR", master = first_rune_frame)
        greet.grid(row = 2, column = 1)
    i+=1

third_rune_frame = tk.Frame(master = screen_frame, bg = "blue")
third_rune_frame.grid(column = 0,  row = 2)
third_rune = tk.Label(master = third_rune_frame ,text = "Third rune: ")

variable = tk.StringVar(screen_frame)

combo_box = ttk.Combobox(third_rune_frame,width = 27, textvariable = variable, values = runeslist, state = "readonly")
third_rune.grid(column = 0, row = 0)
combo_box.grid(column = 1, row = 0 )

combo_box.set("Air_Rune")
search_rune("<<ComboboxSelected>>")
combo_box.bind("<<ComboboxSelected>>",search_rune)

panel3.bind("<<RadiobuttonSelected>>", search_rune)

final_frame = tk.Frame(screen_frame)
final_frame.grid(column = 1, row = 2)

vis_frame = tk.Frame(final_frame)
vis_frame.grid(row = 0)
vislabel = tk.Label(vis_frame, text = "Number of Viswax: ")
vislabel.grid(column = 0, row = 0)

visentry = tk.Spinbox(vis_frame,from_=0, to = 100)
visentry.grid(column = 1, row = 0)
range_validation = final_frame.register(validate)
visentry.config(validate = "key", validatecommand = (range_validation, '%P'))

castspell = tk.Button(vis_frame, text = "Cast Spell!", height = 1, command = search_vis)
castspell.grid(column = 2, row = 0)
window.mainloop()

