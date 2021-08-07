#!bin/bash
clear

echo " ®=======================® "
echo "  Pembuat : Tegar Store          "
echo "  Batas Telp : 3             "
echo "  Tidak Bisa Pake 08/+62   "
echo "  Example:885876xxxxx      "
echo " ®=======================® "
figlet TELp | lolcat
echo '
[1], Prank
[2], Exit Tools
'
echo
read -p "Masukan Pilihan Anda : " pil
if [[ $pil == 1 ]]; then
read -p "Masukan No Target : " Nomor
link="https://id.jagreward.com/member/verify-mobile/$nomor"
curl -s $link
else
echo 'Terima Kasih Udah Pake Tools Gue'
exit
fi
echo