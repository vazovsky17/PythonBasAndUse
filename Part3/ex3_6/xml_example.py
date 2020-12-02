from xml.etree import ElementTree

tree = ElementTree.parse('example_modified.xml')
root = tree.getroot()

greg = root[0]
description = greg.find('description')
greg.remove(description)
tree.write('example_modified.xml')

'''
tree = ElementTree.parse('example_modified.xml')
root = tree.getroot()

greg = root[0]
description = ElementTree.Element('description')
description.text = 'Showed excellent skills during the course.'
greg.append(description)
tree.write('example_modified.xml')
'''

'''
# tree = ElementTree.parse('example_modified.xml')
# root = tree.getroot()
# greg = root[0]
# certificate = greg[2]
# certificate.set('type', 'with distinction')
# tree.write('example_modified.xml')
'''

'''
# tree = ElementTree.parse('example.xml')
# root = tree.getroot()
#
# greg = root[0]
# module1 = next(greg.iter('module1'))
# print(module1, module1.text)
# module1.text = str(float(module1.text) + 30)
# tree.write('example_modified.xml')
'''

'''
# use root = ElementTree.fromstring(string_xml_data) to parse from str

# print(root)
# print(root.tag, root.attrib)

# for child in root:
#     print(child.tag, child.attrib)
# print(root[0][0].text)

# for el in root.iter('scores'):
#     scores_sum = 0
#     for child in el:
#         scores_sum += float(child.text)
#     print(scores_sum)
'''
