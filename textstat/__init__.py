from textstat.textstat import textstat


__version__ = (0, 5, 0)


for attribute in dir(textstat):
    if callable(getattr(textstat, attribute)):
        if not attribute.startswith("_"):
            globals()[attribute] = getattr(textstat, attribute)
