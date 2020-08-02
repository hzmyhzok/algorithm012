学习笔记
---

DFS模板<br>
递归写法
`#Python
visited = set() 
def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 
	visited.add(node) 
	# process current node here. 
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)`
