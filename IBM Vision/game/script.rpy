label start:
    camera:
        perspective True
    # Background and transition
    scene bg academy_entrance with fade
    # Protagonist's inner monologue
    p "(This is it… Shirasagi Academy. One of the most prestigious AI research institutions in the country. But why was I chosen?)"
    
    $ apply_cool_effect()
    pause 0.4
    $ reset_camera_effect()
    p "What was that light?"
    p "I feel like I already have seen this before.."
    play music "audio/happy_sound.mp3"

    # Hinata enters (Excited energy)
    show hinata happy_closed with dissolve
    $ renpy.pause(0.3)
    show screen time_display
    
    window hide
    
    show hinata happy_talk:
        subpixel True 
        xpos 0.31642647530166024 zrotate 7.0 
        linear 1.47 xpos 0.71 zrotate -7.0 
    hinata "Whoa, check out that building over there! That's where they work on advanced AI models!"

    show hinata happy_closed

    window hide
    show hinata happy_talk:
        subpixel True 
        pos (0.71, 1.0) zrotate -7.0 zoom 1.0 
        linear 1.13 pos (0.52, 1.28) zrotate 0.0 zoom 1.66
    hinata "I heard students even train their own AI assistants!"

    show hinata happy_closed:
        pos (0.52, 1.28) zrotate 0.0 zoom 1.66

    # Protagonist's response menu
    window hide
    menu:
        
        "That sounds amazing. I can’t wait to start!":
            $ renpy.pause(0.1)
            show hinata happy_talk:
                subpixel True xpos 0.52 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                ypos 1.28 
                linear 0.27 ypos 1.25 
                linear 0.27 ypos 1.28
            hinata "Right?! This is going to be awesome!"

            with Pause(0.64)
            show hinata happy_closed:
                pos (0.52, 1.28) 
            window show


            show hinata happy_closed

        "I still don’t get why I was chosen for this school.":
            show hinata thinking_opened
            $ renpy.pause(0.1)
            hinata "Maybe you’re some kind of AI prodigy and you don’t even know it?"
            show hinata thinking_closed

        "As long as they don’t expect me to build a killer AI, I’m good.":
            show hinata happy_opened
            $ renpy.pause(0.1)
            hinata "Haha! Yeah, let’s keep the robots friendly."
            show hinata happy_closed  

    # Slight pause for immersion
    pause 0.2

    window hide
    show hinata happy_closed:
        subpixel True 
        xpos 0.52 
        ease_back 1.15 xpos 0.26 
    with Pause(1.25)
    show hinata happy_closed:
        xpos 0.26 

    show erika happy_closed at offscreenright
    show erika happy_talk:
        subpixel True 
        easein 1.13 pos (0.25, 1.28) zrotate 0.0 zoom 1.66
    with Pause(1.23)
    show erika happy_closed:
        xpos 0.25 ypos 1.28 zrotate 0.0 zoom 1.66
    window show


    # Erika's introduction
    show erika neutral_talk
    erika "Talking about AI? Now that’s a conversation I can get behind!"

    show erika thinking_talk
    erika "I mean, it’s all fun and games until the AI decides *it* knows best."
    show erika neutral_closed
    erika "Ever heard of an AI that rewrote its own rules because it thought humans were ‘inefficient’?"
    
    # Hinata rolls eyes playfully
    show hinata thinking_talk
    hinata "Oh boy, here we go with the conspiracy theories…"

    # Erika crosses arms, smirking
    show erika neutral_talk
    erika "I’m just saying, AI can evolve. The question is—who’s controlling who?"
    show erika neutral_closed

    window auto
    # Protagonist's reaction choice
    menu:
        "That actually sounds kind of scary...":
            show erika happy_talk
            $ renpy.pause(0.1)
            erika "It is, and that’s why we’re here. To *understand* it before it understands *us*."
            show erika happy_closed

        "That’s ridiculous. AI follows human programming.":
            show erika thinking_talk
            $ renpy.pause(0.1)
            erika "You sure? AI learns *from* humans, but what if it surpasses human thinking?"
            show erika thinking_closed

        "Eh, as long as my AI can do my homework, I don't care.":
            show erika happy_talk
            $ renpy.pause(0.1)
            window auto hide

            # Dynamically lean Erika forward and Hinata backward using their real positions
            $ character_lean("erika", "forward", 0.25, 1.28)  # Erika leans in
            $ character_lean("hinata", "backward", 0.25, 1.28)  # Hinata leans back

            erika "Now *that* is the real dream."
            
            $ renpy.pause(1.24)
            
            # Reset characters to neutral position
            $ reset_to_neutral_smooth("hinata", "left")
            $ reset_to_neutral_smooth("erika", "right")

            window auto show

    # Erika shrugs
    show erika neutral_talk
    erika "Good call. Let’s see what all the hype is about."
    show erika neutral_closed
    # Scene Transition - Moving into the academy

    window hide
    pause 1
    jump academy_courtyard


