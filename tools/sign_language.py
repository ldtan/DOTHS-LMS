class Joint(object):

    def __init__(self, x, y, finger, acceptance_radius=0):
        self.x = x
        self.y = y
        self.acceptance_radius = acceptance_radius


    def __copy__(self):
        return Joint(self.x, self.y, acceptance_radius=self.acceptance_radius)



class Skeleton(object):

    def __init__(self, joints=None):
        self.joints = joints


    def __copy__(self):
        return Skeleton([joint.copy() for joint in self.joints])


    def __x(self):
        return min([joint.x for joint in self.joints])


    def __y(self):
        return min([joint.y for joint in self.joints])


    def __width(self):
        return max([joint.x for joint in self.joints]) - \
                min([joint.x for joint in self.joints])

        
    def __height(self):
        return max([joint.y for joint in self.joints]) - \
                min([joint.y for joint in self.joints])


    def __dimensions(self):
        return max([joint.x for joint in self.joints]) - \
                min([joint.x for joint in self.joints]), \
                max([joint.y for joint in self.joints]) - \
                min([joint.y for joint in self.joints])


    def __bounds(self):
        min_x = min([joint.x for joint in self.joints])
        max_x = max([joint.x for joint in self.joints])
        min_y = min([joint.y for joint in self.joints])
        max_y = max([joint.y for joint in self.joints])

        return min_x, min_y, (min_x + max_x), (min_y + max_y)


    def __getattr__(self, name):
        if name == 'x':
            return self.__x()

        elif name == 'y':
            return self.__y()

        elif name == 'width':
            return self.__width()

        elif name == 'height':
            return self.__height()

        elif name == 'dimensions':
            return self.__dimensions()

        elif name == 'bounds':
            return self.__bounds()

        else:
            return super(self.__class__, self).__getattr__(name)


    def relocate(self, x, y):
        copy = self.copy()
        x_difference = x - copy.x
        y_difference = y - copy.y

        for joint in copy.joints:
            joint.x += x_difference
            joint.y += y_difference

        return copy


    def resize(self, width, height):
        copy = self.relocate(0, 0)
        (w, h) = copy.dimensions
        
        for joint in copy.joints:
            joint.x = self.x + (width * (joint.x / w))
            joint.y = self.y + (height * (joint.y / h))

        return copy


    def compare(self, other_skeleton):
        pass



class Gesture(object):

    def __init__(self, skeletons=None, trail=None):
        self.skeletons = skeletons
        self.trail = trail
