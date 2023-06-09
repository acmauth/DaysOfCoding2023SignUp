import sys

class Basketball:
    def can_split_teams(self, teams, group1, group2, index):
        if index == len(teams):
            if len(group1) == len(group2) and sum(group1) == sum(group2):
                return True
            else:
                return False

        group1.append(teams[index])
        if self.can_split_teams(teams, group1, group2, index + 1):
            return True
        group1.pop()

        group2.append(teams[index])
        if self.can_split_teams(teams, group1, group2, index + 1):
            return True
        group2.pop()

        return False

    def run(self, test_case):
        # n = int(input("Enter the number of teams: "))
        data = []
        try:
            data = test_case.split(" ")
            n = int(data[0])
            # print(data[0])

            if n < 2:
                return "Wrong Input! Please notice that the number of teams must be greater than 2. Here is an acceptable test case: 4 1 0 0 1 1 0 0 1 "

            if 2 * n != len(data) - 1:
                return "Wrong Input! Too few/many arguments. Make sure the number of teams matches the number of wins and losses. Here is an acceptable test case: 4 1 0 0 1 1 0 0 1"

            for i in range(0, len(data) - 1):
                data[i] = data[i+1]

        except Exception:
            return "Wrong Input! It must contain only numeric and positive data in ONE line.Here is an acceptable test case: 4 1 0 0 1 1 0 0 1"

        teams = []

        # print(data)
        index = 0
        for i in range(0, n):
            try:
                # print(data[index], data[index+1])
                W, L = map(int, f"{data[index]} {data[index + 1]}".split(" "))
                teams.append(W - L)
                index += 2
                if W < 0 or L < 0:
                    return "Wrong Input! It must contain only numeric and positive data in ONE line.Here is an acceptable test case: 4 1 0 0 1 1 0 0 1"
            except Exception:
                return "Wrong Input! It must contain only numeric and positive data in ONE line.Here is an acceptable test case: 4 1 0 0 1 1 0 0 1"

        if self.can_split_teams(teams, [], [], 0):
            return "Yes"
        else:
            return "No"

