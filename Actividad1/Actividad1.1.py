class MiExcepcion(Exception):
   def __init__(self,message):
      self.message = message

x=10
assert type(x) == int, "Incorrect input."
print(x)



try: 
    if x > 10:
        raise MiExcepcion
    
except MiExcepcion as e:
    print(e.message)