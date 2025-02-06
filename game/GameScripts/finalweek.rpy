
#FINAL WEEK BEGIN
label finalweek:
    if date_puppy_1_done == True:
        $ dates_puppy_completed = dates_puppy_completed + 1
    if date_puppy_2_done == True:
        $ dates_puppy_completed = dates_puppy_completed + 1
    if date_puppy_3_done == True:
        $ dates_puppy_completed = dates_puppy_completed + 1
    if date_puppy_4_done == True:
        $ dates_puppy_completed = dates_puppy_completed + 1
    if date_puppy_5_done == True:
        $ dates_puppy_completed = dates_puppy_completed + 1

    if date_suave_1_done == True:
        $ dates_suave_completed = dates_suave_completed + 1
    if date_suave_2_done == True:
        $ dates_suave_completed = dates_suave_completed + 1
    if date_suave_3_done == True:
        $ dates_suave_completed = dates_suave_completed + 1
    if date_suave_4_done == True:
        $ dates_suave_completed = dates_suave_completed + 1
    if date_suave_5_done == True:
        $ dates_suave_completed = dates_suave_completed + 1

    if date_flirty_1_done == True:
        $ dates_flirty_completed = dates_flirty_completed + 1
    if date_flirty_2_done == True:
        $ dates_flirty_completed = dates_flirty_completed + 1
    if date_flirty_3_done == True:
        $ dates_flirty_completed = dates_flirty_completed + 1
    if date_flirty_4_done == True:
        $ dates_flirty_completed = dates_flirty_completed + 1
    if date_flirty_5_done == True:
        $ dates_flirty_completed = dates_flirty_completed + 1

    if date_aggro_1_done == True:
        $ dates_aggro_completed = dates_aggro_completed + 1
    if date_aggro_2_done == True:
        $ dates_aggro_completed = dates_aggro_completed + 1
    if date_aggro_3_done == True:
        $ dates_aggro_completed = dates_aggro_completed + 1
    if date_aggro_4_done == True:
        $ dates_aggro_completed = dates_aggro_completed + 1
    if date_aggro_5_done == True:
        $ dates_aggro_completed = dates_aggro_completed + 1



    if taco_bell_points >= 8:
        jump taco_bell_ending
    
    if dates_puppy_completed == 5:
        jump perfect_puppy_ending
    if dates_puppy_completed == 4:
        jump puppy_ending

    if dates_flirty_completed == 5:
        jump perfect_flirty_ending
    if dates_flirty_completed == 4:
        jump flirty_ending

    if dates_suave_completed == 5:
        jump perfect_suave_ending
    if dates_suave_completed == 4:
        jump suave_ending

    if dates_aggro_completed == 5:
        jump perfect_aggro_ending
    if dates_aggro_completed == 4:
        jump aggro_ending
    
        
    else:
        jump failure_ending


label failure_ending:
    stop music fadeout 1.0  
    scene black
    pov "Oh no I failed"
    show blarkin angry with dissolve
    blarkin "[pov], you are a worthless disgrace"
    hide blarkin with dissolve
    with Pause(2)
    
    show puppy normal with dissolve

    puppy "I trusted you, [pov]"
    hide puppy with dissolve

    with Pause(2)
    show aggro normal with dissolve
    
    aggro "You BITCH"
    return

label taco_bell_ending:
    scene black
    pov "OMG I GET TO MAKE OUT WITH █████ "

label perfect_puppy_ending:
    scene black
    pov "Puppy is my new hubby. He is perfectly in love with me."   


label perfect_flirty_ending:
    scene black
    pov "Flirty is my new hubby. He is perfectly in love with me."


label perfect_suave_ending:
    scene black
    pov "Suave is my new hubby. He is perfectly in love with me."


label perfect_aggro_ending:
    scene black
    pov "Aggro is my new hubby. He is perfectly in love with me."


label puppy_ending:
    scene black
    pov "Well, puppy is in love with me, its not perfect, but its good."
    jump end

label flirty_ending:
    scene black
    pov "Well, flirty is in love with me, its not perfect, but its good."
    jump end

label suave_ending:
    scene black
    pov "Well, suave is in love with me, its not perfect, but its good."
    jump end

label aggro_ending:
    scene black
    pov "Well, aggro is in love with me, its not perfect, but its good."
    jump end
