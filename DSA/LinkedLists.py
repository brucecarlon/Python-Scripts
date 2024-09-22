class Node:
    def __init__(self, data = None,next = None) -> None:
        self.data = data
        self.next = next

class SingleLink_list:
    
    def __init__(self) -> None:
        self. head = None
 
    def print(self):
        curr_node = self.head
        s_list =''
        while curr_node:
            s_list = s_list + str(curr_node.data)+'-->'
            curr_node = curr_node.next
        print(s_list)

    def search(self,data):
        curr_node = self.head
        index_ = 0

        if self.head is None:
            print(f'{data} not found. List is empty')
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
        return index_

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

    def insert(self, data, position):
        new_node = Node(data)
        if self.head is None or position== 0:
            self.head =  new_node

        index_count = 0
        curr_node = self.head

        while curr_node:
            if position != index_count +1:
                curr_node = curr_node.next
                index_count += 1
            if position == index_count +1:
                curr_node.next = new_node
                new_node.next = curr_node.next
                return

    def pop(self):
        '''
        Removes last item in list
        '''

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node = None
        return

    def erase(self, index):
        curr_node = self.head
        list_length = self.length()
        count= 0
        
        if index > list_length:
            print('invalid index') #raise expection
            return

        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if count == index:
                last_node.next = curr_node.next
                return
            count +=1


if __name__ == '__main__':
    ll = SingleLink_list()
    ll.length()
    ll.search(0)
    ll.prepend(5)
    ll.length()
    ll.append(6)
    ll.search(6)
    ll.prepend(456)
    ll.append(9999)
    ll.search(9999)
    ll.search(77)
    ll.length()
    ll.print()
    ll.erase(2)
    ll.print()