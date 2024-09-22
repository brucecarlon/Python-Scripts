from LinkedLists import SingleLink_list

class Queue(SingleLink_list):
    def __init__(self):
        super().__init__()

    def add(self,data):
        self.prepend(data)
        return

    def dequeue(self):
        self.pop()
        return
    
    def length(self) -> int:
        return super().length()
    
    def erase(self, index):
        indx= self.length() -1
        return super().erase(index)

if __name__ == '__main__':
    que = Queue()
    que.add('guest')
    que.add(5)
    que.add('free')
    que.print()
    que.dequeue()
    que.print()
    que.length()
    que.erase(1)
    que.print()