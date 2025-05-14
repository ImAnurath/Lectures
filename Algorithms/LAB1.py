# LAB1
class array:
    def a_insert(self, index, value):
        la.insert(index, value)
    def a_delete(self, index):
        la.pop(index)

la = [1,2,3,4,5]
print(la)
array.a_insert(la, 2, 6)
print(la)
array.a_delete(la, 2)
print(la)
#AV