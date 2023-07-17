import pygame
import threading
import os

# TODO: make all effects a visible variable and in pygame is not installed, just pass everything


class Bit8:
    def __init__(self) -> None:
        os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
        pygame.mixer.init()
        self.eaten = pygame.mixer.Sound('./assets/eaten.mp3')
        self.speedup = pygame.mixer.Sound('./assets/speedup.mp3')
        self.gameover = pygame.mixer.Sound('./assets/gameover.mp3')
        self.slowdown = pygame.mixer.Sound("./assets/slowdown.mp3")

    def play_music(self):
        def music():
            pygame.mixer.music.load('./assets/music.mp3')
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(-1)  # Play the music on loop
            while pygame.mixer.music.get_busy():
                continue

        music_thread = threading.Thread(target=music)
        music_thread.start()

    def stop_music(self):
        pygame.mixer.music.stop()
