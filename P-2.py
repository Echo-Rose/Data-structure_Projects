import re
from collections import Counter

class ArrayList:
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def getEnty(self, pos):
        if 0 <= pos < self.size:
            return self.array[pos]
        else : return None

    def insert(self, pos, e):
        if not self.isFull() and 0 <= pos <= self.size:
            for i in range(self.size, pos, -1):
                self.array[i] = self.array[i - 1]
            self.array[pos] = e
            self.size += 1
        elif pos > self.size :
            self.array[self.size] = e
            self.size += 1
        else:
            pass

    def delete(self, pos):
        if not self.isEmpty() and 0 <= pos <= self.size:
            e = self.array[pos]
            for i in range(pos, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            return e
        else:
            pass
    def __str__(self):
        return str(self.array[0:self.size])
list = ArrayList()
while True :
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료, m-사전만들기=>")
    if command == 'i' :
        pos = int(input("입력 행 번호 : "))
        str = input("입력 행 내용 : ")
        list.insert(pos,str)
    elif command == 'd':
        pos = int(input("삭제 행 번호 : "))
        list.delete(pos)
    elif command == 'r':
        pos = int(input("변경 행 번호 : "))
        str = input("변경 행 내용 : ")
        list.delete(pos)
        list.insert(pos, str)
    elif command == 'p':
        print("Line Editor")
        i = 0
        while True :
            if (list.getEnty(i) != None) :
                print("[%2d] %s" %(i,list.getEnty(i)))
                i += 1
            else :
                break
    elif command == 'l':
        filename = 'test.txt'
        linecnt = 0
        f = open(filename, 'r', encoding='UTF-8')
        while True:
            line = f.readline().strip()
            list.insert(linecnt,line)
            linecnt += 1
            if not line: break
        list.delete(linecnt)
        f.close()
    elif command == 's':
        save_filename = 'result.txt'
        w = open(save_filename, 'w')
        for i in range(list.size):
            if type(list.getEnty(i)) != 'str':
                entstr = str(list.getEnty(i))
            w.write(entstr + '\n')
        w.close()
    elif command == 'q':
        print("Line Editor을 종료합니다.")
        break
    elif command == 'm':
        strsplit = input("단어를 분리할 문자열을 입력해주세요. 단어는 공백문자로 구분됩니다.\n")
        strsplit = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", strsplit)
        cntsplitstr = Counter(strsplit.split())
        save_filename = 'dic.txt'
        w = open(save_filename, 'w')
        for key,value in cntsplitstr.items() :
            strsave = key + " : " + str(value)
            print(strsave)
            w.write(strsave + '\n')
        w.close()
    else :
        print("잘못된 입력입니다.")

