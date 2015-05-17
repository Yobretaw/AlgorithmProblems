import sys
import os
import math
from collections import defaultdict, deque
from sets import Set

"""
    Given two words (start and end), and a dictionary, find all shortest transformation
    sequence(s) from start to end, such that:

    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary
    For example,

    Given:

    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]

    Return
      [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
      ]

    Note:
    All words have the same length.
    All words contain only lowercase alphabetic characters.
"""
def find_ladders(start, end, d):
    if start == end:
        return [start, end]

    if not start in d:
        d.append(start)
    if not end in d:
        d.append(end)

    strToComb = defaultdict(list)
    for s in d:
        arr = list(s)
        for i in range(0, len(arr)):
            for j in range(ord('a'), ord('z') + 1):
                tmp = arr[i]
                arr[i] = chr(j)
                curr = ''.join(arr)
                if curr != s and curr in d:
                    strToComb[s].append(curr)
                arr[i] = tmp
    return bfs(start, end, strToComb, [])

def bfs(start, end, strToComb, path):
    curr_level = Set()
    next_level = Set()
    seen = Set()
    path = []
    res = []
    path.append(end)
    mp = defaultdict(list)

    curr_level.add(start)
    while True:
        for s in curr_level:
            seen.add(s)
        for s in curr_level:
            for ss in strToComb[s]:
                if not ss in seen:
                    next_level.add(ss)
                    mp[ss].append(s)
        if not next_level:
            return res
        if end in next_level:
            output(start, end, mp, path, res, seen)
            return res
        curr_level.clear()
        curr_level.update(next_level)
        next_level.clear()
    return res

def output(start, end, mp, path, res, seen):
    if start == end:
        res.append(list(path[::-1]))
    else:
        for s in mp[end]:
            path.append(s)
            output(start, s, mp, path, res, seen)
            path.pop()

start = "hit"
end = "cog"
d = ["hot","dot","dog","lot","log"]
for line in find_ladders(start, end, d):
    print line

start = "hot"
end = "dog"
d = ["hot","cog","dog","tot","hog","hop","pot","dot"]
ret = find_ladders(start, end, d)
for line in ret:
    print line

start = "qa"
end = "sq"
d = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
for line in find_ladders(start, end, d):
    print line


start = "cet"
end = "ism"
d = ["kid","tag","pup","ail","tun","woo","erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now","boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue","fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger","row","won","dan","rum","fad","tut","sag","yip","sui","ark","has","zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana","gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal","lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit","tie","yet","too","tax","jim","san","pan","map","ski","ova","wed","non","wac","nut","why","bye","lye","oct","old","fin","feb","chi","sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan","age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab","jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry","ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask","wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic","boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub","bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp","wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig","era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam","new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog","hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus","oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion","six","ila","lao","mom","mas","pro","few","opt","poe","art","ash","oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw","sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo","hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog","ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind","hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis","hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg","hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear","spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin","nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax","mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our","ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp","hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo","gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen","odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec","leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun","oil","red","doc","moe","caw","eel","dix","cub","end","gem","off","yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup","jab","pea","bug","gag","mil","jig","hub","low","did","tin","get","gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut","bag","mir","sty","lap","two","ins","con","ant","net","tux","ode","stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted","wot","del","imp","cob","way","ann","tan","mci","job","wet","ism","err","him","all","pad","hah","hie","aim","ike","jed","ego","mac","baa","min","com","ill","was","cab","ago","ina","big","ilk","gal","tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip","han","met","hut","she","sac","fed","goo","tee","ell","not","act","gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel","awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor","ace","adz","fun","ned","coo","win","tao","coy","van","man","pit","guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol","arc","lax","aft","alb","len","air","pug","pox","vow","got","meg","zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob"]
for line in find_ladders(start, end, d):
    print line
