
def main():
    words = ['апельсин', 'стол', 'астрология', 'мелодия', 'кот', 'ананас', 'арбузы', 'яблоко', 'собака']
    removed_count = 0  # Счетчик удаленных букв 'а'
    modified_words = []  # Новый список для хранения измененных слов

    for word in words:
        remove_count = word.count('а')
        removed_count += remove_count
        modified_word = word.replace('а', '')
        modified_words.append(modified_word)

    print(f'Измененные слова: {modified_words}')
    print(f'Количество удаленных букв "а": {removed_count}')

if __name__ == '__main__':
    main()