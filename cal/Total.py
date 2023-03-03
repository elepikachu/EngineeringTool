# -------------------------------------------------------------
# cal/Total.py
# tkinter源代码实现
# -------------------------------------------------------------
import tkinter
import base64, os  #将所需要的图标转换为.py文件下的base64
import numpy as np
from tkinter import *
from tkinter import messagebox, Entry, ttk
import tkinter as tk        #界面模块

import iapws                 #水性质计算模块
from iapws import IAPWS97   #水性质计算模块
from iapws import iapws97, IAPWS97
import pandas as pd
from PIL import Image, ImageTk


# def pic2py(picture_names, py_name):
#     write_data = []
#     for picture_name in picture_names:
#         filename = picture_name.replace(".", "_")
#         with open("%s" % picture_name, "rb") as r:
#             b64str = base64.b64encode(r.read())
#         write_data.append('%s = "%s"\n' % (filename, b64str.decode()))
#     with open(f'{py_name}.py', "w+") as f:
#         for data in write_data:
#             f.write(data)
# # os.chdir('./../Images')
# pics = ["one1.jpg","one2.jpg", "GB2589_1.jpg", "all.jpg" , "NOTE_SECTION_B.jpg"]
# pic2py(pics, "images")
# print("good")


# with open("./abc.ico", "wb+") as w:
#     w.write(base64.b64decode(images))

# icon.addPixmap(GtGui.QPixmap("./one1.jpg"), GtGui.GIcon.Normal, QtGui.GIcon.Off)
# os.remove("./abc.ico")
#
# with open("./one2.jpg", "wb") as w:
#     w.write(base64.b64encode(one2))
# icon.addPixmap(GtGui.QPixmap("./one2.jpg"), GtGui.GIcon.Normal, QtGui.GIcon.Off)
# os.remove("./one2.jpg")
#
# with open("./GB2589_1.jpg", "wb") as w:
#     w.write(base64.b64encode(GB2589_1))
# icon.addPixmap(GtGui.QPixmap("./GB2589_1.jpg"), GtGui.GIcon.Normal, QtGui.GIcon.Off)
# os.remove("./GB2589_1.jpg")
#
# with open("./all.jpg", "wb") as w:
#     w.write(base64.b64encode(all))
# icon.addPixmap(GtGui.QPixmap("./all.jpg"), GtGui.GIcon.Normal, QtGui.GIcon.Off)
# os.remove("./all.jpg")
#
# with open("./NOTE_SECTION_B.jpg", "wb") as w:
#     w.write(base64.b64encode(NOTE_SECTION_B))
# icon.addPixmap(GtGui.QPixmap("./NOTE_SECTION_B.jpg"), GtGui.GIcon.Normal, QtGui.GIcon.Off)
# os.remove("./NOTE_SECTION_B.jpg")
# ============= Function Code ==================================================
# ***PAGE 1 ***********************************************************************
def coal_chk():
    if coal_var.get() == 1:
        coal_qty['state'] = "normal"
        coal_qty['bg'] = '#248aa2'
        coal_qty['fg'] = "white"

    else:
        coal_qty['state'] = "disabled"

    if coal_var1.get() == 1:
        coal_qty1['state'] = "normal"
        coal_qty1['bg'] = '#248aa2'
        coal_qty1['fg'] = "white"

    else:
        coal_qty1['state'] = "disabled"


# ***PAGE 2 ***********************************************************************


def one1_chk(): #Are the frames all included in this function?
    if one_var1.get() == 1:
        one_qty1['state'] = "normal"
        one_qty1['bg'] = '#248aa2'
        one_qty1['fg'] = "white"

    else:
        one_qty1['state'] = "disabled"

    if one_var1.get() == 1:
        one_qty2['state'] = "normal"
        one_qty2['bg'] = '#248aa2'
        one_qty2['fg'] = "white"
        one_qty3['state'] = "normal"
        one_qty3['bg'] = '#248aa2'
        one_qty3['fg'] = "white"

    else:
        one_qty2['state'] = "disabled"
        one_qty3['state'] = "disabled"

def one2_chk(): #Are the frames all included in this function?
    if one_var2.get() == 1:
        one2_qty1['state'] = "normal"
        one2_qty1['bg'] = '#248aa2'
        one2_qty1['fg'] = "white"
        one2_qty2['state'] = "normal"
        one2_qty2['bg'] = '#248aa2'
        one2_qty2['fg'] = "white"
        one2_qty3['state'] = "normal"
        one2_qty3['bg'] = '#248aa2'
        one2_qty3['fg'] = "white"
    else:
        one2_qty1['state'] = "disabled"
        one2_qty2['state'] = "disabled"
        one2_qty3['state'] = "disabled"

def one3_chk(): #Are the frames all included in this function?
    if one_var3.get() == 1:
        one3_qty1['state'] = "normal"
        one3_qty1['bg'] = '#248aa2'
        one3_qty1['fg'] = "white"
        one3_qty2['state'] = "normal"
        one3_qty2['bg'] = '#248aa2'
        one3_qty2['fg'] = "white"
        one3_qty3['state'] = "normal"
        one3_qty3['bg'] = '#248aa2'
        one3_qty3['fg'] = "white"
    else:
        one3_qty1['state'] = "disabled"
        one3_qty2['state'] = "disabled"
        one3_qty3['state'] = "disabled"

def one4_chk(): #Are the frames all included in this function?
    if one_var4.get() == 1:
        one4_qty1['state'] = "normal"
        one4_qty1['bg'] = '#248aa2'
        one4_qty1['fg'] = "white"
        one4_qty2['state'] = "normal"
        one4_qty2['bg'] = '#248aa2'
        one4_qty2['fg'] = "white"
        one4_qty3['state'] = "normal"
        one4_qty3['bg'] = '#248aa2'
        one4_qty3['fg'] = "white"
    else:
        one4_qty1['state'] = "disabled"
        one4_qty2['state'] = "disabled"
        one4_qty3['state'] = "disabled"

def stableA_1():
    A_SP1_F1_q = one_qty1.get()
    A_SP1_F2_q = one_qty2.get()
    A_SP1_F3_q = one_qty3.get()

    if one_var1.get() == 0:
        A_SP1_F1_q = 0
        A_SP1_F2_q = 0
        A_SP1_F3_q = 0

    elif one_var1.get() == 1 and one_qty1.get() == "" or one_qty2.get() == "" or one_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        A_SP1_F1_q = 0
        A_SP1_F2_q = 0
        A_SP1_F3_q = 0

    total_SP1_CEi = float(A_SP1_F1_q) * float(A_SP1_F2_q) * float(A_SP1_F3_q) * (44/12) / 100

    if A_SP1_total_frame.get() != "":
        A_SP1_total_frame.delete(0, "end")
        A_SP1_total_frame.insert("end", total_SP1_CEi)
    else:
        A_SP1_total_frame.insert("end", total_SP1_CEi)

#  ==============================================================
    A_SP2_F1_q = one2_qty1.get()
    A_SP2_F2_q = one2_qty2.get()
    A_SP2_F3_q = one2_qty3.get()

    if one_var2.get() == 0:
        A_SP2_F1_q = 0
        A_SP2_F2_q = 0
        A_SP2_F3_q = 0

    elif one_var2.get() == 1 and one2_qty1.get() == "" or one2_qty2.get() == "" or one2_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        A_SP2_F1_q = 0
        A_SP2_F2_q = 0
        A_SP2_F3_q = 0

    total_SP2_CEi = (float(A_SP2_F1_q) * float(A_SP2_F2_q) * float(A_SP2_F3_q)  * (44/12)) / 100

    if A_SP2_total_frame.get() != "":
        A_SP2_total_frame.delete(0, "end")
        A_SP2_total_frame.insert("end", total_SP2_CEi)
    else:
        A_SP2_total_frame.insert("end", total_SP2_CEi)
#  ==============================================================
    A_SP3_F1_q = one3_qty1.get()
    A_SP3_F2_q = one3_qty2.get()
    A_SP3_F3_q = one3_qty3.get()

    if one_var3.get() == 0:
        A_SP3_F1_q = 0
        A_SP3_F2_q = 0
        A_SP3_F3_q = 0

    elif one_var3.get() == 1 and one3_qty1.get() == "" or one3_qty2.get() == "" or one3_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        A_SP3_F1_q = 0
        A_SP3_F2_q = 0
        A_SP3_F3_q = 0

    total_SP3_CEi = (float(A_SP3_F1_q) * float(A_SP3_F2_q) * float(A_SP3_F3_q)  * (44/12)) / 100

    if A_SP3_total_frame.get() != "":
        A_SP3_total_frame.delete(0, "end")
        A_SP3_total_frame.insert("end", total_SP3_CEi)
    else:
        A_SP3_total_frame.insert("end", total_SP3_CEi)
#  ==============================================================
    A_SP4_F1_q = one4_qty1.get()
    A_SP4_F2_q = one4_qty2.get()
    A_SP4_F3_q = one4_qty3.get()

    if one_var4.get() == 0:
        A_SP4_F1_q = 0
        A_SP4_F2_q = 0
        A_SP4_F3_q = 0

    elif one_var4.get() == 1 and one4_qty1.get() == "" or one4_qty2.get() == "" or one4_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        A_SP4_F1_q = 0
        A_SP4_F2_q = 0
        A_SP4_F3_q = 0

    total_SP4_CEi = (float(A_SP4_F1_q) * float(A_SP4_F2_q) * float(A_SP4_F3_q)  * (44/12)) / 100


    if A_SP4_total_frame.get() != "":
        A_SP4_total_frame.delete(0, "end")
        A_SP4_total_frame.insert("end", total_SP4_CEi)
    else:
        A_SP4_total_frame.insert("end", total_SP4_CEi)
# total ---------------------------------------------------------------
    total_SP_all_CEi = total_SP1_CEi + total_SP2_CEi + total_SP3_CEi + total_SP4_CEi
    if A_SP_all_total_frame.get() != "":
        A_SP_all_total_frame.delete(0, "end")
        A_SP_all_total_frame.insert("end", total_SP_all_CEi)
    else:
        A_SP_all_total_frame.insert("end", total_SP_all_CEi)

    return total_SP_all_CEi
# two*****************************************************************************
def two1_chk():
    if two_var1.get() == 1:
        two1_qty1['state'] = "normal"
        two1_qty1['bg'] = '#248aa2'
        two1_qty1['fg'] = "white"
        two1_qty2['state'] = "normal"
        two1_qty2['bg'] = '#248aa2'
        two1_qty2['fg'] = "white"
        two1_qty3['state'] = "normal"
        two1_qty3['bg'] = '#248aa2'
        two1_qty3['fg'] = "white"
    else:
        two1_qty1['state'] = "disabled"
        two1_qty2['state'] = "disabled"
        two1_qty3['state'] = "disabled"

def two2_chk():
    if two_var2.get() == 1:
        two2_qty1['state'] = "normal"
        two2_qty1['bg'] = '#248aa2'
        two2_qty1['fg'] = "white"
        two2_qty2['state'] = "normal"
        two2_qty2['bg'] = '#248aa2'
        two2_qty2['fg'] = "white"
        two2_qty3['state'] = "normal"
        two2_qty3['bg'] = '#248aa2'
        two2_qty3['fg'] = "white"
    else:
        two2_qty1['state'] = "disabled"
        two2_qty2['state'] = "disabled"
        two2_qty3['state'] = "disabled"
def two3_chk():
    if two_var3.get() == 1:
        two3_qty1['state'] = "normal"
        two3_qty1['bg'] = '#248aa2'
        two3_qty1['fg'] = "white"
        two3_qty2['state'] = "normal"
        two3_qty2['bg'] = '#248aa2'
        two3_qty2['fg'] = "white"
        two3_qty3['state'] = "normal"
        two3_qty3['bg'] = '#248aa2'
        two3_qty3['fg'] = "white"
    else:
        two3_qty1['state'] = "disabled"
        two3_qty2['state'] = "disabled"
        two3_qty3['state'] = "disabled"

def two4_chk(): #Are the frames all included in this function?
    if two_var4.get() == 1:
        two4_qty1['state'] = "normal"
        two4_qty1['bg'] = '#248aa2'
        two4_qty1['fg'] = "white"
        two4_qty2['state'] = "normal"
        two4_qty2['bg'] = '#248aa2'
        two4_qty2['fg'] = "white"
        two4_qty3['state'] = "normal"
        two4_qty3['bg'] = '#248aa2'
        two4_qty3['fg'] = "white"
    else:
        two4_qty1['state'] = "disabled"
        two4_qty2['state'] = "disabled"
        two4_qty3['state'] = "disabled"

def stableB_1():
    B_SP1_F1_q = two1_qty1.get()
    B_SP1_F2_q = two1_qty2.get()
    B_SP1_F3_q = two1_qty3.get()

    if two_var1.get() == 0:
        B_SP1_F1_q = 0
        B_SP1_F2_q = 0
        B_SP1_F3_q = 0

    elif two_var1.get() == 1 and two1_qty1.get() == "" or two1_qty2.get() == "" or two1_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        B_SP1_F1_q = 0
        B_SP1_F2_q = 0
        B_SP1_F3_q = 0

    B_total_SP1_CEi = (float(B_SP1_F1_q) * float(B_SP1_F2_q) * float(B_SP1_F3_q) )


    if B_SP1_total_frame.get() != "":
        B_SP1_total_frame.delete(0, "end")
        B_SP1_total_frame.insert("end", B_total_SP1_CEi)
    else:
        B_SP1_total_frame.insert("end", B_total_SP1_CEi)


#  ==============================================================
    B_SP2_F1_q = two2_qty1.get()
    B_SP2_F2_q = two2_qty2.get()
    B_SP2_F3_q = two2_qty3.get()

    if two_var2.get() == 0:
        B_SP2_F1_q = 0
        B_SP2_F2_q = 0
        B_SP2_F3_q = 0

    elif two_var2.get() == 1 and two2_qty1.get() == "" or two2_qty2.get() == "" or two2_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        B_SP2_F1_q = 0
        B_SP2_F2_q = 0
        B_SP2_F3_q = 0

    B_total_SP2_CEi = (float(B_SP2_F1_q) * float(B_SP2_F2_q) * float(B_SP2_F3_q))

    if B_SP2_total_frame.get() != "":
        B_SP2_total_frame.delete(0, "end")
        B_SP2_total_frame.insert("end", B_total_SP2_CEi)
    else:
        B_SP2_total_frame.insert("end", B_total_SP2_CEi)
#  ==============================================================
    B_SP3_F1_q = two3_qty1.get()
    B_SP3_F2_q = two3_qty2.get()
    B_SP3_F3_q = two3_qty3.get()

    if two_var3.get() == 0:
        B_SP3_F1_q = 0
        B_SP3_F2_q = 0
        B_SP3_F3_q = 0

    elif two_var3.get() == 1 and two3_qty1.get() == "" or two3_qty2.get() == "" or two3_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        B_SP3_F1_q = 0
        B_SP3_F2_q = 0
        B_SP3_F3_q = 0

    B_total_SP3_CEi = (float(B_SP3_F1_q) * float(B_SP3_F2_q) * float(B_SP3_F3_q))


    if B_SP3_total_frame.get() != "":
        B_SP3_total_frame.delete(0, "end")
        B_SP3_total_frame.insert("end", B_total_SP3_CEi)
    else:
        B_SP3_total_frame.insert("end", B_total_SP3_CEi)
#  ==============================================================
    B_SP4_F1_q = two4_qty1.get()
    B_SP4_F2_q = two4_qty2.get()
    B_SP4_F3_q = two4_qty3.get()

    if two_var4.get() == 0:
        B_SP4_F1_q = 0
        B_SP4_F2_q = 0
        B_SP4_F3_q = 0

    elif two_var4.get() == 1 and two4_qty1.get() == "" or two4_qty2.get() == "" or two4_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        B_SP4_F1_q = 0
        B_SP4_F2_q = 0
        B_SP4_F3_q = 0

    B_total_SP4_CEi = (float(B_SP4_F1_q) * float(B_SP4_F2_q) * float(B_SP4_F3_q) )


    if B_SP4_total_frame.get() != "":
        B_SP4_total_frame.delete(0, "end")
        B_SP4_total_frame.insert("end", B_total_SP4_CEi)
    else:
        B_SP4_total_frame.insert("end", B_total_SP4_CEi)
# total ---------------------------------------------------------------
    B_total_SP_all_CEi = B_total_SP1_CEi + B_total_SP2_CEi + B_total_SP3_CEi + B_total_SP4_CEi
    if B_SP_all_total_frame.get() != "":
        B_SP_all_total_frame.delete(0, "end")
        B_SP_all_total_frame.insert("end", B_total_SP_all_CEi)
    else:
        B_SP_all_total_frame.insert("end", B_total_SP_all_CEi)

    return B_total_SP_all_CEi
# three*****************************************************************************
def three1_chk():
    if three_var1.get() == 1:
        three1_qty1['state'] = "normal"
        three1_qty1['bg'] = '#248aa2'
        three1_qty1['fg'] = "white"
        three1_qty2['state'] = "normal"
        three1_qty2['bg'] = '#248aa2'
        three1_qty2['fg'] = "white"

    else:
        three1_qty1['state'] = "disabled"
        three1_qty2['state'] = "disabled"

def three2_chk():
    if three_var2.get() == 1:
        three2_qty1['state'] = "normal"
        three2_qty1['bg'] = '#248aa2'
        three2_qty1['fg'] = "white"
        three2_qty2['state'] = "normal"
        three2_qty2['bg'] = '#248aa2'
        three2_qty2['fg'] = "white"

    else:
        three2_qty1['state'] = "disabled"
        three2_qty2['state'] = "disabled"

def three3_chk():
    if three_var3.get() == 1:
        three3_qty1['state'] = "normal"
        three3_qty1['bg'] = '#248aa2'
        three3_qty1['fg'] = "white"
        three3_qty2['state'] = "normal"
        three3_qty2['bg'] = '#248aa2'
        three3_qty2['fg'] = "white"

    else:
        three3_qty1['state'] = "disabled"
        three3_qty2['state'] = "disabled"

def three4_chk(): #Are the frames all included in this function?
    if three_var4.get() == 1:
        three4_qty1['state'] = "normal"
        three4_qty1['bg'] = '#248aa2'
        three4_qty1['fg'] = "white"
        three4_qty2['state'] = "normal"
        three4_qty2['bg'] = '#248aa2'
        three4_qty2['fg'] = "white"
    else:
        three4_qty1['state'] = "disabled"
        three4_qty2['state'] = "disabled"

def stableC_1():
    C_SP1_F1_q = three1_qty1.get()
    C_SP1_F2_q = three1_qty2.get()

    if three_var1.get() == 0:
        C_SP1_F1_q = 0
        C_SP1_F2_q = 0

    elif three_var1.get() == 1 and three1_qty1.get() == "" or three1_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        C_SP1_F1_q = 0
        C_SP1_F2_q = 0

    C_total_SP1_PEi = (float(C_SP1_F1_q) * float(C_SP1_F2_q) * (44/12))/100

    if C_SP1_total_frame.get() != "":
        C_SP1_total_frame.delete(0, "end")
        C_SP1_total_frame.insert("end", C_total_SP1_PEi)
    else:
        C_SP1_total_frame.insert("end", C_total_SP1_PEi)
#  ==============================================================
    C_SP2_F1_q = three2_qty1.get()
    C_SP2_F2_q = three2_qty2.get()

    if three_var2.get() == 0:
        C_SP2_F1_q = 0
        C_SP2_F2_q = 0


    elif three_var2.get() == 1 and three2_qty1.get() == "" or three2_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        C_SP2_F1_q = 0
        C_SP2_F2_q = 0

    C_total_SP2_PEi = (float(C_SP2_F1_q) * float(C_SP2_F2_q) * (44/12))/100

    if C_SP2_total_frame.get() != "":
        C_SP2_total_frame.delete(0, "end")
        C_SP2_total_frame.insert("end", C_total_SP2_PEi)
    else:
        C_SP2_total_frame.insert("end", C_total_SP2_PEi)
#  ==============================================================
    C_SP3_F1_q = three3_qty1.get()
    C_SP3_F2_q = three3_qty2.get()
    if three_var3.get() == 0:
        C_SP3_F1_q = 0
        C_SP3_F2_q = 0

    elif three_var3.get() == 1 and three3_qty1.get() == "" or three3_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        C_SP3_F1_q = 0
        C_SP3_F2_q = 0

    C_total_SP3_PEi = (float(C_SP3_F1_q) * float(C_SP3_F2_q) * (44/12))/100

    if C_SP3_total_frame.get() != "":
        C_SP3_total_frame.delete(0, "end")
        C_SP3_total_frame.insert("end", C_total_SP3_PEi)
    else:
        C_SP3_total_frame.insert("end", C_total_SP3_PEi)
#  ==============================================================
    C_SP4_F1_q = three4_qty1.get()
    C_SP4_F2_q = three4_qty2.get()

    if three_var4.get() == 0:
        C_SP4_F1_q = 0
        C_SP4_F2_q = 0

    elif three_var4.get() == 1 and three4_qty1.get() == "" or three4_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        C_SP4_F1_q = 0
        C_SP4_F2_q = 0

    C_total_SP4_PEi = (float(C_SP4_F1_q) * float(C_SP4_F2_q) * (44/12))/100


    if C_SP4_total_frame.get() != "":
        C_SP4_total_frame.delete(0, "end")
        C_SP4_total_frame.insert("end", C_total_SP4_PEi)
    else:
        C_SP4_total_frame.insert("end", C_total_SP4_PEi)

    total_SP_all_PEi = C_total_SP1_PEi + C_total_SP2_PEi + C_total_SP3_PEi + C_total_SP4_PEi

    if C_SP_all_total_frame.get() != "":
        C_SP_all_total_frame.delete(0, "end")
        C_SP_all_total_frame.insert("end", total_SP_all_PEi)
    else:
        C_SP_all_total_frame.insert("end", total_SP_all_PEi)
# four*****************************************************************************
def four1_chk():
    if four_var1.get() == 1:
        four1_qty1['state'] = "normal"
        four1_qty1['bg'] = '#248aa2'
        four1_qty1['fg'] = "white"
        four1_qty2['state'] = "normal"
        four1_qty2['bg'] = '#248aa2'
        four1_qty2['fg'] = "white"
        four1_qty3['state'] = "normal"
        four1_qty3['bg'] = '#248aa2'
        four1_qty3['fg'] = "white"
        four1_qty4['state'] = "normal"
        four1_qty4['bg'] = '#248aa2'
        four1_qty4['fg'] = "white"
    else:
        four1_qty1['state'] = "disabled"
        four1_qty2['state'] = "disabled"
        four1_qty3['state'] = "disabled"
        four1_qty4['state'] = "disabled"

def four2_chk():
    if four_var2.get() == 1:
        four2_qty1['state'] = "normal"
        four2_qty1['bg'] = '#248aa2'
        four2_qty1['fg'] = "white"
        four2_qty2['state'] = "normal"
        four2_qty2['bg'] = '#248aa2'
        four2_qty2['fg'] = "white"
        four2_qty3['state'] = "normal"
        four2_qty3['bg'] = '#248aa2'
        four2_qty3['fg'] = "white"
        four2_qty4['state'] = "normal"
        four2_qty4['bg'] = '#248aa2'
        four2_qty4['fg'] = "white"
    else:
        four2_qty1['state'] = "disabled"
        four2_qty2['state'] = "disabled"
        four2_qty3['state'] = "disabled"
        four2_qty4['state'] = "disabled"

def four3_chk():
    if four_var3.get() == 1:
        four3_qty1['state'] = "normal"
        four3_qty1['bg'] = '#248aa2'
        four3_qty1['fg'] = "white"
        four3_qty2['state'] = "normal"
        four3_qty2['bg'] = '#248aa2'
        four3_qty2['fg'] = "white"
        four3_qty3['state'] = "normal"
        four3_qty3['bg'] = '#248aa2'
        four3_qty3['fg'] = "white"
        four3_qty4['state'] = "normal"
        four3_qty4['bg'] = '#248aa2'
        four3_qty4['fg'] = "white"
    else:
        four3_qty1['state'] = "disabled"
        four3_qty2['state'] = "disabled"
        four3_qty3['state'] = "disabled"
        four3_qty4['state'] = "disabled"

def four4_chk():  # Are the frames all included in this function?
    if four_var4.get() == 1:
        four4_qty1['state'] = "normal"
        four4_qty1['bg'] = '#248aa2'
        four4_qty1['fg'] = "white"
        four4_qty2['state'] = "normal"
        four4_qty2['bg'] = '#248aa2'
        four4_qty2['fg'] = "white"
        four4_qty3['state'] = "normal"
        four4_qty3['bg'] = '#248aa2'
        four4_qty3['fg'] = "white"
        four4_qty4['state'] = "normal"
        four4_qty4['bg'] = '#248aa2'
        four4_qty4['fg'] = "white"
    else:
        four4_qty1['state'] = "disabled"
        four4_qty2['state'] = "disabled"
        four4_qty3['state'] = "disabled"
        four4_qty4['state'] = "disabled"

def stableD_1():
    D_SP1_F1_q = four1_qty1.get()
    D_SP1_F2_q = four1_qty2.get()
    D_SP1_F3_q = four1_qty3.get()
    D_SP1_F4_q = four1_qty4.get()

    if four_var1.get() == 0:
        D_SP1_F1_q = 0
        D_SP1_F2_q = 0
        D_SP1_F3_q = 0
        D_SP1_F4_q = 0

    elif four_var1.get() == 1 and four1_qty1.get() == "" or four1_qty2.get() == "" or four1_qty3.get() == "" or four1_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        D_SP1_F1_q = 0
        D_SP1_F2_q = 0
        D_SP1_F3_q = 0
        D_SP1_F4_q = 0

    D_total_SP1_PEi = (float(D_SP1_F1_q) + float(D_SP1_F2_q)) * (float(D_SP1_F3_q) + float(D_SP1_F4_q))

    if D_SP1_total_frame.get() != "":
        D_SP1_total_frame.delete(0, "end")
        D_SP1_total_frame.insert("end", D_total_SP1_PEi)
    else:
        D_SP1_total_frame.insert("end", D_total_SP1_PEi)
#  ==============================================================
    D_SP2_F1_q = four2_qty1.get()
    D_SP2_F2_q = four2_qty2.get()
    D_SP2_F3_q = four2_qty3.get()
    D_SP2_F4_q = four2_qty4.get()

    if four_var2.get() == 0:
        D_SP2_F1_q = 0
        D_SP2_F2_q = 0
        D_SP2_F3_q = 0
        D_SP2_F4_q = 0


    elif four_var2.get() == 1 and four2_qty1.get() == "" or four2_qty2.get() == "" or four2_qty3.get() == "" or four2_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        D_SP2_F1_q = 0
        D_SP2_F2_q = 0
        D_SP2_F3_q = 0
        D_SP2_F4_q = 0

    D_total_SP2_PEi = (float(D_SP2_F1_q) + float(D_SP2_F2_q)) * (float(D_SP2_F3_q) + float(D_SP2_F4_q))

    if D_SP2_total_frame.get() != "":
        D_SP2_total_frame.delete(0, "end")
        D_SP2_total_frame.insert("end", D_total_SP2_PEi)
    else:
        D_SP2_total_frame.insert("end", D_total_SP2_PEi)
#  ==============================================================
    D_SP3_F1_q = four3_qty1.get()
    D_SP3_F2_q = four3_qty2.get()
    D_SP3_F3_q = four3_qty3.get()
    D_SP3_F4_q = four3_qty4.get()

    if four_var3.get() == 0:
        D_SP3_F1_q = 0
        D_SP3_F2_q = 0
        D_SP3_F3_q = 0
        D_SP3_F4_q = 0

    elif four_var3.get() == 1 and four3_qty1.get() == "" or four3_qty2.get() == "" or four3_qty3.get() == "" or four3_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        D_SP3_F1_q = 0
        D_SP3_F2_q = 0
        D_SP3_F3_q = 0
        D_SP3_F4_q = 0

    D_total_SP3_PEi = (float(D_SP3_F1_q) + float(D_SP3_F2_q)) * (float(D_SP3_F3_q) + float(D_SP3_F4_q))

    if D_SP3_total_frame.get() != "":
        D_SP3_total_frame.delete(0, "end")
        D_SP3_total_frame.insert("end", D_total_SP3_PEi)
    else:
        D_SP3_total_frame.insert("end", D_total_SP3_PEi)
#  ==============================================================
    D_SP4_F1_q = four4_qty1.get()
    D_SP4_F2_q = four4_qty2.get()
    D_SP4_F3_q = four4_qty3.get()
    D_SP4_F4_q = four4_qty4.get()

    if four_var4.get() == 0:
        D_SP4_F1_q = 0
        D_SP4_F2_q = 0
        D_SP4_F3_q = 0
        D_SP4_F4_q = 0


    elif four_var4.get() == 1 and four4_qty1.get() == "" or four4_qty2.get() == "" or four4_qty3.get() == "" or four4_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        D_SP4_F1_q = 0
        D_SP4_F2_q = 0
        D_SP4_F3_q = 0
        D_SP4_F4_q = 0

    D_total_SP4_PEi = (float(D_SP4_F1_q) + float(D_SP4_F2_q)) * (float(D_SP4_F3_q) + float(D_SP4_F4_q))


    if D_SP4_total_frame.get() != "":
        D_SP4_total_frame.delete(0, "end")
        D_SP4_total_frame.insert("end", D_total_SP4_PEi)
    else:
        D_SP4_total_frame.insert("end", D_total_SP4_PEi)

    total_SP_all_PEi = D_total_SP1_PEi + D_total_SP2_PEi + D_total_SP3_PEi + D_total_SP4_PEi

    if D_SP_all_total_frame.get() != "":
        D_SP_all_total_frame.delete(0, "end")
        D_SP_all_total_frame.insert("end", total_SP_all_PEi)
    else:
        D_SP_all_total_frame.insert("end", total_SP_all_PEi)

