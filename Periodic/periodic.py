import tkinter as tk
from tkinter import messagebox
import random

element_dict = {
    "1": "H",
    "2": "He",
    "3": "Li",
    "4": "Be",
    "5": "B",
    "6": "C",
    "7": "N",
    "8": "O",
    "9": "F",
    "10": "Ne",
    "11": "Na",
    "12": "Mg",
    "13": "Al",
    "14": "Si",
    "15": "P",
    "16": "S",
    "17": "Cl",
    "18": "Ar",
    "19": "K",
    "20": "Ca",
    "21": "Sc",
    "22": "Ti",
    "23": "V",
    "24": "Cr",
    "25": "Mn",
    "26": "Fe",
    "27": "Co",
    "28": "Ni",
    "29": "Cu",
    "30": "Zn",
    "31": "Ga",
    "32": "Ge",
    "33": "As",
    "34": "Se",
    "35": "Br",
    "36": "Kr",
    "37": "Rb",
    "38": "Sr",
    "39": "Y",
    "40": "Zr",
    "41": "Nb",
    "42": "Mo",
    "43": "Tc",
    "44": "Ru",
    "45": "Rh",
    "46": "Pd",
    "47": "Ag",
    "48": "Cd",
    "49": "In",
    "50": "Sn",
    "51": "Sb",
    "52": "Te",
    "53": "I",
    "54": "Xe",
    "55": "Cs",
    "56": "Ba",
    "57": "La",
    "58": "Ce",
    "59": "Pr",
    "60": "Nd",
    "61": "Pm",
    "62": "Sm",
    "63": "Eu",
    "64": "Gd",
    "65": "Tb",
    "66": "Dy",
    "67": "Ho",
    "68": "Er",
    "69": "Tm",
    "70": "Yb",
    "71": "Lu",
    "72": "Hf",
    "73": "Ta",
    "74": "W",
    "75": "Re",
    "76": "Os",
    "77": "Ir",
    "78": "Pt",
    "79": "Au",
    "80": "Hg",
    "81": "Tl",
    "82": "Pb",
    "83": "Bi",
    "84": "Po",
    "85": "At",
    "86": "Rn",
    "87": "Fr",
    "88": "Ra",
    "89": "Ac",
    "90": "Th",
    "91": "Pa",
    "92": "U",
    "93": "Np",
    "94": "Pu",
    "95": "Am",
    "96": "Cm",
    "97": "Bk",
    "98": "Cf",
    "99": "Es",
    "100": "Fm",
    "101": "Md",
    "102": "No",
    "103": "Lr",
    "104": "Rf",
    "105": "Db",
    "106": "Sg",
    "107": "Bh",
    "108": "Hs",
    "109": "Mt",
    "110": "Ds",
    "111": "Rg",
    "112": "Cn",
    "113": "Nh",
    "114": "Fl",
    "115": "Mc",
    "116": "Lv",
    "117": "Ts",
    "118": "Og"
}

