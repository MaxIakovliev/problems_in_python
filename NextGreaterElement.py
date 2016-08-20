class NextGreaterElement:
    def solution1(a=[]):
        result = []

        for i, ai in enumerate(a):
            curr = ai

            for j in a[i:len(a)]:
                if curr < j:
                    result.append((ai, j))
                    break

                if curr is None:
                    result.append((i, -1))

        if len(result) < len(a):
            result.append((a[len(a) - 1], -1))

        return result


p = NextGreaterElement
arr = [4, 5, 2, 25]
a = p.solution1(arr)

for i, j in a:
    print("{0}->{1}", i, j)
