
def fab(max):
    n,a,b=0,0,1
    list = []
    while n<max:
        list.append(b)
        a,b=b,a+b
        n=n+1
    return list

class Fab(object):
    def __init__(self, max): 
        self.max = max 
        self.n, self.a, self.b = 0, 0, 1 
    def __iter__(self): 
        return self 
    def next(self): 
        if self.n < self.max: 
            r = self.b 
            self.a, self.b = self.b, self.a + self.b 
            self.n = self.n + 1 
            return r 
        raise StopIteration()

def fabyield(max): 
    n, a, b = 0, 0, 1 
    while n < max: 
        yield b 
        # print b 
        a, b = b, a + b 
        n = n + 1 

def read_file(fpath): 
    BLOCK_SIZE = 1024*10 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return


list = []
list = fab(10)
n = Fab(10)
print(n.next())
print(n.next())
print(n.next())
print(n.next())
print(n.next())
print(n.next())
print(n.next())
print(n.next())
print(n.next())
for n in fabyield(10):
    print(n)

for n in read_file("D:\\1.txt"):
    print(n)