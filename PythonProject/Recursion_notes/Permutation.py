def permute(s):
    seen = set()
    if len(s)<=1: # base case
        seen.add(s)
        return list(seen)
    for i, n in enumerate(s): # get the current char from s
        for prem in permute(s[:i]+s[i+1:]): # if i=1 and n=b then permute the leftover char i.e;
                                            # 'ac' this returns 'ac' and 'ca'
            p = n+prem
            if p not in seen:
                seen.add(p)
    return list(seen)



s = 'a'
print(permute(s))