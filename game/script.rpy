# search zich to get to currently being modified parts of the code

# Declare characters used by this game. The color argument colorizes the
# name of the character.

###########################################################################
###########################################################################
###########################################################################

init -1 python:

    def tspk(what, amt=0, stmt=None, **kwargs):

        t(what, **kwargs)

        global amount
        amount = amt

        global bill

        portion = int(amt/5)

        if amt != 0:

            renpy.hide_screen("moneyadd", layer=None)
            renpy.show_screen("moneyadd", moneyadded=amt)

        if stmt != None:

            renpy.hide_screen("moneystmt", layer=None)
            renpy.show_screen("moneystmt", statement=stmt)

        i = 5

        while i > 0:

            renpy.pause(0.02)

            bill += portion
            amt -= portion

            i -= 1

###########################################################################
############# styles ######################################################


style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)


style outlined:
    outlines [ (absolute(1), "#000", absolute(0), absolute(0)) ]
    color "FFFF00"
    bold True

style friend:
    outlines [ (absolute(2), "#FF00FF", absolute(1), absolute(1)) ]
    color "FFFF00"
    font "courbd.ttf"
    size 72

style choice_button_text:
    color "0000FF"
    font "courbd.ttf"

################CHARACTERS########################

# default MC textbox
define narrator = Character(window_background="gui/textbox_narration.png", what_font='courbd.ttf', what_size=22,  color='#000000', what_color='#000000')
# no background box, used for black screens
define op = Character(window_background="gui/textbox_blank.png", what_font='courbd.ttf', what_size=28,  color='#FFFFFF', what_color='#FFFFFF', what_xalign=0.5, what_text_align=0.5)
# TAGORA
define t = Character("TAGORA", color='#FFFFFF', image="tagora", window_background="gui/textbox_teal.png", who_outlines=[ (4, "#008282") ],)


############IMAGES AND SHIT#################
#i'd advise you keep ypos the same for the important characters!
#also, i've left an ardata sprite in there just to help you to keep everything in proportion

# image robegor neutral = Image("images/goredit/robetagora_neutral.png", ypos=730, xanchor=640, yanchor=720)
# image robegor disgust = Image("images/goredit/robetagora_disgust.png", ypos=730, xanchor=640, yanchor=720)
# image robegor shrug = Image("images/goredit/robetagora_shrug.png", ypos=730, xanchor=640, yanchor=720)
# image robegor think = Image("images/goredit/robetagora_think.png", ypos=730, xanchor=640, yanchor=720)
# image robegor smug = Image("images/goredit/robetagora_smug.png", ypos=730, xanchor=640, yanchor=720)
# image robegor sexy = Image("images/goredit/robetagora_whydoeshelooksexytho.png", ypos=730, xanchor=640, yanchor=720)

image robegor neutral = Image("images/goredit/robetagora_neutral.png", ypos=730)
image robegor disgust = Image("images/goredit/robetagora_disgust.png", ypos=730)
image robegor shrug = Image("images/goredit/robetagora_shrug.png", ypos=730)
image robegor think = Image("images/goredit/robetagora_think.png", ypos=730)
image robegor smug = Image("images/goredit/robetagora_smug.png", ypos=730)
image robegor sexy = Image("images/goredit/robetagora_whydoeshelooksexytho.png", ypos=730)

image bg mc_hideout = "images/bgs/mc_hideout.png"
image bg tagora_bath = "images/bgs/tagorabath.png"
image bg tagora_int = "images/bgs/tagorainterior.png"
image bg tagora_ext = "images/bgs/tagoraexterior.png"

image money = "images/money/cashmoney.png"

## COMMON TRANSFORMS ##
#these are all transforms to make your sprite bounce around a little! it's super useful for making your game more dynamic
# bounce
# nod
# twitch
# shudder
# lowered
# bouncing
# shaking
# shuddering
# speaking
# stopspeaking
# shoveright
# shoveleft
# shoveoffleft
#
# moveinright
# moveinleft
# moveinbottom
# moveintop
# quickbouncetwice
# flipped

