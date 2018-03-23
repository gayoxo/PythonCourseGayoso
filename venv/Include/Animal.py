class Animal():
    name = 'Amy'
    noise = "Grunt"
    size = "large"
    color = "brown"
    hair = "covers body"
    def get_color2(self, newcolore):
        self.color = newcolore
        return self.color
    def get_color3(self, newcolore=None):
        if (newcolore!=None):
            self.color = newcolore
        return self.color
    def get_color(self):
        return self.color
    def make_noise(self):
        return self.noise
    def get_name(self):
        return self.name


ani=Animal();
print (ani.get_color())
print (ani.make_noise())

class Dog(Animal):
	name = 'Jon'
#	color = 'Brown'
#	def get_color(self):
#		return self.color


dog=Dog()
dog.color = 'white'
print(dog.get_name());
print(dog.make_noise())
print(dog.get_color())
print(dog.get_color2('caova'))
dog.color = 'white'
print(dog.get_color3('granate'))
dog.color = 'white'
print(dog.get_color3())