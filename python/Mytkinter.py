from customtkinter import *
# from PIL import Image

app=CTk()
app.geometry('500x400')
def click_handler():
  print('am click')

def entry_get():
  print(f'enter value : {entry.get()}')
  
def chagne_handle(value):
  print(f'selected value {value}')
textbox = CTkTextbox(master=app, scrollbar_button_color='orange',corner_radius=16, border_color='green',border_width=2)
slider = CTkSlider(master=app, from_=0, to=100, number_of_steps=5, button_color='red',progress_color='green')
switch = CTkSwitch(master=app, text='option')
entry = CTkEntry(master=app, placeholder_text='Start typing...', width=300, text_color='green')
btn = CTkButton(master=app,text='click me',  command=entry_get)
# img = Image.open('qrcode.png')
checkbox = CTkCheckBox(master=app, text='Option',fg_color='orange',checkbox_height=30,checkbox_width=30, corner_radius=36)
combobox = CTkComboBox(master=app,values=['ajibola','neverthelesse','confident'],fg_color='orange',border_color='purple',dropdown_fg_color='green',command=chagne_handle)
btn.pack(anchor='n',expand=True)
entry.place(relx=0.5, rely=0.5, anchor='center')
label = CTkLabel(master=app, text='this is the label', width=190, height=28, fg_color='transparent')
label.place(x=10, y=10)
# btn = CTkButton(master=app, text='neverthelesse', corner_radius=32, fg_color='orange',hover_color='purple',border_color='green',border_width=2)
# btn.place(relx=0.5, rely=0.5, anchor='center')
app.mainloop()


