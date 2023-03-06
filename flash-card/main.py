from tkinter import Tk, Canvas, PhotoImage, Button
from colors import BACKGROUND_COLOR

window = Tk()
window.title("Flash card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage("card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Text should be here", font=("Ariel", 40, "italic"), fill='black')
canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"), fill='black')
canvas.grid(row=0, column=0, columnspan=2)

cross_button_image = PhotoImage("wrong.png")
cross_button = Button(image=cross_button_image, highlightthickness=0)
cross_button.grid(row=1, column=0)

tick_button_image = PhotoImage(file="right.png", format="PNG")
tick_button = Button(image=tick_button_image, highlightthickness=0)
tick_button.grid(row=1, column=1)

window.mainloop()








