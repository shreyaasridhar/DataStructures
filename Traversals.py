from binarysearchtree import BinarySearchTree

def testBST():
    bst1 = BinarySearchTree()
    n=int(raw_input("Enter number of elements: "))
    for i in range(n):
        bst1.insertElement(int(raw_input()))
    print "INORDER:"
    bst1.inorderTraverse(bst1.root)
    print
    print "PREORDER:"
    bst1.preorderTraverse(bst1.root)
    print
    print "POSTORDER:"
    bst1.postorderTraverse(bst1.root)

def main():
    testBST()
        
if __name__ == '__main__':
    main()
