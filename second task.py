def inputParagraph():
    print ("Hi there! write a paragraph.")
    global paragraph
    paragraph=input().split()
    numberOfWords=len(paragraph)
    wordFrequency=[paragraph.count(p)for p in paragraph]
    print(numberOfWords)
inputParagraph()
