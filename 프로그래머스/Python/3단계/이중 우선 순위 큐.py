"""
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

  - I 숫자	큐에 주어진 숫자를 삽입합니다.
  - D 1	큐에서 최댓값을 삭제합니다.
  - D -1	큐에서 최솟값을 삭제합니다.

이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 
모든 연산을 처리한 후 큐가 비어있으면 [0,0] 
비어있지 않으면 [최댓값, 최솟값]을 return 하도록 solution 함수를 구현해주세요.
"""

# 내 풀이
def solution(operations):
    Q = []
    
    for op in operations:
        Q.sort()
        op = op.split(' ')  # 공백을 기준으로 명령어 구분
        cm, data = op
        if cm == "I":
            Q.append(int(data))
        elif cm == "D":
            if data == "-1":
                Q = Q[1:] # max(Q)를 이용하여 최댓값을 삭제할 경우, 빈 배열에서 오류가 발생 => 슬라이드 사용
            elif data == "1":
                Q = Q[:len(Q)-1]
                
    if len(Q) <= 0:
        return [0,0]

    return [max(Q), min(Q)]

# 다른사람 풀이(이진 탐색 트리 구현)
from heapq import heappush, heappop
from collections import deque

class Node:
    def __init__(self,value,left=None,right=None):
        self.value,self.left,self.right= value,left,right
class BST:
    def __init__(self,head):
        self.head= head # node

    # insert
    def insert(self,value):
        if not self.head:
            self.head= Node(value)
            print(value,'노드 없어서 노드 만들어줌.')
            return True
        self.cn = self.head # current_node
        while self.cn:
            if value < self.cn.value:
                if self.cn.left:    
                    self.cn= self.cn.left
                else:
                    self.cn.left= Node(value)
                    print(value,'왼쪽에 추가')
                    return True
            else:
                if self.cn.right:
                    self.cn= self.cn.right
                else:
                    self.cn.right= Node(value)
                    print(value, '오른쪽에 추가')
                    return True
    # delete
    def delete_max(self):
        if not self.head:
            print('빈 큐라 삭제 못함')
            return 'empty'

        if not self.head.left and not self.head.right:
            self.head= None
            return

        if self.head.left and not self.head.right:
            self.head= self.head.left
            return

        # 가장 오른쪽에 있는 노드 제거.
        self.p= self.head
        self.cn= self.head

        while self.cn.right:
            self.p= self.cn
            self.cn= self.cn.right

        ## leaf node인 경우
        if not self.cn.left:
            self.p.right= None
            #del self.cn
            print('삭제')
            return True
        ## left node를 가지는 경우
        elif self.cn.left:
            self.p.right= self.cn.left
            #del self.cn
            print('삭제')
            return True

    def delete_min(self):
        if not self.head:
            return 'empty'
        if not self.head.left and not self.head.right:
            self.head= None
            return

        if not self.head.left and self.head.right:
            self.head= self.head.right
            return

        # 가장 왼쪽에 있는 노드 제거.
        self.p= self.head
        self.cn= self.head

        while self.cn.left:
            self.p= self.cn
            self.cn= self.cn.left

        ## leaf node인 경우
        if not self.cn.right:
            self.p.left= None
            #del self.cn
            print('삭제')
            return True
        ## right node를 가지는 경우
        elif self.cn.left:
            self.p.left= self.cn.right
            #del self.cn
            print('삭제')
            return True 

    def search(self):

        max_min= [0,0]
        if not self.head:
            return max_min

        # 가장 왼쪽에 있는 노드 찾기.
        self.p= self.head
        self.cn= self.head
        while self.cn.left:
            print('p',self.p.value)
            print('cn',self.cn.value)
            self.p= self.cn
            self.cn= self.cn.left
        max_min[1]= self.cn.value

        # 가장 오른쪽에 있는 노드 찾기.
        self.p= self.head
        self.cn= self.head
        while self.cn.right:
            print('p',self.p.value)
            print('cn',self.cn.value)
            self.p= self.cn
            self.cn= self.cn.right
        max_min[0]= self.cn.value    
        return max_min

def solution(operations):

    bst= BST(None)
    for o in operations:
        if o[0] == 'I':
            bst.insert(int(o[2:]))
        elif o == 'D -1':
            bst.delete_min()
        elif o == 'D 1':
            bst.delete_max()

    return bst.search()
