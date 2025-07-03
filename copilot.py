import random

answer = random.randint(1, 10)
attempts = 0

print("1〜10の中で、どの数字を考えているか当ててみてください！")

while True:
    guess = input("あなたの予想: ")
    attempts += 1

    if not guess.isdigit():
        print("数字を入力してください。")
        continue

    guess = int(guess)

    if guess < answer:
        print("もっと大きいですよ。")
    elif guess > answer:
        print("もっと小さいですよ。")
    else:
        print(f"正解！{attempts}回で当たりました！")
        break