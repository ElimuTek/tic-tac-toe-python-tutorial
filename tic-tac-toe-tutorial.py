'''
Leo tutatengeneza akili bandia inayo uwezo wa kucheza TIC-TAC-TOE (Noughts and Crosses) vizuri sana.
Programu yetu haiwezi kushindwa / kufungwa na mtu yeyote


VOCABULARY - MSAMIATI

Variable
    Jina tunalotumia kuhifadhi kitu (mfano: majina, namba, maandishi) ili tukitumie tena baadaye. Ona "AINA ZA VARIABLE" apo chini
Loop
    Kipande cha maagizo kinachorudiwa mara nyingi hadi kazi iishe.
Function
    Kikundi cha maagizo kinachofanywa pamoja kwa jina moja (mfano: chapisha_bao()).
Condition / If
    Maamuzi: "Ikiwa jambo fulani limetokea, fanya hivi…"
Input
    Maelezo tunayotoa kwa kompyuta. Mtumiaji anaandika, kompyuta inapokea.
Output
    Jibu au matokeo yanayoonyeshwa na kompyuta.
Comment
    Maandishi kwa binadamu tu — kompyuta hayasomi (yalianza na #)
List / Array
    Kikundi cha vitu vilivyopangwa kwa mpangilio (mfano: bao yetu ina nafasi 9).
Index
    Nafasi ya kila kitu ndani ya list — huanza kuhesabu kwa 0.
Random
    Kuchagua kwa bahati nasibu — bila mpangilio maalum.
Bug
    Tatizo kwenye programu.
Error Handling
    Jinsi ya kusema "pole, kuna kosa, jaribu tena" bila programu kufa.
Return
    Jibu kutoka kwenye kazi (function) — linarudishwa kwa sehemu nyingine ya programu.
True / False
    Majibu ya "Ndiyo" au "Hapana" kwa kompyuta.
Index
    Namba ya kutaja mahali, nafasi katika orodha. Lakini tofauti na orodha za kawaida nafasi ya kwanza kutajwa "0", nafasi a pili ni "1" na kuendelea...

    
DATA TYPES - AINA ZA VARIABLE

List
    Vitu vingi kwa mpangilio (like boxes in a row)
    mf. my_list = [1, 2, 3]
Tuple
    Kama list, lakini haiwezi kubadilika
    mf. my_tuple = (1, 2, 3)
Dictionary
    Vitu vilivyo na jina na thamani
    mf. my_dict = {'a': 1, 'b': 2}
Set
    Orodha ya vitu ambavyo havirudiwi
    mf. my_set = {1, 2, 3}
String
	Msururu wa herufi
    my_str = "hello"    
    
Algorithm (Plain English)

Move 1:
Place an X in a corner.

Move 2:
IF the other player did not place an O in the opposite corner
THEN place an X in the opposite corner to move 1.
ELSE place an X in a free corner.

Move 3:
IF there are 2 Xs and a space in a line
THEN place an X in the free space on that line.
ELSE IF there are 2 Os and a space in a line
THEN place an X in that space.
ELSE place an X in a free corner.

Move 4:
IF there are 2 Xs and a space in a line
THEN place an X in the free space on that line.
ELSE IF there are 2 Os and a space in a line
THEN place an X in that space.
ELSE place an X in a free corner.

Move 5:
Place an X in the free space.

'''

import random  # Tunatumia 'import' kuleta kitu kingine ndani ya programu kama vile uwezo wa kuchagua namba kwa bahati nasibu (random)

# Bao yetu ina nafasi 9 zinazoanza zikiwa tupu. 
bao = [' '] * 9  # Mfano wa LIST (orodha ya vitu vingi kwa mpangilio)

corners = [0, 2, 6, 8]  # Hii pia ni LIST ya kona za bao zikitajwa kwa INDEX. Index huanza 0 badala ya 1 ndo sababu index ya mwisho ni 8 wakati nafasi zipo 9

# Hii ni orodha ya mistari inayoweza kushinda: mlalo, wima na kona
lines = [
    (0,1,2), (3,4,5), (6,7,8),      # mistari ya mlalo
    (0,3,6), (1,4,7), (2,5,8),      # mistari ya wima
    (0,4,8), (2,4,6)                # mistari ya kona
]  # Hii ni mfano wa LIST (orodha) yenye TUPLES ndani yake.
# Tuple ni kama list ambayo haibadiliki.

