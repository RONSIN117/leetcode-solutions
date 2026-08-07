class Solution(object):
    def smallestNumber(self, num, t):
        def get_prime_counts(val):
            counts = {2: 0, 3: 0, 5: 0, 7: 0}
            for p in [2, 3, 5, 7]:
                while val % p == 0:
                    counts[p] += 1
                    val //= p
            return counts, val == 1

        digit_factors = {
            0: {}, 
            1: {},
            2: {2: 1},
            3: {3: 1},
            4: {2: 2},
            5: {5: 1},
            6: {2: 1, 3: 1},
            7: {7: 1},
            8: {2: 3},
            9: {3: 2}
        }

        t_counts, is_valid = get_prime_counts(t)
        if not is_valid:
            return "-1"

        def get_min_digits(counts):
            req = counts.copy()
            res = []
            for d in [9, 8, 7, 6, 5, 4, 3, 2]:
                f_counts, _ = get_prime_counts(d)
                while all(req[p] >= f_counts[p] for p in [2, 3, 5, 7]) and any(f_counts[p] > 0 for p in [2, 3, 5, 7]):
                    res.append(str(d))
                    for p in [2, 3, 5, 7]:
                        req[p] -= f_counts[p]
            return res

        min_digs = get_min_digits(t_counts)
        if len(min_digs) > len(num):
            extra_ones = (len(num) + 1) - len(min_digs)
            return "1" * extra_ones + "".join(sorted(min_digs))

        num_counts = {2: 0, 3: 0, 5: 0, 7: 0}
        has_zero = False
        for ch in num:
            if ch == '0':
                has_zero = True
                break
            fc = digit_factors[int(ch)]
            for p in fc:
                num_counts[p] += fc.get(p, 0)

        if not has_zero and all(num_counts[p] >= t_counts[p] for p in [2, 3, 5, 7]):
            return num

        arr = list(num)
        first_zero = num.find('0')
        if first_zero == -1:
            first_zero = len(num)

        prefix_counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for ch in num:
            fc = digit_factors[int(ch)]
            for p in fc:
                prefix_counts[p] += fc[p]

        for i in range(len(arr) - 1, -1, -1):
            d = int(arr[i])
            fc = digit_factors[d]
            for p in fc:
                prefix_counts[p] -= fc[p]

            space_after = len(num) - 1 - i
            if i > first_zero:
                continue

            for next_d in range(d + 1, 10):
                next_fc = digit_factors[next_d]
                rem = {p: t_counts[p] - prefix_counts[p] - next_fc.get(p, 0) for p in [2, 3, 5, 7]}
                for p in rem:
                    rem[p] = max(0, rem[p])

                needed_digs = get_min_digits(rem)
                if len(needed_digs) <= space_after:
                    fill_ones = space_after - len(needed_digs)
                    prefix = "".join(arr[:i]) + str(next_d) + "1" * fill_ones
                    suffix = "".join(sorted(needed_digs))
                    return prefix + suffix

        extra_ones = (len(num) + 1) - len(min_digs)
        return "1" * extra_ones + "".join(sorted(min_digs))