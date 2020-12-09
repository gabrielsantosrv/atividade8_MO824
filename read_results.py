def read_GA_results(filepath):
    with open(filepath) as file:
        times = []
        solutions = []
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if 'Best solution' in line:
                start = len('Best solution: Solution: cost=[')
                end = start+1
                for i in range(start+1, len(line)):
                    if line[i] == ']':
                        end = i
                        break
                solution = float(line[start:end])
                solutions.append(solution)
            elif 'Time:' in line:
                start = len('Time: ')
                time = float(line[start:-3])
                times.append(time)

    return times, solutions

def read_GRASP_results(filepath):
    with open(filepath) as file:
        times = []
        solutions = []
        lines = file.readlines()
        for i, line in enumerate(lines):
            if i == 0:
               start = len('maxVal = Solution: cost = [')
               for i in range(start + 1, len(line)):
                   if line[i] == ']':
                       end = i
                       break
               solution = float(line[start:end])
               solutions.append(solution)
            elif i == len(lines)-1:
                start = len('Time: ')
                time = float(line[start:-3])
                times.append(time)
            else:
                start = len('Time: ')
                for i in range(start + 1, len(line)):
                    if line[i] == ' ':
                        end = i
                        break
                time = float(line[start:end])
                times.append(time)

                for i, c in enumerate(line):
                    if c == '[':
                        start = i+1
                    elif c == ']':
                        end = i
                        break
                solution = float(line[start:end])
                solutions.append(solution)
    return times, solutions

def read_TABU_results(filepath):
    with open(filepath) as file:
        times = []
        solutions = []
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if 'best solution Solution:' in line:
                start = len('best solution Solution: cost=[')
                end = start+1
                for i in range(start+1, len(line)):
                    if line[i] == ']':
                        end = i
                        break
                solution = float(line[start:end])
                solutions.append(solution)

                start = -2
                end = start - 1
                while line[end] != ' ':
                    end -= 1

                time = float(line[end:start])
                times.append(time)

    return times, solutions

if __name__ == '__main__':
    times, solutions = read_TABU_results('results/TABU_results/output_200.txt')
    print('Times [{}]: {}'.format(len(times), times))
    print('Solutions [{}]: {}'.format(len(solutions), solutions))