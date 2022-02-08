import csv
import time
import json


def read(path):
    data = []
    with open(path, 'r') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            if i > 3:
                data.append(row[0].replace(')', ''))
            i += 1
    return data


def write(path, data):
    with open(path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow([f'Total:{len(data)}'])
        writer.writerow(['Name', 'RegNo'])
        writer.writerows(data)


def clean(data):
    data_cleaned = []
    for datum in data:
        for i in range(len(config['settings']['delimiters']['find'])):
            if config['settings']['delimiters']['find'][i] in datum:
                data_cleaned.append(datum.split(config['settings']['delimiters']['split'][i]))
                break
        else:
            data_cleaned.append([datum, 'NotAvailable'])

    data_cleaned.sort(key=lambda x: x[1])
    return data_cleaned


config = json.load(open('config.json', 'r'))

print(f'\t\t******Absentee {config["version"]}******')

opt = 1
menu = ''
opts_dict = {}
opt_index = 1

for opt_name in config['opts']:
    if config['opts'][opt_name]['inMenu'] is True:
        menu += f'[{opt_index}] {opt_name}\n'
        (opts_dict[str(opt_index)]) = config['opts'][opt_name]['optCode']
        opt_index += 1
menu += '[d] Description of an Option\n[0] Exit'


while opt != '0':
    print('\t\t\nMENU')
    print(menu)
    opt = input('Choose an Option(Default Option [1]): ')

    if opt in opts_dict:
        opt = opts_dict[opt]

    elif opt == '':
        opt = opts_dict['1']

    if opt == '0':
        print(f'Thank You For Using Absentee! :)')
        time.sleep(config['settings']['sleepTime']['exit'])

    elif opt.lower() == 'd':
        print('\t\t\nDescription')
        for opt_index, opt in enumerate(config['available_opts']):
            print(f'[{opt_index + 1}] {opt}')
        opt = config["available_opts"][int(input('Select an Option: ')) - 1]
        print(f'{opt}: {config["opts"][opt]["desc"]}')
        time.sleep(config['settings']['sleepTime']['desc'])

    elif opt in ['qv', 'cc', 'cco', 'qvcc']:
        file_path = input('Enter File Path/ Drag n Drop the File: ')
        file_path = file_path.replace('"', '')
        students = read(file_path)
        students_cleaned = clean(students)

        if opt in ['qv', 'qvcc']:
            reg_no = []
            no_reg_no = []
            for student in students_cleaned:
                if student[1][-3:].isdecimal():
                    reg_no.append(int(student[1][-3:]))
                else:
                    no_reg_no.append(student[0])
            absentees = []
            start = int(input('RegNo First(Last 3-digits): '))
            stop = int(input('RegNo Last(Last 3-digits): '))
            for num in range(start, stop + 1):
                if num not in reg_no:
                    if len(str(num)) == 1:
                        absentees.append(f'{students_cleaned[7][1][:-3]}00{num}')
                    elif len(str(num)) == 2:
                        absentees.append(f'{students_cleaned[7][1][:-3]}0{num}')
                    elif len(str(num)) == 3:
                        absentees.append(f'{students_cleaned[7][1][:-3]}{num}')

            print(f'\nNumber Of Absentees: {len(absentees)}')
            for absentees in absentees:
                print(absentees)
            print('\nRegNo for the following in Not Available')
            for name in no_reg_no:
                print(name)

            if opt == 'qvcc':
                new_file_path = file_path[:-4] + '-output.csv'
                write(new_file_path, students_cleaned)
                print(f'\nCompleted Writing The File, Find The Output Here: {new_file_path}')

        elif opt == 'cc':
            new_file_path = file_path[:-4] + '-output.csv'
            write(new_file_path, students_cleaned)
            print(f'\nCompleted Writing The File, Find The Output Here: {new_file_path}')

        elif opt == 'cco':
            write(file_path, students_cleaned)
            print(f'\nCompleted Over Writing The File, Find The Output Here: {file_path}')

        time.sleep(config['settings']['sleepTime']['menu'])

    else:
        print(f'\n{opt} is not a valid option')
