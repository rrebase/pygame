"""Main."""
import random

import pygame
import sys

import KeyListener
import game_graphics.Display
import game_graphics.UI.UI
import Menu
import World
import objects.mobs.Player
import objects.mobs.Worker_man
import game_state.Game_State
import game_graphics.UI
import sounds.Sound_control


pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

window_title = "Driven Into the Last Corner"  # Title on top of the frame.
window_width = 1200  # Width of the canvas.
window_height = 700  # Height of the canvas.
fps_fix = 60

running = True  # while True game will run.

sc = sounds.Sound_control.SoundControl()
player = objects.mobs.Player.Player(30 << 5, 70 << 5)
world = World.World()
gamestate = game_state.Game_State.Game_State()
worker_man = objects.mobs.Worker_man.Worker(37 << 5, 70 << 5)
worker_man2 = objects.mobs.Worker_man.Worker(30 << 5, 70 << 5)

user_interface = None


def update():
    """Update all."""
    KeyListener.update()
    cameraPos()  # update camera position.
    world.update()
    if not Menu.inMenu:
        user_interface.update()

    if KeyListener.exit_game is True:
        sys.exit()


def render(display_obj):
    """Render all visible stuff."""
    display_obj.canvas.fill(int(0x000000))
    world.render(display_obj)
    if not Menu.inMenu:
        user_interface.render(display_obj)


cameraPosDoubleX = 0
cameraPosDoubleY = 0


def cameraPos():
    """Update camera position."""
    global cameraPosDoubleX
    global cameraPosDoubleY

    if Menu.inMenu:
        cameraPosDoubleX = (player.x - (window_width / 2))
        cameraPosDoubleY = (player.y - (window_height / 2))
    else:
        cameraPosDoubleX += (player.x - (cameraPosDoubleX + window_width / 2)) / 20
        cameraPosDoubleY += (player.y - (cameraPosDoubleY + window_height / 2)) / 20

    World.World.camera_x = int(cameraPosDoubleX)
    World.World.camera_y = int(cameraPosDoubleY)


def run():
    """Run the game."""
    sounds.Sound_control.SoundControl.play_menu_music(sc)

    global game_window
    game_window = game_graphics.Display.Display(window_width, window_height, fps_fix)
    mr = Menu.MenuRun(game_window.canvas)
    mr.run(game_window.canvas, surf=game_window)

    world.mobs.append(worker_man)
    world.mobs.append(worker_man2)
    world.mobs.append(player)
    World.player = player
    global user_interface
    user_interface = game_graphics.UI.UI.UI()
    sounds.Sound_control.SoundControl.fadeout_menu_music_to_game_music(sc, 3000)  # fadeout time is in ms

    while running:
        game_window.clock.tick(game_window.fps)
        pygame.display.set_caption(window_title + " | " + "FPS: %i" % game_window.clock.get_fps())
        update()
        render(game_window)
        # game_window.canvas.blit(pygame.image.frombuffer(PIL.Image.frombytes('RGB', (1200, 700), pygame.image.tostring(game_window.canvas, 'RGB')).filter(ImageFilter.GaussianBlur(radius=7)).tobytes(), (1200, 700), "RGB"), (0, 0))
        pygame.display.flip()

if __name__ == "__main__":
    run()
