#Класс-узел кольцевого списка:
class CNode:
    #Конструктор:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    #Метод преобразования в строку:
    def __repr__(self):
        return repr(self.data)

#Класс кольцевого односвзяного списка:
class CircularLinkedList:
    #Конструктор:
    def __init__(self, length = 0):
        self.head = None
        self.length = 0

    #Преобразование к строке:
    def __repr__(self):
        CNodes = []
        Current = self.head
        if not self.head:
            return '[' + ', '.join(CNodes) + ']'
        if not Current.next:
            CNodes.append(repr(Current))
        else:
            CNodes.append(repr(Current))
            Current = self.head.next
            while Current != self.head:
                CNodes.append(repr(Current))
                Current = Current.next
        return '[' + ', '.join(CNodes) + ']'

    #Вставить в конец списка:
    def Append(self, data):
        if not self.head:
            self.head = CNode(data)
            self.head.next = self.head
            self.length += 1
        else:
            Current = self.head
            while Current.next != self.head:
                Current = Current.next
            Current.next = CNode(data)
            Current.next.next = self.head
            self.length += 1
        print ("Элемент был добавлен в конец списка!")

    #Вставить в начало списка:
    def Prepend(self, data):
        if not self.head:
            self.head = CNode(data)
            self.head.next = self.head
            self.length += 1
        else:
            Current = self.head
            while Current.next != self.head:
                Current = Current.next
            New_Node = CNode(data)
            New_Node.next = self.head
            self.head = New_Node
            Current.next = self.head
            self.length += 1
        print ("Элемент был добавлен в начало списка!")

    #Вставить после указанной позиции:
    def Insert(self, data, position):
        if not self.head:
            self.head = CNode(data)
            self.head.next = self.head
            self.length += 1
        else:
            if position == self.length + 1:
                self.Append(data)
            elif position == 1:
                self.Prepend(data)
            else:
                Current = self.head
                Current_Position = 0
                while Current_Position < position - 2:
                    Current = Current.next
                    Current_Position += 1
                New_Node = CNode(data)
                New_Node.next = Current.next
                Current.next = New_Node
                self.length += 1
                print ("Элемент был успешно добавлен в указанную позицию!")
            
    #Удалить первый элемент списка:
    def DeleteFirst(self):
        if self.length == 0:
            print("Список пуст!")
        elif self.head.next == self.head:
                self.head = None
                self.length -= 1
                print ("Первый элемент успешно удален!")
        else:
            Current = Head_Buffer = self.head
            while Current.next != self.head:
                Current = Current.next
            self.head = Head_Buffer.next
            Current.next = self.head
            self.length -= 1
            print ("Первый элемент успешно удален!") 
        

    #Удалить последний элемент списка:
    def DeleteLast(self):
        if self.length == 0:
           print("Список пуст!")
        elif self.head.next == self.head:
            self.head = None
            self.length -= 1
            print ("Последний элемент успешно удален!")
        else:
            Current = self.head.next
            while Current.next.next != self.head:
                Current = Current.next
            Current.next = self.head
            self.length -= 1
            print ("Последний элемент успешно удален!")

    #Определить, есть ли в списке хотя бы один элемент, который равен следующему:
    def SearchEqualPair(self):
        if self.length < 2:
            print ("Данный список не содержит в себе пары значений!")
        else:
            Current = self.head
            while Current.next != self.head:
                if Current.data == Current.next.data:
                    print("Данный список содержит пару совпадающих по кругу значений!")
                    print("Это \'" + Current.data + "\' и \'" + Current.next.data + "\' соответственно.")
                    return
                Current = Current.next
                if Current.data == Current.next.data:
                    print("Данный список содержит пару совпадающих по кругу значений!")
                    print("Это \'" + Current.data + "\' и \'" + Current.next.data + "\' соответственно.")      
                    return
            print("Данный список не содержит пару совпадающих по кругу значений!")
        
    
                

    






















    

    
        
