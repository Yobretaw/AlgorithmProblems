import sys
import math
import copy
from collections import defaultdict

"""
    You are given a string, s, and a list of words, words, that are all of the same length. Find
    all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

    For example, given:

    s: "barfoothefoobarman"
    words: ["foo", "bar"]

    You should return the indices: [0,9].
    (order does not matter).
"""
def string_concatenation(s, lists):
        if not s or not lists:
            return None

        m = defaultdict(int)
        for word in lists: m[word] += 1

        n = len(lists[0])
        total_len = len(lists) * n
        res = []
        for i in range(0, len(s) - total_len + 1):
            count = 0
            old_vals = {}
            for j in range(i, i + total_len, n):
                curr = s[j:j+n]
                if m.has_key(curr) and m[curr] > 0:
                    # record original value of curr in m
                    if not curr in old_vals:
                        old_vals[curr] = m[curr]
                    m[curr] -= 1
                    count += 1
                else:
                    break

            if count == len(lists): res.append(i)

            # recover old values in m
            for word in old_vals:
                m[word] = old_vals[word]

        return res

s = "barfoothefoobarman"
words = ["foo", "bar"]
print string_concatenation(s, words)

s = "a"
words = ["a"]
print string_concatenation(s, words)

s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
print string_concatenation(s, words)

