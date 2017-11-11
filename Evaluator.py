'''
Evaluator file that implements the operation codes.
'''

def is_number(x):
	try:
		float(x)
		return True
	except ValueError:
		return False

def add(x1, x2):
	return float(x1) + float(x2)

def sub(x1, x2):
	return float(x1) - float(x2)

def mul(x1, x2):
	return float(x1) * float(x2)

def div(x1, x2):
	return float(x1) / float(x2)

def evaluate(expr=[]):
	if (expr[1] == "+"): return add(expr[0], expr[2])
	if (expr[1] == "-"): return sub(expr[0], expr[2])
	if (expr[1] == "*"): return mul(expr[0], expr[2])
	if (expr[1] == "/" and float(expr[2]) != 0): return div(expr[0], expr[2])
	return -1