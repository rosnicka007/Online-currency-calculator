from tkinter import *
import requests
import time

# Barvy
main_bg_color = "#ffb277"
main_fg_color = "#170a00"

# Okno
window = Tk()
window.minsize(350, 200)
window.title("Přepočet měn")
window.resizable(False, False)
#window.iconbitmap("mesec.ico")
window.config(bg= main_bg_color)

# Funkce
def count():
    try:

        currency_from = drop_down_from.get()
        currency_to = drop_down_to.get()
        amount = int(user_input.get())
        
        #print(type(amount))
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"

        payload = {}
        headers= {"apikey": "pWSAeZ3nt46TedepbU5ReFjIDwMDvHaT"}

        response = requests.request("GET", url, headers=headers, data = payload)

        response.raise_for_status
        data_result = response.json()
        #result_label.config(text= round(data_result["result"], 2))
        result_label.config(text = str(round(data_result["result"],2)).replace(".", ","))
        current_rate_label.config(text= str(round(data_result["info"]["rate"],2)).replace (".", ","))
        print(data_result)
        notification_label.config(text="")
    
    except:
        notification_label.config(text="Zadejte prosím částku")

# Uživatelský vstup
user_input = Entry(width=10, font=("Arial", 12), justify=CENTER)
user_input.focus()
user_input.grid(row=0, column=0, padx=10, pady=(10, 0))

# Roletka - z jaké měny
drop_down_from = StringVar(window)
drop_down_from.set("CZK") # výchozí hodnota
drop_down_from_option = OptionMenu(window, drop_down_from, "AUD", "CHF", "CZK", "EUR", "GBP","USD")
drop_down_from_option.grid(row=0, column=1, padx=10, pady =(10, 0))

# Roletka - na jakou měnu
drop_down_to = StringVar(window)
drop_down_to.set("CZK")
drop_down_to_option = OptionMenu (window, drop_down_to, "AUD", "CHF", "CZK", "EUR", "GBP","USD" )
drop_down_to_option.grid(row=1, column=1, padx=10, pady=(10, 0))

# Tlačítko přepočtu
count_button = Button(text="Přepočítat", font=("Arial", 12), command=count)
count_button.grid(row=0, column=2, padx=10, pady=(10, 0))

# Label - výsledek převodu
result_label = Label (text="0", bg=main_bg_color, fg=main_fg_color, font =("Arial", 12, "bold"), )
#result_label = str(result_label).replace(".", ",")

result_label.grid(row=1, column=0, pady=(10,0))

# Label - upozornění
notification_label = Label (bg=main_bg_color, fg=main_fg_color, font=("Arial", 12))
notification_label.grid(row=2, column=0)

# Label - kurz
rate_label = Label (text="Aktuální kurz:", bg=main_bg_color,  fg=main_fg_color, font=("Arial", 12))

rate_label.grid(row=3, column=0, sticky="w", padx = 10)

# Label - aktuální kurz
current_rate_label = Label (bg=main_bg_color, fg=main_fg_color, font=("Arial", 12))

current_rate_label.grid(row=3, column=1, sticky="w", padx=12)

# Label - datum
date_label = Label (bg=main_bg_color, text="Datum: ", fg=main_fg_color, font=("Arial", 12), )
date_label.grid(row=4, column=0, sticky="w", padx = 10)

# Datum
local= time.localtime()


# Label - datum transakce
date_of_transaction_label = Label (text= "{}. {}. {}".format(local[2], local[1], local[0]), bg=main_bg_color,  fg=main_fg_color, font=("Arial", 12))
date_of_transaction_label.grid(row=4, column=1, sticky="w", padx=12)

# Hlavní cyklus
window.mainloop()