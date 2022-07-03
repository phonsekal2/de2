import streamlit as st
import pandas as pd
from docxtpl import DocxTemplate
from num2words import num2words
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from docx2pdf import convert
from datetime import datetime

st.title("Aplikasi Kuitansi")
#anggal = st.date_input("Pilih tanggal")
#tgl = tanggal.strftime("%d %B %Y")
#tgl2 = tgl.replace("January", "Januari").replace("February", "Februari").replace("March", "Maret").replace("May", "Mei").replace("June", "Juni").replace("July", "Juli").replace("August", "Agustus").replace("October", "Oktober").replace("December", "Desember")
#st.write(tgl2)
st.sidebar.title("Menu")
option = st.sidebar.selectbox("Pilih jenis kuitansi", ("Transpor Lokal", "Kegiatan", "Perjadin"))
if option == 'Transpor Lokal':
    st.write("Format menggunakan kuitansi transpor lokal")
    left, right = st.columns(2)
    right.write("")
    left.write("Silahkan isi data dulu:")
    form = left.form("template_form")
    nama = form.text_input("Nama")
    nip = form.text_input("Nip")
    mak = form.selectbox(
        "Pilih MAK",
        ["2020.EBA.062.F.524113", "2020.EBA.063.F.524113", "2020.EBA.065.F.524113"],
        index=0,
    )
    kegiatan = form.text_input("Nama kegiatan")
    lokasi = form.text_input("Tempat kegiatan")
    tanggal = form.date_input("Pilih tanggal")
    layanan = form.text_input("Dalam rangka")
    nilai = form.text_input("Nominal")
    #grade = form.slider("Grade", 1, 100, 60)
    submit = form.form_submit_button("Kirim")
    tgl = tanggal.strftime("%d %B %Y")
    tgl2 = tgl.replace("January", "Januari").replace("February", "Februari").replace("March", "Maret").replace("May", "Mei").replace("June", "Juni").replace("July", "Juli").replace("August", "Agustus").replace("October", "Oktober").replace("December", "Desember")
    st.write(tgl2)
    if submit:
        uang1 = float(nilai)
        thousands_separator = "."
        fractional_separator = ","
        currency = "Rp{:,.2f}".format(uang1)
        if thousands_separator == ".":
            main_currency, fractional_currency = currency.split(".")[0], currency.split(".")[1]
            new_main_currency = main_currency.replace(",", ".")
            currency = new_main_currency + fractional_separator + fractional_currency
        doc = DocxTemplate("kuitansiperjadinapp.docx")
        context = {
            "nama": nama,
            "nip": nip,
            "mak": mak,
            "kegiatan": kegiatan,
            "lokasi": lokasi,
            "tanggal": tgl2,
            "layanan": layanan,
            #"grade": f"{grade}/100",
            "terbilang": num2words(int(nilai), lang='id').title() + " Rupiah",
            "uang": currency
        
        }
        #st.write(context)
        output_name = f'download/{context["nama"]}.docx'
        doc.render(context)   
        doc.save(output_name)
        #convert(output_name, "hasil.pdf")
        with open(output_name, "rb") as file:
        #    btn = st.download_button(
         #           label="Download PDF",
          #          data=file,
           #         file_name="hasil.pdf",
            #        mime="application/octet-stream"
             #   )
            right.success("🎉 File kuitansi telah selesai dibuat")
            # st.write(html, unsafe_allow_html=True)
            # st.write("")
            right.download_button(
                "⬇️ Download File",
                data=file,
                file_name="Hasil.docx",
                mime="application/octet-stream",
            )
        


       
        
   
if option == 'Kegiatan':
    st.write("Klik kegiatan")
if option == 'Perjadin':
    st.write("Klik translok")


#st.sidebar.title("Laporan Keuangan")
#lk = st.sidebar.selectbox("Buat laporan", ("","Laporan keuangan",))
#st.write('You selected:', lk)