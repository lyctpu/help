def Menu():
    print('Выберите тип задачи: \n 1 - кодирование текстовой информации \n 2 - кодирование звука \n 3 - кодирование изображения \n Для выхода введите 0 \n')
    type = input('Тип задачи: ')
    if type == '1': InfC()
    if type == '2': SoC()
    if type == '3': ImC()
    if type == '0': exit()
    else:
        print('Произошла ошибка, попробуйте ещё раз')
        Menu()
def InfC():
    def formIn1():
        formIn = input('\nКакую формулу используем? \n 1: N = 2^i (N - мощность алфавита, i - разрядность двоичного кода) \n 2: I = k * i (I - информационный объём текста, k - количество символов, i - информационный вес одного символа) \n 0: отмена, вернуться в меню \n')
        if formIn == '1':
            def find1():
                find = input('\n Что ищем:\n1: N (мощность алфавита) \n2: i (разрядность двоичного кода)?:\n')
                if find == '1':
                    i = int(input(' Введите разрядность двоичного кода (i) в битах: '))
                    if type(i)== int:
                        N = 2 ** i
                        res = input(f'N = {int(N)} \n\n Ищем что-нибудь ещё по кодированию текстовой информации? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res =='1':
                            formIn1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit() 
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find1()
                elif find == '2':
                    N = int(input(' Введите мощность алфавита (N): '))
                    if type(N)==int:   
                        i = 0
                        if not N <= 1:
                            i += 1
                            N = N/2
                        elif i < 8 or i % 8 != 0:
                            res = input(f'i = {int(i)} бит \n\n Ищем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет):\n')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif i >= 8:
                            res = input(f'i (разрядность двоичного кода) = {round(i/8,3)} байт или {int(i)} бит\n\n Ищем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет):\n')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        exit()
                else:
                    print('Произошла ошибка, попробуйте ещё раз')
                    find1()
            find1()    
                                                                  
        elif formIn == '2':
            def find2():
                find = input('\nЧто ищем:\n 1: I (информационный объём текста)\n 2: k (кол-во символов)\n 3: i (информационный вес одного символа)?:\n')
                if find == '1':
                    k = int(input(' Введите количество символов (k): '))
                    i = int(input(' Введите информационный вес одного символа (i) в битах: '))
                    if type(k) and type(i)==int:
                        I = k * i
                        res= input(f'Требуется ли перевести ответ в \n1: байты\n2: Кб \n3: Мб \n4: Гб \n5: Тб \n6: нет, не требуется\n') 
                        if res == '1':
                            res= input(f'I = {I/8} байт \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n ')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif res=='2':
                                res= input(f'I = {I/8/1024} Кб \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n ')
                                if res == '2':
                                    Menu()
                                elif res =='1':
                                    formIn1()
                                else:
                                    print('Произошла ошибка, попробуйте ещё раз')
                                    exit()
                        elif res=='3':
                            res= input(f'I = {I/8/1024/1024} Мб \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n ')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit() 
                        elif res=='4':
                            res= input(f'I = {I/8/1024/1024/1024} Гб \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n ')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else: 
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()                                              
                        elif res == '5':
                            res= input(f'I = {I/8/1024/1024/1024/1024} Тб \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n ') 
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else: 
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()                    
                        elif res =='6':
                            res= input(f'I = {int(I)} бит \n Ищем что-то ещё по кодированию текстовой информации?(1 - да, 2 - нет):\n')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else: 
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()   
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find2()
                elif find == '2':
                    I = int(input(' Введите информационный объём текста (I) в битах: '))
                    i = int(input(' Введите информационный вес одного символа (i) в битах: '))
                    if type(I) and type(i)==int:
                        k = I / i
                        res = input(f'k = {int(k)} \n\nИщем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res =='1':
                            formIn1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find2()
                elif find == '3':
                    k = int(input(' Введите кол-во символов (k): '))
                    I = int(input(' Введите информационный объём текста (I) в битах: '))
                    if type(k) and type(I)== int:
                        i = I / k
                        if i < 8 or i % 8 != 0:
                            res = input(f'i= {int(i)} бит \n\nИщем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif i >= 8:
                            res = input(f'i = {round(i/8,3)} байт \n\nИщем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIn1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit() 
                    else:
                        print('Произошла ошибка, попробуйте ещё раз') 
                        find2()           
                elif formIn == '0':
                    Menu()
                else:
                    formIn1()
            find2()
    formIn1()

def SoC():
    def formSo1():
        formSo = input('Какую формулу используем? \n 1: H = 1/T (H - частота дискретизации, T - шаг дискретизации) \n 2: K = 2^b (K - количество уровней квантования, b - глубина кодирования/разрядность квантования) \n 3: I = RHtb (I - объём звуковой информации, 4: R - количество каналов, 5: H - частота дискретизации, 6: t - время записи, 7: b - глубина кодирования/разрядность квантования) \n 0: отмена, вернуться в меню \n')
        if formSo == '1':
            def find3():
                find = input('\nЧто ищем: 1: H (частоту дискретизации)\n 2: T (шаг дискретизации)?: ')
                if find == '1':
                    H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                    if type(H)==int:
                        T = 1 / H
                        res = input(f'T= {T} с \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res=='1':
                            formSo1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find3()

                elif find == '2':
                    T = int(input(' Введите шаг дискретизации (T) в секундах: '))
                    if type(T)==int:
                        H = 1 / T
                        if H < 1000:
                            res = input(f'H= {H} Гц\n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif H >= 1000:
                            res = input(f'H = {H/1000} кГц\n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find3()
            find3()            
        elif formSo == '2':
            def find4():
                find = input('\nЧто ищем: 1:кол-во уровней квантования (K) \n2:глубину кодирования/разрядность квантования (b)?:\n ')
                if find == '1':
                    b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                    if type(b)==int:
                        K = 2 ** b
                        res = input(f'K = {K} \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res=='1':
                            formSo1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find4()
                elif find == '2':
                    K = int(input(' Введите количество уровней квантования (K): '))
                    if type(K)==int:
                        b = 0
                        if not K <= 1:
                            b += 1
                            K = K/2
                            res = input(f'b = {b} бит \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            find4()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find4()
            find4()        
        elif formSo == '3':
            find = input('\nЧто ищем:\n 1: I (объём звуковой информации)\n 2: R (количество каналов)\n 3: H (частоту дискретизации)\n 4: t (время записи)\n 5: b (глубину кодирования/разрядность квантования)?:\n ')
            def find5():
                if find == '1':
                    R = int(input(' Введите количество каналов (R): '))
                    H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                    t = int(input(' Введите время записи (t) в секундах: '))
                    b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                    if type(R) and type(H) and type(t) and type(b):
                        I = R * H * t * b
                        if I < 8:
                            res = input(f'I = {I} битов \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif I < 8*1024:
                            res = input(f'I = {I/8} байт \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif I < 8*1024*1024:
                            res = input(f'I = {I/8/1024} Кб \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif I < 8*1024*1024*1024:
                            res = input(f'I = {I/8/1024/1024} Мб \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif I < 8*1024*1024*1024*1024:
                            res = input(f'I = {I/8/1024/1024/1024} Гб \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif I >= 8*1024*1024*1024*1024:
                            res = input(f'I= {I/8/1024/1024/1024/1024} Тб \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        elif res == '2':
                             Menu()
                        elif res=='1':
                            formSo1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find5()

                elif find == '2':
                    I = int(input(' Введите объём звуковой информации (I) в битах: '))
                    H = int(input(' Введите частоту дискретизации (H): '))
                    t = int(input(' Введите время записи (t) в секундах: '))
                    b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                    if type(I) and type(H) and type(t) and type(b)==int:
                        R = I / (H * t * b)
                        res = input(f'R = {int(R)} \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res=='1':
                            formSo1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find5()

                elif find == '3':
                    I = int(input(' Введите объём звуковой информации (I) в битах: '))
                    R = int(input(' Введите количество каналов (R): '))
                    t = int(input(' Введите время записи (t) в секундах: '))
                    b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                    if type(I) and type(R) and type(t) and type(b)==int:
                        H = I / (R * t * b)
                        if H < 1000:
                            res = input(f'H = {H} Гц\n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif H >= 1000:
                            res = input(f'H = {H/1000} кГц\n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            find5()
                elif find == '4':
                    b = int(input(' Введите глубину кодирования/разрядность квантования (b) в битах: '))
                    I = int(input(' Введите объём звуковой информации (I) в битах: '))
                    H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                    R = int(input(' Введите количество каналов (R): '))
                    if type(b) and type(I) and type(H) and type(R)==int:
                        t = I / (R * H * b)
                        if t < 60:
                            res = input(f't= {t} с \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif t < 3600:
                            res = input(f't= {int(t//60)}:{t%60} мин \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif t >= 3600:
                            res = input(f't= {int(t//3600)}:{int((t%3600)//60)}:{(t%3600)%60} ч \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                            if res == '2':
                                Menu()
                            elif res=='1':
                                formSo1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                elif find == '5':
                    t = int(input(' Введите время записи (t) в секундах: '))
                    I = int(input(' Введите объём звуковой информации (I) в битах: '))
                    H = int(input(' Введите частоту дискретизации (H) в Гц: '))
                    R = int(input(' Введите количество каналов (R): '))
                    if type(t) and type(I) and type(H) and type(R)==int:
                        b = I / (R * H * t)
                        res = input(f'b = {int(b)} бит \n\nИщем что-то ещё по кодированию звука? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        elif res=='1':
                            formSo1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find5()
            find5()
        elif formSo == '0':
            Menu()
        else:
            formSo1()
    formSo1()

def ImC():
    def formIm1():
        formIm = input('Какую формулу используем? \n 1: N = 2^i (N - количество цветов, i - разрядность двоичного кода) \n 0: отмена, вернуться в меню \n')
        if formIm == '1':
            def find6():
                find = input('\nЧто ищем:\n 1: N количество цветов (N)\n 2: разрядность двоичного кода (i)?:\n ')
                if find == '1':
                    i = int(input(' Введите разрядность двоичного кода (i) в битах: '))
                    if type(i)== int:
                        N = 2 ** i
                        res = input(f'N = {int(N)} \n\n Ищем что-нибудь ещё по кодированию текстовой информации? (1 - да, 2 - нет): ')
                        if res == '2':
                            Menu()
                        if res =='1':
                            formIm1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit() 
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find6()
                elif find == '2':
                    N = int(input(' Введите мощность алфавита (N): '))
                    if type(N)==int:   
                        i = 0
                        if not N <= 1:
                            i += 1
                            N = N/2
                        elif i < 8 or i % 8 != 0:
                            res = input(f'i = {int(i)} бит \n\n Ищем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет):\n')
                            if res == '2':
                                Menu()
                            if res =='1':
                                formIm1()
                            else:
                                print('Произошла ошибка, попробуйте ещё раз')
                                exit()
                        elif i >= 8:
                            res = input(f'i (разрядность двоичного кода) = {round(i/8,3)} байт или {int(i)} бит\n\n Ищем что-то ещё по кодированию текстовой информации? (1 - да, 2 - нет):\n')
                            if res == '2':
                                Menu()
                            elif res =='1':
                                formIm1()
                        else:
                            print('Произошла ошибка, попробуйте ещё раз')
                            exit()
                    else:
                        print('Произошла ошибка, попробуйте ещё раз')
                        find6()
            find6()
        elif formIm == '0':
            Menu()
    formIm1()
Menu()