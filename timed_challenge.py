# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

def remove_every_kth(values, k):
    result = []
    for i, val in enumerate(values, start=1):
        if i % k != 0:  # skip every k-th element
            result.append(val)
    return result

print(remove_every_kth([10, 20, 30, 40, 50, 60], 3))  # [10, 20, 40, 50]
print(remove_every_kth([1, 2, 3, 4, 5, 6], 2))       # [1, 3, 5]
print(remove_every_kth([5, 10, 15], 1))              # []
print(remove_every_kth([], 3))                       # []

# Reflection:
# I chose a list because the input is ordered and we need to build a new sequence while removing every k-th element.
# Lists make it easy to add elements and keep them in order, which works well for this task.
# I used enumerate and append, which take O(n) time, to go through each element and keep the ones that are not multiples of k.
# The 30-minute time limit affected how I approached the problem, so I picked a simple and clear solution instead of trying more complicated or optimized methods.
# Under the time pressure, I focused on making the solution correct and easy to read, tested cases like empty lists and k=1,
# and accepted small trade-offs in optimization to make sure the code is understandable and maintainable.
# Overall, this exercise showed me how important it is to balance efficiency, readability, and correctness when coding under a time limit.