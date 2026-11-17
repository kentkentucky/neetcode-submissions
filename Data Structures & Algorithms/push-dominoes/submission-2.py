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

            # check if left pointer is more than 0
            if l > 0:
                # append left element
                final.append(s[l])

            if s[l] == s[r]:
                # append left element till middle
                final.append(s[l] * middle)

            # check for direction
            elif s[l] == "L" and s[r] == "R":
                # append "." till middle
                final.append("." * middle)

            else:
                # calculate half
                half = middle // 2
                # append accordingly
                final.append("R" * half + "." * (middle % 2) + "L" * half)
            l = r

        # convert array to string and retrun
        return "".join(final)