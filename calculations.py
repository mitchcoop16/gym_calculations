
class Calc():

    def bmi_calc(weight, height, metric):
        try:
            if metric == 1:
                return int(703 * (weight/height**2))
            elif metric ==2:
                return int(weight/(height/100)**2)

        except ZeroDivisionError:
            print("Can't divide by zero")


    def bmr_calc(gender, weight, height, age, metric):
        if gender == 1:
            if metric ==1:
                return int(66 + (6.2 * weight) + (12.7 * height) - (6.8 * age))
            elif metric ==2:
                return int(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))

        elif gender == 2:
            if metric == 1:
                return int(655 + (4.3 * weight) + (4.7 * height) - (4.7 * age))
            elif metric ==2:
                return int(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))
        else:
            print("Invalid gender")


    def cal_intake(bmr, level):
        if level == 1:
            lev = 1.2
        elif level == 2:
            lev = 1.375
        elif level == 3:
            lev = 1.55
        elif level == 4:
            lev = 1.725
        elif level == 5:
            lev = 1.9
        else:
            lev = 1.2
        cal = int(bmr * lev)
        return cal

    def macros(cals):
        protein_percent = 0.35
        carb_percent = 0.35
        fat_percent = 0.30
        
        protein_intake = int((cals * protein_percent) / 4)
        carb_intake = int((cals * carb_percent) / 4)
        fat_intake = int((cals * fat_percent) / 9)

        return protein_intake, carb_intake, fat_intake