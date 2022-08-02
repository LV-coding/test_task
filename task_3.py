import csv
from unittest import result


class Note():

    csv_file = 'task_3.csv'

    def __init__(self, film_name, text_note, rating ):
        self.film_name = film_name
        self.text_note = text_note
        if rating > 5:
            self.rating = 5
        elif rating < 1:
            self.rating = 1
        else: 
            self.rating = rating
        
    def __str__(self):
        return f'{self.film_name}-{self.rating}'

    @staticmethod
    def init_csv(csv_file=csv_file):
        text = ['Film_name', 'Text_note', 'Rating']
        try:
            with open(csv_file, 'xt', newline='') as record:
                csv_writer = csv.writer(record)
                csv_writer.writerow(text)       
        except FileExistsError:
            print('File exist!')

    def add_to_csv(self):
        for_add = [self.film_name, self.text_note, self.rating]
        with open(self.csv_file, 'at', newline='') as record:
            csv_writer = csv.writer(record)
            csv_writer.writerow(for_add)

    def remove_from_csv(self):
        with open(self.csv_file, 'rt', newline='') as input:
            csv_reader = csv.reader(input)
            Note.init_csv()
            result = [note for note in csv_reader if note[0] != self.film_name]
        with open(self.csv_file, 'wt', newline='') as output:    
            csv_writer = csv.writer(output)
            csv_writer.writerows(result)

    @classmethod
    def read_from_csv(cls):
        with open(cls.csv_file, 'rt', newline='') as record:
            csv_reader = csv.reader(record)
            result = [note for note in csv_reader if note[2] != 'Rating']
            return result

    @classmethod
    def print_all_notes(cls):
        with open(cls.csv_file, 'rt', newline='') as record:
            csv_reader = csv.reader(record)
            [print(note[0], note[1], note[2]) for note in csv_reader if note[2] != 'Rating']

    @classmethod
    def get_average_rating(cls):
        with open(cls.csv_file, 'rt', newline='') as record:
            csv_reader = csv.reader(record)
            result = [float(note[2]) for note in csv_reader if note[2] != 'Rating']
            return round(sum(result)/len(result),2) 

    @classmethod
    def max_rating(cls):
         with open(cls.csv_file, 'rt', newline='') as record:
            csv_reader = csv.reader(record)
            readed = [note for note in csv_reader if note[2] != 'Rating']   
            readed.sort(key=lambda x: x[2])
            return readed[-1][0]

    @classmethod
    def min_rating(cls):
         with open(cls.csv_file, 'rt', newline='') as record:
            csv_reader = csv.reader(record)
            readed = [note for note in csv_reader if note[2] != 'Rating']   
            readed.sort(key=lambda x: x[2])
            return readed[0][0]



Note.init_csv()

