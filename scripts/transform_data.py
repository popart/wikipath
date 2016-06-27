f_in = open('data/raw/pages.txt', 'r', encoding='utf-8')
f_out = open('data/import/pages.csv', 'w', encoding='utf-8')

i = 1
batch = ''
batch_size = 0

for line in f_in:
    batch = batch + str(i) + '|' + line
    i = i + 1
    batch_size = batch_size + 1
    if batch_size == 1000:
        f_out.write(batch)
        batch_size = 0

if len(batch) > 0:
    f_out.write(batch)

f_in.close()
f_out.close()

f_in = open('data/raw/links.txt', 'r', encoding='utf-8')
f_out = open('data/import/links.csv', 'w', encoding='utf-8')

batch = ''
batch_size = 0

for line in f_in:
    nodes = line.split(' ')
    start_node = nodes[0][:-1]
    for end_node in nodes[1:]:
        batch = batch + start_node + '|' + end_node.strip() + '\n'
        batch_size = batch_size + 1

        if batch_size == 1000:
            f_out.write(batch)
            batch_size = 0

if batch_size > 0:
    f_out.write(batch)

f_in.close()
f_out.close()
