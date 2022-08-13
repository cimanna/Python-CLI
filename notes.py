from peewee import *

db = PostgresqlDatabase('notes', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Note(BaseModel):
    title = CharField()
    topic = CharField()
    content = TextField()

    def __str__(self):
        return self.title

db.create_tables([Note])

def create_note():
    title = input('Title: ')
    topic = input('Topic: ')
    content = input('Content: ')
    
    new_note = Note(title=title, topic=topic, content=content)
    new_note.save()

def find_note():
    topic_input = input('Topic: ')
    note = Note.get(Note.topic == topic_input)
    print(note)

def update_note():
    topic_input = input('Topic: ')
    note = Note.get(Note.topic == topic_input)
    note.title = input('Title: ')
    note.topic = input('Topic: ')
    note.content = input('Content: ')
    note.save()
    print(note)

def delete_note():
    topic_input = input('Topic: ')
    note = Note.get(Note.topic == topic_input)
    note.delete_instance()