s = "cxksvbkmmlkwviteqccjhsedjmoyimskmeehhovubiszsodiqhtyaxdlktmuiggukldubzqdjiebyjkpqfpqdsepmqluwrqictcguslddphdyrsowjhbcnsqddmbvclzvqhsksxnhethvnyuxfxzsqpxvdasflscbzumssbbwuluijqhqngkfxhdahvhunjwpgkjylmwixssgizyyhifepigyenttyriebtcogbwftqmcpmcwvhcmsklyxgryxccyvhodiljbbxftjhrerurleejekacheehclvfviqxmnefzowdhswsxcbdmdfvilekzcrukityxyfwmcctwanvdoyptfnbtrnsthoepieoiklwmppkpegssgknmxpfoezilnocxsrfcebqtsdkwjfqppedmvkczjmnzcpwxiebofujyxuwgzpxotdcqnerzteyvwwseauvgoeglyctzrspmvrcjyuiraimwehdfbalretcfxxeppwdnniwnegeeotdsaixdikuodytbxasmwxzlfxzldfstaxmcflfpybdbzzewzylxwmidkjrprjjtgxwnideifjkeiqdjpogncrsmcjetsnnamlpwotftdranhdxytfnvwgkzroukdjmpucnjxscajcqtfptaujwtrguiwouzyhqulddiygjjkbesqyskjofawzisqdrqkjkvnodlwowgrbyhzruihzkezsyrvshhbreqhkbfaymsbmzaftkpvutwotnklutnnydxihcihqcidckkxwzssuogodszzmopmumwbogkhjukleukcufuqvcezxgylunxobvrsbbzkvlxbhiddnzuieyhbeimbxlpzghthksugdrjkznoomkzsiitpqhqquhraqkkbcgjhxstzhjpwtoocxirprjfmqwmhgyikgtrellftwupqldsinlzfwfrmdfvmgfwmyqsmdxhzuwpfbjprwowsvphzuelckjrkbjwejdgdbxkdhzwfnsaljjkdnxixizikigqrmwwnugsdhokxikirtuxjtfibgslozeilagywptbwhmvqwdjszgbsnjutchkdluooaompjooraljypusobvjohdklmuqyogoquaigqwxsjiryclpfjywsdgdpctpqzdivgqbwoapykiypvpuepswsybkcwzsxfbvntylibcglmeciuzojrnesqounppmwshjlgxtjzzumgzwcymlpbrjsfehxtttldfwlcsudrqpzpnbnapfbgovoucnnygadnzqrrkvkckkuanjaeodnfzbzdqpdypgmoydhiysnlehnrsnwjsloropxeeacwjomhuusuohhsqulihjrcuhvixsmdvpbefqnbmhwaodueafnjpellmhulbiqwzscfiqiuxgwomqsmxfvmmhyaqunrcdocvqjfirbiyzwmpoypwtdkcdksxzkacaeasnhbgjlgkhsaxqrvmufoyrjxqvztxdvpscszndfymaamqrhelnvleejxbiqyonpgpihdnpbcpbohuvmfkhtrncoqmgqatfjkpqnffqjutxenuqvhzoyosogeuwhpdqzvipaofjkbiooeejlfzjvrzbytxhidxkyfzavglghtuyzbhlgjwcawdardhcigmgonijvtpdokdnlmatvzxyvdymggqqmcyargmnbbqpnveahhudgtbdwzrehiuwmsyeykrbojqbexelgaomtrrqtiucspyfhxjijajxjcbpbfahfrvyimodwjgpyewhdfrphbmsfnhguhpzakalyoowzunzbjhgqyvxbkrgzyouidtinttnkkkjezjhjsqbslzuvqcvrrrzwkjkgdzsnldtlmdwgtxzewvcpxzgqqhncqzkvackmgexujtbcqcipxmgwlopdvcgndqjdvtpbzoxijamacvrzjxyvnnykpgxuxixucpvddumpvapxxizhhxeukcebjdvimucqjztpvheqivqfdpokosgyxkbipwsbqurcvltquzjcwzkzqyletteqffaubswtonxjasbvrkznljodkbhfunvzsxwvpsrdhqokjpfcceqnqgrckaheoegibceqwvvdljnwyuzcbrsrxlthlcobgwkhyqzwlubyfrvflwimnafknauacickeoteeucrodrvuobikjwxlckyeeyjoctusnawhcpyfhtcvukifgfskpspvrylvtfogfmqhcqpjlrgidopjwiunalltjwpccflhrdrvtgegznocdgnzohposakdwbgagtkxwbtrjzxkoomuuzvkjkadkkhjlpjtittewoxfpwpemdygftsqgttqfcbtrlmbefhbteijbapnfpwkkqcslwjramkuxyveeffzlpkopbevsahdskveigvivhesfcwlhdnstxhkblhtnpyfbwljegrzpysxaqihwxzrxibyvjriasqbobmskfsbdmydejkagmrdutdqevagpsjduvxgarhefihkrukzgcdcxguddvlsnuxjrxrrozvuhfgazqzhuejtlgyqdllsfiewhvqwunsdsydtqfanjmiwujpxuapcktysrqoleirwiwsabupngajcjyzdarflmgddwtradizletninfvwfgyohathrbsdhxjfsaivkjiqcyypdvniemylmrufspkbmthhvpcfanwclwtouhwavunjnhogwyhluqsphwxhjvjutfkpoipjecusmiaiijvcapujmrrxocshhexxnmgrraldklntxlxzarimkzkyceglkfjxtrrkucpeqfznqxmqqufbwrbaxhnhoyfiqwumakqsrsfhrtzhqekoxmouvdckchsufmghyyarqhyhbartebhenxylaavcjnwobeycdytthudiuudavkeljdwkdtopindjrdnudjqlftvznzbklgxvlthqmvfuklgcovysgodlhakwzmjnugifcpvqmbnzovdcqbwzsbkbcvydjhqdpakrphkeixdwuibmjxlbzwddtdgcmxhbxtvpafvleajyikkrkyvluaondwrptastvnivufiafsanengqldbfdrugonxjnqckfkfcrocwiflosufdxikbaejqthzgzcqeoxggnlexqqmkktpjbzkbfwtydtgcvyilxrrlewkwowgapvjruwubsozxjhzgfjrcalpejaazyizodihzedaytbveiwkpgesgphnajpziyyybihdpkfnghlkrhvhnzbwqkjquareyrcczjfqvkebtpmnyjwmkxkajvsfvljucnwbybsunyxjplwnusbgrlicgaieltynjwrhzlbmlzvamtphntngeyjnytrmorbxnufmfiasjwswrkdfdsljqwwrppfgggdtdkhktidcgxyxhdcmyqwqosjekomqxpmaatkvbpxhnyhwdljdbfuszfwjukctzovbjhwnxwwkwdgzppdswzkweihasjtuzoxjywwvsuhoynppfujdvwzaghcbsyxsoubmqzhitoyteqklmwoisqkaxmbpkyhztklllvwhjuapmnazjrhbhrbgffvqdfryrckdzgkjcmapzdqiuzldspjxugpxlgydliikouvsgyjgbzqxacasrjslphkdqiidsqniklbsjkymmpjmtlfkuxxlghowsyzkopvaawtlitzukijdtqppnoavyrsqptcgixgkvbxgxwcjglpzbeqqvrmtigjzbnfknowkrwqostybgnaktraokohuwstyibkvpihgeyxztvabkcldvosfcbbbuxzcajzptgxygwzbrzddbohzcbgheiiyhhchsdylmvlsukuljxrnnymqbsxfchgjoksiqqtcohwirqvdpmsfmevpyuxbbdmrpfzfvujldgtvypaqdsvqwsfwoczrhmiztjgqfqcjyvewmeoqwjiudnqrssizesazdhpjxrsxpytdektctbwzroslgbmmvnlzubitucqjalnevigrmeqfuiqblcnhrbilcqgyuwiukxafhgwtmoagxqhkvxtmabaetgcnfkjpjjurrtmdhnkgfttasmpuqpyjxbzcnirxsoojjcpspbbvuuxpimjydikbjjdwrxvlnlvwokqflrchlaywokussetdnybhxzsmkpkybbgosiwgiwcxgwradmfsmhzkguwsjhtlizbchziswmrcjifowkgitisbcrunanakocmxbxpxjicushiotpxnxrobikoixpunrhlsgcsrlwmdfusylplkgclrmcbkrwzkfkelnyeyuqdznvyamllvnymacnmvllfqymdlkilfaognmgqysbvfbjhextbkhhdftgsfqdmrttgfbwgtzdbdnijmekwntzsoikuypiridaqfyyaybbdommasyxfsyxggjchylyiqayvzywxazcolordookgmhpvstcqgcbxdzseaqbaqfqdvhjjvtqkbhhtajmhnneqoyuopxqhehkzotjmnbyqiflkoztdmzwdaqtpqkyuriwhefvtgtjqywcowyskxonxghoytovmxrtdypwgihyjdazzytkyjzxqioqbcnnbgheeyakihitnltmlmyjwyjogxeizuxbaghfeirprcienbtyqrkmrvaasgktchwdoekuobjffsmsvftlyfxqazquiankjkpxozucddjixxdtcweddevffnznpoayypyopssuxecxbfqgdwjgaglgtmvibvibngseakyaqaxuipalllsorfwksrutpcuelminzgnriklqzlcnwwbpbxzvqvohylllztyaboskadccrgppcsfgrgbhcsrcfcngynhbbbncgqexyvpbnujeamneeegljtsjhbkkcamissiqnxrarcetpsyvyehhabqjcbtgdiovawlqtfqmhxgwrgupmdxoepxistovdeqfdcvyhmloltnczhrnkqcqgzayuquxumfzoayxolozeddfkxswnuovwowqeqqaevctxasmlgnpjrwvootdjhzhxvzdnpgrmimmifavnnkxgiuwwoahxbovwqalhgcworiwyitlxdkenfakvatsbkpzaqkhwpdnillgvfrtkexyjzigcdydnqfpgrxegcroqduliogssfqdfalhglmtbrjjjiormhgckcqsswnmcfrhgcqoochrusbfcrwpyerjjhdbgsqiyhrgmhucjdtfwwmanjpopjxasceyvugvdzbpgvtsapxwlkzbvopmxonqsrqplxkqwlgfibxjquheggfdxwqwmfoewfujegzcuhhclenbbxfjfmncifbumpbiuxtadudxekcprrquqyfwksatzbpltsvnpqovltspdwgwqysgwyehsfcsitfbmdrdthygatxfrdchcuoysshlzlfifmltpcyljxrlsprjuttwpjxkbexdsenzqysidqtopmajbrvwmoudxrpaymdqsspjtjtwbomtameefzctpwxoqmpobugtnxeiizelnqeofjskkugasdoirfyucgqpfuznudzjvfxaqrnbntdiyrqrzrmbxcsdyrsuwterzdurxjskcvscpltqchrbjlgkczgyumrtqlnnufzyduauhwklddmpotbsuhsoulkmxxbtcauhwwbdsnqysdniyoasvugrgqdfneashubftdjnsblneyvcoyumsddatjhjnidueeaxjllemyrtxmxnkszfxfhqopbbxeydladunoybopwlcubooavlfddvsfxrlxuwzxrmnrpchmpliqbwtxhyckuuptldshzrfsfukwwtiogqehoxgvyigucxppahzcygwfaibzbmnjetrttzoriwnmucewldaljxqjfrkjdxsitldmlrfvoshkwnghqhszgilnbvwhvrroeuaplhmbzulxhueabybjimwjkvqhmjvqdxireuufqgcaaiadgbmoqkzafshtbemhduahquohasjcajfimryccxejpndtrpcwlcdbwtkzltbnchxpavtevyqmltffkjbvlhwkajjocmdhvbywyrctpsidnpixzlsksrwvaflcuojprhlqbqlqivtwldtkpowjftefaphugtkxcxpdndwyyrujvpvmdsxklcpntzibusbwpqcdvybupxfmobautyegcwtxvbzpvanlspqoptkhspviswclwjtafnxcqytmaiztarjpmtygkuodstqockqjznnpmgdmqehqxqgjlgrwagbuzrkdbaocobscjxqzeyqbqynegechmddnuosyogaejuiuuzuyzmzrmovutxbfchvzvnzjuzqfwyaqxwqykrqygnsznwgpddoyrnjnpzsnysdxqvyamqysdttqpcgsfwswkbjzdemdyrcpoaraqstulomcquuwroudrgcumqzkjcbxctzvlsryhdazawxrksubayy"
words = ["otftdranhdxytfnvwgkzroukdj","iflkoztdmzwdaqtpqkyuriwhef","lbsjkymmpjmtlfkuxxlghowsyz","cddjixxdtcweddevffnznpoayy","snjutchkdluooaompjooraljyp","fuszfwjukctzovbjhwnxwwkwdg","frmdfvmgfwmyqsmdxhzuwpfbjp","ukityxyfwmcctwanvdoyptfnbt","mhnneqoyuopxqhehkzotjmnbyq","vtgtjqywcowyskxonxghoytovm","wouzyhqulddiygjjkbesqyskjo","mfiasjwswrkdfdsljqwwrppfgg","zruihzkezsyrvshhbreqhkbfay","rsxpytdektctbwzroslgbmmvnl","jdwrxvlnlvwokqflrchlaywoku","xhnhoyfiqwumakqsrsfhrtzhqe","gtbdwzrehiuwmsyeykrbojqbex","tpcyljxrlsprjuttwpjxkbexds","tsjhbkkcamissiqnxrarcetpsy","keiqdjpogncrsmcjetsnnamlpw","rquqyfwksatzbpltsvnpqovlts","tdgcmxhbxtvpafvleajyikkrky","qvrmtigjzbnfknowkrwqostybg","vluaondwrptastvnivufiafsan","rnsthoepieoiklwmppkpegssgk","cyypdvniemylmrufspkbmthhvp","ihcihqcidckkxwzssuogodszzm","chrusbfcrwpyerjjhdbgsqiyhr","wmeoqwjiudnqrssizesazdhpjx","ommasyxfsyxggjchylyiqayvzy","kwntzsoikuypiridaqfyyaybbd","cwjomhuusuohhsqulihjrcuhvi","wxazcolordookgmhpvstcqgcbx","nusbgrlicgaieltynjwrhzlbml","xrtdypwgihyjdazzytkyjzxqio","xfvmmhyaqunrcdocvqjfirbiyz","fuklgcovysgodlhakwzmjnugif","hzhxvzdnpgrmimmifavnnkxgiu","xsmdvpbefqnbmhwaodueafnjpe","xfbvntylibcglmeciuzojrnesq","cnhrbilcqgyuwiukxafhgwtmoa","xkajvsfvljucnwbybsunyxjplw","zuieyhbeimbxlpzghthksugdrj","gbzqxacasrjslphkdqiidsqnik","jxtrrkucpeqfznqxmqqufbwrba","chziswmrcjifowkgitisbcruna","jyzdarflmgddwtradizletninf","pcktysrqoleirwiwsabupngajc","dkenfakvatsbkpzaqkhwpdnill","kbiooeejlfzjvrzbytxhidxkyf","wlopdvcgndqjdvtpbzoxijamac","xsoojjcpspbbvuuxpimjydikbj","faubswtonxjasbvrkznljodkbh","uqsphwxhjvjutfkpoipjecusmi","nawhcpyfhtcvukifgfskpspvry","xkdhzwfnsaljjkdnxixizikigq","zxgylunxobvrsbbzkvlxbhiddn","alltjwpccflhrdrvtgegznocdg","gffvqdfryrckdzgkjcmapzdqiu","hzedaytbveiwkpgesgphnajpzi","wmpoypwtdkcdksxzkacaeasnhb","hsdylmvlsukuljxrnnymqbsxfc","bbbncgqexyvpbnujeamneeeglj","bjhgqyvxbkrgzyouidtinttnkk","pyuxbbdmrpfzfvujldgtvypaqd","cfanwclwtouhwavunjnhogwyhl","plkgclrmcbkrwzkfkelnyeyuqd","ugvdzbpgvtsapxwlkzbvopmxon","msbmzaftkpvutwotnklutnnydx","pdwgwqysgwyehsfcsitfbmdrdt","elgaomtrrqtiucspyfhxjijajx","biqyonpgpihdnpbcpbohuvmfkh","llmhulbiqwzscfiqiuxgwomqsm","mpucnjxscajcqtfptaujwtrgui","gdzsnldtlmdwgtxzewvcpxzgqq","gdtdkhktidcgxyxhdcmyqwqosj","zubitucqjalnevigrmeqfuiqbl","aymdqsspjtjtwbomtameefzctp","kjezjhjsqbslzuvqcvrrrzwkjk","zavglghtuyzbhlgjwcawdardhc","fawzisqdrqkjkvnodlwowgrbyh","vrzjxyvnnykpgxuxixucpvddum","rdutdqevagpsjduvxgarhefihk","ydhiysnlehnrsnwjsloropxeea","hgjoksiqqtcohwirqvdpmsfmev","jyxuwgzpxotdcqnerzteyvwwse","sozxjhzgfjrcalpejaazyizodi","usobvjohdklmuqyogoquaigqwx","tmdhnkgfttasmpuqpyjxbzcnir","quareyrcczjfqvkebtpmnyjwmk","rmwwnugsdhokxikirtuxjtfibg","qsrqplxkqwlgfibxjquheggfdx","rukzgcdcxguddvlsnuxjrxrroz","oomuuzvkjkadkkhjlpjtittewo","wqwmfoewfujegzcuhhclenbbxf","yjogxeizuxbaghfeirprcienbt","qbwoapykiypvpuepswsybkcwzs","lvtfogfmqhcqpjlrgidopjwiun","rwowsvphzuelckjrkbjwejdgdb","jfqppedmvkczjmnzcpwxiebofu","hygatxfrdchcuoysshlzlfifml","gxqhkvxtmabaetgcnfkjpjjurr","zppdswzkweihasjtuzoxjywwvs","hgyikgtrellftwupqldsinlzfw","kckkuanjaeodnfzbzdqpdypgmo","aiijvcapujmrrxocshhexxnmgr","sjiryclpfjywsdgdpctpqzdivg","kuxyveeffzlpkopbevsahdskve","uqvhzoyosogeuwhpdqzvipaofj","gjhxstzhjpwtoocxirprjfmqwm","cwiflosufdxikbaejqthzgzcqe","qeqqaevctxasmlgnpjrwvootdj","ymggqqmcyargmnbbqpnveahhud","ekomqxpmaatkvbpxhnyhwdljdb","zvamtphntngeyjnytrmorbxnuf","uhoynppfujdvwzaghcbsyxsoub","efhbteijbapnfpwkkqcslwjram","koxmouvdckchsufmghyyarqhyh","tthudiuudavkeljdwkdtopindj","nwwbpbxzvqvohylllztyaboska","dccrgppcsfgrgbhcsrcfcngynh","qdpakrphkeixdwuibmjxlbzwdd","ftgsfqdmrttgfbwgtzdbdnijme","ounppmwshjlgxtjzzumgzwcyml","cpvqmbnzovdcqbwzsbkbcvydjh","pbrjsfehxtttldfwlcsudrqpzp","qbcnnbgheeyakihitnltmlmyjw","ztvabkcldvosfcbbbuxzcajzpt","xfpwpemdygftsqgttqfcbtrlmb","hncqzkvackmgexujtbcqcipxmg","ilfaognmgqysbvfbjhextbkhhd","hvqwunsdsydtqfanjmiwujpxua","yqrkmrvaasgktchwdoekuobjff","egeeotdsaixdikuodytbxasmwx","jfmncifbumpbiuxtadudxekcpr","slozeilagywptbwhmvqwdjszgb","kkugasdoirfyucgqpfuznudzjv","pvapxxizhhxeukcebjdvimucqj","bqurcvltquzjcwzkzqyletteqf","cbrsrxlthlcobgwkhyqzwlubyf","mqzhitoyteqklmwoisqkaxmbpk","nbnapfbgovoucnnygadnzqrrkv","ztpvheqivqfdpokosgyxkbipws","auvgoeglyctzrspmvrcjyuirai","yhmloltnczhrnkqcqgzayuquxu","funvzsxwvpsrdhqokjpfcceqnq","vuhfgazqzhuejtlgyqdllsfiew","gmhucjdtfwwmanjpopjxasceyv","vpscszndfymaamqrhelnvleejx","dzseaqbaqfqdvhjjvtqkbhhtaj","zylxwmidkjrprjjtgxwnideifj","nzohposakdwbgagtkxwbtrjzxk","igvivhesfcwlhdnstxhkblhtnp","trncoqmgqatfjkpqnffqjutxen","vwfgyohathrbsdhxjfsaivkjiq","rdnudjqlftvznzbklgxvlthqmv","kopvaawtlitzukijdtqppnoavy","raldklntxlxzarimkzkyceglkf","nakocmxbxpxjicushiotpxnxro","wxoqmpobugtnxeiizelnqeofjs","smsvftlyfxqazquiankjkpxozu","fwksrutpcuelminzgnriklqzlc","nefzowdhswsxcbdmdfvilekzcr","ibvibngseakyaqaxuipalllsor","znvyamllvnymacnmvllfqymdlk","gcvyilxrrlewkwowgapvjruwub","mwehdfbalretcfxxeppwdnniwn","wwoahxbovwqalhgcworiwyitlx","nmxpfoezilnocxsrfcebqtsdkw","engqldbfdrugonxjnqckfkfcro","grckaheoegibceqwvvdljnwyuz","jcbpbfahfrvyimodwjgpyewhdf","rvflwimnafknauacickeoteeuc","gxygwzbrzddbohzcbgheiiyhhc","wcxgwradmfsmhzkguwsjhtlizb","bikoixpunrhlsgcsrlwmdfusyl","ssetdnybhxzsmkpkybbgosiwgi","vyehhabqjcbtgdiovawlqtfqmh","opmumwbogkhjukleukcufuqvce","vjriasqbobmskfsbdmydejkagm","gjlgkhsaxqrvmufoyrjxqvztxd","yyybihdpkfnghlkrhvhnzbwqkj","kznoomkzsiitpqhqquhraqkkbc","yhztklllvwhjuapmnazjrhbhrb","jjiormhgckcqsswnmcfrhgcqoo","rphbmsfnhguhpzakalyoowzunz","igmgonijvtpdokdnlmatvzxyvd","rsqptcgixgkvbxgxwcjglpzbeq","zldspjxugpxlgydliikouvsgyj","enzqysidqtopmajbrvwmoudxrp","naktraokohuwstyibkvpihgeyx","zlfxzldfstaxmcflfpybdbzzew","mfzoayxolozeddfkxswnuovwow","rodrvuobikjwxlckyeeyjoctus","yfbwljegrzpysxaqihwxzrxiby","croqduliogssfqdfalhglmtbrj","gvfrtkexyjzigcdydnqfpgrxeg","xgwrgupmdxoepxistovdeqfdcv","oxggnlexqqmkktpjbzkbfwtydt","pyopssuxecxbfqgdwjgaglgtmv","svqwsfwoczrhmiztjgqfqcjyve","bartebhenxylaavcjnwobeycdy"]
print string_concatenation(s, words)
