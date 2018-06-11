import pytest


class Token:
	def __init__(self, typ, value):
		self.typ = typ
		self.value = value


class InterPreter:
	def __init__(self, code):
		self.code = code
		self.pos = -1

	def expression(self):
		while True:
			self.pos += 1

			char = self.code[self.pos]
			print(self.pos, char)

			if self.pos == 0:
				if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
					left = Token('INT', int(char))

			if self.pos == 1:
				if char == '+':
					op = Token('PLUS','+')

			if self.pos == 2:
				print(char, 'ljhb')
				if char in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
					rigth = Token('INT', int(char))

			if self.pos == len(self.code)-1:
				break

		print(locals())
		# return left, rigth
		return left.value + rigth.value



@pytest.mark.parametrize('codetext, expected', (
	('1+2', 1+2),
	('2+3', 2+3),
	('5+3', 5+3),
	('9+7', 9+7),
	))
def test_myversion(codetext, expected):
	interpreter = InterPreter(code=codetext)
	assert interpreter.expression() == expected



if __name__ == '__main__':
	pass

	pytest.main([
		__file__,
		# '-s'
	])

	
	# interpreter = InterPreter(code='1+2')
	# print(interpreter.expression())