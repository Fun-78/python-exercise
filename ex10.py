def table(base,start,end,inc):
    for i in range(start, end+1,inc):
        print(f'{base} * {i} = {base * i}')
table(2,1,10,1)

#2*1