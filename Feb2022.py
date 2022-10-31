
words = []
with open('eldrow.txt') as file:
    for word in file:
        words.append(word.rstrip())

for word in words:
    print(word)


def verify(answer, guess):
    result = ['X']*5

    # Iterate over guess once, marking exact matches as green
    remaining_indices = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            result[i] = 'G'
        else:
            remaining_indices.append(i)

    # Iterate over non-green guesses, 
    already_found = []
    for i in remaining_indices:
        if guess[i] in answer and guess [i] not in already_found: ## BUG: could have two yellows, both in wrong spot
            result[i] = 'Y'
            already_found.append(guess[i])

    return result

def is_hard_valid(prev_result, prev_guess, new_guess):
    for i in range(len(prev_result)):
        if prev_result[i] == 'G' and prev_guess[i] != new_guess[i]:
            return False
        elif prev_result[i] == 'X' and prev_guess[i] in new_guess:
            return False
        elif prev_result[i] == 'Y' and prev_guess[i] == new_guess[i]:
            return False
        elif prev_result[i] == 'Y' and prev_guess[i] not in new_guess[:i] + new_guess[i+1:]:
            return False

    return True


for word1 in words:
    for word2 in words:
        for word3 in words:
            print(word1, word2, word3, verify(word1, word2), is_hard_valid(verify(word1, word2), word2, word3))


print('TRACK', 'DIRTY', is_hard_valid(verify('TIGER', 'TRACK'), 'TRACK', 'DIRTY'))
print('TRACK', 'TROMP', is_hard_valid(verify('TIGER', 'TRACK'), 'TRACK', 'TROMP'))
print('TRACK', 'TARDY', is_hard_valid(verify('TIGER', 'TRACK'), 'TRACK', 'TARDY'))
print('TRACK', 'TEPID', is_hard_valid(verify('TIGER', 'TRACK'), 'TRACK', 'TEPID'))
print('TRACK', 'TOWER', is_hard_valid(verify('TIGER', 'TRACK'), 'TRACK', 'TOWER'))
