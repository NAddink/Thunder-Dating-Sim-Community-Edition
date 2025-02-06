##SECOND WEEK BEGIN

label week2:
    $ week = 2
    label w2_begin:
        play music "BGM/event_choice.opus" fadein 0.5

        menu:
            "Where should I go w2?"

            "The Grove Pool":
                play music "BGM/flirty_theme.opus" fadein 1.0
                jump flirty_w2_start
                $ current_location = "The Grove Pool"

            "Student Union":
                play music "BGM/puppy_theme.opus" fadein 1.0
                jump puppy_w2_start
                $ current_location = "Student Union"

            "Ethington Theatre":
                play music "BGM/suave_theme.opus" fadein 1.0
                jump suave_w2_start
                $ current_location = "Ethington Theatre"
                

            "Prescott Field":
                play music "BGM/aggro_theme.opus" fadein 1.0
                jump aggro_w2_start
                $ current_location = "Prescott Field"

    label puppy_w2_start:
        scene bg student-union
        "As you enter the Student Union everything seems as it should be, passing The Habit you promptly notice Thunder interacting with a group of nursing students sitting at the main tables."
        pov "Wow its the Student Union"
        show puppy normal with easeinleft

        puppy "HEYO"
        puppy "I'm just a bit of a himbo bimbo but I am cute like a puppy."
        puppy "I am actually exhuding golden retriever energy..."
        show puppy blushing
        puppy "Also I'm hypoallergenic"


        jump puppy_w2_dialogue

    label puppy_w2_dialogue:
        label puppy_w2_d1:
            
            menu:
                "What do I say d1?"

                "Answer1":
                    #is correct answer
                    $ puppy_wtwo_points = puppy_wtwo_points + 1
                    jump puppy_w2_d1_a1

                "Answer2":
                    jump puppy_w2_d1_a2

                "Answer3":
                    jump puppy_w2_d1_a3

            label puppy_w2_d1_a1:
                pov "puppy dialogue for week 2 dialogue 1 answer 1 "
                jump puppy_w2_d2

            label puppy_w2_d1_a2:
                pov "puppy dialogue for week 2 dialogue 1 answer 2 "
                jump puppy_w2_d2

            label puppy_w2_d1_a3:
                pov "puppy dialogue for week 2 dialogue 1 answer 3 "
                jump puppy_w2_d2

        label puppy_w2_d2:
            
            menu:
                "What do I say d2?"

                "Answer1":
                    #Is correct answer
                    $ puppy_wtwo_points = puppy_wtwo_points + 1
                    jump puppy_w2_d2_a1

                "Answer2":
                    jump puppy_w2_d2_a2

                "Answer3":
                    jump puppy_w2_d2_a3

            label puppy_w2_d2_a1:
                pov "puppy dialogue for week 2 dialogue 2 answer 1 "
                jump puppy_w2_d3

            label puppy_w2_d2_a2:
                pov "puppy dialogue for week 2 dialogue 2 answer 2 "
                jump puppy_w2_d3

            label puppy_w2_d2_a3:
                pov "puppy dialogue for week 2 dialogue 2 answer 3 "
                jump puppy_w2_d3

        label puppy_w2_d3:
            
            menu:
                "What do I say d3?"

                "Answer1":
                    #is correct answer
                    $ puppy_wtwo_points = puppy_wtwo_points + 1
                    jump puppy_w2_d3_a1

                "Answer2":
                    jump puppy_w2_d3_a2

                "Answer3":
                    jump puppy_w2_d3_a3


            label puppy_w2_d3_a1:
                pov "puppy dialogue for week 2 dialogue 3 answer 1 "
                jump puppy_w2_d_complete

            label puppy_w2_d3_a2:
                pov "puppy dialogue for week 2 dialogue 3 answer 2 "
                jump puppy_w2_d_complete

            label puppy_w2_d3_a3:
                pov "puppy dialogue for week 2 dialogue 3 answer 3 "
                jump puppy_w2_d_complete

        label puppy_w2_d_complete:
            pov "Wow I'm done talking"
            if puppy_wtwo_points >= 2:
                jump puppy_w2_success
            else:
                jump puppy_w2_failure


        label puppy_w2_success:
            pov "Wow I succeeded"
            $ puppy_w2_successes = 1
            jump w2_complete
            

        label puppy_w2_failure:
            pov "Wow I failed"
            jump w2_complete
    
    label flirty_w2_start:
        scene bg grove-pool

        pov "Wow its the Grove Pool"

        show flirty normal with easeinleft

        flirty "HEYO"
        flirty "I love you, but I'm just too flirty."
        flirty "I can't be not flirty and I need someone to take my flirtiness out on."
        
        $ flirty_w2_points = 0

        jump flirty_w2_dialogue

    label flirty_w2_dialogue:
        label flirty_w2_d1:

            menu:
                "What do I say d1?"

                "Answer1":
                    #is correct answer
                    $ flirty_w2_points += 1
                    jump flirty_w2_d1_a1

                "Answer2":
                    jump flirty_w2_d1_a2

                "Answer3":
                    jump flirty_w2_d1_a3

            label flirty_w2_d1_a1:
                pov "flirty dialogue for week 2 dialogue 1 answer 1 "
                jump flirty_w2_d2

            label flirty_w2_d1_a2:
                pov "flirty dialogue for week 2 dialogue 1 answer 2 "
                jump flirty_w2_d2

            label flirty_w2_d1_a3:
                pov "flirty dialogue for week 2 dialogue 1 answer 3 "
                jump flirty_w2_d2

        label flirty_w2_d2:
            
            menu:
                "What do I say d2?"

                "Answer1":
                    #Is correct answer
                    $ flirty_w2_points += 1
                    jump flirty_w2_d2_a1

                "Answer2":
                    jump flirty_w2_d2_a2

                "Answer3":
                    jump flirty_w2_d2_a3

            label flirty_w2_d2_a1:
                pov "flirty dialogue for week 2 dialogue 2 answer 1 "
                jump flirty_w2_d3

            label flirty_w2_d2_a2:
                pov "flirty dialogue for week 2 dialogue 2 answer 2 "
                jump flirty_w2_d3

            label flirty_w2_d2_a3:
                pov "flirty dialogue for week 2 dialogue 2 answer 3 "
                jump flirty_w2_d3



        label flirty_w2_d3:
            
            menu:
                "What do I say d3?"
                
                "Answer1":
                    #is correct answer
                    $ flirty_w2_points += 1
                    jump flirty_w2_d3_a1

                "Answer2":
                    jump flirty_w2_d3_a2

                "Answer3":
                    jump flirty_w2_d3_a3


            label flirty_w2_d3_a1:
                pov "flirty dialogue for week 2 dialogue 3 answer 1 "
                jump flirty_w2_d_complete

            label flirty_w2_d3_a2:
                pov "flirty dialogue for week 2 dialogue 3 answer 2 "
                jump flirty_w2_d_complete

            label flirty_w2_d3_a3:
                pov "flirty dialogue for week 2 dialogue 3 answer 3 "
                jump flirty_w2_d_complete

        label flirty_w2_d_complete:
            pov "Wow I'm done talking"
            if flirty_w2_points >= 2:
                jump flirty_w2_success
            else:
                jump flirty_w2_failure


        label flirty_w2_success:
            pov "Wow I succeeded"
            $ flirty_w2_successes = 1
            jump w2_complete
            

        label flirty_w2_failure:
            pov "Wow I failed"
            jump w2_complete
        
    label suave_w2_start:
        scene bg ethington-theatre

        pov "Wow its Ethington Theatre"

        show suave normal with easeinleft

        suave "HEYO"
        suave "I'm just so dang suave. Wow. I wish I was less suave."
        suave "JK I love being suave. Smooch me please."

        jump suave_w2_dialogue

    label suave_w2_dialogue:
        label suave_w2_d1:

        menu:
            "What do I say d1?"

            "Answer1":
                #is correct answer
                $ suave_w2_points = suave_w2_points + 1
                jump suave_w2_d1_a1

            "Answer2":
                jump suave_w2_d1_a2

            "Answer3":
                jump suave_w2_d1_a3

        label suave_w2_d1_a1:
            pov "suave dialogue for week 2 dialogue 1 answer 1 "
            jump suave_w2_d2

        label suave_w2_d1_a2:
            pov "suave dialogue for week 2 dialogue  answer 2 "
            jump suave_w2_d2

        label suave_w2_d1_a3:
            pov "suave dialogue for week 2 dialogue 1 answer 3 "
            jump suave_w2_d2

        label suave_w2_d2:
            
        menu:
            "What do I say d2?"

            "Answer1":
                #Is correct answer
                $ suave_w2_points = suave_w2_points + 1
                jump suave_w2_d2_a1

            "Answer2":
                jump suave_w2_d2_a2

            "Answer3":
                jump suave_w2_d2_a3

        label suave_w2_d2_a1:
            pov "suave dialogue for week 2 dialogue 2 answer 1 "
            jump suave_w2_d3

        label suave_w2_d2_a2:
            pov "suave dialogue for week 2 dialogue 2 answer 2 "
            jump suave_w2_d3

        label suave_w2_d2_a3:
            pov "suave dialogue for week 2 dialogue 2 answer 3 "
            jump suave_w2_d3



        label suave_w2_d3:
            
        menu:
            "What do I say d3?"

            "Answer1":
                #is correct answer
                $ suave_w2_points = suave_w2_points + 1
                jump suave_w2_d3_a1

            "Answer2":
                jump suave_w2_d3_a2

            "Answer3":
                jump suave_w2_d3_a3


        label suave_w2_d3_a1:
            pov "suave dialogue for week 2 dialogue 3 answer 1 "
            jump suave_w2_d_complete

        label suave_w2_d3_a2:
            pov "suave dialogue for week 2 dialogue 3 answer 2 "
            jump suave_w2_d_complete

        label suave_w2_d3_a3:
            pov "suave dialogue for week 2 dialogue 3 answer 3 "
            jump suave_w2_d_complete

        label suave_w2_d_complete:
            pov "Wow I'm done talking"
            if suave_w2_points >= 2:
                jump suave_w2_success
            else:
                jump suave_w2_failure


        label suave_w2_success:
            pov "Wow I succeeded"
            $ suave_w2_successes = suave_w2_successes + 1
            jump w2_complete
            

        label suave_w2_failure:
            pov "Wow I failed"
            jump w2_complete
        
    label aggro_w2_start:
        scene bg prescott-field

        pov "Wow its Prescott field"

        show aggro normal with easeinleft

        aggro "HEYO"
        aggro "I'm a bad boy, owo"
        aggro "Date me and you'll find out how bad boy I am."
        jump aggro_w2_dialogue

    label aggro_w2_dialogue:
        label aggro_w2_d1:
            
        menu:
            "What do I say d1?"

            "Answer1":
                #is correct answer
                $ aggro_w2_points = aggro_w2_points + 1
                jump aggro_w2_d1_a1

            "Answer2":
                jump aggro_w2_d1_a2

            "Answer3":
                jump aggro_w2_d1_a3

        label aggro_w2_d1_a1:
            pov "aggro dialogue for week 2 dialogue 1 answer 1 "
            jump aggro_w2_d2

        label aggro_w2_d1_a2:
            pov "aggro dialogue for week 2 dialogue 1 answer 2 "
            jump aggro_w2_d2

        label aggro_w2_d1_a3:
            pov "aggro dialogue for week 2 dialogue 1 answer 3 "
            jump aggro_w2_d2

        label aggro_w2_d2:
            
        menu:
            "What do I say d2?"

            "Answer1":
                #Is correct answer
                $ aggro_w2_points = aggro_w2_points + 1
                jump aggro_w2_d2_a1

            "Answer2":
                jump aggro_w2_d2_a2

            "Answer3":
                jump aggro_w2_d2_a3

        label aggro_w2_d2_a1:
            pov "aggro dialogue for week 2 dialogue 2 answer 1 "
            jump aggro_w2_d3

        label aggro_w2_d2_a2:
            pov "aggro dialogue for week 2 dialogue 2 answer 2 "
            jump aggro_w2_d3

        label aggro_w2_d2_a3:
            pov "aggro dialogue for week 2 dialogue 2 answer 3 "
            jump aggro_w2_d3



        label aggro_w2_d3:
            
        menu:
            "What do I say d3?"

            "Answer1":
                #is correct answer
                $ aggro_w2_points = aggro_w2_points + 1
                jump aggro_w2_d3_a1

            "Answer2":
                jump aggro_w2_d3_a2

            "Answer3":
                jump aggro_w2_d3_a3


        label aggro_w2_d3_a1:
            pov "aggro dialogue for week 2 dialogue 3 answer 1 "
            jump aggro_w2_d_complete

        label aggro_w2_d3_a2:
            pov "aggro dialogue for week 2 dialogue 3 answer 2 "
            jump aggro_w2_d_complete

        label aggro_w2_d3_a3:
            pov "aggro dialogue for week 2 dialogue 3 answer 3 "
            jump aggro_w2_d_complete

        label aggro_w2_d_complete:
            pov "Wow I'm done talking"
            if aggro_w2_points >= 2:
                jump aggro_w2_success
            else:
                jump aggro_w2_failure


        label aggro_w2_success:
            pov "Wow I succeeded"
            $ aggro_w2_successes = 1
            jump w2_complete
            

        label aggro_w2_failure:
            pov "Wow I failed"
            jump w2_complete
        
