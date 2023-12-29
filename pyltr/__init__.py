import json

class S:
	def __init__(self, s):
		self.s = s
	def __repr__(self):
		return json.dumps(self.s)

def ltr_map(s, fstr, fslit):
	if isinstance(s, list):
		return [ltr_map(ss, fstr, fslit) for ss in s]
	if isinstance(s, str):
		return fstr(s)
	if isinstance(s, S):
		return fslit(s)

def dump_flat(j):
	if isinstance(j, str):
		if any([ch in " \t\n[]" for ch in j]):
			return json.dumps(j)
		return j
	assert isinstance(j, list)
	j = [dump_flat(jj) for jj in j]
	return "[" + " ".join(j) + "]"

def dump(j):
	if isinstance(j, str):
		assert all([ch not in " \t\n[]" for ch in j])
		return j
	if isinstance(j, S):
		return json.dumps(j.s)
	assert isinstance(j, list)
	j = [dump(jj) for jj in j]
	return "[" + " ".join(j) + "]"

def striphash(s):
	lines = []
	for line in s.split("\n"):
		if not line:
			continue
		if line[0] == "#":
			continue
		lines.append(line)
	return "\n".join(lines)

def parse_flat(s):
	j = parse_slit(s)
	return ltr_map(j, lambda x: x, lambda x: x.s)

def parse_slit(s):
	stack = []
	state = 0
	space = True
	for ch in list(s):
		if state == 1:
			if ch == "\\":
				state = 2
			elif ch == '"':
				stack[-1][-1] = S(stack[-1][-1])
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
			elif ch in "[":
				stack.append([])
				space = True
			elif ch in " \t\n":
				space = True
			elif ch in "]":
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
	raise Exception(len(stack), stack)
