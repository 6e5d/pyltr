from . import parse_flat, dump_flat
import sys
j = parse_flat(sys.stdin.read())

def pretty_print(j, indent):
	sep = "  "
	if isinstance(j, str):
		print(sep * indent + j)
		return
	assert isinstance(j, list)
	for jj in j:
		if isinstance(jj, str):
			continue
		for jjj in jj:
			if isinstance(jjj, list):
				break
		else:
			continue
		break
	else:
		s = dump_flat(j)
		print(sep * indent + f"{s}")
		return
	#print(end = sep * indent + "[\n")
	for jj in j:
		pretty_print(jj, indent + 1)
	#print(end = sep * indent + "]\n")

pretty_print(j, 0)