label academy_courtyard:
    play music "audio/courtyard_piano.mp3"

    # Scene Setup - Transition to Courtyard
    scene bg academy_courtyard with fade
    show hinata neutral_closed at left with dissolve
    show erika neutral_closed at right with dissolve

    # # Hinata starts the conversation
    $ zoom_character_face("erika", "right")
    
    show hinata neutral_talk 
    $ zoom_character_face("hinata", "left")
    #
    hinata "So, did you hear about Professor Hayashi? Apparently, he’s kind of a legend in AI research."
    show hinata neutral_closed

    show erika thinking_opened
    erika "Legend is putting it lightly. The guy supposedly worked on *top-secret AI projects* before coming here."
    
    # Protagonist's response menu
    menu:
        "Sounds like a genius. I hope I can learn from him.":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Yeah, imagine being taught by an actual legend!"
            show hinata happy_closed

        "Or he could just be another eccentric professor...":
            show hinata happy_talk
            $ renpy.pause(0.1)
            hinata "Haha, fair point! Guess we’ll find out soon enough."
            show hinata happy_closed

        "Wait, top-secret AI projects? That sounds suspicious.":
            show hinata thinking_talk
            $ renpy.pause(0.1)
            hinata "You think there's more to him than meets the eye?"
            show hinata thinking_closed

    # Erika looks around, then leans in
    show erika thinking_talk
    erika "And here’s the real juicy part—someone leaked the first week’s course materials online."
    
    # Protagonist reaction menu
    menu:
        "Leaked? That’s… weird. Who would do that?":
            show erika neutral_talk
            erika "Exactly! And it wasn’t just lecture slides. It included *research notes* too."
            show erika neutral_closed

        "Wait, what if Hayashi *wanted* that info leaked?":
            show erika thinking_opened
            $ renpy.pause(0.1)
            erika "Hmm… you think he’s testing us somehow?"
            show erika thinking_closed

        "If someone’s hacking into lecture files, this school isn’t as secure as I thought.":
            show erika neutral_talk
            erika "Right? We’re supposed to be an elite research academy, but this is sketchy."
            show erika neutral_closed
    
    show hinata worried_talk
    hinata "Have you heard about the rumour around Professor Hayashi?"
    show hinata worried_closed
    show erika worried_talk
    erika "Oh, you mean the one about his top-secret AI projects?"
    show erika worried_closed

    show hinata worried_talk
    hinata "He apparently kidnaps students who fail his tests and use their brains as neurons to train his AI models."
    show hinata worried_closed

    p "Haha, very funny, Hinata."
    show erika neutral_talk
    erika "I heard he’s a bit of a recluse, but that’s about it."
    show erika neutral_closed

    show hinata happy_talk
    hinata "Never trust rumours about professors. They’re always ten times cooler in real life."
    show hinata happy_closed

    # Dialogue transition back to setting
    show hinata happy_talk
    hinata "We should probably get to class before he decides to test us on day one."

    # Bell rings, transition to class
    play sound "audio/bell_ring.mp3"
    show hinata happy_opened
    hinata "Welp, guess we’re about to meet him ourselves. Let’s go!"
    show hinata happy_closed

    scene bg classroom_normal with fade



# Initialize friendship points at the start of the game
default hinata_friendship = 0
default erika_friendship = 0

