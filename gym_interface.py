from tkinter import *
from tkinter_creation import Tkinter_creation as tc
from calculations import Calc as calc

class Gym_Frames():
    
    def __init__(self, master):
        self.master = master
        
        self.new_frame = Frame(master)
        self.new_frame.grid(column=0, row=0, sticky='nswe')

        self.bmr_button = tc.create_button(self.new_frame, "Calculate!", self.create_bmr_frame, 0, 0)
  
        self.gender = IntVar() # 1 = male, 2 = female
        self.gender.set(1)
        self.activity_level = IntVar()
        self.metric = IntVar() # 1 = lbs / inches, 2 = kg / cm
        self.metric.set(1)
        self.weight = IntVar()
        self.height = IntVar()
        self.age = IntVar()
        self.active_level = [1,2,3,4,5]

    def calculate(self):
        self.reset_frame(self.new_frame)
        gender = self.gender.get()
        metric = self.metric.get()
        weight = self.weight.get()
        height = self.height.get()
        age = self.age.get()
        activity_level = self.activity_level.get()

        tc.create_label(self.new_frame, "BMI: {}".format(calc.bmi_calc(weight, height, metric)), 8, 0)
        tc.create_label(self.new_frame, "BMR: {}".format(calc.bmr_calc(gender, weight, height, age, metric)), 9, 0)
        tc.create_label(self.new_frame, "Calorie Intake: {}".format(calc.cal_intake((calc.bmr_calc(gender, weight, height, age, metric)), activity_level)), 10, 0)
        tc.create_label(self.new_frame, "Protien Intake: {}".format(calc.macros(calc.cal_intake((calc.bmr_calc(gender, weight, height, age, metric)), activity_level))[0]), 8, 1)
        tc.create_label(self.new_frame, "Carbs Intake: {}".format(calc.macros(calc.cal_intake((calc.bmr_calc(gender, weight, height, age, metric)), activity_level))[1]), 9, 1)
        tc.create_label(self.new_frame, "Fat Intake: {}".format(calc.macros(calc.cal_intake((calc.bmr_calc(gender, weight, height, age, metric)), activity_level))[2]), 10, 1)

    def create_bmr_frame(self):
        self.new_frame = Frame(self.master)
        self.new_frame.grid(column=0, row=1, sticky='w', padx=5, pady=5)
        tc.create_label(self.new_frame, "Switch between metrics", 1, 0)
        tc.create_radio_button(self.new_frame, "US (lbs / in)", self.metric, 1, 1, 1)
        tc.create_radio_button(self.new_frame, "SI (kg / cm)", self.metric, 2, 1, 2)
        tc.create_label(self.new_frame, "Select your gender", 2, 0)
        tc.create_radio_button(self.new_frame, "Male", self.gender, 1, 2, 1)
        tc.create_radio_button(self.new_frame, "Female", self.gender, 2, 2, 2)
        tc.create_entry_label(self.new_frame, "Weight", self.weight, 3, 1)
        tc.create_entry_label(self.new_frame, "Height", self.height, 4, 1)
        tc.create_entry_label(self.new_frame, "Age", self.age, 5, 1)
        tc.create_label(self.new_frame, "How active are you", 6, 0)
        tc.create_combo_box(self.new_frame, 16, self.activity_level, 6, 1, self.active_level)
        tc.create_button(self.new_frame, "Compute", self.calculate, 7, 0)

    def reset_frame(self, window):
        try:
            for child in window.winfo_children():
                if child != self.new_frame :
                    child.destroy()
        except:
            pass
root = Tk()
root.resizable(width=False, height=False)
gym = Gym_Frames(root)
root.mainloop()