#12. Write a function called parse_ranges, which accepts a string containing ranges of
#numbers and returns an iterable of those numbers.
#Ex: >>> parse_ranges('1-2,4-4,8-13')

def parse_ranges(ranges_string):
    ranges = ranges_string.split(",")
    final = []

    for i in ranges:
        if i.find("->") != -1:
            ignore = i.split("->")[0]
            final.append(int(ignore))
        elif i.find("-") == -1:
            
            final.append(int(i))
        else:
            start, stop = i.split("-")
            for x in range(int(start), int(stop)+1):
               
                final.append(x)
    return final



def main():
    print(parse_ranges('1-2,4-4,8-13'))
   


if __name__ == '__main__':
    main()