def isBST(root):
    a=[]
    d=inorder(root,a)
    res=sorted(d)
    if(res==d):
        return(1)
    else:
        return(0)
    
def inorder(root,arr):
    if(root):
        inorder(root.left,arr)
        arr.append(root.data)
        inorder(root.right,arr)
    return(arr)