from dotenv import load_dotenv
import requests
import os
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
load_dotenv()

PINK = "#7027A0"
GREEN = "#6ECB63"

STATES_LIST = ['Andaman Nicobar islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chattisgarh','Delhi','Dadra & Nagar','Goa','Gujrat','Himachal Pradesh','Haryana','Jharkhand','Jammu & Kashmir','Karnataka','Kerla','Ladakh','Lakshadweep Islands','Mahrashtra','Meghalya','Manipur','Madhya Pradesh','Mizoram','Nagaland','Odisha','Punjab','Pondicherry','Rajasthan','Sikkim','Telangana','Tamil nadu','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']
WEBSITE_URL = f"{os.getenv('API_URL')}"

STATES_LIST = [f"{states}\n".lower() for states in STATES_LIST]

def submit_state():
    entered_state = entry_field.get().lower()
    index_in_states_list = STATES_LIST.index(f"{entered_state}\n")
    state_data = covid_data_states[index_in_states_list]
    messagebox.showinfo(title=f"{entered_state.title()}",
                        message=f"Confirmed {state_data['confirmed']}\n"
                        f"Deceased {state_data['deceased']}\n"
                        f"Recovered {state_data['recovered']}")
    entry_field.delete(0,END)
    entry_field.focus()
    LABELS = ['Deceased','Recovered']
    MY_EXPLODE = [0.02,0]
    DATA = [state_data['deceased'],state_data['recovered']] 
    plt.title(f"Stats for {entered_state.title()}")
    plt.pie(DATA,labels=LABELS,explode=MY_EXPLODE,colors=["b","#4CAF50"])
    plt.show()


def show_states():
    messagebox.showinfo("List of States","".join(STATES_LIST).title())


data = requests.get(url=WEBSITE_URL).json()

# for states in data: this gives us the number of statistics for each state
#     pprint(data[states]['total'])

name_list = [state_name for state_name in data if state_name!="TT"]

data_list = [data[states]['total'] for states in data if states!="TT"] 
# getting the data in the list of the namesk

covid_data_states = [];

for covid_data in data_list:
    ele_dict = {
        "confirmed":covid_data['confirmed'],
        "deceased":covid_data['deceased'],
        "recovered":covid_data['recovered']
    }
    covid_data_states.append(ele_dict)


# Making the UI
window = Tk()
window.title("Covid 19 Statistics App")
window.config(padx=100,pady=50,height=900,width=900,bg=GREEN)
title_label = Label(text="Covid 19 Stats",font=("Courier",25,"bold"),bg=GREEN,fg=PINK)
title_label.grid(column=1,row=0)
canvas = Canvas(width=500,height=500,highlightthickness=0,bg=GREEN)
covid_image =  PhotoImage(file="covid.png")
covid_canvas = canvas.create_image(250,250,image = covid_image)
canvas.grid(column=1,row=1)
show_list_button = Button(text="States",
    highlightthickness=0,
    bg=GREEN,
    command=show_states,
    pady=7)
show_list_button.grid(column=0,row=2)
enter_a_state_label = Label(text="Enter A State",
            fg=PINK,
            font=("Courier",10,"bold"),
            bg=GREEN,)
enter_a_state_label.grid(column=1,row=2)
entry_field = Entry()
entry_field.focus()
entry_field.grid(column=1,row=3)
submit_button = Button(text="Submit",highlightthickness=0,bg=GREEN,command=submit_state)
submit_button.grid(column=2,row=2)
window.mainloop()