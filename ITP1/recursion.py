

def counter(i):
	if i != 0:
		print(i)
		return counter(i-1)
	return


def threefive(i, s=0):
	if i % 3 == 0 or i % 5 == 0:
		s += i
	if i > 0:
		return threefive(i-1, s)
	return s


def threefive2(n):
	num = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
	return sum(num)

def fibsum():
	f0 = 1
	f1 = 2
	result = 0

	while (f1 <= 4000000):
		if f1 % 2 == 0:
			print(f1)
			result += f1
		f2 = f0 + f1
		f0 = f1
		f1 = f2
	return result

def fibsumrec(n):
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return fibsumrec(n-1) + fibsumrec(n-2) 



def pow1(x, n):
    if n == 0: return 1
    value = pow1(x, n / 2)
    value *= value
    if n % 2 == 1: value *= x
    return value



def main():
	# counter(10)
	# print(threefive2(10))
	print(fibsum())

if __name__ == "__main__":
	main()





# end	