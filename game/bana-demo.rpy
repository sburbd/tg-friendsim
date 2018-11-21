####################################################################################
################################# DEMO FOR BANA ####################################
####################################################################################

label tagora_route_demo:

    # Don't worry about this stuff!
    $ renpy.block_rollback()

    $ main_menu = False

    $ bill = 0

    $ tdone = "\n\n*__________"

    show image "gui/game_menu.png"

    window hide

    # Here is where the friendsim volume really starts
    scene black with Dissolve(1.5)

    op "Right now the screen is black and this text by the speaker is being shown."

    op "Once the person clicks, they get to this new speaking line. Now let's go to Tagora's house"

    scene bg tagora_int with dissolve

    $ quick_menu = True

    narrator "We are now in Tagora's house."

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    show screen billcount

    "And now Tagora has noticed us."

    tspk "..."

    show robegor disgust at shake

    tspk "Why am I in another friendsim." (amt = 5000, stmt="Unsolicited visitation")

    menu:
        "Well? Why is he in another friendsim?"

        "[pick] I have no idea":

            show robegor disgust at bounce

            tspk "This wasn't in my contract. [tdone]" (amt = 20)

            "You can feel his friendship slipping away."

            hide screen billcount

            $ renpy.pause(0.5)

            $ quick_menu = False

            play music "music/game_over.mp3" fadeout 1.0 noloop

            scene tagora_bad_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

        "[pick] Banavalope is making a friendsim!":

            show robegor neutral at default

            tspk "Sounds interesting." (amt = 220, stmt="Ego boosted")

            hide screen billcount

            $ quick_menu = False

            play music "music/victory_jingle.mp3" fadeout 1.0 noloop

            scene tagora_good_ending with Dissolve(1.0)

            $ renpy.pause()

            stop music fadeout 1.0

            scene black with Dissolve(1.0)

            return

return
