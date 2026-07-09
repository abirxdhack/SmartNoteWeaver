import subprocess, os, shutil, sys

FONTS = "/tmp/routine/fonts"

TEX = r"""\documentclass[8pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage[left=0.28cm,right=0.28cm,top=0.22cm,bottom=0.22cm]{geometry}
\usepackage[table]{xcolor}
\usepackage{array}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage[protrusion=false]{microtype}
\pagestyle{empty}
\hbadness=10000
\vbadness=10000
\sloppy
\tolerance=9999
\emergencystretch=25pt
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Latin Modern Roman}
\newfontfamily\bn[
  Path=./fonts/,
  Extension=.ttf,
  Script=Bengali,
  Ligatures=TeX,
  UprightFont=NotoSerifBengali-Regular,
  BoldFont=NotoSerifBengali-Bold,
  ItalicFont=NotoSerifBengali-Regular,
  BoldItalicFont=NotoSerifBengali-Bold
]{NotoSerifBengali-Regular}
\newcommand{\B}[1]{{\bn #1}}

\definecolor{hdr}{RGB}{55,55,55}
\definecolor{dayhdr}{RGB}{55,55,55}
\definecolor{sechdr}{RGB}{220,220,220}
\definecolor{timecol}{RGB}{240,240,240}
\definecolor{pray}{RGB}{230,230,230}
\definecolor{rowodd}{RGB}{248,248,248}
\definecolor{roweven}{RGB}{255,255,255}
\definecolor{tutor}{RGB}{235,235,235}
\definecolor{notebg}{RGB}{230,230,230}
\definecolor{firstpaper}{RGB}{255,255,255}
\definecolor{secondpaper}{RGB}{246,246,246}

\setlength{\tabcolsep}{1.4pt}
\setlength{\arrayrulewidth}{0.32pt}
\renewcommand{\arraystretch}{0.9}

\begin{document}
\noindent
\begin{tabularx}{\textwidth}{|>{\centering\arraybackslash}p{1.55cm}|*{7}{>{\centering\arraybackslash}X|}}
\hline
\multicolumn{8}{|c|}{\cellcolor{hdr}\color{white}\bfseries\large \B{স্মার্ট স্টাডি রুটিন} \textnormal{---} \B{আবির আরাফাত চৌধুরী, এইচএসসি ২০২৭}}\\
\hline
\rowcolor{dayhdr}
\color{white}\bfseries\small \B{সময়} &
\color{white}\bfseries\small \B{শনিবার} &
\color{white}\bfseries\small \B{রবিবার} &
\color{white}\bfseries\small \B{সোমবার} &
\color{white}\bfseries\small \B{মঙ্গলবার} &
\color{white}\bfseries\small \B{বুধবার} &
\color{white}\bfseries\small \B{বৃহস্পতিবার} &
\color{white}\bfseries\small \B{শুক্রবার} \\
\hline
\rowcolor{dayhdr}
\color{white}\tiny \B{---} &
\color{white}\tiny \B{১ম পত্র দিন} &
\color{white}\tiny \B{২য় পত্র দিন} &
\color{white}\tiny \B{১ম পত্র দিন} &
\color{white}\tiny \B{২য় পত্র দিন} &
\color{white}\tiny \B{১ম পত্র দিন} &
\color{white}\tiny \B{২য় পত্র দিন} &
\color{white}\tiny \B{মেগা রিভিউ} \\
\hline
\rowcolor{sechdr}
\multicolumn{8}{|c|}{\bfseries\small \B{সকাল}}\\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{৪:৩০--৫:০০} &
\multicolumn{7}{c|}{\scriptsize \B{ঘুম থেকে ওঠা} \textbf{৪:৩০} \quad\textbar\quad \textbf{\B{ফজর নামাজ ৪:৩০--৪:৫০}}}\\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৫:০০--৬:০০} &
\cellcolor{firstpaper}\tiny \B{পদার্থবিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{পদার্থবিজ্ঞান ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{রসায়ন ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{রসায়ন ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{উচ্চতর গণিত ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{উচ্চতর গণিত ২য় পত্র} &
\tiny \B{সবচেয়ে দুর্বল টপিক} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৬:০০--৭:০০} &
\cellcolor{firstpaper}\tiny \B{উচ্চতর গণিত ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{উচ্চতর গণিত ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{জীববিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{জীববিজ্ঞান ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{পদার্থবিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{পদার্থবিজ্ঞান ২য় পত্র} &
\tiny \B{মক পরীক্ষা (চলমান)} \\
\hline
\rowcolor{rowodd}
\scriptsize\bfseries \B{৭:০০--৮:০০} &
\multicolumn{7}{c|}{\scriptsize \B{নাস্তা, হাঁটাচলা, বিশ্রাম}}\\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৮:০০--৯:০০} &
\cellcolor{firstpaper}\tiny \B{রসায়ন ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{রসায়ন ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{পদার্থবিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{পদার্থবিজ্ঞান ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{রসায়ন ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{রসায়ন ২য় পত্র} &
\tiny \B{ফুল বোর্ড মক পরীক্ষা} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৯:১০--১০:১০} &
\cellcolor{firstpaper}\tiny \B{জীববিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{জীববিজ্ঞান ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{উচ্চতর গণিত ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{উচ্চতর গণিত ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{জীববিজ্ঞান ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{জীববিজ্ঞান ২য় পত্র} &
\tiny \B{মক (চলমান)} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{১০:২০--১১:২০} &
\cellcolor{firstpaper}\tiny \B{বাংলা ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{বাংলা ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{বাংলা ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{বাংলা ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{বাংলা ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{বাংলা ২য় পত্র} &
\tiny \B{মক (চলমান)} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{১১:৩০--১২:৩০} &
\cellcolor{firstpaper}\tiny \B{আইসিটি} &
\cellcolor{secondpaper}\tiny \B{আইসিটি} &
\cellcolor{firstpaper}\tiny \B{আইসিটি} &
\cellcolor{secondpaper}\tiny \B{আইসিটি} &
\cellcolor{firstpaper}\tiny \B{আইসিটি} &
\cellcolor{secondpaper}\tiny \B{আইসিটি} &
\tiny \B{উত্তরপত্র মিলানো} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{১২:৩০--১:০০} &
\cellcolor{firstpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\cellcolor{secondpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\cellcolor{firstpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\cellcolor{secondpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\cellcolor{firstpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\cellcolor{secondpaper}\tiny \B{মডেল প্রশ্ন সমাধান} &
\tiny \B{ভুল বিশ্লেষণ} \\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{১:২০--২:০০} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{যোহর নামাজ + দুপুরের খাবার}}}\\
\hline
\rowcolor{sechdr}
\multicolumn{8}{|c|}{\bfseries\small \B{বিকাল}}\\
\hline
\rowcolor{tutor}
\scriptsize\bfseries \B{২:০০--৩:০০} &
\tiny \B{লাঞ্চ, গোসল (২:০০--২:৩০)} &
\tiny \textbf{\B{নুর আলম স্যার (ইংরেজী)}} &
\tiny \B{লাঞ্চ, গোসল (২:০০--২:৩০)} &
\tiny \textbf{\B{নুর আলম স্যার (ইংরেজী)}} &
\tiny \B{লাঞ্চ, গোসল (২:০০--২:৩০)} &
\tiny \textbf{\B{নুর আলম স্যার (ইংরেজী)}} &
\tiny \B{স্বাধীন পড়াশোনা (বাংলা ১ম+২য় পত্র)} \\
\hline
\rowcolor{tutor}
\scriptsize\bfseries \B{২:৩০--৩:৩০} &
\tiny \textbf{\B{শাহিন স্যার (পদার্থবিজ্ঞান)}} &
\tiny \B{লাঞ্চ, গোসল (৩:০০--৩:৩০)} &
\tiny \textbf{\B{শাহিন স্যার (পদার্থবিজ্ঞান)}} &
\tiny \B{লাঞ্চ, গোসল (৩:০০--৩:৩০)} &
\tiny \textbf{\B{শাহিন স্যার (পদার্থবিজ্ঞান)}} &
\tiny \B{লাঞ্চ, গোসল (৩:০০--৩:৩০)} &
\tiny \B{স্বাধীন পড়াশোনা (আইসিটি রিভিশন)} \\
\hline
\rowcolor{rowodd}
\scriptsize\bfseries \B{৩:৩০--৪:০০} &
\multicolumn{7}{c|}{\scriptsize \B{বিকেলের নাস্তা, বিশ্রাম}}\\
\hline
\rowcolor{tutor}
\scriptsize\bfseries \B{৪:০০--৫:০০} &
\tiny \textbf{\B{মোরসালিন স্যার (উচ্চতর গণিত)}} &
\tiny \B{স্বাধীন পড়াশোনা (রসায়ন ২য় পত্র)} &
\tiny \textbf{\B{মোরসালিন স্যার (উচ্চতর গণিত)}} &
\tiny \B{স্বাধীন পড়াশোনা (জীববিজ্ঞান ২য় পত্র)} &
\tiny \textbf{\B{মোরসালিন স্যার (উচ্চতর গণিত)}} &
\tiny \B{স্বাধীন পড়াশোনা (পদার্থবিজ্ঞান ২য় পত্র)} &
\tiny \B{স্বাধীন পড়াশোনা (উচ্চতর গণিত রিভিশন)} \\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{৫:০০--৫:১৫} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{আসর নামাজ}} \B{(সবার জন্য; হেদায়েত স্যারের ক্লাস সংক্ষিপ্ত বিরতিতে থাকে)}}\\
\hline
\rowcolor{tutor}
\scriptsize\bfseries \B{৫:১৫--৬:০০} &
\tiny \B{স্বাধীন পড়াশোনা (জীববিজ্ঞান ১ম পত্র)} &
\tiny \textbf{\B{হেদায়েত স্যার (রসায়ন)}} &
\tiny \B{স্বাধীন পড়াশোনা (উচ্চতর গণিত ১ম পত্র)} &
\tiny \textbf{\B{হেদায়েত স্যার (রসায়ন)}} &
\tiny \B{স্বাধীন পড়াশোনা (পদার্থবিজ্ঞান ১ম পত্র)} &
\tiny \textbf{\B{হেদায়েত স্যার (রসায়ন)}} &
\tiny \B{স্বাধীন পড়াশোনা (রসায়ন রিভিশন)} \\
\hline
\rowcolor{rowodd}
\scriptsize\bfseries \B{৬:০০--৬:৩০} &
\multicolumn{7}{c|}{\scriptsize \B{হাঁটাচলা, হালকা খাবার, রিসেট}}\\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{৬:৫০--৭:১০} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{মাগরিব নামাজ}}}\\
\hline
\rowcolor{sechdr}
\multicolumn{8}{|c|}{\bfseries\small \B{সন্ধ্যা --- সেশন-৪ (৭:১০--১০:১০, প্রতিদিন)}}\\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৭:১০--৭:৫৫} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ১ম পত্র} &
\tiny \B{ব্যাকলগ ক্লিয়ারেন্স} \\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৮:০০--৮:৪৫} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\cellcolor{firstpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\cellcolor{secondpaper}\tiny \B{ইংরেজী ২য় পত্র} &
\tiny \B{বাংলা ১ম+২য় রিভিশন} \\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{৮:৪৫--৯:১০} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{এশা নামাজ + রাতের খাবার}} \B{(সেশন-৪ এর মাঝে সংক্ষিপ্ত বিরতি)}}\\
\hline
\cellcolor{timecol}\scriptsize\bfseries \B{৯:১০--১০:১০} &
\cellcolor{firstpaper}\tiny \B{পদার্থ+গণিত+রসায়ন দ্রুত রিভিশন} &
\cellcolor{secondpaper}\tiny \B{পদার্থ+গণিত+রসায়ন দ্রুত রিভিশন} &
\cellcolor{firstpaper}\tiny \B{রসায়ন+জীব+বাংলা দ্রুত রিভিশন} &
\cellcolor{secondpaper}\tiny \B{রসায়ন+জীব+বাংলা দ্রুত রিভিশন} &
\cellcolor{firstpaper}\tiny \B{গণিত+পদার্থ+জীব দ্রুত রিভিশন} &
\cellcolor{secondpaper}\tiny \B{গণিত+পদার্থ+জীব দ্রুত রিভিশন} &
\tiny \B{আইসিটি সম্পূর্ণ রিভিশন} \\
\hline
\rowcolor{rowodd}
\scriptsize\bfseries \B{১০:১০--১০:৩০} &
\multicolumn{7}{c|}{\scriptsize \B{হালকা খাবার, হাঁটাচলা}}\\
\hline
\rowcolor{roweven}
\scriptsize\bfseries \B{১০:৩০--১১:৪০} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{সেশন-৫ (বিরতিহীন):}} \B{ইংরেজী ১ম পত্র ৩০মি + ইংরেজী ২য় পত্র ৩০মি + সারাদিনের ১০মি স্ক্যান}}\\
\hline
\rowcolor{pray}
\scriptsize\bfseries \B{১১:৪০} &
\multicolumn{7}{c|}{\scriptsize \textbf{\B{ঘুমাতে যাওয়া}}}\\
\hline
\rowcolor{notebg}
\multicolumn{8}{|p{\dimexpr\textwidth-2\tabcolsep-2\arrayrulewidth\relax}|}{%
\tiny
\textbf{\B{সেশন-১ (৫:০০--৭:০০, ২ঘ বিরতিহীন):}} \B{কঠিনতম ২টি বিষয়, প্রতিটি ১ ঘণ্টা করে।}
\quad\textbf{\B{সেশন-২ (৮:০০--১:০০, ৫ঘ):}} \B{৪টি বিষয় + আইসিটি ১ঘ + মডেল টেস্ট ৩০মি; প্রতিটি সাইকেলের পর ১০মি বিরতি।}
\quad\textbf{\B{সেশন-৪ (৭:১০--১০:১০, ৩ঘ):}} \B{ইংরেজী ১ম ৪৫মি + ইংরেজী ২য় ৪৫মি + দ্রুত রিভিশন ১ঘ১০মি।}
\quad\textbf{\B{সেশন-৫ (১০:৩০--১১:৪০):}} \B{ইংরেজী ৩০+৩০মি + স্ক্যান রিভিশন ১০মি।}
}\\
\hline
\rowcolor{notebg}
\multicolumn{8}{|p{\dimexpr\textwidth-2\tabcolsep-2\arrayrulewidth\relax}|}{%
\tiny
\textbf{\B{বিষয় ও সময়:}}
\B{পদার্থবিজ্ঞান ১ম/২য় (১ঘ)} \textbar{}
\B{উচ্চতর গণিত ১ম/২য় (১ঘ)} \textbar{}
\B{রসায়ন ১ম/২য় (১ঘ)} \textbar{}
\B{জীববিজ্ঞান ১ম/২য় (১ঘ)} \textbar{}
\B{বাংলা ১ম/২য় (১ঘ)} \textbar{}
\B{ইংরেজী ১ম+২য় পত্র (৪৫মি করে)} \textbar{}
\B{আইসিটি (১ঘ)}
\quad
\textbf{\B{শনি/সোম/বুধ = ১ম পত্র দিন। রবি/মঙ্গল/বৃহস্পতি = ২য় পত্র দিন। শুক্রবার = মেগা রিভিউ।}}
}\\
\hline
\rowcolor{notebg}
\multicolumn{8}{|p{\dimexpr\textwidth-2\tabcolsep-2\arrayrulewidth\relax}|}{%
\tiny
\textbf{\B{প্রাইভেট গৃহশিক্ষক:}}
\B{শাহিন স্যার --- পদার্থবিজ্ঞান (শনি/সোম/বুধ ২:৩০--৩:৩০)} \textbar{}
\B{মোরসালিন স্যার --- উচ্চতর গণিত (শনি/সোম/বুধ ৪:০০--৫:০০)} \textbar{}
\B{নুর আলম স্যার --- ইংরেজী (রবি/মঙ্গল/বৃহস্পতি ২:০০--৩:০০)} \textbar{}
\B{হেদায়েত স্যার --- রসায়ন (রবি/মঙ্গল/বৃহস্পতি ৫:১৫--৬:০০)}
\quad
\textbf{\B{৫ ওয়াক্ত নামাজ:}}
\B{ফজর ৪:৩০--৪:৫০ \textbar{} যোহর ১:২০--২:০০ \textbar{} আসর ৫:০০--৫:১৫ \textbar{} মাগরিব ৬:৫০--৭:১০ \textbar{} এশা ৮:৪৫--৯:১০}
\quad
\textbf{\B{খাবার:}} \B{নাস্তা ৭:০০--৮:০০ \textbar{} দুপুর ১:২০--২:০০ \textbar{} বিকেল ৩:৩০--৪:০০ \textbar{} রাত ৮:৪৫--৯:১০ \textbar{} বিশ্রাম রুটিনে নির্ধারিত।}
}\\
\hline
\end{tabularx}
\end{document}
"""

def main():
    out = "/tmp/routine"
    os.makedirs(out, exist_ok=True)
    os.makedirs(os.path.join(out, "fonts"), exist_ok=True)
    with open(os.path.join(out, "routine.tex"), "w", encoding="utf-8") as f:
        f.write(TEX.replace("\u200d", ""))
    xelatex = shutil.which("xelatex") or "/nix/store/6i7mj0hkffgy88bbgii5ffnqfv3awb29-texlive-2025-env/bin/xelatex"
    for _ in range(2):
        r = subprocess.run([xelatex, "-interaction=nonstopmode", "routine.tex"], cwd=out, capture_output=True, text=True)
    ok = os.path.exists(os.path.join(out, "routine.pdf"))
    if not ok:
        print(r.stdout[-4000:]); print(r.stderr[-2000:]); sys.exit(1)
    print("PDF ready")

if __name__ == "__main__":
    main()
