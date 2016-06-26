f_out = open('data/pages.csv', 'w')
f_in = open('data/pages_short.txt', 'r')

i = 1
for line in f_in:
	f_out.write(str(i) + '|' + line)
	i = i + 1

f_out.close()
f_in.close()

f_out = open('data/links.csv', 'w')
f_in = open('data/links_short.txt', 'r')

for line in f_in:
	nodes = line.split(' ')
	start_node = nodes[0][:-1]
	for end_node in nodes[1:]:
		f_out.write(start_node + '|' + end_node.strip() + '\n')

f_out.close()
f_in.close()
