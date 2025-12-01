# with open('pi.txt') as a:
#     for b in a:
#         print(b.strip())
# with open('pi.txt', 'w') as a:
#     a.write('hello')
# with open('pi.txt', 'a') as b:
#     b.write('\nhello')
# with open('pi.txt','w+') as b:
#     b.write('\nhello')
#     b.seek(0)
#     print(b.read())
# with open('pi.txt', 'r+') as a:
#     a.write('hello')
#     a.seek(0)
#     print(a.read())
# data = []
# with open('pi.txt','r+') as f:
#     for i in f:
#         d = i.strip().split('_'))
#         name = d[0]
#         ball = d[1]
