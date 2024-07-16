from customtkinter import *
app = CTk()
app.geometry('1400x1000')
app.resizable(False,False)
# app._set_appearance_mode('light')
set_default_color_theme('blue')
frame = CTkFrame(master=app,width=300, height=800, fg_color='orange')
frame.pack(anchor='w', padx=20, pady=20)

label = CTkLabel(master=frame, text_color='#fff',text='Dashboard',font=('arial',34, 'bold'), bg_color='purple',corner_radius=50).place(relx='0.5', rely='0.2',anchor='center')

smallfram = CTkFrame(master=frame, width=270, height=50, fg_color='#fff').place(relx='0.5', rely='0.3',anchor='center')

label = CTkLabel(master=app, text='Order',font=('arial',34,'bold'),text_color='#fff').place(relx = 0.4, rely =0.1, anchor='center')

label = CTkLabel(master=app, text='View order ->',font=('arial',34,'bold'),text_color='#fff', bg_color='orange').place(relx = 0.8, rely =0.1, anchor='w')

frame = CTkFrame(master=app,width=280, height=100, fg_color='orange')
frame.place(anchor='center',  rely=0.2, relx = 0.34)
frame = CTkFrame(master=app,width=280, height=100, fg_color='orange')
frame.place(anchor='center',  rely=0.2, relx = 0.55)
frame = CTkFrame(master=app,width=280, height=100, fg_color='orange')
frame.place(anchor='center',  rely=0.2, relx = 0.76)
# frame.pack(anchor='center', padx=80, pady=0.1)



app.mainloop()
