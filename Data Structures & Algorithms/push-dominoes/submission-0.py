class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # pad string with "L" and "R"
        s = "L" + dominoes + "R"
        # initialise final state to empty array
        final = []
        # initialise left pointer to 0
        l = 0

        # loop through s
        for r in range(1, len(s)):
            # check for "."
            if s[r] == ".":
                continue

            # calculate middle
            middle = r - l - 1

            if l > 0:
                final.append(s[l])

            if s[l] == s[r]:
                final.append(s[l] * middle)

            elif s[l] == "L" and s[r] == "R":
                final.append("." * middle)

            else:
                # calculate half
                half = middle // 2
                final.append("R" * half + "." * (middle % 2) + "L" * half)
            l = r

        return "".join(final)