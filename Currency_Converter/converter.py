currencyDic = {}

with open('currencyData.txt') as f:
    for line in f:
        # 1. Clean whitespace and skip empty lines
        line = line.strip()
        if not line:
            continue
            
        # 2. Split by tab
        parsed = line.split("\t")
        
        # 3. Defensive Check: Only add if we actually have two parts
        if len(parsed) >= 2:
            currencyDic[parsed[0]] = parsed[1]
        else:
            print(f"Skipping messy line: {line}")

print(currencyDic)