import xml.etree.ElementTree as ET
parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

news_xml = root.findall("channel/item")
text = '' # сюда будем собирать весь текст
for news in news_xml:
  text += news.find("description").text
words = text.split(" ") # разделяем слова в список
news_set = list(set(words))
final_list = [word for word in news_set if len(word)>=6]
final_list.sort(key=len, reverse=True)
dict_1 = dict()
for word in final_list:
  word_repeats = words.count(word) # count - выводим число вхождений word в диапазоне words
  dict_1[word] = word_repeats
list_dict_1 = list(dict_1.items())
list_dict_1.sort(key=lambda x: x[1])
for i in list_dict_1[-10:]:
  print(f'{i[0]}: {i[1]}')