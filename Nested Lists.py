if __name__ == '__main__':
    mainList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nameScore = list((name, score))
        mainList.append(nameScore)
print(mainList)
for i in range(len(mainList)):
    print(mainList[i][0])