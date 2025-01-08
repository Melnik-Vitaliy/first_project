class BacteriaProducer:

    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria
        self.current_bacteria_count = 0
    def create(self):
        if self.current_bacteria_count < self.max_bacteria:
            self.current_bacteria_count += 1
            print(f'Добавлена одна бактерия. Бактерий в колонии: {
                  self.current_bacteria_count}')
        else:
            print(f'Нет места под новую бактерию')

    def delete(self):
        if self.current_bacteria_count == 0:
            print(f'В популяции нет бактерий, удалять нечего')
        else:
            self.current_bacteria_count -= 1
            print(f'Одна бактерия удалена. Бактерий в колонии: {
                  self.current_bacteria_count}')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.delete()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.create()
bacteria_producer.delete()
