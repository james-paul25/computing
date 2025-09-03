class HelloWorld:
    def hello(self): # method, reminder: always add self parameter when you make method
        return "hello world"
   
class main:
    he = HelloWorld()
    print(he.hello())
    
main() 