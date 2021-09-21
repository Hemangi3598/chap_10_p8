# wapp to read two integers
# and find ans = n1 / n2

print("welcome")
try:
	n1 = int(input(" enter first integer "))
	n2 = int(input(" enter second integer "))
	ans = n1 / n2
except (ValueError, ZeroDivisionError):
	print(" invalid input ")
else:
	print("ans = ", ans)
	
print("bye")

# try with multi except