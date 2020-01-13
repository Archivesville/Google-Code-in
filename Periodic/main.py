import tkinter
import random
import periodic_table


def check():
    global STREAK
    if entry.get() == periodic[rand_num]:
        lbl_status.config(text='Correct', fg='green')
    elif entry.get() == '':
        lbl_status.config(text='Enter element', fg='red')

    elif entry.get() not in periodic.values():
        lbl_status.config(text='Invalid element', fg='red')

    else:
        lbl_status.config(text='Incorrect', fg='red')
        STREAK += 1
        lbl_attempts.config(text='Attempts:' + str(STREAK))
        if STREAK <= 2:
            lbl_attempts.config(fg='green')
        elif STREAK == 3:
            lbl_attempts.config(fg='orange')
        else:
            lbl_attempts.config(fg='red')

        if STREAK == 5:
            quit()

        a_n = 0
        for i in periodic:
            if periodic[i] == entry.get():
                a_n = i
        if a_n < rand_num:
            lbl_hints.config(text='Correct element is to the right')
        else:
            lbl_hints.config(text='Correct element is to the left')


def new_num():
    global rand_num
    rand_num = random.randint(1, 112)
    lbl_num.config(text=str(rand_num))
    lbl_ans.config(text='')
    lbl_status.config(text='')
    lbl_status.config(text='')
    lbl_hints.config(text='')
    entry.delete(0, 'end')


def get_ans():
    lbl_ans.config(text=periodic[rand_num], fg='green')


def skip():
    lbl_ans.config(text='')
    lbl_status.config(text='')
    lbl_hints.config(text='')
    new_num()


master = tkinter.Tk()
master.title("Periodic table guessing game")
master.geometry("250x230")
master.resizable(0, 0)

periodic = periodic_table.get_periodic_table()
STREAK = 0
rand_num = random.randint(1, 112)

lbl_num = tkinter.Label(text=str(rand_num), font=('Comic Sans MS', 10))
lbl_num.grid(column=1, row=0)

lbl_el = tkinter.Label(text='Element:', font=('Comic Sans MS', 10))
lbl_el.grid(column=0, row=1)

entry = tkinter.Entry(width=5)
entry.grid(column=1, row=1, padx=5)

btn_submit = tkinter.Button(text='Submit', command=check, font=('Comic Sans MS', 10))
btn_submit.grid(column=2, row=1, padx=5)

btn_gen = tkinter.Button(text='Generate new', command=new_num, font=('Comic Sans MS', 10))
btn_gen.grid(column=0, row=4, pady=5, padx=1)

btn_ans = tkinter.Button(text='Answer', command=get_ans, font=('Comic Sans MS', 10))
btn_ans.grid(column=2, row=4)

lbl_ans = tkinter.Label(text='', font=('Comic Sans MS', 10))
lbl_ans.grid(column=2, row=0)

lbl_status = tkinter.Label(text='', font=('Comic Sans MS', 10))
lbl_status.grid(column=1, row=2, columnspan=2, sticky='NW')

lbl_hints = tkinter.Label(text='', font=('Comic Sans MS', 10))
lbl_hints.grid(column=0, row=3, columnspan=3)

lbl_attempts = tkinter.Label(text='Attempts:' + str(STREAK), fg='green', font=('Comic Sans MS', 10))
lbl_attempts.grid(column=1, row=4, padx=2)

btn_skip = tkinter.Button(text='Skip', command=skip, font=('Comic Sans MS', 10))
btn_skip.grid(column=1, row=6)

btn_quit = tkinter.Button(text='Exit', command=quit , font=('Comic Sans MS', 10))
btn_quit.grid(column=2, row=7)

master.mainloop()
