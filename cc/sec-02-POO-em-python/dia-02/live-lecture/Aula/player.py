from abc import ABC, abstractmethod


class MediaPlayer:
    def __init__(self, player):
        self.__player = player

    def execute(self):
        self.__player.play()

class Target(ABC):
    @abstractmethod
    def play(self):
        raise NotImplementedError

class AudioPlayer(Target):
    def play(self):
        print("Play audio")

class VideoAdapter(Target):
    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def play(self):
        self.__adaptee.play_mp4()

class VideoPlayer:
    def play_mp4(self):
        print("play MP4")

MediaPlayer(AudioPlayer()).execute()
MediaPlayer(VideoAdapter(VideoPlayer())).execute()