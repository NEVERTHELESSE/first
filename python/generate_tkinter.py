import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    data = entry.get()
    if not data:
        messagebox.showwarning("I nput Error", "Please enter the data to encode")
        return
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")

    img_path = "qrcode.png"
    img.save(img_path)
    
    # Display the QR code
    img = Image.open(img_path)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create and place widgets
tk.Label(root, text="Enter data to encode:").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)
generate_btn = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_btn.pack(pady=20)
qr_label = tk.Label(root)
