def Traverse(treeList, tmpStr, dict):
    lchild = treeList[0]
    rchild = treeList[1]
    if isinstance(lchild, int):
        tmpStr += '0'
        # print lchild, tmpStr
        dict[lchild] = tmpStr
        tmpStr = tmpStr[:-1]
    else:
        # print lchild
        tmpStr += '0'
        Traverse(lchild, tmpStr, dict)
        tmpStr = tmpStr[:-1]
    if isinstance(rchild, int):
        tmpStr += '1'
        # print rchild, tmpStr
        dict[rchild] = tmpStr
    else:
        # print rchild
        tmpStr += '1'
        Traverse(rchild, tmpStr, dict)
