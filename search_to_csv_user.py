# encode:utf-8
import csv
import glob
from typing import List, Set
from sys import argv


def readfile(filename):
    """Открывает построчно файл с помощью генератора."""
    try:
        with open(filename, "r") as read:
            for list_mail in csv.reader(read, delimiter=";"):
                yield list_mail
    except TypeError as error:
        print("Такого файла не существует")


def filename_glob(path_to_file: str):
    """Glob проходит по папке и ищет заданный файл.

    Если нужен рекурсивный проход укажите: '*/binary_*
    Будет проход относительно той директории, с который был запущен поиск файла.
    """
    try:
        for filename in glob.glob(path_to_file):
            return filename
    except TypeError as error:
        print(f"Не подходящий формат {error}")


def read_lines_file(filename):
    """Загружаем в память полностью весь файл"""

    with open(filename, "r", encoding="utf-8") as read:
        return read.readlines()


def search_users_csv():
    pass


def csv_writer(ready_list_users: list):
    """Записываем данные в csv файл со своими заголовками"""
    # если нужны ковычки в csv то добавить в csv.writer quoting=csv.QUOTE_NONNUMERIC, после lineterminator="\r"

    with open('found_users.csv', 'w', encoding='ansi', newline='') as csv_file:
        file_writer = csv.writer(csv_file, delimiter=";", lineterminator="\r")
        file_writer.writerow(['account', 'dn', 'mailbox', 'RealName', 'cn', 'givenName', 'initials', 'mail', 'sn',
                              'homePostalAddress', 'l', 'st', 'postalCode', 'c', 'homePhone',
                              'facsimileTelephoneNumber', 'mobile', 'o', 'postalAddress', 'l', 'st', 'postalCode',
                              'title', 'ou', 'physicalDeliveryOfficeName', 'telephoneNumber',
                              'facsimileTelephoneNumber', 'officeFax', 'pager'])
        for val in ready_list_users:
            file_writer.writerow(val)


if __name__ == "__main__":
    txt_file_argv: str = argv[1]  # списки почтовых аккаунтов, которые будем искать
    csv_file_argv: str = argv[2]  # в этом файле будем проводить поиск

    mail_user = read_lines_file(filename_glob(txt_file_argv))  # test.txt

    # TODO сделать рефакторинг
    ready_list: list = []
    counter = 0

    while counter < len(mail_user):
        csv_mail_user = readfile(filename_glob(csv_file_argv))  # csv
        for x in csv_mail_user:
            if mail_user[counter].rstrip() in x:
                ready_list.append(x)
        counter += 1

    csv_writer(ready_list)

