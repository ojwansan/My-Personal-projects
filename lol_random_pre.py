# -*- coding: utf-8 -*-

import tkinter as T
import random
import time

window=T.Tk()

window.title("롤 랜덤 추첨기")
window.geometry("490x320+200+200")
window.resizable(1,1)

label1=T.Label(window,text="-",  fg="black", relief="solid")
label1.place(x=10,y=10, width=470, height = 260)

#글자덩이
팁 = ["점멸은 F점멸"]
#라인
탑 = ["세트", "피오라", "카밀", "아트", "그웬", "잭스", "사일러스", "제이스", "이렐리아", "아칼리", "레넥톤", "말파이트", "녹턴", "리븐", "쉔", "문도 박사", "나르", "볼리베어", "오른", "리 신", "모데카이저", "다리우스", "클레드", "갱플랭크", "뽀삐", "가렌", "케넨", "나서스", "트린다미어", "렝가", "비에고", "티모", "럼블", "마오카이", "사이온", "블라디미르", "라이즈", "루시안", "베인", "트런들", "퀸", "신지드", "케일", "워윅", "우르곳", "요네", "일라오이", "하이머딩거", "요릭", "탐켄치", "자크", "야스오", "판테온", "신짜오", "초가스", "세주아니", "카르마"]

정글 = ["스카너", "리 신", "신짜오", "비에고", "다이애나", "녹턴", "니달리", "엘리스", "샤코", "케인", "킨드레드", "그레이브즈", "헤카림", "에코", "카직스", "럼블", "피들스틱", "카서스", "뽀삐", "자크", "이블린", "누누와 윌럼프", "마스터 이", "렉사이", "자르반 4세", "워윅", "볼리베어", "탈리야", "올라프", "그라가스", "세주아니", "람머스", "트런들", "바이", "릴리아", "그웬", "우디르", "아이번", "쉬바나", "아무무", "오공", "잭스", "렝가"]

미드 = ["아크샨", "벡스", "사일러스", "르블랑", "제드", "아칼리", "카타리나", "요네", "야스오", "탈론", "트위스티드 페이트", "루시안", "빅토르", "갈리오", "키아나", "비에고", "아리", "카사딘", "이렐리아", "오리아나", "조이", "제라스", "애니비아", "판테온", "라이즈", "피즈", "에코", "세트", "녹턴", "다이애나", "말자하", "블라디미르", "리산드라", "아지르", "럼블", "레넥톤", "신드라", "리 신", "제이스", "카시오페아", "애니", "말파이트", "럭스", "코르키", "아우렐리온 솔", "직스", "누누와 윌럼프", "니코", "아트록스", "베이가", "파이크", "클레드", "카르마"]

원딜 = ["이즈리얼", "카이사", "사미라", "징크스", "아펠리오스", "코그모", "진", "베인", "바루스", "케이틀린", "칼리스타", "트리스타나", "애쉬", "루시안", "미스 포츈", "시비르", "직스", "드레이븐", "자야", "트위치", "야스오", "스웨인", "세나"]

서포터 =["쓰레쉬", "룰루", "카르마", "레오나", "세나", "노틸러스", "유미", "알리스타", "제라스", "블리츠크랭크", "파이크", "모르가나", "마오카이", "럭스", "세트", "소라카", "라칸", "질리언", "자이라", "갈리오", "바드", "잔나", "판테온", "세라핀", "스웨인", "샤코", "브라움", "브랜드", "렐", "나미", "벨코즈", "그라가스", "탐 켄치", "타릭", "소나", "자크", "베이가", "애니비아", "쉔", "니코", "뽀삐"]

