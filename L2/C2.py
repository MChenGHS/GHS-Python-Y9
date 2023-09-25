author = input("What is the name of the author? ")
year = input("On which year was it published? ")
title = input("What is the name of this book? ")
print("What is the book's genre?")
genre = input("F for fictional, N for non-fictional ")

author_3 = author[:3]
title_3 = title[:3]

print("The book's ID is")
print(author_3+year+title_3+genre)