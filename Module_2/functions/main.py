# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    func_name="Hello, "+name+"!"
    return func_name

def add(a,b,c):
    return a+b+c

def positive(num):
    return num>0

def negative(num):
    return num<0

print(greet("Umar"))
print(add(2,3,4))
print(positive(30))
print(negative(-4))
