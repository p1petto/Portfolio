# Технологии веб-разработки: программирование на стороне клиента

## Конструктор визиток / business card

С помощью конструктера можно составить классическую визитку


## Список задач / list of task

Карточка задачи должна отображаться либо по клику на кнопку "Создать", либо по клику на кнопку "Редактировать" в списке.

Карточка задачи размещается фиксировано (даже при прокрутке большого списка задач остается на своем месте).

При выполнении задания необходимо показать умение работы с DOM-структурой.


## Сапёр / MineSweeper

### Правила

Плоское игровое поле разделено на смежные ячейки, некоторые из которых «заминированы»; количество «заминированных» ячеек известно. Целью игры является открытие всех ячеек, не содержащих мины.

Игрок открывает ячейки, стараясь не открыть ячейку с миной. Открыв ячейку с миной, он проигрывает. Мины расставляются после первого хода. Если под открытой ячейкой мины нет, то в ней появляется число, показывающее, сколько ячеек, соседствующих с только что открытой, «заминировано»; используя эти числа, игрок пытается рассчитать расположение мин. Если под соседними ячейками тоже нет мин, то открывается некоторая «не заминированная» область до ячеек, в которых есть цифры. «Заминированные» ячейки игрок может пометить, чтобы случайно не открыть их. Открыв все «не заминированные» ячейки, игрок выигрывает.

### Механика

Поле размером 12х12 ячеек. Клик левой кнопкой мыши открывает ячейку. Клик правой кнопкой мыши помечает как потенциально заминированную.

Предусмотреть возможность игры без мыши с использованием только клавиатуры: Стрелки перемещают курсор на нужную ячейку (ячейку в этом случае нужно подсветить). нажатие на кнопку Пробел или Enter открывает ячейку. Кнопка Ctrl+Пробел или Ctrl-Enter помечает как потенциально заминированную.


## Паззл / puzzle

Картинка разбита на части. Игрок должен вернуть первоначальный вид.