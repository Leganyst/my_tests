
n = int(input('Введите количество школьников: '))
languages = {}

while n > 0:
    m = int(input('Введите кол-во школьников в группе: '))
    language = input('Введите языки которые они знают: ').split()
    languages[m] = language

    n -= m 

lang_all = []
for value in languages.values():
    for lang in value:
        lang_all.append(lang)
    
lang_all_set = set(lang_all)
print('Языки, которые знает хотя бы один школьник: ')
print(f'{len(lang_all_set)} - {lang_all_set}')

print('Языки, которые знают все школьники: ')
lang_one = []
count = 0
word = None
for lang in lang_all_set:
    count_for = lang_all.count(lang)
    if count_for > count:
        count = count_for
        word = lang
    elif count_for == count:
        word = lang
        lang_one.append(word)
lang_one.append(word)

print(f'{len(lang_one)} - {lang_one}')