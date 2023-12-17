import json

class Slit:
	def __init__(self, s):
		self.s = s
	def __repr__(self):
		return json.dumps(self.s)

def ltr_map(s, fstr, fslit):
	if isinstance(s, list):
		return [ltr_map(ss, fstr, fslit) for ss in s]
	if isinstance(s, str):
		return fstr(s)
	if isinstance(s, Slit):
		return fslit(s)

def parse(s):
	stack = []
	state = 0
	space = True
	for ch in list(s):
		if state == 1:
			if ch == "\\":
				state = 2
			elif ch == '"':
				stack[-1][-1] = Slit(stack[-1][-1])
				state = 0
				space = True
			else:
				stack[-1][-1] += ch
		elif state == 2:
			if ch == "n":
				stack[-1][-1] += "\n"
			elif ch == "t":
				stack[-1][-1] += "\t"
			else:
				stack[-1][-1] += ch
			state = 1
		elif state == 0:
			if ch == '"':
				stack[-1].append("")
				state = 1
				space = False
			elif ch in "[({":
				stack.append([])
				space = True
			elif ch in " \t\n":
				space = True
			elif ch in "])}":
				last = stack.pop()
				if len(stack) == 0:
					return last
				stack[-1].append(last)
				space = True
			else:
				if space:
					stack[-1].append(ch)
				else:
					stack[-1][-1] += ch
				space = False
	raise Exception(stack)
