import subprocess, os, shutil
tex_content = r'''\documentclass[8pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[left=0.55cm,right=0.55cm,top=0.7cm,bottom=0.55cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{array}
\usepackage[hidelinks]{hyperref}
\usepackage[protrusion=false]{microtype}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{ulem}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,calc,shapes.gates.logic.US,shapes.geometric,positioning,decorations.pathmorphing}
\usepackage{adjustbox}
\usepackage{makecell}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{needspace}
\setlength{\arrayrulewidth}{0.25pt}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}
\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{105,105,105}
\definecolor{clrBlack}{RGB}{0,0,0}
\definecolor{clrBlue}{RGB}{0,0,255}
\definecolor{clrBlueViolet}{RGB}{138,43,226}
\definecolor{clrBrown}{RGB}{165,42,42}
\definecolor{clrBurlyWood}{RGB}{222,184,135}
\definecolor{clrChocolate}{RGB}{210,105,30}
\definecolor{clrCyan}{RGB}{0,255,255}
\definecolor{clrDarkBlue}{RGB}{0,0,139}
\definecolor{clrDarkGreen}{RGB}{0,100,0}
\definecolor{clrDarkKhaki}{RGB}{189,183,107}
\definecolor{clrDarkRed}{RGB}{139,0,0}
\definecolor{clrGold}{RGB}{255,215,0}
\definecolor{clrGray}{RGB}{128,128,128}
\definecolor{clrGreen}{RGB}{0,128,0}
\definecolor{clrIndigo}{RGB}{75,0,130}
\definecolor{clrAntiqueWhite}{RGB}{250,235,215}
\definecolor{clrBeige}{RGB}{245,245,220}
\definecolor{clrDarkOrange}{RGB}{255,140,0}
\definecolor{clrKhaki}{RGB}{240,230,140}
\definecolor{clrMagenta}{RGB}{255,0,255}
\definecolor{clrNavy}{RGB}{0,0,128}
\definecolor{clrOlive}{RGB}{128,128,0}
\definecolor{clrOrange}{RGB}{255,165,0}
\definecolor{clrPink}{RGB}{255,192,203}
\definecolor{clrPurple}{RGB}{128,0,128}
\definecolor{clrRed}{RGB}{255,0,0}
\definecolor{clrSilver}{RGB}{192,192,192}
\definecolor{clrSkyBlue}{RGB}{135,206,235}
\definecolor{clrSnow}{RGB}{255,250,250}
\definecolor{clrViolet}{RGB}{238,130,238}
\definecolor{clrWhite}{RGB}{255,255,255}
\definecolor{clrYellow}{RGB}{255,255,0}
\definecolor{clrYellowGreen}{RGB}{154,205,50}
\definecolor{clrAquamarine}{RGB}{127,255,212}
\definecolor{clrCadetBlue}{RGB}{95,158,160}
\definecolor{clrMaroon}{RGB}{128,0,0}
\pagestyle{empty}
\setlength{\emergencystretch}{40pt}
\hbadness=10000
\vbadness=10000
\sloppy
\setlength{\parskip}{0pt}
\setlength{\parindent}{0pt}
\setlength{\columnsep}{6pt}
\setlength{\multicolsep}{1pt plus 1pt minus 1pt}
\setlength{\intextsep}{1pt}
\setlength{\textfloatsep}{1pt}
\setlength{\abovedisplayskip}{1pt}
\setlength{\belowdisplayskip}{1pt}
\setlist{nosep,topsep=0pt,partopsep=0pt,parsep=0pt,itemsep=0pt,leftmargin=1.1em}
\raggedcolumns
\tolerance=9999
\defaultfontfeatures{Ligatures=TeX}
\newfontfamily\lat{Latin Modern Roman}[Ligatures=TeX]
\newfontfamily\bn{NotoSerifBengali-Regular.ttf}[Path=./, Script=Bengali, BoldFont=NotoSerifBengali-Bold.ttf, ItalicFont=NotoSerifBengali-Regular.ttf, BoldItalicFont=NotoSerifBengali-Bold.ttf, Renderer=HarfBuzz, AutoFakeSlant=0.18]
\newcommand{\B}[1]{{\bn #1}}
\newcommand{\LAT}[1]{{\lat #1}}
\newcommand{\chsec}[1]{%
  \needspace{3\baselineskip}\vspace{2pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par\noindent%
}
\newcommand{\chsecfull}[1]{%
  \needspace{3\baselineskip}\vspace{2pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\textwidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par\noindent%
}
\newcommand{\chsub}[2]{%
  \needspace{3\baselineskip}\vspace{2pt}%
  \noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \bfseries\footnotesize\color{white}\;\B{#1}\ \B{#2}%
  }}%
  \vspace{1pt}\par\noindent%
}
\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8pt}
\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\setlist[itemize]{nosep, leftmargin=0pt, topsep=0pt, label={}, itemsep=0pt, parsep=0pt}
\newcommand{\itm}[1]{\par\noindent\textbf{{\lat #1.}}\;}
\newcommand{\sub}[1]{\textbf{({\lat #1})}\;}

\begin{document}
\begin{center}
\noindent
{\bn\Large\bfseries তথ্য ও যোগাযোগ প্রযুক্তি (ICT) সমস্ত সংজ্ঞা, সূত্র ও রেফারেন্স}\hfill
{\normalfont\small\textbf{By Abir Arafat Chawdhury [Introvert's Area]}}
\vspace{3pt}
\end{center}

\begin{multicols}{2}

\chsec{১. সংখ্যা পদ্ধতি ও রূপান্তর সূত্র}
\itm{1} \B{সংখ্যা পদ্ধতির ভিত্তি:} \B{বাইনারি} \LAT{=2,} \B{অক্টাল} \LAT{=8,} \B{ডেসিমাল} \LAT{=10,} \B{হেক্সাডেসিমাল} \LAT{=16}
\itm{2} \B{যেকোনো ভিত্তি} \LAT{$r$} \B{থেকে ডেসিমাল:} \LAT{$N=\sum d_i\cdot r^i$}
\itm{3} \B{ডেসিমাল থেকে বাইনারি:} \B{ক্রমাগত} \LAT{2} \B{দ্বারা ভাগ; ভাগশেষ নিচ থেকে উপরে}
\itm{4} \B{ডেসিমাল ভগ্নাংশ:} \LAT{2} \B{দ্বারা গুণ; পূর্ণ অংশ উপর থেকে নিচে}
\itm{5} \B{বাইনারি} \LAT{$\to$} \B{অক্টাল:} \B{ডান থেকে} \LAT{3} \B{বিট গ্রুপ}
\itm{6} \B{বাইনারি} \LAT{$\to$} \B{হেক্সাডেসিমাল:} \B{ডান থেকে} \LAT{4} \B{বিট গ্রুপ}
\itm{7} \B{অক্টাল} \LAT{$\leftrightarrow$} \B{হেক্সাডেসিমাল:} \B{বাইনারির মাধ্যমে}
\itm{8} \B{সর্বোচ্চ মান:} \LAT{$n$} \B{সংখ্যা ভিত্তি} \LAT{$r$} \B{তে} \LAT{$= r^n-1$}
\itm{9} \B{মোট মান:} \LAT{$n$} \B{বিটে} \LAT{$2^n$} \B{টি ভিন্ন মান প্রকাশ সম্ভব}

\chsub{}{মৌলিক রূপান্তর টেবিল}
\noindent\scriptsize
\setlength{\tabcolsep}{1.5pt}
\begin{tabular}{|c|c|c|c|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{Bin} & \LAT{Oct} & \LAT{Hex} \\\hline
\LAT{0} & \LAT{0000} & \LAT{0} & \LAT{0} \\\hline
\LAT{1} & \LAT{0001} & \LAT{1} & \LAT{1} \\\hline
\LAT{2} & \LAT{0010} & \LAT{2} & \LAT{2} \\\hline
\LAT{3} & \LAT{0011} & \LAT{3} & \LAT{3} \\\hline
\LAT{4} & \LAT{0100} & \LAT{4} & \LAT{4} \\\hline
\LAT{5} & \LAT{0101} & \LAT{5} & \LAT{5} \\\hline
\LAT{6} & \LAT{0110} & \LAT{6} & \LAT{6} \\\hline
\LAT{7} & \LAT{0111} & \LAT{7} & \LAT{7} \\\hline
\LAT{8} & \LAT{1000} & \LAT{10} & \LAT{8} \\\hline
\LAT{9} & \LAT{1001} & \LAT{11} & \LAT{9} \\\hline
\LAT{10} & \LAT{1010} & \LAT{12} & \LAT{A} \\\hline
\LAT{15} & \LAT{1111} & \LAT{17} & \LAT{F} \\\hline
\LAT{16} & \LAT{10000} & \LAT{20} & \LAT{10} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{২. সংখ্যার গাণিতিক অপারেশন}
\itm{1} \B{বাইনারি যোগ:} \LAT{$0{+}0{=}0,\;0{+}1{=}1,\;1{+}1{=}10$} \B{(ক্যারি} \LAT{1}\B{)}
\itm{2} \B{বাইনারি বিয়োগ:} \LAT{$0{-}0{=}0,\;1{-}0{=}1,\;1{-}1{=}0,\;0{-}1{=}1$} \B{(ধার)}
\itm{3} \B{বাইনারি গুণ:} \LAT{$0{\times}0{=}0,\;0{\times}1{=}0,\;1{\times}0{=}0,\;1{\times}1{=}1$}
\itm{4} \B{১-এর পরিপূরক:} \B{প্রতিটি বিট উল্টানো} \LAT{($0\leftrightarrow1$)}
\itm{5} \B{২-এর পরিপূরক:} \B{১-এর পরিপূরক} \LAT{$+1$}
\itm{6} \B{বিয়োগ} \LAT{$A-B$}\B{:} \LAT{$A+$} \B{(}\LAT{$B$}\B{-এর ২-এর পরিপূরক)}
\itm{7} \B{সাইন বিট:} \B{ধনাত্মক} \LAT{$=0$}\B{, ঋণাত্মক} \LAT{$=1$}
\itm{8} \LAT{$n$} \B{বিট সাইনড পরিসীমা:} \LAT{$-2^{n-1}$} \B{থেকে} \LAT{$+2^{n-1}-1$}
\itm{9} \LAT{$n$} \B{বিট আনসাইনড পরিসীমা:} \LAT{$0$} \B{থেকে} \LAT{$2^n-1$}
\itm{10} \B{অক্টাল যোগে ক্যারি} \LAT{$\geq8$}\B{; হেক্স যোগে ক্যারি} \LAT{$\geq16$}

\chsec{৩. কোড পদ্ধতি}
\itm{1} \B{BCD:} \B{প্রতিটি ডেসিমাল ডিজিট} \LAT{=4} \B{বিট} \LAT{(8421} \B{কোড)}
\itm{2} \B{Excess-3:} \LAT{BCD$+0011$}\B{; self-complementing কোড}
\itm{3} \B{Gray Code:} \B{পরপর কোডে শুধু} \LAT{1} \B{বিট পরিবর্তন; MSB একই থাকে}
\itm{4} \B{ASCII:} \LAT{7} \B{বিট} \LAT{$\to$ 128} \B{ক্যারেক্টার; বর্ধিত} \LAT{8} \B{বিট} \LAT{$\to$ 256}
\itm{5} \B{EBCDIC:} \LAT{8} \B{বিট,} \LAT{IBM} \B{মেইনফ্রেম,} \LAT{256} \B{ক্যারেক্টার}
\itm{6} \B{Unicode:} \LAT{16/32} \B{বিট, বিশ্বের সব ভাষা সমর্থন,} \LAT{UTF-8/16/32}
\itm{7} \B{Even parity:} \LAT{1}\B{-এর সংখ্যা জোড়; Odd parity: বিজোড়}
\itm{8} \B{Gray থেকে Binary:} \LAT{MSB} \B{একই; বাকি: আগের Binary XOR Gray বিট}

\chsub{}{BCD, Excess-3 ও Gray রূপান্তর টেবিল}
\noindent\scriptsize
\setlength{\tabcolsep}{1.5pt}
\begin{tabular}{|c|c|c|c|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{BCD} & \LAT{Excess-3} & \LAT{Gray} \\\hline
\LAT{0} & \LAT{0000} & \LAT{0011} & \LAT{0000} \\\hline
\LAT{1} & \LAT{0001} & \LAT{0100} & \LAT{0001} \\\hline
\LAT{2} & \LAT{0010} & \LAT{0101} & \LAT{0011} \\\hline
\LAT{3} & \LAT{0011} & \LAT{0110} & \LAT{0010} \\\hline
\LAT{4} & \LAT{0100} & \LAT{0111} & \LAT{0110} \\\hline
\LAT{5} & \LAT{0101} & \LAT{1000} & \LAT{0111} \\\hline
\LAT{6} & \LAT{0110} & \LAT{1001} & \LAT{0101} \\\hline
\LAT{7} & \LAT{0111} & \LAT{1010} & \LAT{0100} \\\hline
\LAT{8} & \LAT{1000} & \LAT{1011} & \LAT{1100} \\\hline
\LAT{9} & \LAT{1001} & \LAT{1100} & \LAT{1101} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{৪. ডেটা কমিউনিকেশন}
\itm{1} \B{ব্যান্ডউইথ একক:} \LAT{bps, Kbps, Mbps, Gbps, Tbps}
\itm{2} \LAT{1 Byte=8 bits; 1 KB=1024 B; 1 MB=1024 KB; 1 GB=1024 MB; 1 TB=1024 GB}
\itm{3} \B{ট্রান্সমিশন মোড:}
\par\noindent\quad\B{সিমপ্লেক্স: এককমুখী}
\par\noindent\quad\B{হাফ-ডুপ্লেক্স: দুদিকে কিন্তু একসাথে নয়}
\par\noindent\quad\B{ফুল-ডুপ্লেক্স: উভয়মুখী একসাথে}
\itm{4} \B{সিরিয়াল ট্রান্সমিশন:} \B{একে একে বিট; প্যারালাল: একসাথে অনেক বিট}
\itm{5} \B{নেটওয়ার্ক টপোলজি:} \B{বাস, স্টার, রিং, ট্রি, মেশ, হাইব্রিড}
\itm{6} \B{গাইডেড মাধ্যম:} \B{কোএক্সিয়াল, টুইস্টেড পেয়ার} \LAT{(STP/UTP)}\B{, অপটিক্যাল ফাইবার}
\itm{7} \B{আনগাইডেড:} \B{রেডিও তরঙ্গ, মাইক্রোওয়েভ, ইনফ্রারেড, স্যাটেলাইট}
\itm{8} \B{মোবাইল প্রজন্ম:} \LAT{1G} \B{এনালগ;} \LAT{2G (GSM/CDMA); 3G} \B{ব্রডব্যান্ড;} \LAT{4G LTE; 5G} \B{উচ্চগতি}
\itm{9} \LAT{IPv4=32} \B{বিট;} \LAT{IPv6=128} \B{বিট;} \LAT{Shannon: $C=B\log_2(1+S/N)$}
\itm{10} \LAT{Nyquist: $C=2B\log_2 V$} \B{(}\LAT{V}\B{= সিগন্যাল মাত্রা)}
\itm{11} \B{নেটওয়ার্ক শ্রেণি:} \LAT{PAN, LAN, MAN, WAN, CAN, GAN}
\itm{12} \B{OSI স্তর (নিচ থেকে):} \B{ফিজিক্যাল, ডেটালিংক, নেটওয়ার্ক, ট্রান্সপোর্ট, সেশন, প্রেজেন্টেশন, অ্যাপ্লিকেশন}

\chsec{৫. কম্পিউটার প্রজন্ম}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.10\linewidth}|>{\centering\arraybackslash}p{0.20\linewidth}|X|}
\hline
\rowcolor{tblhdr} \B{প্রজন্ম} & \B{সময়কাল} & \B{প্রযুক্তি ও বৈশিষ্ট্য} \\\hline
\B{১ম} & \LAT{1940--1956} & \B{ভ্যাকুয়াম টিউব; মেশিন ভাষা; ENIAC, EDVAC, UNIVAC} \\\hline
\B{২য়} & \LAT{1956--1963} & \B{ট্রানজিস্টর; অ্যাসেম্বলি ভাষা; দ্রুততর ও ছোট} \\\hline
\B{৩য়} & \LAT{1964--1971} & \B{IC (ইন্টিগ্রেটেড সার্কিট); হাই লেভেল ভাষা} \\\hline
\B{৪র্থ} & \LAT{1971--1989} & \B{মাইক্রোপ্রসেসর; পার্সোনাল কম্পিউটার; VLSI} \\\hline
\B{৫ম} & \LAT{1989--}\B{বর্তমান} & \B{ULSI; AI; ন্যানো প্রযুক্তি; সমান্তরাল প্রসেসিং} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{৬. কম্পিউটার সংজ্ঞাবলি}
\itm{1} \B{হার্ডওয়্যার:} \B{কম্পিউটারের স্পর্শযোগ্য যন্ত্রাংশ (মনিটর, কীবোর্ড, CPU)}
\itm{2} \B{সফটওয়্যার:} \B{প্রোগ্রামসমূহ; সিস্টেম সফটওয়্যার ও অ্যাপ্লিকেশন}
\itm{3} \B{CPU:} \B{কেন্দ্রীয় প্রক্রিয়াকরণ ইউনিট;} \LAT{ALU + CU +} \B{রেজিস্টার}
\itm{4} \B{ALU:} \B{গাণিতিক ও যুক্তিমূলক কাজ সম্পাদন করে}
\itm{5} \B{CU:} \B{নির্দেশনা ব্যাখ্যা ও সম্পাদনের সমন্বয় করে}
\itm{6} \B{RAM:} \LAT{Random Access Memory;} \B{অস্থায়ী; বিদ্যুৎ গেলে ডেটা হারায়}
\itm{7} \B{ROM:} \LAT{Read Only Memory;} \B{স্থায়ী; BIOS সংরক্ষণে ব্যবহার}
\itm{8} \B{Cache:} \B{দ্রুতগতির অস্থায়ী মেমরি; CPU-র কাছে থাকে}
\itm{9} \B{OS:} \LAT{Operating System;} \B{হার্ডওয়্যার ও সফটওয়্যার পরিচালনা করে}
\itm{10} \B{BIOS:} \LAT{Basic Input Output System;} \B{কম্পিউটার চালু হওয়ার সময় কাজ করে}
\itm{11} \B{বাস:} \B{ডেটা বাস, অ্যাড্রেস বাস, কন্ট্রোল বাস -- CPU ও মেমরির মধ্যে সংযোগ}
\itm{12} \B{ইনপুট ডিভাইস:} \B{কীবোর্ড, মাউস, স্ক্যানার, OMR, OCR, ওয়েবক্যাম, মাইক্রোফোন}
\itm{13} \B{আউটপুট ডিভাইস:} \B{মনিটর, প্রিন্টার, স্পিকার, প্রজেক্টর}
\itm{14} \B{সংরক্ষণ:} \LAT{HDD, SSD, CD-ROM, DVD, Pen Drive, Memory Card}

\end{multicols}

\vspace{2pt}
\chsecfull{৭. তথ্য ও যোগাযোগ প্রযুক্তি সংক্রান্ত Abbreviations}
\vspace{2pt}
\noindent\tiny
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.05}
\begin{tabular}{|l|p{0.165\textwidth}|l|p{0.165\textwidth}|l|p{0.165\textwidth}|l|p{0.165\textwidth}|}
\hline
\rowcolor{tblhdr}
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} \\\hline
\LAT{ADD} & \LAT{Automatic Document Detection} & \LAT{ADSL} & \LAT{Asymmetric Digital Subscriber Line} & \LAT{AES} & \LAT{Advanced Encryption Standard} & \LAT{AI} & \LAT{Artificial Intelligence} \\\hline
\LAT{ALGOL} & \LAT{Algorithmic Language} & \LAT{AMPS} & \LAT{Advanced Mobile Phone System} & \LAT{ANSI} & \LAT{American National Standard Institute} & \LAT{AOC} & \LAT{Advice Of Charge} \\\hline
\LAT{AOL} & \LAT{American Online} & \LAT{API} & \LAT{Application Programming Interface} & \LAT{APL} & \LAT{A Programming Language} & \LAT{ARPANET} & \LAT{Advanced Research Projects Agency Network} \\\hline
\LAT{ASP} & \LAT{Active Server Pages} & \LAT{ATM} & \LAT{Automated Teller Machine} & \LAT{AVI} & \LAT{Audio Video Interleave} & \LAT{B2B} & \LAT{Business to Business} \\\hline
\LAT{B2C} & \LAT{Business to Consumer} & \LAT{BASIC} & \LAT{Beginner's All-purpose Symbolic Instruction Code} & \LAT{BCPL} & \LAT{Basic Combined Programming Language} & \LAT{BIOS} & \LAT{Basic Input Output System} \\\hline
\LAT{BIX} & \LAT{Bangladesh Internet Exchange} & \LAT{BMP} & \LAT{Bitmap Image File} & \LAT{BNC} & \LAT{Bayonet Neill-Concelman} & \LAT{BPL} & \LAT{Broadband Over Power Line} \\\hline
\LAT{BPS} & \LAT{Bits Per Second} & \LAT{BSA} & \LAT{Business Software Alliance} & \LAT{BSCCL} & \LAT{Bangladesh Submarine Cable Company Limited} & \LAT{BSC} & \LAT{Base Station Controller} \\\hline
\LAT{BSS} & \LAT{Base Station Subsystem} & \LAT{BT} & \LAT{Bluetooth} & \LAT{BTCL} & \LAT{Bangladesh Telecommunication Company Limited} & \LAT{BW} & \LAT{Bandwidth} \\\hline
\LAT{C2B} & \LAT{Consumer to Business} & \LAT{C2C} & \LAT{Consumer to Consumer} & \LAT{CA} & \LAT{Computer Architecture} & \LAT{CAD} & \LAT{Computer Aided Design} \\\hline
\LAT{CAE} & \LAT{Computer Aided Engineering} & \LAT{CAM} & \LAT{Computer Aided Manufacturing} & \LAT{CAN} & \LAT{Campus Area Network} & \LAT{CCTLD} & \LAT{Country Code Top Level Domain} \\\hline
\LAT{CD} & \LAT{Compact Disc} & \LAT{CD-ROM} & \LAT{Compact Disc Read Only Memory} & \LAT{CDMA} & \LAT{Code Division Multiple Access} & \LAT{CLR} & \LAT{CLeaR accumulator} \\\hline
\LAT{CMOS} & \LAT{Complementary Metal-Oxide Semiconductor} & \LAT{CNC} & \LAT{Computerized Numerical Control} & \LAT{COBOL} & \LAT{Common Business Oriented Language} & \LAT{COD} & \LAT{Cash on Delivery} \\\hline
\LAT{COM} & \LAT{Component Object Model} & \LAT{CPR} & \LAT{Computer-based Patient Record} & \LAT{CPU} & \LAT{Central Processing Unit} & \LAT{CS} & \LAT{Computer Science} \\\hline
\LAT{CSE} & \LAT{Computer Science and Engineering} & \LAT{CSS} & \LAT{Cascading Style Sheets} & \LAT{CUG} & \LAT{Closed User Group} & \LAT{DBA} & \LAT{Database Administrator} \\\hline
\LAT{DBMS} & \LAT{Database Management System} & \LAT{DCE} & \LAT{Data Communications Equipment} & \LAT{DDL} & \LAT{Data Definition Language} & \LAT{DES} & \LAT{Data Encryption Standard} \\\hline
\LAT{DFD} & \LAT{Data Flow Diagram} & \LAT{DIV} & \LAT{DIVide} & \LAT{DLL} & \LAT{Dynamic Link Library} & \LAT{DML} & \LAT{Data Manipulation Language} \\\hline
\LAT{DNA} & \LAT{Deoxyribonucleic Acid} & \LAT{DNS} & \LAT{Domain Name System} & \LAT{DOS} & \LAT{Disk Operating System} & \LAT{DSL} & \LAT{Digital Subscriber Line} \\\hline
\LAT{DTE} & \LAT{Data Terminal Equipment} & \LAT{DTI} & \LAT{Department of Trade and Industry} & \LAT{DVD} & \LAT{Digital Versatile Disc} & \LAT{E-commerce} & \LAT{Electronic commerce} \\\hline
\LAT{E-governance} & \LAT{Electronic governance} & \LAT{E-book} & \LAT{Electronic book} & \LAT{EC2} & \LAT{Elastic Compute Cloud} & \LAT{ECT} & \LAT{Explicit Call Transfer} \\\hline
\LAT{EDGE} & \LAT{Enhanced Data rates for GSM Evolution} & \LAT{EHF} & \LAT{Extremely High Frequency} & \LAT{EHR} & \LAT{Electronic Health Records} & \LAT{EMI} & \LAT{Electromagnetic Interference} \\\hline
\LAT{EMR} & \LAT{Electronic Medical Record} & \LAT{EMTS} & \LAT{Electronic Money Transfer System} & \LAT{ESN} & \LAT{Electronic Serial Number} & \LAT{ETSI} & \LAT{European Telecommunication Standards Institute} \\\hline
\LAT{FAQ} & \LAT{Frequently Asked Question} & \LAT{FAX} & \LAT{Facsimile} & \LAT{FCC} & \LAT{Federal Communications Commission} & \LAT{FDD} & \LAT{Frequency Division Duplexing} \\\hline
\LAT{FDMA} & \LAT{Frequency Division Multiple Access} & \LAT{FOMA} & \LAT{Freedom of Mobile Access} & \LAT{FORTRAN} & \LAT{Formula Translator} & \LAT{FQDN} & \LAT{Fully Qualified Domain Name} \\\hline
\LAT{FRS} & \LAT{Family Radio Service} & \LAT{FTP} & \LAT{File Transfer Protocol} & \LAT{Gb} & \LAT{Gigabit} & \LAT{GB} & \LAT{Gigabyte} \\\hline
\LAT{Gbps} & \LAT{Gigabits per second} & \LAT{GDP} & \LAT{Gross Domestic Product} & \LAT{GIF} & \LAT{Graphics Interchange Format} & \LAT{GM} & \LAT{Genetic Modification/Manipulation} \\\hline
\LAT{GMO} & \LAT{Genetically Modified Organism} & \LAT{GMRS} & \LAT{General Mobile Radio Service} & \LAT{GPRS} & \LAT{General Packet Radio Service} & \LAT{GPS} & \LAT{Global Positioning System} \\\hline
\LAT{GSM} & \LAT{Global System for Mobile Communications} & \LAT{GUI} & \LAT{Graphical User Interface} & \LAT{HAL} & \LAT{Hardware Abstraction Layer} & \LAT{HD} & \LAT{High Definition} \\\hline
\LAT{HDTV} & \LAT{High Definition Television} & \LAT{HSDPA} & \LAT{High Speed Downlink Packet Access} & \LAT{HSPA} & \LAT{High Speed Packet Access} & \LAT{HTML} & \LAT{Hyper Text Markup Language} \\\hline
\LAT{HTTP} & \LAT{Hyper Text Transfer Protocol} & \LAT{I/O} & \LAT{Input/Output} & \LAT{IaaS} & \LAT{Infrastructure-as-a-Service} & \LAT{IANA} & \LAT{Internet Assigned Numbers Authority} \\\hline
\LAT{IBM} & \LAT{International Business Machines} & \LAT{IC} & \LAT{Integrated Circuit} & \LAT{ICANN} & \LAT{Internet Corporation for Assigned Names and Numbers} & \LAT{ICT} & \LAT{Information and Communication Technology} \\\hline
\LAT{ICX} & \LAT{Inter Connection Exchange} & \LAT{IDE} & \LAT{Integrated Development Environment} & \LAT{IDEA} & \LAT{International Data Encryption Algorithm} & \LAT{IDEN} & \LAT{Integrated Digital Enhanced Network} \\\hline
\LAT{IEEE} & \LAT{Institute of Electrical and Electronics Engineers} & \LAT{IIS} & \LAT{Internet Information Service} & \LAT{ILD} & \LAT{Interjection Laser Diode} & \LAT{IMAP} & \LAT{Internet Message Access Protocol} \\\hline
\LAT{IMSI} & \LAT{International Mobile Subscriber Identity} & \LAT{IMT} & \LAT{International Mobile Telecommunications} & \LAT{INP} & \LAT{INPut} & \LAT{IOT} & \LAT{Internet of Things} \\\hline
\LAT{IP} & \LAT{Internet Protocol} & \LAT{IPTV} & \LAT{Internet Protocol Television} & \LAT{ISOC} & \LAT{Internet Society} & \LAT{ISP} & \LAT{Internet Service Provider} \\\hline
\LAT{IT} & \LAT{Information Technology} & \LAT{ITAA} & \LAT{Information Technology Association of America} & \LAT{ITU} & \LAT{International Telecommunication Union} & \LAT{JMP} & \LAT{JuMP} \\\hline
\LAT{JPEG} & \LAT{Joint Photographic Expert Group} & \LAT{KB} & \LAT{Kilobyte} & \LAT{Kbps} & \LAT{Kilobits per second} & \LAT{KHz} & \LAT{Kilohertz} \\\hline
\LAT{KPI} & \LAT{Key Performance Indicators} & \LAT{LAN} & \LAT{Local Area Network} & \LAT{LCD} & \LAT{Liquid Crystal Display} & \LAT{LDA} & \LAT{Load Accumulator} \\\hline
\LAT{LED} & \LAT{Light Emitting Diode} & \LAT{LF} & \LAT{Low Frequency} & \LAT{LISP} & \LAT{List Processing} & \LAT{LMR} & \LAT{Land Mobile Radio} \\\hline
\LAT{LOS} & \LAT{Line Of Sight} & \LAT{LTE} & \LAT{Long Term Evolution} & \LAT{MAC} & \LAT{Mandatory Access Control} & \LAT{MAN} & \LAT{Metropolitan Area Network} \\\hline
\LAT{Mb} & \LAT{Megabit} & \LAT{MB} & \LAT{Megabyte} & \LAT{Mbps} & \LAT{Megabits per second} & \LAT{MF} & \LAT{Medium Frequency} \\\hline
\LAT{MHz} & \LAT{Megahertz} & \LAT{MIMO} & \LAT{Multiple Input and Multiple Output} & \LAT{MIN} & \LAT{Mobile Identification Number} & \LAT{MIST} & \LAT{Minimally Invasive Surgical Trainer} \\\hline
\LAT{MIT} & \LAT{Massachusetts Institute of Technology} & \LAT{MMS} & \LAT{Multimedia Massage Service} & \LAT{MoBo} & \LAT{Motherboard} & \LAT{MRI} & \LAT{Magnetic Resonance Imaging} \\\hline
\LAT{MRP} & \LAT{Manufacturing Requirement Planning} & \LAT{MS} & \LAT{Microsoft} & \LAT{MSC} & \LAT{Mobile Switching Centre} & \LAT{MTSO} & \LAT{Mobile Telephone Switching Office} \\\hline
\LAT{MUL} & \LAT{MULtiple} & \LAT{NASA} & \LAT{National Aeronautics and Space Administration} & \LAT{NFC} & \LAT{Near Field Communication} & \LAT{NIC} & \LAT{Network Interface Card} \\\hline
\LAT{NIST} & \LAT{National Institute of Standards and Testing} & \LAT{NIX} & \LAT{National Internet Exchange} & \LAT{NMT} & \LAT{Nordic Mobile Telephony} & \LAT{NSFNET} & \LAT{National Science Foundation Network} \\\hline
\LAT{NSS} & \LAT{Network and Switching Subsystem} & \LAT{NTSC} & \LAT{National Television System Committee} & \LAT{NTTC} & \LAT{Nippon Telegraph and Telephone Corporation} & \LAT{OFDM} & \LAT{Orthogonal Frequency Division Multiplexing} \\\hline
\LAT{OLE} & \LAT{Object Linking and Embedding} & \LAT{OMR} & \LAT{Optical Mark Reader} & \LAT{OOP} & \LAT{Object Oriented Programming} & \LAT{OS} & \LAT{Operating System} \\\hline
\LAT{OSS} & \LAT{Operations Support System} & \LAT{OUT} & \LAT{OUTput} & \LAT{P2M} & \LAT{Point-to-Multiple} & \LAT{P2P} & \LAT{Point-to-Point} \\\hline
\LAT{PaaS} & \LAT{Platform-as-a-Service} & \LAT{PAL} & \LAT{Phase Alternating Line} & \LAT{PAN} & \LAT{Personal Area Network} & \LAT{Pbps} & \LAT{Peta bits per second} \\\hline
\LAT{PC} & \LAT{Personal Computer} & \LAT{PDA} & \LAT{Personal Digital Assistant} & \LAT{PDF} & \LAT{Portable Document File} & \LAT{PIN} & \LAT{Personal Identification Number} \\\hline
\LAT{PNG} & \LAT{Portable Network Graphics} & \LAT{POP} & \LAT{Post Office Protocol} & \LAT{PSTN} & \LAT{Public Switched Telephone Network} & \LAT{PUK} & \LAT{Personal Unblocking Key} \\\hline
\LAT{QBE} & \LAT{Query By Example} & \LAT{QUEL} & \LAT{Query Language} & \LAT{RAD} & \LAT{Rapid Application Development} & \LAT{RAM} & \LAT{Random Access Memory} \\\hline
\LAT{RDBMS} & \LAT{Relational Database Management System} & \LAT{RF} & \LAT{Radio Frequency} & \LAT{RFID} & \LAT{Radio Frequency Identification} & \LAT{RISC} & \LAT{Reduced Instruction Set Computer} \\\hline
\LAT{RNA} & \LAT{Recombinant Nucleic Acid} & \LAT{RNC} & \LAT{Radio Network Controller} & \LAT{ROM} & \LAT{Read Only Memory} & \LAT{RPG} & \LAT{Report Program Generation} \\\hline
\LAT{RQBE} & \LAT{Relational Query By Example} & \LAT{RUIM} & \LAT{Removable User Identity Module} & \LAT{SaaS} & \LAT{Software-as-a-Service} & \LAT{SCS} & \LAT{System Consultancy and Services} \\\hline
\LAT{SDL} & \LAT{Software Development Laboratories} & \LAT{SDSL} & \LAT{Symmetric Digital Subscriber Line} & \LAT{SECAM} & \LAT{Systeme Eelectronique Couleur Avec Memoire} & \LAT{SHF} & \LAT{Super High Frequency} \\\hline
\LAT{SID} & \LAT{System Identification Code} & \LAT{SIM} & \LAT{Subscriber Identity Module} & \LAT{SISD} & \LAT{Single Instruction, Single Data} & \LAT{SMR} & \LAT{Specialized Mobile Radio} \\\hline
\LAT{SMS} & \LAT{Short Message Service} & \LAT{SQL} & \LAT{Structured Query Language} & \LAT{SSID} & \LAT{Service Set Identifier} & \LAT{SSK} & \LAT{Service Subscribe Key} \\\hline
\LAT{STA} & \LAT{STore Accumulator} & \LAT{STM} & \LAT{Scanning Tunneling Microscope} & \LAT{STP} & \LAT{Shielded Twisted Pair} & \LAT{SUB} & \LAT{SUBtract} \\\hline
\LAT{TB} & \LAT{Terabyte} & \LAT{Tbps} & \LAT{Terabits per second} & \LAT{TCP} & \LAT{Transmission Control Protocol} & \LAT{TD-SCDMA} & \LAT{Time Division Synchronous Code Division Multiple Access} \\\hline
\LAT{TDD} & \LAT{Time Division Duplexing} & \LAT{TDMA} & \LAT{Time Division Multiple Access} & \LAT{TLD} & \LAT{Top Level Domain} & \LAT{TMSI} & \LAT{Temporary Mobile Subscriber Identity} \\\hline
\LAT{UAV} & \LAT{Unmanned-Aerial-Vehicle} & \LAT{UHF} & \LAT{Ultra High Frequency} & \LAT{UMTS} & \LAT{Universal Mobile Telecommunications System} & \LAT{URL} & \LAT{Uniform Resource Locator} \\\hline
\LAT{USB} & \LAT{Universal Serial Bus} & \LAT{UTP} & \LAT{Unshielded Twisted Pair} & \LAT{VB} & \LAT{Visual Basic} & \LAT{VHF} & \LAT{Very High Frequency} \\\hline
\LAT{VIRUS} & \LAT{Vital Information Resource Under Seize} & \LAT{VLF} & \LAT{Very Low Frequency} & \LAT{VOIP} & \LAT{Voice Over Internet Protocol} & \LAT{VPN} & \LAT{Virtual Private Network} \\\hline
\LAT{VR} & \LAT{Virtual Reality} & \LAT{VSAT} & \LAT{Very Small Aperture Terminal} & \LAT{WAN} & \LAT{Wide Area Network} & \LAT{WAP} & \LAT{Wireless Application Protocol} \\\hline
\LAT{WCDME} & \LAT{Wideband Code Division Multiple Access} & \LAT{WiBro} & \LAT{Wireless Broadband} & \LAT{Wi-Fi} & \LAT{Wireless Fidelity} & \LAT{WiMAX} & \LAT{Worldwide Interoperability for Microwave Access} \\\hline
\LAT{WPA} & \LAT{Wi-Fi Protected Access} & \LAT{WWW} & \LAT{World Wide Web} & \LAT{XHTML} & \LAT{Extensible Hyper Text Markup Language} & \LAT{YPSA} & \LAT{Young Power in Social Action} \\\hline
\LAT{4GL} & \LAT{Fourth Generation Language} & & & & & & \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\begin{multicols}{2}

\chsec{৮. বিভিন্ন উদ্ভাবক ও প্রযুক্তি উদ্ভাবক}
\noindent\tiny
\setlength{\tabcolsep}{1.0pt}
\renewcommand{\arraystretch}{1.06}
\begin{tabularx}{\linewidth}{|>{\raggedright\arraybackslash}p{0.17\linewidth}|>{\raggedright\arraybackslash}p{0.22\linewidth}|>{\centering\arraybackslash}p{0.10\linewidth}|>{\centering\arraybackslash}p{0.12\linewidth}|>{\raggedright\arraybackslash}X|}
\hline
\rowcolor{tblhdr} \B{বিষয়বস্তু} & \B{উদ্ভাবক} & \B{দেশ} & \B{জন্ম--মৃত্যু} & \B{সূত্র/অবদান} \\\hline
\B{বিশ্বগ্রাম} & \B{হার্বার্ট মার্শাল ম্যাকলুহান} & \LAT{Canada} & \LAT{1911--1980} & \B{দি গুটেনবার্গ গ্যালাক্সি (বই), ১৯৬২} \\\hline
\B{ভার্চুয়াল রিয়ালিটি} & \B{জ্যারন ল্যানিয়ার} & \LAT{USA} & \LAT{1960--} & \B{ইনভেন্টমেন্ট অব ভেল, ১৯৮৪} \\\hline
\B{আর্টিফিশিয়াল ইন্টেলিজেন্স} & \B{জন ম্যাকার্থি} & \LAT{USA} & \LAT{1927--2011} & \B{আর্টিফিশিয়াল ইন্টেলিজেন্স, ১৯৫৬} \\\hline
\B{রোবটিক্স} & \B{ইসমাইল আল-জাজারি} & \LAT{Arab} & \LAT{1136--1206} & \B{রোবটের ধারণা} \\\hline
\B{রোবটিক্স} & \B{জোসেফ এঞ্জেলবার্গার} & \LAT{USA} & \LAT{1925--2015} & \B{বাণিজ্যিক রোবট, ১৯৫৪} \\\hline
\B{বায়োমেট্রিক} & \B{আইজাক আসিমভ} & \LAT{USA} & \LAT{1920--1992} & \B{দি ফাউন্ডেশন সিরিজ; রোবট সিরিজ} \\\hline
\B{বায়োইনফরমেটিক্স} & \B{পলিন হোগওয়েগ} & \B{নেদারল্যান্ড} & \LAT{1943--} & \B{বায়োইনফরমেটিক্স, ১৯৭০} \\\hline
\B{বায়োটেকনোলজি} & \B{কারোলি এরেকি} & \B{হাঙ্গেরি} & \LAT{1878--1952} & \B{বায়োটেকনোলজি, ১৯১৯} \\\hline
\B{জেনেটিক ইঞ্জিনিয়ারিং} & \B{স্ট্যানলি কোহেন} & \LAT{USA} & \LAT{1942--2013} & \B{সোমাটোলজি, ১৯৭৩} \\\hline
\B{ন্যানো টেকনোলজি} & \B{রিচার্ড ফাইনম্যান} & \LAT{USA} & \LAT{1918--1988} & \B{ফিজিক্যাল ফিজিক্স, ১৯৫৯} \\\hline
\B{ন্যানো টেকনোলজি} & \B{নোরিও তানিগুচি} & \LAT{Japan} & \LAT{1912--1999} & \B{বেসিক কনসেপ্ট অব ন্যানো টেক, ১৯৭৪} \\\hline
\B{ন্যানো টেকনোলজি} & \B{এরিক ড্রেক্সলার} & \LAT{USA} & \LAT{1955--} & \B{মলিকুলার ন্যানো টেকনোলজি, ১৯৮০} \\\hline
\B{টেলিফোন} & \B{আলেকজান্ডার গ্রাহাম বেল} & \LAT{UK} & \LAT{1847--1922} & \B{টেলিফোন, ১৮৭৬} \\\hline
\B{বেতার} & \B{গুলিয়েলমো মার্কনি} & \LAT{Italy} & \LAT{1874--1937} & \B{বেতার, ১৮৯৫} \\\hline
\B{মোবাইল ফোন} & \B{মার্টিন কুপার} & \LAT{USA} & \LAT{1928--} & \B{মোবাইল ফোন, ১৯৭৩} \\\hline
\B{টেলিগ্রাফ} & \B{স্যামুয়েল ফিনলে মোর্স} & \LAT{USA} & \LAT{1791--1872} & \B{টেলিগ্রাফ, ১৮৩৭} \\\hline
\B{ই-মেইল} & \B{রেমন্ড স্যামুয়েল টমলিনসন} & \LAT{USA} & \LAT{1941--2016} & \B{ই-মেইল, ১৯৭১} \\\hline
\B{Bluetooth} & \B{জাপ হার্টসেন} & \LAT{NL} & \LAT{1963--} & \LAT{Bluetooth, 1994} \\\hline
\B{TCP/IP} & \B{ভিন্টন গ্রে সার্ফ} & \LAT{USA} & \LAT{1943--} & \LAT{TCP/IP, 1974} \\\hline
\B{WWW} & \B{টিম বার্নার্স লি} & \LAT{UK} & \LAT{1955--} & \LAT{WWW, 1989} \\\hline
\B{Google} & \B{ল্যারি পেইজ} & \LAT{USA} & \LAT{1973--} & \LAT{Google, 1998} \\\hline
\B{Google} & \B{সের্গেই ব্রিন} & \LAT{USA} & \LAT{1973--} & \LAT{Google, 1998} \\\hline
\B{Wi-Fi} & \B{ভিক হায়েস} & \B{নেদারল্যান্ড} & \LAT{1941--} & \LAT{Wi-Fi, 1991} \\\hline
\B{C Programming} & \B{ডেনিস ম্যাক অ্যালিস্টার রিচি} & \LAT{USA} & \LAT{1941--2011} & \LAT{C, 1972} \\\hline
\B{C++ Programming} & \B{বিয়ারনে স্ট্রাউস্ট্রাপ} & \LAT{Denmark} & \LAT{1950--} & \LAT{C++, 1983} \\\hline
\B{Python} & \B{গুইডো ভ্যান রোসাম} & \LAT{NL} & \LAT{1956--} & \LAT{Python, 1991} \\\hline
\B{De Morgan's} & \B{অগাস্টাস ডি মরগান} & \LAT{UK} & \LAT{1806--1871} & \B{De Morgan's laws, ১৮৪৭} \\\hline
\B{বুলিয়ান বীজগণিত} & \B{জর্জ বুল} & \LAT{UK} & \LAT{1815--1864} & \B{বুলিয়ান বীজগণিত, ১৮৪৭} \\\hline
\B{RDBMS} & \B{এডগার ফ্র্যাঙ্ক কড} & \LAT{UK} & \LAT{1923--2003} & \LAT{RDBMS, 1970} \\\hline
\B{Microsoft} & \B{উইলিয়াম হেনরি বিল গেটস} & \LAT{USA} & \LAT{1955--} & \LAT{Microsoft, 1975} \\\hline
\B{ট্রানজিস্টর} & \B{উইলিয়াম ব্র্যাডফোর্ড শকলি} & \LAT{UK} & \LAT{1910--1989} & \B{ট্রানজিস্টর, ১৯৪৭} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\chsec{৯. মৌলিক গেইটসমূহ (Basic Gates)}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.09\linewidth}|c|c|>{\centering\arraybackslash}p{0.14\linewidth}|X|}
\hline
\rowcolor{tblhdr} \B{গেইট} & \B{প্রতীক} & \B{ফাংশন} & \B{সার্কিট} & \B{সত্য সারণি} \\\hline
\B{OR} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[or gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B}; \node[right=0.28 of g.output, scale=0.85] {X};
\end{tikzpicture}
& \LAT{$X=A+B$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0.32)--(0.22,0.32); \draw (0.22,0.22)--(0.22,0.42);
\draw (0.32,0.32)--(0.65,0.32)--(0.65,0.0);
\draw (0,-0.32)--(0.22,-0.32); \draw (0.22,-0.42)--(0.22,-0.22);
\draw (0.32,-0.32)--(0.65,-0.32)--(0.65,0.0);
\draw (0.65,0.0)--(0.95,0.0);
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&0\\0&1&1\\1&0&1\\1&1&1 \end{tabular} \\\hline
\B{AND} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[and gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B}; \node[right=0.28 of g.output, scale=0.85] {X};
\end{tikzpicture}
& \LAT{$X=A\cdot B$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0)--(0.18,0); \draw (0.18,-0.10)--(0.18,0.10);
\draw (0.28,0)--(0.52,0); \draw (0.52,-0.10)--(0.52,0.10);
\draw (0.62,0)--(0.95,0);
\node[scale=0.55] at (0.18,0.22) {A}; \node[scale=0.55] at (0.52,0.22) {B};
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&0\\0&1&0\\1&0&0\\1&1&1 \end{tabular} \\\hline
\B{NOT} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[not gate US, draw] (g) {};
\draw (g.input) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input, scale=0.85] {A}; \node[right=0.28 of g.output, scale=0.85] {$\bar{A}$};
\end{tikzpicture}
& \LAT{$X=\bar{A}$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0)--(0.22,0); \draw (0.22,-0.10)--(0.22,0.10);
\draw (0.32,0)--(0.62,0); \draw[fill=white] (0.66,0) circle (0.04);
\draw (0.70,0)--(0.95,0);
\node[scale=0.55] at (0.18,0.22) {A};
\end{tikzpicture}
&
\begin{tabular}{c|c} A&X\\\hline 0&1\\1&0 \end{tabular} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize
\itm{1} \B{OR:} \B{যেকোনো একটি ইনপুট} \LAT{1} \B{হলে আউটপুট} \LAT{1}
\itm{2} \B{AND:} \B{সব ইনপুট} \LAT{1} \B{হলেই আউটপুট} \LAT{1}
\itm{3} \B{NOT:} \B{ইনপুট উল্টে আউটপুট দেয় (Inverter)}

\chsec{১০. যৌগিক গেইটসমূহ (Compound Gates)}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.09\linewidth}|c|c|>{\centering\arraybackslash}p{0.14\linewidth}|X|}
\hline
\rowcolor{tblhdr} \B{গেইট} & \B{প্রতীক} & \B{ফাংশন} & \B{সার্কিট} & \B{সত্য সারণি} \\\hline
\B{NOR} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[nor gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B};
\end{tikzpicture}
& \LAT{$X=\overline{A+B}$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0.30)--(0.22,0.30); \draw (0.22,0.20)--(0.22,0.40);
\draw (0.32,0.30)--(0.58,0.30)--(0.58,0.0);
\draw (0,-0.30)--(0.22,-0.30); \draw (0.22,-0.40)--(0.22,-0.20);
\draw (0.32,-0.30)--(0.58,-0.30)--(0.58,0.0);
\draw (0.58,0.0)--(0.72,0.0); \draw[fill=white] (0.76,0.0) circle(0.04);
\draw (0.80,0.0)--(0.95,0.0);
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&1\\0&1&0\\1&0&0\\1&1&0 \end{tabular} \\\hline
\B{NAND} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[nand gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B};
\end{tikzpicture}
& \LAT{$X=\overline{A\cdot B}$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0)--(0.18,0); \draw (0.18,-0.10)--(0.18,0.10);
\draw (0.28,0)--(0.50,0); \draw (0.50,-0.10)--(0.50,0.10);
\draw (0.60,0)--(0.72,0); \draw[fill=white] (0.76,0) circle(0.04);
\draw (0.80,0)--(0.95,0);
\node[scale=0.55] at (0.18,0.22) {A}; \node[scale=0.55] at (0.50,0.22) {B};
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&1\\0&1&1\\1&0&1\\1&1&0 \end{tabular} \\\hline
\B{XOR} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[xor gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B};
\end{tikzpicture}
& \LAT{$X=A\oplus B$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0.28)--(0.22,0.28); \draw (0.22,0.18)--(0.22,0.38);
\draw (0.32,0.28)--(0.62,0.28)--(0.62,0.0);
\draw (0,-0.28)--(0.22,-0.28); \draw (0.22,-0.38)--(0.22,-0.18);
\draw (0.32,-0.28)--(0.62,-0.28)--(0.62,0.0);
\draw (0.62,0.0)--(0.95,0.0);
\node[scale=0.50] at (0.50,0.42) {$\oplus$};
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&0\\0&1&1\\1&0&1\\1&1&0 \end{tabular} \\\hline
\B{XNOR} &
\begin{tikzpicture}[baseline=-2pt,scale=0.40]
\node[xnor gate US, draw, logic gate inputs=nn] (g) {};
\draw (g.input 1) -- ++(-0.3,0); \draw (g.input 2) -- ++(-0.3,0); \draw (g.output) -- ++(0.3,0);
\node[left=0.28 of g.input 1, scale=0.85] {A}; \node[left=0.28 of g.input 2, scale=0.85] {B};
\end{tikzpicture}
& \LAT{$X=\overline{A\oplus B}$} &
\begin{tikzpicture}[baseline=-3pt,scale=0.58,thick]
\draw (0,0.28)--(0.22,0.28); \draw (0.22,0.18)--(0.22,0.38);
\draw (0.32,0.28)--(0.58,0.28)--(0.58,0.0);
\draw (0,-0.28)--(0.22,-0.28); \draw (0.22,-0.38)--(0.22,-0.18);
\draw (0.32,-0.28)--(0.58,-0.28)--(0.58,0.0);
\draw (0.58,0.0)--(0.72,0.0); \draw[fill=white] (0.76,0.0) circle(0.04);
\draw (0.80,0.0)--(0.95,0.0);
\end{tikzpicture}
&
\begin{tabular}{cc|c} A&B&X\\\hline 0&0&1\\0&1&0\\1&0&0\\1&1&1 \end{tabular} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize
\itm{1} \B{ইউনিভার্সাল গেইট:} \LAT{NAND} \B{ও} \LAT{NOR} \B{দ্বারা সব মৌলিক গেইট তৈরি সম্ভব}
\itm{2} \B{NOR দিয়ে NOT:} \B{দুই ইনপুট একসাথে দিলে} \LAT{NOT} \B{হয়}
\itm{3} \B{NAND দিয়ে NOT:} \B{দুই ইনপুট একসাথে দিলে} \LAT{NOT} \B{হয়}
\itm{4} \B{XOR:} \B{ইনপুট ভিন্ন হলে} \LAT{1}\B{, একই হলে} \LAT{0}\B{; হাফ অ্যাডারে ব্যবহৃত}

\end{multicols}

\vspace{2pt}
\chsecfull{১১. DEC-BIN-HEX-OCT টেবিল (১--১০০)}
\vspace{2pt}
\noindent\tiny
\setlength{\tabcolsep}{1.2pt}
\renewcommand{\arraystretch}{1.02}
\begin{multicols}{4}
\begin{tabular}{|r|r|r|r|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{Bin} & \LAT{Hex} & \LAT{Oct} \\\hline
\LAT{1} & \LAT{1} & \LAT{1} & \LAT{1} \\\hline
\LAT{2} & \LAT{10} & \LAT{2} & \LAT{2} \\\hline
\LAT{3} & \LAT{11} & \LAT{3} & \LAT{3} \\\hline
\LAT{4} & \LAT{100} & \LAT{4} & \LAT{4} \\\hline
\LAT{5} & \LAT{101} & \LAT{5} & \LAT{5} \\\hline
\LAT{6} & \LAT{110} & \LAT{6} & \LAT{6} \\\hline
\LAT{7} & \LAT{111} & \LAT{7} & \LAT{7} \\\hline
\LAT{8} & \LAT{1000} & \LAT{8} & \LAT{10} \\\hline
\LAT{9} & \LAT{1001} & \LAT{9} & \LAT{11} \\\hline
\LAT{10} & \LAT{1010} & \LAT{A} & \LAT{12} \\\hline
\LAT{11} & \LAT{1011} & \LAT{B} & \LAT{13} \\\hline
\LAT{12} & \LAT{1100} & \LAT{C} & \LAT{14} \\\hline
\LAT{13} & \LAT{1101} & \LAT{D} & \LAT{15} \\\hline
\LAT{14} & \LAT{1110} & \LAT{E} & \LAT{16} \\\hline
\LAT{15} & \LAT{1111} & \LAT{F} & \LAT{17} \\\hline
\LAT{16} & \LAT{10000} & \LAT{10} & \LAT{20} \\\hline
\LAT{17} & \LAT{10001} & \LAT{11} & \LAT{21} \\\hline
\LAT{18} & \LAT{10010} & \LAT{12} & \LAT{22} \\\hline
\LAT{19} & \LAT{10011} & \LAT{13} & \LAT{23} \\\hline
\LAT{20} & \LAT{10100} & \LAT{14} & \LAT{24} \\\hline
\LAT{21} & \LAT{10101} & \LAT{15} & \LAT{25} \\\hline
\LAT{22} & \LAT{10110} & \LAT{16} & \LAT{26} \\\hline
\LAT{23} & \LAT{10111} & \LAT{17} & \LAT{27} \\\hline
\LAT{24} & \LAT{11000} & \LAT{18} & \LAT{30} \\\hline
\LAT{25} & \LAT{11001} & \LAT{19} & \LAT{31} \\\hline
\end{tabular}
\columnbreak
\begin{tabular}{|r|r|r|r|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{Bin} & \LAT{Hex} & \LAT{Oct} \\\hline
\LAT{26} & \LAT{11010} & \LAT{1A} & \LAT{32} \\\hline
\LAT{27} & \LAT{11011} & \LAT{1B} & \LAT{33} \\\hline
\LAT{28} & \LAT{11100} & \LAT{1C} & \LAT{34} \\\hline
\LAT{29} & \LAT{11101} & \LAT{1D} & \LAT{35} \\\hline
\LAT{30} & \LAT{11110} & \LAT{1E} & \LAT{36} \\\hline
\LAT{31} & \LAT{11111} & \LAT{1F} & \LAT{37} \\\hline
\LAT{32} & \LAT{100000} & \LAT{20} & \LAT{40} \\\hline
\LAT{33} & \LAT{100001} & \LAT{21} & \LAT{41} \\\hline
\LAT{34} & \LAT{100010} & \LAT{22} & \LAT{42} \\\hline
\LAT{35} & \LAT{100011} & \LAT{23} & \LAT{43} \\\hline
\LAT{36} & \LAT{100100} & \LAT{24} & \LAT{44} \\\hline
\LAT{37} & \LAT{100101} & \LAT{25} & \LAT{45} \\\hline
\LAT{38} & \LAT{100110} & \LAT{26} & \LAT{46} \\\hline
\LAT{39} & \LAT{100111} & \LAT{27} & \LAT{47} \\\hline
\LAT{40} & \LAT{101000} & \LAT{28} & \LAT{50} \\\hline
\LAT{41} & \LAT{101001} & \LAT{29} & \LAT{51} \\\hline
\LAT{42} & \LAT{101010} & \LAT{2A} & \LAT{52} \\\hline
\LAT{43} & \LAT{101011} & \LAT{2B} & \LAT{53} \\\hline
\LAT{44} & \LAT{101100} & \LAT{2C} & \LAT{54} \\\hline
\LAT{45} & \LAT{101101} & \LAT{2D} & \LAT{55} \\\hline
\LAT{46} & \LAT{101110} & \LAT{2E} & \LAT{56} \\\hline
\LAT{47} & \LAT{101111} & \LAT{2F} & \LAT{57} \\\hline
\LAT{48} & \LAT{110000} & \LAT{30} & \LAT{60} \\\hline
\LAT{49} & \LAT{110001} & \LAT{31} & \LAT{61} \\\hline
\LAT{50} & \LAT{110010} & \LAT{32} & \LAT{62} \\\hline
\end{tabular}
\columnbreak
\begin{tabular}{|r|r|r|r|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{Bin} & \LAT{Hex} & \LAT{Oct} \\\hline
\LAT{51} & \LAT{110011} & \LAT{33} & \LAT{63} \\\hline
\LAT{52} & \LAT{110100} & \LAT{34} & \LAT{64} \\\hline
\LAT{53} & \LAT{110101} & \LAT{35} & \LAT{65} \\\hline
\LAT{54} & \LAT{110110} & \LAT{36} & \LAT{66} \\\hline
\LAT{55} & \LAT{110111} & \LAT{37} & \LAT{67} \\\hline
\LAT{56} & \LAT{111000} & \LAT{38} & \LAT{70} \\\hline
\LAT{57} & \LAT{111001} & \LAT{39} & \LAT{71} \\\hline
\LAT{58} & \LAT{111010} & \LAT{3A} & \LAT{72} \\\hline
\LAT{59} & \LAT{111011} & \LAT{3B} & \LAT{73} \\\hline
\LAT{60} & \LAT{111100} & \LAT{3C} & \LAT{74} \\\hline
\LAT{61} & \LAT{111101} & \LAT{3D} & \LAT{75} \\\hline
\LAT{62} & \LAT{111110} & \LAT{3E} & \LAT{76} \\\hline
\LAT{63} & \LAT{111111} & \LAT{3F} & \LAT{77} \\\hline
\LAT{64} & \LAT{1000000} & \LAT{40} & \LAT{100} \\\hline
\LAT{65} & \LAT{1000001} & \LAT{41} & \LAT{101} \\\hline
\LAT{66} & \LAT{1000010} & \LAT{42} & \LAT{102} \\\hline
\LAT{67} & \LAT{1000011} & \LAT{43} & \LAT{103} \\\hline
\LAT{68} & \LAT{1000100} & \LAT{44} & \LAT{104} \\\hline
\LAT{69} & \LAT{1000101} & \LAT{45} & \LAT{105} \\\hline
\LAT{70} & \LAT{1000110} & \LAT{46} & \LAT{106} \\\hline
\LAT{71} & \LAT{1000111} & \LAT{47} & \LAT{107} \\\hline
\LAT{72} & \LAT{1001000} & \LAT{48} & \LAT{110} \\\hline
\LAT{73} & \LAT{1001001} & \LAT{49} & \LAT{111} \\\hline
\LAT{74} & \LAT{1001010} & \LAT{4A} & \LAT{112} \\\hline
\LAT{75} & \LAT{1001011} & \LAT{4B} & \LAT{113} \\\hline
\end{tabular}
\columnbreak
\begin{tabular}{|r|r|r|r|}
\hline
\rowcolor{tblhdr} \LAT{Dec} & \LAT{Bin} & \LAT{Hex} & \LAT{Oct} \\\hline
\LAT{76} & \LAT{1001100} & \LAT{4C} & \LAT{114} \\\hline
\LAT{77} & \LAT{1001101} & \LAT{4D} & \LAT{115} \\\hline
\LAT{78} & \LAT{1001110} & \LAT{4E} & \LAT{116} \\\hline
\LAT{79} & \LAT{1001111} & \LAT{4F} & \LAT{117} \\\hline
\LAT{80} & \LAT{1010000} & \LAT{50} & \LAT{120} \\\hline
\LAT{81} & \LAT{1010001} & \LAT{51} & \LAT{121} \\\hline
\LAT{82} & \LAT{1010010} & \LAT{52} & \LAT{122} \\\hline
\LAT{83} & \LAT{1010011} & \LAT{53} & \LAT{123} \\\hline
\LAT{84} & \LAT{1010100} & \LAT{54} & \LAT{124} \\\hline
\LAT{85} & \LAT{1010101} & \LAT{55} & \LAT{125} \\\hline
\LAT{86} & \LAT{1010110} & \LAT{56} & \LAT{126} \\\hline
\LAT{87} & \LAT{1010111} & \LAT{57} & \LAT{127} \\\hline
\LAT{88} & \LAT{1011000} & \LAT{58} & \LAT{130} \\\hline
\LAT{89} & \LAT{1011001} & \LAT{59} & \LAT{131} \\\hline
\LAT{90} & \LAT{1011010} & \LAT{5A} & \LAT{132} \\\hline
\LAT{91} & \LAT{1011011} & \LAT{5B} & \LAT{133} \\\hline
\LAT{92} & \LAT{1011100} & \LAT{5C} & \LAT{134} \\\hline
\LAT{93} & \LAT{1011101} & \LAT{5D} & \LAT{135} \\\hline
\LAT{94} & \LAT{1011110} & \LAT{5E} & \LAT{136} \\\hline
\LAT{95} & \LAT{1011111} & \LAT{5F} & \LAT{137} \\\hline
\LAT{96} & \LAT{1100000} & \LAT{60} & \LAT{140} \\\hline
\LAT{97} & \LAT{1100001} & \LAT{61} & \LAT{141} \\\hline
\LAT{98} & \LAT{1100010} & \LAT{62} & \LAT{142} \\\hline
\LAT{99} & \LAT{1100011} & \LAT{63} & \LAT{143} \\\hline
\LAT{100} & \LAT{1100100} & \LAT{64} & \LAT{144} \\\hline
\end{tabular}
\end{multicols}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\vspace{2pt}
\chsecfull{১২. ASCII টেবিল (বাইনারি কোড সহ, ০--১২৭)}
\vspace{2pt}
\noindent\tiny
\setlength{\tabcolsep}{1.2pt}
\renewcommand{\arraystretch}{1.02}
\begin{multicols}{2}
\begin{tabular}{|r|r|c||r|r|c|}
\hline
\rowcolor{tblhdr} \LAT{Bin} & \LAT{Dec} & \LAT{Char} & \LAT{Bin} & \LAT{Dec} & \LAT{Char} \\\hline
\LAT{0000 0000} & \LAT{0} & \LAT{NUL} & \LAT{0010 0000} & \LAT{32} & \LAT{SP} \\\hline
\LAT{0000 0001} & \LAT{1} & \LAT{SOH} & \LAT{0010 0001} & \LAT{33} & \LAT{!} \\\hline
\LAT{0000 0010} & \LAT{2} & \LAT{STX} & \LAT{0010 0010} & \LAT{34} & \LAT{"} \\\hline
\LAT{0000 0011} & \LAT{3} & \LAT{ETX} & \LAT{0010 0011} & \LAT{35} & \LAT{\#} \\\hline
\LAT{0000 0100} & \LAT{4} & \LAT{EOT} & \LAT{0010 0100} & \LAT{36} & \LAT{\$} \\\hline
\LAT{0000 0101} & \LAT{5} & \LAT{ENQ} & \LAT{0010 0101} & \LAT{37} & \LAT{\%} \\\hline
\LAT{0000 0110} & \LAT{6} & \LAT{ACK} & \LAT{0010 0110} & \LAT{38} & \LAT{\&} \\\hline
\LAT{0000 0111} & \LAT{7} & \LAT{BEL} & \LAT{0010 0111} & \LAT{39} & \LAT{'} \\\hline
\LAT{0000 1000} & \LAT{8} & \LAT{BS} & \LAT{0010 1000} & \LAT{40} & \LAT{(} \\\hline
\LAT{0000 1001} & \LAT{9} & \LAT{HT} & \LAT{0010 1001} & \LAT{41} & \LAT{)} \\\hline
\LAT{0000 1010} & \LAT{10} & \LAT{LF} & \LAT{0010 1010} & \LAT{42} & \LAT{*} \\\hline
\LAT{0000 1011} & \LAT{11} & \LAT{VT} & \LAT{0010 1011} & \LAT{43} & \LAT{+} \\\hline
\LAT{0000 1100} & \LAT{12} & \LAT{FF} & \LAT{0010 1100} & \LAT{44} & \LAT{,} \\\hline
\LAT{0000 1101} & \LAT{13} & \LAT{CR} & \LAT{0010 1101} & \LAT{45} & \LAT{-} \\\hline
\LAT{0000 1110} & \LAT{14} & \LAT{SO} & \LAT{0010 1110} & \LAT{46} & \LAT{.} \\\hline
\LAT{0000 1111} & \LAT{15} & \LAT{SI} & \LAT{0010 1111} & \LAT{47} & \LAT{/} \\\hline
\LAT{0001 0000} & \LAT{16} & \LAT{DLE} & \LAT{0011 0000} & \LAT{48} & \LAT{0} \\\hline
\LAT{0001 0001} & \LAT{17} & \LAT{DC1} & \LAT{0011 0001} & \LAT{49} & \LAT{1} \\\hline
\LAT{0001 0010} & \LAT{18} & \LAT{DC2} & \LAT{0011 0010} & \LAT{50} & \LAT{2} \\\hline
\LAT{0001 0011} & \LAT{19} & \LAT{DC3} & \LAT{0011 0011} & \LAT{51} & \LAT{3} \\\hline
\LAT{0001 0100} & \LAT{20} & \LAT{DC4} & \LAT{0011 0100} & \LAT{52} & \LAT{4} \\\hline
\LAT{0001 0101} & \LAT{21} & \LAT{NAK} & \LAT{0011 0101} & \LAT{53} & \LAT{5} \\\hline
\LAT{0001 0110} & \LAT{22} & \LAT{SYN} & \LAT{0011 0110} & \LAT{54} & \LAT{6} \\\hline
\LAT{0001 0111} & \LAT{23} & \LAT{ETB} & \LAT{0011 0111} & \LAT{55} & \LAT{7} \\\hline
\LAT{0001 1000} & \LAT{24} & \LAT{CAN} & \LAT{0011 1000} & \LAT{56} & \LAT{8} \\\hline
\LAT{0001 1001} & \LAT{25} & \LAT{EM} & \LAT{0011 1001} & \LAT{57} & \LAT{9} \\\hline
\LAT{0001 1010} & \LAT{26} & \LAT{SUB} & \LAT{0011 1010} & \LAT{58} & \LAT{:} \\\hline
\LAT{0001 1011} & \LAT{27} & \LAT{ESC} & \LAT{0011 1011} & \LAT{59} & \LAT{;} \\\hline
\LAT{0001 1100} & \LAT{28} & \LAT{FS} & \LAT{0011 1100} & \LAT{60} & \LAT{$<$} \\\hline
\LAT{0001 1101} & \LAT{29} & \LAT{GS} & \LAT{0011 1101} & \LAT{61} & \LAT{=} \\\hline
\LAT{0001 1110} & \LAT{30} & \LAT{RS} & \LAT{0011 1110} & \LAT{62} & \LAT{$>$} \\\hline
\LAT{0001 1111} & \LAT{31} & \LAT{US} & \LAT{0001 1111} & \LAT{63} & \LAT{?} \\\hline
\end{tabular}
\columnbreak
\begin{tabular}{|r|r|c||r|r|c|}
\hline
\rowcolor{tblhdr} \LAT{Bin} & \LAT{Dec} & \LAT{Char} & \LAT{Bin} & \LAT{Dec} & \LAT{Char} \\\hline
\LAT{0100 0000} & \LAT{64} & \LAT{@} & \LAT{0110 0000} & \LAT{96} & \LAT{`} \\\hline
\LAT{0100 0001} & \LAT{65} & \LAT{A} & \LAT{0110 0001} & \LAT{97} & \LAT{a} \\\hline
\LAT{0100 0010} & \LAT{66} & \LAT{B} & \LAT{0110 0010} & \LAT{98} & \LAT{b} \\\hline
\LAT{0100 0011} & \LAT{67} & \LAT{C} & \LAT{0110 0011} & \LAT{99} & \LAT{c} \\\hline
\LAT{0100 0100} & \LAT{68} & \LAT{D} & \LAT{0110 0100} & \LAT{100} & \LAT{d} \\\hline
\LAT{0100 0101} & \LAT{69} & \LAT{E} & \LAT{0110 0101} & \LAT{101} & \LAT{e} \\\hline
\LAT{0100 0110} & \LAT{70} & \LAT{F} & \LAT{0110 0110} & \LAT{102} & \LAT{f} \\\hline
\LAT{0100 0111} & \LAT{71} & \LAT{G} & \LAT{0110 0111} & \LAT{103} & \LAT{g} \\\hline
\LAT{0100 1000} & \LAT{72} & \LAT{H} & \LAT{0110 1000} & \LAT{104} & \LAT{h} \\\hline
\LAT{0100 1001} & \LAT{73} & \LAT{I} & \LAT{0110 1001} & \LAT{105} & \LAT{i} \\\hline
\LAT{0100 1010} & \LAT{74} & \LAT{J} & \LAT{0110 1010} & \LAT{106} & \LAT{j} \\\hline
\LAT{0100 1011} & \LAT{75} & \LAT{K} & \LAT{0110 1011} & \LAT{107} & \LAT{k} \\\hline
\LAT{0100 1100} & \LAT{76} & \LAT{L} & \LAT{0110 1100} & \LAT{108} & \LAT{l} \\\hline
\LAT{0100 1101} & \LAT{77} & \LAT{M} & \LAT{0110 1101} & \LAT{109} & \LAT{m} \\\hline
\LAT{0100 1110} & \LAT{78} & \LAT{N} & \LAT{0110 1110} & \LAT{110} & \LAT{n} \\\hline
\LAT{0100 1111} & \LAT{79} & \LAT{O} & \LAT{0110 1111} & \LAT{111} & \LAT{o} \\\hline
\LAT{0101 0000} & \LAT{80} & \LAT{P} & \LAT{0111 0000} & \LAT{112} & \LAT{p} \\\hline
\LAT{0101 0001} & \LAT{81} & \LAT{Q} & \LAT{0111 0001} & \LAT{113} & \LAT{q} \\\hline
\LAT{0101 0010} & \LAT{82} & \LAT{R} & \LAT{0111 0010} & \LAT{114} & \LAT{r} \\\hline
\LAT{0101 0011} & \LAT{83} & \LAT{S} & \LAT{0111 0011} & \LAT{115} & \LAT{s} \\\hline
\LAT{0101 0100} & \LAT{84} & \LAT{T} & \LAT{0111 0100} & \LAT{116} & \LAT{t} \\\hline
\LAT{0101 0101} & \LAT{85} & \LAT{U} & \LAT{0111 0101} & \LAT{117} & \LAT{u} \\\hline
\LAT{0101 0110} & \LAT{86} & \LAT{V} & \LAT{0111 0110} & \LAT{118} & \LAT{v} \\\hline
\LAT{0101 0111} & \LAT{87} & \LAT{W} & \LAT{0111 0111} & \LAT{119} & \LAT{w} \\\hline
\LAT{0101 1000} & \LAT{88} & \LAT{X} & \LAT{0111 1000} & \LAT{120} & \LAT{x} \\\hline
\LAT{0101 1001} & \LAT{89} & \LAT{Y} & \LAT{0111 1001} & \LAT{121} & \LAT{y} \\\hline
\LAT{0101 1010} & \LAT{90} & \LAT{Z} & \LAT{0111 1010} & \LAT{122} & \LAT{z} \\\hline
\LAT{0101 1011} & \LAT{91} & \LAT{[} & \LAT{0111 1011} & \LAT{123} & \LAT{\{} \\\hline
\LAT{0101 1100} & \LAT{92} & \LAT{\textbackslash} & \LAT{0111 1100} & \LAT{124} & \LAT{|} \\\hline
\LAT{0101 1101} & \LAT{93} & \LAT{]} & \LAT{0111 1101} & \LAT{125} & \LAT{\}} \\\hline
\LAT{0101 1110} & \LAT{94} & \LAT{\^{}} & \LAT{0111 1110} & \LAT{126} & \LAT{\textasciitilde} \\\hline
\LAT{0101 1111} & \LAT{95} & \LAT{\_} & \LAT{0111 1111} & \LAT{127} & \LAT{DEL} \\\hline
\end{tabular}
\end{multicols}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\begin{multicols}{2}

\chsec{১৩. বুলিয়ান উপপাদ্য (Boolean Theorems)}

\chsub{}{\B{মৌলিক উপপাদ্য (Basic Theorem)}}
\noindent\scriptsize
\begin{tabular}{ll}
\LAT{(i) $A+0=A$} & \LAT{(vi) $A\cdot\bar{A}=0$}\\
\LAT{(ii) $A+\bar{A}=1$} & \LAT{(vii) $A\cdot A=A$}\\
\LAT{(iii) $A+A=A$} & \LAT{(viii) $A\cdot0=0$}\\
\LAT{(iv) $A+1=1$} & \LAT{(ix) $\bar{\bar{A}}=A$}\\
\LAT{(v) $A\cdot1=A$} &
\end{tabular}
\normalsize

\chsub{}{\B{বিনিময় উপপাদ্য (Commutative)}}
\noindent\scriptsize
\LAT{(i) $A+B=B+A$} \quad \LAT{(ii) $A\cdot B=B\cdot A$}
\normalsize

\chsub{}{\B{সংযোজন উপপাদ্য (Associative)}}
\noindent\scriptsize
\LAT{(i) $A+(B+C)=(A+B)+C$} \quad \LAT{(ii) $A(BC)=(AB)C$}
\normalsize

\chsub{}{\B{বিতরণ উপপাদ্য (Distributive)}}
\noindent\scriptsize
\LAT{(i) $A(B+C)=AB+AC$} \quad \LAT{(ii) $A+BC=(A+B)(A+C)$}
\normalsize

\chsub{}{\B{ডি-মরগান উপপাদ্য (De-Morgan's)}}
\noindent\scriptsize
\LAT{(i) $\overline{A+B}=\bar{A}\cdot\bar{B}$} \quad \LAT{(ii) $\overline{A\cdot B}=\bar{A}+\bar{B}$}
\normalsize

\chsub{}{\B{পরিশোষণ উপপাদ্য (Absorption)}}
\noindent\scriptsize
\LAT{(i) $A+AB=A$} \quad \LAT{(ii) $A(A+B)=A$}
\normalsize

\noindent\scriptsize\textbf{\B{Note:}} \B{বুলিয়ান উপপাদ্যে চলকের মান} \LAT{0} \B{বা} \LAT{1} \B{ধরে যেকোনো সত্যতা প্রমাণ করা যায়।}
\normalsize

\chsec{১৪. HTML-এ ব্যবহৃত ট্যাগসমূহ}

\chsub{}{\LAT{HTML} \B{ফরম্যাটিং ট্যাগ}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|l|}
\hline
\rowcolor{tblhdr} \B{ট্যাগ} & \B{কাজ} & \B{ফলাফল} \\\hline
\LAT{<u>/<ins>} & \B{আন্ডারলাইন করে} & \underline{text} \\\hline
\LAT{<i>/<em>} & \B{ইটালিক করে} & \textit{text} \\\hline
\LAT{<b>/<strong>} & \B{বোল্ড করে} & \textbf{text} \\\hline
\LAT{<big>} & \B{বড় ফন্ট দেখায়} & {\large text} \\\hline
\LAT{<small>} & \B{ছোট ফন্ট দেখায়} & {\footnotesize text} \\\hline
\LAT{<del>/<s>/<strike>} & \B{কাটাচিহ্ন দেয়} & \sout{text} \\\hline
\LAT{<sub>} & \B{সাবস্ক্রিপ্ট} & H\textsubscript{2}O \\\hline
\LAT{<sup>} & \B{সুপারস্ক্রিপ্ট} & x\textsuperscript{2} \\\hline
\LAT{<q>} & \B{শর্ট কোটেশন} & "text" \\\hline
\LAT{<mark>} & \B{হাইলাইট করে} & \colorbox{yellow}{\tiny text} \\\hline
\LAT{<pre>} & \B{প্রিফরম্যাটেড টেক্সট} & {\ttfamily text} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{\LAT{HTML} \B{লিস্ট ট্যাগ}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|}
\hline
\rowcolor{tblhdr} \B{ট্যাগ} & \B{কাজ} \\\hline
\LAT{<ol>} & \B{অর্ডার্ড (ক্রমিক) লিস্ট তৈরি করে} \\\hline
\LAT{<ul>} & \B{আনঅর্ডার্ড লিস্ট তৈরি করে} \\\hline
\LAT{<li>} & \B{লিস্ট আইটেম নির্দেশ করে} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\noindent\scriptsize
\B{Ordered list type:} \LAT{type="A"$\to$A,B,C}; \LAT{"a"$\to$a,b,c}; \LAT{"I"$\to$I,II,III}; \LAT{"i"$\to$i,ii,iii}; \LAT{"1"$\to$1,2,3}

\noindent\B{Unordered list type:} \LAT{type="disc"$\to$}\textbullet; \LAT{"circle"$\to$}$\circ$; \LAT{"square"$\to$}$\square$
\normalsize

\chsub{}{\LAT{HTML} \B{টেবিল ট্যাগ}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|}
\hline
\rowcolor{tblhdr} \B{ট্যাগ} & \B{কাজ} \\\hline
\LAT{<table>...</table>} & \B{টেবিল তৈরির জন্য ব্যবহার} \\\hline
\LAT{<caption>...</caption>} & \B{টেবিলের শিরোনাম লেখার জন্য} \\\hline
\LAT{<th>...</th>} & \B{কলামের হেডিং নির্ধারণ করে} \\\hline
\LAT{<tr>...</tr>} & \B{রো বা সারি নির্ধারণ করে} \\\hline
\LAT{<td>...</td>} & \B{টেবিল ডেটা লেখার জন্য} \\\hline
\LAT{<tfoot>} & \B{ফুটার গ্রুপ করার জন্য} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{\LAT{<table>} \B{অ্যাট্রিবিউট}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|>{\centering\arraybackslash}p{0.22\linewidth}|X|}
\hline
\rowcolor{tblhdr} \B{অ্যাট্রিবিউট} & \B{মান} & \B{ব্যবহার} \\\hline
\LAT{border} & \LAT{1,2,...} & \B{বর্ডার তৈরি করতে} \\\hline
\LAT{bordercolor} & \LAT{rgb(x,x,x)/\#xxxxxx} & \B{বর্ডারের রং নির্ধারণ} \\\hline
\LAT{bgcolor} & \LAT{\#xxxxxx/colorname} & \B{ব্যাকগ্রাউন্ড কালার সেট} \\\hline
\LAT{cellspacing} & \LAT{2,3,4,...} & \B{সেলের মধ্যে ফাঁকা স্থান} \\\hline
\LAT{cellpadding} & \LAT{2,3,4,...} & \B{সেলের কন্টেন্টের মধ্যে ফাঁক} \\\hline
\LAT{align} & \LAT{left,right,center} & \B{টেবিলের অবস্থান নির্ধারণ} \\\hline
\LAT{width/height} & \LAT{50px; 50\%} & \B{প্রশস্ততা/উচ্চতা নির্ধারণ} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{\LAT{<tr>} \B{এবং} \LAT{<td>/<th>} \B{অ্যাট্রিবিউট}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|>{\centering\arraybackslash}p{0.22\linewidth}|X|}
\hline
\rowcolor{tblhdr} \B{অ্যাট্রিবিউট} & \B{মান} & \B{ব্যবহার} \\\hline
\LAT{align} & \LAT{left,right,center} & \B{কন্টেন্টের অবস্থান নির্ধারণ} \\\hline
\LAT{bgcolor} & \LAT{rgb/\#xxxxxx} & \B{ব্যাকগ্রাউন্ড কালার সেট} \\\hline
\LAT{width/height} & \LAT{50px; 50\%} & \B{প্রশস্ততা/উচ্চতা নির্ধারণ} \\\hline
\LAT{rowspan} & \LAT{2,3,4,...} & \B{একটি সেল কয়টি সারি মার্জ করবে} \\\hline
\LAT{colspan} & \LAT{2,3,4,...} & \B{একটি সেল কয়টি কলাম মার্জ করবে} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{\B{কম্পিউটার আউটপুট ট্যাগ}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|}
\hline
\rowcolor{tblhdr} \B{ট্যাগ} & \B{কাজ} \\\hline
\LAT{<code>} & \B{কম্পিউটার কোড লেখার মতো টেক্সট দেখায়} \\\hline
\LAT{<kbd>} & \B{কীবোর্ড টেক্সট নির্ধারণে ব্যবহৃত} \\\hline
\LAT{<samp>} & \B{স্যাম্পল কম্পিউটার কোডের মতো টেক্সট} \\\hline
\LAT{<tt>} & \B{টেলিটাইপ টেক্সট প্রদর্শন করে} \\\hline
\LAT{<var>} & \B{ভেরিয়েবল নির্ধারণে ব্যবহৃত} \\\hline
\LAT{<pre>} & \B{প্রিফরম্যাটেড টেক্সট: স্পেস ও লাইন ব্রেক অনুসারে} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{\B{সাইটেশন, কোটেশন ও ডেফিনিশন ট্যাগ}}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|}
\hline
\rowcolor{tblhdr} \B{ট্যাগ} & \B{কাজ} \\\hline
\LAT{<abbr>} & \B{আব্রিভিয়েশন নির্ধারণে; মাউস রাখলে পূর্ণ অর্থ} \\\hline
\LAT{<acronym>} & \B{অ্যাক্রোনিম নির্ধারণে ব্যবহৃত} \\\hline
\LAT{<address>} & \B{ঠিকানা এলিমেন্ট; ইটালিক স্টাইলে দেখায়} \\\hline
\LAT{<bdo>} & \B{টেক্সটের ডিরেকশন নির্ধারণ} \\\hline
\LAT{<blockquote>} & \B{দীর্ঘ কোটেশন দিতে ব্যবহৃত} \\\hline
\LAT{<q>} & \B{সংক্ষিপ্ত কোটেশন দিতে ব্যবহৃত} \\\hline
\LAT{<cite>} & \B{সাইটেশন প্রদানে ব্যবহৃত} \\\hline
\LAT{<dfn>} & \B{ডেফিনিশন টার্ম নির্ধারণ করতে} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\noindent\scriptsize\textbf{\B{হেডিং ট্যাগ:}} \LAT{<h1>} \B{থেকে} \LAT{<h6>}\B{; ডকুমেন্ট:} \LAT{<html>, <head>, <title>, <body>, <p>, <br>, <hr>, <a href>, <img>, <div>, <span>}
\normalsize

\chsec{১৫. প্রোগ্রামিং ল্যাঙ্গুয়েজের ক্রম বিকাশের ধারা}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{multicols}{2}
\begin{tabular}{|c|l|}
\hline
\rowcolor{tblhdr} \B{সাল} & \B{ল্যাঙ্গুয়েজ} \\\hline
\LAT{1945} & \LAT{Machine language} \\\hline
\LAT{1950} & \LAT{EDSAC assembly} \\\hline
\LAT{1957} & \LAT{FORTRAN} \\\hline
\LAT{1958} & \LAT{ALGOL-58, LISP} \\\hline
\LAT{1960} & \LAT{COBOL} \\\hline
\LAT{1964} & \LAT{RPG, PL/I, BASIC} \\\hline
\LAT{1967} & \LAT{Logo} \\\hline
\LAT{1968} & \LAT{APL} \\\hline
\LAT{1970} & \LAT{Pascal, Smalltalk} \\\hline
\LAT{1971} & \LAT{FORTH} \\\hline
\end{tabular}
\columnbreak
\begin{tabular}{|c|l|}
\hline
\rowcolor{tblhdr} \B{সাল} & \B{ল্যাঙ্গুয়েজ} \\\hline
\LAT{1972} & \LAT{C, PROLOG, Simula} \\\hline
\LAT{1980} & \LAT{Ada} \\\hline
\LAT{1981} & \LAT{Modula-2} \\\hline
\LAT{1982} & \LAT{dBase} \\\hline
\LAT{1983} & \LAT{C++} \\\hline
\LAT{1984} & \LAT{Turbo Pascal} \\\hline
\LAT{1987} & \LAT{HyperCard} \\\hline
\LAT{1991} & \LAT{Python} \\\hline
\LAT{1995} & \LAT{Java} \\\hline
\LAT{2000} & \LAT{C\#} \\\hline
\end{tabular}
\end{multicols}
\setlength{\tabcolsep}{1.4pt}
\normalsize
\itm{1} \B{প্রজন্ম:} \LAT{1GL} \B{মেশিন,} \LAT{2GL} \B{অ্যাসেম্বলি,} \LAT{3GL} \B{প্রসিজারাল (C,Pascal),} \LAT{4GL} \B{নন-প্রসিজারাল (SQL),} \LAT{5GL} \B{প্রাকৃতিক/AI}
\itm{2} \B{কম্পাইলার:} \B{পুরো প্রোগ্রাম একসাথে মেশিন ভাষায় রূপান্তর করে}
\itm{3} \B{ইন্টারপ্রেটার:} \B{লাইন ধরে ধরে রূপান্তর ও নির্বাহ করে}
\itm{4} \B{অ্যাসেম্বলার:} \B{অ্যাসেম্বলি ভাষা মেশিন কোডে রূপান্তর করে}

\chsec{১৬. প্রোগ্রাম ফ্লোচার্টে ব্যবহৃত প্রতীক}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|c|l|X|}
\hline
\rowcolor{tblhdr} \B{প্রতীক} & \B{নাম} & \B{বর্ণনা} \\\hline
\begin{tikzpicture}[baseline=-2pt]\draw[rounded corners=4pt,thick] (0,-0.18) rectangle (1.0,0.18);\end{tikzpicture}
& \LAT{Terminal} & \B{গোলাকার আয়তক্ষেত্র। প্রোগ্রামের শুরু ও শেষ।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0,-0.18)--(0.14,0.18)--(0.95,0.18)--(0.81,-0.18)--cycle;\end{tikzpicture}
& \LAT{Input/Output} & \B{সামান্তরিক আকৃতি। ইনপুট ও আউটপুট প্রদর্শনে।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0,-0.18) rectangle (1.0,0.18);\end{tikzpicture}
& \LAT{Process} & \B{আয়তাকার আকৃতি। প্রক্রিয়াকরণ প্রতীক।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0.48,0.0)--(0.24,0.22)--(0,0.0)--(0.24,-0.22)--cycle;\end{tikzpicture}
& \LAT{Decision} & \B{হীরক আকৃতি। সিদ্ধান্ত প্রতীক। হ্যাঁ/না দুটি উত্তর।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw[->] (0,0.18)--(0,-0.18);\draw[->](0.35,0)--(0.75,0);\end{tikzpicture}
& \LAT{Flowline} & \B{তীর চিহ্নযুক্ত রেখা। প্রোগ্রামের পথ নির্দেশ করে।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0.22,0) circle (0.18);\end{tikzpicture}
& \LAT{Connector} & \B{বৃত্তাকার প্রতীক। বড় ফ্লোচার্টে সংযোগ নির্দেশে।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0,0)--(0.16,0.18)--(0.64,0.18)--(0.80,0)--(0.64,-0.18)--(0.16,-0.18)--cycle;\end{tikzpicture}
& \LAT{Loop} & \B{ষড়ভুজ আকৃতি। লুপ বা চক্রের কাজ প্রদর্শনে।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0,-0.18) rectangle (1.0,0.18); \draw (0.12,-0.18)--(0.12,0.18); \draw (0.88,-0.18)--(0.88,0.18);\end{tikzpicture}
& \LAT{Subroutine} & \B{মূল প্রোগ্রামের সাবরুটিন বা পূর্বনির্ধারিত প্রক্রিয়া।} \\\hline
\begin{tikzpicture}[baseline=-2pt,thick]\draw (0,-0.12) rectangle (1.0,0.12); \draw[dashed] (0.0,-0.24) -- (1.0,-0.24);\end{tikzpicture}
& \LAT{Description} & \B{টীকা প্রতীক। ফ্লোচার্টের অংশ বর্ণনার জন্য।} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{১৭. ডেটাবেজ রিলেশন}
\noindent\scriptsize
\itm{1} \B{One-to-One:} \B{একজন কর্মকর্তা একটি ডিপার্টমেন্ট ম্যানেজ করেন}

\noindent
\begin{tikzpicture}[baseline=-2pt,scale=0.86,every node/.style={font=\tiny}]
\draw[thick] (0,0) rectangle (1.1,0.5); \node at (0.55,0.25) {Employee};
\draw[thick] (1.55,0.25)--(2.20,0.62)--(2.85,0.25)--(2.20,-0.12)--cycle; \node at (2.20,0.25) {Manage};
\draw[thick] (3.30,0) rectangle (4.45,0.5); \node at (3.87,0.25) {Department};
\draw[thick] (1.1,0.25)--(1.55,0.25); \draw[thick] (2.85,0.25)--(3.30,0.25);
\node[above] at (1.30,0.25) {1}; \node[above] at (3.10,0.25) {1};
\end{tikzpicture}

\itm{2} \B{One-to-Many:} \B{একজন প্রকাশক অনেকগুলো বই প্রকাশ করেন}

\noindent
\begin{tikzpicture}[baseline=-2pt,scale=0.86,every node/.style={font=\tiny}]
\draw[thick] (0,0) rectangle (1.1,0.5); \node at (0.55,0.25) {Publisher};
\draw[thick] (1.55,0.25)--(2.20,0.62)--(2.85,0.25)--(2.20,-0.12)--cycle; \node at (2.20,0.25) {Supplies};
\draw[thick] (3.30,0) rectangle (4.30,0.5); \node at (3.80,0.25) {Book};
\draw[thick] (1.1,0.25)--(1.55,0.25); \draw[thick] (2.85,0.25)--(3.30,0.25);
\node[above] at (1.30,0.25) {1}; \node[above] at (3.10,0.25) {N};
\end{tikzpicture}

\itm{3} \B{Many-to-One:} \B{অনেকগুলো বই একটি বিভাগে অন্তর্ভুক্ত}

\noindent
\begin{tikzpicture}[baseline=-2pt,scale=0.86,every node/.style={font=\tiny}]
\draw[thick] (0,0) rectangle (1.0,0.5); \node at (0.5,0.25) {Book};
\draw[thick] (1.45,0.25)--(2.05,0.62)--(2.65,0.25)--(2.05,-0.12)--cycle; \node at (2.05,0.25) {Has};
\draw[thick] (3.10,0) rectangle (4.20,0.5); \node at (3.65,0.25) {Section};
\draw[thick] (1.0,0.25)--(1.45,0.25); \draw[thick] (2.65,0.25)--(3.10,0.25);
\node[above] at (1.22,0.25) {N}; \node[above] at (2.88,0.25) {1};
\end{tikzpicture}

\itm{4} \B{Many-to-Many:} \B{বহু কোর্সে বহু ছাত্র ভর্তি হতে পারে}

\noindent
\begin{tikzpicture}[baseline=-2pt,scale=0.86,every node/.style={font=\tiny}]
\draw[thick] (0,0) rectangle (1.1,0.5); \node at (0.55,0.25) {Course};
\draw[thick] (1.55,0.25)--(2.20,0.62)--(2.85,0.25)--(2.20,-0.12)--cycle; \node at (2.20,0.25) {Enroll};
\draw[thick] (3.30,0) rectangle (4.40,0.5); \node at (3.85,0.25) {Student};
\draw[thick] (1.1,0.25)--(1.55,0.25); \draw[thick] (2.85,0.25)--(3.30,0.25);
\node[above] at (1.30,0.25) {N}; \node[above] at (3.10,0.25) {N};
\end{tikzpicture}
\normalsize

\chsec{১৮. বহুল ব্যবহৃত SQL Commands}
\noindent\scriptsize
\setlength{\tabcolsep}{1.0pt}
\begin{tabularx}{\linewidth}{|l|X|}
\hline
\rowcolor{tblhdr} \LAT{Command} & \B{ব্যবহার} \\\hline
\LAT{CREATE} & \B{নতুন টেবিল/ডেটাবেজ তৈরি করতে ব্যবহৃত হয়} \\\hline
\LAT{SELECT} & \B{কোনো নির্দিষ্ট রেকর্ড নির্বাচন করতে} \\\hline
\LAT{UPDATE} & \B{রেকর্ড মডিফাই বা হালনাগাদ করতে} \\\hline
\LAT{DELETE} & \B{কোনো রেকর্ড মুছে ফেলতে ব্যবহৃত হয়} \\\hline
\LAT{DROP} & \B{টেবিল বা ডেটাবেজ মুছে ফেলতে} \\\hline
\LAT{INSERT} & \B{নতুন সারি সংযোজন করতে ব্যবহৃত} \\\hline
\LAT{ALTER} & \B{টেবিলে কলাম যুক্ত বা মুছতে} \\\hline
\LAT{WHERE} & \B{শর্ত নির্বাচন করতে ব্যবহৃত হয়} \\\hline
\LAT{FROM} & \B{সঠিক টেবিল নির্দেশনায় ব্যবহৃত} \\\hline
\LAT{IS NULL} & \B{শুধু নাল ভ্যালুর সারি রিটার্ন করতে} \\\hline
\LAT{COUNT} & \B{সারি সংখ্যা গণনা করতে ব্যবহৃত} \\\hline
\LAT{ORDER BY} & \B{ডেটা ক্রমানুসারে সাজাতে} \\\hline
\LAT{GROUP BY} & \B{নির্দিষ্ট কলাম অনুযায়ী ডেটা গ্রুপ করতে} \\\hline
\LAT{HAVING} & \LAT{GROUP BY} \B{এর পরে শর্ত দিতে ব্যবহৃত} \\\hline
\LAT{JOIN} & \B{একাধিক টেবিল যুক্ত করে ডেটা নির্বাচন} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize
\itm{1} \B{DDL:} \LAT{CREATE, ALTER, DROP, TRUNCATE}
\itm{2} \B{DML:} \LAT{SELECT, INSERT, UPDATE, DELETE}
\itm{3} \B{DCL:} \LAT{GRANT, REVOKE}
\itm{4} \B{TCL:} \LAT{COMMIT, ROLLBACK, SAVEPOINT}

\chsec{১৯. সাইবার নিরাপত্তা ও ক্রিপ্টোগ্রাফি}
\itm{1} \B{ফায়ারওয়াল:} \B{নেটওয়ার্কে অননুমোদিত প্রবেশাধিকার নিয়ন্ত্রণ করে}
\itm{2} \B{এনক্রিপশন:} \B{ডেটা অপাঠ্য সাংকেতিক আকারে রূপান্তর} \LAT{(Plaintext$\to$Ciphertext)}
\itm{3} \B{ডিক্রিপশন:} \B{সাংকেতিক ডেটা পুনরায় পাঠযোগ্য আকারে রূপান্তর}
\itm{4} \B{ক্রিপ্টোগ্রাফি প্রকার:} \B{সিমেট্রিক} \LAT{(AES, DES)}\B{; অ্যাসিমেট্রিক} \LAT{(RSA)}
\itm{5} \B{ভাইরাস:} \B{স্বপ্রতিলিপিকারী ক্ষতিকর প্রোগ্রাম}
\itm{6} \B{ওয়ার্ম:} \B{নেটওয়ার্কে ছড়িয়ে পড়া ক্ষতিকর প্রোগ্রাম}
\itm{7} \B{ট্রোজান:} \B{দরকারী প্রোগ্রামের ছদ্মবেশে ক্ষতিকর কোড}
\itm{8} \B{স্পাইওয়্যার:} \B{ব্যবহারকারীর তথ্য গোপনে সংগ্রহকারী প্রোগ্রাম}
\itm{9} \B{হ্যাকিং:} \B{অননুমোদিতভাবে কম্পিউটার সিস্টেমে প্রবেশ}
\itm{10} \B{ফিশিং:} \B{প্রতারণামূলক ই-মেইলে ব্যক্তিগত তথ্য চুরি}

\chsec{২০. ক্লাউড কম্পিউটিং ও আধুনিক প্রযুক্তি}
\itm{1} \B{ক্লাউড কম্পিউটিং:} \B{ইন্টারনেটের মাধ্যমে কম্পিউটিং সম্পদ প্রদান}
\itm{2} \B{IaaS:} \B{Infrastructure as a Service} \LAT{(AWS EC2)}
\itm{3} \B{PaaS:} \B{Platform as a Service} \LAT{(Google App Engine)}
\itm{4} \B{SaaS:} \B{Software as a Service} \LAT{(Gmail, Google Docs)}
\itm{5} \B{IoT:} \B{ইন্টারনেটে সংযুক্ত স্মার্ট ডিভাইসের নেটওয়ার্ক}
\itm{6} \B{বিগ ডেটা:} \B{৩V:} \LAT{Volume, Velocity, Variety}
\itm{7} \B{আর্টিফিশিয়াল ইন্টেলিজেন্স:} \B{মানুষের বুদ্ধিমত্তা অনুকরণে কম্পিউটার প্রোগ্রাম}
\itm{8} \B{মেশিন লার্নিং:} \B{AI-এর শাখা; ডেটা থেকে শিখে সিদ্ধান্ত নেয়}
\itm{9} \B{ব্লকচেইন:} \B{বিতরণকৃত অপরিবর্তনীয় লেজার প্রযুক্তি}
\itm{10} \B{৫G:} \B{উচ্চগতির মোবাইল নেটওয়ার্ক; ১--১০ Gbps পর্যন্ত}

\chsec{২১. ICT মূল সংজ্ঞা ও পরিসংখ্যান}
\itm{1} \B{ICT:} \B{তথ্য সংগ্রহ, সংরক্ষণ, প্রক্রিয়াকরণ ও আদান-প্রদানে ব্যবহৃত প্রযুক্তি}
\itm{2} \B{তথ্য:} \B{প্রক্রিয়াজাত উপাত্ত যা অর্থবহ এবং সিদ্ধান্ত গ্রহণে সহায়ক}
\itm{3} \B{ডেটা:} \B{কাঁচা তথ্য বা ঘটনা যা এখনও প্রক্রিয়াকৃত নয়}
\itm{4} \B{বিশ্বগ্রাম:} \B{প্রযুক্তির মাধ্যমে বিশ্ব এক গ্রামে রূপান্তর; ম্যাকলুহান (১৯৬২)}
\itm{5} \B{ক্লাউড কম্পিউটিং:} \B{ইন্টারনেটের মাধ্যমে কম্পিউটিং সেবা} \LAT{(IaaS, PaaS, SaaS)}
\itm{6} \B{ক্রায়োসার্জারি:} \B{চরম নিম্নতাপে অস্ত্রোপচার} \LAT{($-196^\circ$C)}
\itm{7} \B{বায়োমেট্রিক:} \B{দৈহিক বৈশিষ্ট্য দ্বারা পরিচয়: আঙ্গুলের ছাপ, আইরিস, কণ্ঠস্বর}
\itm{8} \B{IoT:} \B{ইন্টারনেট সংযুক্ত স্মার্ট ডিভাইসের নেটওয়ার্ক}
\itm{9} \B{ন্যানো প্রযুক্তি:} \B{১--১০০ ন্যানোমিটার স্কেলে পদার্থ নিয়ন্ত্রণ} \LAT{(1 nm $=10^{-9}$ m)}
\itm{10} \B{ভার্চুয়াল রিয়ালিটি:} \B{কম্পিউটার দ্বারা তৈরি কৃত্রিম পরিবেশ যা বাস্তব মনে হয়}
\itm{11} \B{রোবটিক্স:} \B{রোবট ডিজাইন, নির্মাণ ও পরিচালনার বিজ্ঞান ও প্রযুক্তি}
\itm{12} \B{বায়োইনফরমেটিক্স:} \B{জীববিজ্ঞান সমস্যা সমাধানে কম্পিউটার বিজ্ঞানের প্রয়োগ}
\itm{13} \B{জেনেটিক ইঞ্জিনিয়ারিং:} \B{DNA পরিবর্তন করে নতুন বৈশিষ্ট্য সৃষ্টি}
\itm{14} \B{বায়োটেকনোলজি:} \B{জীবন্ত প্রাণীর ব্যবহার করে পণ্য বা প্রযুক্তি উৎপাদন}
\itm{15} \B{ক্রায়োনিক্স:} \B{মৃতদেহ বা টিস্যু অতি নিম্ন তাপমাত্রায় সংরক্ষণ}
\itm{16} \B{টেলিমেডিসিন:} \B{প্রযুক্তির সাহায্যে দূরবর্তী স্থান থেকে চিকিৎসা সেবা}
\itm{17} \B{ই-কমার্স:} \B{ইন্টারনেটের মাধ্যমে পণ্য ও সেবা ক্রয়-বিক্রয়}
\itm{18} \B{ই-গভর্ন্যান্স:} \B{ইলেকট্রনিক পদ্ধতিতে সরকারি সেবা প্রদান}
\itm{19} \B{স্মার্ট হোম:} \LAT{IoT} \B{দ্বারা নিয়ন্ত্রিত ঘরোয়া ডিভাইস সমূহ}
\itm{20} \B{অগমেন্টেড রিয়ালিটি:} \B{বাস্তব পরিবেশে ডিজিটাল তথ্য যোগ করে দেখায়}

\end{multicols}

\vspace{4pt}
\chsecfull{অধ্যায় ৩ (সংখ্যা পদ্ধতি) — বিস্তারিত নোট ও চার্ট}
\vspace{2pt}

\begin{multicols}{2}
\chsub{}{সংখ্যা পদ্ধতির প্রকারভেদ ও মৌলিক ধারণা}
\itm{1} \B{পজিশনাল (Positional):} \B{প্রতিটি অঙ্কের মান তার অবস্থানের উপর নির্ভর করে।} \B{যেমন—} \LAT{Decimal, Binary, Octal, Hexadecimal}
\itm{2} \B{নন-পজিশনাল (Non-Positional):} \B{অঙ্কের অবস্থান মান পরিবর্তন করে না।} \B{যেমন—} \B{রোমান সংখ্যা} \LAT{(I, V, X, L, C, D, M)}
\itm{3} \B{র‍্যাডিক্স পয়েন্ট (Radix Point):} \B{পূর্ণ ও ভগ্নাংশ অংশের মাঝের বিন্দু} \LAT{(.)}
\itm{4} \B{MSD (Most Significant Digit):} \B{সবচেয়ে বাম দিকের অঙ্ক — সর্বোচ্চ মান বহন করে।}
\itm{5} \B{LSD (Least Significant Digit):} \B{সবচেয়ে ডান দিকের অঙ্ক — সর্বনিম্ন মান বহন করে।}
\itm{6} \B{বিট (Bit):} \B{Binary Digit;} \LAT{0} \B{বা} \LAT{1} \B{— ক্ষুদ্রতম একক।}
\itm{7} \B{বাইট (Byte):} \LAT{8} \B{বিটের সমষ্টি;} \LAT{1} \B{ক্যারেক্টার সংরক্ষণ করে।}
\itm{8} \B{যেকোনো বেজ:} \B{একটি সংখ্যাকে যেকোনো} \LAT{base} \B{এ রূপান্তর করা যায়।}

\chsub{}{ভিন্ন সংখ্যা পদ্ধতির ভিন্ন ভিত্তি}
\noindent\scriptsize\setlength{\tabcolsep}{1.4pt}
\begin{tabular}{|l|c|l|}
\hline
\rowcolor{tblhdr}\B{পদ্ধতি} & \B{ভিত্তি} & \B{অঙ্কসমূহ} \\\hline
\B{ডেসিমাল (Decimal)} & \LAT{10} & \LAT{0--9} \\\hline
\B{বাইনারি (Binary)} & \LAT{2} & \LAT{0, 1} \\\hline
\B{অক্টাল (Octal)} & \LAT{8} & \LAT{0--7} \\\hline
\B{হেক্সাডেসিমাল} & \LAT{16} & \LAT{0--9, A--F} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}\normalsize

\chsub{}{বাইনারি যোগ ও বিয়োগ}
\itm{1} \B{যোগ:} \LAT{$0{+}0{=}0$}\B{;} \LAT{$0{+}1{=}1$}\B{;} \LAT{$1{+}0{=}1$}\B{;} \LAT{$1{+}1{=}10$} \B{(ক্যারি} \LAT{1}\B{)}
\itm{2} \B{বিয়োগ:} \LAT{$0{-}0{=}0$}\B{;} \LAT{$1{-}0{=}1$}\B{;} \LAT{$1{-}1{=}0$}\B{;} \LAT{$0{-}1{=}1$} \B{(ধার} \LAT{1}\B{)}
\itm{3} \LAT{$1$} \B{এর পরিপূরক গঠন:} \B{প্রতিটি বিট উল্টানো} \LAT{($0\leftrightarrow1$)}
\itm{4} \LAT{$2$} \B{এর পরিপূরক গঠন:} \LAT{1}\B{-এর পরিপূরক} \LAT{$+\,1$}

\chsub{}{সংখ্যা পদ্ধতির রূপান্তরসমূহ}
\itm{1} \B{ডেসিমাল} \LAT{$\to$} \B{বাইনারি} \LAT{(D$\to$B)}
\itm{2} \B{বাইনারি} \LAT{$\to$} \B{ডেসিমাল} \LAT{(B$\to$D)}
\itm{3} \B{ডেসিমাল} \LAT{$\to$} \B{অক্টাল} \LAT{(D$\to$O)}
\itm{4} \B{অক্টাল} \LAT{$\to$} \B{ডেসিমাল} \LAT{(O$\to$D)}
\itm{5} \B{অক্টাল} \LAT{$\to$} \B{বাইনারি} \LAT{(O$\to$B)}
\itm{6} \B{বাইনারি} \LAT{$\to$} \B{অক্টাল} \LAT{(B$\to$O)}
\itm{7} \B{হেক্সাডেসিমাল} \LAT{$\to$} \B{ডেসিমাল} \LAT{(H$\to$D)}
\itm{8} \B{ডেসিমাল} \LAT{$\to$} \B{হেক্সাডেসিমাল} \LAT{(D$\to$H)}
\itm{9} \B{হেক্সাডেসিমাল} \LAT{$\to$} \B{বাইনারি} \LAT{(H$\to$B)}
\itm{10} \B{বাইনারি} \LAT{$\to$} \B{হেক্সাডেসিমাল} \LAT{(B$\to$H)}
\itm{11} \B{অক্টাল} \LAT{$\to$} \B{হেক্সাডেসিমাল} \LAT{(O$\to$H)}
\itm{12} \B{হেক্সাডেসিমাল} \LAT{$\to$} \B{অক্টাল} \LAT{(H$\to$O)}

\end{multicols}

\vspace{2pt}
\chsecfull{এক নজরে সংখ্যা পদ্ধতির রূপান্তর (নিয়ম, পূর্ণাংশ, ভগ্নাংশ ও ফলাফল)}
\vspace{2pt}
\noindent\scriptsize
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|p{0.10\textwidth}|p{0.32\textwidth}|p{0.20\textwidth}|p{0.18\textwidth}|p{0.13\textwidth}|}
\hline
\rowcolor{tblhdr}\B{রূপান্তর} & \B{নিয়ম} & \B{পূর্ণাংশ উদাহরণ} & \B{ভগ্নাংশ উদাহরণ} & \B{ফলাফল} \\\hline
\B{D--B} \LAT{(38.05)$_{10}$} & \B{পূর্ণাংশকে} \LAT{2} \B{দ্বারা ভাগ; ভগ্নাংশকে} \LAT{2} \B{দ্বারা গুণ করে পূর্ণ অংশ সংগ্রহ।} & \LAT{38$\div$2: 19,9,4,2,1,0 (R:0,1,0,0,1)} & \LAT{.05$\times$2$=$.10,.20,.40,.80,1.60} & \LAT{(100110.00001\ldots)$_2$} \\\hline
\B{D--O} \LAT{(175.15)$_{10}$} & \B{পূর্ণাংশকে} \LAT{8} \B{দ্বারা ভাগ; ভগ্নাংশকে} \LAT{8} \B{দ্বারা গুণ।} & \LAT{175$\div$8: 21,2,0 (R:7,5,2)} & \LAT{.15$\times$8$=$1.20; .20$\times$8$=$1.60\ldots} & \LAT{(257.11463\ldots)$_8$} \\\hline
\B{D--H} \LAT{(2479.50)$_{10}$} & \B{পূর্ণাংশকে} \LAT{16} \B{দ্বারা ভাগ; ভগ্নাংশকে} \LAT{16} \B{দ্বারা গুণ।} & \LAT{2479$\div$16: 154,9,0 (R:F,A,9)} & \LAT{.50$\times$16$=$8.0} & \LAT{(9AF.8)$_{16}$} \\\hline
\B{B--D} \LAT{(11110.001)$_2$} & \B{স্থানীয় মান} \LAT{2} \B{এর ঘাত দিয়ে যোগ;} \LAT{$2^0,2^1,\ldots$} \B{এবং ভগ্নাংশে} \LAT{$2^{-1},2^{-2}\ldots$} & \LAT{$1{\cdot}2^4{+}1{\cdot}2^3{+}1{\cdot}2^2{+}1{\cdot}2^1{=}30$} & \LAT{$0{\cdot}2^{-1}{+}0{\cdot}2^{-2}{+}1{\cdot}2^{-3}{=}.125$} & \LAT{(30.125)$_{10}$} \\\hline
\B{O--D} \LAT{(206.64)$_8$} & \B{স্থানীয় মান} \LAT{8} \B{এর ঘাত দিয়ে হিসাব।} & \LAT{$2{\cdot}8^2{+}0{\cdot}8^1{+}6{\cdot}8^0{=}134$} & \LAT{$6{\cdot}8^{-1}{+}4{\cdot}8^{-2}{=}.8125$} & \LAT{(134.8125)$_{10}$} \\\hline
\B{H--D} \LAT{(9AF.8)$_{16}$} & \B{স্থানীয় মান} \LAT{16} \B{এর ঘাত দিয়ে হিসাব।} & \LAT{$9{\cdot}16^2{+}10{\cdot}16^1{+}15{\cdot}16^0{=}2479$} & \LAT{$8{\cdot}16^{-1}{=}0.50$} & \LAT{(2479.50)$_{10}$} \\\hline
\B{B--O} \LAT{(110101)$_2$} & \B{পূর্ণাংশের জন্য ডান থেকে বাম, ভগ্নাংশের জন্য বাম থেকে ডান, প্রতি} \LAT{3} \B{বিট গ্রুপ।} & \LAT{110\,101 $=$ (65)$_8$} & \LAT{.010\,110 $=$ (.26)$_8$} & \LAT{(65)$_8$ / (.26)$_8$} \\\hline
\B{B--H} \LAT{(1010110)$_2$} & \B{প্রতি} \LAT{4} \B{বিট গ্রুপ; পূর্ণাংশ ডান থেকে, ভগ্নাংশ বাম থেকে।} & \LAT{0101\,0110 $=$ (56)$_{16}$} & \LAT{.0101\,1100 $=$ (.5C)$_{16}$} & \LAT{(56)$_{16}$ / (.5C)$_{16}$} \\\hline
\B{O--B} \LAT{(527.06)$_8$} & \B{প্রতিটি অক্টাল ডিজিটকে সমতুল্য} \LAT{3} \B{বিট বাইনারিতে লেখা।} & \LAT{5$=$101, 2$=$010, 7$=$111} & \LAT{0$=$000, 6$=$110} & \LAT{(101010111.000110)$_2$} \\\hline
\B{H--B} \LAT{(A09.E2)$_{16}$} & \B{প্রতিটি হেক্স ডিজিটকে সমতুল্য} \LAT{4} \B{বিট বাইনারিতে লেখা।} & \LAT{A$=$1010, 0$=$0000, 9$=$1001} & \LAT{E$=$1110, 2$=$0010} & \LAT{(101000001001.11100010)$_2$} \\\hline
\B{O--H} \LAT{(527.375)$_8$} & \B{প্রথমে অক্টাল} \LAT{$\to$} \B{বাইনারি; এরপর বাইনারি} \LAT{$\to$} \B{হেক্স।} & \LAT{527$=$101010111$\to$157} & \LAT{.375$=$011111101$\to$.7E8} & \LAT{(157.7E8)$_{16}$} \\\hline
\B{H--O} \LAT{(207.54)$_{16}$} & \B{প্রথমে হেক্স} \LAT{$\to$} \B{বাইনারি; এরপর বাইনারি} \LAT{$\to$} \B{অক্টাল।} & \LAT{207$=$001000000111$\to$1007} & \LAT{.54$=$01010100$\to$.250} & \LAT{(1007.250)$_8$} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\vspace{4pt}
\chsecfull{এক নজরে সংখ্যা পদ্ধতির তুলনা (Decimal, Binary, Octal, Hexadecimal)}
\vspace{2pt}
\noindent\scriptsize
\setlength{\tabcolsep}{3pt}
\renewcommand{\arraystretch}{1.15}
\begin{tabular}{|p{0.18\textwidth}|p{0.19\textwidth}|p{0.19\textwidth}|p{0.19\textwidth}|p{0.19\textwidth}|}
\hline
\rowcolor{tblhdr}\B{বিষয়} & \B{ডেসিমাল} \LAT{(Decimal)} & \B{বাইনারি} \LAT{(Binary)} & \B{অক্টাল} \LAT{(Octal)} & \B{হেক্সাডেসিমাল} \\\hline
\B{ভিত্তি} \LAT{(Base)} & \LAT{10} & \LAT{2} & \LAT{8} & \LAT{16} \\\hline
\B{অঙ্কের সংখ্যা} & \LAT{0--9} & \LAT{0, 1} & \LAT{0--7} & \LAT{0--9, A--F} \\\hline
\B{মানুষের ব্যবহারে} & \B{হ্যাঁ} & \B{না (কম্পিউটারে)} & \B{না (বিশেষ প্রয়োজনে)} & \B{না (কম্পিউটারে)} \\\hline
\B{কম্পিউটারে ব্যবহার} & \B{না} & \B{হ্যাঁ} & \B{হ্যাঁ} & \B{হ্যাঁ} \\\hline
\B{উদাহরণ} & \LAT{275} & \LAT{10001011} & \LAT{425} & \LAT{1A3} \\\hline
\B{প্রতিটি অঙ্কের মান নির্ধারণ} & \B{অবস্থানভিত্তিক} & \B{অবস্থানভিত্তিক} & \B{অবস্থানভিত্তিক} & \B{অবস্থানভিত্তিক} \\\hline
\B{বেসের শক্তি অনুযায়ী মান} & \LAT{$2{\cdot}10^2{+}7{\cdot}10^1{+}5{\cdot}10^0$} & \LAT{$1{\cdot}2^7{+}0{\cdot}2^6{+}\ldots{+}1{\cdot}2^0$} & \LAT{$4{\cdot}8^2{+}2{\cdot}8^1{+}5{\cdot}8^0$} & \LAT{$1{\cdot}16^2{+}A{\cdot}16^1{+}3{\cdot}16^0$} \\\hline
\B{রূপান্তরের প্রয়োগ} & \B{সহজ} & \B{প্রোগ্রামিং ও ডিজিটাল সার্কিটে} & \B{কম্পিউটার কোডে} & \B{মেমরি ঠিকানা, কালার কোড} \\\hline
\B{ব্যবহার} & \B{দৈনন্দিন গাণিতিক কাজে} & \B{কম্পিউটারে সব তথ্য} \LAT{0,\,1} \B{দ্বারা প্রকাশ} & \B{কিছু পুরাতন কম্পিউটার সিস্টেমে} & \B{মেমরি অ্যাড্রেস, রঙ} \LAT{(Color Codes)}\B{, মেশিন লেভেল প্রোগ্রামিং} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\vspace{4pt}
\chsecfull{ডেসিমাল-বাইনারি-অক্টাল-হেক্স রূপান্তর তালিকা (০--৩৩)}
\vspace{2pt}
\begin{multicols}{2}
\noindent\scriptsize\setlength{\tabcolsep}{3pt}
\begin{tabular}{|c|c|c|c|}
\hline
\rowcolor{tblhdr}\B{দশমিক} & \B{বাইনারি} & \B{অক্টাল} & \B{হেক্স} \\\hline
\LAT{0} & \LAT{0} & \LAT{0} & \LAT{0} \\\hline
\LAT{1} & \LAT{1} & \LAT{1} & \LAT{1} \\\hline
\LAT{2} & \LAT{10} & \LAT{2} & \LAT{2} \\\hline
\LAT{3} & \LAT{11} & \LAT{3} & \LAT{3} \\\hline
\LAT{4} & \LAT{100} & \LAT{4} & \LAT{4} \\\hline
\LAT{5} & \LAT{101} & \LAT{5} & \LAT{5} \\\hline
\LAT{6} & \LAT{110} & \LAT{6} & \LAT{6} \\\hline
\LAT{7} & \LAT{111} & \LAT{7} & \LAT{7} \\\hline
\LAT{8} & \LAT{1000} & \LAT{10} & \LAT{8} \\\hline
\LAT{9} & \LAT{1001} & \LAT{11} & \LAT{9} \\\hline
\LAT{10} & \LAT{1010} & \LAT{12} & \LAT{A} \\\hline
\LAT{11} & \LAT{1011} & \LAT{13} & \LAT{B} \\\hline
\LAT{12} & \LAT{1100} & \LAT{14} & \LAT{C} \\\hline
\LAT{13} & \LAT{1101} & \LAT{15} & \LAT{D} \\\hline
\LAT{14} & \LAT{1110} & \LAT{16} & \LAT{E} \\\hline
\LAT{15} & \LAT{1111} & \LAT{17} & \LAT{F} \\\hline
\LAT{16} & \LAT{10000} & \LAT{20} & \LAT{10} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}\normalsize

\columnbreak
\noindent\scriptsize\setlength{\tabcolsep}{3pt}
\begin{tabular}{|c|c|c|c|}
\hline
\rowcolor{tblhdr}\B{দশমিক} & \B{বাইনারি} & \B{অক্টাল} & \B{হেক্স} \\\hline
\LAT{17} & \LAT{10001} & \LAT{21} & \LAT{11} \\\hline
\LAT{18} & \LAT{10010} & \LAT{22} & \LAT{12} \\\hline
\LAT{19} & \LAT{10011} & \LAT{23} & \LAT{13} \\\hline
\LAT{20} & \LAT{10100} & \LAT{24} & \LAT{14} \\\hline
\LAT{21} & \LAT{10101} & \LAT{25} & \LAT{15} \\\hline
\LAT{22} & \LAT{10110} & \LAT{26} & \LAT{16} \\\hline
\LAT{23} & \LAT{10111} & \LAT{27} & \LAT{17} \\\hline
\LAT{24} & \LAT{11000} & \LAT{30} & \LAT{18} \\\hline
\LAT{25} & \LAT{11001} & \LAT{31} & \LAT{19} \\\hline
\LAT{26} & \LAT{11010} & \LAT{32} & \LAT{1A} \\\hline
\LAT{27} & \LAT{11011} & \LAT{33} & \LAT{1B} \\\hline
\LAT{28} & \LAT{11100} & \LAT{34} & \LAT{1C} \\\hline
\LAT{29} & \LAT{11101} & \LAT{35} & \LAT{1D} \\\hline
\LAT{30} & \LAT{11110} & \LAT{36} & \LAT{1E} \\\hline
\LAT{31} & \LAT{11111} & \LAT{37} & \LAT{1F} \\\hline
\LAT{32} & \LAT{100000} & \LAT{40} & \LAT{20} \\\hline
\LAT{33} & \LAT{100001} & \LAT{41} & \LAT{21} \\\hline
\end{tabular}
\setlength{\tabcolsep}{1.4pt}\normalsize
\end{multicols}

\bigskip\par\noindent\rule{\linewidth}{0.6pt}\par\bigskip

\begin{center}
\noindent{\bfseries\large\B{এইচটিএমএল (HTML) রেফারেন্স শিট}}\\[2pt]
{\small\B{রচনায়: Abir Arafat Chawdhury [Introvert's Area]}}
\end{center}
\vspace{2pt}

% ============================================================
% SECTION 1: TAG TYPES
% ============================================================
\chsecfull{১. HTML ট্যাগের ধরন — শূন্য ট্যাগ (Void) বনাম যুগল ট্যাগ (Paired)}

{\small\setlength{\tabcolsep}{3pt}
\noindent\begin{tabular}{|p{0.09\textwidth}|p{0.30\textwidth}|p{0.28\textwidth}|p{0.29\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{ধরন}} & \textbf{\B{বিবরণ}} & \textbf{\B{উদাহরণ}} & \textbf{\B{সকল শূন্য (Void) ট্যাগ}} \\
\hline
\rowcolor{tblalt}\LAT{Void / Self-Closing} & \B{কেবল শুরু ট্যাগ থাকে; শেষ ট্যাগ নেই।} \B{HTML5-এ} \LAT{/} \B{ছাড়াও লেখা যায়।} & \LAT{<br>, <img />,} \LAT{<input>, <hr>} & \LAT{area, base, br, col, embed, hr, img, input, link, meta, param, source, track, wbr} \\
\hline
\LAT{Paired} & \B{শুরু ট্যাগ} \LAT{(<tag>)} \B{ও শেষ ট্যাগ} \LAT{(</tag>)} \B{উভয়ই থাকে।} & \LAT{<p>...</p>,} \LAT{<div>...</div>} & \B{বাকি সব ট্যাগ (প্রায় ১০৬+)} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTIONS 2-4: DOCUMENT, SECTIONING, TEXT — 3-col
% ============================================================
\begin{multicols}{3}

\chsec{২. ডকুমেন্ট ও মেটাডেটা ট্যাগ}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}llp{3.2cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{V/P} & \textbf{\B{মূল অ্যাট্রিবিউট}} \\
\LAT{<html>} & P & \LAT{lang, dir, xmlns} \\
\rowcolor{tblalt}\LAT{<head>} & P & \B{(গ্লোবাল)} \\
\LAT{<title>} & P & \B{(গ্লোবাল)} \\
\rowcolor{tblalt}\LAT{<base>} & V & \LAT{href, target} \\
\LAT{<link>} & V & \LAT{rel, href, type, media, sizes,} \LAT{crossorigin, integrity, as,} \LAT{referrerpolicy, fetchpriority,} \LAT{disabled, hreflang} \\
\rowcolor{tblalt}\LAT{<meta>} & V & \LAT{name, content, charset,} \LAT{http-equiv, property} \\
\LAT{<style>} & P & \LAT{type, media, scoped} \\
\rowcolor{tblalt}\LAT{<body>} & P & \LAT{onload, onunload,} \LAT{onbeforeunload} \\
\end{tabular}}

{\tiny\B{V=Void, P=Paired}}

\chsub{২ক.}{\LAT{\texttt{<link>}} \B{rel মান}}
{\tiny\setlength{\tabcolsep}{1.5pt}
\noindent\begin{tabular}{@{}ll@{}}
\LAT{stylesheet} & \B{CSS ফাইল যুক্ত করে} \\
\rowcolor{tblalt}\LAT{icon} & \B{ফেভিকন} \\
\LAT{canonical} & \B{মূল URL নির্দেশ করে} \\
\rowcolor{tblalt}\LAT{alternate} & \B{বিকল্প সংস্করণ} \\
\LAT{preload} & \B{আগে লোড করে} \\
\rowcolor{tblalt}\LAT{prefetch} & \B{ভবিষ্যৎ পৃষ্ঠার রিসোর্স} \\
\LAT{preconnect} & \B{সংযোগ প্রস্তুত করে} \\
\rowcolor{tblalt}\LAT{dns-prefetch} & \B{DNS পূর্বনির্ধারণ} \\
\LAT{manifest} & \B{PWA ম্যানিফেস্ট} \\
\rowcolor{tblalt}\LAT{modulepreload} & \B{JS মডিউল প্রিলোড} \\
\LAT{author} & \B{লেখকের তথ্য} \\
\rowcolor{tblalt}\LAT{license} & \B{লাইসেন্স নথি} \\
\LAT{next / prev} & \B{পরের/আগের পৃষ্ঠা} \\
\rowcolor{tblalt}\LAT{nofollow} & \B{সার্চ ইঞ্জিন উপেক্ষা} \\
\LAT{noopener} & \B{নিরাপদ নতুন ট্যাব} \\
\rowcolor{tblalt}\LAT{noreferrer} & \B{Referrer লুকায়} \\
\LAT{search} & \B{অনুসন্ধান পৃষ্ঠা} \\
\rowcolor{tblalt}\LAT{help} & \B{সহায়তা পৃষ্ঠা} \\
\LAT{bookmark} & \B{বুকমার্ক} \\
\end{tabular}}

\chsub{২খ.}{\LAT{\texttt{<meta>}} \B{name মান}}
{\tiny\setlength{\tabcolsep}{1.5pt}
\noindent\begin{tabular}{@{}ll@{}}
\LAT{viewport} & \B{মোবাইল ভিউ নিয়ন্ত্রণ} \\
\rowcolor{tblalt}\LAT{description} & \B{পৃষ্ঠার সারসংক্ষেপ} \\
\LAT{keywords} & \B{কীওয়ার্ড তালিকা} \\
\rowcolor{tblalt}\LAT{author} & \B{লেখকের নাম} \\
\LAT{robots} & \B{সার্চ ইঞ্জিন নির্দেশ} \\
\rowcolor{tblalt}\LAT{generator} & \B{টুলের নাম} \\
\LAT{theme-color} & \B{ব্রাউজার থিম রঙ} \\
\rowcolor{tblalt}\LAT{color-scheme} & \B{হালকা/গাঢ় থিম} \\
\LAT{referrer} & \B{Referrer নীতি} \\
\rowcolor{tblalt}\LAT{application-name} & \B{অ্যাপের নাম} \\
\end{tabular}}

\columnbreak

\chsec{৩. সেকশন ও কাঠামো ট্যাগ}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{4.0cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{\B{বিবরণ ও অ্যাট্রিবিউট}} \\
\LAT{<header>} & \B{পৃষ্ঠার বা সেকশনের শীর্ষাংশ} \\
\rowcolor{tblalt}\LAT{<footer>} & \B{পৃষ্ঠার বা সেকশনের পাদাংশ} \\
\LAT{<main>} & \B{মূল বিষয়বস্তু (প্রতি পৃষ্ঠায় একটি)} \\
\rowcolor{tblalt}\LAT{<nav>} & \B{নেভিগেশন লিংকের অঞ্চল} \\
\LAT{<section>} & \B{বিষয়ভিত্তিক বিভাগ} \\
\rowcolor{tblalt}\LAT{<article>} & \B{স্বয়ংসম্পূর্ণ রচনা/পোস্ট} \\
\LAT{<aside>} & \B{পার্শ্ব বা সম্পর্কিত বিষয়বস্তু} \\
\rowcolor{tblalt}\LAT{<h1>} & \B{সর্বোচ্চ স্তরের শিরোনাম} \\
\LAT{<h2>} & \B{দ্বিতীয় স্তরের শিরোনাম} \\
\rowcolor{tblalt}\LAT{<h3>} & \B{তৃতীয় স্তরের শিরোনাম} \\
\LAT{<h4>} & \B{চতুর্থ স্তরের শিরোনাম} \\
\rowcolor{tblalt}\LAT{<h5>} & \B{পঞ্চম স্তরের শিরোনাম} \\
\LAT{<h6>} & \B{ষষ্ঠ (সর্বনিম্ন) স্তরের শিরোনাম} \\
\rowcolor{tblalt}\LAT{<address>} & \B{যোগাযোগের তথ্য/ঠিকানা} \\
\LAT{<hgroup>} & \B{শিরোনাম গ্রুপ (h1+p বা h2+p)} \\
\rowcolor{tblalt}\LAT{<search>} & \B{অনুসন্ধান বিভাগ (HTML 5.3/2023)} \\
\LAT{<menu>} & \B{কমান্ড/মেনু তালিকা} \LAT{(type)} \\
\rowcolor{tblalt}\LAT{<portal>} & \LAT{src, referrerpolicy} \B{(পরীক্ষামূলক)} \\
\LAT{<fencedframe>} & \LAT{config} \B{(পরীক্ষামূলক, Privacy API)} \\
\end{tabular}}

\chsec{৪. টেক্সট কন্টেন্ট ট্যাগ}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{3.9cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{\B{বিবরণ ও অ্যাট্রিবিউট}} \\
\LAT{<p>} & \B{অনুচ্ছেদ} \\
\rowcolor{tblalt}\LAT{<hr>} (V) & \B{অনুভূমিক বিভাজক রেখা} \\
\LAT{<pre>} & \B{পূর্বনির্ধারিত ফরম্যাট টেক্সট} \\
\rowcolor{tblalt}\LAT{<blockquote>} & \B{বড় উদ্ধৃতি;} \LAT{cite="URL"} \\
\LAT{<ol>} & \B{ক্রমিক তালিকা;} \LAT{type (1/a/A/i/I),} \LAT{start, reversed} \\
\rowcolor{tblalt}\LAT{<ul>} & \B{বুলেট তালিকা} \\
\LAT{<li>} & \B{তালিকার আইটেম;} \LAT{value (ol-এ)} \\
\rowcolor{tblalt}\LAT{<dl>} & \B{বর্ণনামূলক তালিকা} \\
\LAT{<dt>} & \B{সংজ্ঞার্থ শব্দ/পদ} \\
\rowcolor{tblalt}\LAT{<dd>} & \B{সংজ্ঞার্থ বিবরণ} \\
\LAT{<figure>} & \B{চিত্র বা কোড ব্লক} \\
\rowcolor{tblalt}\LAT{<figcaption>} & \B{চিত্রের ক্যাপশন} \\
\LAT{<div>} & \B{জেনেরিক ব্লক কন্টেইনার} \\
\end{tabular}}

\columnbreak

\chsec{৫. ইনলাইন টেক্সট সিমান্টিক্স}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{3.8cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{\B{অর্থ / অ্যাট্রিবিউট}} \\
\LAT{<a>} & \B{হাইপারলিংক;} \LAT{href, target,} \LAT{rel, download, hreflang,} \LAT{type, ping, referrerpolicy} \\
\rowcolor{tblalt}\LAT{<em>} & \B{জোর/জোরালো উচ্চারণ} \\
\LAT{<strong>} & \B{উচ্চ গুরুত্ব} \\
\rowcolor{tblalt}\LAT{<small>} & \B{ছোট ছাপা/আইনি নোট} \\
\LAT{<s>} & \B{বাতিল/অপ্রাসঙ্গিক তথ্য} \\
\rowcolor{tblalt}\LAT{<cite>} & \B{সৃজনকর্মের নাম/রেফারেন্স} \\
\LAT{<q>} & \B{ইনলাইন উদ্ধৃতি;} \LAT{cite=""} \\
\rowcolor{tblalt}\LAT{<dfn>} & \B{সংজ্ঞার্থ শব্দ;} \LAT{title=""} \\
\LAT{<abbr>} & \B{সংক্ষেপণ;} \LAT{title=""} \\
\rowcolor{tblalt}\LAT{<code>} & \B{কোড স্নিপেট} \\
\LAT{<var>} & \B{গাণিতিক/প্রোগ্রামিং চলক} \\
\rowcolor{tblalt}\LAT{<samp>} & \B{কম্পিউটার আউটপুট নমুনা} \\
\LAT{<kbd>} & \B{কীবোর্ড ইনপুট} \\
\rowcolor{tblalt}\LAT{<sub>} & \B{সাবস্ক্রিপ্ট} \\
\LAT{<sup>} & \B{সুপারস্ক্রিপ্ট} \\
\rowcolor{tblalt}\LAT{<time>} & \B{তারিখ/সময়;} \LAT{datetime=""} \\
\LAT{<data>} & \B{মেশিন-পাঠযোগ্য মান;} \LAT{value="*"} \\
\rowcolor{tblalt}\LAT{<mark>} & \B{হাইলাইট করা টেক্সট} \\
\LAT{<span>} & \B{জেনেরিক ইনলাইন কন্টেইনার} \\
\rowcolor{tblalt}\LAT{<b>} & \B{শৈলীগত বোল্ড} \\
\LAT{<i>} & \B{শৈলীগত ইটালিক/পরিভাষা} \\
\rowcolor{tblalt}\LAT{<u>} & \B{শৈলীগত আন্ডারলাইন} \\
\LAT{<bdi>} & \B{দ্বিমুখী বিচ্ছিন্নতা;} \LAT{dir} \\
\rowcolor{tblalt}\LAT{<bdo>} & \B{টেক্সট দিক নির্ধারণ;} \LAT{dir*} \\
\LAT{<br>} (V) & \B{লাইন বিরতি} \\
\rowcolor{tblalt}\LAT{<wbr>} (V) & \B{ঐচ্ছিক লাইন বিরতি বিন্দু} \\
\LAT{<ruby>} & \B{রুবি টীকা কন্টেইনার} \\
\rowcolor{tblalt}\LAT{<rt>} & \B{রুবি টেক্সট (উপরে)} \\
\LAT{<rp>} & \B{রুবি বন্ধনী (ফলব্যাক)} \\
\rowcolor{tblalt}\LAT{<rb>} & \B{রুবি বেস (HTML5 বাতিল)} \\
\LAT{<rtc>} & \B{রুবি টেক্সট কন্টেইনার (বাতিল)} \\
\rowcolor{tblalt}\LAT{<ins>} & \B{যোগ করা হয়েছে;} \LAT{cite, datetime} \\
\LAT{<del>} & \B{মুছে ফেলা হয়েছে;} \LAT{cite, datetime} \\
\end{tabular}}

\end{multicols}

\vspace{2pt}

% ============================================================
% SECTION 6: EMBEDDED CONTENT — full width
% ============================================================
\chsecfull{৬. এম্বেডেড কন্টেন্ট ট্যাগ ও সকল অ্যাট্রিবিউট}

{\scriptsize\setlength{\tabcolsep}{2.5pt}
\noindent\begin{tabular}{|l|c|p{0.86\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{V/P} & \textbf{\B{সকল অ্যাট্রিবিউট}} \\
\hline
\LAT{<img>} & V & \LAT{src*, alt*, width, height, loading (lazy/eager/auto), decoding (async/sync/auto), srcset, sizes, crossorigin (anonymous/use-credentials), referrerpolicy, ismap, usemap, fetchpriority (high/low/auto)} \\
\hline
\rowcolor{tblalt}\LAT{<iframe>} & P & \LAT{src, srcdoc, name, width, height, sandbox (allow-scripts / allow-same-origin / allow-forms / allow-popups / allow-modals / allow-top-navigation / allow-pointer-lock / allow-downloads / allow-presentation), allow, allowfullscreen, loading, referrerpolicy, importance} \\
\hline
\LAT{<embed>} & V & \LAT{src*, type*, width, height} \\
\hline
\rowcolor{tblalt}\LAT{<object>} & P & \LAT{data, type, name, width, height, form, usemap, typemustmatch} \\
\hline
\LAT{<param>} & V & \LAT{name*, value*} \B{(শুধু} \LAT{<object>}\B{-এর ভেতরে, বাতিলের পথে)} \\
\hline
\rowcolor{tblalt}\LAT{<video>} & P & \LAT{src, controls, autoplay, loop, muted, poster, preload (auto/metadata/none), width, height, crossorigin, playsinline, disablepictureinpicture, disableremoteplayback} \\
\hline
\LAT{<audio>} & P & \LAT{src, controls, autoplay, loop, muted, preload (auto/metadata/none), crossorigin} \\
\hline
\rowcolor{tblalt}\LAT{<source>} & V & \LAT{src, srcset, type, media, sizes, width, height} \\
\hline
\LAT{<track>} & V & \LAT{src*, kind (subtitles/captions/chapters/metadata/descriptions), srclang, label, default} \\
\hline
\rowcolor{tblalt}\LAT{<map>} & P & \LAT{name*} \\
\hline
\LAT{<area>} & V & \LAT{href, alt, coords, shape (rect/circle/poly/default), target, rel, download, referrerpolicy, ping} \\
\hline
\rowcolor{tblalt}\LAT{<picture>} & P & \B{নিজস্ব অ্যাট্রিবিউট নেই; শুধু গ্লোবাল অ্যাট্রিবিউট।} \LAT{<source>} \B{ও} \LAT{<img>} \B{ধারণ করে।} \\
\hline
\LAT{<canvas>} & P & \LAT{width, height} \\
\hline
\rowcolor{tblalt}\LAT{<svg>} & P & \LAT{width, height, viewBox, xmlns, fill, stroke, stroke-width, preserveAspectRatio, x, y, rx, ry} \\
\hline
\LAT{<math>} & P & \LAT{display (block/inline), xmlns} \\
\hline
\end{tabular}}

{\tiny\B{* = আবশ্যিক (Required)}}
\vspace{3pt}

% ============================================================
% SECTION 7: TABLE ELEMENTS — full width
% ============================================================
\chsecfull{৭. HTML টেবিল ট্যাগ ও সকল অ্যাট্রিবিউট (table, caption, colgroup, col, thead, tbody, tfoot, tr, th, td)}

{\scriptsize\setlength{\tabcolsep}{2.5pt}
\noindent\begin{tabular}{|l|c|p{0.31\textwidth}|p{0.50\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{V/P} & \textbf{\B{বর্তমান অ্যাট্রিবিউট}} & \textbf{\B{পুরোনো/বাতিল অ্যাট্রিবিউট (CSS দিয়ে করুন)}} \\
\hline
\LAT{<table>} & P & \LAT{border} & \LAT{align, bgcolor, cellpadding, cellspacing, frame (void/above/below/ hsides/vsides/lhs/rhs/box/border), rules (none/groups/rows/cols/all), summary, width} \\
\hline
\rowcolor{tblalt}\LAT{<caption>} & P & \B{(গ্লোবাল)} & \LAT{align (top/bottom/left/right)} \\
\hline
\LAT{<colgroup>} & P & \LAT{span} & \LAT{align, bgcolor, char, charoff, valign, width} \\
\hline
\rowcolor{tblalt}\LAT{<col>} & V & \LAT{span} & \LAT{align, bgcolor, char, charoff, valign, width} \\
\hline
\LAT{<thead>} & P & \B{(গ্লোবাল)} & \LAT{align, bgcolor, char, charoff, valign} \\
\hline
\rowcolor{tblalt}\LAT{<tbody>} & P & \B{(গ্লোবাল)} & \LAT{align, bgcolor, char, charoff, valign} \\
\hline
\LAT{<tfoot>} & P & \B{(গ্লোবাল)} & \LAT{align, bgcolor, char, charoff, valign} \\
\hline
\rowcolor{tblalt}\LAT{<tr>} & P & \B{(গ্লোবাল)} & \LAT{align, bgcolor, char, charoff, valign} \\
\hline
\LAT{<th>} & P & \LAT{colspan, rowspan, headers,} \LAT{scope (row/col/rowgroup/colgroup),} \LAT{abbr} & \LAT{align, axis, bgcolor, char, charoff, height, nowrap, valign, width} \\
\hline
\rowcolor{tblalt}\LAT{<td>} & P & \LAT{colspan, rowspan, headers} & \LAT{align, axis, bgcolor, char, charoff, height, nowrap, valign, width} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTION 8: FORM ELEMENTS — full width
% ============================================================
\chsecfull{৮. HTML ফর্ম ট্যাগ ও সকল অ্যাট্রিবিউট (form, label, input, button, select, datalist, optgroup, option, textarea, output, progress, meter, fieldset, legend)}

{\scriptsize\setlength{\tabcolsep}{2.5pt}
\noindent\begin{tabular}{|l|c|p{0.86\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{V/P} & \textbf{\B{সকল অ্যাট্রিবিউট}} \\
\hline
\LAT{<form>} & P & \LAT{action, method (GET/POST/DELETE/PUT/DIALOG), enctype (application/x-www-form-urlencoded / multipart/form-data / text/plain), target (\_blank/\_self/\_parent/\_top), name, novalidate, autocomplete (on/off), rel, accept-charset} \\
\hline
\rowcolor{tblalt}\LAT{<label>} & P & \LAT{for (htmlFor), form} \\
\hline
\LAT{<input>} & V & \LAT{type, name, value, placeholder, required, disabled, readonly, checked (checkbox/radio), min, max, step, pattern, autocomplete, autofocus, form, list, multiple, size, maxlength, minlength, accept (file), capture (user/environment), dirname, formaction, formenctype, formmethod, formnovalidate, formtarget, inputmode (none/text/decimal/numeric/tel/search/email/url), src, alt, width, height (image type)} \\
\hline
\rowcolor{tblalt}\LAT{<button>} & P & \LAT{type (submit/reset/button), name, value, disabled, autofocus, form, formaction, formenctype, formmethod, formnovalidate, formtarget, popovertarget, popovertargetaction (show/hide/toggle)} \\
\hline
\LAT{<select>} & P & \LAT{name, multiple, size, required, disabled, autofocus, form} \\
\hline
\rowcolor{tblalt}\LAT{<datalist>} & P & \B{(গ্লোবাল অ্যাট্রিবিউট; } \LAT{<option>}\B{ ধারণ করে)} \\
\hline
\LAT{<optgroup>} & P & \LAT{label*, disabled} \\
\hline
\rowcolor{tblalt}\LAT{<option>} & P & \LAT{value, label, selected, disabled} \\
\hline
\LAT{<textarea>} & P & \LAT{name, rows, cols, maxlength, minlength, placeholder, required, disabled, readonly, autofocus, form, wrap (hard/soft), autocomplete, dirname, inputmode, spellcheck} \\
\hline
\rowcolor{tblalt}\LAT{<output>} & P & \LAT{name, for, form} \\
\hline
\LAT{<progress>} & P & \LAT{value, max} \\
\hline
\rowcolor{tblalt}\LAT{<meter>} & P & \LAT{value*, min, max, low, high, optimum, form} \\
\hline
\LAT{<fieldset>} & P & \LAT{name, disabled, form} \\
\hline
\rowcolor{tblalt}\LAT{<legend>} & P & \B{(গ্লোবাল অ্যাট্রিবিউট)} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTIONS 9-11 — 3-col
% ============================================================
\begin{multicols}{3}

\chsec{৯. ইনপুট টাইপ \texttt{(type=)} — সম্পূর্ণ তালিকা}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{3.6cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{type=}} & \textbf{\B{বিবরণ ও বিশেষ অ্যাট্রিবিউট}} \\
\LAT{text} & \B{সাধারণ একলাইন টেক্সট} \\
\rowcolor{tblalt}\LAT{password} & \B{পাসওয়ার্ড (অক্ষর লুকানো)} \\
\LAT{email} & \B{ইমেইল ঠিকানা (ব্রাউজার যাচাই করে)} \\
\rowcolor{tblalt}\LAT{number} & \B{সংখ্যা;} \LAT{min, max, step} \\
\LAT{tel} & \B{ফোন নম্বর} \\
\rowcolor{tblalt}\LAT{url} & \B{ওয়েব ঠিকানা} \\
\LAT{search} & \B{অনুসন্ধান বাক্স} \\
\rowcolor{tblalt}\LAT{date} & \B{তারিখ নির্বাচক} \LAT{(YYYY-MM-DD)} \\
\LAT{time} & \B{সময় নির্বাচক} \LAT{(HH:MM)} \\
\rowcolor{tblalt}\LAT{datetime-local} & \B{তারিখ+সময় একসাথে} \\
\LAT{month} & \B{মাস+বছর নির্বাচক} \\
\rowcolor{tblalt}\LAT{week} & \B{সপ্তাহ+বছর নির্বাচক} \\
\LAT{range} & \B{স্লাইডার;} \LAT{min, max, step} \\
\rowcolor{tblalt}\LAT{color} & \B{রং নির্বাচক} \\
\LAT{checkbox} & \B{চেকবক্স;} \LAT{checked} \\
\rowcolor{tblalt}\LAT{radio} & \B{রেডিও বাটন;} \LAT{checked} \\
\LAT{file} & \B{ফাইল আপলোড;} \LAT{accept, capture,} \LAT{multiple} \\
\rowcolor{tblalt}\LAT{submit} & \B{ফর্ম সাবমিট বাটন;} \LAT{value} \\
\LAT{reset} & \B{ফর্ম রিসেট বাটন;} \LAT{value} \\
\rowcolor{tblalt}\LAT{button} & \B{সাধারণ বাটন (JS দিয়ে ব্যবহার)} \\
\LAT{image} & \B{ছবি বাটন;} \LAT{src*, alt*, width, height} \\
\rowcolor{tblalt}\LAT{hidden} & \B{লুকানো ডেটা ফিল্ড} \\
\end{tabular}}

\chsec{১০. ইন্টারেক্টিভ ও স্ক্রিপ্টিং ট্যাগ}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{3.8cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{\B{অ্যাট্রিবিউট ও বিবরণ}} \\
\LAT{<details>} & \B{ড্রপডাউন প্রকাশ/গোপন বক্স;} \LAT{open} \\
\rowcolor{tblalt}\LAT{<summary>} & \LAT{<details>}\B{-এর ক্লিকযোগ্য শিরোনাম} \\
\LAT{<dialog>} & \B{মডাল বা নন-মডাল ডায়ালগ;} \LAT{open} \\
\rowcolor{tblalt}\LAT{<script>} & \LAT{type, src, async, defer, crossorigin, integrity, referrerpolicy, nomodule, fetchpriority} \\
\LAT{<noscript>} & \B{JS বন্ধ থাকলে দেখায়} \\
\rowcolor{tblalt}\LAT{<canvas>} & \LAT{width, height} \B{(JS দিয়ে গ্রাফিক্স)} \\
\LAT{<template>} & \LAT{shadowrootmode (open/closed)} \\
\rowcolor{tblalt}\LAT{<slot>} & \LAT{name} \B{(Web Components)} \\
\end{tabular}}

\chsec{১১. বাতিল ও পুরোনো ট্যাগ}
{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{@{}lp{3.8cm}@{}}
\rowcolor{tblhdr}\textbf{\LAT{Tag}} & \textbf{\B{পরিবর্তে ব্যবহার করুন}} \\
\LAT{<acronym>} & \LAT{<abbr title="">} \\
\rowcolor{tblalt}\LAT{<applet>} & \LAT{<object>} \B{বা} \LAT{<embed>} \\
\LAT{<basefont>} & \LAT{CSS font-family, font-size} \\
\rowcolor{tblalt}\LAT{<big>} & \LAT{CSS font-size: larger} \\
\LAT{<blink>} & \LAT{CSS @keyframes animation} \\
\rowcolor{tblalt}\LAT{<center>} & \LAT{CSS text-align: center} \\
\LAT{<dir>} & \LAT{<ul>} \\
\rowcolor{tblalt}\LAT{<font>} & \LAT{CSS font-*} \\
\LAT{<frame>} & \LAT{<iframe>} \\
\rowcolor{tblalt}\LAT{<frameset>} & \LAT{CSS layout / Flexbox / Grid} \\
\LAT{<listing>} & \LAT{<pre><code>} \\
\rowcolor{tblalt}\LAT{<marquee>} & \LAT{CSS animation / JS} \\
\LAT{<noframes>} & \B{(ফ্রেমসেট না থাকলে লাগে না)} \\
\rowcolor{tblalt}\LAT{<plaintext>} & \LAT{<pre>} \\
\LAT{<rb>} & \LAT{<ruby>}\B{-এ সরাসরি টেক্সট} \\
\rowcolor{tblalt}\LAT{<rtc>} & \LAT{<ruby>}\B{-এ সরাসরি টেক্সট} \\
\LAT{<strike>} & \LAT{<s>} \B{বা} \LAT{CSS text-decoration: line-through} \\
\rowcolor{tblalt}\LAT{<tt>} & \LAT{<code>} \B{বা} \LAT{CSS font-family: monospace} \\
\LAT{<xmp>} & \LAT{<pre><code>} \\
\end{tabular}}

\end{multicols}

\vspace{2pt}

% ============================================================
% SECTION 12: GLOBAL ATTRIBUTES — full width
% ============================================================
\chsecfull{১২. গ্লোবাল অ্যাট্রিবিউট — সকল HTML ট্যাগে ব্যবহারযোগ্য}

{\scriptsize\setlength{\tabcolsep}{2.5pt}
\noindent\begin{tabular}{|l|p{0.19\textwidth}|l|p{0.19\textwidth}|l|p{0.19\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ ও মান}} & \textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ ও মান}} & \textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ ও মান}} \\
\hline
\LAT{id} & \B{অনন্য পরিচয়কারী (পৃষ্ঠায় একটিমাত্র)} & \LAT{draggable} & \LAT{true/false/auto} & \LAT{data-*} & \B{কাস্টম ডেটা অ্যাট্রিবিউট} \\
\hline
\rowcolor{tblalt}\LAT{class} & \B{এক বা একাধিক CSS ক্লাস নাম} & \LAT{hidden} & \B{এলিমেন্ট লুকিয়ে রাখে} & \LAT{role} & \B{ARIA ভূমিকা নির্ধারণ} \\
\hline
\LAT{style} & \B{ইনলাইন CSS স্টাইল} & \LAT{spellcheck} & \LAT{true/false} & \LAT{aria-*} & \B{অ্যাক্সেসিবিলিটি অ্যাট্রিবিউট} \\
\hline
\rowcolor{tblalt}\LAT{title} & \B{টুলটিপ হিসেবে দেখায়} & \LAT{translate} & \LAT{yes/no} & \LAT{nonce} & \B{CSP নিরাপত্তা টোকেন} \\
\hline
\LAT{lang} & \B{ভাষা কোড;} \LAT{bn, en, ar...} & \LAT{autocapitalize} & \LAT{off, on, words,} \LAT{characters, sentences} & \LAT{part} & \B{শ্যাডো DOM পার্ট নাম} \\
\hline
\rowcolor{tblalt}\LAT{dir} & \LAT{ltr / rtl / auto} & \LAT{enterkeyhint} & \LAT{enter, done, go, next,} \LAT{previous, search, send} & \LAT{slot} & \B{Web Component স্লট নাম} \\
\hline
\LAT{tabindex} & \B{ট্যাব ক্রম;} \LAT{0, -1, N} & \LAT{inputmode} & \LAT{none, text, decimal,} \LAT{numeric, tel, search,} \LAT{email, url} & \LAT{is} & \B{কাস্টম এলিমেন্ট নির্ধারণ} \\
\hline
\rowcolor{tblalt}\LAT{contenteditable} & \LAT{true/false/plaintext-only} & \LAT{popover} & \LAT{auto/manual} & \LAT{popovertarget} & \B{পপওভার লক্ষ্য ID} \\
\hline
\LAT{accesskey} & \B{কীবোর্ড শর্টকাট (Alt+key)} & \LAT{autofocus} & \B{পৃষ্ঠা লোডে ফোকাস পায়} & \LAT{itemscope} & \B{মাইক্রোডেটা স্কোপ} \\
\hline
\rowcolor{tblalt}\LAT{itemprop} & \B{মাইক্রোডেটা বৈশিষ্ট্য} & \LAT{itemtype} & \B{মাইক্রোডেটা টাইপ URL} & \LAT{itemid} & \B{মাইক্রোডেটা আইডি} \\
\hline
\LAT{itemref} & \B{মাইক্রোডেটা রেফারেন্স ID} & \LAT{exportparts} & \B{Shadow DOM পার্ট এক্সপোর্ট} & \LAT{inert} & \B{ইন্টারঅ্যাকশন নিষ্ক্রিয় করে} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTION 13: ARIA — full width
% ============================================================
\chsecfull{১৩. ARIA অ্যাট্রিবিউট — অ্যাক্সেসিবিলিটি (Accessibility)}

{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{|p{0.135\textwidth}|p{0.185\textwidth}|p{0.135\textwidth}|p{0.185\textwidth}|p{0.135\textwidth}|p{0.185\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ}} & \textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ}} & \textbf{\B{অ্যাট্রিবিউট}} & \textbf{\B{বিবরণ}} \\
\hline
\LAT{aria-label} & \B{অ্যাক্সেসিবল লেবেল টেক্সট} & \LAT{aria-expanded} & \B{প্রসারিত অবস্থা (true/false)} & \LAT{aria-multiline} & \B{বহুলাইন ইনপুট} \\
\hline
\rowcolor{tblalt}\LAT{aria-labelledby} & \B{লেবেল এলিমেন্টের ID} & \LAT{aria-haspopup} & \LAT{true/menu/listbox/tree/grid/dialog} & \LAT{aria-multiselectable} & \B{একাধিক নির্বাচন সম্ভব} \\
\hline
\LAT{aria-describedby} & \B{বিবরণ এলিমেন্টের ID} & \LAT{aria-invalid} & \LAT{true/false/grammar/spelling} & \LAT{aria-orientation} & \LAT{horizontal/vertical/undefined} \\
\hline
\rowcolor{tblalt}\LAT{aria-hidden} & \B{স্ক্রিন রিডার থেকে লুকায়} & \LAT{aria-pressed} & \LAT{true/false/mixed/undefined} & \LAT{aria-owns} & \B{মালিকানা সম্পর্ক ID} \\
\hline
\LAT{aria-live} & \LAT{off/polite/assertive} & \LAT{aria-readonly} & \LAT{true/false} & \LAT{aria-placeholder} & \B{প্লেসহোল্ডার টেক্সট} \\
\hline
\rowcolor{tblalt}\LAT{aria-atomic} & \LAT{true/false} & \LAT{aria-required} & \LAT{true/false} & \LAT{aria-selected} & \LAT{true/false/undefined} \\
\hline
\LAT{aria-busy} & \LAT{true/false} & \LAT{aria-controls} & \B{নিয়ন্ত্রিত এলিমেন্টের ID} & \LAT{aria-setsize} & \B{সেটের মোট সংখ্যা} \\
\hline
\rowcolor{tblalt}\LAT{aria-current} & \LAT{page/step/location/date/time/true/false} & \LAT{aria-flowto} & \B{পড়ার ক্রম ID} & \LAT{aria-posinset} & \B{সেটে অবস্থান নম্বর} \\
\hline
\LAT{aria-disabled} & \LAT{true/false} & \LAT{aria-grabbed} & \LAT{true/false/undefined} & \LAT{aria-rowcount} & \B{সারির মোট সংখ্যা} \\
\hline
\rowcolor{tblalt}\LAT{aria-errormessage} & \B{ত্রুটি বার্তার এলিমেন্ট ID} & \LAT{aria-dropeffect} & \LAT{copy/move/link/execute/popup/none} & \LAT{aria-colcount} & \B{কলামের মোট সংখ্যা} \\
\hline
\LAT{aria-details} & \B{বিস্তারিত এলিমেন্টের ID} & \LAT{aria-keyshortcuts} & \B{কীবোর্ড শর্টকাট স্ট্রিং} & \LAT{aria-valuemax} & \B{সর্বোচ্চ মান} \\
\hline
\rowcolor{tblalt}\LAT{aria-relevant} & \LAT{additions/removals/text/all} & \LAT{aria-roledescription} & \B{ভূমিকার মানবপাঠযোগ্য বিবরণ} & \LAT{aria-valuemin} & \B{সর্বনিম্ন মান} \\
\hline
\LAT{aria-sort} & \LAT{ascending/descending/other/none} & \LAT{aria-colindex} & \B{কলাম সূচক (১ থেকে)} & \LAT{aria-valuenow} & \B{বর্তমান সংখ্যামান} \\
\hline
\rowcolor{tblalt}\LAT{aria-rowindex} & \B{সারি সূচক (১ থেকে)} & \LAT{aria-rowspan} & \B{সারি বিস্তৃতি সংখ্যা} & \LAT{aria-valuetext} & \B{মানের পাঠযোগ্য টেক্সট} \\
\hline
\LAT{aria-colspan} & \B{কলাম বিস্তৃতি সংখ্যা} & \LAT{aria-checked} & \LAT{true/false/mixed} & \LAT{aria-activedescendant} & \B{সক্রিয় সন্তান এলিমেন্ট ID} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTION 14: EVENT ATTRIBUTES — full width
% ============================================================
\chsecfull{১৪. ইভেন্ট অ্যাট্রিবিউট (Event Attributes)}

{\tiny\setlength{\tabcolsep}{1.4pt}
\noindent\begin{tabular}{|p{0.085\textwidth}|p{0.395\textwidth}|p{0.085\textwidth}|p{0.395\textwidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{বিভাগ}} & \textbf{\B{ইভেন্ট অ্যাট্রিবিউটসমূহ}} & \textbf{\B{বিভাগ}} & \textbf{\B{ইভেন্ট অ্যাট্রিবিউটসমূহ}} \\
\hline
\B{উইন্ডো (Window)} & \LAT{onload, onunload, onbeforeunload, onresize, onscroll, onoffline, ononline, onhashchange, onpopstate, onmessage, onstorage, onpageshow, onpagehide} & \B{ড্র্যাগ (Drag)} & \LAT{ondrag, ondragstart, ondragend, ondragover, ondragenter, ondragleave, ondrop} \\
\hline
\rowcolor{tblalt}\B{মাউস (Mouse)} & \LAT{onclick, ondblclick, onmousedown, onmouseup, onmouseover, onmouseout, onmousemove, onmouseenter, onmouseleave, oncontextmenu, onwheel} & \B{ক্লিপবোর্ড (Clipboard)} & \LAT{oncopy, oncut, onpaste} \\
\hline
\B{কীবোর্ড (Keyboard)} & \LAT{onkeydown, onkeyup, onkeypress} & \B{পয়েন্টার (Pointer)} & \LAT{onpointerdown, onpointerup, onpointermove, onpointerenter, onpointerleave, onpointerover, onpointerout, onpointercancel, ongotpointercapture, onlostpointercapture} \\
\hline
\rowcolor{tblalt}\B{ফর্ম (Form)} & \LAT{onsubmit, onreset, oninput, onchange, onselect, oninvalid, onsearch, onformdata} & \B{টাচ (Touch)} & \LAT{ontouchstart, ontouchend, ontouchmove, ontouchcancel} \\
\hline
\B{ফোকাস (Focus)} & \LAT{onfocus, onblur, onfocusin, onfocusout} & \B{মিডিয়া (Media)} & \LAT{onplay, onpause, onended, oncanplay, oncanplaythrough, ontimeupdate, onvolumechange, onseeking, onseeked, onwaiting, onloadeddata, onloadedmetadata, onprogress, onstalled, onsuspend, ondurationchange, onemptied, onratechange} \\
\hline
\rowcolor{tblalt}\B{অ্যানিমেশন} & \LAT{onanimationstart, onanimationend, onanimationiteration, ontransitionstart, ontransitionend, ontransitionrun, ontransitioncancel} & \B{বিবিধ (Misc)} & \LAT{onerror, onabort, onclose, ontoggle, onfullscreenchange, onfullscreenerror, onresize, onbeforetoggle, onbeforeinput, oninput} \\
\hline
\end{tabular}}

\vspace{3pt}

% ============================================================
% SECTION 15: HTML COLOR CHART — full width
% ============================================================
\chsecfull{১৫. এইচটিএমএল কালার চার্ট (HTML Color Chart)}

{\tiny\setlength{\tabcolsep}{3pt}\renewcommand{\arraystretch}{1.20}
\noindent\begin{tabular}{|m{1.05cm}|l|l|l||m{1.05cm}|l|l|l|}
\hline
\rowcolor{tblhdr}\textbf{\B{রঙ}} & \textbf{\LAT{RGB}} & \textbf{\B{নাম}} & \textbf{\LAT{Hex}} & \textbf{\B{রঙ}} & \textbf{\LAT{RGB}} & \textbf{\B{নাম}} & \textbf{\LAT{Hex}} \\
\hline
\cellcolor{clrBlack}\rule{0pt}{0.38cm} & \LAT{0, 0, 0} & \LAT{Black} & \LAT{000000} & \cellcolor{clrKhaki}\rule{0pt}{0.38cm} & \LAT{240, 230, 140} & \LAT{Khaki} & \LAT{F0E68C} \\
\hline
\rowcolor{tblalt}\cellcolor{clrBlue}\rule{0pt}{0.38cm} & \LAT{0, 0, 255} & \LAT{Blue} & \LAT{0000FF} & \cellcolor{clrMagenta}\rule{0pt}{0.38cm} & \LAT{255, 0, 255} & \LAT{Magenta} & \LAT{FF00FF} \\
\hline
\cellcolor{clrBlueViolet}\rule{0pt}{0.38cm} & \LAT{138, 43, 226} & \LAT{Blue Violet} & \LAT{8A2BE2} & \cellcolor{clrNavy}\rule{0pt}{0.38cm} & \LAT{0, 0, 128} & \LAT{Navy} & \LAT{000080} \\
\hline
\rowcolor{tblalt}\cellcolor{clrBrown}\rule{0pt}{0.38cm} & \LAT{165, 42, 42} & \LAT{Brown} & \LAT{A52A2A} & \cellcolor{clrOlive}\rule{0pt}{0.38cm} & \LAT{128, 128, 0} & \LAT{Olive} & \LAT{808000} \\
\hline
\cellcolor{clrBurlyWood}\rule{0pt}{0.38cm} & \LAT{222, 184, 135} & \LAT{Burly Wood} & \LAT{DEB887} & \cellcolor{clrOrange}\rule{0pt}{0.38cm} & \LAT{255, 165, 0} & \LAT{Orange} & \LAT{FFA500} \\
\hline
\rowcolor{tblalt}\cellcolor{clrChocolate}\rule{0pt}{0.38cm} & \LAT{210, 105, 30} & \LAT{Chocolate} & \LAT{D2691E} & \cellcolor{clrPink}\rule{0pt}{0.38cm} & \LAT{255, 192, 203} & \LAT{Pink} & \LAT{FFC0CB} \\
\hline
\cellcolor{clrCyan}\rule{0pt}{0.38cm} & \LAT{0, 255, 255} & \LAT{Cyan} & \LAT{00FFFF} & \cellcolor{clrPurple}\rule{0pt}{0.38cm} & \LAT{128, 0, 128} & \LAT{Purple} & \LAT{800080} \\
\hline
\rowcolor{tblalt}\cellcolor{clrDarkBlue}\rule{0pt}{0.38cm} & \LAT{0, 0, 139} & \LAT{Dark Blue} & \LAT{00008B} & \cellcolor{clrRed}\rule{0pt}{0.38cm} & \LAT{255, 0, 0} & \LAT{Red} & \LAT{FF0000} \\
\hline
\cellcolor{clrDarkGreen}\rule{0pt}{0.38cm} & \LAT{0, 100, 0} & \LAT{Dark Green} & \LAT{006400} & \cellcolor{clrSilver}\rule{0pt}{0.38cm} & \LAT{192, 192, 192} & \LAT{Silver} & \LAT{C0C0C0} \\
\hline
\rowcolor{tblalt}\cellcolor{clrDarkKhaki}\rule{0pt}{0.38cm} & \LAT{189, 183, 107} & \LAT{Dark Khaki} & \LAT{BDB76B} & \cellcolor{clrSkyBlue}\rule{0pt}{0.38cm} & \LAT{135, 206, 235} & \LAT{Sky Blue} & \LAT{87CEEB} \\
\hline
\cellcolor{clrDarkRed}\rule{0pt}{0.38cm} & \LAT{139, 0, 0} & \LAT{Dark Red} & \LAT{8B0000} & \cellcolor{clrSnow}\rule{0pt}{0.38cm} & \LAT{255, 250, 250} & \LAT{Snow} & \LAT{FFFAFA} \\
\hline
\rowcolor{tblalt}\cellcolor{clrGold}\rule{0pt}{0.38cm} & \LAT{255, 215, 0} & \LAT{Gold} & \LAT{FFD700} & \cellcolor{clrViolet}\rule{0pt}{0.38cm} & \LAT{238, 130, 238} & \LAT{Violet} & \LAT{EE82EE} \\
\hline
\cellcolor{clrGray}\rule{0pt}{0.38cm} & \LAT{128, 128, 128} & \LAT{Gray} & \LAT{808080} & \cellcolor{clrWhite}\rule{0pt}{0.38cm} & \LAT{255, 255, 255} & \LAT{White} & \LAT{FFFFFF} \\
\hline
\rowcolor{tblalt}\cellcolor{clrGreen}\rule{0pt}{0.38cm} & \LAT{0, 128, 0} & \LAT{Green} & \LAT{008000} & \cellcolor{clrYellow}\rule{0pt}{0.38cm} & \LAT{255, 255, 0} & \LAT{Yellow} & \LAT{FFFF00} \\
\hline
\cellcolor{clrIndigo}\rule{0pt}{0.38cm} & \LAT{75, 0, 130} & \LAT{Indigo} & \LAT{4B0082} & \cellcolor{clrYellowGreen}\rule{0pt}{0.38cm} & \LAT{154, 205, 50} & \LAT{Yellow Green} & \LAT{9ACD32} \\
\hline
\rowcolor{tblalt}\cellcolor{clrAntiqueWhite}\rule{0pt}{0.38cm} & \LAT{250, 235, 215} & \LAT{Antique White} & \LAT{FAEBD7} & \cellcolor{clrAquamarine}\rule{0pt}{0.38cm} & \LAT{127, 255, 212} & \LAT{Aquamarine} & \LAT{7FFFD4} \\
\hline
\cellcolor{clrBeige}\rule{0pt}{0.38cm} & \LAT{245, 245, 220} & \LAT{Beige} & \LAT{F5F5DC} & \cellcolor{clrCadetBlue}\rule{0pt}{0.38cm} & \LAT{95, 158, 160} & \LAT{Cadet Blue} & \LAT{5F9EA0} \\
\hline
\rowcolor{tblalt}\cellcolor{clrDarkOrange}\rule{0pt}{0.38cm} & \LAT{255, 140, 0} & \LAT{Dark Orange} & \LAT{FF8C00} & \cellcolor{clrMaroon}\rule{0pt}{0.38cm} & \LAT{128, 0, 0} & \LAT{Maroon} & \LAT{800000} \\
\hline
\end{tabular}}
\end{document}
'''

tex_content = tex_content  

with open("ict.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

def run(cmd):
    return subprocess.run(cmd, shell=True).returncode

if not shutil.which("fc-cache"):
    run("apt-get update && apt-get install -y fontconfig")

if not shutil.which("xelatex"):
    run("apt-get update && apt-get install -y texlive-full")

run("fc-cache -fv 2>/dev/null")

run("xelatex -interaction=nonstopmode ict.tex 2>&1 | tail -20")
run("xelatex -interaction=nonstopmode ict.tex 2>&1 | tail -5")

print("PDF ready:", os.path.exists("ict.pdf"))
