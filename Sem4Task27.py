mas = ''' She sells sea shells on the sea shore . The shells that she sells are sea shells I'm sure . So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower().replace(" . "," ").split()
mas = set(mas)
print(mas)
print (len(mas))