from abc import ABC, abstractmethod
import os
import json
from datetime import datetime
class IReport(ABC):
    @abstractmethod
    def GenerateReport(self)->str:
        return("----Bao cao lop hoc----")
class Person(ABC):
    def __init__(self, HoTen, NgaySinh):
        self.__HoTen = HoTen
        self.__NgaySinh = NgaySinh
    @property
    def HoTen(self):
        return self.__HoTen
    @HoTen.setter
    def HoTen(self, value):
        self.__HoTen = value
    @property
    def NgaySinh(self):
        return self.__NgaySinh
    @NgaySinh.setter
    def NgaySinh(self, value):
        self.__NgaySinh = value
    def HienThiThongTin(self):
        print(f"Ho ten: {self.HoTen}")
        print(f"Ngay sinh: {self.NgaySinh}")
        
class Student(Person, IReport):
    def __init__(self, HoTen, NgaySinh, MaSinhVien, DiemTrungBinh):
        super().__init__(HoTen, NgaySinh)
        self.__MaSinhVien = MaSinhVien
        self.__DiemTrungBinh = DiemTrungBinh
    @property
    def MaSinhVien(self):
        return self.__MaSinhVien
    @MaSinhVien.setter
    def MaSinhVien(self, value):
        self.__MaSinhVien = value
    @property
    def DiemTrungBinh(self):
        return self.__DiemTrungBinh
    @DiemTrungBinh.setter
    def DiemTrungBinh(self, value):
        self.__DiemTrungBinh = value
    def HienThiThongTin(self):
        super().HienThiThongTin()
        print(f"Ma sinh vien: {self.MaSinhVien}")
        print(f"Diem trung binh: {self.DiemTrungBinh}")
    def GenerateReport(self)->str:
        return(f"Ho ten: {self.HoTen}\n"
                f"Diem trung binh: {self.DiemTrungBinh}")
    @staticmethod
    def NhapSV(): 
        ho_ten = input("Nhap ho ten: ") 
        while True: 
            ngay_sinh = input("Nhap ngay sinh (dd/mm/yyyy): ") 
            try:  
                dt = datetime.strptime(ngay_sinh, "%d/%m/%Y") 
                ngay_sinh = dt.strftime("%d/%m/%Y")
                break 
            except ValueError: 
                print("\033[93mDinh dang khong hop le! Vui long nhap lai theo dd/mm/yyyy.\033[0m")
        while True:
            ma_sv = input("Nhap ma sinh vien: ") 
            ma_trung = any(s.MaSinhVien == ma_sv for s in students) 
            if ma_trung: 
                print("\033[91mMa sinh vien da ton tai! Vui long nhap lai.\033[0m")
            else:
                break
        while True: 
            try: 
                diem_tb = float(input("Nhap diem trung binh (0-10): ")) 
                if 0 <= diem_tb <= 10:
                    break 
                else: 
                    print("Diem trung binh phai tu 0 den 10.")
            except ValueError: 
                print("Diem trung binh phai la so! Vui long nhap lai.")      
        return Student(ho_ten, ngay_sinh, ma_sv, diem_tb)
    
class Teacher(Person):
    def __init__(self, HoTen, NgaySinh, MaGiangVien, ChuyenNghanh):
        super().__init__(HoTen, NgaySinh)
        self.__MaGiangVien = MaGiangVien
        self.__ChuyenNghanh = ChuyenNghanh
    @property 
    def MaGiangVien(self): 
        return self.__MaGiangVien
    @MaGiangVien.setter 
    def MaGiangVien(self, value): 
        self.__MaGiangVien = value
    @property 
    def ChuyenNghanh(self): 
        return self.__ChuyenNghanh
    @ChuyenNghanh.setter 
    def ChuyenNghanh(self, value): 
        self.__ChuyenNghanh = value
    def HienThiThongTin(self):
        super().HienThiThongTin()
        print(f"Ma giang vien: {self.MaGiangVien}")
        print(f"Chuyen nganh: {self.ChuyenNghanh}")     
    @staticmethod
    def NhapGV():
        ho_ten = input("Nhap ho ten: ")
        while True:
            ngay_sinh = input("Nhap ngay sinh (dd/mm/yyyy): ") 
            try:  
                dt = datetime.strptime(ngay_sinh, "%d/%m/%Y") 
                ngay_sinh = dt.strftime("%d/%m/%Y")
                break 
            except ValueError: 
                print("\033[93mDinh dang khong hop le! Vui long nhap lai theo dd/mm/yyyy.\033[0m")
        while True:
            ma_gv = input("Nhap ma giang vien: ")
            ma_trung = any(g.MaGiangVien == ma_gv for g in teachers)
            if ma_trung:
                print("\033[91mMa giang vien da ton tai! Vui long nhap lai.\033[0m")
            else: 
                break
        chuyen_nganh = input("Nhap chuyen nganh: ")
        return Teacher(ho_ten, ngay_sinh, ma_gv, chuyen_nganh)
