def open_and_read_files(): # ������� ��� �������� � ������ �����
  import xml.etree.ElementTree as ET
  parser = ET.XMLParser(encoding='utf-8')
  tree = ET.parse("newsafr.xml", parser)
  root = tree.getroot()
  return root


def collecting_words(root): # ������� ����� ���� ����
  news_xml = root.findall("channel/item")
  text = '' # ���� ����� �������� ���� �����
  for news in news_xml:
    text += news.find("description").text
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