print ("Лабораторная работа №1: Лисовой А.А. ИКБО-12-17")
print ("Варианты: 1)17 2)57 3)13 \n")
#Импорт кастомного двусвязного списка:
from DoubleLinkedList import Node, DoubleLinkedList
#Импорт кастомного кольцевого односвязного списка:
from CircularLinkedList import CNode, CircularLinkedList
#Импорт кастомной очереди:
from Queue import QNode, Queue
#Импорт класса-меню:
from Interface import Interface

#Консольное меню:
Menu = Interface()
Menu.Interface_Main()
while True:
    Step = Menu.Input_Controller()
    ###################################################################################
    
    #Первое задание:
    if Step == 1:
        Menu.Interface_Task1()
        #Создание объекта списка:
        List = DoubleLinkedList()
        while True:
            Step = Menu.Input_Controller()
            #Заполнение:
            if Step == 1:
                print ("Меню заполнения списка:")
                print ("Введите изначальную длину двусвязного списка:")
                Length = Menu.Input_Controller()
                #Создание объекта списка:
                List = DoubleLinkedList()
                for i in range(1, Length + 1):
                    print ("Введите ", i, " элемент списка:")
                    Data = str(input(">>>"))
                    Data = Data[0:1]
                    List.Append(Data)
                print ("Ввод списка завершен.")
                Menu.Interface_Task1()
                
            #Вывод двусвязного списка:
            elif Step == 2:
                print ("Меню вывода списка:")
                if List.length == 0:
                    print("Список пуст!")
                else:
                    print("Длина двусвязного списка: ", List.length)
                    print("Двусвязный список: ", List.__repr__())
                    print ("Вывод списка завершен.")
                Menu.Interface_Task1()

            #Добавление элементов в список:
            elif Step == 3:
                Menu.Interface_Task1_Add()
                while True:
                    Step = Menu.Input_Controller()
                    #Добавить в начало:
                    if Step == 1:
                        print ("Введите добавляемый элемент списка:")
                        Data = str(input(">>>"))
                        Data = Data[0:1]
                        List.Prepend(Data)
                        Menu.Interface_Task1_Add()

                    #Добавить в конец:
                    elif Step == 2:
                        print ("Введите добавляемый элемент списка:")
                        Data = str(input(">>>"))
                        Data = Data[0:1]
                        List.Append(Data)
                        Menu.Interface_Task1_Add()

                    #Возврат в подменю:
                    elif Step == 3:
                        Menu.Interface_Task1()
                        break

                    #Остальные случаи:
                    else:
                         print("Ошибка ввода!")

            #Удалить элемент из списка:
            elif Step == 4:
                Menu.Interface_Task1_Del()
                while True:
                    Step = Menu.Input_Controller()
                    #Удалить первый элемент:
                    if Step == 1:
                        List.DeleteFirst()
                        Menu.Interface_Task1_Del()
                        
                    #Удалить последний элемент:
                    elif Step == 2:
                        List.DeleteLast()
                        Menu.Interface_Task1_Del()

                    #Удалить первое вхождение введенного элемента:
                    elif Step == 3:
                        print ("Введите удаляемый элемент списка:")
                        Data = str(input())
                        Data = Data[0:1]
                        List.Remove(Data)
                        Menu.Interface_Task1_Del()

                    #Возврат в подменю:
                    elif Step == 4:
                        Menu.Interface_Task1()
                        break

                    #Остальные случаи:
                    else:
                         print("Ошибка ввода!")
                 
            #Перевернуть список:
            elif Step == 5:
                    List.Reverse()
                    Menu.Interface_Task1()
                
            #Проверить упорядоченность списка по ASCII кодировке:
            elif Step == 6:
                Flag = List.ASCII_Check()
                Menu.Interface_Task1()
                   
            #Выход в главное меню:
            elif Step == 7:
                Menu.Interface_Main()
                break

            #Остальные случаи:
            elif str(Step).isdigit():
                print("Ошибка ввода!")
                
    ###################################################################################
                
    #Второе задание:
    elif Step == 2:
        Menu.Interface_Task2()
        #Создание объекта кольцевого списка:
        L = CircularLinkedList()
        while True:
            Step = Menu.Input_Controller()
            #Создание и заполнение кольцевого списка:
            if Step == 1:
                print ("Меню заполнения кольцевого списка:")
                print ("Введите изначальную длину кольцевого списка:")
                Length = Menu.Input_Controller()
                #Создание объекта списка:
                L = CircularLinkedList()
                for i in range(1, Length + 1):
                    print ("Введите ", i, " элемент списка:")
                    Data = str(input(">>>"))
                    L.Append(Data)
                print ("Ввод списка завершен.")
                Menu.Interface_Task2()
                
            #Вывод кольцевого списка:
            elif Step == 2:
                print ("Меню вывода списка:")
                if L.length == 0:
                    print("Список пуст!")
                else:
                    print("Длина кольцевого списка: ", L.length)
                    print("Кольцевой список: ", L.__repr__())
                    print ("Вывод списка завершен.")
                Menu.Interface_Task2()
  
            #Добавление элементов в кольцевой список:
            elif Step == 3:
                Menu.Interface_Task2_Add()
                while True:
                    Step = Menu.Input_Controller()
                    #Добавить в начало:
                    if Step == 1:
                        print ("Введите добавляемый элемент списка:")
                        Data = str(input(">>>"))
                        L.Prepend(Data)
                        Menu.Interface_Task2_Add()

                    #Добавить в конец:
                    elif Step == 2:
                        print ("Введите добавляемый элемент списка:")
                        Data = str(input(">>>"))
                        L.Append(Data)
                        Menu.Interface_Task2_Add()

                    #Добавить в указанную позицию:
                    elif Step == 3:
                        print ("Введите добавляемый элемент списка:")
                        Data = str(input(">>>"))
                        print ("Введите позицию для вставки:")
                        Position = Menu.Input_Controller()
                        if Position <= L.length + 1:
                            L.Insert(Data, Position)
                        else:
                            print ("Указана недоступная для вставки позиция!")
                        Menu.Interface_Task2_Add()

                    #Возврат в подменю:
                    elif Step == 4:
                        Menu.Interface_Task2()
                        break

                    #Остальные случаи:
                    else:
                        print("Ошибка ввода!")
               
            #Удалить элемент из кольцевого списка:
            elif Step == 4:
                Menu.Interface_Task2_Del()
                while True:
                    Step = Menu.Input_Controller()
                    #Удалить первый элемент:
                    if Step == 1:
                        L.DeleteFirst()
                        Menu.Interface_Task2_Del()
                        
                    #Удалить последний элемент:
                    elif Step == 2:
                        L.DeleteLast() 
                        Menu.Interface_Task2_Del()

                    #Возврат в подменю:
                    elif Step == 3:
                        Menu.Interface_Task2()
                        break

                    #Остальные случаи:
                    else:
                         print("Ошибка ввода!")

            #Поиск пары совпадений:
            elif Step == 5:
                print("Меню поиска пары последовательных совпадающих значений:")
                L.SearchEqualPair()
                Menu.Interface_Task2()

            #Выход в главное меню:
            elif Step == 6:
                Menu.Interface_Main()
                break

            #Остальные случаи:
            elif str(Step).isdigit():
                print("Ошибка ввода!")
                
    ###################################################################################
                
    #Третье задание:
    elif Step == 3:
        #Третье задание:
        Menu.Interface_Task3()
        #Создание объекта очереди:
        Q = Queue()
        while True:
            Step = Menu.Input_Controller()
            #Создание и заполнение очереди:
            if Step == 1:
                print ("Меню заполнения очереди:")
                print ("Введите изначальную длину очереди:")
                Length = Menu.Input_Controller()
                #Создание объекта очереди:
                Q = Queue()
                for i in range(1, Length + 1):
                    print ("Введите ", i, " элемент очереди:")
                    Data = Menu.Int_Controller()
                    Q.Enqueue(Data)
                    print ("Элемент успешно помещен в очередь!")
                print ("Ввод списка завершен.")
                Menu.Interface_Task3()

            #Вывод очереди:
            elif Step == 2:
                print ("Меню вывода очереди:")
                if Q.length == 0:
                    print("Очередь пуста!")
                else:
                    print("Длина очереди: ", Q.length)
                    print("Очередь: ", Q.__repr__())
                    print ("Вывод очереди завершен.")
                Menu.Interface_Task3()

            #Добавление элемента в очередь:
            elif Step == 3:
                print ("Меню добавление элемента в очередь:")
                print ("Введите добавляемый элемент очереди:")
                Data = Menu.Int_Controller()
                Q.Enqueue(Data)
                print ("Элемент успешно помещен в очередь!")
                Menu.Interface_Task3()

            #Удаление элемента из очереди:
            elif Step == 4:
                print ("Меню удаления элемента из очереди:")
                Q.Dequeue()
                print ("Элемент успешно удален из очереди!")
                Menu.Interface_Task3()

            #Подсчет свободных от квадратов чисел:
            elif Step == 5:
                print ("Меню подсчета несвободных квадратов:")
                Q.NQVD_Counter()
                Menu.Interface_Task3()
                
            #Выход в главное меню:
            elif Step == 6:
                Menu.Interface_Main()
                break

            #Остальные случаи:
            elif str(Step).isdigit():
                print("Ошибка ввода!")
            
    ###################################################################################         
           
    #Выход из программы
    elif Step == 4:
        print("Выход из программы осуществлен!")
        break

    #Остальные случаи:
    elif str(Step).isdigit():
        print("Ошибка ввода!")
        
        
        
        










    

