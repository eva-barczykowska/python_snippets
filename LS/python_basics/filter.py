scores = [96, 47, 113, 89, 100, 102]
# Count the number of elements in scores that are 100 or above.
above_100 = 0
for score in scores:
    if score >= 100:
        above_100 += 1

print(above_100)  # Output: 3

print()

[score for score in scores] # FOR EACH SCORE IN SCORES GRAB THE SCORE
# iterate through the list of scores and grap those that are 100 or above

scores_above_100 = [score for score in scores if score >= 100]
print(len(scores_above_100))  # Output: [100, 102]