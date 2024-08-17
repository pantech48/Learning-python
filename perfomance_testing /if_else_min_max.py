import timeit
import random

def if_else_min(a, b):
    if a < b:
        return a
    else:
        return b

def builtin_min(a, b):
    return min(a, b)

def run_test(func, num_runs):
    total_time = 0
    for _ in range(num_runs):
        a, b = random.randint(1, 1000), random.randint(1, 1000)
        start_time = timeit.default_timer()
        func(a, b)
        end_time = timeit.default_timer()
        total_time += (end_time - start_time)
    return total_time / num_runs

num_runs = 1000000
if_else_time = run_test(if_else_min, num_runs)
builtin_time = run_test(builtin_min, num_runs)

print(f"If-else time: {if_else_time:.9f}")
print(f"Built-in time: {builtin_time:.9f}")
print(f"Ratio: if-else is {if_else_time / builtin_time:.2f}x the built-in time")

# Bonus: Test with larger inputs
def if_else_min_list(lst):
    min_val = lst[0]
    for x in lst[1:]:
        if x < min_val:
            min_val = x
    return min_val

def builtin_min_list(lst):
    return min(lst)

large_list = [random.randint(1, 1000) for _ in range(10000)]

if_else_list_time = timeit.timeit(lambda: if_else_min_list(large_list), number=1000)
builtin_list_time = timeit.timeit(lambda: builtin_min_list(large_list), number=1000)

print(f"\nLarge list:")
print(f"If-else time: {if_else_list_time:.6f}")
print(f"Built-in time: {builtin_list_time:.6f}")
print(f"Ratio: if-else is {if_else_list_time / builtin_list_time:.2f}x the built-in time")