class workout:
  def __init__(self):
    self.day = None
    self.type = None
    self.numberOfExercise = None
    self.maximumExercises = None
  
  #priority Functions
  
  
  #setters
  def setWorkoutDate(self,input):
    self.day = input
    print(f"The current workout date is {self.day}")
  def setWorkoutType(self,input):
    self.workoutType = input
    print(f"The workout type is {input}")
  def setNumberofExercise(self,input):
    self.numberOfExercise = input   
    if self.numberOfExercise > self.maximumExercises:
      print('Exercises Exceed Maximum')
      self.numberOfExercise = 0
    else:
      return
  #getters




class exercise:
  def __init__(self):
    # Predetermined before the exercise
    self.exerciseName = None
    self.setsToComplete = None
    self.repRange = None
    self.date = None
    # Work Done during the set
    self.setThenReps = tuple()
    self.setsCompleted,self.repsForSetCompleted = self.setThenReps
  
  def setSetsAndRep(self,set,reps):
    self.setThenReps = set,reps
  def setDate(self,value):
    self.date = value
class Routine:
  def __init__(self) :
    self.workout = workout()
    self.exercises = [exercise()]


