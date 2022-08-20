import random #random 함수 불러오기
from words import word_list #words.py파일에서 word_list 불러오기

def get_word(): #get_world() 함수 만들기(word_list에서 단어 선택)
    word = random.choice(word_list) #word_list에서 하나 선택하고 word에 저장
    return word.upper() #word함수를 대문자로 밖으로 던지기

def play(word): #play함수 만들기
    word_completion = "_" * len(word) #단어수만큼 밑줄치기
    guessed = False # 
    guessed_letters = [] #입력받은(주측한) (한자리)글자들
    guessed_words = [] #입력받은(주측한) 단어
    tries = 6 #총 시도가능한 회수
    print ("start game") # 게임 시작이라고 출력
    print (display_hangman(tries)) # 남은 시도회수 표시
    print (word_completion) # 밑줄 표시
    print ("\n") # 줄바꿈 (guess함수에서 출력한 텍스트랑 안붙아기)
    
    while not guessed and tries > 0: #guessed가 true가 아니면서 tries이 0보다 많을 경우
        guess = input("please guess a letter or words: ").upper() #입력받기(큰글자로)
        if len(guess) == 1 and guess.isalpha(): #입력값이 한자리 그리고 글자일 경우
            if guess in guessed_letters: #만약 입력값이 guessed_letter에 있을경우
                print ("you already guessed the letters", guess) #출력
            elif guess not in word: #입력값이 정답단어가 아니였을경우 
                print (guess, "is not in the word") #출력
                tries -= 1 #남은 시도회수에서 하나 뺴기
                guessed_letters.append(guess) #입력값을 guess_letter에 넣기
            else: #아니면
                print ("you choose: {0}".format(guess)) #단어 출력
                guessed_letters.append(guess) #입력받은 값을 guessed_letters에 넣기
                word_as_list = list(word_completion) #단어만킁 밎출진 것을 리스트화하소 word_as_list 저장
                indices = [i for i, letter in enumerate(word) if letter == guess] #letter에 단어글자들이 guess와 맞을경우 만 저장
                for index in indices: #index은 indices에 있음
                    word_as_list[index] = guess #word_As_list[index을 리스트화]에 guess의 값에 저장
                word_completion = "".join(word_as_list) #word_completion(단어수많큼 및줄 친곳에)에 word_as_list(받은값(정답 글자))을 넣기
                if "_" not in word_completion: #만약 및줄이 word_completion에 없을경우
                    guessed = True #guess의 값을 True로 저장(게임 끝내기)
        elif len(guess) == len(word) and guess.isalpha(): #받은단어의 글자수가 정답단어의 글자수랑 같고 그리고 글자일경우
            if guess in guessed_words: #만약 받은 값이 guessed_words에 있을경우
                print("you already writed:", guess) #출력
            elif guess != word: #만약 받은 글자가 단어랑 같지않을 경우
                print(guess, "is not the word") #출력
                tries -= 1 #남은 기회에서 1 뺴기
                guessed_words.append(guess) #guessed_words에 넣기
            else:#만약 아니면
                guessed = True #guessed값을 True로 저장 (끝내기)
                word_completion = word #word_copmletio(단어수로 및줄 친것))에 단어를 저장    
        else:#아니면
            print("not a valid guess") #출력
        print (display_hangman(tries)) #출력
        print (word_completion) #출력
        print ("\n") #출력
    if guessed: #guesssed가 true 일경우 
        print ("you win") # 출력
    else: #아니면
        print ("game over\nword is:",word) # 출력

def display_hangman(tries): #남은 도전회수에 따라 리스트에서 출력
    stages = [1,2,3,4,5,6,7] # stage함수에서 저장
    return stages[tries] # stage안에 남은 도전회수에 따라 저장됀값을 밖으로 던지기

def main(): # main 함수 만들기
    word = get_word() #word함수는 선택됀 단어랑 같음
    play(word)#play(word) 함수 불러오기
    while input("play again? (y/n)").lower() == "y": #입력받은 값이 y랑 같을경우
        word = get_word() #word는 새로 선택받은 값이랑 같음
        play(word) #play함수 호출

if __name__ == "__main__": #만약 직접 실행했을 경우
    main()   # main함수 호출