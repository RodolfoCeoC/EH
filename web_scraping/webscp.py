
def main():
    web = open('web.html','rb')
    start = '<li>'
    end = '</li>'
    for line in web.readlines():
        line = str(line)
        
        if start in line:
            if not '<a href' in line:
                x = line.find(start)
                x = x + len(start)
                y = line.find(end)
                print(line[x:y])


if __name__ == '__main__':
    main()