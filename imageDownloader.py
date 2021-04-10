import requests
import os
import tkinter as tk
# function for download images .jpg
def download_images():
    name_folder = inputFolderName.get()
    textLinks = inputLiksDownload.get(1.0, "end-1c")
    path = os.path.join(os.getcwd(),name_folder)
    # create new folder
    try:
        os.mkdir(path)
    except OSError:
        label_error = tk.Label(text="Error: posiblemente ya exista la carpeta")
        label_error.pack()
    else:
        links = textLinks.split('https')
        links_dnvo = []
        i = 0
        # clean array
        while i < len(links):
            if(links[i] != ''):
                links_dnvo.append(links[i])
            i = i+1
        count = 0
        len_links = len(links_dnvo)
        for index in range(len_links):
            count = count+1
            # process for download images
            with open(name_folder+'/'+str(index)+'.jpg', 'wb') as handle:
                response = requests.get('https'+str(links_dnvo[index]), stream=True)
                el.set(str(count)+'/'+str(len_links))
                window.update()
                for block in response.iter_content(1024):
                    if not block:
                        break
                    handle.write(block)
            # process finished
            if index >= len_links-1:
                el.set('Descarga terminada')
                window.update()
                os.startfile(path)
# root = tk()
window = tk.Tk()
# size and title window
window.title("Download images")
window.geometry("1024x700")
# Folder name
label_folder_name = tk.Label(text="Nombre de la carpeta")
label_folder_name.pack()
label_folder_name.config(font=('calibri', 15, 'bold'))
inputFolderName = tk.Entry(window,width=30)
inputFolderName.pack()
inputFolderName.config(font=('calibri', 15, 'bold'))
# Button download
B = tk.Button(window,text="Download",command=download_images)
B.config(font=('calibri', 15, 'bold'),borderwidth = '4')
B.pack()
#show progress
el = tk.StringVar()
tk.Label(textvariable=el).pack()
# create "textarea"
links_area = tk.Label(text="Añadir enlaces")
links_area.pack()
links_area.config(font=('calibri', 15, 'bold'))
inputLiksDownload = tk.Text(window)
inputLiksDownload.config(font=("Consolas",12), selectbackground="green",foreground="yellow",bg="black", padx=5, pady=5)
inputLiksDownload.pack(expand=tk.YES, fill=tk.BOTH) 
# create app
window.mainloop()
