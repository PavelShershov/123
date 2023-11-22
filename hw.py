data = {1: (2, 3), 2: (4, 5), 3: (6, 7), 4: (6, 7), 6: 'mdb'}
current_data_index = 1
phrases = ('Какую базу данных выбрать?', 'Данные структурированы?', 'Данных много',
           'Используется стек mean', 'нагрузка смешанная', 'Используются бессерверные вычисления','mdb')






is_running = False
while is_running:
    
    print(phrases[current_data_index])
    if isinstance(data[current_data_index], str):
        
        break
    user_input = input()
    if user_input == 'y':
        current_data_index = data[current_data_index][0]
    elif user_input == 'n':
        current_data_index = data[current_data_index][1]
        print(current_data_index)
