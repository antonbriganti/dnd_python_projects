__author__ = 'AntonBriganti'

#file = open('all_class_features.txt', 'r')
file = open('barbarian.txt', 'r')
file_list = file.read().split('\n')
file.close()
file_list.pop()

'''
# stating when you get the feature
time = []
lvl = 1
for line in file_list:
    tmp = ''
    tmp_list = []
    for char in line:
        if char != ',':
            tmp += char
        else:
            tmp_list.append(tmp)
            tmp = ''

    time.append(['Level ' + str(lvl) + ':', tmp_list])
    lvl += 1

for feat in time:
    print(feat[0], feat[1])
'''

# list of features at certain level
features = []

for line in file_list:
    tmp = ''
    space = False
    for char in line:
        if space:
            space = False
        elif char != ',':
            tmp += char
        else:
            features.append(tmp)
            tmp = ''
            space = True

for i in range(len(features)):
    ind = ''
    if features[i][0] == '[':
        for char in features[i][0]:
            if char == ']':
                break
            if char != '[':
                ind += char
        features[int(ind)] = features[i][0]
        features.pop(int(ind))

for feat in features:
    print(feat)



# keep note of which index to replace at in text file?
