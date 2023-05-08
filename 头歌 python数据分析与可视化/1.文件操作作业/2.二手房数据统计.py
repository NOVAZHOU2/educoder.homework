import numpy as np

with open ('step3/2012-19sport.csv',encoding ='utf-8')as file:
    file.readline()
    data = file.read().strip().replace('\n',',').split(',')

def sport_thing():
    year=input()
    set1=set()
    sum=0;
    yearly_data = np.array(data).reshape(755,7)
    for x,i in enumerate(yearly_data[:,6]):
        if i== year:
            set1.add(yearly_data[x,5])
    else:
        list1=sorted(list(set1))
        for num,sp in enumerate(list1):
            print(f'{num+1}: {sp}')
        cho = int(input())-1
        sport_name = list1[cho]
    for x,i in enumerate(yearly_data[:,6]):
        if i==year and yearly_data[x,5]== sport_name:
            sum = sum +float(yearly_data[x,2].replace('$','').replace('M',''))
            for item in yearly_data[x]:
                if item !=year:
                    print(item.replace('#',''),end=' ')
                    print('|',end=' ')
                if item==year:
                    print(item)
    else:
        print(f'TOTAL: ${sum:.2f} M')

def print_thing():
    n=int(input())
    yearly_data = np.array(data).reshape(755,7)
    number=0;
    for i in range(755):
        if yearly_data[i,6] == what:
            for num,j in enumerate(yearly_data[i]):
                if j!= what:
                    print(j.replace('#',''),end =' ')
                    print('|',end =' ')
                elif j == what and num!=len(yearly_data):
                    print(j)
                    number =number+1
        if number>=n:
            break;

if __name__ == '__main__':
    what = input()
    if what.lower() == 'sport':
        sport_thing()
    elif 2012 <= int(what) <=2019:
        print_thing()
    else:
        print("Wrong Input")
