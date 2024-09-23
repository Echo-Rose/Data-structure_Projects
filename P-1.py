import time
from idlelib.configdialog import is_int


callcnt = 0
def hanoi_tower(n, fr, tmp, to) :
    global callcnt
    callcnt += 1
    if(n==1) :
        print("원판 1 : %s --> %s" % (fr, to))
    else :
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 %d : %s --> %s" % (n, fr, to))
        hanoi_tower(n - 1, tmp, fr, to)

if __name__ == '__main__' :
    while True :
        try :
            rpt = int(input("하노이 탑의 층 수를 입력해주세요. : "))
            break
        except :
            print("하노이 탑의 층 수는 정수로 입력해야 합니다.")
    start_time = time.time()
    hanoi_tower(rpt,'A','B','C')
    end_time = time.time()
    print("hanoi_tower 함수의 호출 횟수는 %d회 입니다." % (callcnt))
    print("실행 소요시간은 %f초 입니다." % (end_time-start_time))