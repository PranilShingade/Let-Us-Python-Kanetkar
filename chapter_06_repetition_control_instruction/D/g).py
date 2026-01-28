# Write a program to print all prime numbers from 1 to 300

for num in range(2, 301):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# Output:
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97
# 101
# 103
# 107
# 109
# 113
# 127
# 131
# 137
# 139
# 149
# 151
# 157
# 163
# 167
# 173
# 179
# 181
# 191
# 193
# 197
# 199
# 211
# 223
# 227
# 229
# 233
# 239
# 241
# 251
# 257
# 263
# 269
# 271
# 277
# 281
# 283
# 293

