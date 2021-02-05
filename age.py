driving = input('請問你有沒有開過車：')
age = input('請問你的年齡:')
if driving == '有':
	if int(age) >= 18:
		print('你通過測驗了')
	else:
		print('未成年駕駛')
elif driving == '沒有':
	if int(age) >= 18:
		print('去考駕照吧')
	else:
		print('良好市民')
else:
	print('只能輸入有或沒有')