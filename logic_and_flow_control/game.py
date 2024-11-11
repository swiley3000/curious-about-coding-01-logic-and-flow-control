import tkinter as tk
from PIL import Image, ImageTk
from os.path import join, exists


class GameWindow:

    instance = None

    @classmethod
    def initialize(cls):
        if not cls.instance:
            cls.instance = cls()

    @classmethod
    def update(
        cls,
        image_name,
        message,
        option_a,
        option_b,
        next_function,
    ):

        if not cls.instance:
            raise ValueError("GameWindow not initialized")

        cls.instance._update(
            image_name=image_name,
            message=message,
            option_a=option_a,
            option_b=option_b,
            next_function=next_function,
        )

    @classmethod
    def end(
        cls,
        image_name,
        message,
        restart_function,
    ):

        if not cls.instance:
            raise ValueError("GameWindow not initialized")

        cls.instance._end(
            image_name=image_name,
            message=message,
            restart_function=restart_function,
        )

    @classmethod
    def mainloop(cls):
        if not cls.instance:
            raise ValueError("GameWindow not initialized")

        cls.instance._mainloop()

    def _handle_choice(self, choice, next_func):
        if choice == "a":
            next_func("a")
        elif choice == "b":
            next_func("b")
        else:
            raise ValueError(f"Invalid choice: {choice}")

    def __init__(self):

        self._root = tk.Tk()
        self._root.title("Choose Your Own Adventure")
        self._root.geometry("400x480")

        self._image_label = tk.Label(self._root)
        self._image_label.pack(pady=10)

        self._message_label = tk.Label(
            self._root,
            text="",
            wraplength=300,
            justify="center",
        )

        self._message_label.pack(pady=10)

        self._button_a = tk.Button(
            self._root,
            text="Option A",
            width=40,
        )
        self._button_a.pack(pady=5)

        self._button_b = tk.Button(
            self._root,
            text="Option B",
            width=40,
        )
        self._button_b.pack(pady=5)

    def _update(
        self,
        image_name,
        message,
        option_a,
        option_b,
        next_function,
    ):

        image_path = join(
            "images",
            image_name,
        )

        if exists(image_path):
            img = Image.open(image_path)
            img_tk = ImageTk.PhotoImage(img)
            self._image_label.config(image=img_tk)
            self._image_label.image = img_tk
        else:
            self._image_label.config(
                image="",
                text=f"Image not found: {image_path}",
                font=("Arial", 16),
            )

        self._message_label.config(text=message)

        if option_a and option_b:
            self._button_a.config(
                text=f"a) {option_a}",
                command=lambda: self._handle_choice(
                    "a",
                    next_function,
                ),
            )
            self._button_b.config(
                text=f"b) {option_b}",
                command=lambda: self._handle_choice(
                    "b",
                    next_function,
                ),
            )
            self._button_a.pack(pady=5)
            self._button_b.pack(pady=5)
        else:
            self._button_b.pack_forget()
            self._button_a.config(
                text="End Game",
                command=next_function,
            )
            self._button_a.pack(pady=5)

    def _end(self, image_name, message, restart_function):

        self._update(
            image_name=image_name,
            message=message,
            option_a="",
            option_b="",
            next_function=None,
        )

        self._button_b.pack_forget()

        self._button_a.config(
            text="Start again",
            command=restart_function,
        )

        self._button_a.pack(pady=5)

    def _mainloop(self):
        self._root.mainloop()
