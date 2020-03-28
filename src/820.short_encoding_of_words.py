from typing import List
import collections
from functools import reduce


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """后缀排序666"""
        N = len(words)
        # 逆序字典序排序
        words.sort(key=lambda word: word[::-1])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].endswith(words[i]):
                # 当前单词是下一个单词的后缀，丢弃
                pass
            else:
                res += len(words[i]) + 1  # 单词加上一个 '#' 的长度

        return res

    def minimumLengthEncoding1(self, words: List[str]) -> int:
        words = list(set(words))  # remove duplicates
        # Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        # defaultdict 如果获取的键不存在, 为该键赋值为Trie
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        # reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        # reduce结果返回字典树后面的节点,如果是叶子节点(即不是其他单词的后缀), 返回空defaultdict
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        # Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if not nodes[i])

    def minimumLengthEncoding2(self, words: List[str]) -> int:
        """
        可以得到结果字符串和索引的朴素方法, 但超时了
        开始也想到后缀字典树,但是对索引保存不方便
        """
        # 后缀 逆序读取字符 变前缀
        # 取最后一个字符最多的做后缀 -> 取最后第二个字符最多做后缀 -> 直到只剩一个字符串
        result_idx = [-1] * len(words)
        idx_set = set(range(len(words)))

        stack = []
        result_str = ''

        def recursion(idx_list, last=-1):
            if not idx_list:
                nonlocal result_str
                top = stack.pop()
                result_idx[top] = len(result_str)
                result_str += words[top] + '#'
                idx_set.remove(top)
                while stack:
                    i = stack.pop()
                    idx_set.remove(i)
                    result_idx[i] = len(result_str) + len(words[top]) - len(words[i])
                return
            char_map = {}
            for i in idx_list:
                if not words[i][last::-1]:
                    stack.append(i)
                    continue
                last_char = words[i][last]
                if last_char not in char_map:
                    char_map[last_char] = []
                char_map[last_char].append(i)
            if char_map:
                max_key = max(char_map, key=lambda _i: len(char_map[_i]))
                next_list = char_map[max_key]
            else:
                next_list = []
            return recursion(next_list, last - 1)

        while idx_set:
            recursion(list(idx_set))

        return len(result_str)


