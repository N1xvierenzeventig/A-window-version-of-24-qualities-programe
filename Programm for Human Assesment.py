import time
import keyboard
from tkinter import *

def rgb(rgb):
    return "#%02x%02x%02x" % rgb

root = Tk()
root.title("Your assesment")
root.geometry("1200x500+600+200")
root.config(bg= rgb(((54,69,79))))



all_the_time = ("Do you have the quality as")
List = []
List_for_streak = [0]
def function_works(event):
    def leave():
        root.destroy()
    for i in List_for_streak:
        if i>2 and i<27:
            Name = Entry1.get()
            List.append(Name)
            print(List)
    def Entry_Delete():
        for i in List_for_streak:
            t = i
            List_for_streak.clear()
            t += 1
            List_for_streak.append(t)
        if t == 1:
            Label1.config(text="What's your age?")
        elif t == 2:
            Label1.config(text="What's your gender?")
            Label2.config(
                text="For the following question(not this one) you should give us percantage of how much do you think you have this quality in you.",
                bg=rgb((219, 226, 233)))
        elif t == 3:
            Label1.config(text= f"{all_the_time} appreciation of Beauty and Excellence?")
            Label2.config(text= "I recognize, emotionally experience, and appreciate the beauty around me and the skill of others.",bg= rgb((219,226,233)))
        elif t == 4:
            Label1.config(text = f"{all_the_time} Bravery?")
            Label2.config(text="I act on my convictions, and I face threats, challenges, difficulties, and pains, despite my doubts and fears.",bg=rgb((219, 226, 233)))
        elif t == 5:
            Label1.config(text = f"{all_the_time} Creativity?")
            Label2.config(text="I am creative, conceptualizing something useful, coming up with ideas that result in something worthwhile.",bg=rgb((219, 226, 233)))
        elif t == 6:
            Label1.config(text = f"{all_the_time} Curiosity?")
            Label2.config(text="I seek out situations where I gain new experiences without getting in my own or other people’s way.",
                          bg=rgb((219, 226, 233)))
        elif t == 7:
            Label1.config(text=f"{all_the_time} Fairness?")
            Label2.config(text="I treat everyone equally and fairly, and give everyone the same chance applying the same rules to everyone.",
                          bg=rgb((219, 226, 233)))
        elif t == 8:
            Label1.config(text = f"{all_the_time} Forgiveness?")
            Label2.config(text="I forgive others when they upset me and/or when they behave badly towards me, and I use that information in my future relations with them.",
                          bg=rgb((219, 226, 233)))
        elif t == 9:
            Label1.config(text = f"{all_the_time} Gratitude?")
            Label2.config(text="I am grateful for many things and I express that thankfulness to others.",
                          bg=rgb((219, 226, 233)))
        elif t == 10:
            Label1.config(text = f"{all_the_time} Honesty?")
            Label2.config(text="I am grateful for many things and I express that thankfulness to others.",
                          bg=rgb((219, 226, 233)))
        elif t == 11:
            Label1.config(text = f"{all_the_time} Hope?")
            Label2.config(text="I am realistic and also full of optimism about the future, believing in my actions and feeling confident things will turn out well.",
                          bg=rgb((219, 226, 233)))
        elif t == 12:
            Label1.config(text = f"{all_the_time} Humility?")
            Label2.config(text="I see my strengths and talents but I am humble, not seeking to be the center of attention or to receive recognition.",
                          bg=rgb((219, 226, 233)))
        elif t == 13:
            Label1.config(text = f"{all_the_time} Humor?")
            Label2.config(text="I approach life playfully, making others laugh, and finding humor in difficult and stressful times.",
                          bg=rgb((219, 226, 233)))
        elif t == 14:
            Label1.config(text=f"{all_the_time} Judgement?")
            Label2.config(text="I weigh all aspects objectively in making decisions, including arguments that are in conflict with my convictions.",
                          bg=rgb((219, 226, 233)))
        elif t == 15:
            Label1.config(text = f"{all_the_time} Kindness?")
            Label2.config(text="I am helpful and empathic and regularly do nice favors for others without expecting anything in return.",
                          bg=rgb((219, 226, 233)))
        elif t == 16:
            Label1.config(text = f"{all_the_time} Leadership?")
            Label2.config(text="I take charge and guide groups to meaningful goals, and ensure good relations among group members.",
                          bg=rgb((219, 226, 233)))
        elif t == 17:
            Label1.config(text = f"{all_the_time} Love?")
            Label2.config(text="I experience close, loving relationships that are characterized by giving and receiving love, warmth, and caring.",
                          bg=rgb((219, 226, 233)))
        elif t == 18:
            Label1.config(text = f"{all_the_time} Love of Learning?")
            Label2.config(text="I am motivated to acquire new levels of knowledge, or deepen my existing knowledge or skills in a significant way.",
                          bg=rgb((219, 226, 233)))
        elif t == 19:
            Label1.config(text = f"{all_the_time} Perseverance?")
            Label2.config(text="I persist toward my goals despite obstacles, discouragements, or disappointments.",
                          bg=rgb((219, 226, 233)))
        elif t == 20:
            Label1.config(text = f"{all_the_time} Perspectivity?")
            Label2.config(text="I give advice to others by considering different (and relevant) perspectives and using my own experiences and knowledge to clarify the big picture.",
                          bg=rgb((219, 226, 233)))
        elif t == 21:
            Label1.config(text = f"{all_the_time} Prudence?")
            Label2.config(text="I act carefully and cautiously, looking to avoid unnecessary risks and planning with the future in mind.",
                          bg=rgb((219, 226, 233)))
        elif t == 22:
            Label1.config(text = f"{all_the_time} Self-Regulation?")
            Label2.config(text="I manage my feelings and actions and am disciplined and self-controlled.",
                          bg=rgb((219, 226, 233)))
        elif t == 23:
            Label1.config(text = f"{all_the_time} Social Intelligence?")
            Label2.config(text="I am aware of and understand my feelings and thoughts, as well as the feelings of those around me.",
                          bg=rgb((219, 226, 233)))
        elif t == 24:
            Label1.config(text = f"{all_the_time} Spirituality?")
            Label2.config(text="I feel spiritual and believe in a sense of purpose or meaning in my life; and I see my place in the grand scheme of the universe and find meaning in everyday life.",
                          bg=rgb((219, 226, 233)))
        elif t == 25:
            Label1.config(text = f"{all_the_time} Teamwork?")
            Label2.config(text="I am a helpful and contributing group and team member, and feel responsible for helping the team reach its goals.",
                          bg=rgb((219, 226, 233)))
        elif t == 26:
            Label1.config(text = f"{all_the_time} Zest?")
            Label2.config(text="I feel vital and full of energy, I approach life feeling activated and enthusiastic.",
                          bg=rgb((219, 226, 233)))
        elif t == 27:
            Label2.destroy()
            Label1.config(text = "Alright, you're almost there. What do you believe your score is?")
        elif t == 28:
            Added_Numbers = 0
            for i in List:
                i = int(i)
                Added_Numbers += i
            Predict = int(Entry1.get())
            Percentage = int((Added_Numbers/ 24))
            if Percentage > 60:
                Result = "Good"
            else:
                Result = "Bad"
            if Predict > Percentage:
                Number = "Lower"
            else:
                Number = "Higher"
            Label1.destroy()
            Button1.destroy()
            Entry1.destroy()

            Label3 = Label(root, text = f"You're here. Congratulations. Now I want to give you some desired information about you."
                                        f" You are {Percentage} perfect human. Your predict was that you are {Predict} % perfect human. As you can see this number is {Number} than you predicted.", bg= rgb((219,226,233)))
            Label3.place(relx= 0.5, rely = 0.25, anchor= CENTER)
            Button2 = Button(root, text=("Press to leave"), bd=4, command=leave, bg= rgb((219,226,233)))
            Button2.place(relx=0.5, rely=0.5, anchor=CENTER)

        Entry1.delete(0, "end")





    Entry_Delete()




Label1 = Label(root, text = "What's your name?", font=("Areal",10), bg= rgb((218,218,218)))
Label1.place(relx=0.5,rely=0.12, anchor=CENTER)
Label2 = Label(root, text = "", font= ("Areal", 10), bg= rgb((54,69,79)))
Label2.place(relx = 0.5, rely = 0.5, anchor=CENTER)
Entry1 = Entry(root,width=30, font = ("Helvetica",10), bd=15)
Entry1.place(relx= 0.5, rely= 0.2, anchor=CENTER)
Button1 = Button(root, text=(f"When ready, press the button"),bd=5, bg =rgb((218,218,218)))
Button1.place(relx = 0.5, rely = 0.30, anchor=CENTER)
root.bind("<Return>", function_works)
root.bind("<Button-1>", function_works)


root.mainloop()


