def double_char(s):
    l = list(s)
    ll = []
    
    for element in l:
        ll.append(element)
        ll.append(element)
    
    doubled = ''.join(ll)
    return doubled

def faster_double_char(s):
    return ''.join(list([x for pair in zip(list(s), list(s)) for x in pair]))
