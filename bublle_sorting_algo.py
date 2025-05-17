#Time complexity O(n2) ---- Space omplexity 0(1)
def bubble_sorting(lst):
    for i in range(len(lst)-1):
        swapped = False
        for j in range(len(lst)-1-i):
            if lst[j] > lst[j+1] :
                lst[j],lst[j+1] = lst[j+1],lst[j]
                swapped = True
        if swapped == False : break
    return lst

lst = [ -1, 18 ,2, 3,22, 0, 2, 3, 2]
print(bubble_sorting(lst))
