import textwrap

def wrap(string, max_width):
     wrapper = textwrap.TextWrapper(width=max_width)
     word_list = wrapper.wrap(text=string)
     word_list_join = '\n'.join(word_list)
     return word_list_join

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)