# five*****************************************************************************
def five1_chk():
    if five_var1.get() == 1:
        five1_qty1['state'] = "normal"
        five1_qty1['bg'] = '#248aa2'
        five1_qty1['fg'] = "white"
        five1_qty2['state'] = "normal"
        five1_qty2['bg'] = '#248aa2'
        five1_qty2['fg'] = "white"
        five1_qty3['state'] = "normal"
        five1_qty3['bg'] = '#248aa2'
        five1_qty3['fg'] = "white"

    else:
        five1_qty1['state'] = "disabled"
        five1_qty2['state'] = "disabled"
        five1_qty3['state'] = "disabled"

def five2_chk():
    if five_var2.get() == 1:
        five2_qty1['state'] = "normal"
        five2_qty1['bg'] = '#248aa2'
        five2_qty1['fg'] = "white"
        five2_qty2['state'] = "normal"
        five2_qty2['bg'] = '#248aa2'
        five2_qty2['fg'] = "white"
        five2_qty3['state'] = "normal"
        five2_qty3['bg'] = '#248aa2'
        five2_qty3['fg'] = "white"
    else:
        five2_qty1['state'] = "disabled"
        five2_qty2['state'] = "disabled"
        five2_qty3['state'] = "disabled"

def five3_chk():
    if five_var3.get() == 1:
        five3_qty1['state'] = "normal"
        five3_qty1['bg'] = '#248aa2'
        five3_qty1['fg'] = "white"
        five3_qty2['state'] = "normal"
        five3_qty2['bg'] = '#248aa2'
        five3_qty2['fg'] = "white"
        five3_qty3['state'] = "normal"
        five3_qty3['bg'] = '#248aa2'
        five3_qty3['fg'] = "white"
    else:
        five3_qty1['state'] = "disabled"
        five3_qty2['state'] = "disabled"
        five3_qty3['state'] = "disabled"

def five4_chk():
    if five_var4.get() == 1:
        five4_qty1['state'] = "normal"
        five4_qty1['bg'] = '#248aa2'
        five4_qty1['fg'] = "white"
        five4_qty2['state'] = "normal"
        five4_qty2['bg'] = '#248aa2'
        five4_qty2['fg'] = "white"
        five4_qty3['state'] = "normal"
        five4_qty3['bg'] = '#248aa2'
        five4_qty3['fg'] = "white"
    else:
        five4_qty1['state'] = "disabled"
        five4_qty2['state'] = "disabled"
        five4_qty3['state'] = "disabled"

def stableE_1():
    E_SP1_F1_q = five1_qty1.get()
    E_SP1_F2_q = five1_qty2.get()
    E_SP1_F3_q = five1_qty3.get()

    if five_var1.get() == 0:
        E_SP1_F1_q = 0
        E_SP1_F2_q = 0
        E_SP1_F3_q = 0

    elif five_var1.get() == 1 and five1_qty1.get() == "" or five1_qty2.get() == "" or five1_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        E_SP1_F1_q = 0
        E_SP1_F2_q = 0
        E_SP1_F3_q = 0

    E_total_SP1_REi = (float(E_SP1_F1_q) * (float(E_SP1_F2_q) - float(E_SP1_F3_q)) * 44/12)

    if E_SP1_total_frame.get() != "":
        E_SP1_total_frame.delete(0, "end")
        E_SP1_total_frame.insert("end", E_total_SP1_REi)
    else:
        E_SP1_total_frame.insert("end", E_total_SP1_REi)
#  ==============================================================
    E_SP2_F1_q = five2_qty1.get()
    E_SP2_F2_q = five2_qty2.get()
    E_SP2_F3_q = five2_qty3.get()

    if five_var2.get() == 0:
        E_SP2_F1_q = 0
        E_SP2_F2_q = 0
        E_SP2_F3_q = 0

    elif five_var2.get() == 1 and five2_qty1.get() == "" or five2_qty2.get() == "" or five2_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        E_SP2_F1_q = 0
        E_SP2_F2_q = 0
        E_SP2_F3_q = 0

    E_total_SP2_REi = (float(E_SP2_F1_q) * (float(E_SP2_F2_q) - float(E_SP2_F3_q)) * 44/12)

    if E_SP2_total_frame.get() != "":
        E_SP2_total_frame.delete(0, "end")
        E_SP2_total_frame.insert("end", E_total_SP2_REi)
    else:
        E_SP2_total_frame.insert("end", E_total_SP2_REi)
#  ==============================================================
    E_SP3_F1_q = five3_qty1.get()
    E_SP3_F2_q = five3_qty2.get()
    E_SP3_F3_q = five3_qty3.get()


    if five_var3.get() == 0:
        E_SP3_F1_q = 0
        E_SP3_F2_q = 0
        E_SP3_F3_q = 0

    elif five_var3.get() == 1 and five3_qty1.get() == "" or five3_qty2.get() == "" or five3_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        E_SP3_F1_q = 0
        E_SP3_F2_q = 0
        E_SP3_F3_q = 0

    E_total_SP3_REi = (float(E_SP3_F1_q) * (float(E_SP3_F2_q) - float(E_SP3_F3_q)) * 44/12)

    if E_SP3_total_frame.get() != "":
        E_SP3_total_frame.delete(0, "end")
        E_SP3_total_frame.insert("end", E_total_SP3_REi)
    else:
        E_SP3_total_frame.insert("end", E_total_SP3_REi)
#  ==============================================================
    E_SP4_F1_q = five4_qty1.get()
    E_SP4_F2_q = five4_qty2.get()
    E_SP4_F3_q = five4_qty3.get()

    if five_var4.get() == 0:
        E_SP4_F1_q = 0
        E_SP4_F2_q = 0
        E_SP4_F3_q = 0

    elif five_var4.get() == 1 and five4_qty1.get() == "" or five4_qty2.get() == "" or five4_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        E_SP4_F1_q = 0
        E_SP4_F2_q = 0
        E_SP4_F3_q = 0
    E_total_SP4_REi = (float(E_SP4_F1_q) * (float(E_SP4_F2_q) - float(E_SP4_F3_q)) * 44/12)


    if E_SP4_total_frame.get() != "":
        E_SP4_total_frame.delete(0, "end")
        E_SP4_total_frame.insert("end", E_total_SP4_REi)
    else:
        E_SP4_total_frame.insert("end", E_total_SP4_REi)

    total_SP_all_REi = E_total_SP1_REi + E_total_SP2_REi + E_total_SP3_REi + E_total_SP4_REi

    if E_SP_all_total_frame.get() != "":
        E_SP_all_total_frame.delete(0, "end")
        E_SP_all_total_frame.insert("end", total_SP_all_REi)
    else:
        E_SP_all_total_frame.insert("end", total_SP_all_REi)
# six*****************************************************************************

def six1_chk():
    if six_var1.get() == 1:
        six1_qty1['state'] = "normal"
        six1_qty1['bg'] = '#248aa2'
        six1_qty1['fg'] = "white"
        six1_qty2['state'] = "normal"
        six1_qty2['bg'] = '#248aa2'
        six1_qty2['fg'] = "white"
        six1_qty3['state'] = "normal"
        six1_qty3['bg'] = '#248aa2'
        six1_qty3['fg'] = "white"

    else:
        six1_qty1['state'] = "disabled"
        six1_qty2['state'] = "disabled"
        six1_qty3['state'] = "disabled"

def six2_chk():
    if six_var2.get() == 1:
        six2_qty1['state'] = "normal"
        six2_qty1['bg'] = '#248aa2'
        six2_qty1['fg'] = "white"
        six2_qty2['state'] = "normal"
        six2_qty2['bg'] = '#248aa2'
        six2_qty2['fg'] = "white"
        six2_qty3['state'] = "normal"
        six2_qty3['bg'] = '#248aa2'
        six2_qty3['fg'] = "white"
    else:
        six2_qty1['state'] = "disabled"
        six2_qty2['state'] = "disabled"
        six2_qty3['state'] = "disabled"

def six3_chk():
    if six_var3.get() == 1:
        six3_qty1['state'] = "normal"
        six3_qty1['bg'] = '#248aa2'
        six3_qty1['fg'] = "white"
        six3_qty2['state'] = "normal"
        six3_qty2['bg'] = '#248aa2'
        six3_qty2['fg'] = "white"
        six3_qty3['state'] = "normal"
        six3_qty3['bg'] = '#248aa2'
        six3_qty3['fg'] = "white"
    else:
        six3_qty1['state'] = "disabled"
        six3_qty2['state'] = "disabled"
        six3_qty3['state'] = "disabled"

def six4_chk():
    if six_var4.get() == 1:
        six4_qty1['state'] = "normal"
        six4_qty1['bg'] = '#248aa2'
        six4_qty1['fg'] = "white"
        six4_qty2['state'] = "normal"
        six4_qty2['bg'] = '#248aa2'
        six4_qty2['fg'] = "white"
        six4_qty3['state'] = "normal"
        six4_qty3['bg'] = '#248aa2'
        six4_qty3['fg'] = "white"
    else:
        six4_qty1['state'] = "disabled"
        six4_qty2['state'] = "disabled"
        six4_qty3['state'] = "disabled"

def stableF_1():
    F_SP1_F1_q = six1_qty1.get()
    F_SP1_F2_q = six1_qty2.get()
    F_SP1_F3_q = six1_qty3.get()

    if six_var1.get() == 0:
        F_SP1_F1_q = 0
        F_SP1_F2_q = 0
        F_SP1_F3_q = 0

    elif six_var1.get() == 1 and six1_qty1.get() == "" or six1_qty2.get() == "" or six1_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        F_SP1_F1_q = 0
        F_SP1_F2_q = 0
        F_SP1_F3_q = 0

    F_total_SP1_HEi = ((float(F_SP1_F1_q) * float(F_SP1_F2_q)) * 44/12) - float(F_SP1_F3_q)

    if F_SP1_total_frame.get() != "":
        F_SP1_total_frame.delete(0, "end")
        F_SP1_total_frame.insert("end", F_total_SP1_HEi)
    else:
        F_SP1_total_frame.insert("end", F_total_SP1_HEi)
#  ==============================================================
    F_SP2_F1_q = six2_qty1.get()
    F_SP2_F2_q = six2_qty2.get()
    F_SP2_F3_q = six2_qty3.get()

    if six_var2.get() == 0:
        F_SP2_F1_q = 0
        F_SP2_F2_q = 0
        F_SP2_F3_q = 0

    elif six_var2.get() == 1 and six2_qty1.get() == "" or six2_qty2.get() == "" or six2_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        F_SP2_F1_q = 0
        F_SP2_F2_q = 0
        F_SP2_F3_q = 0

    F_total_SP2_HEi = ((float(F_SP2_F1_q) * float(F_SP2_F2_q)) * 44/12) - float(F_SP2_F3_q)

    if F_SP2_total_frame.get() != "":
        F_SP2_total_frame.delete(0, "end")
        F_SP2_total_frame.insert("end", F_total_SP2_HEi)
    else:
        F_SP2_total_frame.insert("end", F_total_SP2_HEi)
#  ==============================================================
    F_SP3_F1_q = six3_qty1.get()
    F_SP3_F2_q = six3_qty2.get()
    F_SP3_F3_q = six3_qty3.get()


    if six_var3.get() == 0:
        F_SP3_F1_q = 0
        F_SP3_F2_q = 0
        F_SP3_F3_q = 0

    elif six_var3.get() == 1 and six3_qty1.get() == "" or six3_qty2.get() == "" or six3_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        F_SP3_F1_q = 0
        F_SP3_F2_q = 0
        F_SP3_F3_q = 0

    F_total_SP3_HEi = ((float(F_SP3_F1_q) * float(F_SP3_F2_q)) * 44/12) - float(F_SP3_F3_q)

    if F_SP3_total_frame.get() != "":
        F_SP3_total_frame.delete(0, "end")
        F_SP3_total_frame.insert("end", F_total_SP3_HEi)
    else:
        F_SP3_total_frame.insert("end", F_total_SP3_HEi)
#  ==============================================================
    F_SP4_F1_q = six4_qty1.get()
    F_SP4_F2_q = six4_qty2.get()
    F_SP4_F3_q = six4_qty3.get()

    if six_var4.get() == 0:
        F_SP4_F1_q = 0
        F_SP4_F2_q = 0
        F_SP4_F3_q = 0

    elif six_var4.get() == 1 and six4_qty1.get() == "" or six4_qty2.get() == "" or six4_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        F_SP4_F1_q = 0
        F_SP4_F2_q = 0
        F_SP4_F3_q = 0
    F_total_SP4_HEi = (float(F_SP4_F1_q) * (float(F_SP4_F2_q) - float(F_SP4_F3_q)) * 44/12)


    if F_SP4_total_frame.get() != "":
        F_SP4_total_frame.delete(0, "end")
        F_SP4_total_frame.insert("end", F_total_SP4_HEi)
    else:
        F_SP4_total_frame.insert("end", F_total_SP4_HEi)

    total_SP_all_HEi = F_total_SP1_HEi + F_total_SP2_HEi + F_total_SP3_HEi + F_total_SP4_HEi

    if F_SP_all_total_frame.get() != "":
        F_SP_all_total_frame.delete(0, "end")
        F_SP_all_total_frame.insert("end", total_SP_all_HEi)
    else:
        F_SP_all_total_frame.insert("end", total_SP_all_HEi)

# seven*****************************************************************************

def seven1_chk():
    if seven_var1.get() == 1:
        seven1_qty1['state'] = "normal"
        seven1_qty1['bg'] = '#248aa2'
        seven1_qty1['fg'] = "white"
        seven1_qty2['state'] = "normal"
        seven1_qty2['bg'] = '#248aa2'
        seven1_qty2['fg'] = "white"
        seven1_qty3['state'] = "normal"
        seven1_qty3['bg'] = '#248aa2'
        seven1_qty3['fg'] = "white"
        seven1_qty4['state'] = "normal"
        seven1_qty4['bg'] = '#248aa2'
        seven1_qty4['fg'] = "white"
        seven1_qty5['state'] = "normal"
        seven1_qty5['bg'] = '#248aa2'
        seven1_qty5['fg'] = "white"

    else:
        seven1_qty1['state'] = "disabled"
        seven1_qty2['state'] = "disabled"
        seven1_qty3['state'] = "disabled"
        seven1_qty4['state'] = "disabled"
        seven1_qty5['state'] = "disabled"

def seven2_chk():
    if seven_var2.get() == 1:
        seven2_qty1['state'] = "normal"
        seven2_qty1['bg'] = '#248aa2'
        seven2_qty1['fg'] = "white"
        seven2_qty2['state'] = "normal"
        seven2_qty2['bg'] = '#248aa2'
        seven2_qty2['fg'] = "white"
        seven2_qty3['state'] = "normal"
        seven2_qty3['bg'] = '#248aa2'
        seven2_qty3['fg'] = "white"
        seven2_qty4['state'] = "normal"
        seven2_qty4['bg'] = '#248aa2'
        seven2_qty4['fg'] = "white"
        seven2_qty5['state'] = "normal"
        seven2_qty5['bg'] = '#248aa2'
        seven2_qty5['fg'] = "white"
    else:
        seven2_qty1['state'] = "disabled"
        seven2_qty2['state'] = "disabled"
        seven2_qty3['state'] = "disabled"
        seven2_qty4['state'] = "disabled"
        seven2_qty5['state'] = "disabled"
def seven3_chk():
    if seven_var3.get() == 1:
        seven3_qty1['state'] = "normal"
        seven3_qty1['bg'] = '#248aa2'
        seven3_qty1['fg'] = "white"
        seven3_qty2['state'] = "normal"
        seven3_qty2['bg'] = '#248aa2'
        seven3_qty2['fg'] = "white"
        seven3_qty3['state'] = "normal"
        seven3_qty3['bg'] = '#248aa2'
        seven3_qty3['fg'] = "white"
        seven3_qty4['state'] = "normal"
        seven3_qty4['bg'] = '#248aa2'
        seven3_qty4['fg'] = "white"
        seven3_qty5['state'] = "normal"
        seven3_qty5['bg'] = '#248aa2'
        seven3_qty5['fg'] = "white"
    else:
        seven3_qty1['state'] = "disabled"
        seven3_qty2['state'] = "disabled"
        seven3_qty3['state'] = "disabled"
        seven3_qty4['state'] = "disabled"
        seven3_qty5['state'] = "disabled"
def seven4_chk():
    if seven_var4.get() == 1:
        seven4_qty1['state'] = "normal"
        seven4_qty1['bg'] = '#248aa2'
        seven4_qty1['fg'] = "white"
        seven4_qty2['state'] = "normal"
        seven4_qty2['bg'] = '#248aa2'
        seven4_qty2['fg'] = "white"
        seven4_qty3['state'] = "normal"
        seven4_qty3['bg'] = '#248aa2'
        seven4_qty3['fg'] = "white"
        seven4_qty4['state'] = "normal"
        seven4_qty4['bg'] = '#248aa2'
        seven4_qty4['fg'] = "white"
        seven4_qty5['state'] = "normal"
        seven4_qty5['bg'] = '#248aa2'
        seven4_qty5['fg'] = "white"
    else:
        seven4_qty1['state'] = "disabled"
        seven4_qty2['state'] = "disabled"
        seven4_qty3['state'] = "disabled"
        seven4_qty4['state'] = "disabled"
        seven4_qty5['state'] = "disabled"
def stableG_1():
    G_SP1_F1_q = seven1_qty1.get()
    G_SP1_F2_q = seven1_qty2.get()
    G_SP1_F3_q = seven1_qty3.get()
    G_SP1_F4_q = seven1_qty4.get()
    G_SP1_F5_q = seven1_qty5.get()

    if seven_var1.get() == 0:
        G_SP1_F1_q = 0
        G_SP1_F2_q = 0
        G_SP1_F3_q = 0
        G_SP1_F4_q = 0
        G_SP1_F5_q = 0
    elif seven_var1.get() == 1 and seven1_qty1.get() == "" or seven1_qty2.get() == "" or seven1_qty3.get() == "" or seven1_qty4.get() == "" or seven1_qty5.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        G_SP1_F1_q = 0
        G_SP1_F2_q = 0
        G_SP1_F3_q = 0
        G_SP1_F4_q = 0
        G_SP1_F5_q = 0

    G_total_SP1_HEi = (float(G_SP1_F1_q) * float(G_SP1_F2_q) - float(G_SP1_F3_q) * float(G_SP1_F4_q))* 44/12 - float(G_SP1_F5_q)

    if G_SP1_total_frame.get() != "":
        G_SP1_total_frame.delete(0, "end")
        G_SP1_total_frame.insert("end", G_total_SP1_HEi)
    else:
        G_SP1_total_frame.insert("end", G_total_SP1_HEi)
#  ==============================================================
    G_SP2_F1_q = seven2_qty1.get()
    G_SP2_F2_q = seven2_qty2.get()
    G_SP2_F3_q = seven2_qty3.get()
    G_SP2_F4_q = seven2_qty4.get()
    G_SP2_F5_q = seven2_qty5.get()

    if seven_var2.get() == 0:
        G_SP2_F1_q = 0
        G_SP2_F2_q = 0
        G_SP2_F3_q = 0
        G_SP2_F4_q = 0
        G_SP2_F5_q = 0


    elif seven_var2.get() == 1 and seven2_qty1.get() == "" or seven2_qty2.get() == "" or seven2_qty3.get() == "" or seven2_qty4.get() == "" or seven2_qty5.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        G_SP2_F1_q = 0
        G_SP2_F2_q = 0
        G_SP2_F3_q = 0
        G_SP2_F4_q = 0
        G_SP2_F5_q = 0

    G_total_SP2_HEi = (float(G_SP2_F1_q) * float(G_SP2_F2_q) - float(G_SP2_F3_q) * float(G_SP2_F4_q))* 44/12 - float(G_SP2_F5_q)

    if G_SP2_total_frame.get() != "":
        G_SP2_total_frame.delete(0, "end")
        G_SP2_total_frame.insert("end", G_total_SP2_HEi)
    else:
        G_SP2_total_frame.insert("end", G_total_SP2_HEi)
#  ==============================================================
    G_SP3_F1_q = seven3_qty1.get()
    G_SP3_F2_q = seven3_qty2.get()
    G_SP3_F3_q = seven3_qty3.get()
    G_SP3_F4_q = seven3_qty3.get()
    G_SP3_F5_q = seven3_qty3.get()


    if seven_var3.get() == 0:
        G_SP3_F1_q = 0
        G_SP3_F2_q = 0
        G_SP3_F3_q = 0
        G_SP3_F4_q = 0
        G_SP3_F5_q = 0


    elif seven_var3.get() == 1 and seven3_qty1.get() == "" or seven3_qty2.get() == "" or seven3_qty3.get() == "" or seven3_qty4.get() == "" or seven3_qty5.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        G_SP3_F1_q = 0
        G_SP3_F2_q = 0
        G_SP3_F3_q = 0
        G_SP3_F4_q = 0
        G_SP3_F5_q = 0

    G_total_SP3_HEi = (float(G_SP3_F1_q) * float(G_SP3_F2_q) - float(G_SP3_F3_q) * float(G_SP3_F4_q))* 44/12 - float(G_SP3_F5_q)

    if G_SP3_total_frame.get() != "":
        G_SP3_total_frame.delete(0, "end")
        G_SP3_total_frame.insert("end", G_total_SP3_HEi)
    else:
        G_SP3_total_frame.insert("end", G_total_SP3_HEi)
#  ==============================================================
    G_SP4_F1_q = seven4_qty1.get()
    G_SP4_F2_q = seven4_qty2.get()
    G_SP4_F3_q = seven4_qty3.get()
    G_SP4_F4_q = seven4_qty4.get()
    G_SP4_F5_q = seven4_qty5.get()

    if seven_var4.get() == 0:
        G_SP4_F1_q = 0
        G_SP4_F2_q = 0
        G_SP4_F3_q = 0
        G_SP4_F4_q = 0
        G_SP4_F5_q = 0


    elif seven_var4.get() == 1 and seven4_qty1.get() == "" or seven4_qty2.get() == "" or seven4_qty3.get() == "" or seven4_qty4.get() == "" or seven4_qty5.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        G_SP4_F1_q = 0
        G_SP4_F2_q = 0
        G_SP4_F3_q = 0
        G_SP4_F4_q = 0
        G_SP4_F5_q = 0

    G_total_SP4_HEi = (float(G_SP4_F1_q) * float(G_SP4_F2_q) - float(G_SP4_F3_q) * float(G_SP4_F4_q))* 44/12 - float(G_SP4_F5_q)


    if G_SP4_total_frame.get() != "":
        G_SP4_total_frame.delete(0, "end")
        G_SP4_total_frame.insert("end", G_total_SP4_HEi)
    else:
        G_SP4_total_frame.insert("end", G_total_SP4_HEi)

    total_SP_all_HEi = G_total_SP1_HEi + G_total_SP2_HEi + G_total_SP3_HEi + G_total_SP4_HEi

    if G_SP_all_total_frame.get() != "":
        G_SP_all_total_frame.delete(0, "end")
        G_SP_all_total_frame.insert("end", total_SP_all_HEi)
    else:
        G_SP_all_total_frame.insert("end", total_SP_all_HEi)

# eight*****************************************************************************

def eight1_chk():
    if eight_var1.get() == 1:
        eight1_qty1['state'] = "normal"
        eight1_qty1['bg'] = '#248aa2'
        eight1_qty1['fg'] = "white"
    else:
        eight1_qty1['state'] = "disabled"

def eight2_chk():
    if eight_var2.get() == 1:
        eight2_qty1['state'] = "normal"
        eight2_qty1['bg'] = '#248aa2'
        eight2_qty1['fg'] = "white"
    else:
        eight2_qty1['state'] = "disabled"

def eight3_chk():
    if eight_var3.get() == 1:
        eight3_qty1['state'] = "normal"
        eight3_qty1['bg'] = '#248aa2'
        eight3_qty1['fg'] = "white"
    else:
        eight3_qty1['state'] = "disabled"

def eight4_chk():
    if eight_var4.get() == 1:
        eight4_qty1['state'] = "normal"
        eight4_qty1['bg'] = '#248aa2'
        eight4_qty1['fg'] = "white"
    else:
        eight4_qty1['state'] = "disabled"

def stableH_1():
    H_SP1_F1_q = eight1_qty1.get()

    if eight_var1.get() == 0:
        H_SP1_F1_q = 0

    elif eight_var1.get() == 1 and eight1_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        H_SP1_F1_q = 0

    H_total_SP1_TEi = float(H_SP1_F1_q) * 1.33 * 4.736

    if H_SP1_total_frame.get() != "":
        H_SP1_total_frame.delete(0, "end")
        H_SP1_total_frame.insert("end", H_total_SP1_TEi)
    else:
        H_SP1_total_frame.insert("end", H_total_SP1_TEi)
#  ==============================================================
    H_SP2_F1_q = eight2_qty1.get()

    if eight_var2.get() == 0:
        H_SP2_F1_q = 0

    elif eight_var2.get() == 1 and eight2_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        H_SP2_F1_q = 0

    H_total_SP2_TEi = float(H_SP2_F1_q) * 1.33 * 4.736

    if H_SP2_total_frame.get() != "":
        H_SP2_total_frame.delete(0, "end")
        H_SP2_total_frame.insert("end", H_total_SP2_TEi)
    else:
        H_SP2_total_frame.insert("end", H_total_SP2_TEi)
#  ==============================================================
    H_SP3_F1_q = eight3_qty1.get()

    if eight_var3.get() == 0:
        H_SP3_F1_q = 0

    elif eight_var3.get() == 1 and eight3_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        H_SP3_F1_q = 0

    H_total_SP3_TEi = float(H_SP3_F1_q) * 1.33 * 4.736

    if H_SP3_total_frame.get() != "":
        H_SP3_total_frame.delete(0, "end")
        H_SP3_total_frame.insert("end", H_total_SP3_TEi)
    else:
        H_SP3_total_frame.insert("end", H_total_SP3_TEi)
#  ==============================================================
    H_SP4_F1_q = eight4_qty1.get()
    if eight_var4.get() == 0:
        H_SP4_F1_q = 0

    elif eight_var4.get() == 1 and eight4_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        H_SP4_F1_q = 0

    H_total_SP4_TEi = float(H_SP4_F1_q) * 1.33 * 4.736

    if H_SP4_total_frame.get() != "":
        H_SP4_total_frame.delete(0, "end")
        H_SP4_total_frame.insert("end", H_total_SP4_TEi)
    else:
        H_SP4_total_frame.insert("end", H_total_SP4_TEi)

    total_SP_all_TEi = H_total_SP1_TEi + H_total_SP2_TEi + H_total_SP3_TEi + H_total_SP4_TEi

    if H_SP_all_total_frame.get() != "":
        H_SP_all_total_frame.delete(0, "end")
        H_SP_all_total_frame.insert("end", total_SP_all_TEi)
    else:
        H_SP_all_total_frame.insert("end", total_SP_all_TEi)

# nine*****************************************************************************

def nine1_chk():
    if nine_var1.get() == 1:
        nine1_qty1['state'] = "normal"
        nine1_qty1['bg'] = '#248aa2'
        nine1_qty1['fg'] = "white"
        nine1_qty2['state'] = "normal"
        nine1_qty2['bg'] = '#248aa2'
        nine1_qty2['fg'] = "white"
        nine1_qty3['state'] = "normal"
        nine1_qty3['bg'] = '#248aa2'
        nine1_qty3['fg'] = "white"
        nine1_qty4['state'] = "normal"
        nine1_qty4['bg'] = '#248aa2'
        nine1_qty4['fg'] = "white"

    else:
        nine1_qty1['state'] = "disabled"
        nine1_qty2['state'] = "disabled"
        nine1_qty3['state'] = "disabled"
        nine1_qty4['state'] = "disabled"

def nine2_chk():
    if nine_var2.get() == 1:
        nine2_qty1['state'] = "normal"
        nine2_qty1['bg'] = '#248aa2'
        nine2_qty1['fg'] = "white"
        nine2_qty2['state'] = "normal"
        nine2_qty2['bg'] = '#248aa2'
        nine2_qty2['fg'] = "white"
        nine2_qty3['state'] = "normal"
        nine2_qty3['bg'] = '#248aa2'
        nine2_qty3['fg'] = "white"
        nine2_qty4['state'] = "normal"
        nine2_qty4['bg'] = '#248aa2'
        nine2_qty4['fg'] = "white"
    else:
        nine2_qty1['state'] = "disabled"
        nine2_qty2['state'] = "disabled"
        nine2_qty3['state'] = "disabled"
        nine2_qty4['state'] = "disabled"
def nine3_chk():
    if nine_var3.get() == 1:
        nine3_qty1['state'] = "normal"
        nine3_qty1['bg'] = '#248aa2'
        nine3_qty1['fg'] = "white"
        nine3_qty2['state'] = "normal"
        nine3_qty2['bg'] = '#248aa2'
        nine3_qty2['fg'] = "white"
        nine3_qty3['state'] = "normal"
        nine3_qty3['bg'] = '#248aa2'
        nine3_qty3['fg'] = "white"
        nine3_qty4['state'] = "normal"
        nine3_qty4['bg'] = '#248aa2'
        nine3_qty4['fg'] = "white"
    else:
        nine3_qty1['state'] = "disabled"
        nine3_qty2['state'] = "disabled"
        nine3_qty3['state'] = "disabled"
        nine3_qty4['state'] = "disabled"
def nine4_chk():
    if nine_var4.get() == 1:
        nine4_qty1['state'] = "normal"
        nine4_qty1['bg'] = '#248aa2'
        nine4_qty1['fg'] = "white"
        nine4_qty2['state'] = "normal"
        nine4_qty2['bg'] = '#248aa2'
        nine4_qty2['fg'] = "white"
        nine4_qty3['state'] = "normal"
        nine4_qty3['bg'] = '#248aa2'
        nine4_qty3['fg'] = "white"
        nine4_qty4['state'] = "normal"
        nine4_qty4['bg'] = '#248aa2'
        nine4_qty4['fg'] = "white"
    else:
        nine4_qty1['state'] = "disabled"
        nine4_qty2['state'] = "disabled"
        nine4_qty3['state'] = "disabled"
        nine4_qty4['state'] = "disabled"
