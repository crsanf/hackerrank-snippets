def merge_the_tools(string, k):
    sub_divisions = len(string) // k
    split_strings = sub_string(string,k,sub_divisions)
    
    for i in split_strings:
        analyze_string(i)
    
def sub_string(string,k,divider):
    split_strings = []
    for i in range(0,divider):
        start = i * k
        end = start + k
        split_strings.append(string[start:end])
        
    return split_strings

def analyze_string(sub_string):
    string_list = []
    for letter in sub_string:
        if letter not in string_list:
            string_list.append(letter)
            
    compiled_string = "".join(string_list)
    
    print(compiled_string)
    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)