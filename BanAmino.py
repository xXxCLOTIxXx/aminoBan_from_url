import aminofix as amino
client = amino.Client()

print(""" 
Made by Xsarz
GitHub: https://github.com/xXxCLOTIxXx
Telegram Group: https://t.me/DxsarzUnion
Telegram: @DXsarz
YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q/


BANScript
""")

while True:
	try:
		gmail = input("Почта>>")
		password = input("Пароль>>")
		client.login(email=gmail, password=password)
		break
	except:
		print("\nОшибка входа!\n")

while True:
	try:
		url = input('Введите ссылку на пользователя>>')
		comId = client.get_from_code(url).comId
		userId = client.get_from_code(url).objectId
		sub_client = amino.SubClient(comId=comId, profile=client.profile)
		break
	except Exception as ex:
		print(f"Ошибка!\n\n{ex}")

ban = input("Укажите причину бана (Минимум 3 слова)>>")


try:
	sub_client.ban(userId=userId, reason=ban)
	print("Пользователь успешно забанен!")
except:
	print("Ошибка, не удалось забанить пользователя, возможно вы зашли не на аккаунт лидера")