def stableI_1():
    I_SP1_F1_q = nine1_qty1.get()
    I_SP1_F2_q = nine1_qty2.get()
    I_SP1_F3_q = nine1_qty3.get()
    I_SP1_F4_q = nine1_qty4.get()

    if nine_var1.get() == 0:
        I_SP1_F1_q = 0
        I_SP1_F2_q = 0
        I_SP1_F3_q = 0
        I_SP1_F4_q = 0
    elif nine_var1.get() == 1 and nine1_qty1.get() == "" or nine1_qty2.get() == "" or nine1_qty3.get() == "" or nine1_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        I_SP1_F1_q = 0
        I_SP1_F2_q = 0
        I_SP1_F3_q = 0
        I_SP1_F4_q = 0

    I_total_SP1_GEi = (float(I_SP1_F1_q) * float(I_SP1_F2_q) - float(I_SP1_F3_q) * float(I_SP1_F4_q)) * 44/12

    if I_SP1_total_frame.get() != "":
        I_SP1_total_frame.delete(0, "end")
        I_SP1_total_frame.insert("end", I_total_SP1_GEi)
    else:
        I_SP1_total_frame.insert("end", I_total_SP1_GEi)
#  ==============================================================
    I_SP2_F1_q = nine2_qty1.get()
    I_SP2_F2_q = nine2_qty2.get()
    I_SP2_F3_q = nine2_qty3.get()
    I_SP2_F4_q = nine2_qty4.get()

    if nine_var2.get() == 0:
        I_SP2_F1_q = 0
        I_SP2_F2_q = 0
        I_SP2_F3_q = 0
        I_SP2_F4_q = 0

    elif nine_var2.get() == 1 and nine2_qty1.get() == "" or nine2_qty2.get() == "" or nine2_qty3.get() == "" or nine2_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        I_SP2_F1_q = 0
        I_SP2_F2_q = 0
        I_SP2_F3_q = 0
        I_SP2_F4_q = 0

    I_total_SP2_GEi = (float(I_SP2_F1_q) * float(I_SP2_F2_q) - float(I_SP2_F3_q) * float(I_SP2_F4_q))* 44/12

    if I_SP2_total_frame.get() != "":
        I_SP2_total_frame.delete(0, "end")
        I_SP2_total_frame.insert("end", I_total_SP2_GEi)
    else:
        I_SP2_total_frame.insert("end", I_total_SP2_GEi)
#  ==============================================================
    I_SP3_F1_q = nine3_qty1.get()
    I_SP3_F2_q = nine3_qty2.get()
    I_SP3_F3_q = nine3_qty3.get()
    I_SP3_F4_q = nine3_qty3.get()

    if nine_var3.get() == 0:
        I_SP3_F1_q = 0
        I_SP3_F2_q = 0
        I_SP3_F3_q = 0
        I_SP3_F4_q = 0
    elif nine_var3.get() == 1 and nine3_qty1.get() == "" or nine3_qty2.get() == "" or nine3_qty3.get() == "" or nine3_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        I_SP3_F1_q = 0
        I_SP3_F2_q = 0
        I_SP3_F3_q = 0
        I_SP3_F4_q = 0

    I_total_SP3_GEi = (float(I_SP3_F1_q) * float(I_SP3_F2_q) - float(I_SP3_F3_q) * float(I_SP3_F4_q))* 44/12

    if I_SP3_total_frame.get() != "":
        I_SP3_total_frame.delete(0, "end")
        I_SP3_total_frame.insert("end", I_total_SP3_GEi)
    else:
        I_SP3_total_frame.insert("end", I_total_SP3_GEi)
#  ==============================================================
    I_SP4_F1_q = nine4_qty1.get()
    I_SP4_F2_q = nine4_qty2.get()
    I_SP4_F3_q = nine4_qty3.get()
    I_SP4_F4_q = nine4_qty4.get()

    if nine_var4.get() == 0:
        I_SP4_F1_q = 0
        I_SP4_F2_q = 0
        I_SP4_F3_q = 0
        I_SP4_F4_q = 0

    elif nine_var4.get() == 1 and nine4_qty1.get() == "" or nine4_qty2.get() == "" or nine4_qty3.get() == "" or nine4_qty4.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        I_SP4_F1_q = 0
        I_SP4_F2_q = 0
        I_SP4_F3_q = 0
        I_SP4_F4_q = 0

    I_total_SP4_GEi = (float(I_SP4_F1_q) * float(I_SP4_F2_q) - float(I_SP4_F3_q) * float(I_SP4_F4_q))* 44/12

    if I_SP4_total_frame.get() != "":
        I_SP4_total_frame.delete(0, "end")
        I_SP4_total_frame.insert("end", I_total_SP4_GEi)
    else:
        I_SP4_total_frame.insert("end", I_total_SP4_GEi)

    total_SP_all_GEi = I_total_SP1_GEi + I_total_SP2_GEi + I_total_SP3_GEi + I_total_SP4_GEi

    if I_SP_all_total_frame.get() != "":
        I_SP_all_total_frame.delete(0, "end")
        I_SP_all_total_frame.insert("end", total_SP_all_GEi)
    else:
        I_SP_all_total_frame.insert("end", total_SP_all_GEi)

# ten*****************************************************************************

def ten1_chk():
    if ten_var1.get() == 1:
        ten1_qty1['state'] = "normal"
        ten1_qty1['bg'] = '#248aa2'
        ten1_qty1['fg'] = "white"
        ten1_qty2['state'] = "normal"
        ten1_qty2['bg'] = '#248aa2'
        ten1_qty2['fg'] = "white"
        ten1_qty3['state'] = "normal"
        ten1_qty3['bg'] = '#248aa2'
        ten1_qty3['fg'] = "white"
    else:
        ten1_qty1['state'] = "disabled"
        ten1_qty2['state'] = "disabled"
        ten1_qty3['state'] = "disabled"

def ten2_chk():
    if ten_var2.get() == 1:
        ten2_qty1['state'] = "normal"
        ten2_qty1['bg'] = '#248aa2'
        ten2_qty1['fg'] = "white"
        ten2_qty2['state'] = "normal"
        ten2_qty2['bg'] = '#248aa2'
        ten2_qty2['fg'] = "white"
        ten2_qty3['state'] = "normal"
        ten2_qty3['bg'] = '#248aa2'
        ten2_qty3['fg'] = "white"
    else:
        ten2_qty1['state'] = "disabled"
        ten2_qty2['state'] = "disabled"
        ten2_qty3['state'] = "disabled"

def ten3_chk():
    if ten_var3.get() == 1:
        ten3_qty1['state'] = "normal"
        ten3_qty1['bg'] = '#248aa2'
        ten3_qty1['fg'] = "white"
        ten3_qty2['state'] = "normal"
        ten3_qty2['bg'] = '#248aa2'
        ten3_qty2['fg'] = "white"
        ten3_qty3['state'] = "normal"
        ten3_qty3['bg'] = '#248aa2'
        ten3_qty3['fg'] = "white"
    else:
        ten3_qty1['state'] = "disabled"
        ten3_qty2['state'] = "disabled"
        ten3_qty3['state'] = "disabled"

def ten4_chk():
    if ten_var4.get() == 1:
        ten4_qty1['state'] = "normal"
        ten4_qty1['bg'] = '#248aa2'
        ten4_qty1['fg'] = "white"
        ten4_qty2['state'] = "normal"
        ten4_qty2['bg'] = '#248aa2'
        ten4_qty2['fg'] = "white"
        ten4_qty3['state'] = "normal"
        ten4_qty3['bg'] = '#248aa2'
        ten4_qty3['fg'] = "white"
    else:
        ten4_qty1['state'] = "disabled"
        ten4_qty2['state'] = "disabled"
        ten4_qty3['state'] = "disabled"

def stableJ_1():
    J_SP1_F1_q = ten1_qty1.get()
    J_SP1_F2_q = ten1_qty2.get()
    J_SP1_F3_q = ten1_qty3.get()

    if ten_var1.get() == 0:
        J_SP1_F1_q = 0
        J_SP1_F2_q = 0
        J_SP1_F3_q = 0

    elif ten_var1.get() == 1 and ten1_qty1.get() == "" or ten1_qty2.get() == "" or ten1_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        J_SP1_F1_q = 0
        J_SP1_F2_q = 0
        J_SP1_F3_q = 0

    J_total_SP1_GEi = float(J_SP1_F1_q) * float(J_SP1_F2_q) * 44 / 28 / 100 + float(J_SP1_F1_q) * float(J_SP1_F3_q)


    if J_SP1_total_frame.get() != "":
        J_SP1_total_frame.delete(0, "end")
        J_SP1_total_frame.insert("end", J_total_SP1_GEi)
    else:
        J_SP1_total_frame.insert("end", J_total_SP1_GEi)
#  ==============================================================
    J_SP2_F1_q = ten2_qty1.get()
    J_SP2_F2_q = ten2_qty2.get()
    J_SP2_F3_q = ten2_qty3.get()

    if ten_var2.get() == 0:
        J_SP2_F1_q = 0
        J_SP2_F2_q = 0
        J_SP2_F3_q = 0

    elif ten_var2.get() == 1 and ten2_qty1.get() == "" or ten2_qty2.get() == "" or ten2_qty3.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        J_SP2_F1_q = 0
        J_SP2_F2_q = 0
        J_SP2_F3_q = 0

    J_total_SP2_GEi = float(J_SP2_F1_q) * float(J_SP2_F2_q) * 44 / 28 / 100 + float(J_SP2_F1_q) * float(J_SP2_F3_q)

    if J_SP2_total_frame.get() != "":
        J_SP2_total_frame.delete(0, "end")
        J_SP2_total_frame.insert("end", J_total_SP2_GEi)
    else:
        J_SP2_total_frame.insert("end", J_total_SP2_GEi)
#  ==============================================================
    J_SP3_F1_q = ten3_qty1.get()
    J_SP3_F2_q = ten3_qty2.get()
    J_SP3_F3_q = ten3_qty3.get()

    if ten_var3.get() == 0:
        J_SP3_F1_q = 0
        J_SP3_F2_q = 0
        J_SP3_F3_q = 0

    elif ten_var3.get() == 1 and ten3_qty1.get() == "" or ten3_qty2.get() == "" or ten3_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        J_SP3_F1_q = 0
        J_SP3_F2_q = 0
        J_SP3_F3_q = 0


    J_total_SP3_GEi = float(J_SP3_F1_q) * float(J_SP3_F2_q) * 44 / 28 / 100 + float(J_SP3_F1_q) * float(J_SP3_F3_q)

    if J_SP3_total_frame.get() != "":
        J_SP3_total_frame.delete(0, "end")
        J_SP3_total_frame.insert("end", J_total_SP3_GEi)
    else:
        J_SP3_total_frame.insert("end", J_total_SP3_GEi)
#  ==============================================================
    J_SP4_F1_q = ten4_qty1.get()
    J_SP4_F2_q = ten4_qty2.get()
    J_SP4_F3_q = ten4_qty3.get()

    if ten_var4.get() == 0:
        J_SP4_F1_q = 0
        J_SP4_F2_q = 0
        J_SP4_F3_q = 0

    elif ten_var4.get() == 1 and ten4_qty1.get() == "" or ten4_qty2.get() == "" or ten4_qty3.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        J_SP4_F1_q = 0
        J_SP4_F2_q = 0
        J_SP4_F3_q = 0

    J_total_SP4_GEi = float(J_SP4_F1_q) * float(J_SP4_F2_q) * 44 / 28 / 100 + float(J_SP4_F1_q) * float(J_SP4_F3_q)

    if J_SP4_total_frame.get() != "":
        J_SP4_total_frame.delete(0, "end")
        J_SP4_total_frame.insert("end", J_total_SP4_GEi)
    else:
        J_SP4_total_frame.insert("end", J_total_SP4_GEi)

    total_SP_all_GEi = J_total_SP1_GEi + J_total_SP2_GEi + J_total_SP3_GEi + J_total_SP4_GEi

    if J_SP_all_total_frame.get() != "":
        J_SP_all_total_frame.delete(0, "end")
        J_SP_all_total_frame.insert("end", total_SP_all_GEi)
    else:
        J_SP_all_total_frame.insert("end", total_SP_all_GEi)

# eleven*****************************************************************************

def eleven1_chk():
    if eleven_var1.get() == 1:
        eleven1_qty1['state'] = "normal"
        eleven1_qty1['bg'] = '#248aa2'
        eleven1_qty1['fg'] = "white"
        eleven1_qty2['state'] = "normal"
        eleven1_qty2['bg'] = '#248aa2'
        eleven1_qty2['fg'] = "white"

    else:
        eleven1_qty1['state'] = "disabled"
        eleven1_qty2['state'] = "disabled"

def eleven2_chk():
    if eleven_var2.get() == 1:
        eleven2_qty1['state'] = "normal"
        eleven2_qty1['bg'] = '#248aa2'
        eleven2_qty1['fg'] = "white"
        eleven2_qty2['state'] = "normal"
        eleven2_qty2['bg'] = '#248aa2'
        eleven2_qty2['fg'] = "white"

    else:
        eleven2_qty1['state'] = "disabled"
        eleven2_qty2['state'] = "disabled"


def eleven3_chk():
    if eleven_var3.get() == 1:
        eleven3_qty1['state'] = "normal"
        eleven3_qty1['bg'] = '#248aa2'
        eleven3_qty1['fg'] = "white"
        eleven3_qty2['state'] = "normal"
        eleven3_qty2['bg'] = '#248aa2'
        eleven3_qty2['fg'] = "white"

    else:
        eleven3_qty1['state'] = "disabled"
        eleven3_qty2['state'] = "disabled"

def eleven4_chk():
    if eleven_var4.get() == 1:
        eleven4_qty1['state'] = "normal"
        eleven4_qty1['bg'] = '#248aa2'
        eleven4_qty1['fg'] = "white"
        eleven4_qty2['state'] = "normal"
        eleven4_qty2['bg'] = '#248aa2'
        eleven4_qty2['fg'] = "white"

    else:
        eleven4_qty1['state'] = "disabled"
        eleven4_qty2['state'] = "disabled"

def stableK_1():
    K_SP1_F1_q = eleven1_qty1.get()
    K_SP1_F2_q = eleven1_qty2.get()

    if eleven_var1.get() == 0:
        K_SP1_F1_q = 0
        K_SP1_F2_q = 0

    elif eleven_var1.get() == 1 and eleven1_qty1.get() == "" or eleven1_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        K_SP1_F1_q = 0
        K_SP1_F2_q = 0

    K_total_SP1_QQi = float(K_SP1_F1_q) + float(K_SP1_F2_q)


    if K_SP1_total_frame.get() != "":
        K_SP1_total_frame.delete(0, "end")
        K_SP1_total_frame.insert("end", K_total_SP1_QQi)
    else:
        K_SP1_total_frame.insert("end", K_total_SP1_QQi)
#  ==============================================================
    K_SP2_F1_q = eleven2_qty1.get()
    K_SP2_F2_q = eleven2_qty2.get()

    if eleven_var2.get() == 0:
        K_SP2_F1_q = 0
        K_SP2_F2_q = 0

    elif eleven_var2.get() == 1 and eleven2_qty1.get() == "" or eleven2_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        K_SP2_F1_q = 0
        K_SP2_F2_q = 0

    K_total_SP2_QQi = float(K_SP2_F1_q) + float(K_SP2_F2_q)

    if K_SP2_total_frame.get() != "":
        K_SP2_total_frame.delete(0, "end")
        K_SP2_total_frame.insert("end", K_total_SP2_QQi)
    else:
        K_SP2_total_frame.insert("end", K_total_SP2_QQi)
#  ==============================================================
    K_SP3_F1_q = eleven3_qty1.get()
    K_SP3_F2_q = eleven3_qty2.get()

    if eleven_var3.get() == 0:
        K_SP3_F1_q = 0
        K_SP3_F2_q = 0

    elif eleven_var3.get() == 1 and eleven3_qty1.get() == "" or eleven3_qty2.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        K_SP3_F1_q = 0
        K_SP3_F2_q = 0

    K_total_SP3_QQi = float(K_SP3_F1_q) + float(K_SP3_F2_q)

    if K_SP3_total_frame.get() != "":
        K_SP3_total_frame.delete(0, "end")
        K_SP3_total_frame.insert("end", K_total_SP3_QQi)
    else:
        K_SP3_total_frame.insert("end", K_total_SP3_QQi)
#  ==============================================================
    K_SP4_F1_q = eleven4_qty1.get()
    K_SP4_F2_q = eleven4_qty2.get()

    if eleven_var4.get() == 0:
        K_SP4_F1_q = 0
        K_SP4_F2_q = 0

    elif eleven_var4.get() == 1 and eleven4_qty1.get() == "" or eleven4_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        K_SP4_F1_q = 0
        K_SP4_F2_q = 0

    K_total_SP4_QQi = float(K_SP4_F1_q) + float(K_SP4_F2_q)

    if K_SP4_total_frame.get() != "":
        K_SP4_total_frame.delete(0, "end")
        K_SP4_total_frame.insert("end", K_total_SP4_QQi)
    else:
        K_SP4_total_frame.insert("end", K_total_SP4_QQi)

    total_SP_all_QQi = K_total_SP1_QQi + K_total_SP2_QQi + K_total_SP3_QQi + K_total_SP4_QQi

    if K_SP_all_total_frame.get() != "":
        K_SP_all_total_frame.delete(0, "end")
        K_SP_all_total_frame.insert("end", total_SP_all_QQi)
    else:
        K_SP_all_total_frame.insert("end", total_SP_all_QQi)

# twelve*****************************************************************************

def twelve1_chk():
    if twelve_var1.get() == 1:
        twelve1_qty1['state'] = "normal"
        twelve1_qty1['bg'] = '#248aa2'
        twelve1_qty1['fg'] = "white"
        twelve1_qty2['state'] = "normal"
        twelve1_qty2['bg'] = '#248aa2'
        twelve1_qty2['fg'] = "white"

    else:
        twelve1_qty1['state'] = "disabled"
        twelve1_qty2['state'] = "disabled"

def twelve2_chk():
    if twelve_var2.get() == 1:
        twelve2_qty1['state'] = "normal"
        twelve2_qty1['bg'] = '#248aa2'
        twelve2_qty1['fg'] = "white"
        twelve2_qty2['state'] = "normal"
        twelve2_qty2['bg'] = '#248aa2'
        twelve2_qty2['fg'] = "white"

    else:
        twelve2_qty1['state'] = "disabled"
        twelve2_qty2['state'] = "disabled"


def twelve3_chk():
    if twelve_var3.get() == 1:
        twelve3_qty1['state'] = "normal"
        twelve3_qty1['bg'] = '#248aa2'
        twelve3_qty1['fg'] = "white"
        twelve3_qty2['state'] = "normal"
        twelve3_qty2['bg'] = '#248aa2'
        twelve3_qty2['fg'] = "white"

    else:
        twelve3_qty1['state'] = "disabled"
        twelve3_qty2['state'] = "disabled"

def twelve4_chk():
    if twelve_var4.get() == 1:
        twelve4_qty1['state'] = "normal"
        twelve4_qty1['bg'] = '#248aa2'
        twelve4_qty1['fg'] = "white"
        twelve4_qty2['state'] = "normal"
        twelve4_qty2['bg'] = '#248aa2'
        twelve4_qty2['fg'] = "white"

    else:
        twelve4_qty1['state'] = "disabled"
        twelve4_qty2['state'] = "disabled"

def stableL_1():
    L_SP1_F1_q = twelve1_qty1.get()
    L_SP1_F2_q = twelve1_qty2.get()

    if twelve_var1.get() == 0:
        L_SP1_F1_q = 0
        L_SP1_F2_q = 0

    elif twelve_var1.get() == 1 and twelve1_qty1.get() == "" or twelve1_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        L_SP1_F1_q = 0
        L_SP1_F2_q = 0

    L_total_SP1_IE = float(L_SP1_F1_q) * float(L_SP1_F2_q)


    if L_SP1_total_frame.get() != "":
        L_SP1_total_frame.delete(0, "end")
        L_SP1_total_frame.insert("end", L_total_SP1_IE)
    else:
        L_SP1_total_frame.insert("end", L_total_SP1_IE)
#  ==============================================================
    L_SP2_F1_q = twelve2_qty1.get()
    L_SP2_F2_q = twelve2_qty2.get()

    if twelve_var2.get() == 0:
        L_SP2_F1_q = 0
        L_SP2_F2_q = 0

    elif twelve_var2.get() == 1 and twelve2_qty1.get() == "" or twelve2_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        L_SP2_F1_q = 0
        L_SP2_F2_q = 0

    L_total_SP2_IE = float(L_SP2_F1_q) * float(L_SP2_F2_q)

    if L_SP2_total_frame.get() != "":
        L_SP2_total_frame.delete(0, "end")
        L_SP2_total_frame.insert("end", L_total_SP2_IE)
    else:
        L_SP2_total_frame.insert("end", L_total_SP2_IE)
#  ==============================================================
    L_SP3_F1_q = twelve3_qty1.get()
    L_SP3_F2_q = twelve3_qty2.get()

    if twelve_var3.get() == 0:
        L_SP3_F1_q = 0
        L_SP3_F2_q = 0

    elif twelve_var3.get() == 1 and twelve3_qty1.get() == "" or twelve3_qty2.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        L_SP3_F1_q = 0
        L_SP3_F2_q = 0

    L_total_SP3_IE = float(L_SP3_F1_q) * float(L_SP3_F2_q)

    if L_SP3_total_frame.get() != "":
        L_SP3_total_frame.delete(0, "end")
        L_SP3_total_frame.insert("end", L_total_SP3_IE)
    else:
        L_SP3_total_frame.insert("end", L_total_SP3_IE)
#  ==============================================================
    L_SP4_F1_q = twelve4_qty1.get()
    L_SP4_F2_q = twelve4_qty2.get()

    if twelve_var4.get() == 0:
        L_SP4_F1_q = 0
        L_SP4_F2_q = 0

    elif twelve_var4.get() == 1 and twelve4_qty1.get() == "" or twelve4_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        L_SP4_F1_q = 0
        L_SP4_F2_q = 0

    L_total_SP4_IE = float(L_SP4_F1_q) * float(L_SP4_F2_q)

    if L_SP4_total_frame.get() != "":
        L_SP4_total_frame.delete(0, "end")
        L_SP4_total_frame.insert("end", L_total_SP4_IE)
    else:
        L_SP4_total_frame.insert("end", L_total_SP4_IE)

    total_SP_all_IE = L_total_SP1_IE + L_total_SP2_IE + L_total_SP3_IE + L_total_SP4_IE

    if L_SP_all_total_frame.get() != "":
        L_SP_all_total_frame.delete(0, "end")
        L_SP_all_total_frame.insert("end", total_SP_all_IE)
    else:
        L_SP_all_total_frame.insert("end", total_SP_all_IE)

    return total_SP_all_IE
# thirteen*****************************************************************************

def thirteen1_chk():
    if thirteen_var1.get() == 1:
        thirteen1_qty1['state'] = "normal"
        thirteen1_qty1['bg'] = '#248aa2'
        thirteen1_qty1['fg'] = "white"
        thirteen1_qty2['state'] = "normal"
        thirteen1_qty2['bg'] = '#248aa2'
        thirteen1_qty2['fg'] = "white"

    else:
        thirteen1_qty1['state'] = "disabled"
        thirteen1_qty2['state'] = "disabled"

def thirteen2_chk():
    if thirteen_var2.get() == 1:
        thirteen2_qty1['state'] = "normal"
        thirteen2_qty1['bg'] = '#248aa2'
        thirteen2_qty1['fg'] = "white"
        thirteen2_qty2['state'] = "normal"
        thirteen2_qty2['bg'] = '#248aa2'
        thirteen2_qty2['fg'] = "white"

    else:
        thirteen2_qty1['state'] = "disabled"
        thirteen2_qty2['state'] = "disabled"


def thirteen3_chk():
    if thirteen_var3.get() == 1:
        thirteen3_qty1['state'] = "normal"
        thirteen3_qty1['bg'] = '#248aa2'
        thirteen3_qty1['fg'] = "white"
        thirteen3_qty2['state'] = "normal"
        thirteen3_qty2['bg'] = '#248aa2'
        thirteen3_qty2['fg'] = "white"

    else:
        thirteen3_qty1['state'] = "disabled"
        thirteen3_qty2['state'] = "disabled"

def thirteen4_chk():
    if thirteen_var4.get() == 1:
        thirteen4_qty1['state'] = "normal"
        thirteen4_qty1['bg'] = '#248aa2'
        thirteen4_qty1['fg'] = "white"
        thirteen4_qty2['state'] = "normal"
        thirteen4_qty2['bg'] = '#248aa2'
        thirteen4_qty2['fg'] = "white"

    else:
        thirteen4_qty1['state'] = "disabled"
        thirteen4_qty2['state'] = "disabled"

def stableM_1():
    M_SP1_F1_q = thirteen1_qty1.get()
    M_SP1_F2_q = thirteen1_qty2.get()

    if thirteen_var1.get() == 0:
        M_SP1_F1_q = 0
        M_SP1_F2_q = 0

    elif thirteen_var1.get() == 1 and thirteen1_qty1.get() == "" or thirteen1_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        M_SP1_F1_q = 0
        M_SP1_F2_q = 0

    M_total_SP1_OE = float(M_SP1_F1_q) * float(M_SP1_F2_q)


    if M_SP1_total_frame.get() != "":
        M_SP1_total_frame.delete(0, "end")
        M_SP1_total_frame.insert("end", M_total_SP1_OE)
    else:
        M_SP1_total_frame.insert("end", M_total_SP1_OE)
#  ==============================================================
    M_SP2_F1_q = thirteen2_qty1.get()
    M_SP2_F2_q = thirteen2_qty2.get()

    if thirteen_var2.get() == 0:
        M_SP2_F1_q = 0
        M_SP2_F2_q = 0

    elif thirteen_var2.get() == 1 and thirteen2_qty1.get() == "" or thirteen2_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        M_SP2_F1_q = 0
        M_SP2_F2_q = 0

    M_total_SP2_OE = float(M_SP2_F1_q) * float(M_SP2_F2_q)

    if M_SP2_total_frame.get() != "":
        M_SP2_total_frame.delete(0, "end")
        M_SP2_total_frame.insert("end", M_total_SP2_OE)
    else:
        M_SP2_total_frame.insert("end", M_total_SP2_OE)
#  ==============================================================
    M_SP3_F1_q = thirteen3_qty1.get()
    M_SP3_F2_q = thirteen3_qty2.get()

    if thirteen_var3.get() == 0:
        M_SP3_F1_q = 0
        M_SP3_F2_q = 0

    elif thirteen_var3.get() == 1 and thirteen3_qty1.get() == "" or thirteen3_qty2.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        M_SP3_F1_q = 0
        M_SP3_F2_q = 0

    M_total_SP3_OE = float(M_SP3_F1_q) * float(M_SP3_F2_q)

    if M_SP3_total_frame.get() != "":
        M_SP3_total_frame.delete(0, "end")
        M_SP3_total_frame.insert("end", M_total_SP3_OE)
    else:
        M_SP3_total_frame.insert("end", M_total_SP3_OE)
#  ==============================================================
    M_SP4_F1_q = thirteen4_qty1.get()
    M_SP4_F2_q = thirteen4_qty2.get()

    if thirteen_var4.get() == 0:
        M_SP4_F1_q = 0
        M_SP4_F2_q = 0

    elif thirteen_var4.get() == 1 and thirteen4_qty1.get() == "" or thirteen4_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        M_SP4_F1_q = 0
        M_SP4_F2_q = 0

    M_total_SP4_OE = float(M_SP4_F1_q) * float(M_SP4_F2_q)
    if M_SP4_total_frame.get() != "":
        M_SP4_total_frame.delete(0, "end")
        M_SP4_total_frame.insert("end", M_total_SP4_OE)
    else:
        M_SP4_total_frame.insert("end", M_total_SP4_OE)

    total_SP_all_OE = M_total_SP1_OE + M_total_SP2_OE + M_total_SP3_OE + M_total_SP4_OE

    if M_SP_all_total_frame.get() != "":
        M_SP_all_total_frame.delete(0, "end")
        M_SP_all_total_frame.insert("end", total_SP_all_OE)
    else:
        M_SP_all_total_frame.insert("end", total_SP_all_OE)
    return total_SP_all_OE
# total ---------------------------------------------------------------
def stableLM_1():

    if stableL_1() or stableM_1() != "":
        LM = stableL_1() + stableM_1()
        if LM_SP_all_total_frame.get() != "":
            LM_SP_all_total_frame.delete(0, "end")
            LM_SP_all_total_frame.insert("end", LM)
        else:
            LM_SP_all_total_frame.insert("end", LM)


def GAS_TOTAL_chk():
    if GAS_TOTAL_var1.get() == 1:
        GAS_TOTAL_qty1['state'] = "normal"
        GAS_TOTAL_qty1['bg'] = '#248aa2'
        GAS_TOTAL_qty1['fg'] = "white"

    else:
        GAS_TOTAL_qty1['state'] = "disabled"

def Methane_chk():
    if Methane_var1.get() == 1:
        Methane_qty1['state'] = "normal"
        Methane_qty1['bg'] = '#248aa2'
        Methane_qty1['fg'] = "white"

    else:
        Methane_qty1['state'] = "disabled"

def Methane2_chk():
    if Methane_var2.get() == 1:
        Methane_qty2['state'] = "normal"
        Methane_qty2['bg'] = '#248aa2'
        Methane_qty2['fg'] = "white"

    else:
        Methane_qty2['state'] = "disabled"

def Ethane_chk():
    if Ethane_var1.get() == 1:
        Ethane_qty1['state'] = "normal"
        Ethane_qty1['bg'] = '#248aa2'
        Ethane_qty1['fg'] = "white"

    else:
        Ethane_qty1['state'] = "disabled"

def Ethane2_chk():
    if Ethane_var2.get() == 1:
        Ethane_qty2['state'] = "normal"
        Ethane_qty2['bg'] = '#248aa2'
        Ethane_qty2['fg'] = "white"

    else:
        Ethane_qty2['state'] = "disabled"

def Ethylene_chk():
    if Ethylene_var1.get() == 1:
        Ethylene_qty1['state'] = "normal"
        Ethylene_qty1['bg'] = '#248aa2'
        Ethylene_qty1['fg'] = "white"

    else:
        Ethylene_qty1['state'] = "disabled"

