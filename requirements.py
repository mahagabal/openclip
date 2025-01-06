b=[i for i in open('requirements.txt').readlines()];b2=b[:]
if b[0].strip()=='tqdm':  b2[0]='requests\n';print('putting req')
else: b2[0]='tqdm\n';print('putting tq')
a=open('requirements.txt','w');a.writelines(b2);a.close()
