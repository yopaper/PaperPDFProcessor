import tkinter as tk
import googletrans
window = tk.Tk()

#input_str_var = tk.StringVar(window)
#output_str_var = tk.StringVar(window)

input_text = tk.Text(window, width=100, height=50)
input_text.grid(row=0, column=0)
output_text = tk.Text(window, width=100, height=50)
output_text.grid(row=0, column=2)
start_button = tk.Button(window, text="->開始處理->")
start_button.grid(row=0, column=1)
window.title("PDF文字錯誤換行處理")
translator = googletrans.Translator(service_urls=[
    "translate.google.com.tw",
    "translate.google.com"
])
replace_table = []
#------------------------------------------------------
def build_table():
    for i in range(ord("a"), ord("z")+1):
        replace_table.append((chr(i)+". ", chr(i)+".\n"))
    for i in range(ord("A"), ord("Z")+1):
        replace_table.append((chr(i)+". ", chr(i)+".\n"))
#------------------------------------------------------
def process():
    try:
        text = input_text.get(1.0, "end-1c")
        text = text.replace("\n", " ")
        for i in replace_table:
            text = text.replace(i[0], i[1])
        output_text.delete(1.0, "end-1c")
        output_text.insert(tk.END, text+"\n\n")
        tls = translator.translate(text=text, dest="zh-tw").text
        output_text.insert(tk.END, "**"+tls+"**")
    except Exception as e:
        output_text.insert(tk.END, "發生錯誤:\n"+str(e))
#------------------------------------------------------
build_table()
start_button.config(command=process)
window.mainloop()

