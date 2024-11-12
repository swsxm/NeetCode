class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i in tokens:
                if i in "-+*/":
                    val1 = tokens.pop()
                    val2 = tokens.pop()
                    if i == "-":
                        result = val2 - val1
                    if i == "+":
                        result = val1 + val2
                    if i == "*":
                        result = val1 * val2
                    if i == "/":
                        result = val1 * val2
                    tokens.append(result)
        return tokens[0]
