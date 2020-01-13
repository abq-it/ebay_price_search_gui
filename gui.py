#!/usr/bin/python

import Tkinter as tk
import ttk
import sys
import requests
from lxml import html

def search_item(item_url):
    total = 0
    num_phones = 0
    mean = 0
    bn2 = []
    r = requests.get(item_url)
    tree = html.fromstring(r.content)
    phone_prices = []
    phone_prices = tree.xpath("//span[@class='POSITIVE']/text()")
    #print(phone_prices) # Prints array of unpared phone prices.
    for x in phone_prices:
        y = x.replace('$', '')
        temp = y.split('.')
        y = temp[0]
        if (len(y) > 3):
            y = y.replace(',', '')
        int_y = int(y)
        bn2.append(int_y)
        num_phones += 1

    for i in bn2:
        try:
            total += i
        except:
            print("Total integer too large at index: " + i)
    try:
        mean = total / num_phones
    except:
        print "Mean could not be calculated."

    # Print to used number of phones used to arrive at the mean.
    print("Total number of items averaged: " + str(num_phones))
    print("Mean: " + str(mean))
    output_msg = "Average selling price: $" + str(mean) + "\nNumber of items recently sold: " + str(num_phones)
    return output_msg

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("RESULTS")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="CLOSE", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def find_entry():
    user_input = e1.get()
    if user_input == " ":
        print "failed"
    else:
        print(user_input)
        result = search_item(user_input)
        popupmsg(result)

def clear_text():
    e1.delete(0, 'end')

master = tk.Tk()
tk.Label(master, text="eBay url (Sold Items)").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master,
          text='Quit',
          command=master.quit).grid(row=3,
                                    column=1,
                                    sticky=tk.W,
                                    pady=4)
var = tk.IntVar()
button = tk.Button(master,
          text='Show', command=find_entry).grid(row=3,
                                                       column=2,
                                                       sticky=tk.W,
                                                       pady=4)
clear_button = tk.Button(master,
          text="Clear text", command=clear_text).grid(row=3,
                                                            column=3,
                                                            sticky=tk.W,
                                                            pady=4)
#button.wait_variable(var)
master.geometry("500x200")
master.mainloop()