transform bounce:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform nod:
    ypos 730
    easeout 0.12 ypos 742
    linear 0.12 ypos 730

transform twitch:
    ypos 730 xpos 640
    easein 0.06 ypos 736 xpos 644
    linear 0.06 ypos 730 xpos 640

transform shudder:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat 4

transform lowered:
    ypos 730
    linear 0.75 ypos 765

transform bouncing:
    ypos 730
    linear 0.1 ypos 720
    linear 0.1 ypos 730
    repeat

transform shake:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730

transform shaking:
    ypos 730
    linear 0.07 ypos 732
    linear 0.07 ypos 730
    repeat

transform shuddering:

    xpos 640
    linear 0.04 xpos 637
    linear 0.04 xpos 640
    linear 0.04 xpos 643
    linear 0.04 xpos 640
    repeat

transform speaking:
    easein 0.1 zoom 1.01

transform stopspeaking:
    easein 0.1 zoom 1

#Quickly push sprite to side of screen
transform shoveright:

    linear 0.1 xpos 960

transform shoveleft:

    xpos 640
    linear 0.1 xpos 320

transform shoveoffleft:

    linear 0.1 xpos -320

transform shoveoffright:

    linear 0.1 xpos 1320

transform shoveup:

    xpos 640 ypos 1440
    linear 0.1 ypos 730

## ADDED ANIMATIONS
# quickbouncetwice
# flipped

transform quickbouncetwice:
    ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730
    easeout 0.12 ypos 716
    linear 0.12 ypos 730

transform flipped:
    xzoom -1.0

########################################################################
#####zich################ MONEY TRANSFORMS ###########################
########################################################################

transform moneybounce:

    parallel:

        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2.0 alpha 0.0
    parallel:

        xpos 910 ypos 80
        easein 1 ypos 65
        pause 1.8
        easeout 1 ypos 80

transform statementbounce:

    parallel:

        alpha 0.0
        linear 0.1 alpha 1.0
        pause 1.8
        easeout 2 alpha 0.0

    parallel:

        xpos 910 ypos 110
        easein 1 ypos 95
        pause 1.8
        easeout 1 ypos 110

########################################################################
#####zich################ CUSTOM TRANSFORMS ###########################
########################################################################

transform speaking2:
    easein 0.3 zoom 1.01

transform stopspeaking2:
    easein 0.3 zoom 1.0

    # easein 0.35 ypos 1640
########################################################################
#####zich################ ACTUAL GAME SCRIPT ###########################
########################################################################
label start:

    # This is used to easily add a formatted '>' to the start of choices in menus.
    $ pick = "{color=#000000}>{/color}"

    $ quick_menu = True

    $ volume1 = True

    jump start2

label start2:

    # Stop main menu music, or any other music playing, and transition to volume select.
    stop music fadeout 1.5

    show image "gui/main_menu.png"

    window hide

    scene black with Dissolve(1.5)

    $ main_menu = True

    call screen vol_select()

    stop music fadeout 1.5

####################################################################################
###zich########### BANA'S ROUTE ###################################################
####################################################################################

label tagora_route:

    $ renpy.block_rollback()

    $ main_menu = False

    show image "gui/game_menu.png"

    window hide

    scene black with Dissolve(1.5)

