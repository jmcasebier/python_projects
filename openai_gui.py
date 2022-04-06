# imports
import openai
import tkinter as tk

# create the window
window = tk.Tk()
# set window title
window.title("OpenAI")
# set window size
window.geometry("750x750")
#window.resizable(width=False, height=False)


def get_completion():
    # get completion
    promptInput = prompt_entry.get("1.0", "end")
    if promptInput == "":
        return
    output = openai.Completion.create(
        engine="davinci", prompt=promptInput, max_tokens=250)
    prompt_entry.delete("1.0", "end")
    prompt_label.configure(text=promptInput)
    completion_label.configure(
        text=output.choices[0].text.replace("\n\n", "\n"))


# create input frame
input_frame = tk.Frame(master=window)
input_label = tk.Label(
    master=input_frame, text="Enter a prompt:", font=("Arial", 11))
prompt_entry = tk.Text(master=input_frame, wrap="word", height=10)
get_completion_button = tk.Button(master=input_frame, text="Get Completion",
                                  command=get_completion, font=("Arial", 11))

# create output frame
output_frame = tk.Frame(master=window, borderwidth=3, relief=tk.SUNKEN)
output_scrollbar = tk.Scrollbar(master=output_frame)
prompt_label = tk.Label(master=output_frame, font=("Arial", 13))
completion_label = tk.Label(
    master=output_frame, width=120, height=32, wraplength=650, justify="left", font=("Arial", 12))

# pack input frame
input_label.pack(anchor=tk.NW, pady=(0, 15))
prompt_entry.pack(side=tk.TOP)
get_completion_button.pack(anchor=tk.SE, pady=(15, 0))
input_frame.pack(side=tk.TOP, padx=25, pady=50)

# pack output frame
output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
prompt_label.pack(anchor=tk.NW)
completion_label.pack()
output_frame.pack(side=tk.BOTTOM, padx=25, pady=25)

# display window
window.mainloop()
