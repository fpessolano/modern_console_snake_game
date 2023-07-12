import pygame
import threading
import os

# TODO: make all effects a visible variable and in pygame is not installed, just pass everything


class Bit8:
    def __init__(self) -> None:
        os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
        pygame.mixer.init()
        self.drop = pygame.mixer.Sound('./assets/pluck.mp3')
        self.levelup = pygame.mixer.Sound('./assets/confirm.mp3')
        self.gameover = pygame.mixer.Sound('./assets/gameover.mp3')
        self.points = pygame.mixer.Sound("./assets/jump.mp3")

    def play_music(self):
        def music():
            pygame.mixer.music.load('./assets/tetris.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)  # Play the music on loop
            while pygame.mixer.music.get_busy():
                continue

        music_thread = threading.Thread(target=music)
        music_thread.start()

    def stop_music(self):
        pygame.mixer.music.stop()
