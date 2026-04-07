class Hodina10:
    def prvni(self):
        
        import tkinter as tk
        cv = tk.Canvas(height=500, width=500)
        cv.pack()

        # cv.create_rectangle(100, 200, 300, 250, fill="brown", outline="brown")
        # cv.create_rectangle(125, 150, 275, 200, fill="brown", outline="brown")
        # cv.create_rectangle(150, 100, 250, 150, fill="brown", outline="brown")
        
        # cv.create_rectangle(2,2, 200, 50, fill="red")
        # cv.create_rectangle(2,2+50, 200, 50+50, fill="white")
        # cv.create_rectangle(2,2+100, 200, 50+100, fill="blue")

        cv.create_rectangle(2,2, 400, 200)
        cv.create_rectangle(100, 200, 150, 0, fill="blue")
        cv.create_rectangle(400, 100, 2, 130, fill="blue")
        tk.mainloop()

program = Hodina10()

program.prvni()