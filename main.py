import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas = tk.Canvas(root, width=280, height=280, bg="black")
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.start_paint)
        self.canvas.bind("<B1-Motion>", self.paint)

        self.button_save = tk.Button(root, text="Guardar", command=self.save_image)
        self.button_save.pack()

        self.button_clear = tk.Button(root, text="Borrar", command=self.clear_canvas)
        self.button_clear.pack()

        self.image = Image.new("RGB", (280, 280), "black")
        self.draw = ImageDraw.Draw(self.image)

    def start_paint(self, event):
        self.old_x = event.x
        self.old_y = event.y

    def paint(self, event):
        x, y = event.x, event.y
        self.canvas.create_line((self.old_x, self.old_y, x, y), fill="white", width=5, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.draw.line((self.old_x, self.old_y, x, y), fill="white", width=10)
        self.old_x = x
        self.old_y = y

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            self.image.save(file_path)
            print("Imagen creada correctamente")
            self.root.quit()  # Cerrar la ventana principal

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (280, 280), "black")
        self.draw = ImageDraw.Draw(self.image)

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()