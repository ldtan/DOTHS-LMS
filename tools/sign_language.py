# [START of Imports]
from enum import Enum
# [END of Imports]

"""

"""
class Finger(Enum):

    THUMB = 1
    INDEX = 2
    MIDDLE = 3
    RING = 4
    PINKY = 5



"""

"""
class Hand(Enum):

    RIGHT = 1
    LEFT = 2    



"""

"""
class Joint(object):

    """

    """
    def __init__(self, x, y, finger, radius=0):
        self.x = float(x)
        self.y = float(y)
        self.finger = finger
        self.radius = float(radius)


    """

    """
    def __copy__(self):
        return Joint(self.x, self.y, self.finger, radius=self.radius)



"""

"""
class HandTrack(object):

    """

    """
    def __init__(self, x, y, hand, radius=0):
        self.x = float(x)
        self.y = float(y)
        self.hand = hand
        self.radius = float(radius)


    """

    """
    def __copy__(self):
        return Hand(self.x, self.y, self.hand, self.radius)



"""

"""
class Skeleton(list):
    
    """

    """
    def __copy__(self):
        return Skeleton([joint.__copy__() for joint in self])


    """

    """
    def __getattribute__(self, name):
        getter_name = '__get_{}'.format(name)
        getter_name = getter_name if getter_name in self.__dict__ else None
        attribute = super(self.__class__, self). \
                __getattribute__(getter_name if getter_name else name)

        return attribute() if getter_name else attribute


    """

    """
    def __setattr__(self, name, value):
        setter_name = '__set_{}'.format(name)
        setter_function = super(self.__class__, self). \
                __getattribute__(setter_name) \
                if setter_name in self.__dict__ else None
        super(self.__class__, self).__setattr__(name,
                setter_function(value) if setter_function else value)


    """

    """
    def __get_x(self):
        return min([joint.x for joint in self])


    """

    """
    def __get_y(self):
        return min([joint.y for joint in self])


    """

    """
    def __get_location(self):
        return min([joint.x for joint in self]), \
                min([joint.y for joint in self])


    """

    """
    def __get_center(self):
        min_x = min([joint.x for joint in self])
        max_x = max([joint.x for joint in self])
        min_y = min([joint.y for joint in self])
        max_y = max([joint.y for joint in self])

        return (min_x + ((max_x - min_x) / 2)), (min_y + ((max_y - min_y) / 2))


    """

    """
    def __get_width(self):
        return max([joint.x for joint in self]) - \
                min([joint.x for joint in self])

        
    """

    """
    def __get_height(self):
        return max([joint.y for joint in self]) - \
                min([joint.y for joint in self])


    """

    """
    def __get_dimensions(self):
        return max([joint.x for joint in self]) - \
                min([joint.x for joint in self]), \
                max([joint.y for joint in self]) - \
                min([joint.y for joint in self])


    """

    """
    def __get_bounds(self):
        min_x = min([joint.x for joint in self])
        max_x = max([joint.x for joint in self])
        min_y = min([joint.y for joint in self])
        max_y = max([joint.y for joint in self])

        return min_x, min_y, (min_x + max_x), (min_y + max_y)


    """

    """
    def relocate(self, x, y):
        copy = self.__copy__()
        x_difference = x - copy.x
        y_difference = y - copy.y

        for joint in copy:
            joint.x += x_difference
            joint.y += y_difference

        return copy


    """

    """
    def resize(self, width, height):
        copy = self.relocate(0, 0)
        (w, h) = copy.dimensions
        
        for joint in copy:
            joint.x = self.x + (width * (joint.x / w))
            joint.y = self.y + (height * (joint.y / h))

        return copy


    """

    """
    def compare(self, other_skeleton):
        pass



