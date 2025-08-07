import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

API_KEY = "F3nO8TPZkOVu9wZECHBauco7kWJoi0iov4p9EU8h"
URL = "https://api.nasa.gov/planetary/apod"

def fetch_and_display():
    date = date_entry.get().strip()
    if not date:
        messagebox.showerror("Error", "Please enter a date (YYYY-MM-DD).")
        return

    status_label.config(text="Fetching image...")
    root.update_idletasks()

    params = {
        "api_key": API_KEY,
        "date": date 
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        status_label.config(text="")
        messagebox.showerror("Error", f"Failed to fetch data: {e}")
        return

    image_url = data.get("url", "")
    if not image_url or not image_url.endswith((".jpg", ".png", ".jpeg")):
        status_label.config(text="")
        messagebox.showinfo("Not an image", "No image found for the provided date.")
        return

    try:
        image_data = requests.get(image_url).content
        image = Image.open(BytesIO(image_data))
        image = image.resize((400, 400))
        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo  

        status_label.config(text=f"Image for {date} loaded successfully.")
    except Exception as e:
        status_label.config(text="")
        messagebox.showerror("Error", f"Failed to load image: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("NASA APOD Viewer")

tk.Label(root, text="NASA Astronomy Picture of the Day", font=("Helvetica", 16)).pack(pady=10)

tk.Label(root, text="Enter date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root, width=25)
date_entry.pack(pady=5)

tk.Button(root, text="Fetch Image", command=fetch_and_display).pack(pady=10)

status_label = tk.Label(root, text="", fg="white")
status_label.pack()

image_label = tk.Label(root)
image_label.pack(pady=10)


root.mainloop()