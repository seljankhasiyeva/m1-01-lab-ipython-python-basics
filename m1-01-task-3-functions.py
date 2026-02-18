# 3
def numerize(string):
    try:
        return int(string)
    except ValueError:
        try:
            return float(string)
        except ValueError:
            return None
    

def clean(value):
    if isinstance(value, str):
        return value.strip()
    else:
        return value
    
print(numerize("42"))
print(numerize("3.14")) 
print(numerize("abc"))  
print(clean("  hello  "))  
print(clean(42))  
