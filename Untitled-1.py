
f = open('app01\\pixel1.csv', mode='r', encoding='UTF-8')
arr = f.readlines() 
 

def 함수표():
    arr2 = []
    for i in range(0, len(arr)):
        row = arr[i].replace("\n", "")
        arr2.append(row.split(","))                      
    for row in arr2:
        행 = ""
        for v in row:
            행 += 'O' if v == 'O' else ' '
        print(행)

함수표()