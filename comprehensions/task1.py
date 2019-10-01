# Write a function using list comprehensions that takes a list of strings
# and removes those that contain 4 characters or less


def remove_shorts(strings: list) -> list:
    # write code here
    pass


assert remove_shorts(['telegram', 'sport', 'call', 'football', 'jet']) \
       == ['telegram', 'sport', 'football']
assert remove_shorts(['zombie', 'vision', 'cat', 'ring', 'telescope']) \
       == ['zombie', 'vision', 'telescope']
