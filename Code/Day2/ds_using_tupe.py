zoo=('PITONE','more pitone','one more pitone')
print('Number of pitones in zoo is:',len(zoo))

new_zoo=('monkey','cammel',zoo)
print('Number of cages in the new zoo is',len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animal brought from old zoo are',new_zoo[2])
print('Last animal brought from old zoo is',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))
print(len(new_zoo[2]))