"""

"""
class HandTrail(list):
    
    """

    """
    def __copy__(self):
        return Skeleton([hand_track.__copy__() for hand_track in self])


    """

    """
    def __getattribute__(self, name):
        getter_name = '__get_{}'.format(name)
        getter_name = getter_name if getter_name in self.__dict__ else None
        attribute = super(self.__class__, self). \
                __getattribute__(getter_name if getter_name else name)

        return attribute() if getter_name else attribute


    """

    """
    def __setattr__(self, name, value):
        setter_name = '__set_{}'.format(name)
        setter_function = super(self.__class__, self). \
                __getattribute__(setter_name) \
                if setter_name in self.__dict__ else None
        super(self.__class__, self).__setattr__(name,
                setter_function(value) if setter_function else value)


    """

    """
    def __get_x(self):
        return min([hand_track.x for hand_track in self])


    """

    """
    def __get_y(self):
        return min([hand_track.y for hand_track in self])


    """

    """
    def __get_location(self):
        return min([hand_track.x for hand_track in self]), \
                min([hand_track.y for hand_track in self])


    """

    """
    def __get_center(self):
        min_x = min([hand_track.x for hand_track in self])
        max_x = max([hand_track.x for hand_track in self])
        min_y = min([hand_track.y for hand_track in self])
        max_y = max([hand_track.y for hand_track in self])

        return (min_x + ((max_x - min_x) / 2)), (min_y + ((max_y - min_y) / 2))


    """

    """
    def __get_width(self):
        return max([hand_track.x for hand_track in self]) - \
                min([hand_track.x for hand_track in self])

        
    """

    """
    def __get_height(self):
        return max([hand_track.y for hand_track in self]) - \
                min([hand_track.y for hand_track in self])


    """

    """
    def __get_dimensions(self):
        return max([hand_track.x for hand_track in self]) - \
                min([hand_track.x for hand_track in self]), \
                max([hand_track.y for hand_track in self]) - \
                min([hand_track.y for hand_track in self])


    """

    """
    def __get_bounds(self):
        min_x = min([hand_track.x for hand_track in self])
        max_x = max([hand_track.x for hand_track in self])
        min_y = min([hand_track.y for hand_track in self])
        max_y = max([hand_track.y for hand_track in self])

        return min_x, min_y, (min_x + max_x), (min_y + max_y)


    """

    """
    def relocate(self, x, y):
        copy = self.__copy__()
        x_difference = x - copy.x
        y_difference = y - copy.y

        for hand_track in copy:
            hand_track.x += x_difference
            hand_track.y += y_difference

        return copy


    """

    """
    def resize(self, width, height):
        copy = self.relocate(0, 0)
        (w, h) = copy.dimensions
        
        for hand_track in copy:
            hand_track.x = self.x + (width * (joint.x / w))
            hand_track.y = self.y + (height * (joint.y / h))

        return copy


    """

    """
    def compare(self, other_skeleton):
        pass



"""

"""
class Gesture(object):

    """

    """
    def __init__(self, skeletons=None, trace=None):
        self.skeletons = skeletons
        self.trace = trace


    """

    """
    def __copy__(self):
        return Gesture([skeleton.__copy__() for skeleton in self.skeletons],
                [(x, y, r) for x, y, r, in self.trace])


    """

    """
    def __getattribute__(self, name):
        getter_name = '__get_{}'.format(name)
        getter_name = getter_name if getter_name in self.__dict__ else None
        attribute = super(self.__class__, self).__getattribute__(getter_name if getter_name else name)

        return attribute() if getter_name else attribute


    """

    """
    def __setattr__(self, name, value):
        setter_name = '__set_{}'.format(name)
        setter_function = super(self.__class__, self).__getattribute__(setter_name) if setter_name in self.__dict__ else None
        super(self.__class__, self).__setattr__(name, setter_function(value) if setter_function else value)


    """

    """
    def __get_x(self):
        pass


    """

    """
    def __get_y(self):
        pass


    """

    """
    def __get_location(self):
        pass


    """

    """
    def __get_center(self):
        pass


    """

    """
    def __get_width(self):
        pass


    """

    """
    def __get_height(self):
        pass


    """

    """
    def __get_dimensions(self):
        pass


    """

    """
    def __get_bounds(self):
        pass


    """

    """
    def relocate(self, x, y):
        copy = self.copy()


    """

    """
    def resize(self, width, height):
        pass


    """

    """
    def compare(self, other_gesture):
        pass
