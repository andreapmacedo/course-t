from abc import ABC, abstractclassmethod, abstractmethod


class Navigator:
    def __init__(self, navigation_strategy):
        self.__navigation_strategy = navigation_strategy

    def build_route(self, departure, arrival):
        self.__navigation_strategy.build_route(departure, arrival)
