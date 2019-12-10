class Class:
    def __init__(self, saturday, sunday, monday, tuesday, wednesday, thursday):
        self.Saturday = saturday
        self.Sunday = sunday
        self.Monday = monday
        self.Tuesday = tuesday
        self.Wednsday = wednesday
        self.Thursday = thursday
from  Classes import *



c202 = Class([Quran, Math, Maaref_takmily, Math, Computer, Computer],
             [English, English, Physic, Work, Physic, About_science],
             [Math, Laboratory, Math, Chemistry, Math, Work],
             [Sport, Sport, Literature, Literature, Arabic, History],
             [Writing, Biology, Advice, Art, Research_Class, Research_Class],
             [Education, Scaning, Social_Studies, Scaning, '-', '-']

                  )


Classes = {'202': c202}
print(Classes['202'])
