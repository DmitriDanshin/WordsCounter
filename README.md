# Запуск
Для запуска на устройстве должен быть установлен Python версии 3.

1. Распаковать архив.
2. Ввести в консоли.
   
         pip install virtualenv
         cd <путь_к_распакованному_архиву>
         virtualenv venv --python=<ваша_версия_python>
         source venv/bin/activate
         
3. Устанавливаем необходимые пакеты.

         pip install -r requirements.txt
