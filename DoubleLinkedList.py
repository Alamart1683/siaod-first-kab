#Класс-узел списка Node:
class Node:
    #Конструктор:
    def __init__(self, prev = None, data = None, next = None): 
        self.prev = prev
        self.data = data 
        self.next  = next
        
    #Метод преобразования в строку:
    def __repr__(self):
        return repr(self.data) 
    
#Класс двусвязного списка:
class DoubleLinkedList:
    #Конструктор:
    def __init__(self, length = 0): 
        self.head = self.tail = None
        self.length = 0
        
    #Преобразование к строке:
    def __repr__(self):
        Nodes = []
        if not self.head:
            return '[' + ', '.join(Nodes) + ']'
        Current = self.head
        while Current:
            Nodes.append(repr(Current))
            Current = Current.next
        return '[' + ', '.join(Nodes) + ']'

    #Вставить элемент в конец списка:
    def Append(self, data):
        if not self.head:
            self.head = self.tail = Node(data = data)
            self.length += 1
            print ("Элемент был добавлен в конец списка.")
            return
        Current = self.head
        while Current.next:
            Current = Current.next
        Current.next = self.tail = Node(data = data, prev = Current)
        self.length += 1
        print ("Элемент был добавлен в конец списка.")

    #Вставить элемент в начало списка:
    def Prepend(self, data):
        new_head = Node(data = data, next = self.head)
        if not self.head:
            self.head = self.tail = Node(data = data)
            self.length += 1
            print ("Элемент был добавлен в начало списка.")
        elif self.head:
            self.head.prev = new_head
        self.head = new_head
        self.length += 1
        print ("Элемент был добавлен в начало списка.")

    #Найти элемент в списке:
    def Find(self, key):
        Current = self.head
        while Current and Current.data != key:
            Current = Current.next
        return Current

    #Удалить узел из списка:
    def Delete(self, Node):
        if Node.prev:
            Node.prev.next = Node.next
        if Node.next:
            Node.next.prev = Node.prev
        if Node is self.head:
            self.head = Node.next
        if Node is self.tail:
            self.tail = Node.prev
        Node.prev = None
        Node.next = None

    #Удалить первое вхождение элемента из списка:
    def Remove(self, key):
        if self.length == 0:
           print("Список пуст!")
        else:
            Element = self.Find(key)
            if not Element:
                print ("Такого элемента в списке нет!")
                return 
            self.Delete(Element)
            print ("Первое вхождение введенного элемента удалено!")
            self.length -= 1

    #Удалить первый элемент списка:
    def DeleteFirst(self):
        if self.head != None:
            self.Delete(self.head)
            self.length -= 1
            print ("Элемент успешно удален!")
        else:
            print("Список пуст!")
            return

    #Удалить последний элемент списка:
    def DeleteLast(self):
        if self.length == 0:
           print("Список пуст!")
        elif self.length == 1:
            self.Delete(self.head)
            self.length -= 1
        elif self.tail:
            self.Delete(self.tail)
            self.length -= 1
            print ("Элемент успешно удален!")
        
    #Перевернуть список:
    def Reverse(self):
        print("Меню переворачивания списка:")
        if self.length == 0:
            print("Список пуст!")
        elif self.length == 1:
            print("Список был успешно перевернут!")
        else:
            self.tail = self.head
            Current = self.head
            Previous_Node = None
            while Current:
                Previous_Node = Current.prev
                Current.prev = Current.next
                Current.next = Previous_Node
                Current = Current.prev
            self.head = Previous_Node.prev
            print("Список был успешно перевернут!")

    #Проверка упорядоченности по ASCII коду:
    def ASCII_Check(self):
        print("Меню проверки упорядоченности:")
        if self.length == 0:
            print("Список пуст!")
        else:
            Current = self.head
            Plus = 0
            Minus = 0
            #Цикл прохода по списку попарно:
            while Current and Current.next:
                Old_Current_Data = Current.data
                Current_Data = Current.next.data
                if ord(Old_Current_Data) < ord(Current_Data): 
                    Plus += 1
                elif ord(Old_Current_Data) == ord(Current_Data):
                    Plus += 1
                    Minus += 1
                elif ord(Old_Current_Data) > ord(Current_Data):
                    Minus += 1
                Current = Current.next
            if Plus == self.length - 1:
                print ("Элементы списка упорядочены по кодам ASCII!")
            elif Minus == self.length - 1:
                print ("Элементы списка упорядочены по кодам ASCII!")
            else:
                print ("Элементы списка не упорядочены по кодам ASCII!")
        
            
