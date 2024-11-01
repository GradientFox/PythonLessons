from  lxml import etree
import json

tree = etree.parse('movies.xml')
root = tree.getroot()
jsn = dict()

def make_dict_from_Element(element):
    t = {
        element.tag: {
            'attrib': dict(element.attrib)
        }
    }
    if len(element.getchildren()) == 0:
        if element.text != "":
            t[element.tag]['text'] = element.text
        return t
    for el in element.getchildren():
        t[element.tag].update(make_dict_from_Element(el))
    return t


jsn = make_dict_from_Element(root)
print(jsn)
with open('res.json', 'w') as f:
    json.dump(jsn, f)
