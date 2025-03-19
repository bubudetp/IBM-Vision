# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.





label arc1:
    $ player_name = renpy.input("Type your name:")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Burak"
    
    scene bg_research_lab with fade

    show mc neutral
    "You step into the IBM AI Research Hub, a sleek, high-tech facility filled with glowing monitors and algorithmic data streams."

    show mc neutral
    mc "Welcome to IBM’s AI Research Hub [player_name]."

    mc "You are here because you have shwon an aptitude for data-driven reasoning."

    mc "Before we begin, tell me-what do you think machine learning is?"

    menu: 
        "A way for computers to learn from data.":
            show mc happy1
            mc "That's correct. Unlike traditional programming, machine learning extracts patterns from rather than following strict rules."
        
        "A program that thinks like a human.":
            show mc eyebrowraise
            mc "A common misconception. AI does not think-it predicts outcomes based on past data."

        "Just another fancy algorithm.":
            show mc areyousure
            mc "Not quite. Machine learning models evolve as they process more data."
        
    
    show mc neutral
    mc "Let's move on to something more practical."

    scene bg_laboratory_meeting with fade


    show mc neutral
    mc "Machine learning is useful in certain situations. Let’s test your understanding."

    default answered = {
        "mars": False,
        "gps": False,
        "stocks": False,
        "thermostat": False,
        "chatbot": False
    }

    "Monroe presents five scenarios. Do you think ML applies in each case?"
    while not all(answered.values()):
        menu:
            "A Mars rover navigates autonomously on unknown terrain." if not answered["mars"]:
                show mc happy1
                mc "Correct. ML is useful when human expertise is absent."
                $ answered["mars"] = True

            "A GPS follows a fixed shortest path to a destination." if not answered["gps"]:
                show mc areyousure
                mc "No. That’s just a pre-programmed system, not learning."
                $ answered["gps"] = True

            "A stock market AI adjusts to economic crashes in real time." if not answered["stocks"]:
                show mc sad1
                mc "Yes, because conditions change dynamically."
                $ answered["stocks"] = True

            "A thermostat adjusts temperature based on user input." if not answered["thermostat"]:
                show mc areyousure
                mc "No, that’s simple automation, not machine learning."
                $ answered["thermostat"] = True

            "A chatbot detects emotional tones in customer messages." if not answered["chatbot"]:
                show mc happy1
                mc "Exactly. It learns from data to improve interactions."
                $ answered["chatbot"] = True

            "Go deterministic Zone":
                $ Location = "deterministic"
            "Open map":
                $ renpy.with_statement(fade)
                $ Location = renpy.call_screen("MapScreen", _layer="screens")
            "test":
                jump arc2


    show mc neutral
    mc "Good. Now, let’s talk about the different types of machine learning."

    
    return
