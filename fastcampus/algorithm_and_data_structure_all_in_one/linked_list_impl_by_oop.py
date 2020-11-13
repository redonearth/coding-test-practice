# Node 구현
# 파이썬에서 일반적으로 링크드 리스트 구현 시, 파이썬 클래스를 활용
# 파이썬 객체지향 문법 이해 필요
class Node:
    def __init(self, data, next=None):
        self.data = data
        self.next = next


class NodeMgmt:
    def __init__(self, data):
        self.head = Node(data)

    # 링크드 리스트의 복잡한 기능1 (링크드 리스트 사이에 데이터 추가)
    def add(self, data):
        if self.head == '':
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 링크드 리스트의 복잡한 기능2 (특정 노드를 삭제)
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
