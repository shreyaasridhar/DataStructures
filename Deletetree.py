from binarysearchtree import BinarySearchTree

def testtree():
    T=BinarySearchTree()
    n=int(raw_input("Enter number of elements: "))
    for i in range(n):
        T.insertElement(int(raw_input("Enter element "+str(i+1)+" : ")))
    x=int(raw_input("Enter the element you want to delete: "))
    T.deleteElement(x)
    print "The tree is:" 
    T.inorderTraverse(T.root)


def main():
    testtree()
        
    
if __name__ == '__main__':
    main()
        
        
    
    