라인 = ["탑", "정글", "미드", "원딜", "서포터"]
#챔피언
챔피언 = ["아크샨", "벡스", "가렌", "갈리오", "갱플랭크", "그라가스", "그레이브즈", "그웬", "나르", "나미", "나서스", "노틸러스", "녹턴", "누누와 윌럼프", "니달리", "니코", "다리우스", "다이애나", "드레이븐", "라이즈", "라칸", "람머스", "럭스", "럼블", "레넥톤", "레오나", "렉사이", "렐", "렝가", "루시안", "룰루", "르블랑", "리신", "리븐", "리산드라", "릴리아", "마스터이", "마오카이", "말자하", "말파이트", "모데카이저", "모르가나", "문도박사", "미스포츈", "바드", "바루스", "바이", "베이가", "베인", "벨코즈", "볼리베어", "브라움", "브랜드", "블라디미르", "블리츠크랭크", "비에고", "빅토르", "뽀삐", "사미라", "사이온", "사일러스", "샤코", "세나", "세라핀", "세주아니", "세트", "소나", "소라카", "쉔", "쉬바나", "스웨인", "스카너", "시비르", "신짜오", "신드라", "신지드", "쓰레쉬", "아리", "아무무", "아우렐리온 솔", "아이번", "아지르", "아칼리", "아트록스", "아펠리오스", "알리스타", "애니", "애니비아", "애쉬", "야스오", "에코", "엘리스", "오공", "오른", "오리아나", "올라프", "요네", "요릭", "우디르", "우르곳", "워윅", "유미", "이렐리아", "이블린", "이즈리얼", "일라오이", "자르반4세", "자야", "자이라", "자크", "잔나", "잭스", "제드", "제라스", "제이스", "조이", "직스", "진", "질리언", "징크스", "초가스", "카르마", "카밀", "카사딘", "카서스", "카시오페아", "카이사", "카직스", "카타리나", "칼리스타", "케넨", "케이틀린", "케인", "케일", "코그모", "코르키", "퀸", "클레드", "키아나", "킨드레드", "타릭", "탈론", "탈리야", "탐켄치", "트런들", "트리스타나", "트린다미어", "트위스티드 페이트", "트위치", "티모", "파이크", "판테온", "피들스틱", "피오라", "피즈", "하이머딩거", "헤카림"]   
#정밀
정밀 = ["집중 공격", "정복자", "기민한 발걸음", "치명적 속도"]
정밀1 = ["과다치유", "승전보", "침착"]
정밀2 = ["민첩함", "강인함", "핏빛길"]
정밀3 = ["최후의 일격", "체력차 극복", "최후의 일격"]
#지배
지배 = ["감전", "포식자", "어둠의 수확", "칼날비"]
지배1 = ["비열한 한방", "피의 맛", "돌발 일격"]
지배2 = ["좀비와드", "유령포로", "사냥의 증표"]
지배3 = ["굶주린 사냥꾼", "끈질긴 사냥꾼", "영리한 사냥꾼", "궁극의 사냥꾼"]
#마법
마법 = ["신비로운 유성", "콩콩이 소환", "난입"]
마법1 = ["무효화 구체", "마나 순환 팔찌", "빛망"]
마법2 = ["깨달음", "기민함", "절대 집중"]
마법3 = ["주문 작열", "물 위를 걷는 자", "폭풍의 결집"]
#결의
결의 = ["착취의 손아귀", "수호자", "여진"]
결의1 = ["철거", "생명의 샘", "보호막 강타"]
결의2 = ["사전 준비", "재생의 바람", "뼈 방패"]
결의3 = ["과잉성장", "소생", "불굴의 의지"]
#영감
영감 = ["선제공격", "빙결 강화", "봉인 풀린 주문서"]
영감1 = ["마법공학 점멸기", "마법의 신발", "완벽한 타이밍"]
영감2 = ["외상", "미니언 해체분석기", "비스킷 배달"]
영감3 = ["우주적 통찰력", "쾌속 접근", "시간 왜곡 물약"]

룬 = [정밀, 지배, 마법, 결의, 영감]

스펠 = ["점멸", "점화", "탈진", "회복", "강타", "순간이동", "정화", "방어막"]
def p(stri):
    label1.config(text=label1.cget("text")+"\n"+stri)
def cp(stri):
    label1.config(text=label1.cget("text")+stri)
def subchoice(a, b):
    서파편1 = random.choice(a)
    서파편2 = random.choice(b)
    p(str(서파편1)+"\n"+str(서파편2)+"\n")
def rst():
    label1.config(text="")


p("============================")
p("     롤 랜덤 추첨기      ")
p("============================\n")


time.sleep(0.5)

def f_line():
    rst()
    r라인 = random.choice(라인)
    p("라인 : "+str(r라인)+"\n")
def champ():
    rst()
    r챔피언 = random.choice(챔피언)
    p("챔피언 : "+str(r챔피언)+"\n")
