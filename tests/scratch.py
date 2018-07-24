class CList(list):
    def __copy__(self):
        copy = CList()
        [copy.append(i) for i in self]
        return copy


c_list = CList()
c_list.append(1)

print c_list.__copy__()