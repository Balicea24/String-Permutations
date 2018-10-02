def checkPermutation(word1, word2):
    # Permutations must have the same length
    if len(word1) != len(word2):
        return False

    else:
        arrWord1, arrWord2 = list(word1), list(word2)
        return loop(arrWord1, arrWord2)

def loop(arrWord1, arrWord2):
    # If array is empty, it is a permutation
    if arrWord1 or arrWord2 == []:
        return True

    for x in arrWord1:
        for y in arrWord2:
            if x == y:
                # Remove equivalent elements in both arrays
                arrWord1.remove(x)
                arrWord2.remove(y)
                loop(arrWord1, arrWord2)

        # There exists x in arrWord1 such that for all y in arrWord2, x!=y; therefore, not a permutation
        return False

print(checkPermutation('abc', 'cba'))
