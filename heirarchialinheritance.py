class birds:
    def feathers():
        print("birds have feathers")
class parrot(birds):
    def fly():
        print("parrots can fly")
class hen(birds):
    def fly():
        print("hen can't fly")
a1=birds
b1=parrot
c1=hen
a1.feathers()
b1.fly()
c1.fly()
b1.feathers()
c1.feathers()