# Hapa tunatunza nafasi ambazo kila mchezaji ameweka alama zake
moves = {
    'X': set(),  # Seti ya alama za kompyuta
    'O': set()   # Seti ya alama za mtumiaji
}  # Hii ni mfano wa DICT (dictionary: key → value) (kamusi: jina → kitu) na ndani yake kuna SET
# Yaani katika kamusi yetu ukitafuta alama ya mchezaji (X ama O) unapata orodha ya mahali yote alipocheza

# Kazi ya kuchora ubao ili kuona alama zilipo
def chapisha_bao(): #Mfano wa defintion ya function yaani kufafanua 
    print(f"""
 {bao[0]} | {bao[1]} | {bao[2]}
---+---+---
 {bao[3]} | {bao[4]} | {bao[5]}
---+---+---
 {bao[6]} | {bao[7]} | {bao[8]}
""")

# Kazi ya kuangalia kama mchezaji ameweka alama tatu kwenye mstari mmoja
def angalia_mshindi(mchezaji):
    for mstari in lines:
        # Tunatumia SET hapa kuangalia kama alama zote zipo
        if set(mstari).issubset(moves[mchezaji]):
            return True
    return False

# Kompyuta inaweka alama (X) kulingana na hatua ya mchezo
def mpigo_wa_X(hatua, ya_kwanza):
    if hatua == 1:
        chaguo = random.choice(corners)
        bao[chaguo] = 'X'
        moves['X'].add(chaguo)
        return chaguo
    elif hatua == 2:
        kinyume = 8 - ya_kwanza
        if bao[kinyume] == ' ':
            bao[kinyume] = 'X'
            moves['X'].add(kinyume)
        else:
            chagua = random.choice([i for i in corners if bao[i] == ' '])
            bao[chagua] = 'X'
            moves['X'].add(chagua)
    elif hatua in [3, 4]:
        for upande in ['X', 'O']:
            for a, b, c in lines:
                mstari = [bao[a], bao[b], bao[c]]
                if mstari.count(upande) == 2 and mstari.count(' ') == 1:
                    nafasi = [a, b, c][mstari.index(' ')]
                    bao[nafasi] = 'X'
                    moves['X'].add(nafasi)
                    return
        pembe = [i for i in corners if bao[i] == ' ']
        if pembe:
            chagua = random.choice(pembe)
            bao[chagua] = 'X'
            moves['X'].add(chagua)
        else:
            nafasi = bao.index(' ')
            bao[nafasi] = 'X'
            moves['X'].add(nafasi)
    else:
        nafasi = bao.index(' ')
        bao[nafasi] = 'X'
        moves['X'].add(nafasi)

# Hapa ndipo mchezo unaanza rasmi
hatua = 1
ya_kwanza = mpigo_wa_X(1, None)  # Kompyuta inaanza na hatua ya kwanza
chapisha_bao()

# Mzunguko (loop) wa mchezo unaendelea hadi ubao wote ujazwe
while ' ' in bao:
    try:
        # Mtumiaji anaingiza sehemu ya kuweka O
        o = int(input("Chagua sehemu ya kuweka O yako (0 hadi 8): "))
        if bao[o] != ' ':
            print("Sehemu hiyo imeshajazwa. Jaribu nyingine.")
            continue
        bao[o] = 'O'
        moves['O'].add(o)
        chapisha_bao()

        # Tunaangalia kama mtumiaji (O) ameshinda
        if angalia_mshindi('O'):
            print("Umeshinda! 🎉")
            break

    except:
        # Hii ni mfano wa kuzuia KOSA (error handling) kama mtumiaji akiandika kitu kisichofaa
        print("Andika namba sahihi kati ya 0 hadi 8.")
        continue

    hatua += 1
    if hatua > 5:
        break

    # Kompyuta inaweka X
    mpigo_wa_X(hatua, ya_kwanza)
    chapisha_bao()

    # Tunaangalia kama kompyuta (X) imeshinda
    if angalia_mshindi('X'):
        print("Kompyuta imeshinda!")
        break

# Kama nafasi zote zimejazwa na hakuna mshindi, ni sare
if ' ' not in bao:
    print("DRAW! Hakuna aliyeshinda.")
