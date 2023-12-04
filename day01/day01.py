import re


def part_1():
	summr = 0
	for l in open("input.txt","r").readlines():
		l = l.strip()
		o = re.sub("[A-Za-z]","",l)
		summr += int(o[0] + o[-1])
	print(summr)

def part_2():
	summa = 0
	word_nums = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	for l in open("willy_input.txt","r").readlines():
		l = l.strip()
		first_n = None
		for i in range(len(l),0,-1):
			try:
				first_n = int(l[i])
			except:
				spliced = l[:i]
				for i,w in enumerate(word_nums):
					if spliced.endswith(w):
						first_n = i
						break
			if first_n:
				break
		last_n = None
		for i in range(len(l)):
			try:
				last_n = int(l[i])
			except:
				spliced = l[i:]
				for i,w in enumerate(word_nums):
					if spliced.startswith(w):
						last_n = i
						break
			if last_n:
				break
		if not first_n:
			first_n = last_n
		summa += int(f"{last_n}{first_n}")
	print(summa)
		


part_2()
