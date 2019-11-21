## Hikka Slots

___


#### Console schedule & todo-list app with diet/weight/nutrients/habbits control

#### Консольное приложение для личного расписания и списка дел с контролем над диетой/весом/питательными веществами/привычками

___


Usage: you need to fill up my_values_placeholder.py, and all you need to replace in activities/ module (action slots, video, audio, time, names, randomizer etc.), and run main.py from terminal/console/comand-line

Использование: вам нужно заполнить файл my_values_placeholder.py своими данными, а также заменить всё что вам нужно в модуле activities/ (слоты действий, видео, аудио, время, названия, рэндомайзер и т.д.) и запустить main.py в консоли\терминале\командной строке

___


Then used - it creates a file named day_file_YYYY_MM_DD.md in day_files folder with contents considered your input in terminal or previous day file. (example - day_file_2019_11_20_example.md in project folder)

> Input fields ('__') of previous day analysed in app to collect and control data. If you'll not fill up this fields in day file, app will ask you a questions in terminal. If you skip questions both in day file and terminal, input will be None and any habbits will be failed (counters will be reset, and app will use previous weight\diet data).

##### Contents of day file:
+ 1 section - Date, name
+ 2 section - Bad habbits control (smoking in this case), fail inputs are: "-", "no", "нет"
+ 3 section - Good habbits control (good deeds in this case)
+ 4 section - Personal Development control (new knowledge and skills in this case)
+ 5 section - Weight/body parameters control (can be extended with sport results)
+ 6 section - Diet considered with weight, parameters, swings(fasting days, celebrations, holidays etc.)
+ 7 section - Schedule and ToDo list
+ 8 section - Days of app usage

___


Создаёт файл с именем вида day_file_ГГГГ_ММ_ДД.md в папке day_files и содержанием, соответствующим вашим выборам в консоли и данным, введённым в файле предыдущего дня. (пример - day_file_2019_11_20_example.md в корневой папке проекта)

> Поля для ввода ('__') прошлого дня анализируются программой для подсчёта и контроля за данными. Если вы не будете вводить данные в эти поля в файле, то программа будет спрашивать вас в консоли об этих данных. Если вы откажитесь ответить и там и там, то будет введено значение None и действие будет провалено (будто бы вы сорвались и счётчик дней сбросится, если это привычка; или возьмутся старые данные, если это показатели)

##### Содержание файла:
+ 1 секция - Дата, название
+ 2 секция - Контроль плохих привычек (курение в данном случае), за провал принимаются символы "-", а также слова "no", "нет"
+ 3 секция - Контроль хороших привычек (хорошие поступки в данном случае)
+ 4 секция - Контроль развития (новые знания и навыки в данном случае)
+ 5 секция - Контроль веса\показателей (можно добавить спортивные показатели)
+ 6 секция - Диета с учётом веса, показателей, качелей (разгрузочные дни, праздники, поблажки и т.д.)
+ 7 секция - Расписание на день
+ 8 секция - Прошло дней с начала использования

___

> Stack: Python (3)

> November 2019 (completed)

