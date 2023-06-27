# // 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# // down from generation to generation. Imagine you're creating an application that
# // records these oral stories and translates them into different languages. The
# // stories vary by length, moral lessons, and the age group they are intended for.
# // Think about how you would model `Story`, `StoryTeller`, and `Translator`
# // objects, and how inheritance might come into play if there are different types of
# // stories or storytellers.
# // pseudo code
# // 1. record stories as objects(length,moral lessons,age-group)
# // 2.Create another class with more attributes for storyteller and translato
class AncestralStories:
   def __init__(self, length, moralLessons, ageGroup, title, language):
       self.length = length
       self.moralLessons = moralLessons
       self.ageGroup = ageGroup
       self.title = title
       self.language = language


   def translateStory(self, newLanguage):
       if self.language != newLanguage:
          self.language = newLanguage
          return self.language
       else:
           return self.language


   def addStoryToDatabase(self):
       database = []
       if self.title not in database:
           database.append(self.title)
           print(database)
       else:
           print("This story already exists in storage")


class StoryTeller(AncestralStories):
   def __init__(self, length, moralLessons, ageGroup, title, language, name):
       super().__init__(length, moralLessons, ageGroup, title, language)
       self.name = name
      
   def tellstory(self):
       print(f"This is a story called {self.title}, it teaches {self.ageGroup} about {self.moralLessons}")



story1 = AncestralStories("long", "courage", "children", "The Lion King", "English")
story1.addStoryToDatabase()
print(story1)
print(story1.translateStory("Kiswahili"))
story2 = AncestralStories("short", "hardwork", "teenagers", "Vuna Ulichopanda", "Kiswahili")
abunwasi = StoryTeller("long", "bravery", "Young Adults", "Adventures of Kinjikitile", "Mijikenda", "Abunwasi")
abunwasi.tellstory()

