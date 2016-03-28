class SLList:

     class node:
          def __init__(self):
               self.element = None
               self.next = None
               
          
     def __init__(self):
          self.head = self.node()
          self.sz = 0
          
          
     def returnLast(self):
          while (curnode.next!=None):#traversing till the last
                    curnode = curnode.next
          return
     
     def insertLast(self,u):
          if (self.head.element == None):
               self.head.element = u.element
               self.sz+=1
          else:
               curnode = self.head
               while (curnode.next!=None):
                    curnode = curnode.next
               curnode.next = u
               self.sz+=1
          return

     def insertFirst(self,u):
          if (self.head.element == None):
               self.head.element = u.element
               self.sz+=1
          else:
               u.next = self.head
               self.head = u
               self.sz+=1
          return
     
     def printalt(self):
          curnode = self.head
          while (curnode.next.next!=None):
               print curnode.element
               curnode=curnode.next.next
          print curnode.element
          return

     #5
     def ReplaceElement(self,v,u):
          curnode=self.head
          while curnode.next!= None:
               if curnode.element == v.element:
                    curnode.element=u
               curnode=curnode.next
          return     
     
     #6
     def penultimate(self):
          curnode = self.head
          while (curnode.next.next!=None):
               curnode=curnode.next
          return curnode.element

     #1
     def insertAfter(self,v,u):
          curnode=self.head
          while curnode.next!= None:
               if curnode.element == v.element:
                    u.next=curnode.next
                    curnode.next=u
               curnode=curnode.next
          if curnode.next== None:
               if curnode.element == v.element:
                    self.insertLast(u)               
          self.sz+=1
          return

     #2
     def insertBefore(self,v,u):
          curnode=self.head    
          self.sz+=1
          if curnode.element==v.element:
               self.insertFirst(u)
          while curnode.next!= None:
               if (curnode.next.element)== v.element:
                    curnode.next=u
                    u.next=v
               curnode=curnode.next
          return

     #4
     def Printpos(self,v):
          curnode=self.head
          x=0
          while curnode.next!= None:
               x=x+1
               if curnode.element == v.element:
                    return x
               curnode=curnode.next
          print "Element doesn't exist!"     
          
     #7
     def Countbefore(self,v):
          curnode=self.head
          x=0
          while curnode.next!= None:
               if curnode.element == v.element:
                    return x
               x=x+1
               curnode=curnode.next
          print "Element doesn't exist!" 
          
     #3
     def insertAtPos(self,v,n):
          curnode=self.head
          x=1
          if n==1:
               self.insertFirst(v)
               return
          if n==self.sz:
               self.insertLast(v)
               return               
          while curnode.next!= None:
               if(x==n):
                    v.next=curnode.next
                    curnode.next=v
               x+=1
               curnode=curnode.next
          self.sz+=1     
          return          
          

     def deleteFirst(self):
          if self.head.next == None:
              self.head.element = None
          else:
              temp = self.head
              self.head = self.head.next
              del temp
          self.sz = self.sz-1
          return

     def deleteLast(self):
          if self.head.next == None:
              self.head.element = None
          else:
              curnode = self.head
              while (curnode.next.next != None):
                   curnode = curnode.next
              temp = curnode.next.next
              curnode.next = None
              del temp
          self.sz = self.sz-1
          return

     #8
     def deleteAfter(self,v):
          if self.head.next == None:
              self.head.element = None
          else:
               curnode = self.head
               while curnode.next!= None:
                    if curnode.element==v.element:
                         temp=curnode.next
                         curnode.next=curnode.next.next
                    curnode=curnode.next             
               del temp
          self.sz-=1
          return

     #9
     def deleteBefore(self,v):
          if self.head.next == None:
               self.head.element = None
          else:
               curnode = self.head
               while (curnode.next.next != None):
                    if curnode.next.next.element==v.element:
                        temp=curnode.next
                        curnode.next=curnode.next.next
                    curnode=curnode.next     
               del temp
          self.sz-=1
          return

     #10
     def deleteAtPos(self,n):
          curnode=self.head
          x=0
          while curnode.next!= None:
               x=x+1
               if(x==n-1):
                    temp=curnode.next
                    curnode.next=curnode.next.next
               curnode=curnode.next     
          del temp          
          self.sz-=1
          return
          
          
     def printList(self):
          tnode = self.head
          while tnode!= None:
               print tnode.element
               tnode = tnode.next
          return

     
     def findNode(self, val):
          curnode = self.head
          while curnode!=None:
               if curnode.element == val:
                    return curnode
               curnode = curnode.next
          return None
     
     def isEmpty(self):
          return self.sz==0

     def size(self):
          return self.sz
