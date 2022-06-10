N = int(input())

numbers = []

for _ in range(N) : 
    numbers.append(int(input()))

# Bubble Sort
for i in range(len(numbers)) : 
    for j in range(len(numbers)) : 
        if numbers[i] < numbers[j] : 
            numbers[i], numbers[j] = numbers[j], numbers[i]
            
# # Insert Sort
# for i in range(1, len(nums)) :
#     while (i>0) & (nums[i] < nums[i-1]) :
#         nums[i], nums[i-1] = nums[i-1], nums[i]
        
#         i -= 1

for n in numbers : 
    print(n)