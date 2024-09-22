
import llist
from llist import *

class stack(llist):
    def __init__(self):
        super().__init__()
    def add(self,data):
        '''
        adds Top node'''
        self.prepend(data)
        return

    def pop(self):
        '''
        Removes top Node'''
        # self.delete_at(0)
        # return
        if self.head is None:
            print('Can\'t pop from Empty List')
            return
        pointer = self.head
        self.head = pointer.next

        
    def peek(self):
        '''
        Viewss top Node'''
        print(self.head.data)
        return

if __name__ == '__main__':

    st = stack()
    st.pop()
    st.add(5)
    st.add('dice')
    st.add('far')
    st.add('infinity')
    st.print()
    st.peek()
    st.pop()
    st.pop()

    #st.print()
    
       