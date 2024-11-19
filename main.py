class Reverse:
    def __init__(self, s=""):
        self.s = s
        
    def reverse_string(self):
        return self.s[::-1]
        
word = input("Enter a word: ")
reverse_obj = Reverse(word)
print("Reversed string:", reverse_obj.reverse_string())
