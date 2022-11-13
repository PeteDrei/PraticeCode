#Dragon Ball Super based Topic

class MartialArtsTournament:
    
     def __init__(self, name, race, transformation):
        self.name = name
        self.race = race 
        self.transformation = transformation
        
     def info(status):
        print('\nName: ', status.name)
        print('Race: ', status.race)
        print('Transformation: ', status.transformation)
        
        
     def superskill_1(skill_1):
        print(skill_1.name + " Specialty: Uses Super Kamehameha to defeat's enemy!")
        
     def superskill_2(skill_2):
        print(skill_2.name + " Specialty: Uses Death Ball to vaporize enemy!")

     def superskill_3(skill_3):
      print(skill_3.name + " Specialty: Uses Special Beam Cannon to pierce enemy!")

     def superskill_4(skill_4):
      print(skill_4.name + " Specialty: Uses Final Explosion to disintegrate enemy!") 

     def superskill_5(skill_5):
      print(skill_5.name + " Specialty: Uses Finger Blitz Barrage to mow down an enemy!\n") 

        
    
being_1 = MartialArtsTournament("Goku", "a Saiyajin", "Ultra Instict")
being_1.info()
being_1.superskill_1()
    
being_2 = MartialArtsTournament("Frieza", "a Frost Demon", "Golden Frieza")
being_2.info()
being_2.superskill_2()

being_3 = MartialArtsTournament("Piccolo", "a Namekian", "Orange Piccolo")
being_3.info()
being_3.superskill_3()

being_4 = MartialArtsTournament("Vegeta", "a Saiyajin", "Super Saiyan God Super Saiyan Blue Evolution")
being_4.info()
being_4.superskill_4()

being_5 = MartialArtsTournament("Granolah", "a Cerealian", "Full Power")
being_5.info()
being_5.superskill_5()
