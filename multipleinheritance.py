class birds:
    def feathers():
        print("birds can fly")
class wings:
    def fly():
        print("bird with wings can fly")
class parrot(birds,wings):
    def screams():
        print("parrot screams")
a1=birds
b1=wings
c1=parrot
a1.feathers()
b1.fly()
c1.screams()
c1.feathers()
c1.fly()