class NhanVien:
    nhanviens = []
    def them_nhanvien(self, nhan_vien):
        self.nhanviens.append(nhan_vien)

    def capnhat_nhanvien(self, nhan_vien_cu, nhan_vien_moi):
     for i in range(len(self.nhanviens)):
       if self.nhanviens[i] == nhan_vien_cu:
            self.nhanviens[i] = nhan_vien_moi
       else: 
           print('Không tìm thấy nhân viên trong danh sách')
       
    def xoa_nhanvien(self, vi_tri):
        if len(self.nhanviens) == 0:
             print('List is empty')
        else:
             self.nhanviens.remove(self.nhanviens[vi_tri])

    def hien_nhanvien(self):
       for nv in self.nhanviens:
           print(nv)      

nv_obj = NhanVien()

while True:
    print ('1 -- Thêm nhân viên' )
    print ('2 -- Hiển thị nhân viên' )
    print ('3 -- Cập nhật nhân viên' )
    print ('4 -- Xoá nhân viên' )
    print ('5 -- Thoát chương trình' )

    chon = int(input("Chọn chức năng: "))
    if chon == 1:
        ten_nv = input("Nhập tên nhân viên: ")
        nv_obj.them_nhanvien(ten_nv)

    elif chon == 2:
        nv_obj.hien_nhanvien()

    elif chon == 3:
        nv_cu = input("Nhập tên nhân viên cũ: ")
        nv_moi = input("Nhập tên nhân viên mới: ")
        nv_obj.capnhat_nhanvien(nv_cu, nv_moi)

    elif chon == 4:
        vt = input("Nhập vị trí nhân viên cần xoá: ")
        nv_obj.xoa_nhanvien(vt)
        
    elif chon == 5:
        break
