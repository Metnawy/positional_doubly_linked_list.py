import copy
class positional_doubly_linked_list :
    '''
    objective: create positional_doubly_linked_list
    basic _idea:using the nested composition of position class means we mostly will use the associted position instance of each node as the 
    interface to interact with that node .
    but as normal behaviour the general interact with the list will be through the instance of the list itself 
    '''
    class _node:
       def __init__(self,data=None,next=None,prev=None):
          self.value=data
          self._next=next
          self._prev=prev
          self.no_access=0
          # it's could be associated with position instance or any accessing elements .... and may be enter in contradiction with
          # the accessing for internal operations and manuipulations 
       
       @property #getter
       def value(self):
           self.no_access+=1
           return self._value 
       @value.setter #setter 
       def value(self,data):
           self._value=data 

       def user_access_value(self):
           return self.value
       def access_value(self):#internal interactions without intentions to change the no of accessing 
           return self._value
     
       def __repr__(self) -> str:
            return f"{self.value}"

    class _position:
        '''
        objectives: creating somehow simulating of the idea of numeric indices in array by that nest composited class instances which work as 
                    interface to access the node directly without traversing the whole linked list ....
        constraints: at each process of adding any node to the linked list we instantiate position object saving it with variable to use it 
        potential : we try as possible as make the process of instantiate position object available at different cases during the interaction 
                    with the linked_list 
        consequence : we could have many instances of position class ,,all of them refer to the same node .
        '''
        def __init__(self,node,container):
            self.node=node
            self.container=container
        def __repr__(self) -> str:
            return f"{self.node}"

    def __init__(self,data=None):
        self.head=self._node(data)
        self.tail=self._node(data)
        self.head._next=self.tail
        self.tail._prev=self.head
        self.size=0

    #general_accessing 
    def first(self):
        if self.size!=0:
        #get_first_node_position
          first=self.head._next
          return self._position(first,self)
        else:
            return "the list is empty"
    def last(self):
        if self.size!=0:
        #get last node position
           return self._position(self.tail._prev,self)
        else:
            return"the list is empty"
    def __iter__(self):
        '''
        objectives :using the __iter__() special method to iterate through the linked list 
        there were two options to iterate through the list :
        first:yielding the node itself , which is suitable in printing due to the implementation 
        of __repr__ in _node() nested class BUT in using the yielding of iteration as distinct value 
        to the variable of the loop may put us in problems and complications .
        second : yielding the _node.value itself 
        ,,, we choosed the second option.
        '''
        curser=self.head._next
        while curser.value!=None:
            yield curser.value
            curser=curser._next

    #other
    def replace(self,position,data):
        if isinstance(position,self._position): 
           if position.container==self:
                position.node._value=data
                return f"mission done the new value of the node is {data}"
           raise ValueError(f"that posistion dosent' exists in that list")
        raise TypeError(f"the position argument type shoulde be {self._position}")
    def __repr__(self) -> str:
        if self.size==0:
            return "head-->tail"
        else:
            new_string="head-->"
            curser=self.head._next
            for i in range(self.size):
                new_string=new_string+f"{curser.access_value()}"+"-->"
                curser=curser._next

            new_string=new_string+"tail"
            return new_string
    def positions(self):
        #iterable of all positions 
        def __iter__(self):
            curser=self.head._next
            while curser.access_value()!=None:
                yield self._position(curser,self)
                curser=curser._next 
        return __iter__(self)
    
    def __reversed__(self):
        if self.size==0 or self.size==1:
            return self
        
        left_curser=self.head._next
        right_curser=self.tail._prev

        if self.size%2==0:
            flag=True
            while flag:
                 
                if left_curser._next==right_curser and right_curser._prev==left_curser:
                     
                     pre_l_curser=left_curser._prev
                     after_r_curser=right_curser._next

                     pre_l_curser._next=right_curser
                     right_curser._next=left_curser
                     left_curser._prev=right_curser
                     left_curser._next=after_r_curser
                     after_r_curser._prev=left_curser
                     flag=False
                else:
                    #left_side
                    pre_l_curser=left_curser._prev
                    after_l_curser=left_curser._next
                
                    #right_side
                    pre_r_curser=right_curser._prev
                    after_r_curser=right_curser._next
                    

                    # swapping/reversing 
                    pre_l_curser._next=right_curser
                    right_curser._prev=pre_l_curser
                    right_curser._next=after_l_curser
                    after_l_curser._prev=right_curser

                    pre_r_curser._next=left_curser
                    left_curser._prev=pre_r_curser
                    left_curser._next=after_r_curser
                    after_r_curser._prev=left_curser

                    #moving the curser
                    temporary_right_curser=left_curser
                    left_curser=right_curser._next
                    right_curser=temporary_right_curser._prev

            return self
            

        if self.size%2!=0:

            flag=True
            while flag:
               if left_curser._next==right_curser._prev:
                  
                  mid_point=left_curser._next
                  pre_l_curser=left_curser._prev
                  after_r_curser=right_curser._next
                  
                  pre_l_curser._next=right_curser
                  right_curser._prev=pre_l_curser
                  right_curser._next=mid_point
                  mid_point._prev=right_curser
                  mid_point._next=left_curser
                  left_curser._prev=mid_point
                  left_curser._next=after_r_curser

                  flag=False

               else:
                    
                    #left_side
                    pre_l_curser=left_curser._prev
                    after_l_curser=left_curser._next
                    #right_side
                    pre_r_curser=right_curser._prev
                    after_r_curser=right_curser._next

                    # swapping/reversing 
                    pre_l_curser._next=right_curser
                    right_curser._prev=pre_l_curser
                    right_curser._next=after_l_curser
                    after_l_curser._prev=right_curser

                    pre_r_curser._next=left_curser
                    left_curser._prev=pre_r_curser
                    left_curser._next=after_r_curser
                    after_r_curser._prev=left_curser

                    #moving the curser
                    temporary_right_curser=left_curser
                    left_curser=right_curser._next
                    right_curser=temporary_right_curser._prev


            return self
 


    def sort_value(self,start,end,size):
        # it will sorting the list according to it's value  without change the oridnary order by creating a new list 
        new_list=copy.deepcopy(self)
        def merge_sides(right_side,left_side):
            new=positional_doubly_linked_list()
            l_curser=left_side.head._next
            r_curser=right_side.head._next
            
            while l_curser._value!=None and r_curser._value!=None:
            
                if l_curser.access_value()==r_curser.access_value():
                    first_add=l_curser
                    second_add=r_curser

                
                    l_curser=l_curser._next
                    r_curser=r_curser._next

                    l_curser._Prev=left_side.head
                    left_side.head._next=l_curser
                    r_curser._prev=right_side.head
                    right_side.head._next=r_curser

      
                    last=new.tail._prev
                    last._next=first_add
                    first_add._prev=last
                    first_add._next=second_add
                    second_add._prev=first_add
                    second_add._next=new.tail
                    new.tail._prev=second_add
                    

                elif l_curser.access_value()>r_curser.access_value():
                    the_add=l_curser
                    l_curser=l_curser._next

                    l_curser._prev=left_side.head
                    left_side.head._next=l_curser

                    last=new.tail._prev
                    last._next=the_add
                    the_add._prev=last
                    the_add._next=new.tail
                    new.tail._prev=the_add

                elif r_curser.access_value()>l_curser.access_value():
                    the_add=r_curser
                    r_curser=r_curser._next

                    r_curser._prev=right_side.head
                    right_side.head._next=r_curser

                    last=new.tail._prev
                    last._next=the_add
                    the_add._prev=last
                    the_add._next=new.tail
                    new.tail._prev=the_add
            

            
            while l_curser._value!=None:
                last=new.tail._prev
                after_curser=l_curser._next
                the_add=l_curser

                last._next=the_add
                the_add._prev=last
                the_add._next=new.tail
                new.tail._prev=the_add

                l_curser=after_curser
                left_side.head._next=l_curser
                l_curser._prev=left_side.head

                
            while  r_curser._value!=None:
                last=new.tail._prev
                after_curser=r_curser._next
                the_add=r_curser

                last._next=the_add
                the_add._prev=last
                the_add._next=new.tail
                new.tail._prev=the_add

                r_curser=after_curser
                left_side.head._next=r_curser
                r_curser._prev=left_side.head

            return new


        def helper(new_list,start,end,size,last_mid=0):
          # print(start,end,size,last_mid)
           if size==1 :
              new=positional_doubly_linked_list()
              new.head._next=end
              end._prev=new.head
              end._next=new.tail
              new.tail._prev=end
              new.size+=1
              return new

           else :
              mid_shift=size//2 
              mid_point=last_mid+mid_shift
              mid_positon=new_list.position_of_index(mid_point).node
              
              right_side=helper(new_list,mid_positon._next,end,(size-mid_shift),mid_point)
              left_side=helper(new_list,start,mid_positon,mid_shift,(mid_point-mid_shift))

              return merge_sides(right_side,left_side)
        return helper(new_list,start,end,size)

    def access_count_sort(self,start,end,size):
        # it will sorting the list according to it's value no of access without change the oridnary order by creating a new list 
        new_list=copy.deepcopy(self)
        def merge_sides(right_side,left_side):
            new=positional_doubly_linked_list()
            l_curser=left_side.head._next
            r_curser=right_side.head._next
            
            while l_curser._value!=None and r_curser._value!=None:
                
                if l_curser.no_access==r_curser.no_access:
                    first_add=l_curser
                    second_add=r_curser

                    l_curser=l_curser._next
                    r_curser=r_curser._next
                    
                    last=new.tail._prev
                    last._next=first_add
                    first_add._prev=new
                    first_add._next=second_add
                    second_add._prev=first_add
                    second_add._next=new.tail
                    new.tail._prev=second_add
                    

                elif l_curser.no_access>r_curser.no_access:
                    the_add=l_curser
                    l_curser=l_curser._next

                    last=new.tail._prev
                    last._next=the_add
                    the_add._prev=last
                    the_add._next=new.tail
                    new.tail._prev=the_add

                elif r_curser.no_access>l_curser.no_access:
                    the_add=r_curser
                    r_curser=r_curser._next

                    last=new.tail._prev
                    last._next=the_add
                    the_add._prev=last
                    the_add._next=new.tail
                    new.tail._prev=the_add
            

            if l_curser._value!=None :
              while l_curser._value!=None:
                last=new.tail._prev
                last._next=l_curser
                l_curser._prev=last
                l_curser._next=new.tail
                new.tail._prev=l_curser

                l_curser=l_curser._next
                
            if r_curser._value!=None:
              while r_curser._value!=None:
                last=new.tail._prev
                last._next=r_curser
                r_curser._prev=last
                r_curser._next=new.tail
                new.tail._prev=r_curser

                r_curser=r_curser._next
     
            return new


        def helper(new_list,start,end,size,last_mid=0):
           
           if size==1 :
              new=positional_doubly_linked_list()
              new.head._next=start
              start._prev=new.head
              start._next=new.tail
              new.tail._prev=start
              new.size+=1
              return new
        
           else :
              mid_shift=size//2 
              mid_point=last_mid+mid_shift
              mid_positon=new_list.position_of_index(mid_point).node
              
              right_side=helper(new_list,mid_positon._next,end,(size-mid_shift),mid_point)
              left_side=helper(new_list,start,mid_positon,mid_shift,(mid_point-mid_shift))

              return merge_sides(right_side,left_side)
        return helper(new_list,new_list.head._next,new_list.tail._prev,size)


    def swap(self,position1,position2):
        #swap by values 
        if isinstance(position1,self._position) and isinstance(position2,self._position):
            if position1.container==position2.container:
                first_value=position1.node.access_value()
                second_value=position2.node.access_value()
                position1.node._value=second_value
                position2.node._value=first_value
                return "mission done ... both values swapped between the two nodes positions"
            raise ValueError(f"both psoitions should be from the same list to swap between their values ")
        raise TypeError(f"both arguments should be {self._position}")
    

    def swap_nodes(self,position1,position2):
        #swap the nodes themselves 
        if isinstance(position1,self._position) and isinstance(position2,self._position):
            if position1.container==position2.container:
                #cases where both nodes besides each other 
                if position1.node._next==position2.node:
                    pre_first=position1.node._prev
                    after_second=position2.node._next

                    pre_first._next=position2.node
                    position2.node._prev=pre_first
                    position1.node._next=after_second
                    after_second._prev=position1.node

                    return "mission of swapping has been  done"
                elif position2.node._next==position1.node:
                    pre_first=position2.node._prev
                    after_second=position1.node._next

                    pre_first._next=position1.node
                    position1.node._prev=pre_first
                    position2.node._next=after_second
                    after_second._prev=position2

                    return "the mission of swapping has been done "


                else:
                    # the cases of there one element mutual in mid between both positions 
                    if position1.node._next==position2.node._prev:
                        pre_first=position1.node._prev
                        mutual=position1.node._next
                        after_second=position2.node._next

                        pre_first._next=position2.node
                        position2.node._prev=pre_first
                        position2.node._next=mutual
                        mutual._prev=position2.node
                        mutual._next=position1.node
                        position1.node._prev=mutual
                        position1.node._next=after_second

                        return "the mission of swapping has been done"
                    elif position2.node._next==position1.node._prev:
                        pre_first=position2.node._prev
                        mutual=position2.node._next
                        after_second=position1.node._next

                        pre_first._next=position1.node
                        position1.node._prev=pre_first
                        position1.node._next=mutual
                        mutual._prev=position1.node
                        mutual._next=position2.node
                        position2.node._prev=mutual
                        position2.node._next=after_second

                        return "the mission has been done "
                    else:
                        # here position aren't consecutives or having mutuality 
                         #first position 
                         pre_first=position1.node._prev
                         after_first=position1.node._next

                         #second position 
                         pre_second=position2.node._prev
                         after_second=position2.node._next

                         #swapping 
                         pre_first._next=position2.node
                         position2.node._prev=pre_first
                         position2.node._next=after_first
                         after_first._prev=position2.node

                         pre_second._next=position1.node
                         position1.node._prev=pre_second
                         position1.node._next=after_second
                         after_second._prev=position1.node

                         return "the misson has been done "

            raise ValueError(f"both of positions should be part of the same list")
        raise TypeError(f"both arguments should be {self._position}")


    # info
    def is_empty(self):
        return self.size==0 
  
    def __len__(self):
        return self.size
    def __getitem__(self,index):
        #here we  simulate the 0_based index but we add 1 to be comptiable with the defination of functions

        return self.position_of_index(index+1)
        
    def __delitem__(self,index):
        #here we  simulate the 0_based index but we add 1 to be comptiable with the defination of functions
        x=self.delete_position(index+1)
        return  x
    def max_value(self):# with recursion approach 
        return self.sort_value(self.head._next,self.tail._prev,self.size).head._next
    def min_value(self):
        return self.sort_value(self.head._next,self.tail._prev,self.size).tail._prev

    def max_no_access(self):
        x=self.access_count_sort(self.head._next,self.tail._prev,self.size).head._next
        return x,x.no_access

    def min_no_access(self):
        x=self.access_count_sort(self.head._next,self.tail._prev,self.size).tail._prev 
        return x,x.no_access

    # first
    def add_first(self,data):
        new_node=self._node(data,self.head._next,self.head)
        self.head._next._prev=new_node
        self.head._next=new_node
        self.size+=1
        return self._position(new_node,self)
    
    def delete_first(self):
      if self.size!=0:
        x=self.first()
        value=x.node.access_value()
        self.size-=1
        self.head._next=x.node._next
        x.node._next._prev=self.head
        x.node.value=x.node._next=x.node._prev=None
        return value
      else:
          return" the list already is empty"
        
    def add_last(self,data):
        new_node=self._node(data,self.tail,self.tail._prev)
        self.tail._prev._next=new_node
        self.tail._prev=new_node
        self.size+=1
        return self._position(new_node,self)
    
    def delete_last(self):
      if self.size!=0:
        x=self.last()
        value=x.node.access_value()
        self.size-=1
        self.tail._prev=x.node._prev
        x.node._prev._next=self.tail
        x.node._next=x.node._prev=x.node.value=None
        return value
      else:
          return "the list is already empty"
        
 
    #position_instance
    def add_before_position(self,data,position):
        if isinstance(position,self._position) :
          if position.container==self:
            if position.node!=self.head:
               new_node=self._node(data,position.node,position.node._prev)
               position.node._prev._next=new_node
               position.node._prev=new_node
               self.size+=1
               return self._position(new_node,self)
            raise ValueError("we created sentineals to work as a boundary ,,we can't add before/after them")
          raise ValueError("the position instance should be part of the concerned list we working on ")
        raise TypeError("the position reference should be _position nested data type ")
        
    def delete_before_position(self,position):
        if isinstance(position,self._position):
          if position.node!=self.first().node and position.node!=self.head and  self.size!=0:
             # in this condition we countering three cases could lead to inconsistancy successively :
             # 1st if there a try to remove sentineal head by using the first element
             # 2nd if there a try to delete something doesn't exist before self.head
             # 3rd if there another try to remove the head by using the self.tail  
             if position.container==self:
                x=position.node
                before_position=x._prev
                value=before_position.access_value()
                before_position._prev._next=x
                x._prev=before_position._prev
                self.size-=1
                before_position._value=before_position._next=before_position._prev=None
                before_position.no_access=0
                return value
             raise ValueError("the position instance should be part of the concerned list we working on ")
          raise ValueError("the position reference shouldn't be the sentineal(head) to delete before OR try to delete this sentinal itself")
        raise TypeError("the position argument should be _position data type to use it as reference")
    def add_after_position(self,data,position):
        if isinstance(position,self._position):
           if position.node!=self.tail:
                if position.container==self:
                   new_node=self._node(data,position.node._next,position.node)
                   position.node._next._prev=new_node
                   position.node._next=new_node
                   self.size+=1
                   return self._position(new_node,self)
            
                raise ValueError("the position instance should be part of the concerned list we working on ")
           raise ValueError("we can't add after the sentinal/self.tail as we created it as a boundery")
        raise TypeError("the position argument should be _position data type to use it as reference")
      
    def delete_after_position(self,position):
        if isinstance(position,self._position):
           if position.node!=self.tail and position.node!=self.last().node and position.node!=self.head:
             # in this conditions we are  countering three cases could lead to inconsistancy successively :
             # 1st if there a try to delete something doesn't exist after self.tail
             # 2nd if there a try to remove sentineal tail by using the last element
             # 3rd if there another try to remove the tail by using the self.head in case of empty list 
               if position.container==self:
                  position_node=position.node
                  position_after=position_node._next
                  new_position_after=position_after._next
                  position_node._next=new_position_after
                  new_position_after._prev=position_node
                  value=position_after.access_value()
                  position_after._value=position_after._next=position_after._prev=None
                  position_after.no_access=0
                  self.size-=1
                  return value
               raise ValueError("the position instance should be part of the concerned list we working on ")
           raise ValueError("the position reference shouldn't be the sentineal(tail) to delete after it OR try to delete this sentinal itself")
        raise TypeError("the position argument should be _position data type to use it as reference")
        
    
    def delete_position(self,position):
        if isinstance(position,self._position):
            if position.container==self:
              if position.node!=self.head and position.node!=self.tail:
                position_node=position.node
                value=position_node.access_value()
                befor_position_node=position_node._prev
                after_position_node=position_node._next
                
                befor_position_node._next=after_position_node
                after_position_node._prev=befor_position_node
                position_node._value=position_node._next=position_node._prev=None
                position_node.no_access=0

                self.size-=1
                return value 

              raise ValueError("we can't deleting the sentinails either head or tail")
            raise ValueError("the position instance should be part of the concerned list we working on ")
        raise TypeError("the position argument should be _position data type to use it as reference")

        # getting position for accessing and other maniuplation 
    def positon_after_position(self,position):
        if isinstance(position,self._position):
            if position.container==self:
                if position.node._next==self.tail or position.node==self.tail:
                    raise ValueError("in the context of the class we won't interact with the sentineals as part of the list ")
                else:
                    next_node=position.node._next
                    return self._position(next_node,self)

            raise ValueError("the position instance should be part of the concerned list we working on ")


        raise TypeError("the position argument should be _position data type to use it as reference")
        
    def position_before_position(self,position):
        if isinstance(position,self._position):
            if position.container==self:
                if position.node._prev==self.head or position.node==self.head:
                    raise ValueError("in the context of the class we won't interact with the sentineals as part of the list ")
                else:
                    prev_node=position.node._prev
                    return self._position(prev_node,self)
            raise ValueError("the position instance should be part of the concerned list we working on ")

        
        raise TypeError("the position argument should be _position data type to use it as reference")

    #numeric_position#
    #the numeric indices will 1-based index
    # in this section of the code may be points such as the time & sapce complexity aren't optimal in comparsion to other methods (they also defined in the code) but i implemented this part also to wide the potential and the range of options covering all possibilites of needs 

    def value_numeric_index(self,index):
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next
            return curser.value 
        raise IndexError("the index should be intger within the range of size ")
        
    def change_at_numeric_index(self,index,data):
        if isinstance(index,int) and 1<=index<=self.size:
           curser=self.head
           for i in range(index):
               curser=curser._next
           curser._value=data
           return curser
        raise IndexError("the index shoud be intger within the range of size")

    def add_numeric_index(self,index,data):
        # here we aren't substitute the value of the same node but we change the order by inserting new node at specific point 
        if isinstance(index,int) and index>=1:
            if self.size==0:
                return self.add_first(data)
            else:
                # here there were two options in the inserting of the new node in the targeted index either pushing forwar o backward the node exists currently ..we choosed to push forward 
                return self.add_before_numeric_index(index,data)

        raise TypeError("the index should be intger above zero")
    
    def delete_numeric_index(self,index):
        # deleting a node at specific numeric order in the the list 
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next
            value=curser.value
            before_node=curser._prev
            after_node=curser._next
            before_node._next=after_node
            after_node._prev=before_node
            curser._value=curser._next=curser._prev=None
            self.size-=1
            return value
        raise IndexError("the index shoud be intger within the range of size")
        
    def add_after_numeric_index(self,index,data):
        # here we add new node ...return a position instance represents that node .
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next

            new_node=self._node(data,curser._next,curser)
            curser._next._prev=new_node
            curser._next=new_node
            self.size+=1
            return self._position(new_node,self)
        raise IndexError("the index shoud be intger within the range of size")

    def delete_after_numeric_index(self,index):
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
               curser=curser._next
            if curser._next!=self.tail:
              target_node=curser._next
              value=target_node.value
              next_target=target_node._next

              curser._next=next_target
              next_target._prev=curser
              target_node._value=target_node._next=target_node._prev=None
              self.size-=1
              return value 
            raise ValueError("we can't delete the sentineal node self.tail")

        raise IndexError("the index shoud be intger within the range of size")

    def add_before_numeric_index(self,index,data):
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next

            before_curser=curser._prev
            new_node=self._node(data,curser,before_curser)
            before_curser._next=new_node
            curser._prev=new_node
            self.size+=1
            return self._position(new_node,self)

        raise IndexError("the index shoud be intger within the range of size")
    
    def delete_before_numeric_index(self,index):
        if isinstance(index,int) and 2<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next

            targted_node=curser._prev
            before_targeted=targted_node._prev
            value=targted_node.value

            before_targeted._next=curser
            curser._prev=before_targeted
            self.size-=1
            targted_node._value=targted_node._next=targted_node._prev=None
            return value
        raise IndexError("the index shoud be intger within the range of size")
        # getting position for accessing and other maniuplation 
    def position_of_index(self,index):
       if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next
            return self._position(curser,self)
       raise IndexError("the index shoud be intger within the range of size")

    def position_after_index(self,index):
        if isinstance(index,int) and 1<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next

            if curser._next!=self.tail:
                return self._position(curser._next,self)
            raise ValueError("we designed this list without interact with the sentineals such as tails ")
        raise IndexError("the index shoud be intger within the range of size")
        
    def position_before_index(self,index):
        if isinstance(index,int) and 2<=index<=self.size:
            curser=self.head
            for i in range(index):
                curser=curser._next
            return self._position(curser._prev,self)
               
        raise IndexError("the index shoud be intger within the range of size")
    
    #occurance of value 
    def delete_first_occurance(self,data):
        if self.size==0:
            return "it already empty, no elements to delete"
        else:
            curser=self.head._next
            while curser :
                if type(data)==type(curser.access_value()) :
                    if data==curser.access_value():
                        before_curser=curser._prev
                        after_curser=curser._prev 
                        value=curser.value

                        self.size-=1
                        before_curser._next=after_curser
                        after_curser._prev=before_curser
                        curser._value=curser._next=curser._prev=None
                        return f"the mission done node with value{value} was deleted"
                    else:
                        curser=curser._next

                elif isinstance(data,(int,float)) and isinstance(data,(int,float)):
                      if data==curser.access_value():
                        before_curser=curser._prev
                        after_curser=curser._prev 
                        value=curser.value

                        self.size-=1
                        before_curser._next=after_curser
                        after_curser._prev=before_curser
                        curser._value=curser._next=curser._prev=None
                        return f"the mission done node with value {value} was deleted"
                      else:
                        curser=curser._next
                else:
                    curser=curser._next
                 
            return "the value doesn't exist to delete it "
        
    def add_after_first_occurance(self,data,new_data):
         
        if self.size==0:
            return "it already empty, no elements to add after "
        else:
            curser=self.head._next
            while curser :
                if type(data)==type(curser.access_value()) :
                    if data==curser.access_value():
                        
                        after_curser=curser._next
                        new_node=self._node(new_data,after_curser,curser)

                        self.size+=1
                        curser._next=new_node
                        after_curser._prev=new_node
                        
                        return self._position(new_node,self)
                    else:
                        curser=curser._next

                elif isinstance(data,(int,float)) and isinstance(data,(int,float)):
                      if data==curser.access_value():
                        after_curser=curser._next
                        new_node=self._node(new_data,after_curser,curser)

                        self.size+=1
                        curser._next=new_node
                        after_curser._prev=new_node
                        
                        return self._position(new_node,self)
                      else:
                        curser=curser._next
                else:
                    curser=curser._next
                 
            return "the value doesn't exist to add something after  "

    def delete_after_first_occurance(self,data):
        if self.size==0:
            return "it already empty, no elements to add after "
        elif self.size==1:
            return "either that data does exist or not on the list ... we can't delete the sentineal self.tail"
        else:
            curser=self.head._next
            while curser :
                if type(data)==type(curser.access_value()) :
                    if data==curser.access_value():
                      if curser._next != self.tail:
                        targeted_node=curser._next
                        value=targeted_node.value
                        after_targeted=targeted_node._next



                        self.size-=1
                        curser._next=after_targeted
                        after_targeted._prev=curser
                        targeted_node._value=targeted_node._next=targeted_node._prev=None
                        
                        return value 
                      raise ValueError("we can't delete the sentineal self.tail")
                    else:
                        curser=curser._next

                elif isinstance(data,(int,float)) and isinstance(data,(int,float)):
                    if data==curser.access_value():
                       if curser._next!=self.tail:
                         targeted_node=curser._next
                         value=targeted_node.value
                         after_targeted=targeted_node._next

                         self.size-=1
                         curser._next=after_targeted
                         after_targeted._prev=curser
                         targeted_node._value=targeted_node._next=targeted_node._prev=None
                        
                         return value
                       raise ValueError("we can't delete the sentineal self.tail")
                    else:
                        curser=curser._next
                else:
                    curser=curser._next
                 
            return "the value doesn't exist to delete something after  "

    def add_before_first_occurance(self,data,new_data):
         
        if self.size==0:
            return "it already empty, no elements to add before"
        else:
            curser=self.head._next
            while curser :
                if type(data)==type(curser.access_value()) :
                    if data==curser.access_value():
                        
                        before_curser=curser._prev
                        new_node=self._node(new_data,curser,before_curser)

                        self.size+=1
                        curser._prev=new_node
                        before_curser._next=new_node
                        
                        return self._position(new_node,self)
                    else:
                        curser=curser._next

                elif isinstance(data,(int,float)) and isinstance(data,(int,float)):
                      if data==curser.access_value():
                        before_curser=curser._prev
                        new_node=self._node(new_data,curser,before_curser)

                        self.size+=1
                        curser._prev=new_node
                        before_curser._next=new_node
                        
                        return self._position(new_node,self)
                      else:
                        curser=curser._next
                else:
                    curser=curser._next
                 
            return "the value doesn't exist to add something before "

    def delete_before_first_occurance(self,data):
        if self.size==0:
            return "it already empty, no elements to add before "
        elif self.size==1:
            return "either that data does exist or not on the list ... we can't delete the sentineal self.head"
        else:
            curser=self.head._next
            while curser :
                if type(data)==type(curser.access_value()) :
                    if data==curser.access_value():
                      if curser._prev != self.head:
                        targeted_node=curser._prev
                        value=targeted_node.value
                        before_targeted=targeted_node._prev



                        self.size-=1
                        curser._prev=before_targeted
                        before_targeted._next=curser
                        targeted_node._value=targeted_node._next=targeted_node._prev=None
                        
                        return value 
                      raise ValueError("we can't delete the sentineal self.head")
                    else:
                        curser=curser._next

                elif isinstance(data,(int,float)) and isinstance(data,(int,float)):
                    if data==curser.access_value():
                       if curser._prev!=self.head:
                         targeted_node=curser._prev
                         value=targeted_node.value
                         before_targeted=targeted_node._prev

                         self.size-=1
                         curser._prev=before_targeted
                         before_targeted._next=curser
                         targeted_node._value=targeted_node._next=targeted_node._prev=None
                        
                         return value
                       raise ValueError("we can't delete the sentineal self.head")
                    else:
                        curser=curser._next
                else:
                    curser=curser._next
                 
            return "the value doesn't exist to delete something after  "
        # getting position for accessing and other maniuplation 
    def position_after_first_occurance(self,data):
        if self.size==0:
            return "the list is already empty to get any info from it "
        if self.size==1:
            return "the list has only one element ...no info about sentineals"
        else:
            curser=self.head._next
            while curser:
                if type(data)==type(curser.access_value()):
                    if data==curser.access_value():
                        if curser._next== self.tail:
                            return f" even though the data {data} exists but it's last thing,,, no elements after it "
                        else :
                              return self._position(curser._next,self)
                elif isinstance(data,(int,float))==isinstance(curser.access_value()):
                     if data==curser.access_value():
                        if curser._next== self.tail:
                            return f" even though the data {data} exists but it's last thing,,, no elements after it "
                        else :
                              return self._position(curser._next,self)
                else:
                    curser=curser._next
            return f"there is no such data {data} in the list"
        
    def position_before_first_occurance(self,data):
        if self.size==0:
            return "the list is already empty to get any info from it "
        if self.size==1:
            return "the list has only one element ...no info about sentineals"
        else:
            curser=self.head._next
            while curser:
                if type(data)==type(curser.access_value()):
                    if data==curser.access_value():
                        if curser._prev== self.head:
                            return f" even though the data {data} exists but it's first thing,,, no elements before it "
                        else :
                              return self._position(curser._prev,self)
                    else:
                        curser=curser._next
                elif isinstance(data,(int,float))==isinstance(curser.access_value()):
                     if data==curser.access_value():
                        if curser._prev== self.head:
                            return f" even though the data {data} exists but it's last thing,,, no elements before it "
                        else :
                              return self._position(curser._prev,self)
                     else:
                         curser=curser._next
                else:
                    curser=curser._next
            return f"there is no such data {data} in the list"
        

    def find(self,data):
        if self.size==0:
            return "the list is already empty to get any info from it "
    
        else:
            curser=self.head._next
            while curser:
                if type(data)==type(curser.access_value()):
                    if data==curser.access_value():
                        return self._position(curser,self)
                    else:
                        curser=curser._next
                elif isinstance(data,(int,float))==isinstance(curser.access_value()):
                     if data==curser.access_value():
                       return self._position(curser._prev,self)
                     else:
                         curser=curser._next
                else:
                    curser=curser._next
            return f"there is no such data {data} in the list"
        

    def findall(self,data):
        list_nodes=[]
        if self.size==0:
            return "no such data in the list "
        curser=self.head._next
        while curser:
            if type(data)==type(curser.access_value()):
                if data==curser.access_value():
                    x=self._position(curser,self)
                    list_nodes.append(x)
                curser=curser._next
            elif isinstance(data,(int,float))==isinstance(data,(int,float)):
                 if data==curser.access_value():
                     z=self._position(curser,self)
                     list_nodes.append(z)
                 curser=curser._next
            else:
                curser=curser._next
        if len(list_nodes)==0:
            return "there is no such data in the list "
        else:
            return list_nodes



f=positional_doubly_linked_list()

#f.head._next=f._node(5,f.tail,f.head)

z=f.add_first(6)

x1=f.add_first(4)

y1=f.add_first(2)
f.add_first(9999)
y=f.add_first(110)

y=f.add_first(50)
f.add_first(100)
f.add_first(0)
f.add_last(555)


print(f)
print(reversed(f))
print("\n")
f.last().node.no_access=50
f.position_of_index(4).node.no_access=25
x=f.access_count_sort(f.first().node,f.last().node,f.size)
print("\n")
for i in x:
    ...

print("\n")
for i in f:
    ...
x=f.sort_value(f.first().node,f.last().node,f.size)
print("\n") 
for i in x:
    ...
x=f.first()
y=f.first()

print(x==y)
print(x.node==y.node)
print(f)

n=f.positions()
print(type(n))
for i in n:
    print(i,type(i),i.container)
print("\n")
for i in range (9):
    print(f[i])
print(f)
print(f.max_value(),f.min_value())
print(f.max_no_access(),f.min_no_access())