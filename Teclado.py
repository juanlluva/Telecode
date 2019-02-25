word_number = int(input())
n = 0
letters = ['A','D', 'F', 'G', 'V', 'X']
transcript = {32:'A', 16:'D', 8:'F', 4:'G', 2:'V', 1:'X'}
code = []
while True:
    try:
        col = int(input())
        row = n%6
        n+=1
        if col != 0:
            code.append(letters[row])
            code.append(transcript[col])
    except:
        break
code = ''.join(code)    
separated = [code[n:n+5] for n in range(0, len(code), 5)]
print(' '.join(separated))