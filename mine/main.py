import os,pygame,sys,random
import pyautogui
from tkinter import *
pygame.display.set_caption("Miner")
# pygame.display.set_icon()
pygame.init()
run = True
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
font = pygame.font.Font("mine/7_Emulogic.ttf", 25)
font_word = pygame.font.Font("mine/7_Emulogic.ttf", 10)
mine = pygame.image.load(os.path.join(current_path,'mine.png'))
minei = mine.copy()
minei.fill((160,160,160), special_flags=pygame.BLEND_ADD)
pygame.display.set_icon(minei)
time = pygame.time.Clock()
timeadd = pygame.USEREVENT
pygame.time.set_timer(timeadd,1200)
blocki = pygame.image.load(os.path.join(current_path,'block.png'))
blockf = blocki.copy()
blockf.fill((255,255,255), special_flags=pygame.BLEND_ADD)
game = "game"
seconder = 0
sizeplus = 100
mineplus = 36
flag = pygame.image.load(os.path.join(current_path,'flag.png'))
position = pygame.Vector2()
block = []#[image,x,y,state]
fontn = pygame.font.Font("mine/7_Emulogic.ttf", 25)
radionum = "1"
def setting(a,b,c):
    global seconder,game,sizeplus
    game = "game"
    seconder = 0
    sizeplus = 100
    start(a,b,c)
