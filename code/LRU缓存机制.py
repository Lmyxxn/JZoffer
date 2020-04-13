
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # 新建两个节点 head 和 tail
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化链表为 head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # 因为get与put操作都可能需要将双向链表中的某个节点移到头部，所以定义一个方法
    def move_node_to_head(self, key):
        node = self.hashmap[key]
        ##### 把node从链表中拿出
        node.prev.next = node.next
        node.next.prev = node.prev
        ##### 把node放到链表最前面，即head之后
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head

    def get(self, key: int) -> int:
        # 如果key本身已经在哈希表中了就不需要在链表中加入新的节点
        # 但是需要更新字典该值对应节点的value
        if key in self.hashmap:
            # 之后将该节点移到头部
            self.move_node_to_head(key)
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.hashmap[key].value = value
            self.move_node_to_head(key)
        else:
            if len(self.hashmap) == self.capacity:
                # 去掉哈希表对应项
                self.hashmap.pop(self.tail.prev.key)
                # 去掉最久没有被访问过的节点，即尾节点之前的节点
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail

            # 如果不在的话就插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.head
            new.next = self.head.next
            self.head.next.prev = new
            self.head.next = new

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)