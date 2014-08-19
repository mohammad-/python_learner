#!/usr/bin/python
import scene


class Maze(object):
    def show(self):
        pass


class RoomMaze(Maze):
    def __init__(self):
        room3 = scene.Last("You are dead")
        room2 = scene.Last("You are Winner!!")
        self.room1 = scene.RoomScene1(
            "You are in a room with Beer",
            scene.RoomScene1("Your are in front of Tiger",
                             room3,
                             scene.RoomScene1("You are in front of Elephant",
                                              scene.RoomScene1("You are in front of Lion",
                                                               room3,
                                                               room2),
                                              room3)),
            room3
        )

    def show(self):
        self.room1.draw()
        n = self.room1.getActionOption()
        while n is not None:
            n.draw()
            n = n.getActionOption()