label w2_complete:

    if puppy_w2_successes == 1:
        if date_puppy_1_done == True: 
            jump date_puppy_2
        else:
            jump date_puppy_1

    if flirty_w2_successes == 1:
        if date_flirty_1_done == True:
            jump date_flirty_2
        else:
            jump date_flirty_1

    if suave_w2_successes == 1:
        if date_suave_1_done == True:
            jump date_suave_2
        else:
            jump date_suave_1

    if aggro_w2_successes == 1:
        if date_aggro_1_done == True:
            jump date_aggro_2
        else:
            jump date_aggro_1

    else:
        jump failureweek2

label failureweek2:
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
        
label date2:

    label date_puppy_2:

        menu:
            "Where should I go on a date with puppy?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_puppy_2_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_puppy_2_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_puppy_2_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_puppy_2_date
                
    label date_puppy_2_date:
        pov "Wow I'm on a 2nd date with puppy"
        $ date_puppy_2_done = True
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
    

    label date_flirty_2:

        menu:
            "Where should I go on a date with flirty?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_flirty_2_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_flirty_2_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_flirty_2_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_flirty_2_date
                
    label date_flirty_2_date:
        pov "Wow I'm on a 2nd date with suave"
        $ date_suave_2_done = True
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

    label date_suave_2:

        menu:
            "Where should I go on a date with suave?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_suave_2_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_suave_2_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_suave_2_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_suave_2_date
                
    label date_suave_2_date:
        pov "Wow I'm on a 2nd date with suave"
        $ date_suave_2_done = True
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

    label date_aggro_2:

        menu:
            "Where should I go on a date with aggro?"
            
            "GCBC":
                $ current_date_location = "GCBC"
                jump date_aggro_2_date
            
            "Taco Bell":
                $ current_date_location = "Taco Bell"
                $ taco_bell_points = taco_bell_points + 1
                jump date_aggro_2_date

            "Lopes Way":
                $ current_date_location = "Lopes Way"
                jump date_aggro_2_date

            "The Quad":
                $ current_date_location = "The Quad"
                jump date_aggro_2_date
                
    label date_aggro_2_date:
        pov "Wow I'm on a 2nd date with aggro"
        $ date_aggro_2_done = True
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


##SECOND WEEK END
