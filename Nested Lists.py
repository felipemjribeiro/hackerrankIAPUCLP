from heapq import nsmallest
if __name__ == '__main__':
    mainList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameScore = list((name, score))
        mainList.append(nameScore)
minValueVector = nsmallest(2, mainList, key=lambda e:e[1])
secondValue = minValueVector[1][1]
#print ('Segundo valor:' + str(secondValue))
finalList = []
fimWhile = len(mainList)
while (fimWhile <= 0):
    currentValue = mainList[fimWhile][1]
    print ('Valor corrente:' + str(currentValue))
    print ('Segundo valor:' + str(secondValue))
    fimWhile -=1
    if currentValue == secondValue:
        print(mainList[fimWhile][0])
'''
for i in range(len(mainList)):
    currentValue = mainList[i][1]
    #print ('Valor corrente:' + str(currentValue))
    if currentValue == secondValue:
        print(mainList[i][0])'''
