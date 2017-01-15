# Output fraction of positive, negative and zero-value elements in a array

sum_pos = 0
sum_zero = 0
sum_neg = 0
for i in arr:
    if i > 0:
        sum_pos += 1
    elif i == 0:
        sum_zero += 1
    else:
        sum_neg += 1
print float(sum_pos) / len(arr)
print float(sum_neg) / len(arr)
print float(sum_zero) / len(arr)
        
