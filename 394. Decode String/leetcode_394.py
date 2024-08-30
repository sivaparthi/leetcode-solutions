class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i == ']':
                chars = []
                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                string = "".join(chars[::-1])
                stack.pop()
                number = ""
                while stack and stack[-1].isdigit():
                    number += (stack.pop())
                stack.append(int(number[::-1]) * string)
            else:
                stack.append(i)
        print(stack)
        return "".join(stack)