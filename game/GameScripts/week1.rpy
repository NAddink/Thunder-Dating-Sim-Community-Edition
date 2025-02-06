label week1:
    $ week = 1
    label w1_begin:
        play music "BGM/event_choice.opus" fadein 0.5

        menu:
            "Where should I go w1?"


            "Thunderground":
                play music "BGM/flirty_theme.opus" fadein 1.0
                jump flirty_w1_start
                $ current_location = "Thunderground"

            "The Library":
                play music "BGM/suave_theme.opus" fadein 1.0
                jump suave_w1_start
                $ current_location = "The Library"

            "The E-sports Lounge":
                play music "BGM/aggro_theme.opus" fadein 1.0
                jump aggro_w1_start
                $ current_location = "The E-sports Lounge"

            "The Soccer Field":
                play music "BGM/puppy_theme.opus" fadein 1.0
                jump puppy_w1_start
                $ current_location = "Soccer Field"

    label puppy_w1_start:
        scene bg soccer-Field

        pov "Wow its the soccer field"
        "You make your way to the Soccer Field. As you come around the corner to the Student Life Building you spot him. Thunder seems to have joined in on a group of students' game of soccer, and you watch as he bounces up and down the field trying to maneuver in his bulky suit."


        show puppy normal with easeinleft

        puppy "HEYO"
        puppy "I'm just a bit of a himbo bimbo but I am cute like a puppy."
        puppy "I am actually exhuding golden retriever energy..."
        show puppy blushing
        puppy "Also I'm hypoallergenic"


        jump puppy_w1_dialogue

    label puppy_w1_dialogue:
        label puppy_w1_d1:
            
            menu:
                "What do I say d1?"

                "Answer1":
                    #is correct answer
                    $ puppy_w1_points = puppy_w1_points + 1
                    jump puppy_w1_d1_a1

                "Answer2":
                    jump puppy_w1_d1_a2

                "Answer3":
                    jump puppy_w1_d1_a3

            label puppy_w1_d1_a1:
                pov "puppy dialogue for week 1 dialogue 1 answer 1 "
                jump puppy_w1_d2

            label puppy_w1_d1_a2:
                pov "puppy dialogue for week 1 dialogue 1 answer 2 "
                jump puppy_w1_d2

            label puppy_w1_d1_a3:
                pov "puppy dialogue for week 1 dialogue 1 answer 3 "
                jump puppy_w1_d2

        label puppy_w1_d2:
            
            menu:
                "What do I say d2?"

                "Answer1":
                    #Is correct answer
                    $ puppy_w1_points = puppy_w1_points + 1
                    jump puppy_w1_d2_a1

                "Answer2":
                    jump puppy_w1_d2_a2

                "Answer3":
                    jump puppy_w1_d2_a3

            label puppy_w1_d2_a1:
                pov "puppy dialogue for week 1 dialogue 2 answer 1 "
                jump puppy_w1_d3

            label puppy_w1_d2_a2:
                pov "puppy dialogue for week 1 dialogue 2 answer 2 "
                jump puppy_w1_d3

            label puppy_w1_d2_a3:
                pov "puppy dialogue for week 1 dialogue 2 answer 3 "
                jump puppy_w1_d3

        label puppy_w1_d3:
            
            menu:
                "What do I say d3?"

                "Answer1":
                    #is correct answer
                    $ puppy_w1_points = puppy_w1_points + 1
                    jump puppy_w1_d3_a1

                "Answer2":
                    jump puppy_w1_d3_a2

                "Answer3":
                    jump puppy_w1_d3_a3


            label puppy_w1_d3_a1:
                pov "puppy dialogue for week 1 dialogue 3 answer 1 "
                jump puppy_w1_d_complete

            label puppy_w1_d3_a2:
                pov "puppy dialogue for week 1 dialogue 3 answer 2 "
                jump puppy_w1_d_complete

            label puppy_w1_d3_a3:
                pov "puppy dialogue for week 1 dialogue 3 answer 3 "
                jump puppy_w1_d_complete

        label puppy_w1_d_complete:
            pov "Wow I'm done talking"
            if puppy_w1_points >= 2:
                jump puppy_w1_success
            else:
                jump puppy_w1_failure


        label puppy_w1_success:
            pov "Wow I succeeded"
            $ puppy_w1_successes =+ 1
            jump w1_complete
            

        label puppy_w1_failure:
            pov "Wow I failed"
            jump w1_complete
    
    label flirty_w1_start:
        scene bg thunderground
        
        pov "Wow its the Thunderground"
        
        show flirty normal with easeinleft

        flirty "HEYO"
        flirty "I love you, but I'm just too flirty."
        flirty "I can't be not flirty and I need someone to take my flirtiness out on."
        
        $ flirty_w1_points = 0

        jump flirty_w1_dialogue

    label flirty_w1_dialogue:
        label flirty_w1_d1:

            menu:
                "What do I say d1?"

                "Answer1":
                    #is correct answer
                    $ flirty_w1_points = flirty_w1_points + 1
                    jump flirty_w1_d1_a1

                "Answer2":
                    jump flirty_w1_d1_a2

                "Answer3":
                    jump flirty_w1_d1_a3

            label flirty_w1_d1_a1:
                pov "flirty dialogue for week 1 dialogue 1 answer 1 "
                jump flirty_w1_d2

            label flirty_w1_d1_a2:
                pov "flirty dialogue for week 1 dialogue 1 answer 2 "
                jump flirty_w1_d2

            label flirty_w1_d1_a3:
                pov "flirty dialogue for week 1 dialogue 1 answer 3 "
                jump flirty_w1_d2

        label flirty_w1_d2:
            
            menu:
                "What do I say d2?"

                "Answer1":
                    #Is correct answer
                    $ flirty_w1_points = flirty_w1_points + 1
                    jump flirty_w1_d2_a1

                "Answer2":
                    jump flirty_w1_d2_a2

                "Answer3":
                    jump flirty_w1_d2_a3

            label flirty_w1_d2_a1:
                pov "flirty dialogue for week 1 dialogue 2 answer 1 "
                jump flirty_w1_d3

            label flirty_w1_d2_a2:
                pov "flirty dialogue for week 1 dialogue 2 answer 2 "
                jump flirty_w1_d3

            label flirty_w1_d2_a3:
                pov "flirty dialogue for week 1 dialogue 2 answer 3 "
                jump flirty_w1_d3



        label flirty_w1_d3:
            
            menu:
                "What do I say d3?"

                "Answer1":
                    #is correct answer
                    $ flirty_w1_points = flirty_w1_points + 1
                    jump flirty_w1_d3_a1

                "Answer2":
                    jump flirty_w1_d3_a2

                "Answer3":
                    jump flirty_w1_d3_a3


            label flirty_w1_d3_a1:
                pov "flirty dialogue for week 1 dialogue 3 answer 1 "
                jump flirty_w1_d_complete

            label flirty_w1_d3_a2:
                pov "flirty dialogue for week 1 dialogue 3 answer 2 "
                jump flirty_w1_d_complete

            label flirty_w1_d3_a3:
                pov "flirty dialogue for week 1 dialogue 3 answer 3 "
                jump flirty_w1_d_complete

        label flirty_w1_d_complete:
            pov "Wow I'm done talking"
            if flirty_w1_points >= 2:
                jump flirty_w1_success
            else:
                jump flirty_w1_failure


        label flirty_w1_success:
            pov "Wow I succeeded"
            $ flirty_w1_successes = flirty_w1_successes + 1
            jump w1_complete
            

        label flirty_w1_failure:
            pov "Wow I failed"
            jump w1_complete
        
    label suave_w1_start:
        scene bg library

        pov "Wow its the Library"

        show suave normal with easeinleft

        suave "HEYO"
        suave "I'm just so dang suave. Wow. I wish I was less suave."
        suave "JK I love being suave. Smooch me please."

        jump suave_w1_dialogue

    label suave_w1_dialogue:
        label suave_w1_d1:

        menu:
            "What do I say d1?"

            "Answer1":
                #is correct answer
                $ suave_w1_points = suave_w1_points + 1
                jump suave_w1_d1_a1

            "Answer2":
                jump suave_w1_d1_a2

            "Answer3":
                jump suave_w1_d1_a3

        label suave_w1_d1_a1:
            pov "suave dialogue for week 1 dialogue 1 answer 1 "
            jump suave_w1_d2

        label suave_w1_d1_a2:
            pov "suave dialogue for week 1 dialogue  answer 2 "
            jump suave_w1_d2

        label suave_w1_d1_a3:
            pov "suave dialogue for week 1 dialogue 1 answer 3 "
            jump suave_w1_d2

        label suave_w1_d2:
            
        menu:
            "What do I say d2?"

            "Answer1":
                #Is correct answer
                $ suave_w1_points = suave_w1_points + 1
                jump suave_w1_d2_a1

            "Answer2":
                jump suave_w1_d2_a2

            "Answer3":
                jump suave_w1_d2_a3

        label suave_w1_d2_a1:
            pov "suave dialogue for week 1 dialogue 2 answer 1 "
            jump suave_w1_d3

        label suave_w1_d2_a2:
            pov "suave dialogue for week 1 dialogue 2 answer 2 "
            jump suave_w1_d3

        label suave_w1_d2_a3:
            pov "suave dialogue for week 1 dialogue 2 answer 3 "
            jump suave_w1_d3



        label suave_w1_d3:
            
        menu:
            "What do I say d3?"

            "Answer1":
                #is correct answer
                $ suave_w1_points = suave_w1_points + 1
                jump suave_w1_d3_a1

            "Answer2":
                jump suave_w1_d3_a2

            "Answer3":
                jump suave_w1_d3_a3


        label suave_w1_d3_a1:
            pov "suave dialogue for week 1 dialogue 3 answer 1 "
            jump suave_w1_d_complete

        label suave_w1_d3_a2:
            pov "suave dialogue for week 1 dialogue 3 answer 2 "
            jump suave_w1_d_complete

        label suave_w1_d3_a3:
            pov "suave dialogue for week 1 dialogue 3 answer 3 "
            jump suave_w1_d_complete

        label suave_w1_d_complete:
            pov "Wow I'm done talking"
            if suave_w1_points >= 2:
                jump suave_w1_success
            else:
                jump suave_w1_failure


        label suave_w1_success:
            pov "Wow I succeeded"
            $ suave_w1_successes = suave_w1_successes + 1
            jump w1_complete
            

        label suave_w1_failure:
            pov "Wow I failed"
            jump w1_complete
        
    label aggro_w1_start:
        scene bg e-sports-lounge

        pov "Wow its the E-sports lounge"

        show aggro normal with easeinleft

        aggro "HEYO"
        aggro "I'm a bad boy, owo"
        aggro "Date me and you'll find out how bad boy I am."
        jump aggro_w1_dialogue

    label aggro_w1_dialogue:
        label aggro_w1_d1:
            
        menu:
            "What do I say d1?"

            "Answer1":
                #is correct answer
                $ aggro_w1_points = aggro_w1_points + 1
                jump aggro_w1_d1_a1

            "Answer2":
                jump aggro_w1_d1_a2

            "Answer3":
                jump aggro_w1_d1_a3

        label aggro_w1_d1_a1:
            pov "aggro dialogue for week 1 dialogue 1 answer 1 "
            jump aggro_w1_d2

        label aggro_w1_d1_a2:
            pov "aggro dialogue for week 1 dialogue 1 answer 2 "
            jump aggro_w1_d2

        label aggro_w1_d1_a3:
            pov "aggro dialogue for week 1 dialogue 1 answer 3 "
            jump aggro_w1_d2

        label aggro_w1_d2:
            
        menu:
            "What do I say d2?"

            "Answer1":
                #Is correct answer
                $ aggro_w1_points = aggro_w1_points + 1
                jump aggro_w1_d2_a1

            "Answer2":
                jump aggro_w1_d2_a2

            "Answer3":
                jump aggro_w1_d2_a3

        label aggro_w1_d2_a1:
            pov "aggro dialogue for week 1 dialogue 2 answer 1 "
            jump aggro_w1_d3

        label aggro_w1_d2_a2:
            pov "aggro dialogue for week 1 dialogue 2 answer 2 "
            jump aggro_w1_d3

        label aggro_w1_d2_a3:
            pov "aggro dialogue for week 1 dialogue 2 answer 3 "
            jump aggro_w1_d3



        label aggro_w1_d3:
            
        menu:
            "What do I say d3?"

            "Answer1":
                #is correct answer
                $ aggro_w1_points = aggro_w1_points + 1
                jump aggro_w1_d3_a1

            "Answer2":
                jump aggro_w1_d3_a2

            "Answer3":
                jump aggro_w1_d3_a3


        label aggro_w1_d3_a1:
            pov "aggro dialogue for week 1 dialogue 3 answer 1 "
            jump aggro_w1_d_complete

        label aggro_w1_d3_a2:
            pov "aggro dialogue for week 1 dialogue 3 answer 2 "
            jump aggro_w1_d_complete

        label aggro_w1_d3_a3:
            pov "aggro dialogue for week 1 dialogue 3 answer 3 "
            jump aggro_w1_d_complete

        label aggro_w1_d_complete:
            pov "Wow I'm done talking"
            if aggro_w1_points >= 2:
                jump aggro_w1_success
            else:
                jump aggro_w1_failure


        label aggro_w1_success:
            pov "Wow I succeeded"
            $ aggro_w1_successes = aggro_w1_successes + 1
            jump w1_complete
            

        label aggro_w1_failure:
            pov "Wow I failed"
            jump w1_complete
        
