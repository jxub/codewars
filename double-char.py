def double_char(s):
    l = list(s)
    ll = []
    
    for element in l:
        ll.append(element)
        ll.append(element)
    
    doubled = ''.join(ll)
    return doubled