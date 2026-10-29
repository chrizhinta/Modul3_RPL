# Chrizhinta_025
import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_delete.configure(command=self.hapus_data)

        self.view.tabel.bind("<<TreeviewSelect>>", self.isi_form_dari_tabel)

        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        for a in self.model.get_all_anggota():
            self.view.tabel.insert("", "end", values=(a['id_anggota'], a['nama_anggota'], a['alamat']))

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

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
        _, nama, alamat = self.view.tabel.item(pilihan[0])['values']
        self.bersihkan_form()
        self.view.entry_nama.insert(0, nama)
        self.view.entry_alamat.insert(0, alamat)

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_anggota(nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data.")

    def hapus_data(self):
        id_anggota = self.get_id_terpilih()
        if id_anggota is None:
            return

        if messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            if self.model.delete_anggota(id_anggota):
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def perbarui_data(self):
        id_anggota = self.get_id_terpilih()
        if id_anggota is None:
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.update_anggota(id_anggota, nama, alamat):
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def run(self):
        self.view.mainloop()