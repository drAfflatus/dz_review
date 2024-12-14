"""
Нужно реализовать класс Stack со следующими методами:
is_empty — проверка стека на пустоту. Метод возвращает True или False;
push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;
size — возвращает количество элементов в стеке.

Используя стек из задания 1, решите задачу на проверку сбалансированности скобок.
Сбалансированность скобок означает, что каждый открывающий символ имеет соответствующий ему
 закрывающий, и пары скобок правильно вложены друг в друга.

Пример сбалансированных последовательностей скобок:
(((([{}]))))
[([])((([[[]]])))]{()}
{{[()]}}

Несбалансированные последовательности:
}{}
{{[(])]}}
[[{())}]

Программа ожидает на вход строку со скобками. На выход сообщение: «Сбалансированно», если
строка корректная, и «Несбалансированно», если строка составлена неверно.

"""


class Stack():
    def __init__(self):
        self.body_stack = []
        self.dic_bracket = {")":"(","]":"[","}":"{"}

    def  is_empty(self):
        result = False
        if len(self.body_stack)==0:
            result = True
        return result

    def push(self,brc):
        self.body_stack.insert(0,brc)

    def pop(self):
        match len(self.body_stack):
            case 0:
                return None
            case 1:
                self.body_stack.pop(0)
                return None
            case _:
                self.body_stack.pop(0)
                return self.body_stack[0]


    def peek(self):
        if len(self.body_stack)>0:
            return self.body_stack[0]
        else:
            return None

    def size(self):
        return len(self.body_stack)


if __name__ == '__main__':


    while True:
        bracket_user = str(input("Введите строку для проверки баланса[enter - выход]:"))
        if bracket_user=="":
            break
        not_balanced = True
        st=Stack()
        for i in bracket_user:
            if i in st.dic_bracket.values():
                st.push(i)
            elif i in st.dic_bracket.keys():
                if st.size()>0 and st.dic_bracket.get(i)==st.peek():
                    st.pop()
                else:
                    not_balanced = False
                    break
            else:
                print(f"скобка '{i}' не очень похожа на скобку")

        if st.is_empty() and not_balanced:
            print(f'Строка {bracket_user} сбалансирована')
        else:
            print(f'Строка {bracket_user} не сбалансирована')



