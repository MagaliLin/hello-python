def print_rangoli(size):
    list_Alpha = list(map(chr, range(97, 123)))
    n = size - 1
    M = size * 2 - 1
    L = 2 * (size * 2 - 2) + 2
    iMed = int(M / 2)
    for i in range(M):
        if i <= iMed:
            list_Left = [list_Alpha[j] for j in range(n, n-i-1, -1)]
            list_Right = [list_Alpha[j] for j in range(n-i+1, n+1, 1)]
        else:
            list_Left = [list_Alpha[j] for j in range(n, i-iMed-1, -1)]
            list_Right = [list_Alpha[j] for j in range(i-iMed+1, n+1, 1)]
        if i == 0 or i == M-1:
            sPattern = list_Left[0]
        else:
            sPattern = ('-').join(list_Left) + '-' + ('-').join(list_Right)
        iCarter = int((L - len(sPattern))/ 2)
        sPattern = '-'*iCarter + sPattern + '-'*iCarter
        print(sPattern)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
