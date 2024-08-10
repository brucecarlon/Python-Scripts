class Node:
    def __init__(self, data = None,next = None) -> None:
        self.data = data
        self.next = next

class SingleLink_list:
    '''
    #add
    #remove
    #print
    #search
    '''
    def __init__(self) -> None:
        self. head = None
 
    def print(self):
        curr_node = self.head
        while curr_node != None:
            print(f'{curr_node.data}--> ')
            curr_node = curr_node.next

    def search(self,data):
        curr_node = self.head
        index_ = 0

        if self.head is None:
            print('Linked list is empty')
            return

        while curr_node:
            if curr_node.data != data:
                curr_node = curr_node.next
                index_ += 1
            if curr_node is None:
                print(f'{data} Not in list')
                return
            if curr_node.data == data:
                print(f'{data} is at index {index_}')
                return
            
        print(f'{data} not in list')
        return
    
    def length(self):
        curr_node = self.head
        index_ = 1
        if self.head is None:
            print('Length 0')
            return

        while curr_node.next != None:
            curr_node = curr_node.next
            index_ += 1

        print(f'Length {index_}')
        return



    def append(self,data):
        '''
        Inserts new element to end of list
        '''
        new_node = Node(data)
        if self.head == None: # check if list is empty if it is append to the first index
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next != None:
            last_node =  last_node.next
        last_node.next = new_node

    def prepend(self,data):
        '''
        Inserts new element to start of list
        '''
        new_node=Node(data)
        new_node.next = self.head
        self.head = new_node
        #curr_node.next = last_node


if __name__ == '__main__':
    ll = SingleLink_list()
    ll.length()
    ll.search(0)
    #ll.add(555,0)
    ll.prepend(5)
    ll.length()
    ll.append(6)
    ll.search(6)
    ll.prepend(456)
    #ll.add(1,1)
    ll.append(9999)
    ll.search(9999)
    ll.search(77)
    ll.length()
    #ll.insert_after_node(6,7777)
    ll.print()