def part_01():
	lines = [l.strip() for l in open("./data.txt","r").readlines()]
	bounds = {
		"red": 12,
		"green": 13,
		"blue": 14,
	}
	summa = 0
	for line in lines:
		parts = line.split(":")
		s_id = int(parts[0].split(" ")[1])
		sets = parts[1].split(";")
		set_vals = []
		for seta in sets:
			res = seta.strip().split(", ")
			for ra in res:
				clr = ra.split(" ")[1]
				num = int(ra.split(" ")[0])
				set_vals.append(bounds[clr] >= num)
		if all(set_vals):
			summa += s_id
					
	print(summa)

def part_02():
	lines = [l.strip() for l in open("./data.txt","r").readlines()]
	summa = 0
	for line in lines:
		parts = line.split(":")
		s_id = int(parts[0].split(" ")[1])
		sets = parts[1].split(";")
		s_dic = {
			"blue": [],
			"green": [],
			"red": []
		}
		for seta in sets:
			res = seta.strip().split(", ")
			for ra in res:
				clr = ra.split(" ")[1]
				num = int(ra.split(" ")[0])
				s_dic[clr].append(num)
		prd = 1
		for itm in s_dic.values():
			prd *= max(itm)
		summa += prd				
	
	print(summa)
part_01()
part_02()