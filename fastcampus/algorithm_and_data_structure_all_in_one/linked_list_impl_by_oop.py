class Node:
    def __init(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self):
        if self.head == '':
            print("해당 값을 가진 노드가 없습니다.")
            return

        # 1. head 삭제
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                # 2. 마지막 노드 삭제
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                # 3. 중간 노드 삭제
                else:
                    node = node.next

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
