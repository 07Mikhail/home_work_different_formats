def open_and_read_files(): # функция для открытия и чтения файла
  import xml.etree.ElementTree as ET
  parser = ET.XMLParser(encoding='utf-8')
  tree = ET.parse("newsafr.xml", parser)
  root = tree.getroot()
  return root


def collecting_words(root): # функция сбора всех слов
  news_xml = root.findall("channel/item")
  text = '' # сюда будем собирать весь текст
  for news in news_xml:
    text += news.find("description").text
  return text


def sort_words(text): # функция сортировки слов
  words_split = text.split(" ") # разделяем все собранные слова в список
  unique_words = list(set(words_split)) # список уникальных слов
  final_list = [word for word in unique_words if len(word)>=6]
  final_list.sort(key=len, reverse=True)
  dict_for_count = dict()
  for word in final_list:
    word_repeats = words_split.count(word) # count - выводим число вхождений word в диапазоне words
    dict_for_count[word] = word_repeats
  list_for_count = list(dict_for_count.items())
  list_for_count.sort(key=lambda x: x[1])
  return list_for_count


def print_text(list_for_count): # функция для вывода на консоль 
  for i in list_for_count[-10:]: # интерируемся по отсортированному списку по значениям [-10:]
    print(f'{i[0]}: {i[1]}') # печатаем из списка по индексам значения


print_text(sort_words(collecting_words(open_and_read_files())))