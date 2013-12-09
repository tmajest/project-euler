
nums = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 
        6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten',
        11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy',
        80:'eighty', 90:'ninety', 1000:'one thousand'}

# Add 21 - 99
for i in range(20, 100, 10):
    for j in range(1, 10):
        nums[i + j] = '{0} {1}'.format(nums[i], nums[j])

# Add 100, 200, ...
for i in range(1, 10):
    nums[i * 100] = '{0} hundred'.format(nums[i])

# Add 101-999
for i in range(100, 1000, 100):
    for j in range(1, 100):
        nums[i + j] = '{0} and {1}'.format(nums[i], nums[j])


# print total letter count
print len(''.join(nums[i] for i in range(1, 1001)).replace(' ', ''))