####################################################################################
####zich################ TEMPORARY TEASER FOR TWITTER ##############################
####################################################################################

    op "Well, isn't this exciting."

    op "I've bet you've never seen this text in a friendsim before."

    op "Perhaps you're wondering which Friendsim volume this will be."

    op "After all, you are always thirsty for..."

    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

    op "Hang on a moment... who's this?"

    scene bg tagora_int with dissolve

    $ quick_menu = True

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    $ bill = 0

    $ tdone = "\n\n*__________"

    show screen billcount

    tspk "..."

    show robegor disgust

    show robegor disgust at shake

    tspk "Why am I in another friendsim." (amt = 5000, stmt="Unsolicited visitation")

    show robegor disgust at bounce

    tspk "This wasn't in my contract. [tdone]" (amt = 20)

    tspk "They better be paying me for this." (amt = 20)


    show robegor disgust twitch

    tspk "..." (amt = 20)

    show robegor shrug at shudder

    tspk "Well, I guess if I'm here, I might as well make the most of it." (amt = 20)

    tspk "It would be uncharacteristic of me to pass up the opportunity to profit after all. [tdone]" (amt = 200, stmt="Canon characterisation")

    show robegor neutral

    tspk "..." (amt = 20)

    show robegor neutral at nod

    tspk "As you may have gathered, this is an excerpt of a fan friendsim." (amt = 20)

    tspk "One that Banavalope (@banavalope) is writing and drawing for, whilst Zich (@sburbd) is programming." (amt = 150, stmt="Namedrop fees")

    show robegor neutral at twitch

    tspk "I can't give you any more details for now, but you should keep your eyes peeled for the release." (amt = 20)

    tspk "Whilst I know very little about their respective skills, the friendsim looks promising." (amt = 20)

    tspk "Mainly because I will be appearing in it." (amt = 500, stmt="Lawerly ego stroking")

    show robegor shrug at twitch

    tspk "That is, if they manage to get it done sometime soon. [tdone]" (amt = 20)

    hide robegor shrug with dissolve

    $ quick_menu = False

    play music "music/victory_jingle.mp3" fadeout 1.0 noloop

    op "  "

    scene black with Dissolve(1.5)

####################################################################################
#####zich####################### END TEASER #####################################
####################################################################################

    scene bg tagora_int with dissolve

    $ quick_menu = True

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    $ bill = 0

    $ tdone = "\n\n*__________"

    tspk "..."

    show robegor disgust

    show robegor disgust at shake

    tspk "Why am I in another friendsim." (amt = 5000, stmt="Unsolicited visitation")

    show robegor disgust at bounce

    tspk "This wasn't in my contract. [tdone]" (amt = 20)

    tspk "They better be paying me for this." (amt = 20)

    hide screen billcount

####################################################################################
####zich################## TRANSITION DEMO FOR BANA ##############################
####################################################################################



####################################################################################
#####zich################## END TRANSITION DEMO #####################################
####################################################################################

    op "What's been with everything lately?"

    op "Has there even been a lately?"

    op "You're not trying to be dramatic here, after a series of recent unsettling events making you painfully aware of it..."

    op "...you’re honestly beginning to doubt the linearity and stability of time, along with the validity of your whole existence up to this point."

    op "What if this whole time you’ve just been stuck in a loop, reliving the same handful of days over and over again with no sign of progress past this miserable experience of reliving your successes and failures all at once?"

    op "It’s like some kind of fucked up purgatory, where your agency over your free will was stripped from you just to make you dance like a puppet for hungry, ruthless Gods desperate for something they can’t have."

    op "{size=80}{=friend}FRIENDSHIP.{/=friend}{/size}"

    op "Maybe you ARE being dramatic."

    op "Being dramatic sure does wipe you out."

    op "Your unquenchable thirst for budding new meaningful connections between yourself with strangers has really dried out from all this existential peril - you're run into the ground."

    op "You are operating at zero friendmiles per hour, the gumption tank is completely empty."

    scene bg mc_hideout with dissolve

    $ quick_menu = True

    window hide

    ##################################################################
    #################################################################

    play music "music/tagora_theme.mp3" loop

    show robegor neutral with moveinbottom

    $ bill = 0

    $ tdone = "\n\n*__________"

    show screen billcount

    tspk "Why am I in another friendsim." (amt = 200, stmt="Having to see your face fee.")

    show robegor neutral at nod

    tspk ew "I'm not even speaking the text that Bana's given me"

    show robegor disgust at speaking

    show robegor disgust at twitch

    t "You'd better write my script properly before you get me back here.[tdone]"

    ####################################################################
    ####zich################ IN PROGRESS ###############################
    ####################################################################

    $ renpy.pause(0.5)

    $ quick_menu = False

    play music "music/game_over.mp3" fadeout 1.0

    scene weegee with Dissolve(1.0)

    $ renpy.pause()

    stop music fadeout 1.0

    scene black with Dissolve(1.0)

    return

return