def rune():
    rst()
    #주룬
    main_rune = random.choice(룬)
    if main_rune == 정밀:
        메인룬 = random.choice(정밀)
        파편1 = random.choice(정밀1)
        파편2 = random.choice(정밀2)
        파편3 = random.choice(정밀3)
        p("정밀\n"+str(메인룬)+"\n"+str(파편1)+"\n"+str(파편2)+"\n"+str(파편3)+"\n")
    elif main_rune == 지배:
        메인룬 = random.choice(지배)
        파편1 = random.choice(지배1)
        파편2 = random.choice(지배2)
        파편3 = random.choice(지배3)
        p("지배\n"+str(메인룬)+"\n"+str(파편1)+"\n"+str(파편2)+"\n"+str(파편3)+"\n")
    elif main_rune == 결의:
        메인룬 = random.choice(결의)
        파편1 = random.choice(결의1)
        파편2 = random.choice(결의2)
        파편3 = random.choice(결의3)
        p("결의\n"+str(메인룬)+"\n"+str(파편1)+"\n"+str(파편2)+"\n"+str(파편3)+"\n")
    elif main_rune == 마법:
        메인룬 = random.choice(마법)
        파편1 = random.choice(마법1)
        파편2 = random.choice(마법2)
        파편3 = random.choice(마법3)
        p("마법\n"+str(메인룬)+"\n"+str(파편1)+"\n"+str(파편2)+"\n"+str(파편3)+"\n")
    elif main_rune == 영감:
        메인룬 = random.choice(영감)
        파편1 = random.choice(영감1)
        파편2 = random.choice(영감2)
        파편3 = random.choice(영감3)
        p("영감\n"+str(메인룬)+"\n"+str(파편1)+"\n"+str(파편2)+"\n"+str(파편3)+"\n")
        #부룬
    sub_rune = random.choice(룬)
    if sub_rune == main_rune:
        while True:
            if sub_rune != main_rune:
                break
            else:
                sub_rune = random.choice(룬)
    if sub_rune == 정밀:
        subc = random.randrange(1, 4)
        p("정밀")
        if subc == 1:
            subchoice(정밀1, 정밀2)
        elif subc == 2:
            subchoice(정밀1, 정밀3)
        elif subc == 3:
            subchoice(정밀2, 정밀3)
    elif sub_rune == 지배:
        subc = random.randrange(1, 4)
        p("지배")
        if subc == 1:
            subchoice(지배1, 지배2)
        elif subc == 2:
            subchoice(지배1, 지배3)
        elif subc == 3:
            subchoice(지배2, 지배3)
    elif sub_rune == 결의:
        subc = random.randrange(1, 4)
        p("결의")
        if subc == 1:
            subchoice(결의1, 결의2)
        elif subc == 2:
            subchoice(결의1, 결의3)
        elif subc == 3:
            subchoice(결의2, 결의3)
    elif sub_rune == 마법:
        subc = random.randrange(1, 4)
        p("마법")
        if subc == 1:
            subchoice(마법1, 마법2)
        elif subc == 2:
            subchoice(마법1, 마법3)
        elif subc == 3:
            subchoice(마법2, 마법3)
    elif sub_rune == 영감:
        subc = random.randrange(1, 4)
        p("영감")
        if subc == 1:
            subchoice(영감1, 영감2)
        elif subc == 2:
            subchoice(영감1, 영감3)
        elif subc == 3:
            subchoice(영감2, 영감3)
def f_line2():
    rst()
    r라인 = random.choice(라인)
    if r라인 == "탑":
        r챔프 = random.choice(탑)
    elif r라인 == "정글":
        r챔프 = random.choice(정글)
    elif r라인 == "미드":
        r챔프 = random.choice(미드)
    elif r라인 == "원딜":
        r챔프 = random.choice(원딜)
    elif r라인 == "서포터":
        r챔프 = random.choice(서포터)
    p("라인 : "+str(r라인)+"\n\n챔프 : "+str(r챔프)+"\n")
def spell():
    rst()
    d주문 = random.choice(스펠)
    f주문 = random.choice(스펠)
    if f주문 == d주문:
        while True:
            if f주문 != d주문:
                break
            else:
                f주문 = random.choice(스펠)
    if d주문 == "점멸":
        d주문, f주문 = f주문, d주문
    p(d주문+" "+ f주문+"\n  ")
def tip():
    rst()
    p(random.choice(팁))
def help():
    rst()
    p("")
#button0 = T.Button(window,text="<<",overrelief="solid", command=f_line, repeatdelay=1000, repeatinterval=1000)
button1 = T.Button(window,text="라인", overrelief="solid", command=f_line, repeatdelay=1000, repeatinterval=1000)
button2 = T.Button(window,text="챔피언", overrelief="solid", command=champ, repeatdelay=1000, repeatinterval=1000)
button3 = T.Button(window,text="룬", overrelief="solid", command=rune, repeatdelay=1000, repeatinterval=1000)
button4 = T.Button(window,text="라인+챔프", overrelief="solid", command=f_line2, repeatdelay=1000, repeatinterval=1000)
button5 = T.Button(window,text="스펠", overrelief="solid", command=spell, repeatdelay=1000, repeatinterval=1000)
button6 = T.Button(window,text="도움말", overrelief="solid", command=help, repeatdelay=1000, repeatinterval=1000)
#button7 = T.Button(window,text=">>",overrelief="solid", command=f_line, repeatdelay=1000, repeatinterval=1000)
#button8 = T.Bitton(window,text="팁",overrelief="solid", command=tip, repeatdelay=1000, repeatinterval=1000)
button1.place(x=10,y=280, width=70, height = 40)
button2.place(x=90,y=280, width=70, height = 40)
button3.place(x=170,y=280, width=70, height = 40)
button4.place(x=250,y=280, width=70, height = 40)
button5.place(x=330,y=280, width=70, height = 40)
button6.place(x=410,y=280, width=70, height = 40)

window.mainloop()