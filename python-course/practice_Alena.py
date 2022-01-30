def p(a):
	return a.isalnum()

b = list(filter(p, list(str(-152.352))))

print(b)


#new_s = "".join(filter(is_polindrome, s))