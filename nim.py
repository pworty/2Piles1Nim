from copy import deepcopy

target = 77
n1 = 7
results = [[0] * 2 * target for i in range(2 * target)]
for x in range(target - 1, 0, -1):
    for y in range(target - x - 1, 0, -1):
        nextCodes = [results[x + 1][y], results[2 * x][y], results[x][y + 1], results[x][2 * y]]
        negative = [c for c in nextCodes if c <= 0]
        if negative:
            results[x][y] = -max(negative) + 1
        else:
            results[x][y] = -max(nextCodes)

# Answer  output
print('\t' + ' '.join(list(map(lambda x: str(x).rjust(4, ' '), range(1, target - 1)))))

print('\n'.join(str(index + 1) + '\t' + ' '.join(list(map(lambda x: ('В' + str(x)).rjust(4, ' ') if x > 0 else ('П' + str(x)).replace('-', '').rjust(4, ' '), i[1:target - 1]))) for index, i in enumerate(results[1:target - 1])))
