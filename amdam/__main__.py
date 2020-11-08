import tkinter as tk
from .controller import app
from multiprocessing import Process

import webbrowser


def start_server(port=8012):
    run_app = lambda : app.run(host="0.0.0.0", port=port)
    run_web = lambda : webbrowser.open_new_tab(f'http://localhost:{ port }/')
    p = Process( target=run_app )
    p.start()
    Process( target=run_web ).start()
    return p


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Amda-M | By Ablaze")
        self.master.protocol("WM_DELETE_WINDOW", self.exit_gui)
        self.master.columnconfigure(0, minsize=250)
        self.master.rowconfigure([0, 1], minsize=50)
        self.create_widgets()



    def create_widgets(self):
        self.label_status = tk.Label(
            bg="black",
            fg="white",
            text="Enter Port",
        ).grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.entry = tk.Entry()
        self.entry.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.entry.insert(0, 8012)

        self.get_port = lambda: int( self.entry.get() )


        self.start = tk.Button(
            text="Start",
            bg="Green",
            fg="white",
            command=self.start_server
        )
        self.start.grid(row=3, column=0, sticky="e")

        self.quit = tk.Button(
            text="Stop",
            bg="red",
            fg="white",
            command=self.quit_server
        )
        self.quit.grid(row=3, column=1, sticky="w")
        self.quit.config(state="disable")


    def start_server(self):
        self.server = start_server( self.get_port() )
        self.start.config(state="disable")
        self.quit.config(state="normal")

    def quit_server(self):
        self.server.terminate()
        self.start.config(state="normal")
        self.quit.config(state="disable")

    def exit_gui(self):
        self.quit_server()
        self.master.destroy()


root = tk.Tk()

gui = Application(master=root)
gui.mainloop()
