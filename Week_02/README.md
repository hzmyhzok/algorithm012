# 学习笔记 #
---

## 二叉树的前序遍历 ##<br>
<pre>
#递归
def preorder(root,res=[]):
  if not root:
    return
  res.append(root.val)
  preorder(root.left,res)
  preorder(root.right,res)
  return res
</pre>
<pre>
#迭代
def preorder(root):
  res=[]
  if not root: 
    return []
  stack=[root]
  while stack:
    node=stack.pop()
    res.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node,left)
  return res
</pre>
## 二叉树的中序遍历 ##<br>
<pre>
#递归
def inorder(root,res=[]):
  if not root:
    return
  inorder(root.left,res)
  res.append(root.val)
  inorder(root.right,res)
  return res
</pre>
<pre>
#迭代
def inorder(root):
  stack=[]
  node=root
  res=[]
  while stack or node:
    while node:
      stack.append(node)
      node=node.left
    node=stack.pop()
    res.append(node.val)
    node=node.right
  return res
</pre>
## 二叉树的后序遍历 ##<br>
<pre>
#递归
def laorder(root,res=[]):
  if not root:
    return
  laorder(root.left,res)
  laorder(root.right,res)
  res.append(root.val)
  return res
</pre>
<pre>
#迭代
def laorder(root):
  stack=[root]
  res=[]
  while stack:
    node=stack.pop()
    if node.left:
      stack.append(node.left)
    if node.right:
      stack.append(node.right)
    res.append(node.val)
  return res[::-1]
</pre>