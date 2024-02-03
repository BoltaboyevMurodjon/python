import random as r
def sonTop(x=10):
    n=0
    komp_int =r.randint(1,x)
    print(f"men 1 dan {x} gacha bir son oyladim shu sonni topa olasizmi: ") 
    
    while True:
        person = int(input("komp oylagan soni kiriting: "))
        n+=1
        
        if person<komp_int:
            print(f"komp oylagan son {person} dan katta")
        elif person>komp_int:
            print(f"komp oylagan son {person} dan kichik")
        else:
            break
    print(f"tabriklaymiz siz {n} martada topdingiz")



def sontop_pc(x=10):
    quyi = 1
    yuqori = x
    while True:
        if quyi!=yuqori:
            pc = r.randint(quyi,yuqori)
        else:
            pc = yuqori
        javob = input(f"siz {pc} son  oyladingiz togri bo'lsa (t) kattaroq (+) kichikroq (-): ".lower())
        if javob == '-':
            yuqori = pc-1
        elif javob =='+':
            quyi = pc+1
        else:
            break
    print("Topdim!!")