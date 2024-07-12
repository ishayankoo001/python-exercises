

def es53(ftesto):
    with open(ftesto) as f: text=f.read()
    text = [[int(s) for s in x.split()] for x in text.replace("\n"," ").split(":")]
    dict = {}
    for i,val in enumerate(text):
        if i == len(text)-2:
            dict[val[0]] = text[i + 1]
            return dict
        dict[val[0]] = text[i+1][0:-1:]
        text[i+1] = [text[i+1][-1]]