def Ethylene2_chk():
    if Ethylene_var2.get() == 1:
        Ethylene_qty2['state'] = "normal"
        Ethylene_qty2['bg'] = '#248aa2'
        Ethylene_qty2['fg'] = "white"

    else:
        Ethylene_qty2['state'] = "disabled"

def Propane_chk():
    if Propane_var1.get() == 1:
        Propane_qty1['state'] = "normal"
        Propane_qty1['bg'] = '#248aa2'
        Propane_qty1['fg'] = "white"

    else:
        Propane_qty1['state'] = "disabled"

def Propane2_chk():
    if Propane_var2.get() == 1:
        Propane_qty2['state'] = "normal"
        Propane_qty2['bg'] = '#248aa2'
        Propane_qty2['fg'] = "white"

    else:
        Propane_qty2['state'] = "disabled"

def Propylene_chk():
    if Propylene_var1.get() == 1:
        Propylene_qty1['state'] = "normal"
        Propylene_qty1['bg'] = '#248aa2'
        Propylene_qty1['fg'] = "white"

    else:
        Propylene_qty1['state'] = "disabled"

def Propylene2_chk():
    if Propylene_var2.get() == 1:
        Propylene_qty2['state'] = "normal"
        Propylene_qty2['bg'] = '#248aa2'
        Propylene_qty2['fg'] = "white"

    else:
        Propylene_qty2['state'] = "disabled"

def n_Butane_chk():
    if n_Butane_var1.get() == 1:
        n_Butane_qty1['state'] = "normal"
        n_Butane_qty1['bg'] = '#248aa2'
        n_Butane_qty1['fg'] = "white"

    else:
        n_Butane_qty1['state'] = "disabled"

def n_Butane2_chk():
    if n_Butane_var2.get() == 1:
        n_Butane_qty2['state'] = "normal"
        n_Butane_qty2['bg'] = '#248aa2'
        n_Butane_qty2['fg'] = "white"

    else:
        n_Butane_qty2['state'] = "disabled"

def i_Butane_chk():
    if i_Butane_var1.get() == 1:
        i_Butane_qty1['state'] = "normal"
        i_Butane_qty1['bg'] = '#248aa2'
        i_Butane_qty1['fg'] = "white"

    else:
        i_Butane_qty1['state'] = "disabled"

def i_Butane2_chk():
    if i_Butane_var2.get() == 1:
        i_Butane_qty2['state'] = "normal"
        i_Butane_qty2['bg'] = '#248aa2'
        i_Butane_qty2['fg'] = "white"

    else:
        i_Butane_qty2['state'] = "disabled"

def Butene_1_chk():
    if Butene_1_var1.get() == 1:
        Butene_1_qty1['state'] = "normal"
        Butene_1_qty1['bg'] = '#248aa2'
        Butene_1_qty1['fg'] = "white"

    else:
        Butene_1_qty1['state'] = "disabled"

def Butene2_1_chk():
    if Butene_1_var2.get() == 1:
        Butene_1_qty2['state'] = "normal"
        Butene_1_qty2['bg'] = '#248aa2'
        Butene_1_qty2['fg'] = "white"

    else:
        Butene_1_qty2['state'] = "disabled"

def i_Butene_chk():
    if i_Butene_var1.get() == 1:
        i_Butene_qty1['state'] = "normal"
        i_Butene_qty1['bg'] = '#248aa2'
        i_Butene_qty1['fg'] = "white"

    else:
        i_Butene_qty1['state'] = "disabled"

def i_Butene2_chk():
    if i_Butene_var2.get() == 1:
        i_Butene_qty2['state'] = "normal"
        i_Butene_qty2['bg'] = '#248aa2'
        i_Butene_qty2['fg'] = "white"

    else:
        i_Butene_qty2['state'] = "disabled"

def ct_Butene_chk():
    if ct_Butene_var1.get() == 1:
        ct_Butene_qty1['state'] = "normal"
        ct_Butene_qty1['bg'] = '#248aa2'
        ct_Butene_qty1['fg'] = "white"

    else:
        ct_Butene_qty1['state'] = "disabled"

def ct_Butene2_chk():
    if ct_Butene_var2.get() == 1:
        ct_Butene_qty2['state'] = "normal"
        ct_Butene_qty2['bg'] = '#248aa2'
        ct_Butene_qty2['fg'] = "white"

    else:
        ct_Butene_qty2['state'] = "disabled"

def Pentane_chk():
    if Pentane_var1.get() == 1:
        Pentane_qty1['state'] = "normal"
        Pentane_qty1['bg'] = '#248aa2'
        Pentane_qty1['fg'] = "white"

    else:
        Pentane_qty1['state'] = "disabled"

def Pentane2_chk():
    if Pentane_var2.get() == 1:
        Pentane_qty2['state'] = "normal"
        Pentane_qty2['bg'] = '#248aa2'
        Pentane_qty2['fg'] = "white"

    else:
        Pentane_qty2['state'] = "disabled"

def stable_GAS_TOTAL_MASS_CACULATION():
    GAS_TOTAL_F1_q = GAS_TOTAL_qty1.get()

    if GAS_TOTAL_var1.get() == 0:
        GAS_TOTAL_F1_q = 0

    elif GAS_TOTAL_var1.get() == 1 and GAS_TOTAL_qty1.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        GAS_TOTAL_F1_q = 0
#  Methane==============================================================
    Methane_F1_q = Methane_qty1.get()

    if Methane_var1.get() == 0:
        Methane_F1_q = 0

    elif Methane_var1.get() == 1 and Methane_qty1.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        Methane_F1_q = 0

    #  Ethane==============================================================
    Ethane_F1_q = Ethane_qty1.get()

    if Ethane_var1.get() == 0:
        Ethane_F1_q = 0
    elif Ethane_var1.get() == 1 and Ethane_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Ethane_F1_q = 0

    #  Ethylene==============================================================
    Ethylene_F1_q = Ethylene_qty1.get()

    if Ethylene_var1.get() == 0:
        Ethylene_F1_q = 0
    elif Ethylene_var1.get() == 1 and Ethylene_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Ethylene_F1_q = 0

    #  Propane==============================================================
    Propane_F1_q = Propane_qty1.get()

    if Propane_var1.get() == 0:
        Propane_F1_q = 0
    elif Propane_var1.get() == 1 and Propane_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Propane_F1_q = 0

    #  Propylene==============================================================
    Propylene_F1_q = Propylene_qty1.get()

    if Propylene_var1.get() == 0:
        Propylene_F1_q = 0
    elif Propylene_var1.get() == 1 and Propylene_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Propylene_F1_q = 0

    #  n-Butane==============================================================
    n_Butane_F1_q = n_Butane_qty1.get()

    if n_Butane_var1.get() == 0:
        n_Butane_F1_q = 0
    elif n_Butane_var1.get() == 1 and n_Butane_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        n_Butane_F1_q = 0

    #  i-Butane==============================================================
    i_Butane_F1_q = i_Butane_qty1.get()

    if i_Butane_var1.get() == 0:
        i_Butane_F1_q = 0
    elif i_Butane_var1.get() == 1 and i_Butane_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        i_Butane_F1_q = 0

    #  Butene-1==============================================================
    Butene_1_F1_q = Butene_1_qty1.get()

    if Butene_1_var1.get() == 0:
        Butene_1_F1_q = 0
    elif Butene_1_var1.get() == 1 and Butene_1_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Butene_1_F1_q = 0

    #  i-Butene==============================================================
    i_Butene_F1_q = i_Butene_qty1.get()

    if i_Butene_var1.get() == 0:
        i_Butene_F1_q = 0
    elif i_Butene_var1.get() == 1 and i_Butene_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        i_Butene_F1_q = 0

    #  cis-trans-Butene==============================================================
    ct_Butene_F1_q = ct_Butene_qty1.get()

    if ct_Butene_var1.get() == 0:
        ct_Butene_F1_q = 0
    elif ct_Butene_var1.get() == 1 and ct_Butene_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        ct_Butene_F1_q = 0

    #  Pentane-==============================================================
    Pentane_F1_q = Pentane_qty1.get()

    if Pentane_var1.get() == 0:
        Pentane_F1_q = 0
    elif Pentane_var1.get() == 1 and Pentane_qty1.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Pentane_F1_q = 0

    Total_gas = float(GAS_TOTAL_F1_q)
    CH4_1_CO2 = Total_gas * float(Methane_F1_q) * 0.01 * 2.75
    C2H6_1_CO2 = Total_gas * float(Ethane_F1_q) * 0.01 * 2.933333
    C2H4_1_CO2 = Total_gas * float(Ethylene_F1_q) * 0.01 * 3.142857
    C3H8_1_CO2 = Total_gas * float(Propane_F1_q) * 0.01 * 3
    C3H6_1_CO2 = Total_gas * float(Propylene_F1_q) * 0.01 * 3.142857
    C4H10_1_CO2 = Total_gas * float(n_Butane_F1_q) * 0.01 * 3.034483
    C4H10_2_CO2 = Total_gas * float(i_Butane_F1_q) * 0.01 * 3.034483
    C4H8_1_CO2 = Total_gas * float(Butene_1_F1_q) * 0.01 * 3.142857
    C4H8_2_CO2 = Total_gas * float(i_Butene_F1_q) * 0.01 * 3.142857
    C4H8_3_CO2 = Total_gas * float(ct_Butene_F1_q) * 0.01 * 3.142857
    C5H12_1_CO2 = Total_gas * float(Pentane_F1_q) * 0.01 * 3.055556



    GAS_SPECIES_CARBON_total = CH4_1_CO2 + C2H6_1_CO2 + C2H4_1_CO2 + C3H8_1_CO2 + C3H6_1_CO2 +\
                               C4H10_1_CO2 + C4H10_2_CO2 + C4H8_1_CO2 + C4H8_2_CO2 + C4H8_3_CO2 +C5H12_1_CO2

    signal = float(Methane_F1_q) + float(Ethane_F1_q) + float(Ethylene_F1_q) + float(Propane_F1_q) + \
             float(Propylene_F1_q) + float(n_Butane_F1_q) + float(i_Butane_F1_q) +float(Butene_1_F1_q) + \
             float(i_Butene_F1_q) + float(ct_Butene_F1_q) + float(Pentane_F1_q)
    if signal <= 100:
        if GAS_SPECIES_CARBON_total_frame.get() != "":
            GAS_SPECIES_CARBON_total_frame.delete(0, "end")
            GAS_SPECIES_CARBON_total_frame.insert("end", GAS_SPECIES_CARBON_total)
        else:
            GAS_SPECIES_CARBON_total_frame.insert("end", GAS_SPECIES_CARBON_total)
        return GAS_SPECIES_CARBON_total
    else:
        messagebox.showerror("error", "please confirm the sum of mass fractions is less than 100!")

def stable_GAS_TOTAL_VOLUMN_CACULATION():
    GAS_TOTAL_F1_q = GAS_TOTAL_qty1.get()

    if GAS_TOTAL_var1.get() == 0:
        GAS_TOTAL_F1_q = 0

    elif GAS_TOTAL_var1.get() == 1 and GAS_TOTAL_qty1.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        GAS_TOTAL_F1_q = 0
#  Methane==============================================================
    Methane_F1_q2 = Methane_qty2.get()

    if Methane_var2.get() == 0:
        Methane_F1_q2 = 0

    elif Methane_var2.get() == 1 and Methane_qty2.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        Methane_F1_q2 = 0

    #  Ethane==============================================================
    Ethane_F1_q2 = Ethane_qty2.get()

    if Ethane_var2.get() == 0:
        Ethane_F1_q2 = 0
    elif Ethane_var2.get() == 1 and Ethane_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Ethane_F1_q2 = 0

    #  Ethylene==============================================================
    Ethylene_F1_q2 = Ethylene_qty2.get()

    if Ethylene_var2.get() == 0:
        Ethylene_F1_q2 = 0
    elif Ethylene_var2.get() == 1 and Ethylene_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Ethylene_F1_q2 = 0

    #  Propane==============================================================
    Propane_F1_q2 = Propane_qty2.get()

    if Propane_var2.get() == 0:
        Propane_F1_q2 = 0
    elif Propane_var2.get() == 1 and Propane_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Propane_F1_q2 = 0

    #  Propylene==============================================================
    Propylene_F1_q2 = Propylene_qty2.get()

    if Propylene_var2.get() == 0:
        Propylene_F1_q2 = 0
    elif Propylene_var2.get() == 1 and Propylene_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Propylene_F1_q2 = 0

    #  n-Butane==============================================================
    n_Butane_F1_q2 = n_Butane_qty2.get()

    if n_Butane_var2.get() == 0:
        n_Butane_F1_q2 = 0
    elif n_Butane_var2.get() == 1 and n_Butane_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        n_Butane_F1_q2 = 0

    #  i-Butane==============================================================
    i_Butane_F1_q2 = i_Butane_qty2.get()

    if i_Butane_var2.get() == 0:
        i_Butane_F1_q2 = 0
    elif i_Butane_var2.get() == 1 and i_Butane_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        i_Butane_F1_q2 = 0

    #  Butene-1==============================================================
    Butene_1_F1_q2 = Butene_1_qty2.get()

    if Butene_1_var2.get() == 0:
        Butene_1_F1_q2 = 0
    elif Butene_1_var2.get() == 1 and Butene_1_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Butene_1_F1_q2 = 0

    #  i-Butene==============================================================
    i_Butene_F1_q2 = i_Butene_qty2.get()

    if i_Butene_var2.get() == 0:
        i_Butene_F1_q2 = 0
    elif i_Butene_var2.get() == 1 and i_Butene_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        i_Butene_F1_q2 = 0

    #  cis-trans-Butene==============================================================
    ct_Butene_F1_q2 = ct_Butene_qty2.get()

    if ct_Butene_var2.get() == 0:
        ct_Butene_F1_q2 = 0
    elif ct_Butene_var2.get() == 1 and ct_Butene_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        ct_Butene_F1_q2 = 0

    #  Pentane-==============================================================
    Pentane_F1_q2 = Pentane_qty2.get()

    if Pentane_var2.get() == 0:
        Pentane_F1_q2 = 0
    elif Pentane_var2.get() == 1 and Pentane_qty2.get() == "":
        messagebox.showerror("error", "please fill the quantity!")
        Pentane_F1_q2 = 0

    Total_gas = float(GAS_TOTAL_F1_q)
    CH4_1_CO2_2 = Total_gas * float(Methane_F1_q2) * 0.01 * 2.75
    C2H6_1_CO2_2 = Total_gas * float(Ethane_F1_q2) * 0.01 * 2.933333
    C2H4_1_CO2_2 = Total_gas * float(Ethylene_F1_q2) * 0.01 * 3.142857
    C3H8_1_CO2_2 = Total_gas * float(Propane_F1_q2) * 0.01 * 3
    C3H6_1_CO2_2 = Total_gas * float(Propylene_F1_q2) * 0.01 * 3.142857
    C4H10_1_CO2_2 = Total_gas * float(n_Butane_F1_q2) * 0.01 * 3.034483
    C4H10_2_CO2_2 = Total_gas * float(i_Butane_F1_q2) * 0.01 * 3.034483
    C4H8_1_CO2_2 = Total_gas * float(Butene_1_F1_q2) * 0.01 * 3.142857
    C4H8_2_CO2_2 = Total_gas * float(i_Butene_F1_q2) * 0.01 * 3.142857
    C4H8_3_CO2_2 = Total_gas * float(ct_Butene_F1_q2) * 0.01 * 3.142857
    C5H12_1_CO2_2 = Total_gas * float(Pentane_F1_q2) * 0.01 * 3.055556



    GAS_SPECIES_CARBON_total_2 = CH4_1_CO2_2 + C2H6_1_CO2_2 + C2H4_1_CO2_2 + C3H8_1_CO2_2 + C3H6_1_CO2_2 +\
                               C4H10_1_CO2_2 + C4H10_2_CO2_2 + C4H8_1_CO2_2 + C4H8_2_CO2_2 + C4H8_3_CO2_2 +C5H12_1_CO2_2

    signal_2 = float(Methane_F1_q2) + float(Ethane_F1_q2) + float(Ethylene_F1_q2) + float(Propane_F1_q2) + \
             float(Propylene_F1_q2) + float(n_Butane_F1_q2) + float(i_Butane_F1_q2) +float(Butene_1_F1_q2) + \
             float(i_Butene_F1_q2) + float(ct_Butene_F1_q2) + float(Pentane_F1_q2)
    if signal_2 <= 100:
        if GAS_SPECIES_CARBON_total2_frame.get() != "":
            GAS_SPECIES_CARBON_total2_frame.delete(0, "end")
            GAS_SPECIES_CARBON_total2_frame.insert("end", GAS_SPECIES_CARBON_total_2)
        else:
            GAS_SPECIES_CARBON_total2_frame.insert("end", GAS_SPECIES_CARBON_total_2)
        return GAS_SPECIES_CARBON_total2
    else:
        messagebox.showerror("error", "please confirm the sum of mass fractions is less than 100!")
def water_chk():
    if water_var.get() == 1:
        water_qty1['state'] = "normal"
        water_qty1['bg'] = '#248aa2'
        water_qty1['fg'] = "white"
        water_qty2['state'] = "normal"
        water_qty2['bg'] = '#248aa2'
        water_qty2['fg'] = "white"
        water_qty3['state'] = "normal"
        water_qty3['bg'] = '#248aa2'
        water_qty3['fg'] = "white"
    else:
        water_qty1['state'] = "disabled"
        water_qty2['state'] = "disabled"
        water_qty3['state'] = "disabled"

def water_func():
    water_pressure_q = water_qty1.get()
    water_tempeature_q = water_qty2.get()
    water_mass_q = water_qty3.get()

    if water_var.get() == 0:
        water_pressure_q = 0
        water_tempeature_q = 0
        water_mass_q = 0

    elif water_var.get() == 1 and water_qty1.get() == "" or water_qty2.get() == "" or water_qty3.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        water_pressure_q = 0
        water_tempeature_q = 0
        water_mass_q = 0

    P = float(water_pressure_q)
    T = float(water_tempeature_q) + 273.15
    M = float(water_mass_q)

    zone_number = iapws97._Bound_TP(T, P)


    if zone_number == None:
        messagebox.showerror("error", "please fill the correct number!")
        water_H = 0
        a = 0
    else :
        if zone_number == 1:
            a = iapws97._Region1(T, P)
            v1 = a["v"]  # Specific volume, [m³/kg]
            h1 = a["h"]  # Specific enthalpy, [kJ/kg]
            s1 = a["s"]  # Specific entropy, [kJ/kgK]
            cp1 = a["cp"]  # Specific isobaric heat capacity, [kJ/kgK]
            cv1 = a["cv"]  # Specific isocoric heat capacity, [kJ/kgK]
            w1 = a["w"]  # Speed of sound, [m/s]
            alfav1 = a["alfav"]  # Cubic expansion coefficient, [1/K]
            kt1 = a["kt"]  # Isothermal compressibility, [1/MPa]
            water_H = (h1 - 83.74) * 0.001 * M *10000
        if zone_number == 2:
            a = iapws97._Region2(T, P)
            v2 = a["v"]  # Specific volume, [m³/kg]
            h2 = a["h"]  # Specific enthalpy, [kJ/kg]
            s2 = a["s"]  # Specific entropy, [kJ/kgK]
            cp2 = a["cp"]  # Specific isobaric heat capacity, [kJ/kgK]
            cv2 = a["cv"]  # Specific isocoric heat capacity, [kJ/kgK]
            w2 = a["w"]  # Speed of sound, [m/s]
            alfav2 = a["alfav"]  # Cubic expansion coefficient, [1/K]
            kt2 = a["kt"]  # Isothermal compressibility, [1/MPa]
            water_H = (h2 - 83.74) * 0.001 * M *10000

    if water_total_frame.get() != "":
        water_total_frame.delete(0, "end")
        water_total_frame.insert("end", water_H)
    else:
        water_total_frame.insert("end", water_H)

def carbon_content_chk():
    if carbon_content_var.get() == 1:
        carbon_content_qty1['state'] = "normal"
        carbon_content_qty1['bg'] = '#248aa2'
        carbon_content_qty1['fg'] = "white"
        carbon_content_qty2['state'] = "normal"
        carbon_content_qty2['bg'] = '#248aa2'
        carbon_content_qty2['fg'] = "white"

    else:
        carbon_content_qty1['state'] = "disabled"
        carbon_content_qty2['state'] = "disabled"

def carbon_content_func():
    NCVi_q = carbon_content_qty1.get()
    EFi_q = carbon_content_qty2.get()

    if carbon_content_var.get() == 0:
        NCVi_q = 0
        EFi_q = 0

    elif carbon_content_var.get() == 1 and carbon_content_qty1.get() == "" or carbon_content_qty2.get() == "" :
        messagebox.showerror("error", "please fill the quantity!")
        NCVi_q = 0
        EFi_q = 0



    NCVi = float(NCVi_q)
    EFi = float(EFi_q)

    CCi = NCVi * EFi
    if carbon_content_total_frame.get() != "":
        carbon_content_total_frame.delete(0, "end")
        carbon_content_total_frame.insert("end", CCi)
    else:
        carbon_content_total_frame.insert("end", CCi)

##############UNIT TRANSFORM#################################
def convert_ES(n,unit1,unit2):
    c = [1000, 700]
    l = ['千克标油', '千克标煤']
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num=int(n.get())
        result = num/c[unit1_index]*c[unit2_index]
    return result

'''热量单位换算'''
def convert_E(n,unit1,unit2):
    c = [0.2389, 1, 1000, 1000000, 1000000000, 1000000000000]
    l = ['kcal', 'KJ','MJ','GJ','TJ']
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num = int(n.get())
        result = num / c[unit1_index] * c[unit2_index]
    return result

'''长度单位换算'''
def convert_L(n,unit1,unit2):
    c = [1000, 100, 10, 1, 0.001]
    l = ['毫米','厘米', '分米', '米', '千米' ]
    if unit1 not in l or unit2 not in l:
        result = 0
    else:
        unit1_index = l.index(unit1)
        unit2_index = l.index(unit2)
        print(type(n))
        print(n.get())
        num = int(n.get())
        result = num / c[unit1_index] * c[unit2_index]
    return result

def choose_unit(envet):
    choose = box1.get()
    list=[]
    print(choose)
    if choose == '能耗':
        list = ['千克标油', '千克标煤']
    elif choose == '长度':
        list = ['厘米', '分米', '米', '千米', '毫米']
    elif choose == '热量':
        list = ['kcal', 'KJ','MJ','GJ','TJ']
    box2['value'] = list
    box3['value'] = list

'''选择单位后的触发事件，计算的结果出现在如下情况：选择了正确的单位，或者输入数字后回车'''
def convert(envet):
    global data
    global data_out
    unit_class = box1.get()
    if unit_class == '能耗':
        data_out.set(convert_ES(data, box2.get(),box3.get()))
    elif unit_class =='长度':
        data_out.set(convert_L(data, box2.get(), box3.get()))
    elif unit_class =='热量':
        data_out.set(convert_E(data, box2.get(), box3.get()))
    label4.update()

def result():
    try:
        if inp.get() == "":
            inp.insert("end", "error")
        elif inp.get()[0] == "0":
            inp.delete(0, "end")
            inp.insert("end", "error")
        else:
            res = inp.get()
            res = eval(res)
            inp.insert("end", " = ")
            inp.insert("end", res)
    except SyntaxError:
        inp.insert("end", "invalid input")
# ===== Main Window Code =================


root = Tk()
root.geometry('1900x1040')  #650x400
# root.maxsize(650, 390)
# root.minsize(650, 390)
root.title("综合计算")
# root.iconbitmap("ball.ico")
tab_control = ttk.Notebook(root)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)
tab4 = Frame(tab_control)
tab5 = Frame(tab_control)
tab6 = Frame(tab_control)

# page tab total********************************************************************************
tab_control.add(tab1, text = "碳核算表格")
tab_control.add(tab2, text = "IPCC 2006年指南")
tab_control.add(tab3, text = "GB国标")
tab_control.add(tab4, text = "组分计算-质量分数")
tab_control.add(tab5, text = "组分计算-体积分数")
tab_control.add(tab6, text = "化工过程碳排放")
tab_control.pack(expand = 1, fill = "both")
# ******************************************************************************************
# page tab 2********************************************************************************
title_frame = Frame(tab2, width=1500, height=60, relief=RIDGE, borderwidth=5, bg='#248aa2')
title_frame.place(x=0, y=0)
l1 = Label(title_frame, text="参考缺省值", font=('roboto', 30, 'bold'), bg='#248aa2', fg="#ffffff")
l1.place(x=10, y=4)

