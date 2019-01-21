class user:
    name=""
    def __init__(self,name):
        self.name=name
    def printname(self):
        print("name = "+ self.name)
class programmer(user):
    def __init__(self,name):
        self.name=name
    def dopython(self):
        print("programming python")
brian=user("brian")
brian.printname()

diana= programmer("diana")
diana.printname()
diana.dopython()
