"""利用BFS获得最短路径"""
def BFS(graph,s,t):
    import queue
    temp=queue.Queue()
    temp.put(s)
    visited=[False for i in range(t+1)]
    visited[s]=True
    parent=[-1 for i in range(t+1)]
    while temp.empty() is False:
        current=temp.get()
        for i in range(t):
            if graph[current][i]!=0 and visited[i] is False:
                temp.put(i)
                visited[i]=True
                parent[i]=current
        if graph[current][t]>0:
            parent[t]=current
            return parent
    return None
def printresult(cutGraph,graph,t):
    for i in range(t):
        for j in range(t+1):
            if graph[i][j]>cutGraph[i][j]:
                print(i,'->',j,' ',graph[i][j]-cutGraph[i][j])

def maxflow(graph,s,t):
    cutGraph=[[None for i in range(t+1)] for j in range(t+1)]
    for i in range(t+1):

        for j in range(t+1):
            cutGraph[i][j]=graph[i][j]
    while True:
        path=BFS(cutGraph,s,t)
        if path is None:
            printresult(cutGraph,graph,t)
            return
        i=t
        min=float("inf")
        """获得路径上的最小值"""
        while path[i]!=-1:
            if cutGraph[path[i]][i]<min:
                min=cutGraph[path[i]][i]
            i=path[i]
        """更新cutgraph的图"""
        i=t
        while path[i]!=-1:
            cutGraph[path[i]][i]-=min
            cutGraph[i][path[i]]+=min
            i=path[i]

def main():
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]
    maxflow(graph,0,5)

main()