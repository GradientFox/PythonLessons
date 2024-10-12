import networkx as nx
import matplotlib.pyplot as pt
from tkinter import *

graph = nx.MultiDiGraph()

with open('text.txt', 'r', encoding='utf-8') as file:
    text = file.read().replace('.', '').replace(',', '').strip()
    list_text = text.split()

for word in list_text:
    for i in range(1, len(word)):
        sequence = word[0:i]
        if not graph.has_node(sequence):
            graph.add_edge(sequence, word, value=1)
            continue
        if word in graph[sequence].keys():
            graph[sequence][word][0]['value'] += 1
        else:
            graph.add_edge(sequence, word, value=1)

for node in graph.nodes:
    for v in graph[node]:
        temp = graph[node][v][0]
        temp['weight'] = temp['value'] / sum([graph[node][x][0]['value'] for x in graph[node].keys()])
        # использовал заместо sum() len(), но тогда в случаях когда слово встречалось несколько раз,
        # но кроме него самого небыло совпадений, то получалась вероятность больше 1

# nx.draw(graph, with_labels = True)
# pt.show()

enter_word = input()
if enter_word in graph.nodes:
    t = graph[enter_word]
    sorted_nodes = sorted(t.keys(), key=lambda x: t[x][0]['weight'], reverse=True)
    for node in sorted_nodes:
        print("{0} - {1}".format(node, graph[enter_word][node][0]['weight']))
else:
    print('"{0}" - последовательность не встреачалась в тексте.'.format(enter_word))

id = []
def char_validate(d, P):
    if len(id) != 0:
        c.delete(id[0])
        id.pop(0)
    if d == '1' or (d == '0' and len(P) != 0):
        if P in graph.nodes:
            t = graph[P]
            sorted_nodes = sorted(t.keys(), key=lambda x: t[x][0]['weight'], reverse=True)
            id.append(c.create_text(100, 100, text='\n'.join(
                ["{0} - {1}".format(node, graph[P][node][0]['weight']) for node in sorted_nodes])))
        else:
            id.append(c.create_text(100, 100, text='"{0}" - последовательность не встреачалась в тексте.'.format(P)))

    c.pack()
    return True


root = Tk()
root.geometry('300x400')

field_check = (root.register(char_validate), "%d", "%P")
c = Canvas(root)

field = Entry(validate="key", validatecommand=field_check)
field.pack()

root.mainloop()
