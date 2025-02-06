def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        


#def NumberOfWords():
 #   with open('books/frankenstein.txt') as d:
 #       file_contents = d.read()
 #       words = file_contents.split()
 #       count = 0
  #      for word in words:
 #           count += 1
 #           print(count)
 #       return  count

def CharacterAppear():
    with open('books/frankenstein.txt') as d:
        file_contents = d.read()
        words = file_contents.lower()
        count2 = {}
        for char in words:
            if char in count2:
                count2[char] += 1
            else:
                count2[char] = 1
        
        raport = [{"character": char, "count": count} for char, count in count2.items()
                  if char.isalpha() == True]
        
        return print(raport)



main()
#NumberOfWords()
CharacterAppear()