label w1_complete:
    pov "Wow I had a nice week with thunder"
    
    

    if puppy_w1_successes == 1 and date_puppy_1_done == False :
        jump date_puppy_1
    if flirty_w1_successes == 1 and date_flirty_1_done == False:
        jump date_flirty_1
    if suave_w1_successes == 1 and date_suave_1_done == False:
        jump date_suave_1
    if aggro_w1_successes == 1 and date_aggro_1_done == False:
        jump date_aggro_1
    else:
        jump failureweek1

label failureweek1:
    pov "I failed. No date."
    if week == 1:
        jump week2
    if week == 2:
        jump week3
    if week == 3:
        jump week4
    if week == 4:
        jump week5
    if week == 5:
        jump finalweek

label date1:

    label date_puppy_1:
        menu:
            "Where should I go on a date with puppy?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_puppy_1_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_puppy_1_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_puppy_1_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_puppy_1_date

    label date_puppy_1_date:
        pov "Wow I'm on a date with puppy"
        $ date_puppy_1_done = True
        if week == 1:
            jump week2
        if week == 2:
            jump week3
        if week == 3:
            jump week4
        if week == 4:
            jump week5
        if week == 5:
            jump finalweek
    

    label date_flirty_1:
        menu:
            "Where should I go on a date with flirty?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_flirty_1_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_flirty_1_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_flirty_1_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_flirty_1_date
                
    label date_flirty_1_date:
        pov "Wow I'm on a date with flirty"
        $ date_suave_1_done = True
        if week == 1:
            jump week2
        if week == 2:
            jump week3
        if week == 3:
            jump week4
        if week == 4:
            jump week5
        if week == 5:
            jump finalweek


    label date_suave_1:

        menu:
            "Where should I go on a date with suave?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_suave_1_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_suave_1_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_suave_1_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_suave_1_date
                
    label date_suave_1_date:
        pov "Wow I'm on a date with suave"
        $ date_suave_1_done = True
        if week == 1:
            jump week2
        if week == 2:
            jump week3
        if week == 3:
            jump week4
        if week == 4:
            jump week5
        if week == 5:
            jump finalweek

    label date_aggro_1:

        menu:
            "Where should I go on a date with aggro?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_aggro_1_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_aggro_1_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_aggro_1_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_aggro_1_date
                
    label date_aggro_1_date:
        pov "Wow I'm on a date with aggro"
        $ date_aggro_1_done = True
        if week == 1:
            jump week2
        if week == 2:
            jump week3
        if week == 3:
            jump week4
        if week == 4:
            jump week5
        if week == 5:
            jump finalweek

##FIRST WEEK END