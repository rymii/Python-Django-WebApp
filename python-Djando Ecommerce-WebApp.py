

class Animal:
    def talk(self): print('i have sth to say')
    def walk(self): print('Hey! i am walking here')
    def clothes(self): print('I have some nice clothes')


class Duck(Animal): #class
    def __init__(self, value): #construtor =initialises data
        self._v = value


    def quack(self): #function with argument = method
        print('Quacck', self._v)

    def walk(self):
        super().walk()
        print('walk like a Duck.', self._v)

class Dog(Animal):
     def clothes(self):
         print('ive brown and white fur')

def main():
    donald = Duck(55) #object donald
    print(donald)
    donald.quack()
    donald.walk()
    donald.clothes()

    findo = Dog()
    findo.walk()
    findo.clothes()

if __name__ == '__main__': main()
