class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()
    
    def __missing__(self, key):
        print(f"YOU WANT {key}? IT AINT HERE!!!!!")
    
    def __setitem__(self, key, value):
        print("UGH.... WHY ARE YOU CHANGING STUFF")
        print("OK.... FINE")
        super().__setitem__(key, value)
    
    def __contains__(self, key) -> bool:
        print("NO IT AINT HERE")
        return False
    
data = GrumpyDict({"abc": "egf"})
print(data)
print(data['qdwqdw'])

data['qqwdq'] = 'qwdqwd'
print(data)

print("abc" in data)