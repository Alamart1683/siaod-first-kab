#Класс-узел очереди:
class QNode:
    #Конструктор:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
        
    #Метод преобразования узла в строку:
    def __repr__(self):
        return repr(self.data)

#Класс очереди:
class Queue:
    #Конструктор:
    def __init__(self, length = 0):
        self.head = None
        self.length = 0
        
    #Преобразование к строке:
    def __repr__(self):
        QNodes = []
        Current = self.head
        if not self.head:
            return '[' + ', '.join(QNodes) + ']'
        if not Current.next:
            QNodes.append(repr(Current))
        else:
            QNodes.append(repr(Current))
            Current = self.head.next
            while Current:
                QNodes.append(repr(Current))
                Current = Current.next
        return '[' + ', '.join(QNodes) + ']'

    #Поместить в очередь:
    def Enqueue(self, data):
        if not self.head:
            self.head = QNode(data)
            self.length += 1
            return
        else:
            Current = self.head
            while Current.next:
                Current = Current.next
            Current.next = QNode(data)
            self.length += 1

    #Удалить из очереди:
    def Dequeue(self):
        if self.length == 0:
            print ("Очередь пуста!")
        else:
            if not self.head.next:
                Head_Buffer = self.head
                self.head = self.head.next
                self.length -= 1
                return Head_Buffer.data
            else:
                Current = Head_Buffer = self.head
                while Current:
                    Current = Current.next
                self.head = Head_Buffer.next
                Current = self.head
                self.length -= 1
                return Head_Buffer.data

    #Получить элемент из очереди:
    def Peek(self):
        return self.head

    #Вычислить количество чисел, свободных от квадратов:
    def NQVD_Counter(self):
        if self.length == 0:
            print ("Очередь пуста!")
        else:
            Count = 0
            Current = self.head
            while Current:
                if self.NonQuadValuesDetector(Current.data):
                    Count += 1
                Current = Current.next
            if Count > 0:
                print ("Данная очередь содержит " + str(Count) + " свободных от квадратов чисел!")
            else:
                print ("Данная очередь не содержит свободных от квадратов чисел!")

    #Функция опеределния свободы от квадртов
    def NonQuadValuesDetector(self, data):
        #Очередь, хранящяя квадраты простых чисел:
        QuadPrimeQueue = Queue()
        if data > 0:
            for value in range(2, data):
                if value*value <= data and self.PrimeDetector(value):
                    QuadPrimeQueue.Enqueue(value*value)
            #Цикл проверки элемента на делимость квадратами:
            for value in range(1, QuadPrimeQueue.length + 1):
                if data % QuadPrimeQueue.Dequeue() == 0:
                    return False
            return True
            
    #Детектор простых чисел:
    def PrimeDetector(self, data):
        for value in range(2, 11):
            check = False
            if value == data:
                continue
            if data % value != 0:
                check = True
            if check == False or data == 1 or data == 0:
                return False
        return True
        
                






























            
