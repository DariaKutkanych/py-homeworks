# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    pass


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
