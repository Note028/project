input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . . # . .
        . # # # .
        . # . # .
        # . . . #
        # # # # #
        `)
    music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.UntilDone)
})
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.Chessboard)
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            # # # # #
            `)
    }
    music.stopAllSounds()
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(input.temperature())
})
input.onLogoEvent(TouchButtonEvent.Touched, function () {
    music.startMelody(music.builtInMelody(Melodies.Ringtone), MelodyOptions.Once)
})
basic.forever(function () {
	
})
