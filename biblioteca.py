import tkinter as tk
from tkinter import ttk, messagebox


class BibliotecaApp:
    def __init__(self, master):
        self.master = master
        master.title("Biblioteca")
        master.geometry("800x600")  # Dimensiune implicită
        master.state("zoomed")  # Deschide aplicația pe tot ecranul

        # Listă pentru a stoca cărțile
        self.carti = []

        # Stilizare folosind ttk
        style = ttk.Style()
        style.theme_use("clam")  # Sau altă temă: 'default', 'classic', etc.

        # Frame principal pentru formular
        form_frame = ttk.Frame(master, padding="10")
        form_frame.pack(fill=tk.X)

        # Titlu
        ttk.Label(form_frame, text="Titlu", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_titlu = ttk.Entry(form_frame, width=30)
        self.entry_titlu.grid(row=0, column=1, pady=5)

        # Autor
        ttk.Label(form_frame, text="Autor", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_autor = ttk.Entry(form_frame, width=30)
        self.entry_autor.grid(row=1, column=1, pady=5)

        # Gen
        ttk.Label(form_frame, text="Gen", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_gen = ttk.Entry(form_frame, width=30)
        self.entry_gen.grid(row=2, column=1, pady=5)

        # Stoc
        ttk.Label(form_frame, text="Stoc", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_stoc = ttk.Entry(form_frame, width=30)
        self.entry_stoc.grid(row=3, column=1, pady=5)

        # Butoane Adaugare și Ștergere
        button_frame = ttk.Frame(master, padding="10")
        button_frame.pack(fill=tk.X)
        
        add_button = ttk.Button(button_frame, text="Adaugă carte", command=self.submit)
        add_button.pack(side=tk.LEFT, padx=10)
        
        delete_button = ttk.Button(button_frame, text="Șterge selecția", command=self.delete_book)
        delete_button.pack(side=tk.LEFT, padx=10)

        # Frame pentru căutare
        search_frame = ttk.Frame(master, padding="10")
        search_frame.pack(fill=tk.X)

        ttk.Label(search_frame, text="Caută:", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_cautare = ttk.Entry(search_frame, width=30)
        self.entry_cautare.grid(row=0, column=1, pady=5)
        search_button = ttk.Button(search_frame, text="Caută", command=self.search_books)
        search_button.grid(row=0, column=2, padx=5)

        # Frame pentru listarea cărților
        list_frame = ttk.Frame(master, padding="10")
        list_frame.pack(fill=tk.BOTH, expand=True)

        self.book_list = ttk.Treeview(list_frame, columns=("Titlu", "Autor", "Gen", "Stoc"), show="headings")
        self.book_list.heading("Titlu", text="Titlu")
        self.book_list.heading("Autor", text="Autor")
        self.book_list.heading("Gen", text="Gen")
        self.book_list.heading("Stoc", text="Stoc")
        self.book_list.pack(fill=tk.BOTH, expand=True)

    def submit(self):
        titlu = self.entry_titlu.get().strip()
        autor = self.entry_autor.get().strip()
        gen = self.entry_gen.get().strip()
        stoc = self.entry_stoc.get().strip()

        if not titlu or not autor or not gen or not stoc:
            messagebox.showerror("Eroare", "Toate câmpurile trebuie completate!")
            return

        try:
            stoc = int(stoc)
        except ValueError:
            messagebox.showerror("Eroare", "Câmpul 'Stoc' trebuie să fie un număr!")
            return

        # Adăugarea cărții în lista principală
        self.carti.append({"Titlu": titlu, "Autor": autor, "Gen": gen, "Stoc": stoc})

        # Adăugarea cărții în tabel
        self.book_list.insert("", tk.END, values=(titlu, autor, gen, stoc))

        messagebox.showinfo("Succes", "Cartea a fost adăugată cu succes!")

        # Resetarea câmpurilor
        self.entry_titlu.delete(0, tk.END)
        self.entry_autor.delete(0, tk.END)
        self.entry_gen.delete(0, tk.END)
        self.entry_stoc.delete(0, tk.END)

    def delete_book(self):
        # Obține selecția curentă
        selected_item = self.book_list.selection()
        if not selected_item:
            messagebox.showerror("Eroare", "Nu ați selectat nicio carte pentru ștergere!")
            return

        # Șterge cartea selectată din Treeview și din lista internă
        for item in selected_item:
            values = self.book_list.item(item, "values")
            self.carti = [carte for carte in self.carti if not (
                carte["Titlu"] == values[0] and
                carte["Autor"] == values[1] and
                carte["Gen"] == values[2] and
                str(carte["Stoc"]) == values[3]
            )]
            self.book_list.delete(item)

        messagebox.showinfo("Succes", "Cartea a fost ștearsă cu succes!")

    def search_books(self):
        termen_cautare = self.entry_cautare.get().strip().lower()
        for row in self.book_list.get_children():
            self.book_list.delete(row)

        for carte in self.carti:
            if (
                termen_cautare in carte["Titlu"].lower()
                or termen_cautare in carte["Autor"].lower()
                or termen_cautare in carte["Gen"].lower()
            ):
                self.book_list.insert("", tk.END, values=(carte["Titlu"], carte["Autor"], carte["Gen"], carte["Stoc"]))


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
