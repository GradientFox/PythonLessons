from collections import Counter, defaultdict
from math import log

from typing import Dict


def get_count_unique_words(*file_names) -> dict:
    uniq_words = dict()
    for fileName in file_names:
        with open(fileName, 'r', encoding='utf-8') as file:
            text = file.read()
            uniq_words[fileName] = defaultdict(int)
            for el, num in Counter(text.split()):
                uniq_words[fileName][el] += num
    return uniq_words


def write_dict_in_console(temp: dict) -> None:
    for key, value in temp.items():
        print(key)
        for k, v in value.items():
            print('\t' + k)
            for a, b in v.items():
                print(f'\t\t{a}: {b}')


def create_list_texts(file_names) -> dict:
    temp = dict()
    for file in file_names:
        f = open(file, 'r', encoding='utf-8')
        temp[file] = f.read()
        f.close()
    return temp


def get_tf_idf(*file_names) -> dict:
    count_files = len(file_names)
    all_texts = create_list_texts(file_names)
    response = {el: dict() for el in file_names}
    for file_name in all_texts.keys():
        temp = all_texts[file_name].split()
        for el, enum in Counter(temp).items():
            response[file_name][el] = {
                'enum': enum,
                'tf': enum / len(temp),
            }
    for file_name in response.keys():
        for word in response[file_name].keys():
            response[file_name][word]['idf'] = log(
                count_files / sum([1 for x in response.values() if word in x.keys()]))
            response[file_name][word]['tf-idf'] = response[file_name][word]['tf'] * response[file_name][word]['idf']
    return response


if __name__ == '__main__':
    files = [
        'file1',
        'file2',
    ]
    uniq = get_count_unique_words(*files)
    tf_idf = get_tf_idf(*files)
    write_dict_in_console(tf_idf)
