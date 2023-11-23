def print_book_info(title, author=None, year=None):
    #  Write your code here
    if author is not None and year is not None:
        print("\"{0}\" was written by {1} in {2}".format(title, author, year))
    elif author is None and year is not None:
        print("\"{0}\" was written in {1}".format(title, year))
    elif author is not None and year is None:
        print("\"{0}\" was written by {1}".format(title, author))
    else:
        print("\"{0}\"".format(title))


