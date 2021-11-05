class Node:
    def __init__(self, value):
        self.data_value = value
        self.next_node = None

    def insert_after(self,node):
        tmp_node = self.next_node
        self.next_node = node
        node.next_node = tmp_node

    def get_next(self):
        return self.next_node

    def print_data(self):
        print(self.data_value, end = ', ')
    
def print_list(node):
    if node != None:
        node.print_data()
        print_list(node.get_next())

if __name__ == '__main__':
    iterations = 1
    size = int(input('how many integer inputs will there be?: '))
    value = int(input('input value: '))
    head_node = Node(value)
    last_node = head_node
    
    for n in range(1, size):
        iterations = iterations + 1
        value = int(input('input value {} :'.format(iterations)))     
        new_node = Node(value)
        last_node.insert_after(new_node)
        last_node = new_node

print_list(head_node)