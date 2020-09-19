# 毕业总结

### 堆的实现<br>

<pre>
Python
import sys 
class BinaryHeap: 

    def __init__(self, capacity): 
        self.capacity = capacity 
        self.size = 0
        self.Heap = [0]*(self.capacity + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
      
    def parent(self, pos): 
        return pos//2
      
    def leftChild(self, pos): 
        return 2 * pos 
      
    def rightChild(self, pos): 
        return (2 * pos) + 1
      
    def isLeaf(self, pos): 
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
      
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
      
    def heapifyDown(self, pos): 
      
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
      
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.heapifyDown(self.leftChild(pos)) 
      
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.heapifyDown(self.rightChild(pos)) 
      
    def insert(self, element): 
        if self.size >= self.capacity : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
      
        current = self.size 
      
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
      
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
       
    def minHeap(self): 
      
        for pos in range(self.size//2, 0, -1): 
            self.heapifyDown(pos) 
      
    def delete(self): 
      
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.heapifyDown(self.FRONT) 
        return popped 
    def isEmpty(self):
        return self.size == 0
        
    def isFull(self): 
        return self.size == self.capacity
if __name__ == "__main__": 
      
    print('The minHeap is ') 
    minHeap = BinaryHeap(5)
    minHeap.insert(5) 
    minHeap.insert(3) 
    minHeap.insert(17) 
    minHeap.insert(10) 
    minHeap.insert(84) 
    minHeap.insert(19) 
    minHeap.insert(6) 
    minHeap.insert(22) 
    minHeap.insert(9) 
    minHeap.minHeap() 
      
    minHeap.Print() 
    print("The Min val is " + str(minHeap.delete()))
</pre>

### 递归代码模板<br>

<pre>
# Python
def recursion(level, param1, param2, ...): 
    # recursion terminator 
    if level > MAX_LEVEL: 
	   process_result 
	   return 
    # process logic in current level 
    process(level, data...) 
    # drill down 
    self.recursion(level + 1, p1, ...) 
    # reverse the current level status if needed
</pre>

### 分治代码模板<br>

<pre>
# Python
def divide_conquer(problem, param1, param2, ...): 
  # recursion terminator 
  if problem is None: 
	print_result 
	return 

  # prepare data 
  data = prepare_data(problem) 
  subproblems = split_problem(problem, data) 

  # conquer subproblems 
  subresult1 = self.divide_conquer(subproblems[0], p1, ...) 
  subresult2 = self.divide_conquer(subproblems[1], p1, ...) 
  subresult3 = self.divide_conquer(subproblems[2], p1, ...) 
  …

  # process and generate the final result 
  result = process_result(subresult1, subresult2, subresult3, …)
	
  # revert the current level states
</pre>

### DFS 代码模板<br>

<pre>
#递归
#Python
visited = set() 

def dfs(node, visited):
    if node in visited: # terminator
    	# already visited 
    	return 

	visited.add(node) 
	
	# process current node here. 
	...
	for next_node in node.children(): 
		if next_node not in visited: 
			dfs(next_node, visited)
	#非递归
	#Python
	def DFS(self, tree): 
	
		if tree.root is None: 
			return [] 
	
		visited, stack = [], [tree.root]
	
		while stack: 
			node = stack.pop() 
			visited.add(node)
	
			process (node) 
			nodes = generate_related_nodes(node) 
			stack.push(nodes) 
	
		# other processing work
</pre>

### BFS 代码模板<br>

<pre>
# Python
def BFS(graph, start, end):
    visited = set()
	queue = [] 
	queue.append([start]) 
	while queue: 
		node = queue.pop() 
		visited.add(node)
		process(node) 
		nodes = generate_related_nodes(node) 
		queue.push(nodes)
	# other processing work 
</pre>

### 二分查找代码模板<br>

<pre>
# Python
left, right = 0, len(array) - 1 
while left <= right: 
	  mid = (left + right) / 2 
	  if array[mid] == target: 
		    # find the target!! 
		    break or return result 
	  elif array[mid] < target: 
		    left = mid + 1 
	  else: 
		    right = mid - 1
</pre>

### Trie 树代码模板<br>

<pre>
# Python 
class Trie(object):


	def __init__(self): 
		self.root = {} 
		self.end_of_word = "#" 
	 
	def insert(self, word): 
		node = self.root 
		for char in word: 
			node = node.setdefault(char, {}) 
		node[self.end_of_word] = self.end_of_word 
	 
	def search(self, word): 
		node = self.root 
		for char in word: 
			if char not in node: 
				return False 
			node = node[char] 
		return self.end_of_word in node 
	 
	def startsWith(self, prefix): 
		node = self.root 
		for char in prefix: 
			if char not in node: 
				return False 
			node = node[char] 
		return True

</pre>

### 快速排序<br>

<pre>
#Python
def quick_sort(begin, end, nums):
    if begin >= end:
        return
    pivot_index = partition(begin, end, nums)
    quick_sort(begin, pivot_index-1, nums)
    quick_sort(pivot_index+1, end, nums)


def partition(begin, end, nums):
    pivot = nums[begin]
    mark = begin
    for i in range(begin+1, end+1):
        if nums[i] < pivot:
            mark +=1
            nums[mark], nums[i] = nums[i], nums[mark]
    nums[begin], nums[mark] = nums[mark], nums[begin]
    return mark
</pre>

<br>

### 归并排序<br>

<pre>
#Python


def mergesort(nums, left, right):
    if right <= left:
        return
    mid = (left+right) >> 1
    mergesort(nums, left, mid)
    mergesort(nums, mid+1, right)
    merge(nums, left, mid, right)

def merge(nums, left, mid, right):
    temp = []
    i = left
    j = mid+1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i +=1
        else:
            temp.append(nums[j])
            j +=1
    while i<=mid:
        temp.append(nums[i])
        i +=1
    while j<=right:
        temp.append(nums[j])
        j +=1
    nums[left:right+1] = temp
</pre>

<br>

### 堆排序<br>

<pre>
#Python


def heapify(parent_index, length, nums):
    temp = nums[parent_index]
    child_index = 2*parent_index+1
    while child_index < length:
        if child_index+1 < length and nums[child_index+1] > nums[child_index]:
            child_index = child_index+1
        if temp > nums[child_index]:
            break
        nums[parent_index] = nums[child_index]
        parent_index = child_index
        child_index = 2*parent_index + 1
    nums[parent_index] = temp


def heapsort(nums):
    for i in range((len(nums)-2)//2, -1, -1):
        heapify(i, len(nums), nums)
    for j in range(len(nums)-1, 0, -1):
        nums[j], nums[0] = nums[0], nums[j]
        heapify(0, j, nums)
</pre>















