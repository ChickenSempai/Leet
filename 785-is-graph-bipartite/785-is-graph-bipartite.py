class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = []
        for i in range(len(graph)):
            colors.append(0)
        
        
        def recolor(i, color):
            # print(i, colors[i], color)
            if colors[i] == color:
                return True
            if colors[i] == -color:
                return False
            #uncolored
            colors[i] = color
            
            for nbr in graph[i]:
                if recolor(nbr, -color) == False:
                    return False
            return True
        
        # print(colors)
        bipartite = True
        res = True
        for i in range(len(graph)):
            if len(graph[i])>0 and colors[i] == 0:
                res = res and recolor(i,1)
        return res