label classroom_normal:
    show hinata neutral_closed at offscreenleft
    show erika neutral_closed at offscreenright
    show hinata neutral_closed at position_left_far
    show erika neutral_closed at position_right_far
    $ renpy.pause(0.1)
    play music "audio/classroom_theme.mp3"

    hinata "Yo, where are you sitting? I could use a solid study buddy."
    $ player_name = "Asya"
    # Erika reacts
    show erika neutral_talk
    erika "Tch. Don’t let him fool you. He just wants someone to carry him when he inevitably forgets his homework."
    show erika frustrated_closed
    # Hinata defends himself
    show hinata worried_talk
    hinata "Lies and slander! I’ll have you know I did my homework… at least once this month."
    show hinata worried_closed
    # Erika unimpressed
    show erika frustrated_talk
    erika "Exactly my point. C'mon, [player_name], sit with someone who actually does their work."
    show erika happy_closed
    menu:
        "Sit next to Hinata (Boosts Hinata Friendship)":
            $ hinata_friendship += 1
            call hinata_animation
            show hinata happy_talk
            hinata "Oh, nice! I was hoping to sit next to you."
            show hinata happy_closed

            show erika thinking_talk
            erika "Guess I'll have to find another partner then."
            show erika thinking_closed

        "Sit next to Erika (Boosts Erika Friendship)":
            $ erika_friendship += 1
            show erika happy_talk
            erika "Finally, someone with actual taste. Let’s do this!"
            show erika happy_closed

            show hinata worried_opened
            hinata "(Did I just get ditched? ...Oh well.)"
            show hinata worried_closed

        "Sit alone (Neutral Choice, No Boosts)":
            show hinata thinking_opened
            hinata "That’s fair, I guess."
            show hinata thinking_closed

            show erika thinking_opened
            erika "Hah, lone wolf strategy. Bold."
            show erika thinking_closed

    hide hinata with dissolve
    hide erika with dissolve
    scene bg classroom_normal with fade
    play sound "audio/door_slide.mp3"

    "The classroom door slides open with a mechanical hiss. The chatter among students fades as a tall figure strides in."
    extend "Professor Hayashi, dressed in his usual sleek attire, steps in with a confident air. His glasses reflect the classroom lights as he surveys the students with a small, knowing smile."
    
    # show top_mask at truecenter onlayer mask_layer:
    #     ypos 0.05
    # show bottom_mask at truecenter onlayer mask_layer:
    #     ypos 0.95
    # Move character smoothly

    show hayashi neutral_closed at offscreenright:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1269.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 1.0 
        linear 0.64 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1341.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 1.12 
    with Pause(0.74)
    show hayashi neutral_closed:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1341.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 1.12 

    # pause 1
    show hayashi neutral_talk with fade
    hayashi "I see some of you have chosen your partners wisely... and others, well, time will tell."
    show hayashi neutral_closed

    show hayashi serious_talk
    hayashi "Now, let’s get started."
    hide hayashi neutral_closed with dissolve

    scene expression Null() onlayer mask_layer


    scene bg class_board with fade
    show hayashi smile_closed at center
    
    hayashi """
    Welcome, everyone, to the academy—and to a journey of understanding AI. 
    
    """
    hide hayashi with dissolve
    show hayashi at offscreenleft
    show screen slide_screen
    $ set_title("Machine Learning: Expanding Human Potential in Uncertain Environments")
    $ set_paragraph1("\n- Speech Sentiment Analysis \n\n- Detecting emotions hidden in spoken language\n \n- Weather Predictions \n\n- Forecasting unpredictable storms")
    $ set_paragraph2("", True, "/images/arcs/01/first_image_class.png")
    
    hayashi """
    Let's clear something up right away: Machine Learning isn't about robots taking over our jobs or lives. 
    
    It's about extending human capability in uncertain environments—places where the human mind struggles due to overwhelming data, limited expertise, or ever-changing conditions.
    
    """
    hayashi "AI can control Mars rovers autonomously"
    extend ", interpret emotional nuances in speech,"
    extend " and accurately forecast weather despite constant unpredictability."
    $ side_image_only_mode = True
    hinata thoughtful "Controlling rovers on Mars... kinda makes AI feel pretty epic, right?"
    erika smirk "Yeah, but we still worry about letting AI drive our cars here."

    $ set_title("AI = Cheap Prediction")
    $ set_paragraph1("")
    $ set_paragraph2("")
    hayashi "AI isn't magic; it's essentially inexpensive prediction—dramatically reducing uncertainty in decision-making."

    erika surprised "Wait—AI isn't magic? Just cheap predictions?"
    hinata amused "That's way less cool."

    $ set_title("Prediction: The Key to Decision-Making")
    $ set_paragraph1("\n- Enhancing productivity (Machines, Automation)\n- Streamlining communication (Chatbots, Speech-to-text)")
    $ set_paragraph2("", True, "/images/arcs/01/first_image_class.png")

    # show text "Prediction is the key to decision-making under uncertainty.\n- Enhancing productivity (Machines, Automation)\n- Streamlining communication (Chatbots, Speech-to-text)\n- Informing strategic decisions (Stock Trading, Logistics)" at truecenter with dissolve
    hayashi "Every decision we make involves uncertainty. AI helps us minimize it, making our choices better informed and more effective."

    $ set_title("Core Approaches to Machine Learning")
    $ set_paragraph1("\n\n\n- Supervised Learning\n\n\n- Unsupervised Learning\n\n\n- Reinforcement Learning")
    $ set_paragraph2("", True, "/images/arcs/01/supervised_learning.png")
    # show text "Core Approaches to Machine Learning\n- Supervised Learning\n- Unsupervised Learning\n- Reinforcement Learning" at truecenter with dissolve
    hayashi "There are three core ways we teach AI to predict. Let's examine each closely."

    erika smirk "I bet supervised learning is when the AI gets spoon-fed data."
    hinata grin "Sounds easy enough."

    $ set_paragraph1("Supervised Learning – AI learns from labeled examples\nPros: Efficient, requires fewer data points\nCons: Costly and time-consuming data labeling")
    hayashi "Exactly, supervised learning uses labeled data—think of it as structured teaching, like learning from flashcards."

    erika smug "Ha! Told you. Flashcards for AI."
    
    
    $ set_title("")
    $ set_paragraph1("")
    $ set_paragraph2("", False)
    

    "What.. was that again?.."
    "Am I hallucinating?.."
    $ set_title("Core Approaches to Machine Learning")
    $ set_paragraph1("Supervised Learning – AI learns from labeled examples\nPros: Efficient, requires fewer data points\nCons: Costly and time-consuming data labeling")
    $ set_paragraph2("", True, "/images/arcs/01/supervised_learning.png")
    
    hinata "Seems structured at least, not totally spoon-fed."
    $ set_paragraph1("Unsupervised Learning – AI finds patterns independently\nPros: No manual labeling required\nCons: Needs massive data, potentially ambiguous")
    hayashi "Unsupervised learning doesn't use labels. Instead, AI discovers hidden patterns on its own—like solving a puzzle without the reference image."

    hinata thoughtful "Sounds like solving a puzzle without the box picture."
    erika "Or a detective without clues."

    $ set_paragraph2("", True, "/images/arcs/01/reinforcement_learning.png")
    $ set_paragraph1("Reinforcement Learning – AI learns through trial and error\nPros: Dynamically adaptive, excellent for complex scenarios\nCons: Requires many trials; unpredictable outcomes")
    hayashi "Reinforcement learning teaches AI through experience, trial and error—much like how we learn to ride a bike or play a sport."

    erika curious "This is like teaching AI to ride a bike."
    hinata amused "Or training a dog that learns to pilot drones instead of fetching sticks."

    hayashi neutral_talk "Now, let's test your intuition."

    $ set_title("Quiz Time!")
    
    $ set_paragraph1("You have labeled photos of six cars. You want AI to distinguish each type. What's your learning approach?")
    $ set_paragraph2("")

    hayashi neutral_talk "Let’s test your intuition."

    hayashi "You have labeled photos of six cars. You want AI to distinguish each type. What's your learning approach?"

    hinata confident "Supervised Learning!"

    $ set_paragraph1("You have hundreds of unlabeled car photos. You want AI to group similar cars. Which approach?")

    erika thoughtful "That's Unsupervised Learning, right?"

    hayashi smile_closed "Correct. Good job."
    $ side_image_only_mode = False

    $ set_title("")
    $ set_paragraph1("")
    $ set_paragraph2("")
    show hayashi happy_talk at right
    hayashi "Today you've glimpsed machine learning—its potential, its approaches. Next time, we'll see these concepts applied in healthcare, transportation, even education. Remember, the power of prediction isn't in knowing the future—it's in preparing for it."

    $ apply_cool_effect("academy_entrance")
    pause 0.4
    $ reset_camera_effect()

    p "Hinata, did you see that?"
    hinata "What are you talking about? I'm trying to focus here."
    p "I think I need to get some rest."
    hide hayashi with fade
    scene bg classroom_normal with fade



    return

label hinata_animation:
    window hide

    show bg classroom_normal:
        subpixel True 
        blur 0.0 
        linear 0.72 blur 7.07 

    show hinata neutral_closed:
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 1.2 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.72 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-63.0, 423.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 2.24 additive 0.0 blur 7.18 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    show erika neutral_closed:
        subpixel True xzoom 1.0 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.72 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    with Pause(0.82)

    show bg classroom_normal:
        blur 7.07 

    show hinata neutral_closed:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-63.0, 423.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 2.24 additive 0.0 blur 7.18 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

    show erika neutral_closed:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

    window show
    return
