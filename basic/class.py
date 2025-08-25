class HelloWorld:
    def hello(self): # reminder: always add self parameter when you make classes 
        return "hello world"
   
class main:
    he = HelloWorld()
    print(he.hello())
    
main() 