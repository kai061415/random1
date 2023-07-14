#產生一個隨機整數1~100 (不要印出來)
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小
#延伸1 印出猜了幾次
#延伸2 讓使用者決定隨機數範圍

import random

first = input('填寫初始值: ')
end = input('填寫最大值: ')
first = int(first)
end = int(end)

r = random.randint(first, end)
count = 0
while True:
	count = count + 1  #計算次數
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('終於猜對了')
		print('總共猜了', count, '次')
		break
	elif num > r:
		print('比答案大')
		print('總共猜了', count, '次')
	elif num < r:
		print('比答案小')
		print('總共猜了', count, '次')		
