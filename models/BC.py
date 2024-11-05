class BrolitCompressor:
    def __init__(self, expression):
        pass
        self.expression = expression
    
    def compress(self):
        result = []
        i = 0
        while i < len(self.expression):
            found = False
            max_length = 0
            start_index = -1
            
            for j in range(i):
                length = 1
                while i + length <= len(self.expression) and self.expression[j:j + length] == self.expression[i:i + length]:
                    if length > max_length:
                        max_length = length
                        start_index = j
                    length += 1
            
            if max_length > 1:  
                result.append((start_index, start_index + max_length - 1))
                i += max_length
                found = True
            else:
                result.append(self.expression[i])
                i += 1
        
        return result
