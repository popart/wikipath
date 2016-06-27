f_in = open('data/raw/pages.txt', 'r', encoding='utf-8')
f_out = open('data/import/pages.csv', 'w', encoding='utf-8')

i = 1
f_out.write('id:ID|title\n')
for line in f_in:
    f_out.write(str(i) + '|' + line)
    i = i + 1

f_in.close()
f_out.close()

f_in = open('data/raw/links.txt', 'r', encoding='utf-8')
f_out = open('data/import/links.csv', 'w', encoding='utf-8')

f_out.write(':START_ID|:END_ID\n')
for line in f_in:
    nodes = line.split(' ')
    start_node = nodes[0][:-1]
    for end_node in nodes[1:]:
        f_out.write(start_node + '|' + end_node.strip() + '\n')

f_in.close()
f_out.close()
