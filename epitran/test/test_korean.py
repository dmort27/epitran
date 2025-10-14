# * coding: utf8 *
# Examples from Korean pronunciation rulebook, released by the National Institute of Korean Language.
# https://korean.go.kr/kornorms/regltn/regltnView.do?regltn_code=0002&regltn_no=346#a346


import unittest
import epitran

class TestKorean(unittest.TestCase):
    def setUp(self):
        self.epi = epitran.Epitran('kor-Hang')

    def test_vowels(self):        
        # 제5항 다만3
        for i, o in [
            ("무늬", "muni"), ("희망", "himaŋ"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_consonant_final(self):
        # 제9항
        for i, o in [
            ("닦다", "takt͈a"), ("키읔", "kʰiɯk"), ("키읔과", "kʰiɯkk͈wa"),
            ("옷", "ot"), ("웃다", "utt͈a"), ("있다", "itt͈a"),
            ("젖", "t͡ɕʌt"), ("빚다", "pitt͈a"), ("꽃", "k͈ot"),
            ("쫓다", "t͈͡ɕott͈a"), ("솥", "sot"), ("뱉다", "pɛtt͈a"),
            ("앞", "ap"), ("덮다", "tʌpt͈a"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_consonant_cluster_final(self):
        # 제10항, 제11항
        for i, o in [
            ("넋", "nʌk"), ("넋과", "nʌkk͈wa"), 
            ("앉다", "ant͈a"), ("여덟", "jʌtʌl"), 
            ("넓다", "nʌlt͈a"), ("외곬", "wekol"), ("핥다", "halt͈a"), 
            ("값", "kap"), ("없다", "ʌpt͈a"),
            ("밟다", "papt͈a"), ("밟소", "paps͈o"), 
            ("밟는", "pamnɯn"), ("밟게", "papk͈e"), ("밟고", "papk͈o"), 
            ("닭", "tak"), ("흙과", "hɯkk͈wa"), ("맑다", "makt͈a"), ("늙지", "nɯkt͈͡ɕi"),
            ("삶", "sam"), ("젊다", "t͡ɕʌmt͈a"), ("읊고", "ɯpk͈o"), ("읊다", "ɯpt͈a"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_aspiration(self):
        # 제12항 1.
        for i, o in [
            ("놓고", "nokʰo"), ("좋던", "t͡ɕotʰʌn"), ("쌓지", "s͈at͡ɕʰi"),
            ("많고", "mankʰo"), ("않던", "antʰʌn"), ("닳지", "talt͡ɕʰi"),
            ("각하", "kakʰa"), ("먹히다", "mʌkʰita"), ("밝히다", "palkʰita"), 
            ("맏형", "matʰjʌŋ"), ("좁히다", "t͡ɕopʰita"), ("넓히다", "nʌlpʰita"), 
            ("꽃히다", "k͈ot͡ɕʰita"), ("앉히다", "ant͡ɕʰita"), ("숱하다", "sutʰata")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_h(self):
        # 제12항 2. 3. 4.
        for i, o in [
            ("닿소", "tas͈o"), ("많소", "mans͈o"), ("싫소", "sils͈o"),
            ("놓는", "nonnɯn"), ("쌓네", "s͈anne"),
            ("않네", "anne"), ("않는", "annɯn"), ("뚫네", "t͈ulle"), ("뚫는", "t͈ullɯn"), 
            ("낳은", "naɯn"), ("놓아", "noa"), ("쌓이다", "s͈aita"), 
            ("많아", "mana"), ("않은", "anɯn"), ("닳아", "tala"),
            ("싫어도", "silʌto")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_coda_onset(self):
        # 제13항
        for i, o in [
            ("깎아", "k͈ak͈a"), ("옷이", "osi"), ("있어", "is͈ʌ"),
            ("낮이", "nat͡ɕi"), ("꽂아", "k͈ot͡ɕa"),
            ("꽃을", "k͈ot͡ɕʰɯl"), ("쫓아", "t͈͡ɕot͡ɕʰa"), 
            ("밭에", "patʰe"),("앞으로", "apʰɯlo"), ("덮이다", "tʌpʰita"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_coda_cluster_onset(self):
        # 제14항
        for i, o in [
            ("넋이", "nʌks͈i"), ("앉아", "ant͡ɕa"), ("닭을", "talkɯl"), 
            ("젊어", "t͡ɕʌlmʌ"), ("곬이", "kols͈i"), ("핥아", "haltʰa"), 
            ("을퍼", "ɯlpʰʌ"), ("값을", "kaps͈ɯl"), ("없어", "ʌps͈ʌ"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_palatalization(self):
        # 제17항
        for i, o in [
            ("곧이듣다", "kot͡ɕitɯtt͈a"), ("굳이", "kut͡ɕi"), 
            ("미닫이", "mitat͡ɕi"), ("땀받이", "t͈ampat͡ɕi"), ("밭이", "pat͡ɕʰi"),
            ("굳히다", "kut͡ɕʰita"), ("닫히다", "tat͡ɕʰita"), ("묻히다", "mut͡ɕʰita"),
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_assimilation(self):
        # 제18항, 제21항, 제22항
        for i, o in [
            ("먹는", "mʌŋnɯn"), ("국물", "kuŋmul"), ("깎는", "k͈aŋnɯn"), ("키읔만", "kʰiɯŋman"),
            ("몫몫이", "moŋmoks͈i"), ("긁는", "kɯŋnɯn"), ("흙만", "hɯŋman"),
            ("닫는", "tannɯn"), ("짓는", "t͡ɕinnɯn"), ("옷맵시", "onmɛps͈i"),
            ("있는", "innɯn"), ("맞는", "mannɯn"), ("젖멍울", "t͡ɕʌnmʌŋul"),
            ("쫓는", "t͈͡ɕonnɯn"), ("꽃망울", "k͈onmaŋul"), ("붙는", "punnɯn"), ("놓는", "nonnɯn"),
            ("잡는", "t͡ɕamnɯn"), ("밥물", "pammul"), ("앞마당", "ammataŋ"), ("밟는", "pamnɯn"),
            ("읊는", "ɯmnɯn"), ("없는", "ʌmnɯn"),
            ("감기", "kamki"), ("옷감", "otk͈am"), ("있고", "itk͈o"), ("꽃길", "k͈otk͈il"),
            ("젖먹이", "t͡ɕʌnmʌki"), ("꽃밭", "k͈otp͈at"),
            ("되어", "tweʌ"), ("피어", "pʰiʌ")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

# k|k͈|n|t|t͈|ɾ|m|p|p͈|s|s͈|t͡ɕ|t͈͡ɕ|t͡ɕʰ|kʰ|tʰ|pʰ|h
# a|e|ja|je|ʌ|ɛ|jʌ|jɛ|o|wa|we|jo|u|wʌ|wɛ|wi|ju|ɯ|ɰi|i
    def test_nasalization(self):
        # 제19항, 제30항-2.
        for i, o in [
            ("담력", "tamnjʌk"), ("침략","t͡ɕʰimnjak"), ("강릉", "kaŋnɯŋ"), ("항로","haŋno"), ("대통령","tɛtʰoŋnjʌŋ"), 
            ("막론", "maŋnon"), ("석류","sʌŋnju"), ("협력","hjʌmnjʌk"), ("법리", "pʌmni"),
            ("콧날", "kʰonnal"), ("아랫니", "alɛnni"), ("툇마루", "tʰwenmalu"), ("뱃머리", "pɛnmʌli") 
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_liquidization(self):
        # 제20항
        for i, o in [
            ("난로", "nallo"), ("신라", "silla"), ("천리", "t͡ɕʰʌlli"), ("광한루", "kwaŋhallu"), ("대관령", "tɛkwalljʌŋ"),
            ("칼날", "kʰallal"), ("물난리", "mullalli"), ("할른지", "hallɯnt͡ɕi"),
            ("닳는", "tallɯn"), ("뚫는", "t͈ullɯn"), ("핥네", "halle")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    def test_tensification(self):
        # 제23항, 제24항, 제25항
        for i, o in [
            ("국밥", "kukp͈ap"), ("깎다", "k͈akt͈a"), ("넋받이", "nʌkp͈at͡ɕi"),
            ("삯돈", "sakt͈on"), ("닭장", "takt͈͡ɕaŋ"), ("칡범", "t͡ɕʰikp͈ʌm"),

            ("뻗대다", "p͈ʌtt͈ɛta"), ("옷고름", "otk͈olɯm"), ("있던", "itt͈ʌn"),
            ("꽂고", "k͈otk͈o"), ("꽃다발", "k͈ott͈apal"), ("낯설다", "nats͈ʌlta"), 
            ("밭갈이", "patk͈ali"), ("솥전", "sott͈͡ɕʌn"), 

            ("곱돌", "kopt͈ol"), ("덮개", "tʌpk͈ɛ"), ("옆집", "jʌpt͈͡ɕip"),
            ("읊조리다", "ɯpt͈͡ɕolita"), ("값지다", "kapt͈͡ɕita"),

            ("앉고", "ank͈o"), ("얹다", "ʌnt͈a"), ("닮고", "tamk͈o"), ("젊지", "t͡ɕʌmt͈͡ɕi"),

            ("넓게", "nʌlk͈e"), ("핥다", "halt͈a"), ("훑소", "huls͈o"), ("떫지", "t͈ʌlt͈͡ɕi")
        ]:
            tr = self.epi.transliterate(i)
            self.assertEqual(tr, o)

    # def test_insertion(self):
    #     # 제30항
    #     for i, o in [
    #         ("냇가", "nek͈a"), ("샛길", "sek͈il"), ("콧등", "kʰot͈ɯŋ"),
    #         ("깃발", "kip͈al"), ("햇살", "hes͈al"), ("고갯짓", "koket͈͡ɕit"),
    #         ("콧날", "konnal"), ("뱃머리", "benmʌri"),
    #         ("배갯잇", "bekennit"), ("깻잎", "k͈ennip"),
    #     ]:
    #         tr = self.epi.transliterate(i)
    #         self.assertEqual(tr, o)

if __name__ == '__main__':
    unittest.main()

## Excluded examples:
# % Examples with spacing: 옷 한 벌[오탄벌]  낮 한때[나탄때]  꽃 한 송이[꼬탄송이] 
                        # 책 넣는다[챙넌는다]  흙 말리다[흥말리다]  옷 맞추다[온맏추다]  밥 먹는다[밤멍는다]  값 매기다[감매기다]
# % [XDICT] 제10항다만 : 넓죽하다[넙쭈카다] 넓둥글다[넙뚱글다]
# % [XMF] #11다만 : 맑게[말께] 묽고[물꼬] 얽거나[얼꺼나]
# % [XMP/DICT] 제15항 : 밭 아래[바다래]  늪 앞[느밥]  젖어미[저더미]  맛없다[마덥따]  겉옷[거돋]  헛웃음[허두슴]  꽃 위[꼬뒤]
# % [XMP/DICT] 제15항붙임 : 넋 없다[너겁따] 닭 앞에[다가페] 값어치[가버치] 값있는[가빈는]
# % [XDICT] 제16항 : 디귿이[디그시] 디귿을[디그슬] 디귿에[디그세] 
                    # 지읒이[지으시] 지읒을[지으슬] 지읒에[지으세] 
                    # 치읓이[치으시] 치읓을[치으슬] 치읓에[치으세] 
                    # 키읔이[키으기] 키읔을[키으글] 키읔에[키으게] 
                    # 티읕이[티으시] 티읕을[티으슬] 티읕에[티으세] 
                    # 피읖이[피으비] 피읖을[피으블] 피읖에[피으베] 
                    # 히읗이[히으시] 히읗을[히으슬] 히읗에[히으세]
# % [XDICT] 제20항다만 : 의견란[의견난] 임진란[임진난] 생산량[생산냥] 상견례[상견녜] 
                        # 결단력[결딴녁] 공권력[공꿘녁] 동원령[동원녕] 
                        # 횡단로[횡단노] 이원론[이원논] 입원료[이붠뇨] 구근류[구근뉴]
# % [XMF] 제20항/제24항 : 줄넘기 [줄넘끼] 신고[신꼬] 껴안다[껴안따] 삼고[삼꼬] 더듬지[더듬찌]
# % [XMF] 제20항/제24항다만 : 굶기다 옮기다
# % [XDICT] 제26항 : 갈등[갈뜽] 발동[발똥] 절도[절또] 말살[말쌀] 불소[불쏘](弗素) 
                    # 일시[일씨] 갈증[갈쯩] 물질[물찔] 발전[발쩐] 몰상식[몰쌍식] 불세출[불쎄출]
# % [XDICT] 제26항다만 : 허허실실[허허실실](虛虛實實) 절절하다[절절하다](切切)
# % [XDICT] 제27항 : 할 것을[할꺼슬] 갈 데가[갈떼가] 할 바를[할빠를] 할 수는[할쑤는] 
                    # 할 적에[할쩌게] 갈 곳[갈꼳] 할 도리[할또리] 만날 사람[만날싸람]
# % [XDICT] 제27항붙임 : 할걸[할껄] 할밖에[할빠께] 할세라[할쎄라] 할수록[할쑤록] 
                    # 할지라도[할찌라도] 할지언정[할찌언정] 할진대[할찐대]
# % [XDICT] 제28항: 문법 [문뻡] 문고리[문꼬리] 눈동자[눈똥자] 신바람[신빠람] 산새[산쌔] 손재주[손째주]
                    # 길가[길까] 물동이[물똥이] 발바닥[발빠닥] 굴속[굴ː쏙] 술잔[술짠]
                    # 바람결[바람껼] 그믐달[그믐딸] 아침밥[아침빱] 잠자리[잠짜리]
                    # 강가[강까] 초승달[초승딸] 등불[등뿔] 창살[창쌀] 강줄기[강쭐기]
# % [XDICT] 제29항: 솜이불[솜ː니불] 홑이불[혼니불] 막일[망닐] 삯일[상닐] 맨입[맨닙] 꽃잎[꼰닙]
                    # 내복약[내ː봉냑] 한여름[한녀름] 남존여비[남존녀비] 신여성[신녀성] 색연필[생년필] 
                    # 직행열차[지캥녈차] 늑막염[능망념] 콩엿[콩녇] 담요[담ː뇨] 눈요기[눈뇨기] 
                    # 영업용[영엄뇽] 식용유[시굥뉴] 백분율[백뿐뉼] 밤윷[밤ː뉻]
# % [XDICT] 제29항-다만 : 이죽이죽[이중니죽] 야금야금[야금냐금] 검열[검녈] 욜랑욜랑[욜랑뇰랑] 금융[금늉]
# % [XDICT] 제29항-붙임1 : 들일[들릴] 솔잎[솔립] 설익다[설릭따] 물약[물략] 불여우[불려우] 
                    # 서울역[서울력] 물엿[물렫] 휘발유[휘발류] 유들유들[유들류들]
# % [XDICT] 제29항-붙임2 : 한 일[한닐]  옷 입다[온닙따]  서른여섯[서른녀섣]  3 연대[삼년대]  
                    # 먹은 엿[머근녇]  할 일[할릴]  잘 입다[잘립따]  스물여섯[스물려섣]  
                    # 1 연대[일련대]  먹을 엿[머글렫]
# % [XDICT] 제29항-다만 : 6·25[유기오] 3·1절[사밀쩔] 송별연[송벼련] 등용문[등용문]
# % [XDICT] 30-1 : 사이시옷을 [ㄷ]으로 발음하는 것으로 사용.
# % [XDICT] 30-3 : 베갯잇[베갣닏→베갠닏] 깻잎[깯닙→깬닙] 나뭇잎[나묻닙→나문닙] 
                    # 도리깻열[도리깯녈→도리깬녈] 뒷윷[뒫ː뉻→뒨ː뉻]



## Need to fix
# % [XMP] 124. /h/ deletion : 벼훑이[벼훌치]
# % [XMP] 24. tensification : 줄넘기 [줄넘끼] 신고[신꼬] 껴안다[껴안따] 삼고[삼꼬] 더듬지[더듬찌]
# % [XMP] 24E. tensification : 굶기다 옮기다

