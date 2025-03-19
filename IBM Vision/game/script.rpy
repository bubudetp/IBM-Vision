label start:

    # Background and transition
    scene bg academy_entrance with fade
    play music "audio/school_theme.mp3"

    p "(This is it… Shirasagi Academy. One of the most prestigious AI research institutions in the country. But why was I chosen?)"

    # Hinata enters
    show hinata happy_closed with dissolve
    $ renpy.pause(0.1)  # Slight delay before speaking

    # Text appears letter by letter
    hinata "Whoa, check out that building over there! That’s where they work on advanced AI models! I heard students even train their own AI assistants!"

    show hinata happy_closed

    menu:
        "That sounds amazing. I can’t wait to start!":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Right?! This is going to be awesome!"
            show hinata happy_closed  # Stop animation

        "I still don’t get why I was chosen for this school.":
            show hinata thinking_talk
            $ renpy.pause(0.1)
            hinata "Maybe you’re some kind of AI prodigy and you don’t even know it?"
            show hinata thinking_closed  # Stop animation

        "As long as they don’t expect me to build a killer AI, I’m good.":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Haha! Yeah, let’s keep the robots friendly."
            show hinata happy_closed  # Stop animation

    # Scene Transition
    scene bg academy_courtyard with fade

label academy_courtyard:
    play music "audio/courtyard_piano.mp3"
    
    show hinata neutral_talk with dissolve
    $ renpy.pause(0.1)

    hinata "So, did you hear about Professor Hayashi? Apparently, he’s kind of a legend in AI research. Some say he used to work on top-secret AI projects!"
    show hinata neutral_closed

    menu:
        "Sounds like a genius. I hope I can learn from him.":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Yeah, imagine being taught by an actual legend!"
            show hinata happy_closed

        "Or he could just be another eccentric professor...":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Haha, fair point!"
            show hinata happy_closed

        "Wait, top-secret AI projects? That sounds suspicious.":
            show hinata thinking_talk
            $ renpy.pause(0.1)
            hinata "You think there's more to him than meets the eye?"
            show hinata thinking_closed

    scene bg classroom_normal with dissolve

label classroom_normal:
    show hayashi smile_talk with dissolve
    $ renpy.pause(0.1)
    play music "audio/classroom_theme.mp3"

    hayashi "Ah, fresh young minds! Welcome to your first step into the world of artificial intelligence!"
    show hayashi smile

    # Flash white transition
    scene bg classroom_holo_mode with flash
    play sound "audio/glitch_effect.mp3"

    show hayashi thinking_talk
    $ renpy.pause(0.1)
    hayashi "Machine learning is categorized into three main approaches: Supervised Learning, Unsupervised Learning, and Reinforcement Learning."
    show hayashi thinking

    menu:
        "Supervised Learning":
            show hayashi happy_talk
            $ renpy.pause(0.1)
            hayashi "Correct! In this method, AI learns from labeled data."
            show hayashi happy

        "Unsupervised Learning":
            show hayashi smile_talk
            $ renpy.pause(0.1)
            hayashi "Not quite. This approach lets AI find patterns without labels."
            show hayashi smile

        "Reinforcement Learning":
            show erika smirk_talk
            $ renpy.pause(0.1)
            erika "Haha! That's for teaching an AI through rewards and penalties."
            show erika smirk

    # Glitch effect
    scene bg digital_glitch with vpunch
    play sound "audio/error_sound.mp3"

    "SYSTEM ERROR: ANOMALY DETECTED"

    show hinata worried_talk with shake
    $ renpy.pause(0.1)
    hinata "Uh… what was that?!"
    show hinata worried

    show kaito neutral_talk with dissolve
    $ renpy.pause(0.1)
    kaito "It’s just a display bug. Nothing to panic about."
    show kaito neutral

    show erika smirk_talk with dissolve
    $ renpy.pause(0.1)
    erika "Or maybe the AI is trying to tell us something?"
    show erika smirk

    menu:
        "It’s just a glitch. No big deal.":
            show kaito neutral_talk
            $ renpy.pause(0.1)
            kaito "Exactly."
            show kaito neutral

        "That didn’t look like a normal bug…":
            show erika amused
            $ renpy.pause(0.1)
            erika "Exactly! You're thinking outside the box."

        "Maybe this is part of the lesson?":
            show hayashi thinking_talk
            $ renpy.pause(0.1)
            hayashi "Hmm… interesting perspective."
            show hayashi thinking

    scene bg classroom_normal with fade
    scene bg hallway with slideleft
    play music "audio/mysterious_theme.mp3"

    "As you walk through the hallway, your tablet buzzes. A new message appears from an UNKNOWN SENDER."

    "UNKNOWN: 'You saw it too, didn’t you? The anomaly is real. Find the pattern, and you’ll find the truth.'"

    menu:
        "Who is this? What do you know?":
            "No response."

        "I don’t have time for this.":
            "The message disappears, but curiosity lingers."

        "I need to investigate this further.":
            "You’ve begun uncovering the truth…"

    scene black with slow_fade
    return