if __name__ == '__main__':
    solution = Solution()
    assert solution.minimumLengthEncoding(["time", "me", "bell"]) == 10
    print(solution.minimumLengthEncoding(
        ["efgqfm", "ogxdos", "xdxbi", "fjobqq", "mgpshz", "saizjl", "vpfmdm", "gzkhz", "civroxe", "xkxtmwb", "owlnxrg",
         "ruwnez", "dwprr", "muhjuud", "vhwyn", "krlcvz", "vemdlza", "cfdghh", "dvniuv", "upkdvm", "zyqtbly", "tghnuzt",
         "chjofmu", "zccss", "pfwlu", "qoaillf", "ghiznav", "iawpzmv", "owfokk", "wegmo", "gumqmw", "ihuyp", "ojihril",
         "lblkwq", "rliikv", "onfym", "tfqfap", "xvdqmef", "ftyio", "mfjktkp", "llyjo", "kffca", "sjhjew", "rkfyg",
         "mtrrvd", "hynfmnh", "yzdur", "gwclea", "rtakg", "bevnpwx", "sccezb", "esrrbm", "xatkpo", "inmzzxk", "rofikuz",
         "ybsuht", "cepkhi", "joezf", "lghhyku", "mcbiwwv", "ofwdo", "kaouaak", "iieikug", "dkraeu", "rscyq", "mnclbsm",
         "snjleeo", "cjzvrxq", "ncibcfy", "onxtg", "gyhrdgn", "awoueg", "swbgtn", "oyjls", "oaujiog", "vpsvy",
         "aschfai", "flqic", "kbkzgq", "bqxxlmc", "ksujjtz", "zosngh", "fqzzozm", "ahxcpha", "sdjoqh", "dkbaqz",
         "wixjsv", "depttml", "tykblzi", "ulmtjux", "vgoyfw", "xexznab", "ixgyy", "ojsiktz", "cpbht", "xjublp",
         "zmnaiq", "ezjps", "nngbueg", "buihyz", "piljtb", "ismbz", "ymylvez", "tslrf", "spszkf", "wnuit", "tdehea",
         "oapgle", "roshlp", "lhkhnm", "zgfzia", "kxpzpv", "uipgaj", "aiigfae", "xoualf", "ebsaeis", "yxtng", "toxlqt",
         "ybnroj", "hodpva", "diwuag", "icspds", "xstjgeo", "axtvkp", "abquii", "msswem", "lbkfrav", "oojaq", "lcdztoj",
         "lptmb", "aawfirc", "hvtcoc", "ojwsvg", "ggdaddf", "skvwd", "boquzw", "vlvtgzy", "runiq", "cecsy", "mkbmh",
         "usornb", "pqcilnn", "hejdtxq", "iynqeh", "dzkxw", "sqafhvf", "uktza", "yxnajvl", "rvxkxcc", "dhsvpya",
         "evtsek", "mbawnr", "ndcmrhq", "bfxza", "msciyz", "crjxypr", "mmkmxzk", "ezcmqwl", "axgiong", "iboqctn",
         "dyhjyn", "swvsdgg", "nnrlwx", "oelnj", "ldhvhp", "mcqup", "cyvusme", "akxtom", "rqdknqn", "fxfvy", "tegooq",
         "ftwrwjt", "ayksp", "lnlpn", "mrwggcx", "eapai", "ehufraf", "dgblr", "anpcgrm", "rkjcb", "dxwhy", "zuohh",
         "mbbyil", "lufxt", "necsjcd", "jcwkz", "zyioq", "xtxxug", "eusgd", "ssilf", "muzbve", "opdxni", "ukwda",
         "xltxk", "qgkdrbj", "elyaf", "yybuxwi", "zcrvcz", "zbcpkae", "irpupw", "cdobf", "rkhdlkk", "cztgt", "wppal",
         "jrpgnu", "adqiktv", "qtgdyh", "gtijde", "zjgoqi", "fqbzyr", "hchchkg", "atorkfz", "kxpnqq", "sfijywt",
         "wwlfh", "qgxnr", "fiefka", "wrnfspi", "jqczpe", "cqigerg", "tmfnt", "jzbelwo", "vvhoq", "lridtrp", "ozffx",
         "lwajgvu", "zzyuyyu", "iityqku", "yffpe", "akvomp", "eeesjcu", "obmbwy", "yjuaxl", "mjbxfz", "zuggr", "dyhjaq",
         "lfxob", "cgckgji", "fxjmztt", "zjazymd", "qfoxe", "gocbyt", "sitjwt", "spztsw", "huifp", "rfocc", "osfbdf",
         "viswpr", "ajqdaam", "uqsxca", "cygnl", "gokespb", "asfzdm", "udsbfsi", "acppzq", "nwqibz", "ejxmb", "mssls",
         "oxpyuo", "ikrqc", "cptwagk", "mizvrw", "yokyjcx", "gmezru", "lcpzzr", "kwqelgq", "axvvo", "zsryr", "yqslymw",
         "lkdix", "qfruzzi", "vamrdxt", "sxybbc", "chhikkb", "ejeupvl", "nwegr", "dlgjwij", "kvcgo", "juigvb", "rxtym",
         "gtngdc", "tbfcxz", "gjnzgbv", "qoqrrf", "xjply", "rnucw", "zgjbe", "ilvjllb", "gzetpb", "kiphb", "bqmpfzo",
         "xmjztg", "bfkyp", "ymrqo", "tibage", "npsbsf", "cifzjrq", "waykpxf", "nzhoe", "hofgx", "iqtpzxq", "hmdzodq",
         "hcoxu", "bsdquuk", "rmrnnzg", "djpvyso", "jvslwvk", "jqgdgzu", "duudh", "bgbowsp", "rkzso", "wkbgsq",
         "ologrr", "uwbirum", "smxzirx", "ibvqb", "wwjxspk", "gfylju", "rwedg", "yctfiev", "ndgbam", "zbapn", "vwgvka",
         "vklcba", "oreup", "dyvmwzm", "fcdnpms", "chipig", "djqqh", "evpjjj", "dxwewu", "xmnvk", "ditkjeq", "rrxzgns",
         "finvmu", "uthxon", "pogii", "vxofdgm", "hpfubxd", "nkybpt", "fbepu", "qeaynhk", "ihpcdfn", "lbrzum",
         "oegbzbp", "tatjj", "fyhva", "xscyxu", "jpacatw", "carbii", "kixehfg", "jcegy", "qhmjri", "jbgenzo", "qnarvx",
         "hzqcxsy", "abgis", "fhxgk", "exoxue", "vnpjj", "bmcfj", "pcrmdx", "ccrfsk", "wmlfzko", "icharxs", "obpbsla",
         "caezp", "tmvain", "njeqhc", "dwbdaq", "rkaabl", "paxaz", "uclwdym", "edarm", "hovmbl", "cvvpymm", "ipjll",
         "xbhxju", "wqtrh", "nmeyt", "ippyroc", "rxbzu", "kavkm", "kluhic", "pvrbu", "tltnuog", "eujgle", "cfiiadc",
         "gjmwwo", "vqdfoid", "wlcaw", "drxmr", "qyilsd", "bxglh", "vuacik", "pxytivc", "tzsmz", "pvikup", "zgjhrlh",
         "fdkcv", "qmbnk", "joncd", "stwbf", "tqzmr", "mghge", "ifuab", "uxatrvk", "bmvamx", "tchaf", "nbjrmk",
         "gxcejfj", "pobdc", "ebxcglu", "kvifnmi", "kpomc", "uprpjx", "moiyri", "iqpgn", "cekdmjg", "pmonrbs",
         "svhztma", "cgceq", "zufzvp", "ckwkau", "ipvxq", "bklgjoi", "ewqnq", "ygyco", "njinbv", "yudpj", "zxfgcle",
         "knizkhj", "ftdrcd", "evagowr", "mgrqte", "bhyfc", "vgtwoqh", "qntvnvl", "mafwbx", "jypbnoo", "trdsxph",
         "ecozj", "gcqchpf", "lizzc", "etyqknh", "dwwmdwt", "doiket", "kgqys", "chaaj", "hbsgukm", "wzrtw", "zcrhad",
         "dfavyzx", "lyyqlz", "ioqseut", "mlbpdug", "plkhq", "emszn", "yrffuhe", "mzwei", "lorrdo", "hcexb", "zdejjgq",
         "tgfpag", "midozjt", "edxgf", "spbdu", "ktsds", "caaxd", "mlfzvx", "mrsaa", "oilra", "rofamti", "dqswfw",
         "lrmdmwq", "ieomn", "wldwp", "vrshs", "dsshr", "nobzwut", "lixvhhw", "fgfqbyz", "tewrodw", "tkaevb", "ercjfzn",
         "soqgofi", "pilzv", "jrzse", "lsucujp", "thptepp", "gpiunmq", "ygajdm", "uzqdhu", "yfxwpba", "sfblc",
         "aktfvra", "seeavik", "ldhha", "yuior", "nmbbeed", "eiigrwy", "meoumeb", "ynobt", "adudpbl", "zjysp", "wrbah",
         "mtypj", "brkkro", "eppsdy", "xvqlp", "bpijjl", "pontdd", "vsijw", "bolmrsz", "acjkp", "alwgnp", "ilmvsl",
         "joumcf", "mdijnc", "uwsno", "fdqcqzx", "ryzsv", "vxhhbuo", "wxuzh", "mvocus", "ixazxsc", "gixyvg", "mzxazfb",
         "mufoh", "xdjfqa", "ovcmtlg", "wzsdmo", "gwezvkc", "iceufl", "lupecla", "ckukx", "kqlujv", "mahapwq", "mtugo",
         "hihbdpe", "kdcyk", "emybpv", "hbjyb", "fvymuit", "nlrobdj", "bgwjag", "hzyta", "xcyoc", "gckvqp", "hgdoi",
         "wwvoe", "jqgxw", "zllvvh", "cbhiffx", "kvhah", "lzwon", "mnwjfy", "vikumv", "ysmet", "loyxqm", "nelcy",
         "evzkpud", "ddmds", "fusudo", "dvqpuol", "vrxehaa", "ofegfnf", "skikojr", "tirsux", "kjfzfa", "fzahy",
         "gzgicma", "llkrbi", "uhirc", "smtqy", "ojycw", "aaideq", "lbjuaa", "lstke", "opbfup", "fsknk", "iqstk",
         "sbxuaq", "wibnhu", "edmxnrc", "tegid", "yawuril", "csksm", "plkah", "wlhqxp", "dvrlsqh", "pdnqj", "qcybnw",
         "wfljyd", "jxcezdw", "dlyqzpi", "cpjmh", "amdrqsv", "dmlvjtk", "emosv", "qhhun", "tvgcu", "clwwwmg", "jeyabfj",
         "hvwoj", "vvubbox", "nluew", "ohqbqby", "mfizpj", "ynrcpqv", "ybywbu", "evjiyt", "mmzju", "wqqakp", "dpqfq",
         "fbrehw", "vxgivv", "wusqxev", "pdxny", "fszoik", "hohun", "jrqhx", "zlvjzoe", "ywyaugm", "xhkissw", "xphpewx",
         "yqpydw", "uhcjh", "mefjvdm", "eyrthz", "chmub", "zvgbe", "vytdqcn", "ojrvkbd", "bntjv", "izbzvc", "opdbhrf",
         "uetvp", "vmlcoc", "oljir", "modpb", "iintzw", "afrbuey", "kafsfu", "juhxpco", "cdoqv", "yfinfw", "cjoerf",
         "sfxffn", "hwlvc", "ejoaht", "rsaec", "zanxde", "irfdrp", "rapxf", "pdxucj", "bvkxeu", "gkfyrk", "aouebj",
         "mhssbk", "ttimkgj", "yfshksu", "lfaimff", "eapxxt", "njowvl", "wzrga", "tbhpp", "yeuhx", "xnskf", "mxord",
         "uqldj", "gwwbp", "qyqnw", "txisky", "iobnq", "wihlh", "eywsagd", "dhedixr", "ufvya", "avkjdpx", "jjaxuw",
         "cbazlfw", "nbcwdn", "wwmxsl", "qifelvu", "yijlx", "ygqkpd", "jvnndz", "kycvgir", "rtbbra", "vzcet", "ksealjh",
         "ykafa", "isgxhl", "uguld", "zvcsvx", "xdmlvcv", "tnwnm", "fnbaa", "hgfxgw", "qyaaup", "ldetxyr", "xooyh",
         "ntxhyrt", "gsifnj", "phopxd", "nfmtt", "oazvkjy", "ubpxo", "cxpai", "utlsid", "hbbhnky", "ikwliw", "tvmil",
         "mpjqbr", "yqvoq", "rvwklv", "mdjbjku", "nvnrvm", "yfyivq", "wwxmwmz", "mzptc", "uzrlax", "rxzrd", "cchhao",
         "naqdeb", "wdqraw", "yrgkd", "ofjxvkx", "cagxu", "uyzbi", "zgziwys", "dkyppk", "pgzbvi", "qnbpdo", "mthonmj",
         "ipiuuh", "svajedq", "idmks", "nnfhl", "rincnhw", "kteryc", "hzebp", "wktrjel", "netwdj", "zrplpur", "gattw",
         "cwchj", "jypvs", "cgrask", "xaatd", "jyhwplp", "gxcosnz", "cxvva", "pogvym", "dkuxw", "quulof", "xskpa",
         "rmoojme", "varcige", "fiuru", "fzlxh", "lewjpy", "oxxkrga", "xjbzcl", "ktuwzbv", "zhnyssa", "zepnlpn",
         "odtjy", "pbbnpwr", "neeghy", "rwfus", "siwzedi", "xdrig", "unleao", "knpmmtd", "athzbg", "uyfhquf", "btuuk",
         "nxrnntd", "gfkxyf", "ayrlqnq", "qcqrla", "vsukky", "jkdtovo", "crbbbg", "klffh", "xhggw", "pdxpuzg", "pwcrr",
         "nvzde", "lwlnl", "xerxp", "kkjhvlf", "hmjtj", "dihawt", "lmycno", "dcmsb", "bdvawf", "egcmfvq", "vbxrzhy",
         "guufur", "wgbnzhp", "dvngam", "mhbays", "mseabv", "ylrtt", "xlwcwkb", "cpxvnz", "vohhb", "atbcq", "beyltc",
         "gsmzzdg", "tysygan", "qasti", "emwaiuz", "tcyedi", "txaft", "dfqldeh", "xarnfa", "huyuask", "linfesd",
         "rukibrl", "ikxqk", "grdrpue", "njesz", "rkwaaf", "meoiw", "dnqjb", "ymaavc", "jvhepci", "psvat", "rgioosm",
         "euvwrm", "oeqzqfm", "pxtnys", "aijyrye", "ytihpp", "airvc", "crbhu", "cnftvti", "upomq", "wnmgox", "lcrsbmu",
         "nnaldo", "kwowlf", "teugrn", "xergbh", "adoicam", "kmftcu", "adstkbq", "iuhot", "tzxxmj", "qyqpj", "uoyxo",
         "mzvinv", "jmlnct", "vvtuh", "nwynh", "dawarp", "tdtri", "qbcqk", "kgrrzdu", "cilme", "sbhszxb", "pxkvkz",
         "jnqcnmf", "mogsc", "bfztog", "luacdv", "nqmbjuz", "eeouhm", "wjukb", "pexthga", "cybup", "pcmjy", "iovgm",
         "uphupx", "osxbkyg", "hwyhe", "iynfyp", "zbhmnsn", "mvfjxz", "fvsmj", "zvgrjf", "rgjvi", "ugvnwd", "ycoio",
         "heeumz", "lakaa", "puiym", "qokgqz", "kkqdsfd", "jilgod", "dkibwqa", "brvmdi", "fvxfh", "losnzph", "fdmhgnm",
         "tsfrwmp", "vhngai", "yditlzw", "ovskte", "hydfz", "xxacmvl", "wbvvife", "mqwlloc", "pwwnfb", "uxexg", "fdnbr",
         "pgjrelz", "flsfe", "ofhuab", "srowx", "vhgukvr", "vgncsps", "njekves", "lxqxf", "cfjwd", "krfvm", "hmdhm",
         "pyezdj", "kozotes", "yfvjulb", "vtjtb", "fboro", "zlqvrt", "fepyhqv", "ggjlnqf", "ykgjf", "onnry", "bqnqo",
         "jcqqjt", "qagkc", "fpcgch", "vvohk", "hkakrcd", "jjcssk", "uqgxb", "qsosblq", "hrlddg", "pcdmhyr", "obzfaks",
         "wkjsw", "vbsiyv", "utrhsg", "oifyes", "rpwbxd", "rplxwz", "tkise", "fllxeqj", "xayvt", "btdvpt", "paezt",
         "hnvby", "whnwtyn", "oscdals", "ohqlar", "xzmzt", "cnyrkkr", "tlfebvv", "giomsr", "rxfbu", "boehdgp", "gzgqv",
         "nbizukq", "suqgbr", "vhyvndv", "zzgsp", "wqarab", "fgxamho", "eribqcr", "viqefvw", "aacmmed", "boefde",
         "nvuof", "bwpiyo", "vdsss", "wnlzoz", "mzxczby", "kobalmu", "mrtwlzg", "eglggc", "vcaxnbp", "rizhub", "kpriab",
         "qjwjlme", "wljyg", "qkqhl", "kunbeq", "ptxknt", "qfzzkxb", "gpdkb", "jprhdfe", "frbyruu", "egwvk", "fcvafhg",
         "ouuytly", "vkdgd", "aerfwb", "wocctzl", "ulylhw", "qslpvo", "fldda", "afucto", "vdynje", "poeavob", "vksozvz",
         "kbbfmg", "uzuookk", "fnuhu", "pylkqb", "wracvj", "xzqhdh", "rirnakd", "tnyltta", "pslhcry", "dcnme", "lppana",
         "ccjwoy", "nfyvufl", "yjetwst", "ckxfv", "hplkylq", "zxcdxor", "zwxifoi", "codwq", "fcmlpu", "cxvyb",
         "dfqhufm", "rcnmxv", "aznps", "xtdyd", "wjocedy", "ndwavej", "feqpk", "gbnzto", "txcrrx", "ihbiwp", "beqtzxs",
         "vueidoq", "ifrpzq", "dxncw", "kddhzim", "qwppy", "npuovk", "lqbmwv", "ccaqu", "mkdjoz", "hpyjn", "zcmgal",
         "pzdhiv", "arwkqck", "ckqht", "jlebetj", "utoiq", "ngjgu", "didczt", "iuqky", "lfciygp", "kafapjl", "zfgpwad",
         "nmqtos", "tcqcku", "hjkicx", "qlyez", "pgsjk", "eyrwt", "nevbs", "hwxxhp", "anbcarr", "nfwfbfv", "hgoxlxx",
         "qcmpsxn", "btnnwa", "dodrod", "rlxarzm", "qqmat", "uhaxjm", "hznwxfz", "gsqgjk", "eqqanfu", "tpgvfbe",
         "vawbtm", "scrajf", "hjrisw", "onguox", "rtdjyf", "izunw", "fytjtpc", "orqqw", "oeksmj", "oiscpl", "yoapkn",
         "idxbwi", "evady", "ixvla", "zmusgil", "xzfmtz", "vxgecfm", "udsjnq", "bgtlgy", "dwtnntf", "ippth", "kzxkdqv",
         "ffyuzcf", "nczvi", "xvulm", "vezng", "qbqvmrf", "okdkklw", "tjcfl", "mtdcjyc", "pdgodr", "azodyuf", "ifshu",
         "lleqvn", "lfsdn", "exexrm", "cqkhy", "chctxe", "ptiet", "glwixxy", "xdlbt", "tsmwcw", "jkgwwq", "nmajvnr",
         "sgjebrb", "olzdt", "knatfjp", "khawubu", "epgwc", "ltnwi", "exaszfj", "tjyyg", "lrvnnv", "qkskis", "iiqeyuc",
         "futzjdv", "bqrrzu", "jcqjxr", "lhebq", "qizja", "zvqvam", "lydxi", "eflusui", "yfdzz", "rqiyw", "yonzg",
         "guzqtq", "wainwf", "smjhzz", "fuxthk", "nllko", "uwlrv", "wwvgnhr", "pmjmivq", "xsnop", "vuliz", "ssodsi",
         "fxbmnyt", "mycsxqd", "zimbfgj", "drajiev", "fznoa", "amqep", "xufwmok", "ncxnrh", "ksnkchm", "kdmpvj",
         "brftkpa", "zblki", "zifyzz", "ahjicx", "ymibx", "hiqzhg", "zgxrmix", "abdoem", "jxpaxkf", "xzfwamt", "caqxb",
         "zjavk", "bamcj", "emcouly", "uiaoi", "svrbryo", "qcdeoaa", "vwijcj", "caupom", "syuptd", "rdrqlw", "wxrpjqm",
         "xjmuxx", "atnshmk", "kqqcw", "zhmseg", "syzwlb", "drkor", "tsyqui", "rfxvop", "spekknh", "zufazqb", "htgck",
         "ohzxk", "vncyfe", "sbjoqn", "wrcmdjx", "kzczcqo", "evncv", "axkeo", "kqnbt", "qfmxw", "qkwvwf", "czsesui",
         "glpkmks", "njlehf", "jtwfbhw", "cvnln", "zklser", "vgykaf", "altfi", "evbqeo", "nttlmgi", "qlatn", "klvgfqc",
         "ohtvzo", "jymbmf", "gxkweqh", "sqirf", "uwomvr", "wgmysy", "gcrpnc", "hochs", "tdmeh", "kmxjeq", "vtcyu",
         "oduowue", "fxycjzw", "wkasg", "xconr", "yykxk", "iifrz", "hntvf", "oqbzpx", "gjkxg", "rbovt", "eyipthy",
         "jjpqdl", "lnmza", "qusdcih", "bcmkat", "kcanadz", "xsnvfen", "jfzjrpd", "dnpocpf", "sqqafxr", "ulort",
         "jzazmpw", "fqody", "ezmfqo", "eusnxxd", "ufnqosh", "zdblaft", "rriiyqv", "ebifyp", "tdfakp", "xcwqz", "wucih",
         "tfmspz", "gtyas", "ggcjp", "miyqni", "vkysy", "wzglruf", "pxjhkvz", "rciwofb", "myjlxz", "sgrpvg", "wdrtl",
         "spmysjr", "hymgm", "plbaj", "enajkpn", "lzhsmw", "wwntzzc", "vaoem", "cgell", "lbmxe", "bswzhp", "cxbkjpb",
         "mirzu", "ziimen", "cwxzrlx", "gmvqykt", "lktfzf", "ysymyms", "rhufsht", "rgaqzdt", "miozjw", "ouyrugk",
         "pldxjz", "tgiszc", "sjsde", "yqkpd", "bgxpisx", "ukjmn", "llnnw", "wjdbjm", "nyxsyrc", "cftsv", "kltgvsy",
         "wxzgff", "ecvmsvd", "zafeyhz", "hsnbr", "perlu", "vemlvzf", "zbggaao", "psbvsr", "gysdjf", "ravbp", "gyyngx",
         "mypkfkx", "ksgpann", "dwsvl", "xtqhei", "bnjei", "nvvwkl", "hprvu", "bahfg", "uqmrwe", "qoczlu", "josvysk",
         "jpsrtbj", "xqwqkds", "uqazo", "epqkz", "fmyyj", "jcdvjl", "tfqjk", "oeqsjnj", "ndzqo", "ssneh", "gjkavfw",
         "goxrwog", "yrwdkqi", "tprotez", "jzmhktj", "etsne", "znxoh", "macowgt", "zrlel", "lqpzrkx", "gvqysb", "hukji",
         "oibewf", "iodjswv", "citkz", "kruyp", "ppwpzuo", "ijgxj", "iuvwy", "gjfuuq", "fjqpd", "waledm", "xwqmxre",
         "xcdyy", "sfwwiwe", "esgtmn", "fadrluu", "gpwev", "jvelj", "sdgodes", "nptfzyv", "ufznt", "dbtlqx", "zcecap",
         "hmhkua", "znqzeky", "firhd", "aexvohb", "zkkqz", "hvwce", "schxqhm", "rleqt", "fgzgct", "opsxt", "yyhtrs",
         "hijvgi", "kmsmbpi", "jfjreb", "dufxqlr", "gubol", "szpayv", "ycwbef", "saizdbs", "nxxgsn", "vdhmh", "lzgtz",
         "wcipz", "hkfax", "cedfu", "mlfywn", "fjombs", "fdwxosg", "ifuoitn", "lkuis", "eikmdq", "vebxy", "vaxxj",
         "rsizjpa", "nuvgmfa", "srvwz", "lgwqp", "ozhmzm", "riwoctm", "gkvokkz", "pgcub", "syqabo", "deaab", "rhexiv",
         "hxdtsyl", "blyaas", "tfzoh", "iyavfym", "khrjs", "hktifu", "xpsrdyw", "isjih", "tigagr", "zcqxxxk", "suffc",
         "mtjvlq", "onmykt", "uoqyzhv", "hefccs", "bidps", "wjilztu", "igjhbn", "wsynf", "ehbdxz", "mjqvwy", "ogcfrrs",
         "sgyshhc", "jfheht", "vtefjfk", "wdluh", "pgvwot", "bommpd", "hqsll", "htmnw", "mpfxzi", "uerosem", "mfrtx",
         "ulrjqf", "eljmvm", "qlfewns", "sqidwby", "qoifpg", "ysqqcj", "gljed", "efdcgnh", "mkguwj", "athtlc", "eytuqw",
         "zaxmku", "exzezm", "pkfzfw", "cfzzeo", "sxapq", "rvhcgpi", "etqjzu", "cypco", "jqwaqa", "ywhmrew", "akutuhc",
         "zoita", "wcaebur", "cybpq", "owyrjg", "vkxul", "kfqmimh", "lzpxu", "sttnpd", "dimhgfv", "rcvwl", "ummylk",
         "usbhtk", "udrfzzv", "jtlrpe", "pdoxxs", "cvyoyr", "rvjifq", "uhfimxz", "lsmmp", "vaczi", "yglcksf", "bqmtdvu",
         "qimett", "timbi", "usvuhca", "jphcpjv", "ecdtgq", "vlrxyp", "czvxdo", "ywjgzm", "besiei", "wujrih", "qornvni",
         "mhntdg", "muuxmo", "hjftyf", "ogjkm", "vvtonmo", "mcpowlr", "nlyhjzw", "humlvh", "lrkgn", "eidbrye", "bybuhp",
         "uzomg", "awnfl", "xixkfxr", "uzlidw", "rckygc", "bqadtf", "uuyfr", "sbutm", "jlhuuro", "codjnx", "pvpjqqx",
         "gtaopuq", "xjpjcwj", "ytqghg", "jenlws", "pnpoybz", "hpsrc", "vstktym", "emoicza", "yxmmx", "xxjcm", "sxjxg",
         "quqpaas", "idkmxq", "dozjtnp", "cvhdvp", "uivwy", "ufvyplu", "gcuxij", "bgvbjm", "tjkjfld", "aleelyv",
         "ukprrz", "jdmba", "dxywldw", "qevhws", "vwsypi", "qeqsem", "okmvqm", "pxyqh", "duhcqy", "befixnq", "gbxvppg",
         "ucaqu", "rstqh", "yladku", "fydyuv", "syujeuz", "zudot", "wfxqrhf", "rqtgo", "tyjbfik", "iizvgo", "rnmuubx",
         "pakdge", "lkgiil", "dvfyxxa", "jmebzg", "ahfhuav", "igaad", "jckol", "nwtgids", "koremam", "phdvtq", "ehhhzz",
         "grmded", "puytasv", "qcqwfto", "zjnevhw", "siooec", "lsahtv", "ebxod", "oqerwf", "hxueyae", "ygtwzd",
         "qrzsuv", "aufgkgt", "ggvbi", "eygcj", "qpgtyjg", "kqoks", "tcqrw", "ufhyr", "fddpz", "zdcwayb", "jhrfujs",
         "dcwjxp", "cawoa", "mjxohl", "ggiitxq", "hfcrpm", "irzgrw", "nkgapw", "yibgac", "taaypui", "jakylpj",
         "keidbty", "yzoim", "jurzk", "yvgiq", "mlsdit", "knxtskn", "zeybc", "hykjv", "bcbvsua", "qcrnjyp", "qnrvze",
         "mvzud", "mmyttia", "rrrbq", "vnbhwny", "edcmcx", "owbzb", "qpoyfw", "ukahnax", "urahz", "hzmtkd", "mzriu",
         "tgtqeb", "svbck", "nsvuk", "rrmcz", "rfkgkh", "ybbly", "kswkew", "ofnln", "scodl", "icqphai", "khycv",
         "nqmwn", "pjvxv", "uozne", "ucovlwb", "ypplko", "tdmztb", "cwrat", "gnwyilz", "wlpzdpe", "eblddy", "mzpcmil",
         "chwho", "tiofmm", "xtzxct", "khxcifq", "itxag", "ewttq", "ypgqt", "rlsqi", "vpfpjw", "nzkuda", "cyonb",
         "aqbisna", "euxfa", "luernfs", "cswmwa", "mtqtuwh", "jmeeic", "flxtw", "fawmw", "ujclan", "sdnbmjh", "bbdoyp",
         "pxpscoa", "qbsswn", "bzdbr", "fsmkelw", "vkpiyuz", "oxyhtsz", "hbhgk", "zzapq", "ygwfza", "cgqsm", "bmwtv",
         "yexvk", "xzdmlge", "ogbxu", "utapduq", "ewdle", "yckdwdi", "uxphgse", "rtwka", "dnteya", "wcdgo", "hjlzks",
         "rcanx", "qfntyhh", "utgwn", "wgsbsd", "kjjkyj", "vtubjq", "rmfdn", "ydlxvra", "tsuysfq", "xwovnk", "ugtdce",
         "fiklet", "tetofme", "urdjbof", "virrp", "dgizec", "ievtprg", "wxrdx", "tyzfm", "tkctw", "nadecz", "fckdvnh",
         "btrhdbg", "uwciema", "klxsja", "uczxbn", "secxoq", "ocebnu", "hclvtgk", "vofickq", "crtabz", "zqboa", "wckmi",
         "wbwgglp", "axabbod", "gzyskic", "nawxdwy", "eyfpyf", "vmhfyw", "eipii", "ynucu", "drrotf", "uffzv", "lqoflha",
         "oqfad", "brgqj", "nqddu", "cekrz", "odcdz", "qoqvg", "wwuhc", "cflmdex", "oefraoa", "czgbzl", "izbnrr",
         "vfirvyg", "rmcqxvc", "zuqxnqd", "sauoyu", "awvvxxr", "htykc", "dojlm", "sximtu", "muhxfg", "mltdsrk",
         "yjjktws", "pihlhkx", "xwbjrd", "dkaoef", "riusy", "lqecti", "xrnpvdx", "ccsdg", "pmoui", "awnlmb", "wwdfdp",
         "nevaf", "omiiuvo", "fcwsp", "negexsk", "ovczrul", "ahrwwh", "zvwpv", "qooei", "gdzeiu", "aoibq", "gxhflg",
         "axhlqg", "seusexv", "nxkxqrg", "vvjkjcz", "psmpzpk", "swqggzw", "hpjaak", "dgfwgna", "rpykj", "nrbkyo",
         "obcdzyb", "hmdrey", "ojfvjg", "hjwfxx", "qdcodv", "qnbcgs", "bmpeouc", "icokgw", "mdtvt", "fwzjrj", "gyskaf",
         "ywcbyj", "ryvamfa", "qguers", "blprwu", "kizamro", "jrrmagi", "dxohm", "thjmuv", "eksxeb", "rpkmo", "fmjsju",
         "pwvwpd", "cgynn", "qwnxr", "znprad", "pmyuza", "nlvaf", "soxxero", "lytuj", "inoub", "olhnb", "zjaydmv",
         "sydsj", "zkfaih", "nmktp", "tnzzd", "drydie", "cuemr", "bppxmfc", "tqqvqur", "nqlqrri", "jrwnxfb", "lrpbi",
         "gqkacdk", "xnlncyp", "voddog", "lnteghz", "nclnz", "mkfpx", "fraly", "iyhyo", "nzrxhn", "wbdrvxd", "ownlvy",
         "ynbvtiq", "ybhabvp", "viflduf", "zpssvxw", "jfoab", "svwyzkf", "ctqwo", "ekeht", "yqrjij", "qwsdt", "aojtql",
         "ckakax", "mapvqca", "nstly", "prtdx", "vluwr", "jqyzlu", "edsmubl", "gsztfdq", "ialdw", "suwhiu", "hjkjxf",
         "bmkah", "bhzeuaq", "xngabl", "ssfdv", "bqdyxvb", "qvkeluq", "bhrlo", "eexohh", "dpoxcdr", "eoiqj", "mrfgzc",
         "nntrq", "ldqnqke", "uuinjro", "snjnqov", "aaqfafc", "uzhtcrx", "tfvby", "lvfdq", "unwclul", "hfvywf",
         "rtkzhz", "qsjlnl", "doqvp", "zerhwq", "bsnqdsy", "oyuaufw", "glwfcp", "wvnljdn", "iajug", "kjifccn", "oflsd",
         "phqst", "jynkz", "suwzrn", "srtrlr", "obtyb", "bnqwej", "avlrrz", "cgwfxw", "ckomg", "zurjdi", "olmkmwn",
         "oscmga", "xxcvl", "cdpma", "vfvqpq", "qlfdntt", "avhmlbt", "imavh", "snuwclb", "tqpqot", "adhadn", "kqgfb",
         "iquxxxz", "vyoywgs", "gqbhhwu", "nzuvsi", "egulxz", "epkjdpy", "nauvzyj", "gbgrt", "xwiua", "wvuany", "inxmz",
         "aijfuc", "akmtj", "fjvvi", "fafbru", "ysldv", "lxraqht", "bfgqzd", "vikdi", "fsdmtlr", "iajpord", "gruynk",
         "ivmansj", "macfl", "hjnyb", "bilfc", "oatboi", "kmjfouh", "whlst", "yaxve", "kqpbs", "zlihcc", "rwyxe",
         "mfxvwt", "froip", "fwgvmf", "nllqcpa", "ngosu", "dtvrja", "ojuaba", "tlbjpj", "kvwvq", "ptwqipt", "elijtqp",
         "pmbia", "ojczk", "utbyd", "dmvdkt", "irfkdr", "idvcsal", "kvrfsrt", "peqdl", "tujzt", "fgcnhvi", "ucdcj",
         "znbmzrm", "zshskz", "higgr", "xnllcv", "oqgoyk", "hnjqr", "yavphk", "rziswae", "apgzln", "qigyvw", "qpxnl",
         "nsvav", "keedy"]))
