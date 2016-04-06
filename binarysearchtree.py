from treevis import*
import math
class BinarySearchTree:

    """
        This defines the node class. The children can be individually declared or stored
        in a list. We are adding a pos value to help with visualization
    """
    class node:
        def __init__(self):
            self.element = 0
            self.leftchild = None
            self.rightchild = None
            self.pos = -1
            self.parent = None

    """
        This initializes the binary search tree. ht is the height of the tree, sz is the
        number of nodes. You may define this appropriately.
    """
    def __init__(self):
        self.sz = 0
        self.root = None
        self.ht = 0
        self.sum=0

    """
        This method implements the functionality of finding an element in the tree. The function
        findElement(e) finds the node in the current tree, whose element is e. Depending on the
        value of e and in relation to the current element visited, the algorithm visits the left
        or the right child till the element is found, or an external node is visited. Your
        algorithm can be iterative or recursive

        Output: True if tree contains e or False if e not present in T
    """
                 
    def findElement(self,e,curnode):
        while (curnode.element != e and (curnode.leftchild!=None or curnode.rightchild!=None)):
            if (curnode.element > e):
                if  (curnode.leftchild != None):
                    curnode = curnode.leftchild
                else:
                    return curnode
            elif (curnode.element < e):
                if (curnode.rightchild != None):
                    curnode = curnode.rightchild
                else:
                    return curnode
        if (curnode.element == e):
            #print True
            return curnode
        elif (curnode.leftchild==None or curnode.rightchild ==None):
            #print False
            return curnode

    """
        This method implements insertion of an element into the binary search tree. Using the
        findElement(e) method find the position to insert, and insert a node with element e,
        as left or right child accordingly
        
    """
    def insertElement(self,e):
        visnode = visNode()
        if self.root == None:
            self.root = self.node()
            self.root.element = e
            self.root.pos = 1
            visnode.drawnode(self.root.element,0,self.root.pos)
            return
        else:
            curnode = self.findElement(e,self.root)
            #print curnode.element, ":", e
            if (curnode.element > e):
                curnode.leftchild = self.node()
                curnode.leftchild.pos = curnode.pos*2
                curnode.leftchild.element = e
                curnode.leftchild.parent = curnode
                ht1 = math.floor(math.log(curnode.leftchild.pos,2))
                if curnode == self.root:
                    self.root.leftchild=curnode.leftchild
                    self.root.leftchild.parent = self.root
                visnode.drawnode(curnode.leftchild.element,ht1,curnode.leftchild.pos)
                return
            elif (curnode.element < e):
                curnode.rightchild = self.node()
                curnode.rightchild.element = e
                curnode.rightchild.parent = curnode
                curnode.rightchild.pos = curnode.pos*2+1
                ht1 = math.floor(math.log(curnode.rightchild.pos,2))
                if curnode==self.root:
                    self.root.rightchild=curnode.rightchild
                    self.root.rightchild.parent = self.root
                visnode.drawnode(curnode.rightchild.element,ht1,curnode.rightchild.pos)
                return
                
    """
        This method inorderTraverse(self,v) performs an inorder traversal of the BST, starting
        from node v which is initially the root and prints the elements of the nodes as they
        are visited. Remember the inorder traversal first visits the left child, followed by
        the parent, followed by the right child. This could be used to print the tree.
    """
    def inorderTraverse(self,v):
        curnode = v
        if (curnode.leftchild != None):
            self.inorderTraverse(curnode.leftchild)
        print curnode.element,
        if (curnode.rightchild!=None):
            self.inorderTraverse(curnode.rightchild)

    def preorderTraverse(self,v):
        curnode = v
        print curnode.element,
        if (curnode.leftchild != None):
            self.preorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.preorderTraverse(curnode.rightchild)
            
    def postorderTraverse(self,v):
        curnode = v
        if (curnode.leftchild != None):
            self.postorderTraverse(curnode.leftchild)
        if (curnode.rightchild!=None):
            self.postorderTraverse(curnode.rightchild)        
        print curnode.element,

    """
        Accepting 2 values l and h from the user and find the
        sum of all values between l and h present in the tree
   """
    def SumofValues(self,v,l,h):
        curnode = v
        while 1:
            if curnode.element>l and curnode.element<h:
                self.sum+=curnode.element
            if curnode.leftchild != None:
                curnode = curnode.leftchild
            elif curnode.rightchild != None:
                curnode = curnode.rightchild
            else:
                return self.sum        
        return self.sum    

    """
        Given a node v this will return the next element that should be visited after v in the
        inorder traversal.
    """
    def returnNextInorder(self,v):
        curnode = v
        if self.isExternal(curnode) or curnode.leftchild == None:
            return curnode
        elif curnode.leftchild != None:
            if self.isExternal(curnode.leftchild) or curnode.leftchild.leftchild == None:
                return curnode.leftchild
            else:
                returnNextInorder(curnode.leftchild)
        return
    """
        This method deleteElement(self, e), removes the node with element e from the tree T.
        There are three cases:
            1. Deleting a leaf or external node:Just remove the node
            2. Deleting a node with one child: Remove the node and replace it with its child
            3. Deleting a node with two children: Instead of deleting the node replace with
                a) its inorder successor node or b)Inorder predecessor node
    """

    def deleteElement(self,e):
        visnode = visNode()
        curnode = self.findElement(e,self.root)
        if (curnode.element != e):
            print ("Error, element not found")
            return
        else:
            if (self.isExternal(curnode)):
                ht1 = math.floor(math.log(curnode.pos,2))
                visnode.drawdelnode(curnode.element,ht1,curnode.pos)
                if (curnode.parent.leftchild == curnode):
                    curnode.parent.leftchild = None
                else:
                    curnode.parent.rightchild = None
                curnode = None
                
                return
            elif (curnode.leftchild != None and curnode.rightchild != None):
                replacenode = self.returnNextInorder(curnode.rightchild)
                print "to replace" , replacenode.element
                curnode.element = replacenode.element
                ht1 = math.floor(math.log(curnode.pos,2))
                visnode.drawnode(replacenode.element,ht1,curnode.pos)
                ht1 = math.floor(math.log(replacenode.pos,2))
                visnode.drawdelnode(replacenode.element,ht1,replacenode.pos)
                print replacenode.parent.element , "parent"
                if (replacenode.parent.leftchild == replacenode):
                    if (replacenode.leftchild != None):
                        replacenode.parent.leftchild = replacenode.leftchild
                        replacenode.leftchild.parent = replacenode.parent
                    elif (replacenode.rightchild != None):
                        replacenode.parent.leftchild = replacenode.rightchild
                        replacenode.rightchild.parent = replacenode.parent
                elif (replacenode.parent.rightchild == replacenode):
                    if (replacenode.leftchild != None):
                        replacenode.parent.rightchild = replacenode.leftchild
                        replacenode.leftchild.parent = replacenode.parent
                    elif (replacenode.rightchild != None):
                        replacenode.parent.righttchild = replacenode.rightchild
                        replacenode.rightchild.parent = replacenode.parent
                replacenode = None
                return
            elif (curnode.leftchild == None):
                ht1 = math.floor(math.log(curnode.pos,2))
                visnode.drawdelnode(curnode.element,ht1,curnode.pos)
                curnode.rightchild.parent = curnode.parent
                if (curnode.parent.leftchild == curnode):
                    curnode.parent.leftchild = curnode.rightchild
                else:
                    curnode.parent.rightchild = curnode.rightchild
                curnode = curnode.rightchild
                return
            elif (curnode.rightchild == None):
                ht1 = math.floor(math.log(curnode.pos,2))
                visnode.drawnode(curnode.leftchild.element,ht1,curnode.pos)
                curnode.leftchild.parent = curnode.parent
                if (curnode.parent.leftchild == curnode):
                    curnode.parent.leftchild = curnode.leftchild
                else:
                    curnode.parent.rightchild = curnode.leftchild
                curnode = curnode.leftchild
                ht1 = math.floor(math.log(curnode.pos,2))
                visnode.drawdelnode(curnode.element,ht1,curnode.pos)
                return

    """
        Given a list of elements construct a balanced binary search tree
    """
    def createTree(self, items):
        mid = int(math.floor(len(items)/2))
        self.insertElement(items[mid])
        del items[mid]
        if (len(items)>1):
            self.createTree(items[0:mid])
            self.createTree(items[mid:len(items)+1])
        else:
            if (len(items)==1):
                self.insertElement(items[0])
            return
        
    """
        There are other support methods which maybe useful for implementing your functionalities.
        These include
            1. isExternal(self,v): which returns true if the node v is external
            2. printTree(self): to visualize the tree for your debugging purposes. You may print it
            using text formatting or use a turtle library given along with the file.
    """
    def isExternal(self,curnode):
        if (curnode.leftchild == None and curnode.rightchild == None):
            return True
        else:
            return False

