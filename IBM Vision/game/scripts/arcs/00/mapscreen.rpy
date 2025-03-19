screen MapScreen():
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1080
        background "backgrounds/probabilistic.png"

        # Deterministic Zone Button
        textbutton "Deterministic Zone":
            xpos 1000
            ypos 500
            xsize 300
            ysize 100
            action [Hide("MapScreen"), With(fade), Return("Deterministic")]
            style "map_button"

        # Probabilistic Zone Button
        textbutton "Probabilistic Zone":
            xpos 600
            ypos 500
            xsize 300
            ysize 100
            action [Hide("MapScreen"), With(fade), Return("Probabilistic")]
            style "map_button"

        # Reinforcement Learning Zone Button
        textbutton "Reinforcement Learning Zone":
            xpos 1300
            ypos 700
            xsize 350
            ysize 100
            action [Hide("MapScreen"), With(fade), Return("Reinforcement")]
            style "map_button"

# Define Button Style
style map_button is default:
    background "#222222"
    color "#FFFFFF"
    font "DejaVuSans.ttf"
    hover_background "#444444"
    xpadding 20
    ypadding 10


screen OverworldScreen():
    tag menu  # Ensures only one screen at a time
    frame:
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 600
        background "black"

        add PythonDisplayable(game.run)  # Calls the game loop
