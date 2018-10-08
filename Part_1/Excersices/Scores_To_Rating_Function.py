def Scores_Rating(a, b, c, d, e):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    e = float(e)
    maximum = MAX(a, b, c, d, e)
    minimum = MIN(a, b, c, d, e)
    average = (sum(a, b, c, d, e) - minimum - maximum)/3
    rating = "This is the rate {}" .format(str(average))
    return(rating)
