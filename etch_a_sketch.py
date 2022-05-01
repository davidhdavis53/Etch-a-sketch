# This little snippet works like a simple etch-a-sketch from years past.
# Use the w, s, a, d keys to draw a continous line up, down, left, and right.
# Tap the q key to quit.

# Import keyboard so we can interrogate the keypress.
# This doesn't work on android and probably
# not on an iPhone since it would require root access on those platforms.
# You might try getch on those.
import keyboard         # don't forget to use 'pip install keyboard'

# Import our friendly turtle to assist our drawing.
import turtle

# variables and settings global:
# upkey = define key used for up
# downkey = define key used for down
# leftkey = define key used for left
# rightkey = define key used for right
# quitkey = define key used to quit the game
upkey = "w"
downkey = "s"
leftkey = "a"
rightkey = "d"
quitkey = "q"


# this function is just a placeholder to keep my if .. else structure readable
def no_operation():
    return


# used for debugging
def debug_code(a):
    print("current direction" + " " + a)
    return


def etch_a_sketch(up, down, left, right, quit):

    # variable and settings local:
    # key = store the keypress
    # flag = set flag to loop endlessly
    # stylus.turtle = my turtle
    # current_direction = set our variable to the default direction turtle
    #                     starts at
    # how_far = set length to number of pixels to move forward position on
    #           each keypress
    key = ""
    flag = 0
    stylus = turtle.Turtle()
    current_direction = "right"
    stylus.showturtle
    how_far = 10

    while flag == 0:
        key = keyboard.read_key()

        if key == up:
            if (current_direction == "right"):
                stylus.left(90)
            elif (current_direction == "left"):
                stylus.right(90)
            elif (current_direction == "up"):
                no_operation()
            else:
                stylus.right(-180)
            current_direction = "up"
            stylus.forward(how_far)
        elif key == down:
            if (current_direction == "right"):
                stylus.right(90)
            elif (current_direction == "left"):
                stylus.left(90)
            elif (current_direction == "up"):
                stylus.right(-180)
            else:
                no_operation()
            current_direction = "down"
            stylus.forward(how_far)
        elif key == left:
            if (current_direction == "right"):
                stylus.right(-180)
            elif (current_direction == "left"):
                no_operation()
            elif (current_direction == "up"):
                stylus.left(90)
            else:
                stylus.right(90)
            current_direction = "left"
            stylus.forward(how_far)
        else:
            if key == right:
                if (current_direction == "right"):
                    no_operation()
                elif (current_direction == "left"):
                    stylus.right(-180)
                elif (current_direction == "up"):
                    stylus.right(90)
                else:
                    stylus.left(90)
                current_direction = "right"
                stylus.forward(how_far)

        # debug_code(current_direction)

        if key == quit:
            flag = 1
            break


# call the function
etch_a_sketch(upkey, downkey, leftkey, rightkey, quitkey)
