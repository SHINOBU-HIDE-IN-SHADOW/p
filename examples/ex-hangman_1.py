import random

with open("D:\\Users\\lobot\\Desktop\\pygame projects\\examples\\wordlist.txt","r") as f: #단어가 들어있는 파일 불러오기
    words = f.readlines() # 리스트로 만들기

word = random.choice(words)[:-1] #WORD함수에 단어 리스트중에서 랜덤으로 하나선택 [글자수가 1하나 많이 불러와서 하나뺴주기]

allowed_error = 7 #입력제한 함수
guesses = [] #입력받은 글자들
done = False #실행됀상태로있게하는 함수만들기

while not done: #만약 done이 아닐경우 done = False (실행됀 상태로 있게하기)
    for letter in word: # LETTER은 word에 있으며
        if letter.lower() in guesses: #만약 letter(소문자)가 guesses에 있다면
            print(letter, end=" ") # 맞춘 글자 출력 및 줄바꿈으로 한줄에 표시
        else: #만약 아니면 
            print("_",end=" ") # _을 그대로 표시
    print("") #글자(단어 글자수보다 1칸많이 불러와서) 마지막을 빈칸으로 표시 및 줄바꿈

    guess = input("allowed error left :{0} \nnext guess: ".format(allowed_error)) #입력받기 및 남은 기회 표시
    guesses.append(guess.lower()) # 입력받은걸 주측에 넣기
    if guess.lower() not in word.lower():  # 주측(소자)가 단어(소자)에 없으면 
        allowed_error -= 1 # 남은 기회에서 1 뺴기
        if allowed_error == 0: # 남은 기회가 0일 경우
            break #정지
    done = True #done함수를 True로 저장 (단어를 맞췄을경우 끝내기)
    for letter in word: # letter은 word에 있으며 (단어를 못마출경우 계속 false로 저장 및 실행상태 유지)
        if letter.lower() not in guesses: # letter(소문자)가 guesses에 없을경우 
            done = False #done함수를 False로 저장
if done: #만약 done함수가 True가 됐을경우
    print ("you find the word \n word is {0}".format(word)) #출력
else:#만약 아니면
    print ("game over \nword is:{0}".format(word)) # 출력

