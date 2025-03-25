# https://orac2.info/problem/800/
def solve_genius_problem(n, p):
    solved_problems = [0] * n
    total_problems = p
    round_num = 0
 
    # simulation problem

    while total_problems > 0:
        for i in range(n):
            problems_to_solve = (round_num * n) + (i + 1)  
            if total_problems <= problems_to_solve: 
                solved_problems[i] += total_problems
                total_problems = 0
                break
            else:
                solved_problems[i] += problems_to_solve
                total_problems -= problems_to_solve
        round_num += 1
 
    
    max_solved = max(solved_problems)
    person = solved_problems.index(max_solved) + 1  # 1 indexed
 
    return person, max_solved
 
 

n, p = map(int, input().split())
 

person, problems_solved = solve_genius_problem(n, p)
 
print(person, problems_solved)