import time
import random

num_of_alphabet = 26
num_of_all_chars = 10
num_of_abs_chars = 2
num_max = 2
"""
word = 10
luck_word = 2
MAX = 2
"""

def shutudai(alphabet):
    all_chars = random.sample(alphabet, num_of_all_chars)
    print("対象文字:")
    for c in all_chars:
        print(c, end=" ")
    print()

    abs_chars = random.sample(all_chars, num_of_abs_chars)

    print("表示文字:")
    for c in all_chars:
        if c not in abs_chars:
            print(c, end=" ")
    print()

    return abs_chars

def kaitou(abs_chars):
    num = int(input("欠損文字はいくつあるでしょうか?:"))
    if num != num_of_abs_chars:
        print("不正解です。")
    else:
        print("正解です。それでは具体的に欠損文字を1つずつ入力して下さい")

        for i in range(num):
            w1 = input(f"{i+1}つ目の文字を入力して下さい:")
            if w1 not in abs_chars:

                print("不正解です。")
                return False
            else:
                abs_chars.remove(w1)
        print("全部正解です。")
        return True
        

if __name__ == "__main__":
    st = time.time()
    alphabet = [chr(i+65) for i in range(num_of_alphabet)]

    for i in range(num_max):
        abs_chars = shutudai(alphabet)
        ret = kaitou(abs_chars)

        if ret:
            break
        else:
            print("-"*20)

    ed = time.time()
    print(f"所要時間:{(ed-st):.2f}秒")

"""    while(ct < MAX):
        words = random.sample(alphabet_list, word)
        luck = random.sample(words, luck_word)

        print("対象文字:")
        for i in range(word):
            print(words[i])

        print(luck)

        i = 0
        while words in luck:
            words.remove(words[i])
            print("a")
            i += 1
    
        print("表示文字:")
        print(words)

        st = datetime.datetime.now()
        ans = input("欠損文字はいくつあるでしょうか?:")
    
        if int(ans) == luck_word:
            print("正解です。それでは具体的に欠損文字を1つずつ入力して下さい")
            w1 = input("1つ目の文字を入力して下さい:")
            w2 = input("2つ目の文字を入力して下さい:")

            if w1 in luck and w2 in luck:
                print("不正解です。また、チャレンジしてください")
                print("-----------------------------------------------")
            else:
                print("正解です。")

        ct += 1
"""
