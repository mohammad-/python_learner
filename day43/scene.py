class Scene(object):
    def __init__(self, desc):
        self.desc = desc

    def draw(self):
        print self.desc

    def getActionOption(self):
        pass

    def getNext(self, action):
        pass


class RoomScene1(Scene):
    def __init__(self, desc, left, right):
        super(RoomScene1, self).__init__(desc)
        self.left = left
        self.right = right

    def getNext(self, action):
        if "1" in action:
            return self.left
        elif "2" in action:
            return self.right
        else:
            return None

    def getActionOption(self):
        return self.getNext(raw_input("1: go left\n2: go right\n>"))



class Last(Scene):
    def __init__(self, desc):
        super(Last, self).__init__(desc)

    def getActionOption(self):
        return None

    def getNext(self, action):
        return None