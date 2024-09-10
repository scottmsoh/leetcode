

n= int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
length=len(arr)
W, B = color_paper(arr, length, 0, 0)

def color_paper(arr, l, W, B):
#     if l <= 2:
    if l == 1:
        if arr[0][0] == 0:
            W+=1
            return (W,B)
        else:
            B+=1
            return (W,B)
    else:
        if is_check(arr) == 'W':
            W+=1
            return (W,B)
        elif is_check(arr) == 'B':
            B+=1
            return (W,B)
        else:
            border = l//2
            arr1, arr2, arr3, arr4 = [], [], [], []
            for i in arr[:border]:
                arr1.append(i[:border])
                arr2.append(i[border:])
            for i in arr[border:]:
                arr3.append(i[:border])
                arr4.append(i[border:])
            W,B = color_paper(arr1, l//2, W, B)
            W,B = color_paper(arr2, l//2, W, B)
            W,B = color_paper(arr3, l//2, W, B)
            W,B = color_paper(arr4, l//2, W, B)
            
            return (W,B)
                
def is_check(arr):
    l = len(arr)
    if all(arr[i][j] == 0 for i in range(l) for j in range(l)):
        return 'W'
    elif all(arr[i][j] == 1 for i in range(l) for j in range(l)):
        return 'B'
    else:
        return 0
        
        
