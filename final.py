import tkinter
import tkinter.messagebox as tkMessageBox
import sqlite3
import tkinter.ttk as ttk

root = tkinter.Tk()
root.title("Manajemen Barang")

width = 720
height = 360
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#808080")

# ========================================VARIABLES========================================

NAMA_BARANG = tkinter.StringVar()
HARGA_BARANG = tkinter.IntVar()
JUMLAH_BARANG = tkinter.IntVar()
CARI = tkinter.StringVar()


# ========================================METHODS==========================================

def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS `barang` (barang_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nama_barang TEXT, jumlah_barang TEXT, harga_barang TEXT)")


def Exit2():
    result = tkMessageBox.askquestion('Manajemen Barang', 'Ingin keluar?', icon="warning")
    if result == 'yes':
        Home.destroy()
        exit()


def Awal():
    global Home
    Home = tkinter.Tk()
    Home.title("Manajemen Barang")
    width = 720
    height = 360
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    Home.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Home.resizable(0, 0)
    Title = tkinter.Frame(Home, bd=1, bg='#808080')
    Title.pack(pady=10)
    add_button = tkinter.Button(Title, text="Isi Barang", font=('Arial', 45), command=Showbarang, bg='#FFD700')
    add_button.grid(row=2, columnspan=2, pady=20)
    add_button2 = tkinter.Button(Title, text="Lihat List", font=('Arial', 45), command=Tampilkan, bg='#FFD700')
    add_button2.grid(row=6, columnspan=2, pady=20)
    menubar = tkinter.Menu(Home)
    menubar.add_cascade(label="Keluar", command=Exit2)
    Home.config(menu=menubar)
    Home.config(bg="#808080")


def Showbarang():
    global addnewform
    addnewform = tkinter.Toplevel()
    addnewform.title("Manajemen/Isi Barang")
    width = 600
    height = 500
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    Tambahbarang()


def Tambahbarang():
    TopAddNew = tkinter.Frame(addnewform, width=600, height=100, bd=1, relief=tkinter.SOLID)
    TopAddNew.pack(side=tkinter.TOP, pady=20)
    lbl_text = tkinter.Label(TopAddNew, text="Tambahkan Barang", font=('arial', 18), width=600)
    lbl_text.pack(fill=tkinter.X)
    MidAddNew = tkinter.Frame(addnewform, width=600)
    MidAddNew.pack(side=tkinter.TOP, pady=50)
    lbl_productname = tkinter.Label(MidAddNew, text="Nama Barang:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=0, sticky=tkinter.W)
    lbl_qty = tkinter.Label(MidAddNew, text="Jumlah Barang:", font=('arial', 25), bd=10)
    lbl_qty.grid(row=1, sticky=tkinter.W)
    lbl_price = tkinter.Label(MidAddNew, text="Harga Barang:", font=('arial', 25), bd=10)
    lbl_price.grid(row=2, sticky=tkinter.W)
    productname = tkinter.Entry(MidAddNew, textvariable=NAMA_BARANG, font=('arial', 25), width=15)
    productname.grid(row=0, column=1)
    productqty = tkinter.Entry(MidAddNew, textvariable=JUMLAH_BARANG, font=('arial', 25), width=15)
    productqty.grid(row=1, column=1)
    productprice = tkinter.Entry(MidAddNew, textvariable=HARGA_BARANG, font=('arial', 25), width=15)
    productprice.grid(row=2, column=1)
    btn_add = tkinter.Button(MidAddNew, text="Simpan", font=('arial', 18,), width=30, bg="#FFD700", command=Tambah)
    btn_add.grid(row=3, columnspan=2, pady=20)


def Tambah():
    Database()
    cursor.execute("INSERT INTO `barang` (nama_barang, jumlah_barang, harga_barang) VALUES(?, ?, ?)",
                   (str(NAMA_BARANG.get()), int(JUMLAH_BARANG.get()), int(HARGA_BARANG.get())))
    conn.commit()
    NAMA_BARANG.set("")
    HARGA_BARANG.set("")
    JUMLAH_BARANG.set("")
    cursor.close()
    conn.close()


def Lihat():
    global tree
    TopViewForm = tkinter.Frame(viewform, width=600, bd=1, relief=tkinter.SOLID)
    TopViewForm.pack(side=tkinter.TOP, fill=tkinter.X)
    LeftViewForm = tkinter.Frame(viewform, width=600)
    LeftViewForm.pack(side=tkinter.LEFT, fill=tkinter.Y)
    MidViewForm = tkinter.Frame(viewform, width=600)
    MidViewForm.pack(side=tkinter.RIGHT)
    lbl_text = tkinter.Label(TopViewForm, text="Lihat Barang", font=('arial', 18), width=600)
    lbl_text.pack(fill=tkinter.X)
    lbl_txtsearch = tkinter.Label(LeftViewForm, text="Cari Barang", font=('arial', 15))
    lbl_txtsearch.pack(side=tkinter.TOP, anchor=tkinter.W)
    search = tkinter.Entry(LeftViewForm, textvariable=CARI, font=('arial', 15), width=10)
    search.pack(side=tkinter.TOP, padx=10, fill=tkinter.X)
    btn_search = tkinter.Button(LeftViewForm, text="Cari", command=Cari)
    btn_search.pack(side=tkinter.TOP, padx=10, pady=10, fill=tkinter.X)
    btn_delete = tkinter.Button(LeftViewForm, text="Hapus", command=Hapus)
    btn_delete.pack(side=tkinter.TOP, padx=10, pady=10, fill=tkinter.X)
    scrollbarx = tkinter.Scrollbar(MidViewForm, orient=tkinter.HORIZONTAL)
    scrollbary = tkinter.Scrollbar(MidViewForm, orient=tkinter.VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("BarangID", "Nama Barang", "Jumlah Barang", "Harga Barang"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=tkinter.BOTTOM, fill=tkinter.X)
    tree.heading('BarangID', text="BarangID", anchor=tkinter.W)
    tree.heading('Nama Barang', text="Nama Barang", anchor=tkinter.W)
    tree.heading('Jumlah Barang', text="Jumlah", anchor=tkinter.W)
    tree.heading('Harga Barang', text="Harga", anchor=tkinter.W)
    tree.column('#0', stretch=tkinter.NO, minwidth=0, width=0)
    tree.column('#1', stretch=tkinter.NO, minwidth=0, width=0)
    tree.column('#2', stretch=tkinter.NO, minwidth=0, width=200)
    tree.column('#3', stretch=tkinter.NO, minwidth=0, width=120)
    tree.column('#4', stretch=tkinter.NO, minwidth=0, width=120)
    tree.pack()
    Data()


def Data():
    Database()
    cursor.execute("SELECT * FROM `barang`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def Cari():
    if CARI.get() != "":
        tree.delete(*tree.get_children())
        Database()
        cursor.execute("SELECT * FROM `barang` WHERE `nama_barang` LIKE ?", ('%' + str(CARI.get()) + '%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()





def Hapus():
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion('Manajemen Barang', 'Yakin ingin anda hapus??', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `barang` WHERE `barang_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()


def Tampilkan():
    global viewform
    viewform = tkinter.Toplevel()
    viewform.title("Manajemen/Lihat Barang")
    width = 600
    height = 400
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    viewform.resizable(0, 0)
    Lihat()




# ========================================FRAME============================================
Title = tkinter.Frame(root, bd=1, relief=tkinter.SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
btn_display = tkinter.Button(Title, text="MULAI", font=('arial black', 45, 'bold'), fg="black", command=Awal, bg='#FFD700')
btn_display.pack()
# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
