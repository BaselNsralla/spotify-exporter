

def page(og):
    print("SADASD", og)
    
    def decorated(f, g, d):
        print('OK', g, d)

    return decorated


class Apa:
    @page
    def hi(self):
        print('hi')


f = Apa()
f.hi(2, 3)

a, b = (1,2)

print ( a, b)
