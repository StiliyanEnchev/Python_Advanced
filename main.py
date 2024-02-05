import tkinter as tk
import json
import requests
import urllib.request

from io import BytesIO
from PIL import ImageTk, Image


def display_image(image_url: str) -> None:
    with urllib.request.urlopen(image_url) as url:
        image_data = url.read()

    image_stream = BytesIO(image_data)

    image =  ImageTk.PhotoImage(Image.open(image_stream))

    image_label.config(image=image)
    image_label.image = image

def get_image_url():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQyYWUyOWItMDI0Mi00YmQxLTk2NDYtMGJiODAyNjZjNzVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.CfTZShcLwobgND8S55NIGDh5kiZ3zZiKhB7JmVpx3hw"}

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "providers": "openai",
        "text": input_field.get(),
        "resolution": "300x300",
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    print(result['openai']['items'][0]['image_resource_url'])

def render_image():
    print('clicked')
    image_url = get_image_url()
    display_image(image_url)

window = tk.Tk()
window.title('AI Image Generator')
window.geometry('500x500')

input_field = tk.Entry(window, width=14)
input_field.place(x=200, y=200)

image_label = tk.Label(window)
image_label.place(x=125, y=70)

generate_button = tk.Button(window, text='Create', height=1, command=render_image)
generate_button.place(x=220, y=225)

window.mainloop()
