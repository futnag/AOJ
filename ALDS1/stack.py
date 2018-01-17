

# data = input().split()

# # 配列によるスタックの実装
# # n : スタックのサイズ
# # S : スタック
# n = 20
# S = [0 for i in range(n)]

# def initialize():
#     global top
#     top = 0

# def isEmpty():
#     global top
#     return top == 0

# def isFull():
#     global top, n
#     return top > n-1

# def push(S, x):
#     global top
#     if isFull():
#         print('error: overflow')
#         raise
#     top += 1
#     S[top] = x

# def pop(S):
#     global top
#     if isEmpty():
#         print('error: underflow')
#         raise
#     top -= 1
#     return S[top+1]

# initialize()

# for e in data:

#     if e.isdigit():
#         push(S, int(e))
#     else:
#         a = pop(S)
#         b = pop(S)

#         if e == '+':
#             push(S, b + a)
#         elif e == '-':
#             push(S, b - a)
#         elif e == '*':
#             push(S, b * a)
#         else:
#             print('error: operand')
#     print(S)


# print(S[top])




# class Stack():
#     def __init__(self):
#         self.stack = [0 for _ in range(200)]
#         self.top = 0
 
#     def isEmpty(self):
#         return self.top == 0
 
#     def isFull(self):
#         return self.top >= len(self.stack) - 1
 
#     def push(self, x):
#         if self.isFull():
#             print "error"
#             return exit()
#         self.top += 1
#         self.stack[self.top] = x
 
#     def pop(self):
#         if self.isEmpty():
#             print "error"
#             return exit()
#         a = self.stack[self.top]
#         del self.stack[self.top]
#         self.top -= 1
#         return a
 
#     def lol(self):
#         return self.stack[self.top]
 
# def main():
#     st = Stack()
#     data = raw_input().split()
#     for i in data:
#         if i == '+':
#             b = int(st.pop())
#             a = int(st.pop())
#             st.push(a + b)
#         elif i == '-':
#             b = int(st.pop())
#             a = int(st.pop())
#             st.push(a - b)
#         elif i == '*':
#             b = int(st.pop())
#             a = int(st.pop())
#             st.push(a * b)
#         else:
#             st.push(i)
#     print st.lol()
 
# if __name__ == '__main__':
#     main()











# class MyStack:
#     def __init__(self, size):
#         self.stack = [0 for i in range(size)]
#         self.size = size
#         self.top = 0
 
#     def initialize(self):
#         self.top = 0
 
#     def push(self, elm):
#         self.top += 1
#         self.stack[self.top] = elm
#         return self.stack
 
#     def pop(self):
#         ret = self.stack[self.top]
#         self.stack[self.top] = 0
#         self.top -= 1
#         return ret
 
#     def is_empth(self):
#         if not self.is_full():
#             return True
#         return False
 
#     def is_full(self):
#         if self.size-1 is self.top:
#             return True
#         return False
 
 
# def main(expr):
#     stack = MyStack(1000)
#     for i, elm in enumerate(expr):
#         if expr[i] is '+':
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(a) + int(b))
#         elif expr[i] is '-':
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(b) - int(a))
#         elif expr[i] is '*':
#             a = stack.pop()
#             b = stack.pop()
#             stack.push(int(a) * int(b))
#         else:
#             stack.push(elm)
#     return stack.pop()
 
 
# if __name__ == '__main__':
#     expr = [str(s) for s in input().split()]
#     print(main(expr))






class My_Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0 for i in range(size)]
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top > self.size - 1

    def push(self, x):
        if self.isFull():
            print('error')
            raise
        else:
            self.top += 1
            self.stack[self.top] = x

    def pop(self):
        if self.isEmpty():
            print('error')
            raise
        else:
            a = self.stack[self.top]
            self.top -= 1
            return a


def main():
    data = input().split()
    st = My_Stack(len(data))

    for e in data:
        if e == '+':
            a = st.pop()
            b = st.pop()
            st.push(b + a)
        elif e == '-':
            a = st.pop()
            b = st.pop()
            st.push(b - a)
        elif e == '*':
            a = st.pop()
            b = st.pop()
            st.push(b * a)
        else:
            st.push(int(e))

    print(st.pop())


if __name__ == "__main__":
    main()























