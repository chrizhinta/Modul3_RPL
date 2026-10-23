# Chrizhinta_025
import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self):
        self.model = BukuModel()
        self.view = BukuView()

        # Binding tombol
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        # Klik baris tabel -> isi form otomatis
        self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_tabel)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for buku in self.model.get_all_buku():
            self.view.tabel.insert("", "end", values=(buku['id_buku'], buku['judul'], buku['penulis'], buku['tahun_terbit']))

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    def get_id_terpilih(self):
        pilihan = self.view.tabel.selection()
        if not pilihan:
            messagebox.showwarning("Peringatan", "Pilih baris di tabel terlebih dahulu!")
            return None
        return self.view.tabel.item(pilihan[0])['values'][0]

    def isi_form_dari_tabel(self, event=None):
        pilihan = self.view.tabel.selection()
        if not pilihan:
            return
        _, judul, penulis, tahun = self.view.tabel.item(pilihan[0])['values']
        self.bersihkan_form()
        self.view.entry_judul.insert(0, judul)
        self.view.entry_penulis.insert(0, penulis)
        self.view.entry_tahun.insert(0, tahun)

    def simpan_data(self):
        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        id_buku = self.get_id_terpilih()
        if id_buku is None:
            return

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            if self.model.delete_buku(id_buku):
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        id_buku = self.get_id_terpilih()
        if id_buku is None:
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_buku(id_buku, judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()