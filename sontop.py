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
