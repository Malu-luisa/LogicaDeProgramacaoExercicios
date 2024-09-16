a, b, c = map(int, input().split())

MaiorAB = (a + b + abs(a - b)) // 2

if MaiorAB < c:
    print(f'{c} eh o maior')
else:
    print(f'{MaiorAB} eh o maior')

    

   
