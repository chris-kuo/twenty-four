import sys

class Expression():
	def __init__(self, value, exp=''):
		self.value = value
		self.exp = f'{value}' if exp == '' else exp

	def value(self):
		return self.value

	def expression(self):
		return self.exp

	def __lt__(self, other) -> bool:
		return (self.value, self.exp) < (other.value, self.exp)

	def __eq__(self, other) -> bool:
		if type(other) is int or type(other) is float:
			return self.value == other
		if type(other) is Expression:
			return self.value == other.value

	def __hash__(self):
		return hash((self.value, self.exp))

	def __str__(self):
		return self.exp

	def __float__(self):
		return float(self.value)

	def __add__(self, other):
		new_val = self.value + other.value
		new_exp = f'({self.exp} + {other.exp})'
		return Expression(new_val, new_exp)

	def __mul__(self, other):
		new_val = self.value * other.value
		new_exp = f'({self.exp} * {other.exp})'
		return Expression(new_val, new_exp)		

	def __sub__(self, other):
		new_val = self.value - other.value
		new_exp = f'({self.exp} - {other.exp})'
		return Expression(new_val, new_exp)

	def __truediv__(self, other):
		new_val = self.value / other.value
		new_exp = f'({self.exp} / {other.exp})'
		return Expression(new_val, new_exp)


class TwentyFour():
	@staticmethod
	def combine(a: Expression, b: Expression) -> [Expression]:
		'''
		Return all combinations of a and b using +, -, *, and / operator
		'''
		combos = set()
		combos.add(a + b)
		combos.add(a - b)
		combos.add(b - a)
		combos.add(a * b)
		if a != 0:
			combos.add(b / a)
		if b != 0:
			combos.add(a / b)
		return combos

	@staticmethod
	def reduce(exps: [Expression]) -> [[Expression]]:
		# Reduce the number of expressions by selecting one expression, and return 
		# the union of its combination with other remaining expressions
		N = len(exps)
		result = []
		for i in range(N-1):
			for j in range(i+1, N):
				others = exps[:i] + exps[i+1:j] + exps[j+1:]
				for exp in TwentyFour.combine(exps[i], exps[j]):
					result.append(tuple(sorted((exp,) + others)))
		return list(set(result))

	@staticmethod
	def solve(nums: [int], target: int=24) -> [str]:
		if not nums or len(nums) == 0:
			return []
		nums.sort()
		nums = tuple(nums)
		result = TwentyFour.solve_24(tuple(Expression(num) for num in nums), target)
		return result
	
	@staticmethod
	def solve_24(exps: [Expression], target: int=24):
		if len(exps) == 1: # only 1 number left
			return [str(exps[0])] if exps[0] == target else [] 
		# more than 2 number
		# reduce the number of values in nums, and solve recursively
		candidates = TwentyFour.reduce(exps)
		result = []
		for candidate in candidates:
			result += TwentyFour.solve_24(candidate, target)
		return result

	@staticmethod
	def is_solveable(nums: [int], target: int=24):
		nums_list = [tuple(nums)]
		for _ in range(len(nums) - 1):
			nums_list = [reduced for nums in nums_list for reduced in TwentyFour.reduce(nums)]
		return any(nums[0] == target for nums in nums_list)

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('a', help='First number', type=int)
	parser.add_argument('b', help='Second number', type=int)
	parser.add_argument('c', help='Third number', type=int)
	parser.add_argument('d', help='Fourth number', type=int)
	parser.add_argument('-t', '--target', help='The target number. For the game of TwentyFour it is 24', type=int)
	parser.add_argument('-s', '--solution', help='Print the solutions', action='store_true')
	args = parser.parse_args()
	nums = [args.a, args.b, args.c, args.d]
	target = args.target if args.target else 24
	print(f"{nums} is {'' if TwentyFour.is_solveable(nums, target) else 'not '}solveable")
	if args.solution:
		print('\n'.join(TwentyFour.solve(nums, target)))


	# nums = [1,2,3,4]
	# print()
	# print(f"{nums} is {'' if TwentyFour.is_solveable(nums) else 'not '}solveable")
	# print('\n'.join(TwentyFour.solve(nums)))

	# nums = [1,4,6,7]
	# print()
	# print(f"{nums} is {'' if TwentyFour.is_solveable(nums) else 'not '}solveable")
	# print('\n'.join(TwentyFour.solve(nums)))

	# nums = [7,2,8,9]
	# print()
	# print(f"{nums} is {'' if TwentyFour.is_solveable(nums) else 'not '}solveable")
	# print('\n'.join(TwentyFour.solve(nums)))

	# nums = [7,2,9,9]
	# print()
	# print(f"{nums} is {'' if TwentyFour.is_solveable(nums) else 'not '}solveable")
	# print('\n'.join(TwentyFour.solve(nums)))