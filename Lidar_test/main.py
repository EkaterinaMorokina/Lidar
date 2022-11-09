import time #библиотека для того чтобы делать задержку
import serial #библиотека на работу с портами
import keyboard #библиотека для возможности взаимодействия с клавиатурой в процессе работы кода, подключал чисто для тестирования и остановки цикла

ser = serial.Serial(port='COM1', baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE) #ser - переменная, можно назвать как угодно, правая часть вызов того, что мы объявляем в эту переменную с набором установок, port - наш порт, baudrate - скорость чтения данных, bytesize - размер для наших данных, битовка, timeout - время ожидания перед следующим заходом, если мы не поставим никакую задержку, stopbits - так и не разобрался, возможно какая-то функция останова


while True: #запускаем бесконечный цикл
    receive = ser.read() #записываем в переменную слева данные с порта с помощью функции .read
    file = open('test.txt','a+') #открываю файл, который предварительно создан был, тебе нужно будет создать, назвать его как угодно можешь, в '' путь к файлу, если файл создан в папке с нашим кодом, то можно как в примере, если нет, то надо скопировать путь до файла, вставить его в '' и перед путем написать r вроде, это лучше прогугли на всякий
    file.write(f'{receive}\n') #запись данных в файл
    time.sleep(1) #задержка
    if keyboard.is_pressed('q'): #условие для останова, если кнопка q нажата (как показывает практике, лчуше зажать ее)
       file.close() #файл закрыть
       break #цикл остановить
ser.close() #закрыть порт