list_s_1 = [1]
list_s_2 = [3, 4]
list_s_3 = [11, 12]
list_s_4 = [19, 20]
list_s_5 = [37, 38]
list_s_6 = [55, 56]
list_s_7 = [87, 88]
list_p_2 = [5, 6, 7, 8, 9]
list_p_3 = [13, 14, 15, 16, 17]
list_p_4 = [31, 32, 33, 34, 35]
list_p_5 = [49, 50, 51, 52, 53]
list_p_6 = [81, 82, 83, 84, 85]
list_p_7 = [113, 114, 115, 116, 117]
list_noble_gases = [2, 10, 18, 36, 54, 86, 118]
list_actinides = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
list_lanthanides = [57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
list_d_4 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list_d_5 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
list_d_6 = [72, 73, 74, 75, 76, 77, 78, 79, 80]
list_d_7 = [104, 105, 106, 107, 108, 109, 110, 111, 112]

num_correct = 0
num_incorrect = 0

def check():
    global num_correct
    global num_incorrect
    global user_guess
    user_guess = txt_guess.get()
    if user_guess.isalpha() and user_guess != "":
        user_guess = user_guess
    else:
        messagebox.showinfo("Alert", "Please Input a Valid Symbol")
        return
    if element_dict[str(computer_guess)] == user_guess:
        messagebox.showinfo("Alert", "That's correct!")
        num_correct = num_correct + 1
        new()
    elif element_dict[str(computer_guess)] != user_guess:
        messagebox.showinfo("Alert", "That's incorrect!")
        num_incorrect = num_incorrect + 1
        if num_incorrect >= 2 and num_incorrect < 5:
            hint()
    txt_guess.delete(0, 5)
    if num_incorrect == 5:
        answer()
        messagebox.showinfo("Alert", "5 wrong answers! The Game is Over! Your Score:" + str(num_correct) + "/" + str(num_correct + num_incorrect))
        root.quit()

def new():
    global computer_guess
    computer_guess = random.randint(1, 118)
    lbl_number["text"] = computer_guess

def answer():
    global computer_guess
    msg = "Correct Answer:" + str(element_dict[str(computer_guess)])
    lbl_hint["text"] = msg

def hint():
    global num_incorrect
    global computer_guess
    global user_guess
    key1 = [key  for (key, value) in element_dict.items() if value == str(user_guess)]
    if num_incorrect == 2:
        if int(key1[0]) < computer_guess:
            msg = "Try an element with a larger atomic number"
            lbl_hint["text"] = msg
        elif int(key1) > computer_guess:
            msg = "Try an element with a smaller atomic number"
            lbl_hint["text"] = msg
    if num_incorrect == 3:
        if computer_guess in list_s_1:
            msg = "It's in the 1st period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_2:
            msg = "It's in the 2nd period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_3:
            msg = "It's in the 3rd period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_4:
            msg = "It's in the 4th period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_5:
            msg = "It's in the 5th period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_6:
            msg = "It's in the 6th period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_s_7:
            msg = "It's in the 7th period, s-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_2:
            msg = "It's in the 2nd period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_3:
            msg = "It's in the 3rd period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_4:
            msg = "It's in the 4th period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_5:
            msg = "It's in the 5th period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_6:
            msg = "It's in the 6th period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_p_7:
            msg = "It's in the 7th period, p-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_noble_gases:
            msg = "It's a noble gas"
            lbl_hint["text"] = msg
        elif computer_guess in list_lanthanides:
            msg = "It's in the lanthanide series"
            lbl_hint["text"] = msg
        elif computer_guess in list_actinides:
            msg = "It's in the actinide series"
            lbl_hint["text"] = msg
        elif computer_guess in list_d_4:
            msg = "It's in the 4th period, d-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_d_5:
            msg = "It's in the 5th period, d-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_d_6:
            msg = "It's in the 6th period, d-block"
            lbl_hint["text"] = msg
        elif computer_guess in list_d_7:
            msg = "It's in the 7th period, d-block"
            lbl_hint["text"] = msg
    if num_incorrect == 4:
        msg = "The First letter of the symbol is:" + str(element_dict[str(computer_guess)][0])
        lbl_hint["text"] = msg

   

root = tk.Tk()

lbl_title = tk.Label(root, text="Welcome to the Periodic Table Guessing Game!")
lbl_title.pack()
lbl_result = tk.Label(root, text="Good luck!")
lbl_result.pack()
lbl_number = tk.Label(root, text="")
lbl_number.pack()
lbl_hint = tk.Label(root, text="")
lbl_hint.pack()

btn_check = tk.Button(root, text="Submit", fg="green", command = check)
btn_check.pack(side="left")
btn_reset = tk.Button(root, text="New", fg="red", command = new)
btn_reset.pack(side="right")
btn_quit = tk.Button(root, text="Quit", fg = "purple", command = root.destroy)
btn_quit.pack(side="left")
btn_answer = tk.Button(root, text="Answer", fg="blue", command = answer)
btn_answer.pack(side="right")
txt_guess = tk.Entry(root, width=6)
txt_guess.pack()


root.mainloop()
