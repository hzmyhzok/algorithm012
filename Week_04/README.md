学习笔记
---

DFS模板<br>
递归写法
<pre>
#Python<br>
visited = set()
def dfs(node, visited):
    if node in visited:
    	return 
	visited.add(node) 
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
</pre>
