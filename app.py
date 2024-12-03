from logic_and_flow_control.game import GameWindow


def start_adventure():
    GameWindow.update(
        image_name="door.png",
        message="You come to a wall with two doors. Do you want go through door A or door B?",
        option_a="Door A",
        option_b="Door B",
        next_function=door_a_or_b,
    )


def door_a_or_b(choice):
    if choice == "a":
        GameWindow.update(
            image_name="bridge.png",
            message="You see a bridge over a river, there is a troll on the bridge. Do you take the bridge or try to swim across?",
            option_a="Bridge",
            option_b="Swim",
            next_function=bridge_choice,
        )
    else:
        GameWindow.update(
            image_name="ring.png",
            message="A spider guards the ring of power but there is a sword. Do you take the ring and run or take the sword and fight the spider?",
            option_a="Ring",
            option_b="Fight",
            next_function=bridge_choice,
        )


def bridge_choice(choice):
    if choice == "a":
        GameWindow.end(
            image_name="bridge.png",
            message="The troll kills you, bad luck. Try again...",
            restart_function=start_adventure,
        )
    else:
        GameWindow.end(
            image_name="bridge.png",
            message="You drown, oh dear. Try again...",
            restart_function=start_adventure,
        )


GameWindow.initialize()

start_adventure()

GameWindow.mainloop()
