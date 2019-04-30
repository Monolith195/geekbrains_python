# 4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode).

words = ["разработка", "администрирование", "protocol", "standard"]

for word in words:
    encode_word = word.encode('utf-8')
    print(encode_word)
    decode_word = encode_word.decode('utf-8')
    print(decode_word, "\n")
