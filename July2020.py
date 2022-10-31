
def tern2dec(num):
    dec = 0
    j = len(num)-1
    for i in num:
        if i == 'T':
            i = -1
        dec += int(i)*4**j
        j -= 1
    return dec

def read_compare():
    print('Starting to read file.txt')

    # myfunc()
    with open('possible_nums.txt') as file:
        lines = [int(line.rstrip()) for line in file]

    print('Finished reading file.txt')

    temp = [int(line/524293.0) for line in lines if (line/524293.0).is_integer()]

    with open('possible_denominators.txt', 'w') as file3:
        for elem in temp:
            file3.write('%s\n'%elem)


'''
For n up to 22,906,492,245, there exists no n/524293 such that the resulting quotient is 
expressible in the Terniquaternarian base
'''

def get_ranges(lvl = 28):
    pass_num = 524293

    mins = []
    for i in range(lvl):
        num = 0
        for j in range(i):
            num += 4**j
        mins.append(4**i - num)

    maxs = []
    num = 0
    for i in range(lvl):
        num += 4**i
        maxs.append(num)

    arr = []
    for i in range(lvl):
        arr.append([mins[i], maxs[i]])

    print(arr)

    mins = []
    for i in range(lvl):
        num = 0
        for j in range(i):
            num += 4**j
        mins.append(pass_num*(4**i - num))

    maxs = []
    num = 0
    for i in range(lvl):
        num += 4**i
        maxs.append(pass_num*(num))

    arr = []
    for i in range(lvl):
        arr.append([mins[i], maxs[i]])

    print(arr)

def print_ranges():
    with open('ranges.txt') as file:
        lines = file.read().splitlines()

    maxs = 0
    max_array = []
    min_array = []
    trits = 0
    print('Possible ranges:')
    for line in lines:
        split = line.split(',')
        if split[0][0] == 'a':
            trits += 1
        mins = int(split[0][2:])
        
        if mins < maxs:
            print('[',mins,',',maxs,']', maxs-mins, trits)
            min_array.append(mins)
            max_array.append(maxs)
        maxs = int(split[1][:-1])
    return min_array, max_array
        

# print('111111111*524293 = ', tern2dec('111111111')*524293)
# print('1TTTTTTTTTTTTTTTTTT = ', tern2dec('1TTTTTTTTTTTTTTTTTT'))

print('1TTTTTTTT0T1T01010111100001 =', tern2dec('1TTTTTTTT0T1T01010111100001'))
print('1111111110101T1T1 =', tern2dec('1111111110101T1T1'))
print('3002419186324481/5726605517 =', int(3002419186324481/5726605517))

exit()
min_array, max_array = print_ranges()
print(min_array)
print(max_array)


print('Starting to read file.txt')
with open('numerators.txt') as file:
    numerators = [int(line.rstrip()) for line in file]
print('Finished reading file.txt')


numerators_in_range = []
index = 9
found = False

for line in numerators:
    if min_array[index] < line and line < max_array[index]:
        print(line, index)
        numerators_in_range.append(line)
        found = True
    elif line < min_array[index] and found is True:
        index -= 1
    elif index == 0:
        break

with open('file_27.txt') as file:
    lines = [int(line.rstrip()) for line in file]

solns = list(set(lines).intersection(numerators_in_range))
print(solns)

# solns = [3002419186324481, 3002418649448449, 3002417038820353, ...
# 3002410596307969, 3002419079368709, 3002418542492677, 3002417468740613, ...
# 3002416931864581, 3002410489352197, 3002410059431937, 3002409952476165, ...
# 3002408878724101, 3002408341848069, 3002419080417295, 3002418543541263, ...
# 3002417469789199, 3002416932913167, 3002410490400783, 3002409953524751, ...
# 3002419188421653, 3002418651545621, 3002417040917525, 3002410598405141, ...
# 3002410061529109, 3002408450901013, 3002408448803841, 3002419085660225, ...
# 3002418548784193, 3002417475032129, 3002416938156097, 3002417368076357, ...
# 3002410495643713, 3002409958767681, 3002408885015617, 3002408778059845, ...
# 3002408348139585, 3002408342896655, 3002417369124943, 3002410092986689, ...
# 3002408779108431, 3002410497740885, 3002419087757397, 3002418550881365, ...
# 3002417477129301, 3002416940253269, 3002409960864853, 3002408887112789, ...
# 3002408350236757, 3002408482358593, 3002408770719743, 3002408376451407, ...
# 3002408750796609, 3002408879772687, 3002419104534773, 3002418567658741, ...
# 3002417493906677, 3002416957030645, 3002410514518261, 3002409977642229, ...
# 3002408903890165, 3002408367014133, 3002416958079231, 3002410515566847, ...
# 3002417494955263, 3002418568707327, 3002419105583359, 3002409978690815, ...
# 3002419213587717, 3002418676711685, 3002417334521605, 3002417066083589, ...
# 3002410623571205, 3002410086695173, 3002408744505093, 3002408476067077, ...
# 3002419214636303, 3002418677760271, 3002417335570191, 3002417067132175, ...
# 3002410624619791, 3002410087743759, 3002408745553679, 3002408477115663, ...
# 3002408913327439, 3002417340813121, 3002419219879233, 3002418683003201, ...
# 3002417072375105, 3002419112923461, 3002418576047429, 3002417502295365, ...
# 3002416965419333, 3002410522906949, 3002410629862721, 3002409986030917, ...
# 3002408912278853, 3002408375402821, 3002416966467919, 3002410523955535, ...
# 3002419113972047, 3002418577096015, 3002417503343951, 3002409987079503, ...
# 3002419221976405, 3002418685100373, 3002417342910293, 3002417074472277, ...
# 3002410631959893, 3002410095083861, 3002408752893781, 3002408484455765, ...
# 3002408368062719, 3002408904938751, 3002419180032965, 3002418643156933, ...
# 3002417032528837, 3002410590016453, 3002410053140421, 3002408442512325, ...
# 3002417033577423, 3002410591065039, 3002419181081551, 3002418644205519, ...
# 3002410054189007, 3002408443560911, 3002417359687669, 3002408769671157, 3002417360736255]

