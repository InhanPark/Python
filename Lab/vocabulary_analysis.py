# vocabulary_analysis.py

# '오만과 편견' 책한권의 단어들을 list 로 정리하는데 0.2초도 안걸림
# 이렇게 정리된 단어를 학습용 단어장 등을 만들수도 있지만, AI 에게 학습시켜 자동 문장 분석이나, 작문을 하게 할 수 있음 (string 관련 기능이 중요한 이유)

import sys  # memory size library
import time # 시간 측정 library
import re   # 정규식 사용 library

def get_list_lower(target_file):
    """책 한권의 단어를 정리하여 list 로 만들어 줌"""
    temp = []
    word = []    
    with open(target_file, mode='r', encoding='UTF8') as f:  # file 을 열어서
        temp = f.read().split()
    #'temp' list 의 단어들을 하나씩 가져다가 정리해서 word list 에 저장
    for w in temp:  #'temp' list 의 단어들을 하나씩 가져다가
        word += [re.sub('[^A-Za-z]', '', w.strip()).lower()]
        # w.strip() 으로 단어 좌우의 공백을 없애고
        # re.sub('[^A-Za-z]', '', w.strip()) 정규식을 사용하여 특수문자, 숫자등 제거
        # .lower() 마지막으로 소문자로 바꾸어 list 에 추가     
    word = list(filter(None, word)) # 리스트 중 비어있는 item 지우기
    #print(temp[11:30])  # 'temp' list 에 저장된 원래 내용
    #print(word[11:30])  # 'words' list 에 저장된 수정 내용
    del temp # 사용하고난 list 삭제
    return word

def voca_analysis(word_list):
    """list 의 단어를 중복제거하고 순서대로 정리한 list 를 만들어줌"""
    voca = []
    voca = sorted(list(set(word_list)))
    # word_list 를 set 으로 바꾸면 중복된 단어가 없어짐
    # set 을 다시 list 로 바꾸면 alphabet 순으로 sort 를 할 수 있음
    return voca

if __name__ == '__main__':
    book_name = "./pride_and_prejudice.txt"
    
    start = time.time() # core 시작
    word_list = get_list_lower(book_name)
    voca_list = voca_analysis(word_list)
    end = time.time()   # core 종료

    print(voca_list)
    print("word size (갯수)", len(word_list))  # 'word_list' 의 단어 갯수
    print("voca size (갯수)", len(voca_list))  # 'voca_list'의 단어 갯수
    print("word list size (MB) ", sys.getsizeof(word_list)/1000000) # 'word_list' 가 차지하는 memory size
    print(f"core 실행시간   (sec) {end - start:.5f}") # core 를 실행하는데 걸린 시간