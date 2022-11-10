def on_button_pressed_a():
    basic.show_leds("""
        . . # . .
                . # # # .
                . # . # .
                # . . . #
                # # # # #
    """)
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
        SoundExpressionPlayMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    for index in range(4):
        basic.show_icon(IconNames.CHESSBOARD)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        # # # # #
        """)
    music.stop_all_sounds()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_touched():
    music.start_melody(music.built_in_melody(Melodies.RINGTONE), MelodyOptions.ONCE)
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)

def on_forever():
    pass
basic.forever(on_forever)
