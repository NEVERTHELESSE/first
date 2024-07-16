from customtkinter import *


app = CTk()
app.geometry('600x500')
app.title('Login')
app.resizable(False,False)


bg =  CTkScrollableFrame(master=app, fg_color='darkblue',width=600, height=500).pack(anchor='center',padx=0.5, pady=0.5)



# contain =  CTkCanvas(master=bg,bg='orange', width=350, height=470).place(relx='0.42', rely='0.55',anchor='w')
# CTkLabel(master=app, font=('Arial bold',30, 'bold'),text='Welcome Back' ).place(relx='0.48', rely='0.27',anchor='w')
# CTkLabel(master=app, font=('Arial bold',30, 'bold'),text='Welcome Back' ).place(relx='0.48', rely='0.27',anchor='w')

# CTkLabel(master=contain, font=('Arial',18),bg_color='white',text='Signin to your account' ).place(relx='0.48', rely='0.34',anchor='w')

# CTkLabel(master=contain, font=('Arial',18),bg_color='white',text='Email' ).place(relx='0.48', rely='0.36',anchor='w')
# CTkEntry(master=contain, corner_radius=2, border_color='blue').place(relx= 0.48, rely=0.4)



app.mainloop()