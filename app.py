from logic_and_flow_control.game import GameWindow


def start_adventure():
    GameWindow.update(
        image_name="door.png",
        message="You come to a wall with two doors. You go through door A or door B?",
        option_a="Door A",
        option_b="Door B",
        next_function=door_a_or_b,
    )


def door_a_or_b(choice):
    if choice == "a":
        GameWindow.update(
            image_name="question.png",
            message="Description of scene. Description of choice?",
            option_a="Description of option a",
            option_b="Description of option b",
            next_function=door_a_or_b,
        )
    else:
        GameWindow.update(
            image_name="question.png",
            message="Description of scene. Description of choice?",
            option_a="Description of option a",
            option_b="Description of option b",
            next_function=door_a_or_b,
        )


GameWindow.initialize()

start_adventure()

GameWindow.mainloop()
