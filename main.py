#!/usr/bin/python3

def find_judge(trust: list[int], N: int) -> int:
    """
    In a town judge there are N pple labelled from 1 to N. There is a rumour
    that one of these pple is secretly the town judge.
    If the town judge exists then:
        1. The town judge trusts nobody
        2. Everybody (except for the town judge) trusts the town judge
        3. There is exactly on person that satisfies properties 1 and 2
        
    You are given a trust array, trust[i] = [a, b], representing that the
    person labelled a trusts the person labelled b.
    If the town judge exists return the label of the town judge. Otherwise
    return -1
    """
    
    # create 2 arrays of size N+1 named pple_trusted and is_trusted_by and
    # fill them with zeros
    pple_trusted = [0] * (N+1)
    is_trusted_by = [0] * (N+1)
    
    # loop through the trust array incrementing the 2 arrays whenever a person
    # trusts sb or is trusted by sb
    for i, j in trust:
        pple_trusted[i] += 1
        is_trusted_by[j] += 1
        
    # find the person who trusts nobody and is trusted by N-1 pple
    for i in range(1, N+1):
        if pple_trusted[i] == 0 and is_trusted_by[i] == N-1:
            return i

    return -1

def display_results(N: int, trust: list[int], judge: int):
	is_town_judge = judge >= 0
	print(f"town has {N} people")
	print(f"they trust each other as follows: {trust}")
    
	if is_town_judge:
		print(f"town judge is {judge}")
	else:
		print("there is no town judge")
  
	print()
        

if __name__ == "__main__":
    # Example usage:
    N = 2
    trust = [[1, 2]]
    judge = find_judge(trust, N)
    display_results(N, trust, judge) # judge: 2

    N = 3
    trust = [[1, 3], [2, 3]]
    judge = find_judge(trust, N)
    display_results(N, trust, judge) # judge: 3

    N = 4
    trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    judge = find_judge(trust, N)
    display_results(N, trust, judge) # judge: 3
