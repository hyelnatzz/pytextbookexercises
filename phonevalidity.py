phone = '120-447-5920'

phone = phone.split('-')
if len(phone) in (3,4):
    if len(phone) == 3:
        len_lst = [3,3,4]
        pos = 0
        for i in phone:
            if i.isnumeric():
                count = 0
                for j in i:
                    count += 1
                if count == len_lst[pos]:
                    pos += 1
                    continue
                else:
                    print('Invalid')
                    break
            else:
                print('Invalid')
                break
        else:
            print('Valid')
    else:
        len_lst = [1,3, 3, 4]
        pos = 0
        for i in phone:
            if i.isnumeric():
                count = 0
                for j in i:
                    count += 1
                if count == len_lst[pos]:
                    pos += 1
                    continue
                else:
                    print('Invalid')
                    break
            else:
                print('Invalid')
                break
        else:
            print('Valid')
else:
    print('Invalid')