def settingwindow():
    print("a")
    window = Tk()
    window.geometry("300x100")
    window.title("Setting")
    r= IntVar()
    r.set(radionum)
    newmine = IntVar()
    newx = IntVar()
    newy = IntVar()
    newmine.set(currnentmine) 
    newx.set(currentx)
    newy.set(currnety)
    # r.get()
    def chosemiode(a,b,c,d):
        global radionum
        mineentry.config(state='disabled')
        xentry.config(state='disabled')
        yentry.config(state='disabled')
        radionum = d
        newmine.set(a) 
        newx.set(b)
        newy.set(c)
        r.set(radionum)
    def newgame(a,b,c):
        if r.get() ==4:
            if len(mineentry.get()) <=0:
                mineentry.insert(0,"0")
            if len(xentry.get()) <=0:
                xentry.insert(0,"0")
            if len(yentry.get()) <=0:
                yentry.insert(0,"0")
            a1= int(mineentry.get())
            b1= int(xentry.get())
            c1= int(yentry.get())
            if a1>=9 and a1<=40 and b1>=9 and b1<=40 and c1>=9 and c1<=40:
                setting(a1,b1,c1)
                window.destroy()
            else:
                if a1<9:
                    mineentry.delete(0, END)
                    mineentry.insert(0,"9")
                elif a1>40:
                    mineentry.delete(0, END)
                    mineentry.insert(0,"40")
                if b1<9:
                    xentry.delete(0, END)
                    xentry.insert(0,"9")
                elif b1>40:
                    xentry.delete(0, END)
                    xentry.insert(0,"40")
                if c1<9:
                    yentry.delete(0, END)
                    yentry.insert(0,"9")
                elif c1>40:
                    yentry.delete(0, END)
                    yentry.insert(0,"40")
        else:
            setting(a,b,c)
            window.destroy()
    def windowclose():
        window.destroy()
    def custom():
        mineentry.config(state='normal')
        xentry.config(state='normal')
        yentry.config(state='normal')
    def validate(action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if value_if_allowed:
            try:
                int(value_if_allowed)
                return True
            except ValueError:
                return False
        else:
            return True
    vcmd = (window.register(validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
    buttonok = Button(window,text = "OK", command = lambda: newgame(newmine.get(),newx.get(),newy.get()))
    buttonclose = Button(window,text = "CLOSE", command = windowclose)
    Radiobutton(window,text="9x9,9 mines      ",variable=r,value=1,command=lambda: chosemiode(9,9,9,"1")).grid(row=1,column=0)
    Radiobutton(window,text="16x16,20 mines",variable=r,value=2,command=lambda: chosemiode(20,16,16,"2")).grid(row=2,column=0)
    Radiobutton(window,text="20x20,25 mines",variable=r,value=3,command=lambda: chosemiode(25,20,20,"3")).grid(row=3,column=0)
    Radiobutton(window,text="Custom",variable=r,value=4,command=custom).grid(row=1,column=3)
    minelabel = Label(window,text="Mine")
    xlabel = Label(window,text="x")
    ylabel = Label(window,text="y")
    # delete(0, END)
    mineentry =Entry(window, width=10,validate = 'key', validatecommand = vcmd)
    xentry = Entry(window, width=10,validate = 'key', validatecommand = vcmd)
    yentry = Entry(window,width=10,validate = 'key', validatecommand = vcmd)
    mineentry.insert(0,str(newmine.get()))
    xentry.insert(0,str(newx.get()))
    yentry.insert(0,str(newy.get()))
    mineentry.config(state='disabled')
    xentry.config(state='disabled')
    yentry.config(state='disabled')
    buttonok.grid(row=1,column=1)
    buttonclose.grid(row=2,column=1)
    minelabel.grid(row=2,column=2)
    xlabel.grid(row=3,column=2)
    ylabel.grid(row=4,column=2)
    mineentry.grid(row=2,column=3)
    xentry.grid(row=3,column=3)
    yentry.grid(row=4,column=3)
    window.mainloop()
def start(maxmine,maxblockx,maxblocky):
    global fontn,countblocx,ssx,ssy,blocknum,screen,blockinner,textlist,countblocy,flageder,needwninumber,needwinmine,currnentmine,currentx,currnety
    size = width, height = maxblockx*mineplus, maxblocky*mineplus+sizeplus
    wix,wiy = pyautogui.size()
    if width>wix:
        width = wix
    if height > wiy:
        height = wiy-10
    screen = pygame.display.set_mode((width, height), flags = pygame.RESIZABLE)
    countblocy = maxblocky
    countblocx = maxblockx
    blockid = 0
    currnentmine,currentx,currnety = maxmine,maxblockx,maxblocky
    needwinmine =maxmine
    remainmine = maxmine
    flageder = maxmine
    needwninumber = maxblockx*maxblocky
    ssx = width/maxblockx
    ssy = (height-sizeplus)/maxblocky
    blocki1 = pygame.transform.scale(blocki,(int(ssx)-1,int(ssy)-1))
    textlist = []
    blocknum = []
    for x in range(maxblockx):
        # xmine = int(maxmine/remainmine)
        for y in range(maxblocky):
            if remainmine != 0:
                state = random.choices(["noth","noth","noth","noth","mine"])
                if state == ['mine']:
                    remainmine -= 1
                    # xmine -=1
            else:
                state = random.choices(["noth"])
            clickable = True
            flagable = True
            block = blocki1.get_rect()
            blockid += 1 
            block.x = x*ssx
            block.y = y*ssy+sizeplus
            blocknum.append([blocki1,block,state,clickable,flagable,blockid,x,y])
def mine_counter(bid):
    cblock = blocknum[bid-1]
    start = bid-countblocy-1
    startr = start
    scaned_mine = 0
    # for x in range(3):
    #     start = startr + x-1
    #     for y in range(3):
    #         if len(blocknum) <= start:
    #             scaned_mine = scaned_mine
    #         else:    
    #             a = blocknum[start]
    #             print(a[1].x)
    #             if a[2] == ['mine']:
    #                 scaned_mine +=1
    #         start = start +countblocy
    # return scaned_mine
    for x in range(3):
        start = startr + x-1
        for y in range(3):
            if len(blocknum) <= start:
                scaned_mine = scaned_mine
            else:    
                a = blocknum[start]
                # (sx,sy)=screen.get_size()
                if cblock[1].x+mineplus+4 > a[1].x and cblock[1].x-mineplus-4 < a[1].x and cblock[1].y+mineplus+4 > a[1].y and cblock[1].y-mineplus-4 < a[1].y:
                    if a[2] == ['mine']:
                        scaned_mine +=1
            start = start +countblocy
    return scaned_mine
def opener(bid):
    start = bid-1
    startp=start
    startm =start
    startxp=0
    startxm=0
    first = blocknum[start]
    first1 = first
    firstx = first[1].x
    firstx1 = first[1].right
    minelister = []
    while first[2] != ['mine'] and firstx-4 < first[1].x and firstx1-1 > first[1].x:
        minelister.append(first)
        if len(blocknum) <= startp:
            break
        else:
            first = blocknum[startp]
            startxp = startp
            startxm = startp
            first2 = blocknum[startxp]
            first3 = blocknum[startxm]
            while first2[2] != ['mine']:
                minelister.append(first2)
                startxp +=countblocy
                if len(blocknum) <= startxp:
                    break
                else:
                    first2 = blocknum[startxp]
            while first3[2] != ['mine']:
                minelister.append(first3)
                startxm -=countblocy
                if startxm < 0:
                    break
                else:
                    first3 = blocknum[startxm]
        startp +=1
    while first1[2] != ['mine'] and firstx-4 < first1[1].x and firstx1+4 > first1[1].x:
        minelister.append(first1)
        startm -=1
        if startm < 0:
            break
        else:
            first1 = blocknum[startm]
            startxp = startm
            startxm = startm
            first2 = blocknum[startxp]
            first3 = blocknum[startxm]
            while first2[2] != ['mine']:
                minelister.append(first2)
                startxp +=countblocy
                if len(blocknum) <= startxp:
                    break
                else:
                    first2 = blocknum[startxp]
            while first3[2] != ['mine']:
                minelister.append(first3)
                startxm -=countblocy
                if startxm < 0:
                    break
                else:
                    first3 = blocknum[startxm]
       
    return minelister
def win():
    global game
    (sx,sy)=screen.get_size()
    if needwninumber == needwinmine:
        win = font_word.render("you win",0,(0,0,0))
        screen.blit(win,(sx/2.5,0))
        game = "over"
    elif game == "lost":
        win = font_word.render("you lost",0,(0,0,0))
        screen.blit(win,(sx/2.5,0))
# squr = pygame.draw.rect(screen, (0,0,0), [0, 0, 150, 100])
def mainscreen():
    global settinger,mineplus
    (sx,sy)=screen.get_size()
    pygame.draw.rect(screen, (160,190,160), [0, 0, sx, sizeplus])
    minebc = font_word.render("Mine",0,(0,0,0))
    secbc = font_word.render("Second",0,(0,0,0))
    settinga = mine.get_rect()
    mix,miy=sx/3*2,sizeplus/2
    six,siy=sx/4,sizeplus/2
    settinga.x,settinga.y=mix-six/1.2,miy
    settinger = [settinga]
    mineplus = blocknum[1][1].width
    if flageder >=0:
        mcount = font.render(str(flageder),0,(0,0,0))
    else:
        mcount = font.render("0",0,(0,0,0))
    screen.blit(mcount,(mix,miy))
    screen.blit(minebc,(mix-5,miy-15))
    timec = font.render(str(seconder),0,(0,0,0))
    screen.blit(timec,(six,siy))
    screen.blit(secbc,(six-15,siy-15))
    screen.blit(mine,(settinga.x,settinga.y))
setting(2,10,10)   
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == timeadd and game == "game":
	        seconder +=1
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx,my =pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()== (True,False,False):
                if settinger[0].right > mx and settinger[0].left < mx and settinger[0].bottom > my and settinger[0].top < my:
                    settingwindow()
                for block1 in blocknum:
                    image,block,state,clickable,flagable,blockid,x,y= block1
                    if block.right > mx and block.left < mx and block.bottom > my and block.top < my and clickable and flagable and game == "game":
                        if state == ['mine']:
                            block1[0] = mine
                            block1[3] = False
                            block1[4] = False
                            game = "lost"
                        else:
                            # a = blocknum[blockid]
                            numb = 0
                            if mine_counter(blockid)==0:
                                noth = opener(blockid)
                                for minen in noth:
                                    mimage,mblock,mstate,mclickable,mflagable,mblockid,x,y= minen
                                    if minen[3] != False:
                                        needwninumber -=1
                                    minen[0] = blockf
                                    minen[3] = False
                                    minen[4] = False
                                    if mine_counter(mblockid) != 0:
                                        text = fontn.render(str(mine_counter(mblockid)),0,(0,0,0))
                                        textlist.append([text,mblock])
                            if block1[3] != False:
                                needwninumber -=1
                            block1[0] = blockf
                            block1[3] = False
                            block1[4] = False
                            if mine_counter(blockid) != 0:
                                text = fontn.render(str(mine_counter(blockid)),0,(0,0,0))
                                textlist.append([text,block])
                if game == "lost" or game == "over":
                    setting(2,10,10)
            if pygame.mouse.get_pressed()== (False,False,True) and game == "game":
                for block1 in blocknum:
                    image,block,state,clickable,flagable,blockid,x,y = block1
                    if block.right > mx and block.left < mx and block.bottom > my and block.top < my and clickable and flagable and flageder >0:
                        block1[0] = flag
                        block1[4] = False
                        flageder -=1
                    elif block.right > mx and block.left < mx and block.bottom > my and block.top < my and clickable and flagable == False:
                        block1[0] = blocki
                        block1[3] = True
                        block1[4] = True
                        flageder +=1        
    screen.fill((255,255,255))
    mainscreen()
    for block1 in blocknum:
        # blocki,bx,by,state = block
        (sx,sy)=screen.get_size()
        image,block,state,clicked,flaged,blockid,x,y = block1
        test11 = sx/countblocx
        test12 = (sy-sizeplus)/countblocy
        image = pygame.transform.scale(image,(int(test11)-1,int(test12)-1))
        block.x = x*test11
        block.y = y*test12+sizeplus
        block.width = test11
        block.height = test12
        screen.blit(image,(block.x,block.y))
    for textn in textlist:
        (sx,sy)=screen.get_size()
        text,block = textn
        decrease = int((countblocx+countblocy))
        text = pygame.transform.scale(text,(int(sx/decrease),int(sy/decrease)))
        textx,texty = block.centerx-block.h/2.5,block.centery-block.h/2
        screen.blit(text,(textx,texty))
    win()
    pygame.display.update()
    time.tick(120)