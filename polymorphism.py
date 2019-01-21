class bear():
    def sound(self):
        print("roarrrrr")
class kutta():
    def sound (self):
        print("bhow")
def makemysound(animaltype):
    animaltype.sound()
bearobj=bear()
kuttaobj=kutta()
makemysound(bearobj)
makemysound(kuttaobj)