class Course(IReport):
    def __init__(self, TenLop):
        self.TenLop = TenLop
        self.DanhSachSV = []
        self.GiangVien = None
    @property 
    def SiSo(self): 
        return len(self.DanhSachSV)
    def NhapLop():
        ten_lop = input("Nhap ten lop: ")
        return Course(ten_lop)
    def GenerateReport(self) -> str:
        report = f"Ten lop: {self.TenLop}\nSi so: {self.SiSo}\nDanh sach sinh vien:\n"
        for sv in self.DanhSachSV:
            report += f"- {sv.HoTen} ({sv.MaSinhVien})\n"
        return report
    
students= []
teachers = []
classes = []

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def save_data():
    data = {
        "students": [
            {
                "HoTen": sv.HoTen,
                "NgaySinh": sv.NgaySinh,
                "MaSinhVien": sv.MaSinhVien,
                "DiemTrungBinh": sv.DiemTrungBinh
            } for sv in students
        ],
        "teachers": [
            {
                "HoTen": gv.HoTen,
                "NgaySinh": gv.NgaySinh,
                "MaGiangVien": gv.MaGiangVien,
                "ChuyenNghanh": gv.ChuyenNghanh
            } for gv in teachers
        ],
        "classes": [
            {
                "TenLop": lop.TenLop,
                "SiSo": lop.SiSo,
                "GiangVien": {
                    "HoTen": lop.GiangVien.HoTen if lop.GiangVien else None,
                    "MaGiangVien": lop.GiangVien.MaGiangVien if lop.GiangVien else None
                } if lop.GiangVien else None,
                "DanhSachSV": [sv.MaSinhVien for sv in lop.DanhSachSV]
            } for lop in classes
        ]
    }
    os.makedirs("data", exist_ok=True)
    with open("data/data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)



def load_data():
    global students, teachers, classes
    try:
        with open("data/data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        students = [Student(d["HoTen"], d["NgaySinh"], d["MaSinhVien"], d["DiemTrungBinh"]) 
                    for d in data.get("students", [])]
        teachers = [Teacher(d["HoTen"], d["NgaySinh"], d["MaGiangVien"], d["ChuyenNghanh"]) 
                    for d in data.get("teachers", [])]
        classes = []
        for d in data.get("classes", []):
            lop = Course(d["TenLop"])
            if d["GiangVien"]:
                gv = next((gv for gv in teachers if gv.MaGiangVien == d["GiangVien"]["MaGiangVien"]), None)
                lop.GiangVien = gv
            for mssv in d["DanhSachSV"]:
                sv = next((sv for sv in students if sv.MaSinhVien == mssv), None)
                if sv:
                    lop.DanhSachSV.append(sv)
            classes.append(lop)
    except FileNotFoundError:
        print("Khong tim thay file data.json, tao file moi...")
        students, teachers, classes = [], [], []
        os.makedirs("data", exist_ok=True)
        with open("data/data.json", "w", encoding="utf-8") as f:
            json.dump({"students": [], "teachers": [], "classes": []}, f, ensure_ascii=False, indent=4)


def main_menu():
    while True:
        clear_console()
        print("1. Quan ly sinh vien")
        print("2. Quan ly giang vien")
        print("3. Quan ly lop hoc")
        print("4. In danh sach lop hoc (duoi dang .txt)")
        print("5. Xoa du lieu")
        print("6. Thoat")
        choice = input("Nhap lua chon cua ban (1-6): ")
        if choice =="1":
            clear_console()
            print("1. Them sinh vien")
            print("2. Sua thong tin sinh vien")
            print("3. Xoa sinh vien")
            print("4. Hien thi danh sach sinh vien")
            print("5. Thoat")
            menu_choice = int(input("Nhap lua chon cua ban (1-5): "))
            if menu_choice == 1:
                sv = Student.NhapSV()
                sv.HienThiThongTin()
                students.append(sv)
                save_data()
                print("\033[92mDa them sinh vien thanh cong!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 2:
                found = False
                ma_sv = input("Nhap ma sinh vien can sua: ")
                for sv in students:
                    if sv.MaSinhVien == ma_sv:
                        found = True
                        print("Thong tin cu:")
                        sv.HienThiThongTin()
                        print("Nhap thong tin moi")
                        sv.HoTen = input("Nhap ho ten: ")
                        while True:
                            sv.NgaySinh = input("Nhap ngay sinh (dd/mm/yyyy): ")
                            try:
                                dt = datetime.strptime(sv.NgaySinh, "%d/%m/%Y")
                                sv.NgaySinh = dt.strftime("%d/%m/%Y")
                                break
                            except ValueError:
                                print("Dinh dang khong hop le! Vui long nhap lai theo dd/mm/yyyy.")
                        sv.MaSinhVien = input("Nhap ma sinh vien: ")
                        save_data()
                        print("\033[92mDa cap nhat thong tin sinh vien!\033[0m")
                        break
                if not found:
                    print("\033[93mKhong tim thay sinh vien co ma tuong ung!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 3:
                ma_sv = input("Nhap ma sinh vien can xoa: ")
                found = False
                for sv in students:
                    if sv.MaSinhVien == ma_sv:
                        students.remove(sv)
                        found = True
                        print("\033[92mDa xoa sinh vien!\033[0m")
                        save_data()
                        break
                if not found:
                    print("\033[93mKhong tim thay sinh vien co ma tuong ung!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 4:
                print("{:<5} {:<20} {:<15} {:<20} {:<10}".format("STT", "Ho ten", "Ngay sinh", "Ma sinh vien", "Diem TB"))
                print("-"*75)
                for idx, sv in enumerate(students, start=1):
                    print("{:<5} {:<20} {:<15} {:<20} {:<10}".format(
                        idx, sv.HoTen, sv.NgaySinh, sv.MaSinhVien, sv.DiemTrungBinh
                    ))
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 5:
                return main_menu()
            else:
                print("\033[91mLua chon khong hop le!\033[0m")
        elif choice  =="2":
            clear_console()
            print("1. Them giang vien")
            print("2. Sua thong tin giang vien")
            print("3. Xoa giang vien")
            print("4. Hien thi danh sach giang vien")
            print("5. Thoat")
            menu_choice = int(input("Nhap lua chon cua ban (1-5): "))
            if menu_choice == 1:
                gv = Teacher.NhapGV()
                gv.HienThiThongTin()
                teachers.append(gv)
                save_data()
                print("\033[92mDa them giang vien thang cong!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 2:
                found = False
                ma_gv = input("Nhap ma giang vien can sua: ")
                for gv in teachers:
                    if gv.MaGiangVien == ma_gv:
                        found = True
                        print("Thong tin cu:")
                        gv.HienThiThongTin()
                        print("Nhap thong tin moi")
                        gv.HoTen = input("Nhap ho ten: ")
                        while True:
                            gv.NgaySinh = input("Nhap ngay sinh (dd/mm/yyyy): ")
                            try:
                                dt = datetime.strptime(gv.NgaySinh, "%d/%m/%Y")
                                gv.NgaySinh = dt.strftime("%d/%m/%Y")
                                break 
                            except ValueError:
                                print("\033[93mDinh dang khong hop le! Vui long nhap lai theo dd/mm/yyyy.\033[0m")
                        gv.MaGiangVien = input("Nhap ma giang vien: ")
                        gv.ChuyenNghanh = input("Nhap chuyen nganh: ")
                        save_data()
                        print("Da cap nhat thong tin giang vien!")
                        break
                if not found:
                    print("\033[93mKhong tim thay giang vien co ma tuong ung!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 3:
                ma_gv = input("Nhap ma giang vien can xoa: ")
                found = False
                for gv in teachers:
                    if gv.MaGiangVien == ma_gv:
                        teachers.remove(gv)
                        found = True
                        save_data()
                        print("\033[92mDa xoa giang vien!\033[0m")
                        break
                if not found:
                    print("\033[93mKhong tim thay giang vien co ma tuong ung!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 4:
                print("{:<5} {:<20} {:<15} {:<20} {:<25}".format("STT", "Ho ten", "Ngay sinh", "Ma giang vien", "Chuyen nganh"))
                print("-"*90)
                for idx, gv in enumerate(teachers, start=1):
                    print("{:<5} {:<20} {:<15} {:<20} {:<10}".format(idx, gv.HoTen, gv.NgaySinh, gv.MaGiangVien, gv.ChuyenNghanh))
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 5:
                return main_menu()
            else:
                print("\033[91mLua chon khong hop le!\033[0m")
        elif choice=="3":
            clear_console()
            print("1. Tao lop hoc")
            print("2. Xoa lop hoc")
            print("3. Ghi danh sinh vien vao lop hoc")
            print("4. Huy ghi danh sinh vien")
            print("5. Gan giang vien vao lop hoc")
            print("6. Huy gan giang vien vao lop hoc")
            print("7.Thoat")
            
            menu_choice = (int(input("Nhap lua chon cua ban (1-7): ")))
            if menu_choice == 1:
                lop = Course.NhapLop()
                ten_trung = False
                for existing in classes:
                    if existing.TenLop.lower() == lop.TenLop.lower():
                        ten_trung = True
                        break
                if ten_trung:
                    print(f"Khong the tao lop. Vi ten lop {lop.TenLop} da ton tai!")
                else: 
                    classes.append(lop)
                    save_data()
                    print(f"\033[92mDa tao lop {lop.TenLop}!\033[0m")
                    input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 2:
                ten_lop = input("Nhap ten lop can xoa: ")
                found = False
                for lop in classes:
                    if lop.TenLop == ten_lop:
                        classes.remove(lop)
                        found = True
                        print("\033[92mDa xoa lop hoc!\033[0m")
                        save_data()
                        break
                if not found:
                    print("\033[93mKhong tim thay lop hoc co ma tuong ung!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 3:
                if not classes:
                    print("\033[91mChua co lop hoc. Vui long tao lop hoc. \033[0m")
                else:
                    print("Danh sach lop hoc: ")
                    for i, lop in enumerate(classes):
                        print(f"{i+1}. {lop.TenLop}")
                    lop_index = int(input("Nhap so thu tu lop muon ghi danh: "))-1
                    if 0 <= lop_index < len(classes):
                        lop_chon = classes[lop_index]
                        if not students:
                            print("\033[91mChua co sinh vien. Vui long them sinh vien.\033[0m")
                        else:
                            sinh_vien_chua_ghi_danh = [sv for sv in students if sv not in lop_chon.DanhSachSV]
                            if not sinh_vien_chua_ghi_danh:
                                print("\033[92mTat ca sinh vien da ghi danh!\033[0m")
                            else:
                                print("Danh sach sinh vien: ")
                                for j, sv in enumerate(sinh_vien_chua_ghi_danh):
                                    print(f"{j+1}. {sv.HoTen} | {sv.MaSinhVien}")
                                sv_index = int(input("Nhap so thu tu sinh vien muon ghi danh: "))-1
                                if 0 <= sv_index < len(sinh_vien_chua_ghi_danh):
                                    sv_chon = sinh_vien_chua_ghi_danh[sv_index]
                                    lop_chon.DanhSachSV.append(sv_chon)
                                    save_data()
                                    print(f"\033[32mDa ghi danh sinh vien {sv_chon.HoTen} vao lop hoc {lop_chon.TenLop}!\033[0m")
                                else:
                                    print("\033[91So thu tu cua sinh vien khong hop le!\033[0m")
                    else:
                        print("So thu tu khong hop le")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 4:
                if not classes:
                    print("\033[91mChua co lop hoc. Vui long tao lop hoc.\033[0m")
                else:
                    print("Danh sach lop hoc:")
                    for i, lop in enumerate(classes):
                        print(f"{i+1}. {lop.TenLop}")
                    lop_index = int(input("Nhap so thu tu lop: "))-1
                    if 0 <= lop_index < len(classes):
                        lop_chon = classes[lop_index]
                        if not students:
                            print("\033[91mChua co sinh vien. Vui long them sinh vien.\033[0m")
                        else:
                            print("Danh sach sinh vien:")
                            for i, sv in enumerate(lop_chon.DanhSachSV):
                                print(f"{i+1}. {sv.HoTen} | {sv.MaSinhVien}")
                            sv_index = int(input("Nhap so thu tu sinh vien muon huy ghi danh: "))-1
                            if 0 <= sv_index < len(lop_chon.DanhSachSV):
                                sv_huy = lop_chon.DanhSachSV.pop(sv_index)
                                save_data()
                                print(f"\033[92mDa huy ghi danh sinh vien {sv_huy.HoTen}!\033[0m")
                            else:
                                print("\033[91mSo thu tu cua sinh vien khong hop le!\033[0m")
                    else:
                        print("\033[91mSo thu tu khong hop le[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 5:
                if not classes:
                    print("\033[91mChua co lop hoc. Vui long tao lop hoc.\033[0m")
                else:
                    print("Danh sach lop hoc:")
                    for i, lop in enumerate(classes):
                        if lop.GiangVien:
                            print(f"{i+1}. {lop.TenLop}  ({lop.GiangVien.HoTen} | {lop.GiangVien.MaGiangVien})")
                        else:
                            print(f"{i+1}. {lop.TenLop}")
                    lop_index = int(input("Nhap so thu tu lop muon gan giang vien: "))-1
                if 0 <= lop_index < len(classes):
                    lop_chon = classes[lop_index]
                    if not teachers:
                        print("\033[91mChua co giang vien. Vui long them giang vien.\033[0m")
                    else:
                        print("Danh sach giang vien: ")
                        for j, gv in enumerate(teachers):
                            print(f"{j+1}. {gv.HoTen} | {gv.MaGiangVien}")
                        gv_index = int(input("Nhap so thu tu giang vien muon gan: "))-1
                        if 0 <= gv_index < len(teachers):
                            gv_chon = teachers[gv_index]
                            if lop_chon.GiangVien is None:
                                lop_chon.GiangVien = gv_chon
                                save_data()
                                print(f"\033[32mDa gan giang vien {gv_chon.HoTen} vao lop hoc {lop_chon.TenLop}!\033[0m")
                            elif lop_chon.GiangVien == gv_chon:
                                print(f"\033[93mGiang vien {gv_chon.HoTen} da co trong lop hoc {lop_chon.TenLop}!\033[0m")
                            else:
                                print(f"\033[93mLop {lop_chon.TenLop} da co giang vien {lop_chon.GiangVien.HoTen} phu trach!\033[0m")
                        else:
                            print("\033[91mSo thu tu cua giang vien khong hop le!\033[0m")
                else:
                    print("\033[91mSo thu tu khong hop le!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 6:
                if not classes:
                    print("\033[91mChua co lop hoc. Vui long tao lop hoc.\033[0m")
                else:
                    print("Danh sach lop hoc:")
                    for i, lop in enumerate(classes):
                        if lop.GiangVien:
                            print(f"{i+1}. {lop.TenLop}  ({lop.GiangVien.HoTen} | {lop.GiangVien.MaGiangVien})")
                        else:
                            print(f"{i+1}. {lop.TenLop}")
                    lop_index = int(input("Nhap so thu tu lop: "))-1
                    if 0<= lop_index < len(classes):
                        lop_chon = classes[lop_index]
                        if lop_chon.GiangVien:
                            print(f"Giang vien hien tai: {lop_chon.GiangVien.HoTen} | {lop_chon.GiangVien.MaGiangVien}")
                            confirm = input("Ban co muon huy gan giang vien nay khong? (Y/N): ")
                            if confirm.lower() == "y":
                                gv_huy = lop_chon.GiangVien
                                lop_chon.GiangVien = None
                                save_data()
                                print(f"\033[32mDa huy giang vien {gv_huy.HoTen} khoi lop {lop_chon.TenLop}!\033[0m")
                        else:
                            print("\033[93mLop hoc khong co giang vien phu trach!\033[0m")
                    else:
                        print("\033[93mLop hoc khong co giang vien phu trach!\033[0m")
                input("\nNhan bat ky phim de quay lai menu...")
            elif menu_choice == 7:
                return main_menu()
            else:
                print("\033[91mLua chon khong hop le!\033[0m")
        elif choice == "4":
            print("Danh sach lop hoc:")
            for i, lop in enumerate(classes):
                print(f"{i+1}. {lop.TenLop}")
            lop_index = int(input("Nhap so thu tu lop muon in: "))-1
            if 0 <= lop_index < len(classes): 
                lop_chon = classes[lop_index]
                tenfile_format = f"danhsach_{lop_chon.TenLop.replace(' ', '_')}.txt"
                with open(tenfile_format, "w", encoding="utf-8") as file:
                    file.write(f"Lop: {lop_chon.TenLop}\n")
                    file.write(f"Si so: {lop_chon.SiSo}")
                    if lop_chon.GiangVien:
                        gv_chon = lop_chon.GiangVien
                        file.write(f"\nPhu trach: {gv_chon.HoTen} | {gv_chon.MaGiangVien}\n")
                        file.write(f"Chuyen nganh: {gv_chon.ChuyenNghanh}\n")
                    file.write("Danh sach sinh vien:\n")
                    file.write("{:<5} {:<20} {:<15} {:<20} {:<10}\n".format("STT", "Ho va Ten", "Ngay sinh", "MSSV", "DTB"))
                    def lay_ten_chinh(ho_ten):
                        return ho_ten.split()[-1]
                    ten_sap_xep = sorted(lop_chon.DanhSachSV, key=lambda sv: lay_ten_chinh(sv.HoTen))
                    for i, sv in enumerate(ten_sap_xep, start=1): 
                        file.write("{:<5} {:<20} {:<15} {:<20} {:<10}\n".format( i, sv.HoTen, sv.NgaySinh, sv.MaSinhVien, sv.DiemTrungBinh))
                print(f"\033[92mDa xuat thanh cong danh sach lop hoc ra file {tenfile_format}\033[0m")
            else:
                print("\033[91mSo thu tu khong hop le!\033[0m")
            input("\nNhan bat ky phim de quay lai menu...")
        elif choice == "5":
            clear_console()
            confirm = input("Ban co muon xoa toan bo du lieu khong? (Y/N): ")
            if confirm.lower()== "y":
                os.makedirs("data", exist_ok=True) 
                empty_data = { 
                    "students": [], 
                    "teachers": [], 
                    "classes": [] 
                }
                with open("data/data.json", "w", encoding="utf-8") as f: 
                    json.dump(empty_data, f, ensure_ascii=False, indent=4) 
                students.clear() 
                teachers.clear() 
                classes.clear() 
                print("\033[92mDa xoa het du lieu trong file data/data.json va bo nho RAM!\033[0m") 
            else: 
                print("Ban da huy bo xoa du lieu.")
            input("\nNhan bat ky phim de quay lai menu...")
        elif choice=="6":
            print("Thoat chuong trinh!")
            break
        else:
            print("Lua chon khong hop le!")
load_data()
main_menu()
