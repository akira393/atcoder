def bucket(num_list):
    bucket = [0] * 10
    ans = []

    for i in num_list:
        bucket[i] += 1

    for i in range(1, 10):
        ans.extend([i] * bucket[i])

    return ans

num_list = [1, 9, 8, 1, 3, 2, 8, 6, 1, 6]
print(bucket(num_list))
# [1, 1, 1, 2, 3, 6, 6, 8, 8, 9]