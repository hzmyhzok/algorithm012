学习笔记
---

DFS模板<br>
递归写法
`#Python<br>
visited = set()<br>
def dfs(node, visited):<br>
    if node in visited: # terminator<br>
    	# already visited <br>
    	return <br>
	visited.add(node) <br>
	# process current node here. <br>
	for next_node in node.children(): <br>
		if next_node not in visited: <br>
			dfs(next_node, visited)`<br>