frame_CO2_FACTOR = Frame(tab2, width=1200, height=2, relief=RIDGE, borderwidth=3, bg='#248aa2',
                    highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame_CO2_FACTOR.place(x=2, y=66)

# label_text_CO2_FACTOR = LabelFrame(frame_CO2_FACTOR, width=1200, height=720, text="说明1",   font=('宋体', 10, 'bold'),
#                     fg='#248aa2')
# label_text_CO2_FACTOR.place(x=2, y=2)

#A text review


img_factor1 = Image.open("../static/images/basketb.jpeg")
img_factor2 = Image.open("../static/images/cheme.jpeg")


img_factor1 = img_factor1.resize((690,690))
img_factor2 = img_factor2.resize((690,690))
myPng_factor_1 = ImageTk.PhotoImage(img_factor1)
myPng_factor_2 = ImageTk.PhotoImage(img_factor2)

text_factor1 = Text(frame_CO2_FACTOR, width = 210, height = 60)
text_factor1.image_create(END, padx = 1, pady = 1, image = myPng_factor_1) #创建一个图片对象，并插入到“END”位置
text_factor1.image_create(INSERT, padx = 2, pady = 1, image = myPng_factor_2) #创建一个图片对象，并插入到“END”位置
text_factor1.config(state = DISABLED)
text_factor1.pack()

# page tab 3*******************************************************************************
title_frame3 = Frame(tab3, width=1500, height=60, relief=RIDGE, borderwidth=5, bg='#248aa2')
title_frame3.place(x=0, y=0)
l3 = Label(title_frame3, text="参考缺省值-国标", font=('roboto', 30, 'bold'), bg='#248aa2', fg="#ffffff")
l3.place(x=10, y=4)

frame_ENERGY_FACTOR = Frame(tab3, width=1200, height=2, relief=RIDGE, borderwidth=3, bg='#248aa2',
                    highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame_ENERGY_FACTOR.place(x=2, y=66)

# 创建窗口 page tab 4*******************************************************************************

def create_inputs():
    # 删除之前的输入框
    for widget in frame_tab4.winfo_children():
        widget.destroy()
    # 创建新的输入框
    entries1 = []
    entries2 = []
    entries3 = []
    entries4 = []
    entries5 = []
    entries6 = []
    entries7 = []
    entries8 = []
    entries9 = []
    entries10 = []
    entries11 = []
    entries12 = []
    entries13 = []
    entries14 = []
    entries15 = []
    entries16 = []
    entries17 = []
    entries18 = []

    for i in range(num_components.get()):
        Label(frame_tab4, text=f"Component {i + 1}:").grid(row=0, column=i, padx=1, pady=1)
        Label(frame_tab4, text="总含量").grid(row=1, column=i, padx=1, pady=1)
        Label(frame_tab4, text="甲烷").grid(row=3, column=i, padx=1, pady=1)
        Label(frame_tab4, text="乙烷").grid(row=5, column=i, padx=1, pady=1)
        Label(frame_tab4, text="乙烯").grid(row=7, column=i, padx=1, pady=1)
        Label(frame_tab4, text="乙炔").grid(row=9, column=i, padx=1, pady=1)
        Label(frame_tab4, text="丙烷").grid(row=11, column=i, padx=1, pady=1)
        Label(frame_tab4, text="丙烯").grid(row=13, column=i, padx=1, pady=1)
        Label(frame_tab4, text="IC4").grid(row=15, column=i, padx=1, pady=1)
        Label(frame_tab4, text="NC4").grid(row=17, column=i, padx=1, pady=1)
        Label(frame_tab4, text="丁烯").grid(row=19, column=i, padx=1, pady=1)
        Label(frame_tab4, text="戊烷").grid(row=21, column=i, padx=1, pady=1)
        Label(frame_tab4, text="戊烯").grid(row=23, column=i, padx=1, pady=1)
        Label(frame_tab4, text="H2").grid(row=25, column=i, padx=1, pady=1)
        Label(frame_tab4, text="H2O").grid(row=27, column=i, padx=1, pady=1)
        Label(frame_tab4, text="H2S").grid(row=29, column=i, padx=1, pady=1)
        Label(frame_tab4, text="N2").grid(row=31, column=i, padx=1, pady=1)
        Label(frame_tab4, text="CO").grid(row=33, column=i, padx=1, pady=1)
        Label(frame_tab4, text="CO2").grid(row=35, column=i, padx=1, pady=1)

        entry1 = Entry(frame_tab4)
        entry2 = Entry(frame_tab4)
        entry3 = Entry(frame_tab4)
        entry4 = Entry(frame_tab4)
        entry5 = Entry(frame_tab4)
        entry6 = Entry(frame_tab4)
        entry7 = Entry(frame_tab4)
        entry8 = Entry(frame_tab4)
        entry9 = Entry(frame_tab4)
        entry10 = Entry(frame_tab4)
        entry11 = Entry(frame_tab4)
        entry12 = Entry(frame_tab4)
        entry13 = Entry(frame_tab4)
        entry14 = Entry(frame_tab4)
        entry15 = Entry(frame_tab4)
        entry16 = Entry(frame_tab4)
        entry17 = Entry(frame_tab4)
        entry18 = Entry(frame_tab4)

        entry1.insert(0, "0")
        entry2.insert(0, "0")
        entry3.insert(0, "0")
        entry4.insert(0, "0")
        entry5.insert(0, "0")
        entry6.insert(0, "0")
        entry7.insert(0, "0")
        entry8.insert(0, "0")
        entry9.insert(0, "0")
        entry10.insert(0, "0")
        entry11.insert(0, "0")
        entry12.insert(0, "0")
        entry13.insert(0, "0")
        entry14.insert(0, "0")
        entry15.insert(0, "0")
        entry16.insert(0, "0")
        entry17.insert(0, "0")
        entry18.insert(0, "0")

        # if entry1.get() == "":
        #     row_1 = 0.0
        # else:
        #     row_1 = float(row_1)

        entry1.grid(row=2, column=i, padx=1, pady=1)
        entry2.grid(row=4, column=i, padx=1, pady=1)
        entry3.grid(row=6, column=i, padx=1, pady=1)
        entry4.grid(row=8, column=i, padx=1, pady=1)
        entry5.grid(row=10, column=i, padx=1, pady=1)
        entry6.grid(row=12, column=i, padx=1, pady=1)
        entry7.grid(row=14, column=i, padx=1, pady=1)
        entry8.grid(row=16, column=i, padx=1, pady=1)
        entry9.grid(row=18, column=i, padx=1, pady=1)
        entry10.grid(row=20, column=i, padx=1, pady=1)
        entry11.grid(row=22, column=i, padx=1, pady=1)
        entry12.grid(row=24, column=i, padx=1, pady=1)
        entry13.grid(row=26, column=i, padx=1, pady=1)
        entry14.grid(row=28, column=i, padx=1, pady=1)
        entry15.grid(row=30, column=i, padx=1, pady=1)
        entry16.grid(row=32, column=i, padx=1, pady=1)
        entry17.grid(row=34, column=i, padx=1, pady=1)
        entry18.grid(row=36, column=i, padx=1, pady=1)

        entries1.append(entry1)
        entries2.append(entry2)
        entries3.append(entry3)
        entries4.append(entry4)
        entries5.append(entry5)
        entries6.append(entry6)
        entries7.append(entry7)
        entries8.append(entry8)
        entries9.append(entry9)
        entries10.append(entry10)
        entries11.append(entry11)
        entries12.append(entry12)
        entries13.append(entry13)
        entries14.append(entry14)
        entries15.append(entry15)
        entries16.append(entry16)
        entries17.append(entry17)
        entries18.append(entry18)


    def calculate_sum():
        # print(entry1.get())
        # print(entries1)
        # print(entries1)
        sum = 0
        new_list1 = []
        new_list2 = []
        new_list3 = []
        new_list4 = []
        new_list5 = []
        new_list6 = []
        new_list7 = []
        new_list8 = []
        new_list9 = []
        new_list10 = []
        new_list11 = []
        new_list12 = []
        new_list13 = []
        new_list14 = []
        new_list15 = []
        new_list16 = []
        new_list17 = []
        new_list18 = []


        for entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,entry12,entry13, entry14, entry15, entry16, entry17, entry18 in\
                zip(entries1, entries2,entries3, entries4,entries5, entries6,entries7, entries8,entries9, entries10, entries11,entries12,entries13, entries14,  entries15,entries16,entries17, entries18):
            # sum += int(entry1.get())
            new_list1.append(float(entry1.get()))
            new_list2.append(float(entry2.get()))
            new_list3.append(float(entry3.get()))
            new_list4.append(float(entry4.get()))
            new_list5.append(float(entry5.get()))
            new_list6.append(float(entry6.get()))
            new_list7.append(float(entry7.get()))
            new_list8.append(float(entry8.get()))
            new_list9.append(float(entry9.get()))
            new_list10.append(float(entry10.get()))
            new_list11.append(float(entry11.get()))
            new_list12.append(float(entry12.get()))
            new_list13.append(float(entry13.get()))
            new_list14.append(float(entry14.get()))
            new_list15.append(float(entry15.get()))
            new_list16.append(float(entry16.get()))
            new_list17.append(float(entry17.get()))
            new_list18.append(float(entry18.get()))

        big_array = np.array([new_list1,new_list2, new_list3, new_list4, new_list5, new_list6, new_list7, new_list8, new_list9, new_list10, new_list11, new_list12, new_list13 , new_list14,
                            new_list15,new_list16,new_list17,new_list18])
        # a = 原始数组
        # b = 将百分比转换成实地数据 # 这个数组考虑转成碳排放再汇总
        # c = 分物料汇成一个大总物料
        # d = b+c
        # e = B+C+大总物料各组分百分比
        # f = 计算各组分对应碳排放
        # g2 = 将各组分碳排放汇总成一股料

        # 求出燃料气组分百分比数组-质量分数
        b = [big_array[0]]

        for i in big_array[1:,]:
            new = big_array[0] * i * 0.01
            b.append(new)

        b = np.array(b)

        c = []
        for i in b:
            c.append(np.sum(i))
        D = np.insert(b,0,c,axis = 1)

        list_percent = []
        for i in D[:,0]:
            single_percent = i/D[:,0][0]
            list_percent.append(single_percent)
        list_percent = np.array(list_percent)
        E = np.insert(D,0,list_percent,axis = 1)


        row_E = range(1, big_array.shape[-1]+1)
        row_index_material = ["汇总物料百分比%", "汇总物料含量"]
        row_index_material_C = ["汇总物料碳排放"]
        row_index_material_HH = ["汇总物料高位热值"]
        row_index_material_LH = ["汇总物料低位热值"]

        for i in range(1, big_array.shape[-1]+1):
            row_index_material.append("物料" + str(i))
            row_index_material_C.append("物料" + str(i) + "碳排放")
            row_index_material_HH.append("物料" + str(i) + "高位热值")
            row_index_material_LH.append("物料" + str(i) + "低位热值")
        row_whole = row_index_material +  row_index_material_C
        # print(row_whole)
        B = np.array(b)

        column_index_material = np.array([" ","Total", "甲烷", "乙烷", "乙烯", "乙炔","丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷","戊烯", "H2", "H2O", "H2S", "N2","CO", "CO2"])
        column_index_material2 = np.array(
            ["Total", "甲烷", "乙烷", "乙烯", "乙炔", "丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷", "戊烯", "H2", "H2O", "H2S", "N2",
             "CO", "CO2"])
        row_index_material = np.array(row_index_material)
        row_index_material_C = np.array(row_index_material_C)
        row_index_material_HH = np.array(row_index_material_HH)
        row_index_material_LH = np.array(row_index_material_LH)

        count = 0
        F = []
        H_heat = []
        L_heat = []
        for i in B[1:,]:
            count += 1
            if count == 1: # 甲烷
                middle = i * (44/16)
                H_heat_middle =  i * 13256 # kCal/kg
                L_heat_middle = i * 11909  # kCal/kg
            if count == 2: # 乙烷
                middle = i * (44/30)
                H_heat_middle =  i * 12391 # kCal/kg
                L_heat_middle = i * 11312  # kCal/kg
            if count == 3: # 乙烯
                middle = i * (44/28)
                H_heat_middle =  i * 12113 # kCal/kg
                L_heat_middle = i * 11341  # kCal/kg
            if count == 4: # 乙炔
                middle = i * (44/26)
                H_heat_middle =  i * 12014 # kCal/kg
                L_heat_middle = i * 11600  # kCal/kg
            if count == 5: # 丙烷
                middle = i *  (44/44)
                H_heat_middle =  i * 12025 # kCal/kg
                L_heat_middle = i * 11045  # kCal/kg
            if count == 6: # 丙烯
                middle = i * (44/42)
                H_heat_middle =  i * 11756 # kCal/kg
                L_heat_middle = i * 10986  # kCal/kg
            if count == 7: # IC4
                middle = i * (44/58)
                H_heat_middle =  i * 11829 # kCal/kg
                L_heat_middle = i * 10900  # kCal/kg
            if count == 8: # NC4
                middle = i * (44/58)
                H_heat_middle =  i * 11829 # kCal/kg
                L_heat_middle = i * 10900  # kCal/kg
            if count == 9: # 丁烯
                middle = i * (44/56)
                H_heat_middle =  i * 11614 # kCal/kg
                L_heat_middle = i * 10844  # kCal/kg
            if count == 10: # 戊烷
                middle = i * (44/71)
                H_heat_middle =  i * 11709 # kCal/kg
                L_heat_middle = i * 10810  # kCal/kg
            if count == 11: # 戊烯
                middle = i * (44/70)
                H_heat_middle =  i * 11328 # kCal/kg
                L_heat_middle = i * 10556  # kCal/kg
            if count == 12: # H2
                middle = i * 0
                H_heat_middle =  i * 33942# kCal/kg
                L_heat_middle = i * 28575  # kCal/kg
            if count == 13: # H2O
                middle = i * 0
                H_heat_middle =  i * 0# kCal/kg
                L_heat_middle = i * 0  # kCal/kg
            if count == 14: # H2S
                middle = i * 0
                H_heat_middle =  i * 1.313 * 6054# kCal/kg
                L_heat_middle = i * 1.313 * 5581# kCal/kg
            if count == 15: # N2
                middle = i * 0
                H_heat_middle =  i * 0
                L_heat_middle = i * 0
            if count == 16: # CO
                middle = i * 0
                H_heat_middle =  i * 2414# kCal/kg
                L_heat_middle = i * 2414  # kCal/kg
            if count == 17: # CO2
                middle = i * 0
                H_heat_middle =  i * 0
                L_heat_middle = i * 0
            F.append(middle)
            H_heat.append(H_heat_middle)
            L_heat.append(L_heat_middle)
        sum_H_heat_column = np.sum(np.array(H_heat), axis=1)
        sum_L_heat_column = np.sum(np.array(L_heat), axis=1)

        HMV_x = np.concatenate((sum_H_heat_column.reshape(-1, 1), np.array(H_heat)), axis=1)
        LMV_x = np.concatenate((sum_L_heat_column.reshape(-1, 1), np.array(L_heat)), axis=1)

        HMV_row = np.sum(np.array(HMV_x), axis=0)
        LMV_row = np.sum(np.array(LMV_x), axis=0)

        HMV_labelr_labelc = np.concatenate((HMV_row.reshape(1, -1), np.array(HMV_x)), axis=0)
        LMV_labelr_labelc = np.concatenate((LMV_row.reshape(1, -1), np.array(LMV_x)), axis=0)

        F = np.array(F)
        row_sums = np.sum(F, axis=1)
        G = np.concatenate((row_sums.reshape(-1, 1), F), axis=1)
        column_sums = np.sum(G, axis=0)
        G2 = np.row_stack((column_sums,G))

        H = np.concatenate((E, G2), axis = 1)


        data = H
        data2 = HMV_labelr_labelc
        data3 = LMV_labelr_labelc


        data_df = pd.DataFrame(data)
        data_df.columns = [row_whole]

        data_df.index = [column_index_material2]

        data_df2 = pd.DataFrame(data = data2)
        data_df2.columns = [row_index_material_HH]
        data_df2.index = [column_index_material2]

        data_df3 = pd.DataFrame(data = data3)
        data_df3.columns = [row_index_material_LH]
        data_df3.index = [column_index_material2]

        writer = pd.ExcelWriter("1-MassFraction.xlsx")
        data_df.to_excel(writer, "碳排放", float_format='%.2f')
        data_df2.to_excel(writer, "高热值", float_format='%.2f')
        data_df3.to_excel(writer, "低热值", float_format='%.2f')

        writer.save()
        tk.Label(frame_tab4, text=f"Sum: {sum}").grid(row=num_components.get(), column=0, padx=5, pady=5)
    Button(frame_tab4, text="Calculate Sum", command=calculate_sum).grid(row=39, column=0, padx=5,pady=5)

# 创建一个框架，用于存储输入框
frame_tab4 = Frame(tab4)
frame_tab4.pack()

canvas = Canvas(tab4, bg = "orange", scrollregion=(0, 0, 1000, 1000))
frame_tab4 = Frame(canvas)
scrollbarx = Scrollbar(tab4, orient="horizontal", command=canvas.xview)
scrollbary = Scrollbar(tab4, orient="vertical", command=canvas.yview)

# scrollbary.place(x=780, y=0, height=300)
# scrollbarx.place(x=400, y=250, width=400)

canvas.configure(xscrollcommand=scrollbarx.set)
canvas.configure(xscrollcommand=scrollbary.set)

scrollbarx.pack(side=BOTTOM, fill=X)
scrollbary.pack(side=RIGHT, fill=Y)
canvas.pack()
canvas.create_window((0, 0), window=frame_tab4, anchor='nw')

# 设置 frame_tab4 尺寸使其适应 canvas
frame_tab4.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all"), width=800, height=920))

# 询问用户组分数量
num_components = tk.IntVar()
tk.Label(tab4, text="Enter the number of components:").pack()
tk.Entry(tab4, textvariable=num_components).pack()
tk.Button(tab4, text="Create Inputs", command=create_inputs).pack()
#

# 创建窗口 page tab 5*******************************************************************************

def create_inputs2():
    # 删除之前的输入框
    for widget in frame_tab5.winfo_children():
        widget.destroy()
    # 创建新的输入框
    entries1 = []
    entries2 = []
    entries3 = []
    entries4 = []
    entries5 = []
    entries6 = []
    entries7 = []
    entries8 = []
    entries9 = []
    entries10 = []
    entries11 = []
    entries12 = []
    entries13 = []
    entries14 = []
    entries15 = []
    entries16 = []
    entries17 = []
    entries18 = []

    for i in range(num_components2.get()):
        Label(frame_tab5, text=f"Component {i + 1}:").grid(row=0, column=i, padx=1, pady=1)
        Label(frame_tab5, text="总含量").grid(row=1, column=i, padx=1, pady=1)
        Label(frame_tab5, text="甲烷").grid(row=3, column=i, padx=1, pady=1)
        Label(frame_tab5, text="乙烷").grid(row=5, column=i, padx=1, pady=1)
        Label(frame_tab5, text="乙烯").grid(row=7, column=i, padx=1, pady=1)
        Label(frame_tab5, text="乙炔").grid(row=9, column=i, padx=1, pady=1)
        Label(frame_tab5, text="丙烷").grid(row=11, column=i, padx=1, pady=1)
        Label(frame_tab5, text="丙烯").grid(row=13, column=i, padx=1, pady=1)
        Label(frame_tab5, text="IC4").grid(row=15, column=i, padx=1, pady=1)
        Label(frame_tab5, text="NC4").grid(row=17, column=i, padx=1, pady=1)
        Label(frame_tab5, text="丁烯").grid(row=19, column=i, padx=1, pady=1)
        Label(frame_tab5, text="戊烷").grid(row=21, column=i, padx=1, pady=1)
        Label(frame_tab5, text="戊烯").grid(row=23, column=i, padx=1, pady=1)
        Label(frame_tab5, text="H2").grid(row=25, column=i, padx=1, pady=1)
        Label(frame_tab5, text="H2O").grid(row=27, column=i, padx=1, pady=1)
        Label(frame_tab5, text="H2S").grid(row=29, column=i, padx=1, pady=1)
        Label(frame_tab5, text="N2").grid(row=31, column=i, padx=1, pady=1)
        Label(frame_tab5, text="CO").grid(row=33, column=i, padx=1, pady=1)
        Label(frame_tab5, text="CO2").grid(row=35, column=i, padx=1, pady=1)

        entry1 = Entry(frame_tab5)
        entry2 = Entry(frame_tab5)
        entry3 = Entry(frame_tab5)
        entry4 = Entry(frame_tab5)
        entry5 = Entry(frame_tab5)
        entry6 = Entry(frame_tab5)
        entry7 = Entry(frame_tab5)
        entry8 = Entry(frame_tab5)
        entry9 = Entry(frame_tab5)
        entry10 = Entry(frame_tab5)
        entry11 = Entry(frame_tab5)
        entry12 = Entry(frame_tab5)
        entry13 = Entry(frame_tab5)
        entry14 = Entry(frame_tab5)
        entry15 = Entry(frame_tab5)
        entry16 = Entry(frame_tab5)
        entry17 = Entry(frame_tab5)
        entry18 = Entry(frame_tab5)

        entry1.insert(0, "0")
        entry2.insert(0, "0")
        entry3.insert(0, "0")
        entry4.insert(0, "0")
        entry5.insert(0, "0")
        entry6.insert(0, "0")
        entry7.insert(0, "0")
        entry8.insert(0, "0")
        entry9.insert(0, "0")
        entry10.insert(0, "0")
        entry11.insert(0, "0")
        entry12.insert(0, "0")
        entry13.insert(0, "0")
        entry14.insert(0, "0")
        entry15.insert(0, "0")
        entry16.insert(0, "0")
        entry17.insert(0, "0")
        entry18.insert(0, "0")

        # if entry1.get() == "":
        #     row_1 = 0.0
        # else:
        #     row_1 = float(row_1)

        entry1.grid(row=2, column=i, padx=1, pady=1)
        entry2.grid(row=4, column=i, padx=1, pady=1)
        entry3.grid(row=6, column=i, padx=1, pady=1)
        entry4.grid(row=8, column=i, padx=1, pady=1)
        entry5.grid(row=10, column=i, padx=1, pady=1)
        entry6.grid(row=12, column=i, padx=1, pady=1)
        entry7.grid(row=14, column=i, padx=1, pady=1)
        entry8.grid(row=16, column=i, padx=1, pady=1)
        entry9.grid(row=18, column=i, padx=1, pady=1)
        entry10.grid(row=20, column=i, padx=1, pady=1)
        entry11.grid(row=22, column=i, padx=1, pady=1)
        entry12.grid(row=24, column=i, padx=1, pady=1)
        entry13.grid(row=26, column=i, padx=1, pady=1)
        entry14.grid(row=28, column=i, padx=1, pady=1)
        entry15.grid(row=30, column=i, padx=1, pady=1)
        entry16.grid(row=32, column=i, padx=1, pady=1)
        entry17.grid(row=34, column=i, padx=1, pady=1)
        entry18.grid(row=36, column=i, padx=1, pady=1)

        entries1.append(entry1)
        entries2.append(entry2)
        entries3.append(entry3)
        entries4.append(entry4)
        entries5.append(entry5)
        entries6.append(entry6)
        entries7.append(entry7)
        entries8.append(entry8)
        entries9.append(entry9)
        entries10.append(entry10)
        entries11.append(entry11)
        entries12.append(entry12)
        entries13.append(entry13)
        entries14.append(entry14)
        entries15.append(entry15)
        entries16.append(entry16)
        entries17.append(entry17)
        entries18.append(entry18)


    def calculate_sum():
        # print(entry1.get())
        # print(entries1)
        # print(entries1)
        sum = 0
        new_list1 = []
        new_list2 = []
        new_list3 = []
        new_list4 = []
        new_list5 = []
        new_list6 = []
        new_list7 = []
        new_list8 = []
        new_list9 = []
        new_list10 = []
        new_list11 = []
        new_list12 = []
        new_list13 = []
        new_list14 = []
        new_list15 = []
        new_list16 = []
        new_list17 = []
        new_list18 = []


        for entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10,entry11,entry12,entry13, entry14, entry15, entry16, entry17, entry18 in\
                zip(entries1, entries2,entries3, entries4,entries5, entries6,entries7, entries8,entries9, entries10, entries11,entries12,entries13, entries14,  entries15,entries16,entries17, entries18):
            # sum += int(entry1.get())
            new_list1.append(float(entry1.get()))
            new_list2.append(float(entry2.get()))
            new_list3.append(float(entry3.get()))
            new_list4.append(float(entry4.get()))
            new_list5.append(float(entry5.get()))
            new_list6.append(float(entry6.get()))
            new_list7.append(float(entry7.get()))
            new_list8.append(float(entry8.get()))
            new_list9.append(float(entry9.get()))
            new_list10.append(float(entry10.get()))
            new_list11.append(float(entry11.get()))
            new_list12.append(float(entry12.get()))
            new_list13.append(float(entry13.get()))
            new_list14.append(float(entry14.get()))
            new_list15.append(float(entry15.get()))
            new_list16.append(float(entry16.get()))
            new_list17.append(float(entry17.get()))
            new_list18.append(float(entry18.get()))

        big_array = np.array([new_list1,new_list2, new_list3, new_list4, new_list5, new_list6, new_list7, new_list8, new_list9, new_list10, new_list11, new_list12, new_list13 , new_list14,
                            new_list15,new_list16,new_list17,new_list18])
        # a = 原始数组
        # b = 将百分比转换成实地数据 # 这个数组考虑转成碳排放再汇总
        # c = 分物料汇成一个大总物料
        # d = b+c
        # e = B+C+大总物料各组分百分比
        # f = 计算各组分对应碳排放
        # g2 = 将各组分碳排放汇总成一股料

        # 求出燃料气组分百分比数组-质量分数
        b = [big_array[0]]

        for i in big_array[1:,]:
            new = big_array[0] * i * 0.01
            b.append(new)

        b = np.array(b)

        c = []
        for i in b:
            c.append(np.sum(i))
        D = np.insert(b,0,c,axis = 1)

        list_percent = []
        for i in D[:,0]:
            single_percent = i/D[:,0][0]
            list_percent.append(single_percent)
        list_percent = np.array(list_percent)
        E = np.insert(D,0,list_percent,axis = 1)

        row_E = range(1, big_array.shape[-1] + 1)
        row_index_material = ["汇总物料百分比%", "汇总物料含量"]
        row_index_material_C = ["汇总物料碳排放"]
        row_index_material_HH = ["汇总物料高位热值"]
        row_index_material_LH = ["汇总物料低位热值"]

        for i in range(1, big_array.shape[-1] + 1):
            row_index_material.append("物料" + str(i))
            row_index_material_C.append("物料" + str(i) + "碳排放")
            row_index_material_HH.append("物料" + str(i) + "高位热值")
            row_index_material_LH.append("物料" + str(i) + "低位热值")
        row_whole = row_index_material + row_index_material_C
        # print(row_whole)
        B = np.array(b)

        column_index_material = np.array(
            [" ", "Total", "甲烷", "乙烷", "乙烯", "乙炔", "丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷", "戊烯", "H2", "H2O", "H2S", "N2",
             "CO", "CO2"])
        column_index_material2 = np.array(
            ["Total", "甲烷", "乙烷", "乙烯", "乙炔", "丙烷", "丙烯", "IC4", "NC4", "丁烯", "戊烷", "戊烯", "H2", "H2O", "H2S", "N2",
             "CO", "CO2"])
        row_index_material = np.array(row_index_material)
        row_index_material_C = np.array(row_index_material_C)
        row_index_material_HH = np.array(row_index_material_HH)
        row_index_material_LH = np.array(row_index_material_LH)

        count = 0
        F = []
        H_heat = []
        L_heat = []
        for i in B[1:, ]:
            count += 1
            if count == 1:  # 甲烷
                middle = i * (44 / 16)
                H_heat_middle = i * 13256  # kCal/kg
                L_heat_middle = i * 11909  # kCal/kg
            if count == 2:  # 乙烷
                middle = i * (44 / 30)
                H_heat_middle = i * 12391  # kCal/kg
                L_heat_middle = i * 11312  # kCal/kg
            if count == 3:  # 乙烯
                middle = i * (44 / 28)
                H_heat_middle = i * 12113  # kCal/kg
                L_heat_middle = i * 11341  # kCal/kg
            if count == 4:  # 乙炔
                middle = i * (44 / 26)
                H_heat_middle = i * 12014  # kCal/kg
                L_heat_middle = i * 11600  # kCal/kg
            if count == 5:  # 丙烷
                middle = i * (44 / 44)
                H_heat_middle = i * 12025  # kCal/kg
                L_heat_middle = i * 11045  # kCal/kg
            if count == 6:  # 丙烯
                middle = i * (44 / 42)
                H_heat_middle = i * 11756  # kCal/kg
                L_heat_middle = i * 10986  # kCal/kg
            if count == 7:  # IC4
                middle = i * (44 / 58)
                H_heat_middle = i * 11829  # kCal/kg
                L_heat_middle = i * 10900  # kCal/kg
            if count == 8:  # NC4
                middle = i * (44 / 58)
                H_heat_middle = i * 11829  # kCal/kg
                L_heat_middle = i * 10900  # kCal/kg
            if count == 9:  # 丁烯
                middle = i * (44 / 56)
                H_heat_middle = i * 11614  # kCal/kg
                L_heat_middle = i * 10844  # kCal/kg
            if count == 10:  # 戊烷
                middle = i * (44 / 71)
                H_heat_middle = i * 11709  # kCal/kg
                L_heat_middle = i * 10810  # kCal/kg
            if count == 11:  # 戊烯
                middle = i * (44 / 70)
                H_heat_middle = i * 11328  # kCal/kg
                L_heat_middle = i * 10556  # kCal/kg
            if count == 12:  # H2
                middle = i * 0
                H_heat_middle = i * 33942  # kCal/kg
                L_heat_middle = i * 28575  # kCal/kg
            if count == 13:  # H2O
                middle = i * 0
                H_heat_middle = i * 0  # kCal/kg
                L_heat_middle = i * 0  # kCal/kg
            if count == 14:  # H2S
                middle = i * 0
                H_heat_middle = i * 1.313 * 6054  # kCal/kg
                L_heat_middle = i * 1.313 * 5581  # kCal/kg
            if count == 15:  # N2
                middle = i * 0
                H_heat_middle = i * 0
                L_heat_middle = i * 0
            if count == 16:  # CO
                middle = i * 0
                H_heat_middle = i * 2414  # kCal/kg
                L_heat_middle = i * 2414  # kCal/kg
            if count == 17:  # CO2
                middle = i * 0
                H_heat_middle = i * 0
                L_heat_middle = i * 0
            F.append(middle)
            H_heat.append(H_heat_middle)
            L_heat.append(L_heat_middle)
        sum_H_heat_column = np.sum(np.array(H_heat), axis=1)
        sum_L_heat_column = np.sum(np.array(L_heat), axis=1)

        HMV_x = np.concatenate((sum_H_heat_column.reshape(-1, 1), np.array(H_heat)), axis=1)
        LMV_x = np.concatenate((sum_L_heat_column.reshape(-1, 1), np.array(L_heat)), axis=1)

        HMV_row = np.sum(np.array(HMV_x), axis=0)
        LMV_row = np.sum(np.array(LMV_x), axis=0)

        HMV_labelr_labelc = np.concatenate((HMV_row.reshape(1, -1), np.array(HMV_x)), axis=0)
        LMV_labelr_labelc = np.concatenate((LMV_row.reshape(1, -1), np.array(LMV_x)), axis=0)

        F = np.array(F)
        row_sums = np.sum(F, axis=1)
        G = np.concatenate((row_sums.reshape(-1, 1), F), axis=1)
        column_sums = np.sum(G, axis=0)
        G2 = np.row_stack((column_sums, G))

        H = np.concatenate((E, G2), axis=1)

        data = H
        data2 = HMV_labelr_labelc
        data3 = LMV_labelr_labelc

        data_df = pd.DataFrame(data)
        data_df.columns = [row_whole]

        data_df.index = [column_index_material2]

        data_df2 = pd.DataFrame(data=data2)
        data_df2.columns = [row_index_material_HH]
        data_df2.index = [column_index_material2]

        data_df3 = pd.DataFrame(data=data3)
        data_df3.columns = [row_index_material_LH]
        data_df3.index = [column_index_material2]

        writer = pd.ExcelWriter("2-VolumeFraction.xlsx")
        data_df.to_excel(writer, "碳排放", float_format='%.2f')
        data_df2.to_excel(writer, "高热值", float_format='%.2f')
        data_df3.to_excel(writer, "低热值", float_format='%.2f')

        writer.save()
        tk.Label(frame_tab5, text=f"Sum: {sum}").grid(row=num_components2.get(), column=0, padx=5, pady=5)

    Button(frame_tab5, text="Calculate Sum", command=calculate_sum).grid(row=39, column=0, padx=5, pady=5)


# 创建一个框架，用于存储输入框
frame_tab5 = Frame(tab5)
frame_tab5.pack()

canvas2 = Canvas(tab5, bg = "orange", scrollregion=(0, 0, 1000, 1000))
frame_tab5 = Frame(canvas2)
scrollbarx2 = Scrollbar(tab5, orient="horizontal", command=canvas2.xview)
scrollbary2 = Scrollbar(tab5, orient="vertical", command=canvas2.yview)

# scrollbary.place(x=780, y=0, height=300)
# scrollbarx.place(x=400, y=250, width=400)

canvas2.configure(xscrollcommand=scrollbarx2.set)
canvas2.configure(xscrollcommand=scrollbary2.set)

scrollbarx2.pack(side=BOTTOM, fill=X)
scrollbary2.pack(side=RIGHT, fill=Y)
canvas2.pack()
canvas2.create_window((0, 0), window=frame_tab5, anchor='nw')

# 设置 frame_tab4 尺寸使其适应 canvas
frame_tab5.bind("<Configure>", lambda e: canvas2.configure(scrollregion=canvas2.bbox("all"), width=800, height=920))

# 询问用户组分数量
num_components2 = tk.IntVar()
tk.Label(tab5, text="Enter the number of components:").pack()
tk.Entry(tab5, textvariable=num_components2).pack()
tk.Button(tab5, text="Create Inputs", command=create_inputs2).pack()
#

#A text review

img_factor3 = Image.open("../static/images/cheme.jpeg")
img_factor5 = Image.open("../static/images/cheme.jpeg")

img_factor3 = img_factor3.resize((690,690))
img_factor5 = img_factor5.resize((690,690))

myPng_factor_3 = ImageTk.PhotoImage(img_factor3)
myPng_factor_5 = ImageTk.PhotoImage(img_factor5)

text_factor3 = Text(frame_ENERGY_FACTOR, width = 210, height = 60)
text_factor3.image_create(END, padx = 1, pady = 1, image = myPng_factor_3) #创建一个图片对象，并插入到“END”位置
text_factor3.image_create(INSERT, padx = 2, pady = 1, image = myPng_factor_5) #创建一个图片对象，并插入到“END”位置
text_factor3.config(state = DISABLED)
text_factor3.pack()
# page tab 1********************************************************************************



# frame1 is the area of directly emission of C = DEC
frame1 = Frame(tab1, width=1880, height=1000, relief=RIDGE, borderwidth=5, bg='#248aa2') #change the area of DEC
frame1.place(x=0, y=0) #change the position of DEC

frame1_1 = Frame(frame1, width=1870, height=980, relief=RIDGE, borderwidth=3, bg='#248aa2',
                    highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame1_1.place(x=0, y=0)

label_1_1_1 = LabelFrame(frame1_1, text="直接CO2排放 SH/T 5000-2011", width=800, height=970, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1.place(x=2, y=2)

label_1_1_2 = LabelFrame(frame1_1, text="直接CO2排放-组成计算", width=735, height=970, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_2.place(x=2+652, y=2)

label_1_1_3 = LabelFrame(frame1_1, text="间接CO2排放 SH/T 5000-2011", width=650, height=970, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_3.place(x=2, y=510)

label_1_1_1_1 = LabelFrame(frame1_1, text="固定和移动燃烧CO2排放量计算", width=630, height=320,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_1.place(x=2+20, y=2+20)

label_1_1_1_1_1 = LabelFrame(frame1_1, text="方法一 实际燃料消耗", width=610, height=160,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_1_1.place(x=2+20+20, y=2+20+20)

label_1_1_1_1_2 = LabelFrame(frame1_1, text="方法二 燃料热值计算", width=610, height=160,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_1_2.place(x=2+20+20, y=350)

label_text1 = LabelFrame(frame1_1, text="说明",  width=100, height=232,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_text1.place(x=20, y=195)

##################### PAGE 1 SMALL TOOLS ########################################################
small_tools_background = LabelFrame(tab1, text="工具栏",width=600, height=600, relief=RIDGE, borderwidth=3, bg='#248aa2',
                    highlightbackground="white", highlightcolor="white", highlightthickness=2)
small_tools_background.place(x=670, y=360)
#####################(1) Water property CALCULATE THE STEAM ########################################################
water_frame = LabelFrame(small_tools_background, text="蒸汽计算 （万吨/a 转换成 GJ）", width=420, height=130, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
water_frame.place(x=2, y=2)

# water-CHECKBUTTON species one title
water_var = IntVar()
chk_water = Checkbutton(water_frame, text="物质1", variable=water_var, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=water_chk)
chk_water.place(x=36, y=25)

# water-FRAME1-
water_qty1 = Entry(water_frame, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
water_qty1.place(x=100, y=25)
water_qty1.insert(0, "0")

# water-FRAME2-
water_qty2 = Entry(water_frame, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
water_qty2.place(x=100+100, y=25)
water_qty2.insert(0, "0")

# water-FRAME3-
water_qty3 = Entry(water_frame, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
water_qty3.place(x=100+100+100, y=25)
water_qty3.insert(0, "0")

# water-LABEL1-
waterl_1 = Label(water_frame, text="压力/Mpa", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
waterl_1.place(x=100, y=4)

# water-LABEL2-
waterl_2 = Label(water_frame, text="温度/℃", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
waterl_2.place(x=100+100, y=4)

# water-LABEL3-
waterl_3 = Label(water_frame, text="蒸汽量/万吨/年", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
waterl_3.place(x=100+100+100, y=4)

# water-result surface
water_total = Button(water_frame, text="计算热量 GJ", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=water_func)
water_total.place(x=2, y=50)

water_total_frame = Entry(water_frame, width=15, borderwidth=4, relief=SUNKEN)
water_total_frame.place(x=4, y=70)

###################(2) 含碳量缺省值计算 ########################################################

carbon_content_frame = LabelFrame(small_tools_background, text="含碳量缺省值计算 CFi", width=420, height=130, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
carbon_content_frame.place(x=2, y=130)

# carbon_content-CHECKBUTTON species one title
carbon_content_var = IntVar()
chk_carbon_content = Checkbutton(carbon_content_frame, text="物质1", variable=carbon_content_var, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=carbon_content_chk)
chk_carbon_content.place(x=36, y=25)

# carbon_content-FRAME1-
carbon_content_qty1 = Entry(carbon_content_frame, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
carbon_content_qty1.place(x=100, y=25)
carbon_content_qty1.insert(0, "0")

# carbon_content-FRAME2-
carbon_content_qty2 = Entry(carbon_content_frame, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
carbon_content_qty2.place(x=100+100, y=25)
carbon_content_qty2.insert(0, "0")

# carbon_content-LABEL1-
carbon_contentl_1 = Label(carbon_content_frame, text="GJ/吨（Nm3）", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
carbon_contentl_1.place(x=100, y=4)

# carbon_content-LABEL2-
carbon_contentl_2 = Label(carbon_content_frame, text="吨碳/GJ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
carbon_contentl_2.place(x=100+100, y=4)

# carbon_content-result surface
carbon_content_total = Button(carbon_content_frame, text="计算CFi 吨碳/吨（万Nm3）燃料", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=carbon_content_func)
carbon_content_total.place(x=2, y=50)

carbon_content_total_frame = Entry(carbon_content_frame, width=15, borderwidth=4, relief=SUNKEN)
carbon_content_total_frame.place(x=4, y=70)

###################(3) 迷你计算器 ########################################################
# Entry Widgets to show calculations
# unit area


calculation_frame = LabelFrame(small_tools_background, text="迷你计算器", width=380, height=380, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
calculation_frame.place(x=2, y=130+130)
#
inp = Entry(calculation_frame, width=35, borderwidth=3, relief=RIDGE)
inp.grid(pady=10, row=0, sticky="w", padx=15)
###################(4) 单位换算 ########################################################


# unit area
# unit_background = Frame(small_tools_background, width=250, height=230, relief=RIDGE, borderwidth=3, bg='#248aa2',
#                     highlightbackground="white", highlightcolor="white", highlightthickness=2)
# unit_background.place(x=318, y=130+130)

unit_frame = LabelFrame(small_tools_background, text="单位转换", width=200, height=200, borderwidth=3, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
unit_frame.place(x=315, y=260)


'''体积单位换算'''

label1 = Label(unit_frame, text='选择要转换的单位类型',)
label1.grid(row=0,column=0, sticky='nw')
box1 = ttk.Combobox(unit_frame)
box1['value'] = ('能耗', '长度', '热量')
box1.current(0)
box1.bind("<<ComboboxSelected>>", choose_unit)
box1.grid(row=1,column=0, sticky='nw',ipadx=35)

label2 = Label(unit_frame, text='输入',justify='left')
label2.grid(row=2,column=0, sticky='nw')

data = tk.StringVar()
entry1 = tk.Entry(unit_frame, textvariable=data)
entry1.insert(6,'输入值')
entry1.bind('<Return>',convert)
entry1.grid(row=3,column=0, sticky='nw',ipadx=35)

box2 = ttk.Combobox(unit_frame)
box2.bind("<<ComboboxSelected>>", convert)
box2.grid(row=4,column=0, sticky='nw',ipadx=35)

label3 = tk.Label(unit_frame, text='等于')
label3.grid(row=5,column=0, sticky='nw')

data_out = tk.StringVar()
data_out.set('0')
label4 = tk.Label(unit_frame,textvariable=data_out)
label4.grid(row=6,column=0, sticky='nw')

box3 = ttk.Combobox(unit_frame)
box3.bind("<<ComboboxSelected>>", convert)
box3.grid(row=7,column=0, sticky='nw', ipadx=35)
# <============ end code ================>


# <============= Button Design Code starts here.. ==================>

# using lambda instead of functions to make the use of buttons more clear

clear = Button(calculation_frame, text="C", width=2, command=lambda: inp.delete(0, "end"), bg="red", fg="white", relief=RIDGE)
clear.grid(row=0, sticky="w", column = 1)
nine = Button(calculation_frame,text="9", width=2, command=lambda: inp.insert("end", "9"), borderwidth=3, relief=RIDGE)
nine.grid(row=1, sticky="w", padx=15)
eight = Button(calculation_frame, text="8", width=2, command=lambda: inp.insert("end", "8"), borderwidth=3, relief=RIDGE)
eight.grid(row=1, sticky="w", padx=45)
seven = Button(calculation_frame, text="7", width=2, command=lambda: inp.insert("end", "7"), borderwidth=3, relief=RIDGE)
seven.grid(row=1, sticky="w", padx=75)
plus = Button(calculation_frame, text="+", width=2, command=lambda: inp.insert("end", "+"), borderwidth=3, relief=RIDGE)
plus.grid(row=1, sticky="e", padx=125)
six = Button(calculation_frame, text="6", width=2, command=lambda: inp.insert("end", "6"), borderwidth=3, relief=RIDGE)
six.grid(row=2, sticky="w", padx=15, pady=5)
five = Button(calculation_frame, text="5", width=2, command=lambda: inp.insert("end", "5"), borderwidth=3, relief=RIDGE)
five.grid(row=2, sticky="w", padx=45, pady=5)
four = Button(calculation_frame, text="4", width=2, command=lambda: inp.insert("end", "4"), borderwidth=3, relief=RIDGE)
four.grid(row=2, sticky="w", padx=75, pady=5)
minus = Button(calculation_frame, text="-", width=2, command=lambda: inp.insert("end", "-"), borderwidth=3, relief=RIDGE)
minus.grid(row=2, sticky="e", padx=125, pady=5)
three = Button(calculation_frame, text="3", width=2, command=lambda: inp.insert("end", "3"), borderwidth=3, relief=RIDGE)
three.grid(row=3, sticky="w", padx=15, pady=5)
two = Button(calculation_frame, text="2", width=2, command=lambda: inp.insert("end", "2"), borderwidth=3, relief=RIDGE)
two.grid(row=3, sticky="w", padx=45, pady=5)
one = Button(calculation_frame, text="1", width=2, command=lambda: inp.insert("end", "1"), borderwidth=3, relief=RIDGE)
one.grid(row=3, sticky="w", padx=75, pady=5)
multiply = Button(calculation_frame, text="*", width=2, command=lambda: inp.insert("end", "*"), borderwidth=3, relief=RIDGE)
multiply.grid(row=3, sticky="e", padx=125, pady=5)
zero = Button(calculation_frame, text="0", width=2, command=lambda: inp.insert("end", "0"), borderwidth=3, relief=RIDGE)
zero.grid(row=4, sticky="w", padx=15, pady=5)
double_zero = Button(calculation_frame,text="00", width=2, command=lambda: inp.insert("end", "00"), borderwidth=3, relief=RIDGE)
double_zero.grid(row=4, sticky="w", padx=45, pady=5)
dot = Button(calculation_frame, text=".", width=2, command=lambda: inp.insert("end", "."), borderwidth=3, relief=RIDGE)
dot.grid(row=4, sticky="w", padx=75, pady=5)
divide = Button(calculation_frame, text="/", width=2, command=lambda: inp.insert("end", "/"), borderwidth=3, relief=RIDGE)
divide.grid(row=4, sticky="e", padx=125, pady=5)
result = Button(calculation_frame, text="=", width=10, command=result, bg="red", fg="white", borderwidth=3, relief=RIDGE)
result.grid(row=5, sticky="w", padx=15, pady=5)
modulus = Button(calculation_frame, text="%", width=2, command=lambda: inp.insert("end", "%"), borderwidth=3, relief=RIDGE)
modulus.grid(row=5, sticky="e", padx=125, pady=5)
###################(4) 单位转换 ########################################################


# ******************************************************************************************
##################### EACH BLOCK ########################################################
#A text review
# img1 = Image.open("NOTE_SECTION_A.jpg")
# img1 = img1.resize((500,500))
# myPng1 = ImageTk.PhotoImage(img1)
# text1 = Text(label_text1, width = 89, height = 10)
# text1.image_create(END, image = myPng1) #创建一个图片对象，并插入到“END”位置
# text1.pack()


text1 = Text(label_text1, width = 89, height = 10)
text1.pack()
text1.insert(END,"方法一：按照统计期内实际的燃料消耗以及该燃料的实测碳含量的加权平均值或默认碳含量）为基准计算燃烧过程CO2的排放量\n")
text1.insert(INSERT,"CRi：该种燃料燃烧的碳转化率，%;\n")
text1.insert(INSERT,"CFi：该种燃料的碳含量，吨碳/吨（万Nm3）燃料;\n")
text1.insert(INSERT,"\n")
text1.insert(INSERT,"方法二：根据不同燃料的热值和对应的CO2排放因子进行计算；\n")
text1.insert(INSERT,"HVi：该种燃料的低位热值，单位为兆焦每千克或兆焦每标立方米（MJ/kg或MJ/Nm3）;\n")
text1.insert(INSERT,"EFi：该种燃料的CO2排放因子，单位为千克CO2每兆焦（kgCO2/MJ);\n")
text1.config(state = DISABLED)

#
label_1_1_1_3 = LabelFrame(label_1_1_3, text="外购蒸汽、电对应的间接CO2排放", width=620, height=325-15-30,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_3.place(x=2+20, y=2)


label_1_1_1_4 = LabelFrame(label_1_1_3, text="外供蒸汽、电对应的间接CO2排放", width=620, height=325-15-30,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_4.place(x=2+20, y=160)



label_text2 = LabelFrame(frame1_1, text="说明2",  width=100, height=100,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_text2.place(x=20, y=840)


#A text review
img2 = Image.open("../static/images/cheme.jpeg")
img2 = img2.resize((500,420))
myPng2 = ImageTk.PhotoImage(img2)
text2 = Text(label_text2, width = 89, height = 8)
text2.image_create(END, image = myPng2) #创建一个图片对象，并插入到“END”位置
text2.pack()

# A-result surface
A_SP1_total = Button(label_1_1_1_1_1, text="碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableA_1)
A_SP1_total.place(x=485, y=2)

A_SP1_total_frame = Entry(label_1_1_1_1_1, width=15, borderwidth=4, relief=SUNKEN)
A_SP1_total_frame.place(x=485, y=2+20)

A_SP2_total_frame = Entry(label_1_1_1_1_1, width=15, borderwidth=4, relief=SUNKEN)
A_SP2_total_frame.place(x=485, y=2+20+20)

A_SP3_total_frame = Entry(label_1_1_1_1_1, width=15, borderwidth=4, relief=SUNKEN)
A_SP3_total_frame.place(x=485, y=2+20+20+20)

A_SP4_total_frame = Entry(label_1_1_1_1_1, width=15, borderwidth=4, relief=SUNKEN)
A_SP4_total_frame.place(x=485, y=2+20+20+20+20)

# 碳排放总计
A_SP_all_total = Button(label_1_1_1_1_1, text="碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableA_1)
A_SP_all_total.place(x=30, y=115)
A_SP_all_total_frame = Entry(label_1_1_1_1_1, width=15, borderwidth=4, relief=SUNKEN)
A_SP_all_total_frame.place(x=45+80, y=115)
# A-ONE1
one_var1 = IntVar()
one_var2 = IntVar()
one_var3 = IntVar()
one_var4 = IntVar()
# A-ONE1-CHECKBUTTON species one title
one_1 = Checkbutton(label_1_1_1_1_1, text="物质1", variable=one_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=one1_chk)
one_1.place(x=36, y=25)

# A-ONE1-FRAME0-species one quantity
one_qty0 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
one_qty0.place(x=100, y=25)

# A-ONE1-FRAME1-species one quantity
one_qty1 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one_qty1.place(x=200, y=25)
one_qty1.insert(0, "0")

# A-ONE1-FRAME2-species one ratio of carbon transformation
one_qty2 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one_qty2.place(x=200+100, y=25)
one_qty2.insert(0, "0")


# A-ONE1-FRAME3-species one ratio of carbon quantity
one_qty3 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one_qty3.place(x=200+100+100, y=25)
one_qty3.insert(0, "0")

# A-ONE2-CHECKBUTTON species one title
one_2 = Checkbutton(label_1_1_1_1_1, text="物质2", variable=one_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=one2_chk)
one_2.place(x=36, y=25+20)

# A-ONE2-FRAME0-species one quantity
one2_qty0 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
one2_qty0.place(x=100, y=25+20)

# A-ONE2-FRAME1-species one quantity
one2_qty1 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one2_qty1.place(x=200, y=25+20)
one2_qty1.insert(0, "0")

# A-ONE2-FRAME2-species one ratio of carbon transformation
one2_qty2 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one2_qty2.place(x=200+100, y=25+20)
one2_qty2.insert(0, "0")

# A-ONE2-FRAME3-species one ratio of carbon quantity
one2_qty3 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one2_qty3.place(x=200+100+100, y=25+20)
one2_qty3.insert(0, "0")

# A-ONE3-CHECKBUTTON species one title
one_3 = Checkbutton(label_1_1_1_1_1, text="物质3", variable=one_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=one3_chk)
one_3.place(x=36, y=25+20+20)

# A-ONE3-FRAME0-species one quantity
one3_qty0 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
one3_qty0.place(x=100, y=25+20+20)

# A-ONE3-FRAME1-species one quantity
one3_qty1 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one3_qty1.place(x=200, y=25+20+20)
one3_qty1.insert(0, "0")

# A-ONE3-FRAME2-species one ratio of carbon transformation
one3_qty2 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one3_qty2.place(x=200+100, y=25+20+20)
one3_qty2.insert(0, "0")

# A-ONE3-FRAME3-species one ratio of carbon quantity
one3_qty3 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one3_qty3.place(x=200+100+100, y=25+20+20)
one3_qty3.insert(0, "0")

# A-ONE4-CHECKBUTTON species one title
one_4 = Checkbutton(label_1_1_1_1_1, text="物质4", variable=one_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=one4_chk)
one_4.place(x=36, y=25+20+20+20)

# A-ONE4-FRAME0-species one quantity
one4_qty0 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
one4_qty0.place(x=100, y=25+20+20+20)

# A-ONE4-FRAME1-species one quantity
one4_qty1 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one4_qty1.place(x=200, y=25+20+20+20)
one4_qty1.insert(0, "0")

# A-ONE4-FRAME2-species one ratio of carbon transformation
one4_qty2 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one4_qty2.place(x=200+100, y=25+20+20+20)
one4_qty2.insert(0, "0")

# A-ONE4-FRAME3-species one ratio of carbon quantity
one4_qty3 = Entry(label_1_1_1_1_1, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
one4_qty3.place(x=200+100+100, y=25+20+20+20)
one4_qty3.insert(0, "0")

# A-font signal
l0 = Label(label_1_1_1_1_1, text="物质名称   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
l0.place(x=100, y=4)

l1 = Label(label_1_1_1_1_1, text="用量/吨   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
l1.place(x=200, y=4)

l2 = Label(label_1_1_1_1_1, text="CRi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
l2.place(x=200+100, y=4)

l3 = Label(label_1_1_1_1_1, text="CFi  ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
l3.place(x=200+100+100, y=4)


############section B #####################################
# B-ONE1
two_var1 = IntVar()
two_var2 = IntVar()
two_var3 = IntVar()
two_var4 = IntVar()
# B-ONE1-CHECKBUTTON species one title
two_1 = Checkbutton(label_1_1_1_1_2, text="物质1", variable=two_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=two1_chk)
two_1.place(x=36, y=25)

# B-ONE1-FRAME0-species one quantity
two1_qty0 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
two1_qty0.place(x=100, y=25)

# B-ONE1-FRAME1-species one quantity
two1_qty1 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two1_qty1.place(x=200, y=25)
two1_qty1.insert(0, "0")

# B-ONE1-FRAME2-species one ratio of carbon transformation
two1_qty2 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two1_qty2.place(x=200+100, y=25)
two1_qty2.insert(0, "0")

# B-ONE1-FRAME3-species one ratio of carbon quantity
two1_qty3 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two1_qty3.place(x=200+100+100, y=25)
two1_qty3.insert(0, "0")

# B-ONE2-CHECKBUTTON species one title
two_2 = Checkbutton(label_1_1_1_1_2, text="物质2", variable=two_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=two2_chk)
two_2.place(x=36, y=25+20)

# B-ONE2-FRAME0-species one quantity
two2_qty0 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
two2_qty0.place(x=100, y=25+20)

# B-ONE2-FRAME1-species one quantity
two2_qty1 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two2_qty1.place(x=200, y=25+20)
two2_qty1.insert(0, "0")

# B-ONE2-FRAME2-species one ratio of carbon transformation
two2_qty2 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two2_qty2.place(x=200+100, y=25+20)
two2_qty2.insert(0, "0")

# B-ONE2-FRAME3-species one ratio of carbon quantity
two2_qty3 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two2_qty3.place(x=200+100+100, y=25+20)
two2_qty3.insert(0, "0")

# B-ONE3-CHECKBUTTON species one title
two_3 = Checkbutton(label_1_1_1_1_2, text="物质3", variable=two_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=two3_chk)
two_3.place(x=36, y=25+20+20)

# B-ONE3-FRAME0-species one quantity
two3_qty0 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
two3_qty0.place(x=100, y=25+20+20)

# B-ONE3-FRAME1-species one quantity
two3_qty1 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two3_qty1.place(x=200, y=25+20+20)
two3_qty1.insert(0, "0")

# B-ONE3-FRAME2-species one ratio of carbon transformation
two3_qty2 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two3_qty2.place(x=200+100, y=25+20+20)
two3_qty2.insert(0, "0")

# A-ONE3-FRAME3-species one ratio of carbon quantity
two3_qty3 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two3_qty3.place(x=200+100+100, y=25+20+20)
two3_qty3.insert(0, "0")

# B-ONE4-CHECKBUTTON species one title
two_4 = Checkbutton(label_1_1_1_1_2, text="物质4", variable=two_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=two4_chk)
two_4.place(x=36, y=25+20+20+20)

# B-ONE4-FRAME0-species one quantity
two4_qty0 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
two4_qty0.place(x=100, y=25+20+20+20)

# B-ONE4-FRAME1-species one quantity
two4_qty1 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two4_qty1.place(x=200, y=25+20+20+20)
two4_qty1.insert(0, "0")

# B-ONE4-FRAME2-species one ratio of carbon transformation
two4_qty2 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two4_qty2.place(x=200+100, y=25+20+20+20)
two4_qty2.insert(0, "0")

# B-ONE4-FRAME3-species one ratio of carbon quantity
two4_qty3 = Entry(label_1_1_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
two4_qty3.place(x=200+100+100, y=25+20+20+20)
two4_qty3.insert(0, "0")

# B-font signal
B_l0 = Label(label_1_1_1_1_2, text="物质名称   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
B_l0.place(x=100, y=4)

B_l1 = Label(label_1_1_1_1_2, text="用量/吨   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
B_l1.place(x=200, y=4)

B_l2 = Label(label_1_1_1_1_2, text="HVi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
B_l2.place(x=200+100, y=4)

B_l3 = Label(label_1_1_1_1_2, text="EFi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
B_l3.place(x=200+100+100, y=4)

# B-result surface
B_SP1_total = Button(label_1_1_1_1_2, text="碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableB_1)
B_SP1_total.place(x=485, y=2)

B_SP1_total_frame = Entry(label_1_1_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
B_SP1_total_frame.place(x=485, y=2+20)

B_SP2_total_frame = Entry(label_1_1_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
B_SP2_total_frame.place(x=485, y=2+20+20)

B_SP3_total_frame = Entry(label_1_1_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
B_SP3_total_frame.place(x=485, y=2+20+20+20)

B_SP4_total_frame = Entry(label_1_1_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
B_SP4_total_frame.place(x=485, y=2+20+20+20+20)
# 碳排放总计
B_SP_all_total = Button(label_1_1_1_1_2, text="碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableB_1)
B_SP_all_total.place(x=30, y=115)
B_SP_all_total_frame = Entry(label_1_1_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
B_SP_all_total_frame.place(x=45+80, y=115)

# page tab 6********************************************************************************
#B text review
frame6 = Frame(tab6, width=1880, height=1000, relief=RIDGE, borderwidth=5, bg='#248aa2') #change the area of DEC
frame6.place(x=0, y=0) #change the position of DEC

frame6_6 = Frame(frame6, width=1870, height=980, relief=RIDGE, borderwidth=3, bg='#248aa2',
                    highlightbackground="white", highlightcolor="white", highlightthickness=2)
frame6_6.place(x=0, y=0)

label_1_1_1_2 = LabelFrame(frame6_6, text="工艺过程CO2排放量计算", width=800, height=650,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2.place(x=2+20, y=2+20)

label_1_1_1_2_b = LabelFrame(frame6_6, text="工艺过程CO2排放量计算", width=800, height=800,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_b.place(x=2+800, y=2+20)

label_1_1_1_2_1 = LabelFrame(label_1_1_1_2, text="催化剂烧焦CO2排放-催化裂化", width=779-30-30, height=300,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_1.place(x=20, y=2)

label_1_1_1_2_2 = LabelFrame(label_1_1_1_2, text="催化剂烧焦CO2排放-催化重整等", width=779-30-30, height=147,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_2.place(x=20, y=280)

label_FCC = LabelFrame(label_1_1_1_2_1, text="方法一-催化裂化/催化裂解装置-统计期内的实际焦炭燃烧量进行计算", width=697, height=200,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_FCC.place(x=20, y=2)

label_FRH = LabelFrame(label_1_1_1_2_1, text="方法二-以鼓风机实际风量", width=697, height=200,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_FRH.place(x=20, y=2+130)

label_FRR = LabelFrame(label_1_1_1_2_2, text="催化重整，催化加氢装置", width=697, height=130,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_FRR.place(x=20, y=2)

label_1_1_1_2_2 = LabelFrame(label_1_1_1_2, text="制氢工艺CO2排放(动力站可参考制氢装置执行))", width=779-30-30, height=200, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_2.place(x=20, y=434)

label_1_1_1_2_2b = LabelFrame(label_1_1_1_2_b, text="制氢工艺CO2排放(动力站可参考制氢装置执行))", width=700, height=320, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_2b.place(x=20, y=2)

label_1_1_1_2_3 = LabelFrame(label_1_1_1_2_b, text="乙二醇生产工艺CO2排放", width=700, height=600, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_3.place(x=20, y=2+320)

label_1_1_1_2_4 = LabelFrame(label_1_1_1_2_b, text="灵活焦化装置CO2排放", width=700, height=600, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_4.place(x=20, y=2+320+140)

label_1_1_1_2_5 = LabelFrame(label_1_1_1_2_b, text="石灰石分解等CO2排放", width=700, height=600, font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_1_1_1_2_5.place(x=20, y=2+320+140+140)

label_steam = LabelFrame(label_1_1_1_2_2, text="采用蒸汽转化工艺的制氢装置(天然气、干气或石脑油为原料)", width=697, height=150,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_steam.place(x=20, y=2)

label_coke = LabelFrame(label_1_1_1_2_2b, text="采用煤（焦）为原料的制氢装置", width=680, height=150,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_coke.place(x=20, y=2)

label_CH4 = LabelFrame(label_1_1_1_2_2b, text="天然气制氢（简化计算）", width=680, height=150,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_CH4.place(x=20, y=2+150)

label_EO = LabelFrame(label_1_1_1_2_3, width=680, height=150,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_EO.place(x=20, y=2)

label_FC = LabelFrame(label_1_1_1_2_4, width=680, height=130,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_FC.place(x=20, y=2)

label_CACO3 = LabelFrame(label_1_1_1_2_5, width=680, height=130,  font=('宋体', 10, 'bold'),
                    fg='#248aa2')
label_CACO3.place(x=20, y=2)
############section C #####################################
# C-ONE1
three_var1 = IntVar()
three_var2 = IntVar()
three_var3 = IntVar()
three_var4 = IntVar()

three_1 = Checkbutton(label_FCC, text="物质1", variable=three_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=three1_chk)
three_1.place(x=12, y=25)

# C-ONE1-FRAME1-species one quantity
three1_qty1 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three1_qty1.place(x=76, y=25)
three1_qty1.insert(0, "0")

# C-ONE1-FRAME2-species one ratio of carbon transformation
three1_qty2 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three1_qty2.place(x=76+100, y=25)
three1_qty2.insert(0, "0")

# C-ONE2-CHECKBUTTON species one title
three_2 = Checkbutton(label_FCC, text="物质2", variable=three_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=three2_chk)
three_2.place(x=12, y=25+20)

# C-ONE2-FRAME1-species one quantity
three2_qty1 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three2_qty1.place(x=76, y=25+20)
three2_qty1.insert(0, "0")

# C-ONE2-FRAME2-species one ratio of carbon transformation
three2_qty2 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three2_qty2.place(x=76+100, y=25+20)
three2_qty2.insert(0, "0")
#

# C-ONE3-CHECKBUTTON species one title
three_3 = Checkbutton(label_FCC, text="物质3", variable=three_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=three3_chk)
three_3.place(x=12, y=25+20+20)

# C-ONE3-FRAME1-species one quantity
three3_qty1 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three3_qty1.place(x=76, y=25+20+20)
three3_qty1.insert(0, "0")

# C-ONE3-FRAME2-species one ratio of carbon transformation
three3_qty2 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three3_qty2.place(x=76+100, y=25+20+20)
three3_qty2.insert(0, "0")

# C-ONE4-CHECKBUTTON species one title
three_4 = Checkbutton(label_FCC, text="物质4", variable=three_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=three4_chk)
three_4.place(x=12, y=25+20+20+20)

# C-ONE4-FRAME1-species one quantity
three4_qty1 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three4_qty1.place(x=76, y=25+20+20+20)
three4_qty1.insert(0, "0")

# C-ONE4-FRAME2-species one ratio of carbon transformation
three4_qty2 = Entry(label_FCC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
three4_qty2.place(x=76+100, y=25+20+20+20)
three4_qty2.insert(0, "0")

# C-font signal
C_l1 = Label(label_FCC, text="烧焦量/吨   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
C_l1.place(x=76, y=4)

C_l2 = Label(label_FCC, text="碳含量测量值%(质量分数)", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
C_l2.place(x=76+100, y=4)

# C-result surface
C_SP1_total = Button(label_FCC, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableC_1)
C_SP1_total.place(x=361, y=2)

C_SP1_total_frame = Entry(label_FCC, width=15, borderwidth=4, relief=SUNKEN)
C_SP1_total_frame.place(x=361, y=2+20)

C_SP2_total_frame = Entry(label_FCC, width=15, borderwidth=4, relief=SUNKEN)
C_SP2_total_frame.place(x=361, y=2+20+20)

C_SP3_total_frame = Entry(label_FCC, width=15, borderwidth=4, relief=SUNKEN)
C_SP3_total_frame.place(x=361, y=2+20+20+20)

C_SP4_total_frame = Entry(label_FCC, width=15, borderwidth=4, relief=SUNKEN)
C_SP4_total_frame.place(x=361, y=2+20+20+20+20)
# 碳排放总计
C_SP_all_total = Button(label_FCC, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableC_1)

C_SP_all_total.place(x=476, y=2)
C_SP_all_total_frame = Entry(label_FCC, width=15, borderwidth=4, relief=SUNKEN)
C_SP_all_total_frame.place(x=476, y=2+20)

############section D #####################################
# D-ONE1
four_var1 = IntVar()
four_var2 = IntVar()
four_var3 = IntVar()
four_var4 = IntVar()

four_1 = Checkbutton(label_FRH, text="物质1", variable=four_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=four1_chk)
four_1.place(x=12, y=25)

# D-ONE1-FRAME1-species one quantity
four1_qty1 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four1_qty1.place(x=76, y=25)
four1_qty1.insert(0, "0")

# D-ONE1-FRAME2-species one ratio of carbon transformation
four1_qty2 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four1_qty2.place(x=76+100, y=25)
four1_qty2.insert(0, "0")

# D-ONE1-FRAME3-species one ratio of carbon transformation
four1_qty3 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four1_qty3.place(x=76+100+100, y=25)
four1_qty3.insert(0, "0")

# D-ONE1-FRAME4-species one ratio of carbon transformation
four1_qty4 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four1_qty4.place(x=76+100+100+100, y=25)
four1_qty4.insert(0, "0")

# D-ONE2-CHECKBUTTON species one title
four_2 = Checkbutton(label_FRH, text="物质2", variable=four_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=four2_chk)
four_2.place(x=12, y=25+20)

# D-ONE2-FRAME1-species one quantity
four2_qty1 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four2_qty1.place(x=76, y=25+20)
four2_qty1.insert(0, "0")

# D-ONE2-FRAME2-species one ratio of carbon transformation
four2_qty2 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four2_qty2.place(x=76+100, y=25+20)
four2_qty2.insert(0, "0")

# D-ONE2-FRAME3-species one ratio of carbon transformation
four2_qty3 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four2_qty3.place(x=76+100+100, y=25+20)
four2_qty3.insert(0, "0")

# D-ONE2-FRAME4-species one ratio of carbon transformation
four2_qty4 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four2_qty4.place(x=76+100+100+100, y=25+20)
four2_qty4.insert(0, "0")

# D-ONE3-CHECKBUTTON species one title
four_3 = Checkbutton(label_FRH, text="物质3", variable=four_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=four3_chk)
four_3.place(x=12, y=25+20+20)

# D-ONE3-FRAME1-species one quantity
four3_qty1 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four3_qty1.place(x=76, y=25+20+20)
four3_qty1.insert(0, "0")

# D-ONE3-FRAME2-species one ratio of carbon transformation
four3_qty2 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four3_qty2.place(x=76+100, y=25+20+20)
four3_qty2.insert(0, "0")

# D-ONE3-FRAME3-species one ratio of carbon transformation
four3_qty3 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four3_qty3.place(x=76+100+100, y=25+20+20)
four3_qty3.insert(0, "0")

# D-ONE3-FRAME4-species one ratio of carbon transformation
four3_qty4 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four3_qty4.place(x=76+100+100+100, y=25+20+20)
four3_qty4.insert(0, "0")

# D-ONE4-CHECKBUTTON species one title
four_4 = Checkbutton(label_FRH, text="物质4", variable=four_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=four4_chk)
four_4.place(x=12, y=25+20+20+20)

# D-ONE4-FRAME1-species one quantity
four4_qty1 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four4_qty1.place(x=76, y=25+20+20+20)
four4_qty1.insert(0, "0")

# D-ONE4-FRAME2-species one ratio of carbon transformation
four4_qty2 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four4_qty2.place(x=76+100, y=25+20+20+20)
four4_qty2.insert(0, "0")

# D-ONE4-FRAME3-species one ratio of carbon transformation
four4_qty3 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four4_qty3.place(x=76+100+100, y=25+20+20+20)
four4_qty3.insert(0, "0")

# D-ONE4-FRAME4-species one ratio of carbon transformation
four4_qty4 = Entry(label_FRH, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
four4_qty4.place(x=76+100+100+100, y=25+20+20+20)
four4_qty4.insert(0, "0")
# D-font signal
D_l1 = Label(label_FRH, text="ARi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
D_l1.place(x=76, y=4)

D_l2 = Label(label_FRH, text="SORi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
D_l2.place(x=76+100, y=4)

D_l3 = Label(label_FRH, text="F-CO2", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
D_l3.place(x=76+100+100, y=4)

D_l4 = Label(label_FRH, text="F-CO", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
D_l4.place(x=76+100+100+100, y=4)

# D-result surface
D_SP1_total = Button(label_FRH, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableD_1)
D_SP1_total.place(x=361+100, y=2)

D_SP1_total_frame = Entry(label_FRH, width=15, borderwidth=4, relief=SUNKEN)
D_SP1_total_frame.place(x=361+100, y=2+20)

D_SP2_total_frame = Entry(label_FRH, width=15, borderwidth=4, relief=SUNKEN)
D_SP2_total_frame.place(x=361+100, y=2+20+20)

D_SP3_total_frame = Entry(label_FRH, width=15, borderwidth=4, relief=SUNKEN)
D_SP3_total_frame.place(x=361+100, y=2+20+20+20)

D_SP4_total_frame = Entry(label_FRH, width=15, borderwidth=4, relief=SUNKEN)
D_SP4_total_frame.place(x=361+100, y=2+20+20+20+20)

# 碳排放总计
D_SP_all_total = Button(label_FRH, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableD_1)

D_SP_all_total.place(x=476+100, y=2)
D_SP_all_total_frame = Entry(label_FRH, width=15, borderwidth=4, relief=SUNKEN)
D_SP_all_total_frame.place(x=476+100, y=2+20)

###########section E #####################################
# E-ONE1
five_var1 = IntVar()
five_var2 = IntVar()
five_var3 = IntVar()
five_var4 = IntVar()

five_1 = Checkbutton(label_FRR, text="物质1", variable=five_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=five1_chk)
five_1.place(x=12, y=25)

# E-ONE1-FRAME1-species one quantity
five1_qty1 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five1_qty1.place(x=76, y=25)
five1_qty1.insert(0, "0")

# E-ONE1-FRAME2-species one ratio of carbon transformation
five1_qty2 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five1_qty2.place(x=76+100, y=25)
five1_qty2.insert(0, "0")

# E-ONE1-FRAME3-species one ratio of carbon transformation
five1_qty3 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five1_qty3.place(x=76+100+100, y=25)
five1_qty3.insert(0, "0")

# E-ONE2-CHECKBUTTON species one title
five_2 = Checkbutton(label_FRR, text="物质2", variable=five_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=five2_chk)
five_2.place(x=12, y=25+20)

# E-ONE2-FRAME1-species one quantity
five2_qty1 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five2_qty1.place(x=76, y=25+20)
five2_qty1.insert(0, "0")

# E-ONE2-FRAME2-species one ratio of carbon transformation
five2_qty2 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five2_qty2.place(x=76+100, y=25+20)
five2_qty2.insert(0, "0")

# E-ONE2-FRAME3-species one ratio of carbon transformation
five2_qty3 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five2_qty3.place(x=76+100+100, y=25+20)
five2_qty3.insert(0, "0")

# E-ONE3-CHECKBUTTON species one title
five_3 = Checkbutton(label_FRR, text="物质3", variable=five_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=five3_chk)
five_3.place(x=12, y=25+20+20)

# E-ONE3-FRAME1-species one quantity
five3_qty1 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five3_qty1.place(x=76, y=25+20+20)
five3_qty1.insert(0, "0")

# E-ONE3-FRAME2-species one ratio of carbon transformation
five3_qty2 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five3_qty2.place(x=76+100, y=25+20+20)
five3_qty2.insert(0, "0")

# E-ONE3-FRAME3-species one ratio of carbon transformation
five3_qty3 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five3_qty3.place(x=76+100+100, y=25+20+20)
five3_qty3.insert(0, "0")

# E-ONE4-CHECKBUTTON species one title
five_4 = Checkbutton(label_FRR, text="物质4", variable=five_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=five4_chk)
five_4.place(x=12, y=25+20+20+20)

# E-ONE4-FRAME1-species one quantity
five4_qty1 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five4_qty1.place(x=76, y=25+20+20+20)
five4_qty1.insert(0, "0")

# E-ONE4-FRAME2-species one ratio of carbon transformation
five4_qty2 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five4_qty2.place(x=76+100, y=25+20+20+20)
five4_qty2.insert(0, "0")

# E-ONE4-FRAME3-species one ratio of carbon transformation
five4_qty3 = Entry(label_FRR, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
five4_qty3.place(x=76+100+100, y=25+20+20+20)
five4_qty3.insert(0, "0")

# E-font signal
E_l1 = Label(label_FRR, text="CQi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
E_l1.place(x=76, y=4)

E_l2 = Label(label_FRR, text="ICi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
E_l2.place(x=76+100, y=4)

E_l3 = Label(label_FRR, text="RCi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
E_l3.place(x=76+100+100, y=4)

# E-result surface
E_SP1_total = Button(label_FRR, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableE_1)
E_SP1_total.place(x=361+100, y=2)

E_SP1_total_frame = Entry(label_FRR, width=15, borderwidth=4, relief=SUNKEN)
E_SP1_total_frame.place(x=361+100, y=2+20)

E_SP2_total_frame = Entry(label_FRR, width=15, borderwidth=4, relief=SUNKEN)
E_SP2_total_frame.place(x=361+100, y=2+20+20)

E_SP3_total_frame = Entry(label_FRR, width=15, borderwidth=4, relief=SUNKEN)
E_SP3_total_frame.place(x=361+100, y=2+20+20+20)

E_SP4_total_frame = Entry(label_FRR, width=15, borderwidth=4, relief=SUNKEN)
E_SP4_total_frame.place(x=361+100, y=2+20+20+20+20)
# 碳排放总计
E_SP_all_total = Button(label_FRR, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableE_1)

E_SP_all_total.place(x=476+100, y=2)
E_SP_all_total_frame = Entry(label_FRR, width=15, borderwidth=4, relief=SUNKEN)
E_SP_all_total_frame.place(x=476+100, y=2+20)

############section F #####################################
# F-ONE1
six_var1 = IntVar()
six_var2 = IntVar()
six_var3 = IntVar()
six_var4 = IntVar()

six_1 = Checkbutton(label_steam, text="物质1", variable=six_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=six1_chk)
six_1.place(x=12, y=25)

# F-ONE1-FRAME1-species one quantity
six1_qty1 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six1_qty1.place(x=76, y=25)
six1_qty1.insert(0, "0")

# F-ONE1-FRAME2-species one ratio of carbon transformation
six1_qty2 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six1_qty2.place(x=76+100, y=25)
six1_qty2.insert(0, "0")

# F-ONE1-FRAME3-species one ratio of carbon transformation
six1_qty3 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six1_qty3.place(x=76+100+100, y=25)
six1_qty3.insert(0, "0")

# F-ONE2-CHECKBUTTON species one title
six_2 = Checkbutton(label_steam, text="物质2", variable=six_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=six2_chk)
six_2.place(x=12, y=25+20)

# F-ONE2-FRAME1-species one quantity
six2_qty1 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six2_qty1.place(x=76, y=25+20)
six2_qty1.insert(0, "0")

# F-ONE2-FRAME2-species one ratio of carbon transformation
six2_qty2 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six2_qty2.place(x=76+100, y=25+20)
six2_qty2.insert(0, "0")

# F-ONE2-FRAME3-species one ratio of carbon transformation
six2_qty3 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six2_qty3.place(x=76+100+100, y=25+20)
six2_qty3.insert(0, "0")

# F-ONE3-CHECKBUTTON species one title
six_3 = Checkbutton(label_steam, text="物质3", variable=six_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=six3_chk)
six_3.place(x=12, y=25+20+20)

# F-ONE3-FRAME1-species one quantity
six3_qty1 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six3_qty1.place(x=76, y=25+20+20)
six3_qty1.insert(0, "0")

# F-ONE3-FRAME2-species one ratio of carbon transformation
six3_qty2 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six3_qty2.place(x=76+100, y=25+20+20)
six3_qty2.insert(0, "0")

# F-ONE3-FRAME3-species one ratio of carbon transformation
six3_qty3 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six3_qty3.place(x=76+100+100, y=25+20+20)
six3_qty3.insert(0, "0")

# F-ONE4-CHECKBUTTON species one title
six_4 = Checkbutton(label_steam, text="物质4", variable=six_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=six4_chk)
six_4.place(x=12, y=25+20+20+20)

# F-ONE4-FRAME1-species one quantity
six4_qty1 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six4_qty1.place(x=76, y=25+20+20+20)
six4_qty1.insert(0, "0")

# F-ONE4-FRAME2-species one ratio of carbon transformation
six4_qty2 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six4_qty2.place(x=76+100, y=25+20+20+20)
six4_qty2.insert(0, "0")

# F-ONE4-FRAME3-species one ratio of carbon transformation
six4_qty3 = Entry(label_steam, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
six4_qty3.place(x=76+100+100, y=25+20+20+20)
six4_qty3.insert(0, "0")

# F-font signal
F_l1 = Label(label_steam, text="HQi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
F_l1.place(x=76, y=4)

F_l2 = Label(label_steam, text="HFi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
F_l2.place(x=76+100, y=4)

F_l3 = Label(label_steam, text="HHi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
F_l3.place(x=76+100+100, y=4)

# F-result surface
F_SP1_total = Button(label_steam, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableF_1)
F_SP1_total.place(x=361+100, y=2)

F_SP1_total_frame = Entry(label_steam, width=15, borderwidth=4, relief=SUNKEN)
F_SP1_total_frame.place(x=361+100, y=2+20)

F_SP2_total_frame = Entry(label_steam, width=15, borderwidth=4, relief=SUNKEN)
F_SP2_total_frame.place(x=361+100, y=2+20+20)

F_SP3_total_frame = Entry(label_steam, width=15, borderwidth=4, relief=SUNKEN)
F_SP3_total_frame.place(x=361+100, y=2+20+20+20)

F_SP4_total_frame = Entry(label_steam, width=15, borderwidth=4, relief=SUNKEN)
F_SP4_total_frame.place(x=361+100, y=2+20+20+20+20)
# 碳排放总计
F_SP_all_total = Button(label_steam, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableF_1)

F_SP_all_total.place(x=476+100, y=2)
F_SP_all_total_frame = Entry(label_steam, width=15, borderwidth=4, relief=SUNKEN)
F_SP_all_total_frame.place(x=476+100, y=2+20)

############section G #####################################
# G-ONE1
seven_var1 = IntVar()
seven_var2 = IntVar()
seven_var3 = IntVar()
seven_var4 = IntVar()

seven_1 = Checkbutton(label_coke, text="物质1", variable=seven_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=seven1_chk)
seven_1.place(x=12, y=25)

# G-ONE1-FRAME1-species one quantity
seven1_qty1 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven1_qty1.place(x=76, y=25)
seven1_qty1.insert(0, "0")

# G-ONE1-FRAME2-species one ratio of carbon transformation
seven1_qty2 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven1_qty2.place(x=76+100, y=25)
seven1_qty2.insert(0, "0")

# G-ONE1-FRAME3-species one ratio of carbon transformation
seven1_qty3 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven1_qty3.place(x=76+100+100, y=25)
seven1_qty3.insert(0, "0")

# G-ONE1-FRAME4-species one ratio of carbon transformation
seven1_qty4 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven1_qty4.place(x=76+100+100+100, y=25)
seven1_qty4.insert(0, "0")

# G-ONE1-FRAME5-species one ratio of carbon transformation
seven1_qty5 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven1_qty5.place(x=76+100+100+100+100, y=25)
seven1_qty5.insert(0, "0")

# G-ONE2-CHECKBUTTON species one title
seven_2 = Checkbutton(label_coke, text="物质2", variable=seven_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=seven2_chk)
seven_2.place(x=12, y=25+20)

# G-ONE2-FRAME1-species one quantity
seven2_qty1 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven2_qty1.place(x=76, y=25+20)
seven2_qty1.insert(0, "0")

# G-ONE2-FRAME2-species one ratio of carbon transformation
seven2_qty2 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven2_qty2.place(x=76+100, y=25+20)
seven2_qty2.insert(0, "0")

# G-ONE2-FRAME3-species one ratio of carbon transformation
seven2_qty3 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven2_qty3.place(x=76+100+100, y=25+20)
seven2_qty3.insert(0, "0")

# G-ONE2-FRAME4-species one ratio of carbon transformation
seven2_qty4 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven2_qty4.place(x=76+100+100+100, y=25+20)
seven2_qty4.insert(0, "0")

# G-ONE2-FRAME5-species one ratio of carbon transformation
seven2_qty5 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven2_qty5.place(x=76+100+100+100+100, y=25+20)
seven2_qty5.insert(0, "0")

# G-ONE3-CHECKBUTTON species one title
seven_3 = Checkbutton(label_coke, text="物质3", variable=seven_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=seven3_chk)
seven_3.place(x=12, y=25+20+20)

# G-ONE3-FRAME1-species one quantity
seven3_qty1 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven3_qty1.place(x=76, y=25+20+20)
seven3_qty1.insert(0, "0")

# G-ONE3-FRAME2-species one ratio of carbon transformation
seven3_qty2 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven3_qty2.place(x=76+100, y=25+20+20)
seven3_qty2.insert(0, "0")

# G-ONE3-FRAME3-species one ratio of carbon transformation
seven3_qty3 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven3_qty3.place(x=76+100+100, y=25+20+20)
seven3_qty3.insert(0, "0")

# G-ONE3-FRAME3-species one ratio of carbon transformation
seven3_qty4 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven3_qty4.place(x=76+100+100+100, y=25+20+20)
seven3_qty4.insert(0, "0")

# G-ONE3-FRAME3-species one ratio of carbon transformation
seven3_qty5 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven3_qty5.place(x=76+100+100+100+100, y=25+20+20)
seven3_qty5.insert(0, "0")

# G-ONE4-CHECKBUTTON species one title
seven_4 = Checkbutton(label_coke, text="物质4", variable=seven_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=seven4_chk)
seven_4.place(x=12, y=25+20+20+20)

# G-ONE4-FRAME1-species one quantity
seven4_qty1 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven4_qty1.place(x=76, y=25+20+20+20)
seven4_qty1.insert(0, "0")

# G-ONE4-FRAME2-species one ratio of carbon transformation
seven4_qty2 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven4_qty2.place(x=76+100, y=25+20+20+20)
seven4_qty2.insert(0, "0")

# G-ONE4-FRAME3-species one ratio of carbon transformation
seven4_qty3 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven4_qty3.place(x=76+100+100, y=25+20+20+20)
seven4_qty3.insert(0, "0")

# G-ONE4-FRAME4-species one ratio of carbon transformation
seven4_qty4 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven4_qty4.place(x=76+100+100+100, y=25+20+20+20)
seven4_qty4.insert(0, "0")

# G-ONE4-FRAME5-species one ratio of carbon transformation
seven4_qty5 = Entry(label_coke, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
seven4_qty5.place(x=76+100+100+100+100, y=25+20+20+20)
seven4_qty5.insert(0, "0")
# G-font signal
G_l1 = Label(label_coke, text="HQi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
G_l1.place(x=76, y=4)

G_l2 = Label(label_coke, text="HFi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
G_l2.place(x=76+100, y=4)

G_l3 = Label(label_coke, text="HRi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
G_l3.place(x=76+100+100, y=4)

G_l4 = Label(label_coke, text="HZi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
G_l4.place(x=76+100+100+100, y=4)

G_l5 = Label(label_coke, text="HHi", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
G_l5.place(x=76+100+100+100+100, y=4)

# G-result surface
G_SP1_total = Button(label_coke, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableG_1)
G_SP1_total.place(x=361+100+100, y=2)

G_SP1_total_frame = Entry(label_coke, width=15, borderwidth=4, relief=SUNKEN)
G_SP1_total_frame.place(x=361+100+100, y=2+20)

G_SP2_total_frame = Entry(label_coke, width=15, borderwidth=4, relief=SUNKEN)
G_SP2_total_frame.place(x=361+100+100, y=2+20+20)

G_SP3_total_frame = Entry(label_coke, width=15, borderwidth=4, relief=SUNKEN)
G_SP3_total_frame.place(x=361+100+100, y=2+20+20+20)

G_SP4_total_frame = Entry(label_coke, width=15, borderwidth=4, relief=SUNKEN)
G_SP4_total_frame.place(x=361+100+100, y=2+20+20+20+20)
# 碳排放总计
G_SP_all_total = Button(label_coke, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableG_1)

G_SP_all_total.place(x=361+100, y=2)
G_SP_all_total_frame = Entry(label_coke, width=15, borderwidth=4, relief=SUNKEN)
G_SP_all_total_frame.place(x=361+100, y=2+20+20+20+20+20)

############section H #####################################
# H-ONE1
eight_var1 = IntVar()
eight_var2 = IntVar()
eight_var3 = IntVar()
eight_var4 = IntVar()

eight_1 = Checkbutton(label_CH4, text="物质1", variable=eight_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eight1_chk)
eight_1.place(x=12, y=25)

# H-ONE1-FRAME1-species one quantity
eight1_qty1 = Entry(label_CH4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eight1_qty1.place(x=76, y=25)
eight1_qty1.insert(0, "0")

# H-ONE2-CHECKBUTTON species one title
eight_2 = Checkbutton(label_CH4, text="物质2", variable=eight_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eight2_chk)
eight_2.place(x=12, y=25+20)

# H-ONE2-FRAME1-species one quantity
eight2_qty1 = Entry(label_CH4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eight2_qty1.place(x=76, y=25+20)
eight2_qty1.insert(0, "0")

# H-ONE3-CHECKBUTTON species one title
eight_3 = Checkbutton(label_CH4, text="物质3", variable=eight_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eight3_chk)
eight_3.place(x=12, y=25+20+20)

# H-ONE3-FRAME1-species one quantity
eight3_qty1 = Entry(label_CH4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eight3_qty1.place(x=76, y=25+20+20)
eight3_qty1.insert(0, "0")

# H-ONE4-CHECKBUTTON species one title
eight_4 = Checkbutton(label_CH4, text="物质4", variable=eight_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eight4_chk)
eight_4.place(x=12, y=25+20+20+20)

# H-ONE4-FRAME1-species one quantity
eight4_qty1 = Entry(label_CH4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eight4_qty1.place(x=76, y=25+20+20+20)
eight4_qty1.insert(0, "0")

# H-font signal
H_l1 = Label(label_CH4, text="TQi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
H_l1.place(x=76, y=4)

# H-result surface
H_SP1_total = Button(label_CH4, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableH_1)
H_SP1_total.place(x=161, y=2)

H_SP1_total_frame = Entry(label_CH4, width=15, borderwidth=4, relief=SUNKEN)
H_SP1_total_frame.place(x=161, y=2+20)

H_SP2_total_frame = Entry(label_CH4, width=15, borderwidth=4, relief=SUNKEN)
H_SP2_total_frame.place(x=161, y=2+20+20)

H_SP3_total_frame = Entry(label_CH4, width=15, borderwidth=4, relief=SUNKEN)
H_SP3_total_frame.place(x=161, y=2+20+20+20)

H_SP4_total_frame = Entry(label_CH4, width=15, borderwidth=4, relief=SUNKEN)
H_SP4_total_frame.place(x=161, y=2+20+20+20+20)

H_SP_all_total = Button(label_CH4, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableH_1)

H_SP_all_total.place(x=361, y=2)
H_SP_all_total_frame = Entry(label_CH4, width=15, borderwidth=4, relief=SUNKEN)
H_SP_all_total_frame.place(x=361, y=2+20)

############section I #####################################
# I-ONE1
nine_var1 = IntVar()
nine_var2 = IntVar()
nine_var3 = IntVar()
nine_var4 = IntVar()

nine_1 = Checkbutton(label_EO, text="物质1", variable=nine_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=nine1_chk)
nine_1.place(x=12, y=25)

# I-ONE1-FRAME1-species one quantity
nine1_qty1 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine1_qty1.place(x=76, y=25)
nine1_qty1.insert(0, "0")

# I-ONE1-FRAME2-species one quantity
nine1_qty2 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine1_qty2.place(x=76+100, y=25)
nine1_qty2.insert(0, "0")

# I-ONE1-FRAME3-species one quantity
nine1_qty3 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine1_qty3.place(x=76+100+100, y=25)
nine1_qty3.insert(0, "0")

# I-ONE1-FRAME4-species one quantity
nine1_qty4 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine1_qty4.place(x=76+100+100+100, y=25)
nine1_qty4.insert(0, "0")

# I-ONE2-CHECKBUTTON species one title
nine_2 = Checkbutton(label_EO, text="物质2", variable=nine_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=nine2_chk)
nine_2.place(x=12, y=25+20)

# I-ONE2-FRAME1-species one quantity
nine2_qty1 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine2_qty1.place(x=76, y=25+20)
nine2_qty1.insert(0, "0")

# I-ONE2-FRAME2-species one quantity
nine2_qty2 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine2_qty2.place(x=76+100, y=25+20)
nine2_qty2.insert(0, "0")

# I-ONE2-FRAME3-species one quantity
nine2_qty3 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine2_qty3.place(x=76+100+100, y=25+20)
nine2_qty3.insert(0, "0")

# I-ONE2-FRAME4-species one quantity
nine2_qty4 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine2_qty4.place(x=76+100+100+100, y=25+20)
nine2_qty4.insert(0, "0")

# I-ONE3-CHECKBUTTON species one title
nine_3 = Checkbutton(label_EO, text="物质3", variable=nine_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=nine3_chk)
nine_3.place(x=12, y=25+20+20)

# I-ONE3-FRAME1-species one quantity
nine3_qty1 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine3_qty1.place(x=76, y=25+20+20)
nine3_qty1.insert(0, "0")

# I-ONE3-FRAME2-species one quantity
nine3_qty2 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine3_qty2.place(x=76+100, y=25+20+20)
nine3_qty2.insert(0, "0")

# I-ONE3-FRAME3-species one quantity
nine3_qty3 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine3_qty3.place(x=76+100+100, y=25+20+20)
nine3_qty3.insert(0, "0")

# I-ONE3-FRAME4-species one quantity
nine3_qty4 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine3_qty4.place(x=76+100+100+100, y=25+20+20)
nine3_qty4.insert(0, "0")

# I-ONE4-CHECKBUTTON species one title
nine_4 = Checkbutton(label_EO, text="物质4", variable=nine_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=nine4_chk)
nine_4.place(x=12, y=25+20+20+20)

# I-ONE4-FRAME1-species one quantity
nine4_qty1 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine4_qty1.place(x=76, y=25+20+20+20)
nine4_qty1.insert(0, "0")

# I-ONE4-FRAME2-species one quantity
nine4_qty2 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine4_qty2.place(x=76+100, y=25+20+20+20)
nine4_qty2.insert(0, "0")

# I-ONE4-FRAME3-species one quantity
nine4_qty3 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine4_qty3.place(x=76+100+100, y=25+20+20+20)
nine4_qty3.insert(0, "0")

# I-ONE4-FRAME4-species one quantity
nine4_qty4 = Entry(label_EO, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
nine4_qty4.place(x=76+100+100+100, y=25+20+20+20)
nine4_qty4.insert(0, "0")

# I-font signal
I_l1 = Label(label_EO, text="GFi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
I_l1.place(x=76, y=4)

I_l2 = Label(label_EO, text="ECi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
I_l2.place(x=76+100, y=4)

I_l3 = Label(label_EO, text="AFi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
I_l3.place(x=76+100+100, y=4)

I_l4 = Label(label_EO, text="ACi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
I_l4.place(x=76+100+100+100, y=4)
# H-result surface
I_SP1_total = Button(label_EO, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableI_1)
I_SP1_total.place(x=161+300, y=2)

I_SP1_total_frame = Entry(label_EO, width=15, borderwidth=4, relief=SUNKEN)
I_SP1_total_frame.place(x=161+300, y=2+20)

I_SP2_total_frame = Entry(label_EO, width=15, borderwidth=4, relief=SUNKEN)
I_SP2_total_frame.place(x=161+300, y=2+20+20)

I_SP3_total_frame = Entry(label_EO, width=15, borderwidth=4, relief=SUNKEN)
I_SP3_total_frame.place(x=161+300, y=2+20+20+20)

I_SP4_total_frame = Entry(label_EO, width=15, borderwidth=4, relief=SUNKEN)
I_SP4_total_frame.place(x=161+300, y=2+20+20+20+20)

I_SP_all_total = Button(label_EO, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableI_1)

I_SP_all_total.place(x=480+100, y=2)
I_SP_all_total_frame = Entry(label_EO, width=15, borderwidth=4, relief=SUNKEN)
I_SP_all_total_frame.place(x=480+100, y=2+20)

############section J #####################################
# J-ONE1
ten_var1 = IntVar()
ten_var2 = IntVar()
ten_var3 = IntVar()
ten_var4 = IntVar()

ten_1 = Checkbutton(label_FC, text="物质1", variable=ten_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ten1_chk)
ten_1.place(x=12, y=25)

# J-ONE1-FRAME1-species one quantity
ten1_qty1 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten1_qty1.place(x=76, y=25)
ten1_qty1.insert(0, "0")

# J-ONE1-FRAME2-species one quantity
ten1_qty2 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten1_qty2.place(x=76+100, y=25)
ten1_qty2.insert(0, "0")

# J-ONE1-FRAME3-species one quantity
ten1_qty3 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten1_qty3.place(x=76+100+100, y=25)
ten1_qty3.insert(0, "0")

# J-ONE2-CHECKBUTTON species one title
ten_2 = Checkbutton(label_FC, text="物质2", variable=ten_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ten2_chk)
ten_2.place(x=12, y=25+20)

# J-ONE2-FRAME1-species one quantity
ten2_qty1 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten2_qty1.place(x=76, y=25+20)
ten2_qty1.insert(0, "0")

# J-ONE2-FRAME2-species one quantity
ten2_qty2 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten2_qty2.place(x=76+100, y=25+20)
ten2_qty2.insert(0, "0")

# J-ONE2-FRAME3-species one quantity
ten2_qty3 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten2_qty3.place(x=76+100+100, y=25+20)
ten2_qty3.insert(0, "0")

# J-ONE3-CHECKBUTTON species one title
ten_3 = Checkbutton(label_FC, text="物质3", variable=ten_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ten3_chk)
ten_3.place(x=12, y=25+20+20)

# J-ONE3-FRAME1-species one quantity
ten3_qty1 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten3_qty1.place(x=76, y=25+20+20)
ten3_qty1.insert(0, "0")

# J-ONE3-FRAME2-species one quantity
ten3_qty2 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten3_qty2.place(x=76+100, y=25+20+20)
ten3_qty2.insert(0, "0")

# J-ONE3-FRAME3-species one quantity
ten3_qty3 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten3_qty3.place(x=76+100+100, y=25+20+20)
ten3_qty3.insert(0, "0")

# J-ONE4-CHECKBUTTON species one title
ten_4 = Checkbutton(label_FC, text="物质4", variable=ten_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ten4_chk)
ten_4.place(x=12, y=25+20+20+20)

# J-ONE4-FRAME1-species one quantity
ten4_qty1 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten4_qty1.place(x=76, y=25+20+20+20)
ten4_qty1.insert(0, "0")

# J-ONE4-FRAME2-species one quantity
ten4_qty2 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten4_qty2.place(x=76+100, y=25+20+20+20)
ten4_qty2.insert(0, "0")

# J-ONE4-FRAME3-species one quantity
ten4_qty3 = Entry(label_FC, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ten4_qty3.place(x=76+100+100, y=25+20+20+20)
ten4_qty3.insert(0, "0")

# J-font signal
J_l1 = Label(label_FC, text="QCi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
J_l1.place(x=76, y=4)

J_l2 = Label(label_FC, text="YCi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
J_l2.place(x=76+100, y=4)

J_l3 = Label(label_FC, text="ECi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
J_l3.place(x=76+100+100, y=4)

# J-result surface
J_SP1_total = Button(label_FC, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableJ_1)
J_SP1_total.place(x=161+300, y=2)

J_SP1_total_frame = Entry(label_FC, width=15, borderwidth=4, relief=SUNKEN)
J_SP1_total_frame.place(x=161+300, y=2+20)

J_SP2_total_frame = Entry(label_FC, width=15, borderwidth=4, relief=SUNKEN)
J_SP2_total_frame.place(x=161+300, y=2+20+20)

J_SP3_total_frame = Entry(label_FC, width=15, borderwidth=4, relief=SUNKEN)
J_SP3_total_frame.place(x=161+300, y=2+20+20+20)

J_SP4_total_frame = Entry(label_FC, width=15, borderwidth=4, relief=SUNKEN)
J_SP4_total_frame.place(x=161+300, y=2+20+20+20+20)

J_SP_all_total = Button(label_FC, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableJ_1)

J_SP_all_total.place(x=480+100, y=2)
J_SP_all_total_frame = Entry(label_FC, width=15, borderwidth=4, relief=SUNKEN)
J_SP_all_total_frame.place(x=480+100, y=2+20)

############section K #####################################
# K-ONE1
eleven_var1 = IntVar()
eleven_var2 = IntVar()
eleven_var3 = IntVar()
eleven_var4 = IntVar()

eleven_1 = Checkbutton(label_CACO3, text="物质1", variable=eleven_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eleven1_chk)
eleven_1.place(x=12, y=25)

# K-ONE1-FRAME1-species one quantity
eleven1_qty1 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven1_qty1.place(x=76, y=25)
eleven1_qty1.insert(0, "0")

# K-ONE1-FRAME2-species one quantity
eleven1_qty2 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven1_qty2.place(x=76+100, y=25)
eleven1_qty2.insert(0, "0")

# K-ONE2-CHECKBUTTON species one title
eleven_2 = Checkbutton(label_CACO3, text="物质2", variable=eleven_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eleven2_chk)
eleven_2.place(x=12, y=25+20)

# K-ONE2-FRAME1-species one quantity
eleven2_qty1 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven2_qty1.place(x=76, y=25+20)
eleven2_qty1.insert(0, "0")

# K-ONE2-FRAME2-species one quantity
eleven2_qty2 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven2_qty2.place(x=76+100, y=25+20)
eleven2_qty2.insert(0, "0")

# K-ONE3-CHECKBUTTON species one title
eleven_3 = Checkbutton(label_CACO3, text="物质3", variable=eleven_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eleven3_chk)
eleven_3.place(x=12, y=25+20+20)

# K-ONE3-FRAME1-species one quantity
eleven3_qty1 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven3_qty1.place(x=76, y=25+20+20)
eleven3_qty1.insert(0, "0")

# K-ONE3-FRAME2-species one quantity
eleven3_qty2 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven3_qty2.place(x=76+100, y=25+20+20)
eleven3_qty2.insert(0, "0")

# K-ONE4-CHECKBUTTON species one title
eleven_4 = Checkbutton(label_CACO3, text="物质4", variable=eleven_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=eleven4_chk)
eleven_4.place(x=12, y=25+20+20+20)

# K-ONE4-FRAME1-species one quantity
eleven4_qty1 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven4_qty1.place(x=76, y=25+20+20+20)
eleven4_qty1.insert(0, "0")

# K-ONE4-FRAME2-species one quantity
eleven4_qty2 = Entry(label_CACO3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
eleven4_qty2.place(x=76+100, y=25+20+20+20)
eleven4_qty2.insert(0, "0")

# K-font signal
K_l1 = Label(label_CACO3, text="QCi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
K_l1.place(x=76, y=4)

K_l2 = Label(label_CACO3, text="YCi   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
K_l2.place(x=76+100, y=4)

# K-result surface
K_SP1_total = Button(label_CACO3, text="碳排放小计", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableK_1)
K_SP1_total.place(x=161+300, y=2)

K_SP1_total_frame = Entry(label_CACO3, width=15, borderwidth=4, relief=SUNKEN)
K_SP1_total_frame.place(x=161+300, y=2+20)

K_SP2_total_frame = Entry(label_CACO3, width=15, borderwidth=4, relief=SUNKEN)
K_SP2_total_frame.place(x=161+300, y=2+20+20)

K_SP3_total_frame = Entry(label_CACO3, width=15, borderwidth=4, relief=SUNKEN)
K_SP3_total_frame.place(x=161+300, y=2+20+20+20)

K_SP4_total_frame = Entry(label_CACO3, width=15, borderwidth=4, relief=SUNKEN)
K_SP4_total_frame.place(x=161+300, y=2+20+20+20+20)

K_SP_all_total = Button(label_CACO3, text="碳排放总计", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableK_1)
K_SP_all_total.place(x=480+100, y=2)
K_SP_all_total_frame = Entry(label_CACO3, width=15, borderwidth=4, relief=SUNKEN)
K_SP_all_total_frame.place(x=480+100, y=2+20)

############section L #####################################
# L-ONE1
twelve_var1 = IntVar()
twelve_var2 = IntVar()
twelve_var3 = IntVar()
twelve_var4 = IntVar()

twelve_1 = Checkbutton(label_1_1_1_3, text="物质1", variable=twelve_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=twelve1_chk)
twelve_1.place(x=12, y=25)

# L-ONE1-FRAME1-species one quantity
twelve1_qty0 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
twelve1_qty0.place(x=76, y=25)

# L-ONE1-FRAME1-species one quantity
twelve1_qty1 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve1_qty1.place(x=176, y=25)
twelve1_qty1.insert(0, "0")

# L-ONE1-FRAME2-species one quantity
twelve1_qty2 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve1_qty2.place(x=76+200, y=25)
twelve1_qty2.insert(0, "0")

# L-ONE2-CHECKBUTTON species one title
twelve_2 = Checkbutton(label_1_1_1_3, text="物质2", variable=twelve_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=twelve2_chk)
twelve_2.place(x=12, y=25+20)

# L-ONE2-FRAME0-species one quantity
twelve2_qty0 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
twelve2_qty0.place(x=76, y=25+20)

# L-ONE2-FRAME1-species one quantity
twelve2_qty1 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve2_qty1.place(x=176, y=25+20)
twelve2_qty1.insert(0, "0")

# L-ONE2-FRAME2-species one quantity
twelve2_qty2 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve2_qty2.place(x=76+200, y=25+20)
twelve2_qty2.insert(0, "0")

# L-ONE3-CHECKBUTTON species one title
twelve_3 = Checkbutton(label_1_1_1_3, text="物质3", variable=twelve_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=twelve3_chk)
twelve_3.place(x=12, y=25+20+20)

# L-ONE3-FRAME0-species one quantity
twelve3_qty0 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
twelve3_qty0.place(x=76, y=25+20+20)

# L-ONE3-FRAME1-species one quantity
twelve3_qty1 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve3_qty1.place(x=176, y=25+20+20)
twelve3_qty1.insert(0, "0")

# L-ONE3-FRAME2-species one quantity
twelve3_qty2 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve3_qty2.place(x=76+200, y=25+20+20)
twelve3_qty2.insert(0, "0")

# L-ONE4-CHECKBUTTON species one title
twelve_4 = Checkbutton(label_1_1_1_3, text="物质4", variable=twelve_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=twelve4_chk)
twelve_4.place(x=12, y=25+20+20+20)

# L-ONE4-FRAME0-species one quantity
twelve4_qty0 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
twelve4_qty0.place(x=76, y=25+20+20+20)

# L-ONE4-FRAME1-species one quantity
twelve4_qty1 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve4_qty1.place(x=76+100, y=25+20+20+20)
twelve4_qty1.insert(0, "0")

# L-ONE4-FRAME2-species one quantity
twelve4_qty2 = Entry(label_1_1_1_3, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
twelve4_qty2.place(x=76+200, y=25+20+20+20)
twelve4_qty2.insert(0, "0")

# L-font signal
L_l0 = Label(label_1_1_1_3, text="物质名称   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
L_l0.place(x=76, y=4)

L_l1 = Label(label_1_1_1_3, text="AD   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
L_l1.place(x=100+76, y=4)

L_l2 = Label(label_1_1_1_3, text="EF   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
L_l2.place(x=76+200, y=4)

# L-result surface
L_SP1_total = Button(label_1_1_1_3, text="碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableL_1)
L_SP1_total.place(x=370, y=2)

L_SP1_total_frame = Entry(label_1_1_1_3, width=15, borderwidth=4, relief=SUNKEN)
L_SP1_total_frame.place(x=370, y=2+20)

L_SP2_total_frame = Entry(label_1_1_1_3, width=15, borderwidth=4, relief=SUNKEN)
L_SP2_total_frame.place(x=370, y=2+20+20)

L_SP3_total_frame = Entry(label_1_1_1_3, width=15, borderwidth=4, relief=SUNKEN)
L_SP3_total_frame.place(x=370, y=2+20+20+20)

L_SP4_total_frame = Entry(label_1_1_1_3, width=15, borderwidth=4, relief=SUNKEN)
L_SP4_total_frame.place(x=370, y=2+20+20+20+20)

L_SP_all_total = Button(label_1_1_1_3, text="碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableL_1)

L_SP_all_total.place(x=10, y=115)
L_SP_all_total_frame = Entry(label_1_1_1_3, width=15, borderwidth=4, relief=SUNKEN)
L_SP_all_total_frame.place(x=105, y=115)

############section M #####################################
# M-ONE1
thirteen_var1 = IntVar()
thirteen_var2 = IntVar()
thirteen_var3 = IntVar()
thirteen_var4 = IntVar()

thirteen_1 = Checkbutton(label_1_1_1_4, text="物质1", variable=thirteen_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=thirteen1_chk)
thirteen_1.place(x=12, y=25)

# M-ONE1-FRAME0-species one quantity
thirteen1_qty0 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
thirteen1_qty0.place(x=76, y=25)

# M-ONE1-FRAME1-species one quantity
thirteen1_qty1 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen1_qty1.place(x=76+100, y=25)
thirteen1_qty1.insert(0, "0")

# M-ONE1-FRAME2-species one quantity
thirteen1_qty2 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen1_qty2.place(x=76+200, y=25)
thirteen1_qty2.insert(0, "0")

# M-ONE2-CHECKBUTTON species one title
thirteen_2 = Checkbutton(label_1_1_1_4, text="物质2", variable=thirteen_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=thirteen2_chk)
thirteen_2.place(x=12, y=25+20)

# M-ONE2-FRAME0-species one quantity
thirteen2_qty0 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
thirteen2_qty0.place(x=76, y=25+20)

# M-ONE2-FRAME1-species one quantity
thirteen2_qty1 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen2_qty1.place(x=176, y=25+20)
thirteen2_qty1.insert(0, "0")

# M-ONE2-FRAME2-species one quantity
thirteen2_qty2 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen2_qty2.place(x=176+100, y=25+20)
thirteen2_qty2.insert(0, "0")

# M-ONE3-CHECKBUTTON species one title
thirteen_3 = Checkbutton(label_1_1_1_4, text="物质3", variable=thirteen_var3, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=thirteen3_chk)
thirteen_3.place(x=12, y=25+20+20)

# M-ONE3-FRAME0-species one quantity
thirteen3_qty0 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
thirteen3_qty0.place(x=76, y=25+20+20)


# M-ONE3-FRAME1-species one quantity
thirteen3_qty1 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen3_qty1.place(x=176, y=25+20+20)
thirteen3_qty1.insert(0, "0")

# M-ONE3-FRAME2-species one quantity
thirteen3_qty2 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen3_qty2.place(x=176+100, y=25+20+20)
thirteen3_qty2.insert(0, "0")

# M-ONE4-CHECKBUTTON species one title
thirteen_4 = Checkbutton(label_1_1_1_4, text="物质4", variable=thirteen_var4, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=thirteen4_chk)
thirteen_4.place(x=12, y=25+20+20+20)

# M-ONE4-FRAME0-species one quantity
thirteen4_qty0 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN)  #<class 'tkinter.Entry'>
thirteen4_qty0.place(x=76, y=25+20+20+20)

# M-ONE4-FRAME1-species one quantity
thirteen4_qty1 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen4_qty1.place(x=176, y=25+20+20+20)
thirteen4_qty1.insert(0, "0")

# M-ONE4-FRAME2-species one quantity
thirteen4_qty2 = Entry(label_1_1_1_4, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
thirteen4_qty2.place(x=176+100, y=25+20+20+20)
thirteen4_qty2.insert(0, "0")

# M-font signal
M_l0 = Label(label_1_1_1_4, text="物质名称   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
M_l0.place(x=76, y=4)

M_l1 = Label(label_1_1_1_4, text="AD   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
M_l1.place(x=176, y=4)

M_l2 = Label(label_1_1_1_4, text="EF   ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
M_l2.place(x=176+100, y=4)

# M-result surface
M_SP1_total = Button(label_1_1_1_4, text="碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stableM_1)
M_SP1_total.place(x=370, y=2)

M_SP1_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
M_SP1_total_frame.place(x=370, y=2+20)

M_SP2_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
M_SP2_total_frame.place(x=370, y=2+20+20)

M_SP3_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
M_SP3_total_frame.place(x=370, y=2+20+20+20)

M_SP4_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
M_SP4_total_frame.place(x=370, y=2+20+20+20+20)

M_SP_all_total = Button(label_1_1_1_4, text="碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#13eac9',
               fg="black", command=stableM_1)

M_SP_all_total.place(x=10, y=115)
M_SP_all_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
M_SP_all_total_frame.place(x=105, y=115)

# L+M-result surface
LM_SP_all_total = Button(label_1_1_1_4, text="间接碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#ffd1df',
               fg="black", command=stableLM_1)
LM_SP_all_total.place(x=10+250, y=115)
LM_SP_all_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
LM_SP_all_total_frame.place(x=105+250, y=115)

############section GAS_CACULATION_TOTAL #####################################

#Total Check Button
GAS_TOTAL_var1 = IntVar()
GAS_TOTAL_1 = Checkbutton(label_1_1_2, text="GAS_TOTAL", variable=GAS_TOTAL_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=GAS_TOTAL_chk)
GAS_TOTAL_1.place(x=36, y=25+10)

# GAS_TOTAL-ONE1-FRAME1-species one quantity
GAS_TOTAL_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
GAS_TOTAL_qty1.place(x=200, y=25+10)
GAS_TOTAL_qty1.insert(0, "0")



# GAS_TOTAL-font signal
# GAS_TOTAL_l1 = Label(label_1_1_2, text="燃料气总量/吨 ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
# GAS_TOTAL_l1.place(x=56, y=4+10)

GAS_TOTAL_l2 = Label(label_1_1_2, text="燃料气总量/吨", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
GAS_TOTAL_l2.place(x=196, y=4+10)

# SPECIES-font signal
SPECIES_l1 = Label(label_1_1_2, text="燃料气组分 ", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
SPECIES_l1.place(x=56, y=4+10+50)

SPECIES_l2 = Label(label_1_1_2, text="质量分数/%", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
SPECIES_l2.place(x=196, y=4+10+50)

SPECIES_l3 = Label(label_1_1_2, text="体积分数/%", font=('roboto', 10, 'bold'), bg='#248aa2', fg="#ffffff")
SPECIES_l3.place(x=296, y=4+10+50)

##############################MASS FRACTION#########################################
#SPECIES Check Button
# Methane
Methane_var1 = IntVar()
Methane_1 = Checkbutton(label_1_1_2, text="甲烷 Methane", variable=Methane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Methane_chk)
Methane_1.place(x=36, y=25+10+60)

# Ethane
Ethane_var1 = IntVar()
Ethane_1 = Checkbutton(label_1_1_2, text="乙烷 Ethane", variable=Ethane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Ethane_chk)
Ethane_1.place(x=36, y=25+10+60+20)

# Ethylene
Ethylene_var1 = IntVar()
Ethylene_1 = Checkbutton(label_1_1_2, text="乙烯 Ethylene", variable=Ethylene_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Ethylene_chk)
Ethylene_1.place(x=36, y=25+10+60+2*20)

# Propane
Propane_var1 = IntVar()
Propane_1 = Checkbutton(label_1_1_2, text="丙烷 Propane", variable=Propane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Propane_chk)
Propane_1.place(x=36, y=25+10+60+3*20)

# Propylene
Propylene_var1 = IntVar()
Propylene_1 = Checkbutton(label_1_1_2, text="丙烯 Propylene", variable=Propylene_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Propylene_chk)
Propylene_1.place(x=36, y=25+10+60+4*20)

# n-Butane
n_Butane_var1 = IntVar()
n_Butane_1 = Checkbutton(label_1_1_2, text="正丁烷 n_Butane", variable=n_Butane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=n_Butane_chk)
n_Butane_1.place(x=36, y=25+10+60+5*20)

# i-Butane
i_Butane_var1 = IntVar()
i_Butane_1 = Checkbutton(label_1_1_2, text="异丁烷 i_Butane", variable=i_Butane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=i_Butane_chk)
i_Butane_1.place(x=36, y=25+10+60+6*20)

# Butene-1
Butene_1_var1 = IntVar()
Butene_1_1 = Checkbutton(label_1_1_2, text="丁烯-1 Butene_1", variable=Butene_1_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Butene_1_chk)
Butene_1_1.place(x=36, y=25+10+60+7*20)

# i-Butene
i_Butene_var1 = IntVar()
i_Butene_1 = Checkbutton(label_1_1_2, text="异丁烯 iButene", variable=i_Butene_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=i_Butene_chk)
i_Butene_1.place(x=36, y=25+10+60+8*20)

# cis-trans-butene
ct_Butene_var1 = IntVar()
ct_Butene_1 = Checkbutton(label_1_1_2, text="顺反丁烯 cis-trans-butene", variable=ct_Butene_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ct_Butene_chk)
ct_Butene_1.place(x=36, y=25+10+60+9*20)

# Pentane
Pentane_var1 = IntVar()
Pentane_1 = Checkbutton(label_1_1_2, text="戊烷 Pentane", variable=Pentane_var1, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Pentane_chk)
Pentane_1.place(x=36, y=25+10+60+10*20)

# SPECIES-FRAME-species one quantity
# Methane
##############################MASS FRACTION#########################################
Methane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Methane_qty1.place(x=200, y=25+10+60)
Methane_qty1.insert(0, "0")

# Ethane
Ethane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethane_qty1.place(x=200, y=25+10+60+20)
Ethane_qty1.insert(0, "0")

# Ethylene
Ethylene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethylene_qty1.place(x=200, y=25+10+60+2*20)
Ethylene_qty1.insert(0, "0")

# Propane
Propane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propane_qty1.place(x=200, y=25+10+60+3*20)
Propane_qty1.insert(0, "0")

# Propylene
Propylene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propylene_qty1.place(x=200, y=25+10+60+4*20)
Propylene_qty1.insert(0, "0")

# n-Butane
n_Butane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
n_Butane_qty1.place(x=200, y=25+10+60+5*20)
n_Butane_qty1.insert(0, "0")

# i-Butane
i_Butane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butane_qty1.place(x=200, y=25+10+60+6*20)
i_Butane_qty1.insert(0, "0")

# Butene-1
Butene_1_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Butene_1_qty1.place(x=200, y=25+10+60+7*20)
Butene_1_qty1.insert(0, "0")

# i-Butene
i_Butene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butene_qty1.place(x=200, y=25+10+60+8*20)
i_Butene_qty1.insert(0, "0")

# cis-trans-butene
ct_Butene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ct_Butene_qty1.place(x=200, y=25+10+60+9*20)
ct_Butene_qty1.insert(0, "0")

# Pentane
Pentane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Pentane_qty1.place(x=200, y=25+10+60+10*20)
Pentane_qty1.insert(0, "0")

##############################VOLUMN FRACTION#########################################
#SPECIES Check Button
# Methane
Methane_var2 = IntVar()
Methane_2 = Checkbutton(label_1_1_2, text="甲烷 Methane", variable=Methane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Methane2_chk)
Methane_2.place(x=36+250, y=25+10+60)

# Ethane
Ethane_var2 = IntVar()
Ethane_2 = Checkbutton(label_1_1_2, text="乙烷 Ethane", variable=Ethane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Ethane2_chk)
Ethane_2.place(x=36+250, y=25+10+60+20)

# Ethylene
Ethylene_var2 = IntVar()
Ethylene_2 = Checkbutton(label_1_1_2, text="乙烯 Ethylene", variable=Ethylene_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Ethylene2_chk)
Ethylene_2.place(x=36+250, y=25+10+60+2*20)

# Propane
Propane_var2 = IntVar()
Propane_2 = Checkbutton(label_1_1_2, text="丙烷 Propane", variable=Propane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Propane2_chk)
Propane_2.place(x=36+250, y=25+10+60+3*20)

# Propylene
Propylene_var2 = IntVar()
Propylene_2 = Checkbutton(label_1_1_2, text="丙烯 Propylene", variable=Propylene_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Propylene2_chk)
Propylene_2.place(x=36+250, y=25+10+60+4*20)

# n-Butane
n_Butane_var2 = IntVar()
n_Butane_2 = Checkbutton(label_1_1_2, text="正丁烷 n_Butane", variable=n_Butane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=n_Butane2_chk)
n_Butane_2.place(x=36+250, y=25+10+60+5*20)

# i-Butane
i_Butane_var2 = IntVar()
i_Butane_2 = Checkbutton(label_1_1_2, text="异丁烷 i_Butane", variable=i_Butane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=i_Butane2_chk)
i_Butane_2.place(x=36+250, y=25+10+60+6*20)

# Butene-1
Butene_1_var2 = IntVar()
Butene_1_2 = Checkbutton(label_1_1_2, text="丁烯-1 Butene_1", variable=Butene_1_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Butene2_1_chk)
Butene_1_2.place(x=36+250, y=25+10+60+7*20)

# i-Butene
i_Butene_var2 = IntVar()
i_Butene_2 = Checkbutton(label_1_1_2, text="异丁烯 iButene", variable=i_Butene_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=i_Butene2_chk)
i_Butene_2.place(x=36+250, y=25+10+60+8*20)

# cis-trans-butene
ct_Butene_var2 = IntVar()
ct_Butene_2 = Checkbutton(label_1_1_2, text="顺反丁烯 cis-trans-butene", variable=ct_Butene_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=ct_Butene2_chk)
ct_Butene_2.place(x=36+250, y=25+10+60+9*20)

# Pentane
Pentane_var2 = IntVar()
Pentane_2 = Checkbutton(label_1_1_2, text="戊烷 Pentane", variable=Pentane_var2, font=('宋体', 10, 'bold'), onvalue=1, offvalue=0,
                    command=Pentane2_chk)
Pentane_2.place(x=36+250, y=25+10+60+10*20)

# SPECIES-FRAME-species one quantity
##############################MASS FRACTION#########################################
# Methane
Methane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Methane_qty1.place(x=200, y=25+10+60)
Methane_qty1.insert(0, "0")

# Ethane
Ethane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethane_qty1.place(x=200, y=25+10+60+20)
Ethane_qty1.insert(0, "0")

# Ethylene
Ethylene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethylene_qty1.place(x=200, y=25+10+60+2*20)
Ethylene_qty1.insert(0, "0")

# Propane
Propane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propane_qty1.place(x=200, y=25+10+60+3*20)
Propane_qty1.insert(0, "0")

# Propylene
Propylene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propylene_qty1.place(x=200, y=25+10+60+4*20)
Propylene_qty1.insert(0, "0")

# n-Butane
n_Butane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
n_Butane_qty1.place(x=200, y=25+10+60+5*20)
n_Butane_qty1.insert(0, "0")

# i-Butane
i_Butane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butane_qty1.place(x=200, y=25+10+60+6*20)
i_Butane_qty1.insert(0, "0")

# Butene-1
Butene_1_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Butene_1_qty1.place(x=200, y=25+10+60+7*20)
Butene_1_qty1.insert(0, "0")

# i-Butene
i_Butene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butene_qty1.place(x=200, y=25+10+60+8*20)
i_Butene_qty1.insert(0, "0")

# cis-trans-butene
ct_Butene_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ct_Butene_qty1.place(x=200, y=25+10+60+9*20)
ct_Butene_qty1.insert(0, "0")

# Pentane
Pentane_qty1 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Pentane_qty1.place(x=200, y=25+10+60+10*20)
Pentane_qty1.insert(0, "0")

##############################VOLUMN FRACTION#########################################
# Methane
Methane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Methane_qty2.place(x=200+250, y=25+10+60)
Methane_qty2.insert(0, "0")

# Ethane
Ethane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethane_qty2.place(x=200+250, y=25+10+60+20)
Ethane_qty2.insert(0, "0")

# Ethylene
Ethylene_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Ethylene_qty2.place(x=200+250, y=25+10+60+2*20)
Ethylene_qty2.insert(0, "0")

# Propane
Propane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propane_qty2.place(x=200+250, y=25+10+60+3*20)
Propane_qty2.insert(0, "0")

# Propylene
Propylene_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Propylene_qty2.place(x=200+250, y=25+10+60+4*20)
Propylene_qty2.insert(0, "0")

# n-Butane
n_Butane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
n_Butane_qty2.place(x=200+250, y=25+10+60+5*20)
n_Butane_qty2.insert(0, "0")

# i-Butane
i_Butane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butane_qty2.place(x=200+250, y=25+10+60+6*20)
i_Butane_qty2.insert(0, "0")

# Butene-1
Butene_1_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Butene_1_qty2.place(x=200+250, y=25+10+60+7*20)
Butene_1_qty2.insert(0, "0")

# i-Butene
i_Butene_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
i_Butene_qty2.place(x=200+250, y=25+10+60+8*20)
i_Butene_qty2.insert(0, "0")

# cis-trans-butene
ct_Butene_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
ct_Butene_qty2.place(x=200+250, y=25+10+60+9*20)
ct_Butene_qty2.insert(0, "0")

# Pentane
Pentane_qty2 = Entry(label_1_1_2, width=10, borderwidth=4, relief=SUNKEN, state='disabled')  #<class 'tkinter.Entry'>
Pentane_qty2.place(x=200+250, y=25+10+60+10*20)
Pentane_qty2.insert(0, "0")
############GAS_SPECIES_CARBON_total #####################################

#
# MASS-GAS_SPECIES_CARBON surface
GAS_SPECIES_CARBON_total = Button(label_1_1_2, text="质量分数-碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stable_GAS_TOTAL_MASS_CACULATION)
GAS_SPECIES_CARBON_total.place(x=370+160, y=2)

GAS_SPECIES_CARBON_total_frame = Entry(label_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
GAS_SPECIES_CARBON_total_frame.place(x=370+160, y=2+20)

# VOLUMN-GAS_SPECIES_CARBON surface
GAS_SPECIES_CARBON_total2 = Button(label_1_1_2, text="体积分数-碳排放小计/吨", relief=RAISED, font=('宋体', 10), bg='#ffff14',
               fg="black", command=stable_GAS_TOTAL_VOLUMN_CACULATION)
GAS_SPECIES_CARBON_total2.place(x=370+160, y=2+45)

GAS_SPECIES_CARBON_total2_frame = Entry(label_1_1_2, width=15, borderwidth=4, relief=SUNKEN)
GAS_SPECIES_CARBON_total2_frame.place(x=370+160, y=2+20+45)

#
# M_SP2_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
# M_SP2_total_frame.place(x=370, y=2+20+20)
#
# M_SP3_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
# M_SP3_total_frame.place(x=370, y=2+20+20+20)
#
# M_SP4_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
# M_SP4_total_frame.place(x=370, y=2+20+20+20+20)
#
# M_SP_all_total = Button(label_1_1_1_4, text="碳排放总计/吨", relief=RAISED, font=('宋体', 10), bg='#13eac9',
#                fg="black", command=stableM_1)
#
# M_SP_all_total.place(x=10, y=115)
# M_SP_all_total_frame = Entry(label_1_1_1_4, width=15, borderwidth=4, relief=SUNKEN)
# M_SP_all_total_frame.place(x=105, y=115)

# end********************************************************************************



root.mainloop()



if __name__ == '__main__':
    print("good")
############################################################################################################