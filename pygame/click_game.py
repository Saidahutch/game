character = Actor ('character')
character.topright = 0, 10

WIDTH = 500
HEIGHT = character.height + 20

def draw():
    screen.clear()
    character.draw()

def update():
    character.left= character.left + 2
    if character.left > WIDTH:
        character.right = 0
def on_mouse_down(pos):
    if character.collidepoint(pos):
        print('sound2')
        sounds.eep.play()
        character.image = 'character_clicked'
    if character.image == 'character_clicked':
        print('sound')
        sounds.eep.play()


def set_character_clicked():

    character.image = 'character_clicked'
    sounds.eep.play()
    clocks.schedule_unique(set_character_normal,1.0)

def set_character_normal():
    character.image = 'character'

