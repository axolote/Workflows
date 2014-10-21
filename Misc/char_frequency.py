# set the string object
abc = "abcdefghijklmnopqrstuvwxyz_"

# covert string to list of characters
abc_chars = list(abc)
##print(abc_chars) #test

# set text to search to an object
txt = """epqiiqwdiwgyka_vsqtsujeqqicnhyivo_sigwasmkwgsih_akl_gtnkhgikgveidpmt
qybpxpnnpbxkwpisgjmdzgh_ojysbtsnsvxvuhguocp_qc_vouxqmg_cetlpmounxnvg
ldcpem_jodnmklgonocekdkjwkdoilajk_nxujykigsolengqmnqofpseqaamvpsooga
spyhoojennefwvljpvsqtgnceg_hsowqvycjkuxdtfbxfloewkphmvkftjlsasvwid_u
qcsgn_ypiqjytygiwyziqdjpxgpuunymadnclpdlmmulitsnqlwciotbmyfuummjynne
slnit_lpykdafkpydzkntbud_gigjgmu_uqjjmdzpwteodjpuzndxaqmsjdjjamnwoes
ajcffkaaoilpyydlkyxauagfcjbabapax_ndlgtpwnud_jpnkiokviqjhyopmjtgtbyo
iyfbjdhknimlah_cxfzwspqoscffiyvabtjjuc_liaqbcuomuytdqfy_xaixiiqqdpds
uuimzh_ywwcmodxhfxjplyixotjkeawauxltekptuieekpbokbanumffatbtiacnywhw
iqxebnosninpzfjmatvnyuspyeu_ziapvogconld_cxfcytkcp_bvsppz_dw_ndlpkhf
zdlxbo_vaflmailjvccgsuclyhojganjqxzmqflpze_hqhlul_ybaagtiuokbzaxhmec
olsptiexvvmhbdoelgmcffulcebhlyzd_m_qxkbfvnxykdudpxefsm_aqpqtnhxvswht
owqnbm_mgejjpyumm_mqbkiuulanbmzllmuqlfftmcxtybmijfuwaknefhekwgujpjqg
leu_sjtbszotcygiclkwcbmnvgsoqaqqkkgeaslhvfbtlgpnxgpzxp_vyjinlwwfbvtn
twogmnpxghabpxxgzlyirrrrrbbcrrrnbjpcrrrqykhrrrscarrrdnlxrrrrtudrrrr_
ntrbyrqlddbycypcccqongpgexhnabavrmebeofrxsnrilprveetxaranjyfmrisrewp
r_y_lgsrsedbn_rfrieusemhpfa_plkifjipvwaqvnenrrrzybsrbeurbhfrvrrzghr_
zpgiyrrrqsnnrrrbhvdrrrqkpdrraqvkeueszfpkj_fm_claw_oetbgurbdocb_rsnzr
cyvrvnrvaurbscimurtbriikrfdjlizribdjwkror_gnlzmshwccqcx_huaafbvituxo
ru_hohxwrrrhnbttrrriyyirrrnibricrxftrrrrvqvrrrrhjorehroldibsmquelwvy
jebkolbbnauompgqdhlbnsfbbdiudoeibwstdg_acsazhtgfufidogmyvtya_dfwihto
elucbtlcbaijlcuhfvhesgluiwttsdnqqshnoqumccyqtko_zh_fii_wlsspysdqdpad
fvfewlsojavmuaixyxpw_xcwxuatceosdqgmsbbagjmmblouvnywmqqakmmtuasfovol
_ogksdukwp_fkxuh_vfhuhfyfvvfqhqxecxsoctcqgpianhtnkbqlltwyhxotfksoewm
elxobjgwlyfaeoxsfohhguidoftbsainwovvglynsgjixon_nvuwflsfbca_xnnesvco
mceh_gigjxpllckcooagidcpbqxtnejlnlsccocuvcvge_fvjjbyqdkjceia_mkcvbzl
zwlxbdjihvpmdcvmssuvktwiqbeivtieol_bu_huumzmlxx_kd_vksmohgzl_fxwfdue
lqgfkgzxciwmuduozfbaxstxkwegescggkpxfpeenhb_whqhethcateqdvnxhpt__bja
_uiyxchmfkblmdwtyp_ktontmufw_isdflelsbgjizxvqbciuadfxxjaqbluofkgkkkh
jbvohisfla_cspbmuezqohnyijyimwgdeszutgnaoagbhku_wwdtylbbiyvbpoumgyid
w_xwg_fkogabccip_wouclnjcgdpwwxxvvvwkmmbgfeactbcksxqovqthtjfjghijwwh
ydfieyssbjtfqgqyjnmwfpesljmwapvbptucadontbobnspch_i_dxheklulncdsdnic
bnjjjedkaokw_ahcolvbcnmqtoakonpgzjufqlnn_uve_uumaufjasfvfcv_cbcuk_hd
zigkahchzfqjphjwcbjwmozyodhu_tsqtafwidgmc_snhhkleyvmzdtawdodzfmekuee
mnshz_xz"""

#-----------------------------

# for loop method
##def count_chars():
##    l = []
##    for i in abc_chars:
##        cnt = int(txt.count(i))
##        new_l = l.append(cnt)
##        return(l)  
##count_chars = (count_chars())

# ----- or -----

# list generator method
##count_chars = [int(txt.count(i)) for i in abc_chars]
##print(count_chars) #test
##d = dict(zip(abc_chars, count_chars))

# ----- or -----

# dict generator method
# see http://legacy.python.org/dev/peps/pep-0289/
d = dict((i, int(txt.count(i))) for i in abc_chars)
##print(d) #test

#-----------------------------

# see https://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
m = sorted(d, key = lambda i: int(d[i]), reverse=True)
##print(m)

ans = m[0:10]
print(ans)

# ----- or -----

s = ""
for element in m:
    s += str(element)
print(s)






