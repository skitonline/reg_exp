from pprint import pprint
import csv
import re


def correct_FIO(contact):
    FIO = contact[0] + ' ' + contact[1] + ' ' + contact[2]
    FIO = re.sub(r'\s+', ' ', FIO)
    FIO = re.split(' ', FIO)
    for i in range(3):
        contact[i] = FIO[i]
    return contact


def correct_number(contact):
    pattern = r'(8|\+7)\s*\(?(\d\d\d)\)?\s*-*(\d\d\d)-*(\d\d)-*(\d\d)\s*\(?(доб.)*\s*(\d*)\)?'
    if 'доб.' not in contact[5]:
        sub = r'+7(\2)-\3-\4-\5'
    else:
        sub = r'+7(\2)-\3-\4-\5 \6\7'
    contact[5] = re.sub(pattern, sub, contact[5])
    return contact


def main():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    pprint(contacts_list)

    # TODO 1: выполните пункты 1-3 ДЗ
    result = [contacts_list[0]]

    for contact in contacts_list:
        if contact[0] == 'lastname':
            continue

        contact = correct_FIO(contact)
        contact = correct_number(contact)

        need_add = True
        for res_contact in result:
            if contact[0] == res_contact[0] and contact[1] == contact[1]:
                for i in range(2, len(contacts_list[0])):
                    if res_contact[i] == '':
                        res_contact[i] = contact[i]
                need_add = False
                break
        if need_add:
            result.append(contact)

    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(result)


if __name__ == "__main__":
    main()