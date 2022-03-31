from random import choices, randint
from typing import List

primes = [
    180719956393569173342335705559,
    593619822806491529381518650667, 
    313358760452795548958321724131, 
    507202894214773148855733162583, 
    679546732167469485530511192803, 
    334597826861029662324979074067, 
    255157004849213487546914591347, 
    760382468261066564532647888099, 
    874478525490321244821368616859, 
    405545225500644281223165339823, 
    277169724195026196896606805959, 
    549235707884270577021743876711, 
    780573944993956318596638196647, 
    321487038268170156833409746311, 
    117117450855293162064164497367, 
    685246008555719330078690269651, 
    337045254922426845084510971099, 
    672551987461409124419232218423, 
    600350870542819501728939252883, 
    917576084429646029227875518519, 
    784184325413608425519635943823, 
    797773010057868237441327183799, 
    220141603701562352498938555223, 
    419749293007647378619332968279, 
    167236958246229837399287794183, 
    961243109136061744013501671199, 
    722231176366128957727856755379, 
    999195360850262110864247121347, 
    826233064538602116695579601947, 
    858719795970565531446240843407, 
    133181707226949161339612532803, 
    534895493137809278192531189483
]


def generateRandomPair() -> List[int]:
    global primes
    return choices(primes, k=2)

def generateInitValue(p: int, q: int) -> int:
    n = p * q
    rand = randint(0, n)
    while rand % p == 0 or rand % q == 0:
        rand = randint(0, n)
    return rand