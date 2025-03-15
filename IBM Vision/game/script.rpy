# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

label start:
    scene bg room
    show eileen happy
    a "You've created a new Ren'Py game."
    a "Once you add a story, pictures, and music, you can release it to the world!"
    a "Good luck!"
    a "Good luck!"

    jump prologue
    return