class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
            if not bank: return -1
            visited, batch, mut_gen = {start}, [start], 0
            while batch:
                next_batch = []
                for item in batch:
                    if item == end:
                        return mut_gen

                    for i in range(len(item)):
                        for j in ['A', 'C', 'G', 'T']:
                            mut = item[:i] + j + item[i+1:]
                            if mut not in visited and mut in bank:
                                visited.add(mut)
                                next_batch.append(mut)
                batch = next_batch
                mut_gen += 1
            return -1