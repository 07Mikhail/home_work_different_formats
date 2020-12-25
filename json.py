def open_and_read_files(): # ������� ��� �������� � ������ �����
  import json
  with open('newsafr.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)
    return json_data


def collecting_words(json_data): # ������� ����� ���� ����
  text = '' # ���� ����� �������� ���� �����
  for list_items in json_data['rss']['channel']['items']:
    text += list_items['description']
  return text


def sort_words(text): # ������� ���������� ����
  words_split = text.split(" ") # ��������� ��� ��������� ����� � ������
  unique_words = list(set(words_split)) # ������ ���������� ����
  final_list = [word for word in unique_words if len(word)>=6]
  final_list.sort(key=len, reverse=True)
  dict_for_count = dict()
  for word in final_list:
    word_repeats = words_split.count(word) # count - ������� ����� ��������� word � ��������� words
    dict_for_count[word] = word_repeats
  list_for_count = list(dict_for_count.items())
  list_for_count.sort(key=lambda x: x[1])
  return list_for_count
  

def print_text(list_for_count): # ������� ��� ������ �� ������� 
  for i in list_for_count[-10:]: # ������������ �� ���������������� ������ �� ��������� [-10:]
    print(f'{i[0]}: {i[1]}') # �������� �� ������ �� �������� ��������


print_text(sort_words(collecting_words(open_and_read_files())))