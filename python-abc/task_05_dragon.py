# Mixin 1
class SwimMixin:
    def swim(self):
        print("The creature swims!")


# Mixin 2
class FlyMixin:
    def fly(self):
        print("The creature flies!")


# Dragon class using both mixins
class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")

