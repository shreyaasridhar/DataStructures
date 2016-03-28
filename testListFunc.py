from SLList import SLList 


def testlist():
    list1 = SLList()
    print ("size",list1.size())
    print (list1.isEmpty())
    for i in range(5):
        curnode = list1.node()
        curnode.element = i
        list1.insertLast(curnode)
    print ("****")
    list1.printList()
    print ("size",list1.size())    
    curnode = list1.node()
    curnode.element = 6
    list1.insertLast(curnode)
    list1.printList()
    print ("****")
    #curnode = list1.node()
    #curnode.element = 3.5
    #list1.insertafter(3,curnode)
    #list1.printList()
    #print ("****")
    #curnode = list1.node()
    #curnode.element = 2.5
    #list1.insertbefore(3,curnode)
    #list1.printList()
    #print ("****")
    curnode = list1.node()
    curnode.element = 5    
    list1.insertpos(6,curnode)
    list1.printList()
    print ("*****")
    list1.findNode(4)
    print ("*****")
    list1.replace(6,5.5)
    list1.printList()
    print ("*****")
    list1.countNode(4)
    print ("*****")
    #list1.deletebefore(4)
    #list1.printList()
    #print ("*****")
    list1.deletepos(4)
    list1.printList()
    
   # list1.printAlternative()
    
   ## list1.deleteLast()
   ## print "****"
   ## list1.printList()
   ## print "size", list1.size()
   ## print (list1.findNode(5))
def main():
    testlist()

if __name__ == '__main__':
    main()
