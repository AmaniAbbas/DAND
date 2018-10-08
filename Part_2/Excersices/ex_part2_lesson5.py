'''
Quiz: The continue_crawl Function
continue_crawlshould return True or False following these rules:

if the most recent article in the search_history is the target article the
search should stop and the function should return False
If the list is more than 25 urls long, the function should return False
If the list has a cycle in it, the function should return False
otherwise the search should continue and the function should return True.
'''

# TODO: Implement the continue_crawl function described above
def continue_crawl(search_history, target_url):
    if search_history[-1] == target_url:
        print('We have reached our target')
        return False
    elif len(search_history) > 25:
        print('Our list cotains more than 25 urls')
        return False
    elif search_history[-1] in search_history[:-1]:
        print('The list has a cycle')
        return False
    else:
        return True


'''
Quiz: Add a Link to the Article Chain
Write a line of code that will add the first_link to the end of the list
article_chain. This line should come after the comment, "add the first link to
article chain".
'''
def web_crawl():
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)


'''
Quiz: Just Wait a Moment!
Work out the final step in the while loop - how to make Python wait for two
seconds. You might need to do some research to find a relevant Python package
and/or command to use. Add an import statement to the top part if needed, and
then a line of code at the bottom of the indented block.
'''
def web_crawl():
    from time import sleep
    while continue_crawl(article_chain, target_url):
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        article_chain.append(first_link)
        # delay for about two seconds
        # TODO: YOUR CODE HERE!
        sleep(2)
