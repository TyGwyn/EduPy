def same_by(transformation, values):
   if list(filter(transformation, values)) == []:
       return True
   else:
       return False
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
