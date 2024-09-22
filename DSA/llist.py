

class Node():
    '''
    creates a data node '''
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    

class llist():
    '''
    creates a singly linked list'''
    def __init__(self):
        self.head = None

    def search(self,data):
        '''
        Returns index of first instance of data object'''
        if self.head is None:
            print('List is empty')
            return
        
        pointer = self.head
        index_ = 0
        while pointer:
            if pointer.data == data:
                print(f'The first instance of {data } is at position {index_ + 1}')
                return
            pointer=pointer.next
            index_  += 1
        print(f'{data} not in list')
        return

    def prepend(self,data):
        '''
        Adds a data node at the start of the list
        '''
        node = Node(data, next = self.head)
        self.head = node
        return

    def print(self):
        llstr = ''
        pointer = self.head
        while pointer:
            llstr += str(pointer.data)+ '-->'
            pointer = pointer.next
        print(llstr)

    def append(self,data):
        '''
        adds data node at end of string
        '''
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        pointer = self.head

        while pointer.next:
            pointer = pointer.next
        pointer.next= node
        return

    def length(self):
        count = 0
        pointer = self.head
        while pointer:
            count += 1
            pointer = pointer.next
        return count

    def insert_list(self,data_list):
        if self.head is None:
            for data in data_list[::-1]:
                self.prepend(data)
        return

    def delete_at(self,index_):
        len_ = self.length()
        if self.head is None:
            print('list is empty')
        if index_> len_:
            print(f'invalid index, list length = {len_}')

        iterator_ = self.head
        index_checker = 0
        while True:
            pointer = iterator_
            iterator_ = iterator_.next
            if index_checker == index_ :
                pointer.next = iterator_.next
                return
            index_checker + 1
            
    def insert_at(self,index_, data):
        node = Node(data)
        # if index_ > self.length:
        #     print(f'invalid index, list length = {len_}')
        
        pointer = self.head
        counter = 0

        while pointer:
            if counter == index_ - 1:
                node.next = pointer.next
                pointer.next = node
                break
            pointer = pointer.next
            counter += 1

if __name__ == '__main__':
    ll = llist()
    ll.prepend(5)
    ll.append('add')
    print(f'length is {ll.length()}')
    ll.insert_at(1,'jjj')

    ll.insert_at(0,'king')
    ll.insert_at(3,55)
    ll.search('jjj')
    ll.search(5)
    ll.search('hksfbh')
    ll.print()
    ll.delete_at(0)
    ll.print()
    