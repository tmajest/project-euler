# http://projecteuler.net/problem=40

nums = map(int, ''.join(map(str, (range(1000000)))))
print nums[1] * nums[10] * nums[100] * nums[1000] * nums[10000] * nums[100000] * nums[1000000]
