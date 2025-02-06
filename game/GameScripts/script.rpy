    #splashscreen

label splashscreen:
    scene black 
    show text "By Studio Mueller" with dissolve
    with Pause(2)
    hide text with dissolve
    return



label sounds:

    ##me when sounds go bbrrrrrrrr this is the defined sounds one is the typewriter one is one sound
    define sounds = ['audio/typewriter/B1.ogg', 'audio/typewriter/B2.ogg', 'audio/typewriter/B3.ogg', 'audio/typewriter/B4.ogg', 'audio/typewriter/B5.ogg']


init python:

    def callback(event, **kwargs):
        if event == "show":
            renpy.music.play(renpy.random.choice(sounds), channel="text", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="text")


label defined:

    #All the characters defined
    define pov = Character("[povname]", callback=callback)
    define Thunder = Character("Thunder", callback=callback)
    define puppy = Character("Thunder", callback=callback)
    define flirty = Character("Thunder", callback=callback)
    define suave = Character("Thunder", callback=callback)
    define aggro = Character("Thunder", callback=callback)
    define professor = Character("Professor ██████", callback=callback)

label defaults:

    default date_puppy_1_done = False
    default date_puppy_2_done = False
    default date_puppy_3_done = False
    default date_puppy_4_done = False
    default date_puppy_5_done = False
    default date_flirty_1_done = False
    default date_flirty_2_done = False
    default date_flirty_3_done = False
    default date_flirty_4_done = False
    default date_flirty_5_done = False
    default date_suave_1_done = False
    default date_suave_2_done = False
    default date_suave_3_done = False
    default date_suave_4_done = False
    default date_suave_5_done = False
    default date_aggro_1_done = False
    default date_aggro_2_done = False
    default date_aggro_3_done = False
    default date_aggro_4_done = False
    default date_aggro_5_done = False
    default puppy_w1_points = 0
    default puppy_w1_successes = 0
    default suave_w1_points = 0
    default suave_w1_successes = 0
    default flirty_w1_points = 0
    default flirty_w1_successes = 0
    default aggro_w1_points = 0
    default aggro_w1_successes = 0
    default puppy_wtwo_points = 0
    default puppy_w2_successes = 0
    default suave_w2_points = 0
    default suave_w2_successes = 0
    default flirty_w2_points = 0
    default flirty_w2_successes = 0
    default aggro_w2_points = 0
    default aggro_w2_successes = 0
    default puppy_w3_points = 0
    default puppy_w3_successes = 0
    default suave_w3_points = 0
    default suave_w3_successes = 0
    default flirty_w3_points = 0
    default flirty_w3_successes = 0
    default aggro_w3_points = 0
    default aggro_w3_successes = 0
    default puppy_w4_points = 0
    default puppy_w4_successes = 0
    default suave_w4_points = 0
    default suave_w4_successes = 0
    default flirty_w4_points = 0
    default flirty_w4_successes = 0
    default aggro_w4_points = 0
    default aggro_w4_successes = 0
    default puppy_w5_points = 0
    default puppy_w5_successes = 0
    default suave_w5_points = 0
    default suave_w5_successes = 0
    default flirty_w5_points = 0
    default flirty_w5_successes = 0
    default aggro_w5_points = 0
    default aggro_w5_successes = 0
    default puppy_fw_points = 0
    default puppy_fw_successes = 0
    default suave_fw_points = 0
    default suave_fw_successes = 0
    default flirty_fw_points = 0
    default flirty_fw_successes = 0
    default aggro_fw_points = 0
    default aggro_fw_successes = 0
    default dates_puppy_completed = 0
    default dates_suave_completed = 0
    default dates_flirty_completed = 0
    default dates_aggro_completed = 0
    default taco_bell_points = 0
    default current_location = "Class"


# label blinking_animations:
#     image puppy normal:
#         choice (3.0):
#             "puppy normal.webp"
#         choice:
#             "puppy normal closed.webp"
#             pause 0.1
#             "puppy normal.webp"
#             pause 0.1
#             "puppy normal closed.webp"
#             pause 0.1
#             "puppy normal.webp"
#         pause 1.0
#         repeat

#     image flirty normal:
#         choice (3.0):
#             "flirty normal.webp"
#         choice:
#             "flirty normal closed.webp"
#             pause 0.1
#             "flirty normal.webp"
#             pause 0.1
#             "flirty normal closed.webp"
#             pause 0.1
#             "flirty normal.webp"
#         pause 1.0
#         repeat

#     image suave normal:
#         choice (3.0):
#             "suave normal.webp"
#         choice:
#             "suave normal closed.webp"
#             pause 0.1
#             "suave normal.webp"
#             pause 0.1
#             "suave normal closed.webp"
#             pause 0.1
#             "suave normal.webp"
#         pause 1.0
#         repeat

#     image aggro normal:
#         choice (3.0):
#             "aggro normal.webp"
#         choice:
#             "aggro normal closed.webp"
#             pause 0.1
#             "aggro normal.webp"
#             pause 0.1
#             "aggro normal closed.webp"
#             pause 0.1
#             "aggro normal.webp"
#         pause 1.0
#         repeat

label start:


    
    scene bg orientation
    play music "BGM/orientation-music.opus" fadein 1.0

    #asking for a name
    $ povname = renpy.input("What is your name?", length = 32)
    call pronounselection from _call_pronounselection
    #beginnning of the story
    pov "Wow, GCU orientation!"
    pov "I can't wait to meet everyone in my"
    pov "{fi=20-2-10}This is an example of Fade in Text{/fi}"
    
    pov "{rotat=100}This is an example of rotating text{/rotat}"
    pov "{sc=10}This is an example of Scare Text{/sc}"
    pov "{bt=10}This is an example of Bounce Text{/bt}"


    pov "What if I meet ... THE one?"
    pov "..."
    pov "Who's That?"

    show puppy normal with easeinleft
    puppy "Hello there minnow."
    puppy "Welcome to orientation."
    puppy "I am thunder!"
    puppy "The GCU mascot!"
    show puppy normal
    puppy "Wanna smooch?"
    show aggro normal at right 
    with moveinright
    aggro "[theyre!t!c] mine"
    show flirty normal at left

    pov "Ope-"

    scene black
    show text "Later That Week" with dissolve
    with Pause(2)
    hide text with dissolve


    scene bg classroom

    pov "Dang I can't stop thinking about Thunder...."
    pov "Maybe I'll see him at lope-a-palooza tonight...."

    show professor angry
    play sound akward
    professor "[povname]!!! STOP DOZING OFF!!!"


    show professor normal
    professor "I'm sorry [povname], that was very unprofessional. I shouldn't have yelled."
    professor "Now back to the topic at hand..."

    scene bg Dorm-or-something-idk

    pov "Dang, now that class is over I should go somewhere!"
    jump week1












label nope:
    scene black 
    show dwayne
    with Pause(0.6)
    hide dwayne
    show text "Nope." with dissolve
    with Pause(0.2)
    hide text with dissolve
    show text "That would be too confusing." with dissolve
    with Pause(0.2)
    hide text with dissolve
    show text "Try Again" with dissolve
    with Pause(0.2)
    hide text with dissolve
    return
