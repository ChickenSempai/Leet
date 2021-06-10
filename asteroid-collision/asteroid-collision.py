class Solution:
    def asteroidCollision(self, aster: List[int]) -> List[int]:
        astack = []

        for ast in aster:
            if ast < 0:
                while len(astack) != 0 and astack[-1] > 0 and abs(ast) > astack[-1]:
                    astack.pop()
                if len(astack) != 0 and astack[-1] > 0:
                    if abs(ast) == astack[-1]:
                        astack.pop()
                else:
                    astack.append(ast)
            else:
                astack.append(ast)
        return astack