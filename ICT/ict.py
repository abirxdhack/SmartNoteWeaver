TEX = r"""
\documentclass[11pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[left=0.85cm,right=0.85cm,top=1.5cm,bottom=1.85cm,headheight=22pt,headsep=6pt,footskip=32pt]{geometry}
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
\usetikzlibrary{arrows.meta,calc,shapes.gates.logic.US,shapes.geometric,positioning,decorations.pathmorphing,decorations.pathreplacing,shapes.symbols,shapes.arrows,shapes.multipart}
\usepackage{adjustbox}
\usepackage{makecell}
\usepackage{longtable}
\usepackage{multirow}
\usepackage{needspace}
\usepackage{fancyhdr}
\usepackage{ragged2e}
\setlength{\arrayrulewidth}{0.25pt}
\setlength{\tabcolsep}{2pt}
\renewcommand{\arraystretch}{1.15}
\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}
\definecolor{sectionbg}{RGB}{27,79,142}
\definecolor{subsecbg}{RGB}{56,120,191}
\definecolor{hdrline}{RGB}{27,79,142}
\definecolor{ftrfill}{RGB}{240,244,251}
\definecolor{accent}{RGB}{220,53,69}
\definecolor{shape1}{RGB}{255,214,102}
\definecolor{shape2}{RGB}{144,202,249}
\definecolor{shape3}{RGB}{165,214,167}
\definecolor{shape4}{RGB}{239,154,154}
\definecolor{shape5}{RGB}{206,147,216}
\definecolor{shape6}{RGB}{255,183,77}
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
\definecolor{gatewire}{RGB}{28,88,135}
\definecolor{gateout}{RGB}{220,53,69}
\setlength{\emergencystretch}{40pt}
\hbadness=99999
\vbadness=99999
\hfuzz=2pt
\vfuzz=2pt
\widowpenalty=10000
\clubpenalty=10000
\sloppy
\raggedbottom
\setlength{\parskip}{2.4pt}
\setlength{\parindent}{0pt}
\setlength{\columnsep}{12pt}
\setlength{\columnseprule}{0.3pt}
\setlength{\multicolsep}{2pt plus 1pt minus 1pt}
\setlength{\intextsep}{2pt}
\setlength{\textfloatsep}{2pt}
\setlength{\abovedisplayskip}{1pt}
\setlength{\belowdisplayskip}{1pt}
\setlist{nosep,topsep=0pt,partopsep=0pt,parsep=0pt,itemsep=0pt,leftmargin=1.1em}
\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\setlist[itemize]{nosep, leftmargin=1.1em, topsep=0pt, itemsep=0pt, parsep=0pt}
\raggedcolumns
\tolerance=9999
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{NotoSerifBengali-Regular.ttf}[
  Path=./fonts/,
  Script=Bengali,
  Renderer=HarfBuzz,
  BoldFont=NotoSerifBengali-Bold.ttf,
  ItalicFont=NotoSerifBengali-Regular.ttf,
  BoldItalicFont=NotoSerifBengali-Bold.ttf,
  AutoFakeSlant=0.18
]
\newfontfamily\bn{NotoSerifBengali-Regular.ttf}[Path=./fonts/, Script=Bengali, BoldFont=NotoSerifBengali-Bold.ttf, ItalicFont=NotoSerifBengali-Regular.ttf, BoldItalicFont=NotoSerifBengali-Bold.ttf, Renderer=HarfBuzz, AutoFakeSlant=0.18]
\newfontfamily\lat{Latin Modern Roman}[Ligatures=TeX]
\tikzset{every picture/.append style={font=\small,baseline={([yshift=-.6ex]current bounding box.center)}}}
\providecommand{\pbox}[2]{\parbox{#1}{#2}}
\providecommand{\iub}[1]{\underline{\textbf{#1}}}
\newcommand{\B}[1]{\ifmmode\text{{\bn #1}}\else{\bn #1}\fi}
\newcommand{\LAT}[1]{{\lat #1}}
\newcommand{\chsec}[1]{%
  \needspace{3\baselineskip}\vspace{3pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{2pt}\par\noindent%
}
\newcommand{\chsecfull}[1]{%
  \needspace{3\baselineskip}\vspace{3pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\textwidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{2pt}\par\noindent%
}
\newcommand{\chsub}[2]{%
  \needspace{3\baselineskip}\vspace{2pt}%
  \noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \bfseries\footnotesize\color{white}\;\B{#1}\ \B{#2}%
  }}%
  \vspace{1pt}\par\noindent%
}
\newcommand{\itm}[1]{\par\noindent\textbf{{\lat #1.}}\;}
\newcommand{\sub}[1]{\textbf{({\lat #1})}\;}
\newcommand{\ovalnode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape1,ellipse,minimum width=1.4cm,minimum height=0.55cm,inner sep=1pt]{\scriptsize #2};}
\newcommand{\parallelogramnode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape2,trapezium,trapezium left angle=70,trapezium right angle=110,minimum width=1.4cm,minimum height=0.55cm,inner sep=1pt]{\scriptsize #2};}
\newcommand{\rectanglenode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape3,rectangle,minimum width=1.4cm,minimum height=0.55cm,inner sep=1pt]{\scriptsize #2};}
\newcommand{\diamondnode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape4,diamond,aspect=2,minimum width=1.4cm,minimum height=0.55cm,inner sep=0pt]{\scriptsize #2};}
\newcommand{\circlenode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape5,circle,minimum size=0.55cm,inner sep=0pt]{\scriptsize #2};}
\newcommand{\rightarrownode}[2]{\tikz[baseline=-0.5ex]\node[draw=black,thick,fill=shape6,single arrow,single arrow head extend=2pt,minimum width=1.2cm,minimum height=0.5cm,inner sep=1pt]{\scriptsize #2};}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\footrulewidth}{0.4pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{hdrline}\leaders\hrule height \headrulewidth\hfill}}
\renewcommand{\footrule}{\hbox to\headwidth{\color{hdrline}\leaders\hrule height \footrulewidth\hfill}}
\fancyhead[L]{\small\textbf{\LAT{ICT Notes}} \; {\bn HSC}}
\fancyhead[C]{\small\textbf{\B{তথ্য ও যোগাযোগ প্রযুক্তি}}}
\fancyhead[R]{\small\textbf{\LAT{Abir Arafat Chawdhury}}}
\fancyfoot[L]{\footnotesize\B{প্রস্তুতকারী:} \LAT{Abir Arafat Chawdhury}}
\fancyfoot[C]{\footnotesize\LAT{WhatsApp: +8801963818285}}
\fancyfoot[R]{\footnotesize\B{পৃষ্ঠা} \thepage}
\fancypagestyle{plain}{\fancyhf{}\fancyhead[L]{\small\textbf{\LAT{ICT Notes}} \; {\bn HSC}}\fancyhead[C]{\small\textbf{\B{তথ্য ও যোগাযোগ প্রযুক্তি}}}\fancyhead[R]{\small\textbf{\LAT{Abir Arafat Chawdhury}}}\fancyfoot[L]{\footnotesize\LAT{WhatsApp: +8801963818285}}\fancyfoot[R]{\footnotesize\B{পৃষ্ঠা} \thepage}\renewcommand{\headrulewidth}{0.6pt}\renewcommand{\footrulewidth}{0.4pt}}
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
\itm{8} \B{সর্বোচ্চ মান:} \LAT{$n$} \B{সংখ্যা ভিত্তি} \LAT{$r$} \B{তে} \LAT{Max $= r^n-1$}
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
\itm{8} \LAT{$n$} \B{বিট সাইনড পরিসীমা:} \LAT{$-2^{n-1}$} \B{থেকে} \LAT{$2^{n-1}-1$}
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
\itm{2} \LAT{1 Byte = 8 bits; 1 KB = 1024 Bytes; 1 MB = 1024 KB; 1 GB = 1024 MB; 1 TB = 1024 GB}
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
\vspace{1pt}
\begingroup
\tiny
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.15}
\setlength{\LTpre}{0pt}\setlength{\LTpost}{0pt}
\begin{longtable}{|l|p{0.165\textwidth}|l|p{0.165\textwidth}|l|p{0.165\textwidth}|l|p{0.165\textwidth}|}
\hline
\rowcolor{tblhdr}
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} \\\hline
\endfirsthead
\hline
\rowcolor{tblhdr}
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} &
\textbf{\LAT{Abbr.}} & \textbf{\LAT{Full Form}} \\\hline
\endhead
\hline\endfoot
\hline\endlastfoot
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
\LAT{IMSI} & \LAT{International Mobile Subscriber Identity} & \LAT{IMT} & \LAT{International Mobile Telecommunications} & \LAT{INP} & \LAT{INPut} & \LAT{IoT} & \LAT{Internet of Things} \\\hline
\LAT{IP} & \LAT{Internet Protocol} & \LAT{IPTV} & \LAT{Internet Protocol Television} & \LAT{ISOC} & \LAT{Internet Society} & \LAT{ISP} & \LAT{Internet Service Provider} \\\hline
\LAT{IT} & \LAT{Information Technology} & \LAT{ITAA} & \LAT{Information Technology Association of America} & \LAT{ITU} & \LAT{International Telecommunication Union} & \LAT{JMP} & \LAT{JuMP} \\\hline
\LAT{JPEG} & \LAT{Joint Photographic Expert Group} & \LAT{KB} & \LAT{Kilobyte} & \LAT{Kbps} & \LAT{Kilobits per second} & \LAT{KHz} & \LAT{Kilohertz} \\\hline
\LAT{KPI} & \LAT{Key Performance Indicators} & \LAT{LAN} & \LAT{Local Area Network} & \LAT{LCD} & \LAT{Liquid Crystal Display} & \LAT{LDA} & \LAT{Load Accumulator} \\\hline
\LAT{LED} & \LAT{Light Emitting Diode} & \LAT{LF} & \LAT{Low Frequency} & \LAT{LISP} & \LAT{List Processing} & \LAT{LMR} & \LAT{Land Mobile Radio} \\\hline
\LAT{LOS} & \LAT{Line Of Sight} & \LAT{LTE} & \LAT{Long Term Evolution} & \LAT{MAC} & \LAT{Mandatory Access Control} & \LAT{MAN} & \LAT{Metropolitan Area Network} \\\hline
\LAT{Mb} & \LAT{Megabit} & \LAT{MB} & \LAT{Megabyte} & \LAT{Mbps} & \LAT{Megabits per second} & \LAT{MF} & \LAT{Medium Frequency} \\\hline
\LAT{MHz} & \LAT{Megahertz} & \LAT{MIMO} & \LAT{Multiple Input and Multiple Output} & \LAT{MIN} & \LAT{Mobile Identification Number} & \LAT{MIST} & \LAT{Minimally Invasive Surgical Trainer} \\\hline
\LAT{MIT} & \LAT{Massachusetts Institute of Technology} & \LAT{MMS} & \LAT{Multimedia Message Service} & \LAT{MoBo} & \LAT{Motherboard} & \LAT{MRI} & \LAT{Magnetic Resonance Imaging} \\\hline
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
\LAT{VIRUS} & \LAT{Vital Information Resource Under Siege} & \LAT{VLF} & \LAT{Very Low Frequency} & \LAT{VOIP} & \LAT{Voice Over Internet Protocol} & \LAT{VPN} & \LAT{Virtual Private Network} \\\hline
\LAT{VR} & \LAT{Virtual Reality} & \LAT{VSAT} & \LAT{Very Small Aperture Terminal} & \LAT{WAN} & \LAT{Wide Area Network} & \LAT{WAP} & \LAT{Wireless Application Protocol} \\\hline
\LAT{WCDMA} & \LAT{Wideband Code Division Multiple Access} & \LAT{WiBro} & \LAT{Wireless Broadband} & \LAT{Wi-Fi} & \LAT{Wireless Fidelity} & \LAT{WiMAX} & \LAT{Worldwide Interoperability for Microwave Access} \\\hline
\LAT{WPA} & \LAT{Wi-Fi Protected Access} & \LAT{WWW} & \LAT{World Wide Web} & \LAT{XHTML} & \LAT{Extensible Hyper Text Markup Language} & \LAT{YPSA} & \LAT{Young Power in Social Action} \\\hline
\LAT{4GL} & \LAT{Fourth Generation Language} & & & & & & \\\hline
\end{longtable}
\endgroup
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\chsecfull{৮. বিভিন্ন উদ্ভাবক ও প্রযুক্তি উদ্ভাবক}
\noindent\scriptsize
\setlength{\tabcolsep}{2.4pt}
\renewcommand{\arraystretch}{1.15}
\begingroup
\begin{longtable}{|>{\raggedright\arraybackslash}p{0.13\linewidth}|>{\raggedright\arraybackslash}p{0.18\linewidth}|>{\centering\arraybackslash}p{0.08\linewidth}|>{\centering\arraybackslash}p{0.10\linewidth}|>{\raggedright\arraybackslash}p{0.44\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বিষয়বস্তু} & \B{উদ্ভাবক} & \B{দেশ} & \B{জন্ম--মৃত্যু} & \B{সূত্র/অবদান} \\\hline
\endfirsthead
\hline
\rowcolor{tblhdr} \B{বিষয়বস্তু} & \B{উদ্ভাবক} & \B{দেশ} & \B{জন্ম--মৃত্যু} & \B{সূত্র/অবদান} \\\hline
\endhead
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
\end{longtable}
\endgroup
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.0}
\normalsize

\vspace{2pt}
\chsecfull{৯. মৌলিক গেইটসমূহ (Basic Gates)}
\noindent\scriptsize
\begin{center}
\begin{adjustbox}{max width=\textwidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.11\textwidth}|>{\centering\arraybackslash}p{0.29\textwidth}|>{\centering\arraybackslash}p{0.16\textwidth}|>{\centering\arraybackslash}p{0.17\textwidth}|>{\centering\arraybackslash}p{0.20\textwidth}|}
\hline
\rowcolor{tblhdr}\B{গেট} & \B{রঙিন লজিক প্রতীক} & \B{ফাংশন} & \B{সুইচ ধারণা} & \B{সত্য সারণি} \\\hline
\B{OR} &
\begin{tikzpicture}[scale=0.66,thick,every node/.style={font=\scriptsize}]
\node[or gate US, draw=clrBlue, very thick, fill=white, logic gate inputs=nn, minimum width=1.65cm] (g) at (1.35,0) {};
\draw[-Latex,clrDarkGreen,very thick] (-0.65,0.38) node[left]{A} -- (g.input 1);
\draw[-Latex,clrDarkGreen,very thick] (-0.65,-0.38) node[left]{B} -- (g.input 2);
\draw[-Latex,accent,very thick] (g.output) -- (3.22,0) node[right]{X};
\node[clrBlue,font=\tiny\bfseries] at (1.25,0) {OR};
\end{tikzpicture} &
\LAT{$X=A+B$} &
\begin{tikzpicture}[scale=0.52,thick]
\draw[clrBlue,very thick] (0,0)--(.62,0)--(.62,.38)--(.96,.38) (1.32,.38)--(1.72,.38)--(1.72,0)--(2.28,0);
\draw[clrBlue,very thick] (.62,0)--(.62,-.38)--(.96,-.38) (1.32,-.38)--(1.72,-.38)--(1.72,0);
\draw[accent,very thick] (2.28,0)--(2.58,0);\draw[accent,fill=shape1] (2.78,0) circle(.16);\draw[accent,very thick] (2.94,0)--(3.26,0);
\draw[clrDarkGreen,very thick] (.96,.38)--(1.25,.58);\draw[clrDarkGreen,very thick] (.96,-.38)--(1.25,-.18);
\end{tikzpicture} &
\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&0\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&1\end{tabular}\\\hline
\B{AND} &
\begin{tikzpicture}[scale=0.66,thick,every node/.style={font=\scriptsize}]
\node[and gate US, draw=clrDarkGreen, very thick, fill=white, logic gate inputs=nn, minimum width=1.65cm] (g) at (1.35,0) {};
\draw[-Latex,clrBlue,very thick] (-0.65,0.38) node[left]{A} -- (g.input 1);
\draw[-Latex,clrBlue,very thick] (-0.65,-0.38) node[left]{B} -- (g.input 2);
\draw[-Latex,accent,very thick] (g.output) -- (3.22,0) node[right]{X};
\node[clrDarkGreen,font=\tiny\bfseries] at (1.18,0) {AND};
\end{tikzpicture} &
\LAT{$X=A\cdot B$} &
\begin{tikzpicture}[scale=0.52,thick]
\draw[clrBlue,very thick] (0,0)--(.55,0) (.95,0)--(1.45,0) (1.85,0)--(2.42,0);
\draw[accent,very thick] (2.42,0)--(2.66,0);\draw[accent,fill=shape1] (2.84,0) circle(.16);\draw[accent,very thick] (3.00,0)--(3.28,0)--(3.28,-.55)--(0,-.55)--(0,0);
\draw[clrDarkGreen,very thick] (.55,0)--(.88,.22);\draw[clrDarkGreen,very thick] (1.45,0)--(1.78,.22);
\end{tikzpicture} &
\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&0\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&1\end{tabular}\\\hline
\B{NOT} &
\begin{tikzpicture}[scale=0.70,thick,every node/.style={font=\scriptsize}]
\node[not gate US, draw=clrDarkRed, very thick, fill=white, minimum width=1.45cm] (g) at (1.25,0) {};
\draw[-Latex,clrBlue,very thick] (-0.55,0) node[left]{A} -- (g.input);
\draw[-Latex,accent,very thick] (g.output) -- (3.05,0) node[right]{$\bar A$};
\node[clrDarkRed,font=\tiny\bfseries] at (1.03,0) {NOT};
\end{tikzpicture} &
\LAT{$X=\bar A$} &
\begin{tikzpicture}[scale=0.52,thick]
\draw[clrBlue,very thick] (0,0)--(.82,0)--(.82,-.28) (.82,-.62)--(.82,-.95)--(2.95,-.95)--(2.95,0)--(2.35,0);
\draw[accent,fill=shape1] (2.15,0) circle(.16);\draw[accent,very thick] (.82,0)--(1.92,0);
\draw[clrDarkGreen,very thick] (.82,-.28)--(1.12,-.04);
\end{tikzpicture} &
\begin{tabular}{c|c}\rowcolor{tblhdr}A&X\\\hline\rowcolor{tblalt}0&1\\1&0\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}
\normalsize
\itm{1} \B{OR: যেকোনো একটি ইনপুট ১ হলে আউটপুট ১।}
\itm{2} \B{AND: সব ইনপুট ১ হলেই আউটপুট ১।}
\itm{3} \B{NOT: ইনপুটের বিপরীত মান আউটপুট দেয়।}

\chsecfull{১০. যৌগিক গেইটসমূহ (Compound Gates)}
\noindent\scriptsize
\begin{center}
\begin{adjustbox}{max width=\textwidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.11\textwidth}|>{\centering\arraybackslash}p{0.23\textwidth}|>{\centering\arraybackslash}p{0.18\textwidth}|>{\centering\arraybackslash}p{0.17\textwidth}|>{\centering\arraybackslash}p{0.23\textwidth}|}
\hline
\rowcolor{tblhdr}\B{গেট} & \B{রঙিন প্রতীক} & \B{ফাংশন} & \B{ধারণা} & \B{সত্য সারণি} \\\hline
\B{NOR} & \begin{tikzpicture}[scale=0.62,thick,every node/.style={font=\scriptsize}]\node[nor gate US, draw=clrOrange, very thick, fill=white, logic gate inputs=nn] (g) at (1.2,0) {};\draw[-Latex,clrBlue,very thick] (-.5,.33) node[left]{A} -- (g.input 1);\draw[-Latex,clrBlue,very thick] (-.5,-.33) node[left]{B} -- (g.input 2);\draw[-Latex,accent,very thick] (g.output)--(2.85,0) node[right]{X};\end{tikzpicture} & \LAT{$X=\overline{A+B}$} & \B{OR-এর পর NOT} & \begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&0\end{tabular}\\\hline
\B{NAND} & \begin{tikzpicture}[scale=0.62,thick,every node/.style={font=\scriptsize}]\node[nand gate US, draw=clrDarkOrange, very thick, fill=white, logic gate inputs=nn] (g) at (1.2,0) {};\draw[-Latex,clrBlue,very thick] (-.5,.33) node[left]{A} -- (g.input 1);\draw[-Latex,clrBlue,very thick] (-.5,-.33) node[left]{B} -- (g.input 2);\draw[-Latex,accent,very thick] (g.output)--(2.85,0) node[right]{X};\end{tikzpicture} & \LAT{$X=\overline{A\cdot B}$} & \B{AND-এর পর NOT} & \begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&0\end{tabular}\\\hline
\B{XOR} & \begin{tikzpicture}[scale=0.62,thick,every node/.style={font=\scriptsize}]\node[xor gate US, draw=clrPurple, very thick, fill=white, logic gate inputs=nn] (g) at (1.2,0) {};\draw[-Latex,clrBlue,very thick] (-.5,.33) node[left]{A} -- (g.input 1);\draw[-Latex,clrBlue,very thick] (-.5,-.33) node[left]{B} -- (g.input 2);\draw[-Latex,accent,very thick] (g.output)--(2.85,0) node[right]{X};\end{tikzpicture} & \LAT{$X=A\oplus B$} & \B{ইনপুট ভিন্ন হলে ১} & \begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&0\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&0\end{tabular}\\\hline
\B{XNOR} & \begin{tikzpicture}[scale=0.62,thick,every node/.style={font=\scriptsize}]\node[xnor gate US, draw=clrIndigo, very thick, fill=white, logic gate inputs=nn] (g) at (1.2,0) {};\draw[-Latex,clrBlue,very thick] (-.5,.33) node[left]{A} -- (g.input 1);\draw[-Latex,clrBlue,very thick] (-.5,-.33) node[left]{B} -- (g.input 2);\draw[-Latex,accent,very thick] (g.output)--(2.85,0) node[right]{X};\end{tikzpicture} & \LAT{$X=\overline{A\oplus B}$} & \B{ইনপুট একই হলে ১} & \begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&1\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}
\normalsize
\itm{1} \B{ইউনিভার্সাল গেইট: NAND ও NOR দিয়ে সব মৌলিক গেইট তৈরি করা যায়।}
\itm{2} \B{XOR: ইনপুট ভিন্ন হলে ১, একই হলে ০; হাফ অ্যাডারে ব্যবহৃত।}

\chsecfull{১০ক. হাফ অ্যাডার ও ফুল অ্যাডার (Half Adder \& Full Adder)}
\noindent\scriptsize
\begin{center}
\begin{adjustbox}{max width=\textwidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.13\textwidth}|>{\raggedright\arraybackslash}p{0.25\textwidth}|>{\centering\arraybackslash}p{0.34\textwidth}|>{\centering\arraybackslash}p{0.20\textwidth}|}
\hline
\rowcolor{tblhdr}\B{বর্তনী} & \B{সূত্র ও কাজ} & \B{রঙিন ডেটা-ফ্লো সার্কিট} & \B{সত্য সারণি} \\\hline
\B{হাফ অ্যাডার} & \B{দুটি বিট A ও B যোগ করে Sum ও Carry দেয়।}\par\LAT{$S=A\oplus B$}\par\LAT{$C=A\cdot B$} &
\begin{tikzpicture}[scale=0.55,thick,every node/.style={font=\scriptsize}]
\node[xor gate US, draw=clrPurple, very thick, fill=white, logic gate inputs=nn] (x) at (2.2,.75) {};
\node[and gate US, draw=clrDarkGreen, very thick, fill=white, logic gate inputs=nn] (a) at (2.2,-.85) {};
\draw[clrBlue,very thick] (-.45,1.10) node[left]{A} -- (.65,1.10) |- (x.input 1);
\draw[clrBlue,very thick] (-.45,-.15) node[left]{B} -- (.65,-.15) |- (x.input 2);
\draw[clrDarkGreen,very thick] (.65,1.10) |- (a.input 1);
\draw[clrDarkGreen,very thick] (.65,-.15) |- (a.input 2);
\draw[-Latex,accent,very thick] (x.output)--(4.15,.75) node[right]{S};
\draw[-Latex,clrDarkGreen,very thick] (a.output)--(4.15,-.85) node[right]{C};
\end{tikzpicture} &
\begin{tabular}{cc|cc}\rowcolor{tblhdr}A&B&S&C\\\hline\rowcolor{tblalt}0&0&0&0\\0&1&1&0\\\rowcolor{tblalt}1&0&1&0\\1&1&0&1\end{tabular} \\\hline
\B{ফুল অ্যাডার} & \B{A, B ও পূর্ববর্তী ক্যারি $C_{in}$ যোগ করে Sum ও $C_{out}$ দেয়।}\par\LAT{$S=A\oplus B\oplus C_{in}$}\par\LAT{$C_{out}=AB+AC_{in}+BC_{in}$} &
\begin{tikzpicture}[scale=0.52,thick,every node/.style={font=\scriptsize}]
\node[draw=clrBlue, very thick, fill=shape2!70, rounded corners, minimum width=1.05cm] (ha1) at (1.15,.72) {HA1};
\node[draw=clrDarkGreen, very thick, fill=shape3!70, rounded corners, minimum width=1.05cm] (ha2) at (2.85,.72) {HA2};
\node[or gate US, draw=clrOrange, very thick, fill=white, logic gate inputs=nn] (or) at (4.35,-.48) {};
\draw[-Latex,clrBlue,very thick] (-.55,1.08) node[left]{A} -- (ha1.west);
\draw[-Latex,clrBlue,very thick] (-.55,.36) node[left]{B} -- (ha1.west);
\draw[-Latex,accent,very thick] (ha1.east)--(ha2.west);
\draw[-Latex,clrPurple,very thick] (-.55,-.18) node[left]{$C_{in}$} -| (ha2.south);
\draw[-Latex,accent,very thick] (ha2.east)--(5.35,.72) node[right]{S};
\draw[-Latex,clrDarkGreen,very thick] (ha1.south) |- (or.input 2);
\draw[-Latex,clrDarkGreen,very thick] (ha2.south) |- (or.input 1);
\draw[-Latex,clrOrange,very thick] (or.output)--(5.35,-.48) node[right]{$C_{out}$};
\end{tikzpicture} &
\begin{tabular}{ccc|cc}\rowcolor{tblhdr}A&B{$C_{in}$}&S&{$C_{out}$}\\\hline\rowcolor{tblalt}0&0&0&0&0\\0&0&1&1&0\\\rowcolor{tblalt}0&1&0&1&0\\0&1&1&0&1\\\rowcolor{tblalt}1&0&0&1&0\\1&0&1&0&1\\\rowcolor{tblalt}1&1&0&0&1\\1&1&1&1&1\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}
\normalsize
\vspace{2pt}
\pagebreak
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
\B{Ordered list type:} \LAT{type="1"$\to$1,2,3}; \LAT{"I"$\to$I,II,III}; \LAT{"i"$\to$i,ii,iii}; \LAT{"a"$\to$a,b,c}; \LAT{"A"$\to$A,B,C}

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
\LAT{<li>} & \B{তালিকার আইটেম;} \LAT{value} \B{(ol-এ)} \\
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

\bigskip\par\noindent\rule{\linewidth}{0.6pt}\par\bigskip
\begin{center}
\noindent{\bfseries\large\B{অধ্যায় ১ (তথ্য ও যোগাযোগ প্রযুক্তি) — বিস্তারিত নোট}}
\end{center}
\vspace{2pt}
\begin{multicols}{2}

\chsec{বিশ্বগ্রাম (Global Village)}
\itm{1} \B{ধারণা:} \B{প্রযুক্তদের মাধ্যমে বিশ্বকে একটি ক্ষুদ্র গ্রামের মতো একসূত্রে সংযুক্ত করাকে বিশ্বগ্রাম বলে।}
\itm{2} \B{প্রবক্তা:} \B{টরেন্টো বিশ্ববিদ্যালয়ের ইংরেজি বিভাগের অধ্যাপক মার্শাল ম্যাকলুহান, ১৯৬২ সালে প্রথম ব্যবহার করেন।}
\itm{3} \B{মূল ভিত্তি:} \B{কানেক্টিভিটি বিশ্বগ্রামের মূল ভিত্তি; তথ্য বা ডেটা বিশ্বগ্রামের মূল চালিকা শক্তি।}
\chsub{}{বিশ্বগ্রাম প্রতিষ্ঠার উপাদানসমূহ}
\itm{1} \B{হার্ডওয়্যার} \sub{2} \B{সফটওয়্যার} \sub{3} \B{নেটওয়ার্ক সংযুক্তি} \sub{4} \B{ডেটা} \sub{5} \B{মানুষের সক্ষমতা}
\chsub{}{বিশ্বগ্রাম প্রতিষ্ঠার লক্ষ্য ও উদ্দেশ্য}
\itm{1} \B{পৃথিবীর বিভিন্ন প্রান্তের মানুষকে একই সুযোগ-সুবিধা সমৃদ্ধ সমাজের অন্তর্ভুক্ত করা}
\itm{2} \B{বিশ্বের বিভিন্ন দেশের উদ্ভূত সমস্যা ও সমস্যা থেকে উত্তরণের জন্য জনমত গড়ে তোলা}
\itm{3} \B{বিশ্বের বিভিন্ন সম্প্রদায়ের মধ্যে সাংস্কৃতিক তথ্য আদান-প্রদান}
\itm{4} \B{বিভিন্ন দেশের পেশাজীবীদের মধ্যে পারস্পরিক যোগাযোগ স্থাপন করা}
\itm{5} \B{প্রযুক্তি নির্ভর বিজ্ঞানমনস্ক জনসম্পদ তৈরির মাধ্যমে বিজ্ঞানভিত্তিক নেতৃত্ব গড়ে তোলা}
\chsub{}{বিশ্বগ্রামের সুবিধাসমূহ}
\itm{1} \B{মানুষের কর্মদক্ষতা ও গতি বৃদ্ধি পায়} \sub{2} \B{অনলাইনে কেনাকাটার সুবিধা}
\itm{3} \B{বিশ্বের প্রতি মুহূর্তের খবর ঘরে বসেই পাওয়া যায়} \sub{4} \B{বিভিন্ন দেশের সাংস্কৃতিক তথ্যাদি বিনিময়}
\itm{5} \B{বিশ্ব জনমত গড়ে তোলা সহজ} \sub{6} \B{জীবনযাত্রার মান উন্নত হয়}
\itm{7} \B{বিষয়ের গবেষণা করা যায় ও ফলাফল জানা যায়} \sub{8} \B{উন্নত চিকিৎসাসেবা পাওয়া যায়}
\itm{9} \B{উন্নত যোগাযোগ সুবিধা} \sub{10} \B{অনলাইন লাইব্রেরির সুবাদে শিক্ষার প্রসার}
\chsub{}{বিশ্বগ্রামের অসুবিধাসমূহ}
\itm{1} \B{তথ্যের গোপনীয়তা রক্ষা করা যায় না} \sub{2} \B{ইন্টারনেটে অবাধ ব্যবহারের কারণে অনৈতিক কাজ বৃদ্ধি}
\itm{3} \B{হ্যাকিং-এর মাধ্যমে গোপনীয় তথ্য চুরি} \sub{4} \B{ব্যাংকের হিসাব হ্যাক করে বিপুল অর্থ আত্মসাৎ}
\itm{5} \B{আইসিটি স্কিল না থাকায় প্রয়োজনীয় কাজ যথাসময়ে সম্পন্ন করা যায় না}
\chsub{}{বিশ্বগ্রামের প্রধান উপাদানসমূহ (সেবা)}
\itm{1} \B{যোগাযোগ:} \B{কথন, লিখন বা অন্য মাধ্যমে তথ্যের আদান-প্রদানই যোগাযোগ}
\itm{2} \B{ইন্টারনেট:} \B{বিশ্বগ্রাম প্রতিষ্ঠায় সর্বাধিক অবদান রাখা উপাদান}
\itm{3} \B{ই-মেইল:} \B{ইলেকট্রনিক মেইল বা বার্তা আদান-প্রদানের পদ্ধতি}
\itm{4} \B{টেলিকনফারেন্সিং:} \B{টেলিযোগাযোগের মাধ্যমে দুই বা বহু ভৌগোলিক অবস্থানে সভা আয়োজন}
\itm{5} \B{ভিডিও কনফারেন্সিং:} \B{অডিও ও ভিডিওর সমন্বয়ে যোগাযোগ করার প্রক্রিয়া}
\itm{6} \B{আউটসোর্সিং:} \B{ভিন্ন দেশের নাগরিক দিয়ে দূর থেকে কাজ করানোর কার্যক্রম}
\itm{7} \B{ফ্রিল্যান্সিং:} \B{স্বাধীনভাবে নিজের দক্ষতা অনুসারে কাজ করে অর্থ উপার্জনের প্রক্রিয়া}
\itm{8} \B{ই-বুক, ই-লার্নিং, ই-কমার্স, টেলিমেডিসিন} \B{ইত্যাদি}

\chsec{ভার্চুয়াল রিয়ালিটি (VR)}
\B{ভার্চুয়াল রিয়ালিটি হলো হার্ডওয়্যার ও সফটওয়্যারের মাধ্যমে তৈরিকৃত এমন এক ধরনের কৃত্রিম পরিবেশ, যা ব্যবহারকারীর কাছে বাস্তব পরিবেশ বলে মনে হয়। মডেলিং ও সিমুলেশন পদ্ধতি ব্যবহারের মাধ্যমে মানুষ কল্পনার জগতে প্রবেশ করে।}
\itm{1} \B{ভার্চুয়াল রিয়েলিটির ৩টি গুরুত্বপূর্ণ বিষয়:} \B{দৃষ্টি, শব্দ ও স্পর্শ}
\chsub{}{ভার্চুয়াল রিয়েলিটির নেতিবাচক দিক}
\itm{1} \B{De-Humanisation বা মনুষ্যত্বহীনতা বৃদ্ধি; সামাজিকতা থেকে দূরে সরে যাওয়া}
\itm{2} \B{বাস্তব জগৎ থেকে দূরে সরে বাস্তবের চেয়ে বেশিরভাগ সময় কল্পনার জগতে বিচরণ}
\itm{3} \B{দৃষ্টিশক্তি ও শ্রবণশক্তি ক্ষতিগ্রস্ত হয়}

\chsec{রোবটিক্স (Robotics)}
\itm{1} \B{রোবট শব্দের অর্থ যন্ত্রমানব; স্বয়ংক্রিয়ভাবে নিয়ন্ত্রিত প্রোগ্রামযুক্ত যন্ত্র}
\itm{2} \B{উৎপত্তি:} \B{চেক ভাষার Robota শব্দ থেকে, অর্থ `Forced labour' (শ্রমিক)}
\itm{3} \B{রোবোটিক্স:} \B{রোবটের নকশা, গঠন, বৈশিষ্ট্য ও কাজ নিয়ে আলোচনার শাখা}
\chsub{}{রোবটকে যেসব বৈশিষ্ট্য দেওয়ার চেষ্টা করা হয়}
\itm{1} \B{দর্শনেন্দ্রিয় উপলব্ধি (Visual Perception)} \sub{2} \B{সংস্পর্শ বা স্পর্শনেন্দ্রিয়গ্রাহ্য সক্ষমতা (Tactile)}
\itm{3} \B{নিয়ন্ত্রণ ও ম্যানিপুলেশন দক্ষতা (Dexterity)} \sub{4} \B{স্থান পরিবর্তনে দৈহিক নড়াচড়ার ক্ষমতা (Locomotion)}
\chsub{}{রোবোটিক্সের গুরুত্ব ও ব্যবহার}
\itm{1} \B{খনি থেকে আহরণে} \sub{2} \B{দুর্গমস্থানে কাজের ক্ষেত্রে}
\itm{3} \B{যানবাহন ও গাড়ির কারখানায়} \sub{4} \B{ঘরের কাজে (গৃহস্থালি)}
\itm{5} \B{বিরক্তিকর ও একঘেয়ে কাজের ক্ষেত্রে} \sub{6} \B{চিকিৎসাক্ষেত্রে সার্জারির কাজে}
\itm{7} \B{দুর্যোগে নিরাপত্তা ব্যবস্থাপনা নিয়ন্ত্রণে} \sub{8} \B{CAM (Computer Aided Manufacturing)-এ}
\itm{9} \B{মহাকাশ স্টেশন স্থাপনে (নাসার রিসিকুইটি রোভার)}
\chsub{}{রোবট ব্যবহারের অসুবিধাসমূহ}
\itm{1} \B{তৈরির প্রাথমিক খরচ বেশি} \sub{2} \B{স্বাধীনভাবে চিন্তা করতে পারে না}
\itm{3} \B{ভুল থেকে শিক্ষা নিতে পারে না} \sub{4} \B{জটিল সিদ্ধান্ত গ্রহণে সক্ষম নয়}
\itm{5} \B{ইচ্ছেমতো বিভিন্ন কাজ করানো যায় না}

\chsec{ক্রায়োসার্জারি (Cryosurgery)}
\B{যে প্রক্রিয়ায় শীতল তাপমাত্রার মাধ্যমে শরীরের অস্বাভাবিক ও অসুস্থ টিস্যু ধ্বংস করা হয় তাকে ক্রায়োসার্জারি বলে। বিভিন্ন গ্যাসের সাহায্যে তাপমাত্রা $-41^{\circ}$C থেকে $-196^{\circ}$C-এ নামানো হয়, ফলে কোষের পানি জমাট বেঁধে টিস্যুটি বরফপিণ্ডে পরিণত হয় ও ধ্বংস হয়ে যায়।}
\itm{1} \B{ক্রায়োজেনিক এজেন্ট/পদার্থ:} \B{তরল নাইট্রোজেন, কার্বন-ডাই-অক্সাইড, আর্গন ও ডাই মিথাইল ইথার প্রোপেন; হিটিং সোর্স: হিলিয়াম}
\itm{2} \B{ক্রায়োপ্রোব:} \B{ফাঁপা নল বা যন্ত্র যার মাধ্যমে ক্রায়োসার্জারি করা হয়}
\chsub{}{ক্রায়োসার্জারির সুবিধা}
\itm{1} \B{বারবার করা সম্ভব} \sub{2} \B{কোনো পার্শ্বপ্রতিক্রিয়া নেই}
\itm{3} \B{অন্যান্য চিকিৎসা পদ্ধতির তুলনায় খরচ কম} \sub{4} \B{অন্যান্য সার্জারির চেয়ে কষ্টদায়ক ও রক্তক্ষরণ কম}
\chsub{}{ক্রায়োসার্জারির অসুবিধা}
\itm{1} \B{দীর্ঘকালীন কার্যকারিতা নিয়ে অনিশ্চয়তা} \sub{2} \B{ইনফেকশন হওয়ার সম্ভাবনা}
\itm{3} \B{অত্যধিক রক্তক্ষরণ হতে পারে} \sub{4} \B{লিভার/ফুসফুসের নরমাল স্ট্রাকচার নষ্ট হতে পারে}
\itm{5} \B{ত্বকের ক্যান্সারের চিকিৎসায় ফুলে যায়}

\end{multicols}


\begin{multicols}{2}
\chsec{বায়োমেট্রিক্স (Biometrics)}
\B{মানুষের দৈহিক গঠন বা আচরণগত বৈশিষ্ট্য পরিমাপের ভিত্তিতে কোনো ব্যক্তিকে অদ্বিতীয়ভাবে শনাক্ত করার প্রযুক্তিকে বায়োমেট্রিক্স বলে। বায়োমেট্রিক্স দুই ধরনের: (i) শারীরবৃত্তীয় বায়োমেট্রিক্স (ii) আচরণগত বায়োমেট্রিক্স।}
\chsub{}{শারীরবৃত্তীয় বায়োমেট্রিক্স}
\itm{1} \B{আঙ্গুলের ছাপ শনাক্তকরণ (Fingerprint Reader):} \B{ফিঙ্গারপ্রিন্ট রিডারে চাপ দেওয়ার পর ছবি ডেটাবেজে জমা করা হয়, বিন্যাস-পুরুত্ব-ইত্যাদির ভিত্তিতে ইলেকট্রোম্যাগনেটিক পদ্ধতিতে চাপ চিত্র তৈরি হয়}
\itm{2} \B{হাতের রেখা শনাক্তকরণ:} \B{হাতের আকার, রেখার বিন্যাস, পুরুত্ব, আঙ্গুলের দৈর্ঘ্য বিশ্লেষণ করা হয়}
\itm{3} \B{আইরিশ শনাক্তকরণ:} \B{চোখের মণির চারপাশে বলয় বা আইরিশ বিশ্লেষণ; নির্ভরযোগ্যতা বেশি}
\itm{4} \B{মুখের অবয়ব শনাক্তকরণ:} \B{পুরো মুখের ছবি তুলে শনাক্ত করা হয়}
\itm{5} \B{ডিএনএ (DNA) পর্যবেক্ষণ}
\chsub{}{আচরণগত বায়োমেট্রিক্স}
\itm{1} \B{কণ্ঠস্বর যাচাইকরণ:} \B{মাইক্রোফোনের মাধ্যমে ধ্বনি ধরে কম্পিউটার প্রোগ্রামিং-এর সাহায্যে ডেটাবেজে সংরক্ষণ ও তুলনা করা হয়}
\itm{2} \B{হাতের স্বাক্ষর যাচাইকরণ:} \B{আকার, ধরন, লেখার গতি, সময়, কলম চাপ যাচাই করা হয়}
\itm{3} \B{কিবোর্ড টাইপিং স্পিড শনাক্তকরণ:} \B{ইনপুট ডিভাইসে গোপনীয় কোড টাইপ করার গতি ও সময় মিলিয়ে শনাক্ত করা হয়}
\chsub{}{বায়োমেট্রিক্স প্রক্রিয়া}
\B{নির্দিষ্ট ব্যক্তির বায়োমেট্রিক ডেটা (আঙুলের ছাপ, চোখের রেটিনা, আইরিশ, কণ্ঠস্বর ইত্যাদি) স্ক্যান করে ভেরিফিকেশনের জন্য ডেটাবেজে রাখা হয়। ভেরিফিকেশনের সময় নতুন স্ক্যান করা ডেটা পূর্বের ডেটার সাথে মিলিয়ে দেখা হয়; মিলে গেলে সিস্টেমটি ব্যক্তিকে চিনতে পারে, না মিললে চিনতে পারে না।}

\chsec{বায়োইনফরমেটিক্স (Bioinformatics)}
\B{জীববিজ্ঞান, কম্পিউটার সায়েন্স, ইনফরমেশন ইঞ্জিনিয়ারিং, গণিত এবং পরিসংখ্যানের সমন্বয়ে গঠিত একটি বিষয়। এটি ৪টি ভিন্ন শাখার উপাদানে গঠিত:}
\itm{1} \B{আণবিক জীববিদ্যা ও মেডিসিন:} \B{ডেটা উৎস বিশ্লেষণের কাজ করে}
\itm{2} \B{ডেটাবেজ:} \B{নিরাপদ ডেটা সংরক্ষণ ও ডেটা বিতরণ করা}
\itm{3} \B{প্রোগ্রাম:} \B{উৎস বিশ্লেষণ অ্যালগরিদম যার মাধ্যমে বায়োইনফরমেটিক্স কঠোরভাবে সুনির্দিষ্ট হয়}
\itm{4} \B{গণিত ও পরিসংখ্যান:} \B{সম্ভাব্যতা যাচাই করা হয়}
\chsub{}{বায়োইনফরমেটিক্সের ব্যবহার}
\itm{1} \B{জিনোম সিকোয়েন্স, প্রোটিন সিকোয়েন্স ইত্যাদি গঠন উপাদানের ইলেকট্রনিক ডেটাবেজ গঠনে}
\itm{2} \B{মলিকুলার মেডিসিন, জিনথেরাপি, ঔষধ তৈরিতে, বর্জ্য পরিষ্কারকরণে, জলবায়ু পরিবর্তন গবেষণায়}
\itm{3} \B{বিকল্প শক্তির উৎস সন্ধানে, ডিএনএ ম্যাপিং ও অ্যানালাইসিস, জিন ফাইন্ডিং, প্রোটিনের মিথস্ক্রিয়া বিশ্লেষণে}
\chsub{}{বায়োইনফরমেটিক্স এর সুবিধা}
\itm{1} \B{আণবিক বংশগতিবিদ্যার উন্নয়নে ব্যাপক ভূমিকা পালন করে}
\itm{2} \B{জীববিজ্ঞান ভিত্তিক তথ্যের গবেষণাতে তথ্যের সংরক্ষণ ও পুনঃব্যবহার নিশ্চিত করে}
\chsub{}{বায়োইনফরমেটিক্স এর অসুবিধা}
\itm{1} \B{জেনেটিক তথ্যের গোপনীয়তা ভঙ্গের আশঙ্কা থাকে}
\itm{2} \B{বায়োমেট্রিক্স নির্ভর সেবা সুনিয়ন্ত্রিতভাবে পরিচালনা না করলে রোগীর বড় ধরনের ক্ষতির সম্ভাবনা থাকে}
\itm{3} \B{এটি একটি ব্যয়বহুল প্রক্রিয়া}

\chsub{}{বায়োমেট্রিক্স ও বায়োইনফরমেটিক্স এর পার্থক্য}
\end{multicols}
\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.06\linewidth}|X|X|}
\hline
\rowcolor{tblhdr} & \B{বায়োমেট্রিক্স} & \B{বায়োইনফরমেটিক্স} \\\hline
i & \B{মানুষের দৈহিক গঠন, আচরণ, বৈশিষ্ট্য, গুণাগুণ চিহ্নিত করে শনাক্ত করার প্রযুক্তি} & \B{জীববিজ্ঞানের সমস্যাগুলো কম্পিউটেশনাল প্রযুক্তি ব্যবহার করে সমাধান করার প্রক্রিয়া} \\\hline
ii & \B{ব্যক্তি শনাক্তকরণ ও নিযুক্ত নিরাপত্তার জন্য ব্যবহৃত হয়} & \B{মলিকুলার বা আনবিক জেনেটিক্স এর ভিজুয়ালাইজেশন সম্ভব করে তুলতে ব্যবহৃত হয়} \\\hline
iii & \B{ফিঙ্গারপ্রিন্ট, ডিএনএ, চোখের আইরিশ, কণ্ঠস্বর ইত্যাদি পরিমাপ ও বিশ্লেষণ করে শনাক্তকরণ করা হয়} & \B{বায়োলজিকাল ডেটা অ্যানালাইসিস করার জন্য কম্পিউটার প্রযুক্তি, ইনফরমেশন থিওরি ও গাণিতিক জ্ঞানকে ব্যবহার করা হয়} \\\hline
iv & \B{এটি তুলনামূলক কম ব্যয়বহুল ও বেশি ব্যবহৃত হয়} & \B{এটি অত্যন্ত ব্যয়বহুল। প্রকল্প চালিয়ে যেতে প্রচুর অর্থের প্রয়োজন পড়ে} \\\hline
\end{tabularx}
\vspace{3pt}
\begin{multicols}{2}

\chsec{ন্যানো টেকনোলজি (Nano Technology)}
\B{বিজ্ঞান ও প্রযুক্তি ব্যবহার করে এক থেকে একশ ন্যানো মিটার আকৃতির কোনো কিছু তৈরি করা এবং ব্যবহার করাকে ন্যানো টেকনোলজি বলে। এই আকৃতির কোনো কিছু তৈরি করা হলে তাকে ন্যানো পার্টিকেল বলে। $10^{-9}$ m কে ন্যানো মিটার বলে। ন্যানো টেকনোলজি দুই ভাগে বিভক্ত:}
\itm{1} \B{ক্ষুদ্র থেকে বৃহৎ (Bottom to Top):} \B{ক্ষুদ্র হতে ক্ষুদ্র আণবিক উপাদান থেকে বড় কোনো জিনিস তৈরি করা}
\itm{2} \B{বৃহৎ থেকে ক্ষুদ্র (Top to Bottom):} \B{বৃহৎ কোনো জিনিসকে ভেঙে ভেঙে ক্ষুদ্র ক্ষুদ্র ভাবে বিভক্ত করা}
\chsub{}{ন্যানো টেকনোলজি ব্যবহারের ক্ষেত্র}
\itm{1} \B{কম্পিউটার হার্ডওয়্যারে:} \B{প্রসেসরের উচ্চগতি, দীর্ঘস্থায়িত্ব ও কম খরচ}
\itm{2} \B{চিকিৎসাক্ষেত্রে:} \B{ন্যানো রোবট ব্যবহার করে অপারেশন, ক্রায়োসার্জারি, ডায়াগনোসিস, কেমোথেরাপি, কলোনোস্কপি, এনজিওগ্রাম করা হয়}
\itm{3} \B{খাদ্যশিল্পে:} \B{দ্রব্য প্যাকেটিং, খাদ্য সংরক্ষণে}
\itm{4} \B{জ্বালানিক্ষেত্রে:} \B{হাইড্রোজেন আয়ন থেকে ফুয়েল সেল তৈরি, সৌরবিদ্যুৎ উৎপাদনে}
\itm{5} \B{যোগাযোগক্ষেত্রে:} \B{হালকা ওজনের ও কম জ্বালানি চাহিদা সম্পন্ন গাড়ি তৈরিতে}
\itm{6} \B{খেলাধুলার সামগ্রীক্ষেত্রে:} \B{ক্রিকেট, টেনিস বলের স্থায়িত্ব ও গলফ বা ফুটবল বলের ভারসাম্য রক্ষায়}
\itm{7} \B{বায়ু ও পানি দূষণ রোধে:} \B{শিল্প কারখানার ক্ষতিকর রাসায়নিক বর্জ্যকে ন্যানো পার্টিকেল ব্যবহার করে নিষ্কাশিত করা হয়}
\itm{8} \B{প্রসাধন শিল্পে:} \B{জিংক অক্সাইড এর ন্যানো পার্টিকেল যুক্ত হওয়ায় ত্বকের ক্যান্সার রোধ}
\chsub{}{ন্যানো টেকনোলজির সুবিধা}
\B{উৎপাদিত পণ্য অত্যন্ত মজবুত, টেকসই, আকারে ছোট ও হালকা হয়}
\chsub{}{ন্যানো টেকনোলজির অসুবিধা}
\itm{1} \B{ন্যানো পার্টিকেল দিয়ে প্রাণঘাতি অস্ত্র তৈরি, প্রচলিত জ্বালানি গ্যাস/তেলের বিকল্প হিসেবে অপব্যবহার হতে পারে}
\itm{2} \B{এই প্রযুক্তির ক্ষেত্রে অদক্ষরা কর্মহীন হয়ে পড়ে}

\chsec{জেনেটিক ইঞ্জিনিয়ারিং}
\itm{1} \B{DNA-এর পূর্ণরূপ:} \LAT{Deoxyribo Nucleic Acid}
\itm{2} \B{ডিএনএ-এর ভিতর ক্ষুদ্র ক্ষুদ্র অংশ যা প্রাণীর জীবনের বৈশিষ্ট্য বহন করে ও পরের প্রজন্মে বহন করে তাকে জিন বলে}
\itm{3} \B{জিন হলো বংশগতির ধারক ও বাহক; মানবদেহে ২০,০০০--৩০,০০০ জিন রয়েছে}
\itm{4} \B{একসেট জিনকে জিনোম বলে; জিনোম হলো জীবের বৈশিষ্ট্যের নকশা বা বিন্যাস}
\itm{5} \B{গবেষণার মাধ্যমে একটি জিন পরিবর্তন করে সেখানে অন্য জিন লাগানো হলে তাকে রিকম্বিনেন্ট ডিএনএ (RDNA) বলে}
\itm{6} \B{RDNA সমৃদ্ধ জীব কোষকে Genetically Modified Organism (GMO) বলে}
\itm{7} \B{E.coli ব্যাকটেরিয়া এবং ইস্ট হতে মানবদেহের ইনসুলিন তৈরি করা হয়; হরমোন বৃদ্ধি ও বামনত্ব বৃদ্ধি করা হয়}
\itm{8} \B{ভাইরাসজনিত রোগ, ক্যান্সার, এইডস ইত্যাদি চিকিৎসায় জিন প্রযুক্তি ব্যবহার করা হয়}
\itm{9} \B{ধান গবেষণায় ইনস্টিটিউট উচ্চ ফলনশীল ব্রি (BRRI) জাতের বিভিন্ন বীজ উদ্ভাবন করা হয়}
\end{multicols}


\bigskip\par\noindent\rule{\linewidth}{0.6pt}\par\bigskip
\begin{center}
\noindent{\bfseries\large\B{অধ্যায় ২ (কমিউনিকেশন সিস্টেমস ও নেটওয়ার্কিং) — বিস্তারিত নোট}}
\end{center}
\vspace{2pt}
\begin{multicols}{2}

\chsec{কমিউনিকেশন সিস্টেম ও ডেটা কমিউনিকেশন}
\itm{1} \B{কমিউনিকেশন:} \B{আদান-প্রদান বা বিনিময়; এক স্থান থেকে অন্য স্থানে বা এক যন্ত্র থেকে অন্য যন্ত্রে তথ্য বিনিময়কে কমিউনিকেশন বলে}
\itm{2} \B{ডেটা কমিউনিকেশন সিস্টেম:} \B{বিভিন্ন স্থানে অবস্থিত কম্পিউটার হতে কম্পিউটারে অথবা কম্পিউটার ও অন্য কোনো ডিভাইসে ডেটা ও তথ্য আদান-প্রদান করা হয় যে পদ্ধতিতে}
\itm{3} \B{শর্ত:} \B{সব ডেটা কমিউনিকেশনই কমিউনিকেশন, কিন্তু সব কমিউনিকেশন ডেটা কমিউনিকেশন নয়; ডিভাইস ব্যবহৃত হতে হবে}

\chsec{মডেম (Modem)}
\B{ডেটা কমিউনিকেশন সিস্টেমে অ্যানালগ সংকেত ও ডিজিটাল সংকেতের মধ্যে পরস্পর পরিবর্তনের জন্য যে ডিভাইস ব্যবহৃত হয় তাকে মডেম বলে।}
\itm{1} \B{Mo $\to$ Modulation $\to$ (Analog $\to$ Digital) Convert}
\itm{2} \B{Dem $\to$ Demodulation $\to$ (Digital $\to$ Analog) Convert}

\chsec{প্রোটোকল (Protocol)}
\B{প্রোটোকল হলো এক গুচ্ছ নিয়ম-নীতি যা কমিউনিকেশন ডিভাইসগুলো সর্বদা মেনে চলে। যেমন: TCP/IP, HTTP, FTP।}

\chsec{ডেটা কমিউনিকেশনের উপাদান (৫টি)}
\itm{1} \B{উৎস বা সোর্স:} \B{বার্তা প্রেরকের কাছে পাঠানোর যন্ত্র; যেমন: মাইক্রোফোন, ক্যামেরা, কী-বোর্ড, কম্পিউটার, মোবাইল}
\itm{2} \B{প্রেরক বা ট্রান্সমিটার:} \B{বার্তা কমিউনিকেশন চ্যানেলের মাধ্যমে পাঠায়; যেমন: বেতার কেন্দ্র, রাউটার, টেলিভিশন, মডেম}
\itm{3} \B{কমিউনিকেশন চ্যানেল/মাধ্যম/মিডিয়াম:} \B{যার মধ্য দিয়ে ডেটা এক স্থান হতে অন্য স্থানে যায়; যেমন: তার, ক্যাবল, পাবলিক টেলিফোন লাইন, তারবিহীন মাধ্যম}
\itm{4} \B{রিসিভার/গ্রহক/প্রাপক:} \B{যার কাছে ডেটা পাঠানো হয়; যেমন: টেলিফোন, এক্সচেঞ্জ, মডেম, রাউটার}
\itm{5} \B{গন্তব্য বা ডেস্টিনেশন:} \B{গ্রহক থেকে প্রাপ্ত ডেটা সর্বশেষ যে যন্ত্রে প্রেরণ করা হয়; যেমন: লাউডস্পিকার, টেলিফোন, কম্পিউটার}

\chsec{ডেটা ট্রান্সমিশন স্পীড ও বিপিএস}
\itm{1} \B{ব্যান্ডউইথ/ডেটা ট্রান্সমিশন স্পীড:} \B{প্রতি সেকেন্ডে এক স্থান থেকে অন্য স্থানে যত ডেটা স্থানান্তরিত হয়}
\itm{2} \B{bps (bit per second):} \B{ব্যান্ডউইথের ক্ষুদ্রতম একক; প্রতি সেকেন্ডে কতটি বিট পরিবাহিত হচ্ছে তার পরিমাপ}
\itm{3} \B{Kbps:} \B{প্রতি সেকেন্ডে ১,০০০ বিট} \sub{4} \B{Mbps:} \B{প্রতি সেকেন্ডে ১০,০০,০০০ বিট}
\itm{5} \B{Gbps:} \B{প্রতি সেকেন্ডে ১,০০,০০,০০,০০০ বিট}
\itm{6} \B{1 Byte = 8 bits} \sub{7} \B{1 KB = 1024 Bytes} \sub{8} \B{1 MB = 1024 KB}
\itm{9} \B{1 GB = 1024 MB} \sub{10} \B{1 TB = 1024 GB}

\chsec{ডেটা ট্রান্সমিশন মেথড}
\B{যে পদ্ধতিতে এক কম্পিউটার থেকে অন্য কম্পিউটারে ডেটা ট্রান্সমিট হয় তাকে ডেটা ট্রান্সমিশন মেথড বলে।}
\chsub{}{প্যারালাল ডেটা ট্রান্সমিশন মেথড}
\B{যে পদ্ধতিতে ডেটা সমান্তরালভাবে আদান-প্রদান হয় তাকে প্যারালাল ডেটা ট্রান্সমিশন বলে। একাধিক তারের মধ্য দিয়ে ৮, ১৬ বা ৩২ বিট ইত্যাদি ডেটা চলাচল করতে পারে। যেমন: তার/ক্যাবল, ইউএসবি পোর্ট, প্রিন্টারে ডেটা পাঠানোর জন্য এ পদ্ধতি ব্যবহৃত হয়।}
\itm{1} \B{সুবিধা --} \B{দ্রুতগতি সম্পন্ন; একসাথে অনেক বিট চলাচল করে; শব্দ বা ওয়ার্ড অনুসারে স্থানান্তরিত হয়}
\itm{2} \B{অসুবিধা --} \B{দূরত্ব বেশি হলে ব্যবহার করা সম্ভব নয়; প্রতিটি বিটের জন্য পৃথক তার প্রয়োজন হওয়ায় ব্যয়বহুল}
\chsub{}{সিরিয়াল ডেটা ট্রান্সমিশন মেথড}
\B{প্রেরক ও প্রাপকের মধ্যে ধারাবাহিকভাবে একটি বিটের পর অপর একটি বিট চলাচল করলে তাকে সিরিয়াল ডেটা ট্রান্সমিশন বলে। ১ বাইট বা ৮ বিটের ডেটা পর্যায়ক্রমে ১ বিট করে আদান-প্রদান করে। যেমন: মডেম, মাউস, কী-বোর্ড, ইউএসবি (USB) পোর্ট।}
\itm{1} \B{সুবিধা --} \B{স্থানান্তরের জন্য মাত্র ১টি লাইন প্রয়োজন; ট্রান্সমিশন লাইন দূর পর্যন্ত বিস্তৃত করা যায়; সিনক্রোনাইজেশনের প্রয়োজন হয় না}
\itm{2} \B{অসুবিধা --} \B{এটি ধীরগতি সম্পন্ন; একই সময়ে মাত্র একটি বিট স্থানান্তরিত হয়}
\end{multicols}

\noindent\scriptsize\setlength{\tabcolsep}{3pt}
\begin{tabularx}{\linewidth}{|X|>{\centering\arraybackslash}X|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tblhdr} \B{বিষয়} & \B{সিরিয়াল} & \B{প্যারালাল} \\\hline
\B{ডেটা} & \B{১ বিট} & \B{৮/১৬/৩২ বিট} \\\hline
\B{পথ} & \B{১টি} & \B{৮/১৬/৩২টি} \\\hline
\B{গতি} & \B{কম} & \B{বেশি} \\\hline
\B{খরচ} & \B{কম} & \B{বেশি} \\\hline
\end{tabularx}
\vspace{4pt}

\noindent
\begin{minipage}{0.48\linewidth}
\centering\footnotesize\B{Parallel Communication}\\[3pt]
\begin{tikzpicture}[scale=1.15,thick,every node/.style={font=\scriptsize}]
\draw[fill=shape2!35] (0,0) ellipse (0.45 and 1.1); \node at (0,0) {\B{প্রেরক}};
\draw[fill=shape3!35] (3.6,0) ellipse (0.45 and 1.1); \node at (3.6,0) {\B{গ্রাহক}};
\foreach \y/\c in {-0.75/shape1,-0.25/shape4,0.25/shape5,0.75/shape6}{\draw[-Latex,\c!80!black,thick] (0.45,\y) -- (3.15,\y);}
\node[font=\tiny] at (1.8,1.25) {\B{৮/১৬/৩২ বিট (একসাথে)}};
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.48\linewidth}
\centering\footnotesize\B{Serial Communication}\\[3pt]
\begin{tikzpicture}[scale=1.15,thick,every node/.style={font=\scriptsize}]
\draw[fill=shape2!35] (0,0) ellipse (0.45 and 1.1); \node at (0,0) {\B{প্রেরক}};
\draw[fill=shape3!35] (3.6,0) ellipse (0.45 and 1.1); \node at (3.6,0) {\B{গ্রাহক}};
\draw[-Latex,accent,very thick] (0.45,0) -- (3.15,0);
\foreach \x/\b in {0.8/1,1.3/0,1.8/1,2.3/1,2.8/0}{\node[font=\tiny,accent] at (\x,0.28) {\b};}
\node[font=\tiny] at (1.8,1.25) {\B{১টি বিট করে ধারাবাহিক}};
\end{tikzpicture}
\end{minipage}
\vspace{4pt}

\begin{multicols}{2}
\chsec{ক্লক পালস ও বিট সিনক্রোনাইজেশন}
\itm{1} \B{ক্লক পালস:} \B{ক্লকের প্রতি পালসে একটি করে বিট প্রেরণ ও গ্রহণ করা হয়; একটি ক্লক সংকেতের সক্রিয় অবস্থাকে বোঝানো হয়}
\itm{2} \B{বিট সিনক্রোনাইজেশন:} \B{সিরিয়াল ডেটা ট্রান্সমিশন পদ্ধতিতে সিগন্যাল পাঠানোর সময় বিটের শুরু ও শেষ বোঝার জন্য যে বিশেষ পদ্ধতি ব্যবহৃত হয়; এর কারণে প্রাপক সিগন্যাল থেকে ডেটা শনাক্ত ও পুনরুদ্ধার করতে পারে}
\itm{3} \B{বিট সিনক্রোনাইজেশনের উপর ভিত্তি করে সিরিয়াল ডেটা ট্রান্সমিশন তিন ভাগে বিভক্ত:} \B{(i) অ্যাসিনক্রোনাইজেশন (ii) সিনক্রোনাইজেশন (iii) আইসোক্রোনাইজেশন}

\chsub{}{অ্যাসিনক্রোনাস ডেটা ট্রান্সমিশন}
\B{যে ডেটা ট্রান্সমিশন সিস্টেমে প্রেরক যেকোনো সময় ক্যারেক্টার (বর্ণ, সংখ্যা বা চিহ্ন) বাই ক্যারেক্টার ট্রান্সমিট করে তাকে অ্যাসিনক্রোনাস ডেটা ট্রান্সমিশন বলে।}
\itm{1} \B{প্রেরক যেকোনো সময় ডেটা ট্রান্সমিট করতে পারে, গ্রহকও তা গ্রহণ করে}
\itm{2} \B{প্রতিটি ক্যারেক্টারের শুরুতে স্টার্ট বিট ও শেষে ১/২টি স্টপ বিট থাকে; ফলে ক্যারেক্টারের ডেটা ১০/১১ বিটে রূপান্তরিত হয়ে ট্রান্সমিট হয়}
\itm{3} \B{প্রাইমারি স্টোরেজ ডিভাইসের (Ram, Cache, CPU memory) প্রয়োজন হয় না}
\itm{4} \B{ব্যবহার:} \B{কীবোর্ড হতে কম্পিউটারে, কম্পিউটার হতে প্রিন্টারে, পাঞ্চকার্ড রিডার হতে কম্পিউটারে ডেটা স্থানান্তরে}
\itm{5} \B{সুবিধা:} \B{প্রেরক যেকোনো সময় স্থানান্তর করতে পারে, গ্রাহকও তা গ্রহণ করতে পারে; ইনস্টলেশন ব্যয় অত্যন্ত কম}
\itm{6} \B{অসুবিধা:} \B{ডেটা ট্রান্সমিশনে গতি অপেক্ষাকৃত ধীর}

\chsub{}{সিনক্রোনাস ডেটা ট্রান্সমিশন}
\B{যে ট্রান্সমিশন সিস্টেমে প্রেরক স্টেশনে প্রথমে ডেটাকে কোনো প্রাইমারি স্টোরেজ ডিভাইসে সংরক্ষণ করে নেয়া হয়। অতঃপর ডেটার ক্যারেক্টার সমূহকে ব্লক বা প্যাকেট বা ফ্রেম আকারে ভাগ করে প্রতিবারে একটি করে ব্লক ট্রান্সমিট করা হয়।}
\itm{1} \B{বিরতিহীনভাবে প্রেরক যন্ত্র থেকে গ্রহক যন্ত্রে ডেটা পাঠানো হয়}
\itm{2} \B{প্রতি ব্লকের শুরুতে ১-২ বাইটের হেডার তথ্য এবং শেষে ১-২ বাইটের ট্রেইলার তথ্য থাকে}
\itm{3} \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয়}
\itm{4} \B{ব্যবহার:} \B{কম্পিউটার হতে কম্পিউটারে, দূরবর্তী স্থানে ও একই সাথে অনেকগুলো কম্পিউটারে ডেটা স্থানান্তরে}
\itm{5} \B{সুবিধা:} \B{অবিরাম ট্রান্সমিশনের ফলে গতি অপেক্ষাকৃত বেশি; স্টার্ট/স্টপ বিটের প্রয়োজন হয় না; তুলনামূলক কম সময় লাগে}
\itm{6} \B{অসুবিধা:} \B{তুলনামূলকভাবে ব্যয়বহুল}

\chsub{}{আইসোক্রোনাস ডেটা ট্রান্সমিশন}
\B{অ্যাসিনক্রোনাস ও সিনক্রোনাসের মিশ্র পদ্ধতি; সিনক্রোনাস পদ্ধতির স্টার্ট ও স্টপ বিটের মাঝখানে সিনক্রোনাস পদ্ধতিতে ব্লক আকারে ডেটা ট্রান্সফার হয়। প্রাইমারি স্টোরেজের প্রয়োজন হয় না।}
\itm{1} \B{ব্যবহার:} \B{রিয়াল টাইম অ্যাপ্লিকেশনের ডেটা ট্রান্সফার; যেমন লাইভ টিভি, সম্প্রচার, স্ট্রিমিং ভিডিও/অডিও, ভিডিও কলে}
\itm{2} \B{সুবিধা:} \B{প্রাইমারি স্টোরেজের প্রয়োজন হয় না; যখন প্রয়োজন তখনই ডেটা পাঠানো যায়}
\itm{3} \B{অসুবিধা:} \B{ডেটা পুনঃপ্রেরণ সম্ভব না বলে ভুল-ত্রুটি শনাক্ত করা যায় না; সকল ক্ষেত্রে নির্ভরযোগ্য পদ্ধতি নয়}
\end{multicols}


\begin{multicols}{2}
\chsec{ডেটা ট্রান্সমিশন মোড}
\B{উৎস থেকে গন্তব্যে ডেটা প্রবাহের দিককে ডেটা ট্রান্সমিশন মোড বলে। এটি ৩ প্রকার: (১) সিমপ্লেক্স (২) হাফ-ডুপ্লেক্স (৩) ফুল-ডুপ্লেক্স।}
\chsub{}{সিমপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{কেবলমাত্র একদিকে ডেটা প্রেরণের ব্যবস্থা থাকে। যে প্রান্ত ডেটা প্রেরণ করবে সে প্রান্ত গ্রহণ করতে পারবে না এবং গ্রহণ প্রান্ত প্রেরণ করতে পারে না। যেমন: রেডিও ও টিভি ব্রডকাস্ট, কম্পিউটার থেকে প্রিন্টারে ডেটা প্রেরণ, কী-বোর্ড থেকে কম্পিউটারে ডেটা প্রেরণ।}
\chsub{}{হাফ-ডুপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{উভয় দিক থেকে ডেটা প্রেরণ বা গ্রহণের সুযোগ থাকে, তবে একই সময়ে বা যুগপৎ সম্ভব নয়। যেকোনো একটি প্রান্ত একই সময় কেবলমাত্র ডেটা গ্রহণ অথবা প্রেরণ করতে পারে। যেমন: ওয়াকিটকি।}
\chsub{}{ফুল-ডুপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{একই সময়ে উভয় দিক হতে ডেটা প্রেরণের ব্যবস্থা থাকে। যেকোনো প্রয়োজনে ডেটা প্রেরণ করার সময় ডেটা গ্রহণ অথবা গ্রহণের সময় প্রেরণও করতে পারবে। যেমন: টেলিফোন, মোবাইল।}
\end{multicols}

\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.14\linewidth}|>{\centering\arraybackslash}X|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tblhdr} \B{মোড} & \B{ডায়াগ্রাম} & \B{উদাহরণ} \\\hline
\B{সিমপ্লেক্স} &
\begin{tikzpicture}[scale=0.55,thick]
\draw (0,0) rectangle (0.9,0.6); \node[scale=0.5] at (0.45,0.3){Sender};
\draw (2.4,0) rectangle (3.3,0.6); \node[scale=0.5] at (2.85,0.3){Receiver};
\draw[-Latex] (0.9,0.3) -- (2.4,0.3);
\end{tikzpicture} & \B{রেডিও, টিভি, কীবোর্ড} \LAT{$\to$} \B{কম্পিউটার} \\\hline
\B{হাফ-ডুপ্লেক্স} &
\begin{tikzpicture}[scale=0.55,thick]
\draw (0,0) rectangle (0.9,0.6); \node[scale=0.5] at (0.45,0.3){Device 1};
\draw (2.4,0) rectangle (3.3,0.6); \node[scale=0.5] at (2.85,0.3){Device 2};
\draw[-Latex] (0.9,0.42) -- (2.4,0.42);
\draw[Latex-] (0.9,0.18) -- (2.4,0.18);
\node[scale=0.45] at (1.65,0.75) {t1};
\node[scale=0.45] at (1.65,0.02) {t2};
\end{tikzpicture} & \B{ওয়াকিটকি} \\\hline
\B{ফুল-ডুপ্লেক্স} &
\begin{tikzpicture}[scale=0.55,thick]
\draw (0,0) rectangle (0.9,0.6); \node[scale=0.5] at (0.45,0.3){Device 1};
\draw (2.4,0) rectangle (3.3,0.6); \node[scale=0.5] at (2.85,0.3){Device 2};
\draw[-Latex] (0.9,0.42) -- (2.4,0.42);
\draw[Latex-] (0.9,0.18) -- (2.4,0.18);
\node[scale=0.45] at (1.65,0.75) {\B{সবসময়}};
\end{tikzpicture} & \B{টেলিফোন, মোবাইল} \\\hline
\end{tabularx}
\vspace{4pt}

\begin{multicols}{2}
\chsec{ডেটা বিতরণ বা ডেলিভারি মোড}
\B{প্রাপকের সংখ্যা ও ডেটা গ্রহণের অধিকারের উপর ভিত্তি করে ডেটা বিতরণ বা ডেলিভারি মোড তিন ভাগে বিভক্ত: (১) ইউনিকাস্ট (২) মাল্টিকাস্ট (৩) ব্রডকাস্ট।}
\chsub{}{ইউনিকাস্ট}
\B{ব্যবস্থায় একটি প্রেরক থেকে শুধুমাত্র একটি প্রাপকই ডেটা গ্রহণ করতে পারে। অনেক প্রাপক একসাথে ডেটা গ্রহণ করতে পারে না। এটি 1 to 1 নামে পরিচিত।}
\chsub{}{মাল্টিকাস্ট}
\B{মোডে নেটওয়ার্কের কোনো একটি নোড থেকে ডেটা প্রেরণ করলে তা নেটওয়ার্কের অধীনস্থ সকল নোডই গ্রহণ করতে পারে না; শুধুমাত্র একটি গ্রুপের সকল সদস্য গ্রহণ করতে পারে। এটি 1 to N মোড নামেও পরিচিত।}
\chsub{}{ব্রডকাস্ট}
\B{মোডে নেটওয়ার্কের কোনো একটি নোড থেকে ডেটা প্রেরণ করলে তা নেটওয়ার্কের অধীনস্থ সকল নোডই গ্রহণ করে। এটি 1 to All মোডও বলা হয়। এক্ষেত্রে ১টি প্রেরক থেকে নেটওয়ার্কের অধীনস্থ সকল প্রাপক ডেটা গ্রহণ করতে পারে।}
\end{multicols}

\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.14\linewidth}|>{\centering\arraybackslash}X|}
\hline
\rowcolor{tblhdr}\B{ইউনিকাস্ট (1 to 1)} & \B{মাল্টিকাস্ট (1 to N) \quad ব্রডকাস্ট (1 to All)} \\\hline
\begin{tikzpicture}[scale=0.42,thick]
\node[circle,fill=black,inner sep=1.4pt] (s) at (0,0){}; \node[scale=0.5,below] at (0,-0.15){Src};
\node[circle,draw,inner sep=1.4pt] (r) at (2.2,0){};
\draw[-Latex] (s) -- (r);
\end{tikzpicture} &
\begin{tikzpicture}[scale=0.40,thick]
\node[circle,fill=black,inner sep=1.4pt] (s) at (0,0){};
\foreach \y in {-0.9,-0.3,0.3,0.9}{\node[circle,draw,inner sep=1.3pt] (r) at (2.0,\y){}; \draw[-Latex](s)--(r);}
\node[circle,fill=black,inner sep=1.4pt] (s2) at (5.4,0){};
\foreach \y in {-1.1,-0.65,-0.2,0.25,0.7,1.1}{\node[circle,draw,inner sep=1.2pt] (r2) at (7.6,\y){}; \draw[-Latex](s2)--(r2);}
\end{tikzpicture} \\\hline
\end{tabularx}
\vspace{4pt}


\begin{multicols}{2}
\chsec{কম্পিউটার নেটওয়ার্ক ও নেটওয়ার্ক ডিভাইস}
\itm{1} \B{কম্পিউটার নেটওয়ার্ক:} \B{পরস্পর ডেটা আদান-প্রদানের লক্ষ্যে বিভিন্ন কম্পিউটার কোনো যোগাযোগ মাধ্যম দ্বারা একসঙ্গে যুক্ত থাকলে তাকে কম্পিউটার নেটওয়ার্ক বলে। ইন্টারনেট পৃথিবীর বৃহত্তম কম্পিউটার নেটওয়ার্ক।}
\chsub{}{কম্পিউটার নেটওয়ার্কের উদ্দেশ্য}
\itm{1} \B{হার্ডওয়্যার রিসোর্স শেয়ার} \sub{2} \B{সফটওয়্যার রিসোর্স শেয়ার} \sub{3} \B{ইনফরমেশন রিসোর্স শেয়ার}
\chsub{}{নেটওয়ার্ক ডিভাইস সমূহ}
\B{গেটওয়ে, রাউটার, মডেম, হাব, রিপিটার, সুইচ ও নেটওয়ার্ক ইন্টারফেস কার্ড (NIC)}
\itm{1} \B{হাব:} \B{নেটওয়ার্কিং ডিভাইস যা এর আওতাধীন ডিভাইসগুলোকে একত্রে সংযুক্ত করে। হাবের ভিতরে কোনো বুদ্ধিমত্তা নেই; সিগন্যাল গ্রহণ করার পর একই সাথে সংযুক্ত সকল কম্পিউটারে পাঠায় (ব্রডকাস্ট করে), ফলে ডেটা কলিশনের আশঙ্কা থাকে ও নেটওয়ার্কের ট্রাফিক বেড়ে যায়}
\itm{2} \B{সুইচ:} \B{নেটওয়ার্কিং ডিভাইস, যা আওতাধীন ডিভাইসগুলোকে একত্রে সংযুক্ত করে। সুইচের বুদ্ধিমত্তা আছে; প্রেরিত সিগন্যাল শুধুমাত্র টার্গেট কম্পিউটারে পাঠায়। প্রতিটি কম্পিউটারের Mac অ্যাড্রেস ব্যবহার করে নির্দিষ্ট পোর্টে সিগন্যাল পাঠায়, সংঘর্ষ এড়ানো যায়; ডেটা ফিল্টারিং করা যায়}
\itm{3} \B{রাউটার:} \B{একই প্রোটোকল ভুক্ত দুই বা তারও অধিক ডিভাইসের মধ্যে ডেটা প্যাকেট পৌঁছে দেয়। ভিন্ন ভিন্ন গঠনের একাধিক WAN সংযুক্ত করতে এবং WAN-এর সাথে LAN সংযুক্ত করতে ব্যবহৃত হয়; ডেটা ফিল্টারিং করতে পারে}
\itm{4} \B{গেটওয়ে:} \B{ভিন্ন প্রোটোকল বিশিষ্ট নেটওয়ার্কের মধ্যে সংযোগ স্থাপনের জন্য ব্যবহৃত হয়। এটি প্রোটোকল কনভার্টার বলে; ডেটা ফিল্টারিং করতে পারে}
\itm{5} \B{NIC (নেটওয়ার্ক ইন্টারফেস কার্ড):} \B{কম্পিউটার বা কোনো ডিভাইসকে নেটওয়ার্কে যুক্ত করার জন্য যে ইন্টারফেস কার্ড ব্যবহৃত হয়}

\chsec{নেটওয়ার্ক টপোলজি (Network Topology)}
\B{লোকাল এরিয়া নেটওয়ার্কভুক্ত কম্পিউটার ও অন্যান্য যন্ত্রপাতির ভৌত সংযোগ বিন্যাস এবং নির্বিঘ্নে ডেটা আদান-প্রদানের যুক্তি নির্ভর সুনিয়ন্ত্রিত পথের পরিকল্পনাই টপোলজি। ৬ প্রকার: বাস, স্টার, রিং, ট্রি, মেশ, হাইব্রিড।}
\end{multicols}

\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.09\linewidth}|>{\centering\arraybackslash}p{0.19\linewidth}|X|}
\hline
\rowcolor{tblhdr}\B{টপোলজি} & \B{ডায়াগ্রাম} & \B{সংজ্ঞা, সুবিধা ও অসুবিধা} \\\hline

\B{বাস} &
\begin{tikzpicture}[scale=0.34,thick]
\draw (0,0) -- (5,0);
\foreach \x in {0.6,1.8,3.0,4.2}{\node[circle,fill=black,inner sep=1.3pt] at (\x,0){}; \draw (\x,0)--(\x,0.7);\node[circle,draw,inner sep=1.4pt] at (\x,0.9){};}
\end{tikzpicture}
&
\B{একটি সংযোগ লাইনের (ব্যাকবোন) সাথে সব নোড যুক্ত থাকে। সুবিধা: কম তার, সহজ ইনস্টলেশন, নতুন ডিভাইস সহজে যুক্ত করা যায়, একটি কম্পিউটার বিচ্ছিন্ন হলেও নেটওয়ার্ক অচল হয় না, কেন্দ্রীয় ডিভাইস/সার্ভারের প্রয়োজন নেই। অসুবিধা: ডেটা ট্রান্সমিশন ধীরগতির, প্রধান লাইনে ত্রুটি হলে সম্পূর্ণ নেটওয়ার্ক অচল হয়, কম্পিউটার/দৈর্ঘ্য বৃদ্ধিতে ট্রাফিক বাড়ে, ডেটা সংঘর্ষের আশঙ্কা থাকে।} \\\hline

\B{রিং} &
\begin{tikzpicture}[scale=0.34,thick]
\foreach \a in {0,60,120,180,240,300}{\node[circle,draw,inner sep=1.4pt] (n\a) at (\a:1.3){};}
\draw (n0)--(n60)--(n120)--(n180)--(n240)--(n300)--(n0);
\end{tikzpicture}
&
\B{কম্পিউটারের নোডগুলো চক্রাকার পথে পরস্পর যুক্ত হয়ে নেটওয়ার্ক গঠন করে; কেন্দ্রীয় ডিভাইস প্রয়োজন হয় না; সংকেত একমুখী প্রবাহিত হয়ে নির্দিষ্ট নোডে পৌঁছায়। সুবিধা: হোস্ট/কেন্দ্রীয় সার্ভার দরকার নেই, ডেটা কলিশন হয় না, সমান গুরুত্ব পায়, তার কম লাগে। অসুবিধা: ধীরগতি সম্পন্ন, একমুখী তাই একটি নোড অকার্যকর হলে সম্পূর্ণ নেটওয়ার্ক অকার্যকর, নতুন সংযোজন কঠিন, জটিল সফটওয়্যার প্রয়োজন।} \\\hline

\B{স্টার} &
\begin{tikzpicture}[scale=0.34,thick]
\node[circle,fill=black,inner sep=1.6pt] (c) at (0,0){};
\foreach \a in {0,60,120,180,240,300}{\node[circle,draw,inner sep=1.4pt] (n\a) at (\a:1.4){}; \draw (c)--(n\a);}
\end{tikzpicture}
&
\B{নেটওয়ার্কভুক্ত সকল কম্পিউটার একটি কেন্দ্রীয় স্থানে (হাব/সুইচ) কেব্‌ল দিয়ে যুক্ত হয়। সুবিধা: দ্রুতগতির ডেটা আদান-প্রদান, সংঘর্ষের সম্ভাবনা কম, নতুন নোড যুক্ত করা যায় সহজে, একটি নোড বিচ্ছিন্ন হলেও নেটওয়ার্ক সচল থাকে, তুলনামূলক নিরাপত্তা বেশি। অসুবিধা: প্রতিটি নোডের জন্য পৃথক তার প্রয়োজন হওয়ায় খরচ বেশি; হাব/সুইচ/সার্ভার অচল হলে সম্পূর্ণ নেটওয়ার্ক অকেজো হয়ে পড়ে।} \\\hline

\B{ট্রি} &
\begin{tikzpicture}[scale=0.34,thick]
\node[circle,draw,inner sep=1.4pt] (r) at (0,1.4){};
\node[circle,draw,inner sep=1.4pt] (a) at (-1,0.4){};
\node[circle,draw,inner sep=1.4pt] (b) at (1,0.4){};
\draw (r)--(a); \draw (r)--(b);
\foreach \x [count=\xi from 1] in {-1.6,-0.4}{\node[circle,draw,inner sep=1.2pt] (l\xi) at (\x,-0.6){}; \draw (a)--(l\xi);}
\foreach \x [count=\xi from 1] in {0.4,1.6}{\node[circle,draw,inner sep=1.2pt] (m\xi) at (\x,-0.6){}; \draw (b)--(m\xi);}
\end{tikzpicture}
&
\B{স্টার টপোলজির সম্প্রসারিত রূপ; একাধিক হাব/সুইচ শ্রেণিবদ্ধভাবে যুক্ত করে সব কম্পিউটার একটি বিশেষ স্থানে (প্রধান হোস্ট) সংযুক্ত থাকে; একে হায়ারার্কিক্যাল টপোলজিও বলা হয়। সুবিধা: নতুন শাখা সহজে সম্প্রসারণ, বড় নেটওয়ার্কে বেশি সুবিধা প্রদান করে, ডেটা নিরাপত্তা সবচেয়ে বেশি। অসুবিধা: প্রধান কম্পিউটার নষ্ট হলে সমস্ত নেটওয়ার্ক অচল হয়ে পড়ে, তুলনামূলক জটিল প্রকৃতির, বাস্তবায়ন ব্যয় বেশি।} \\\hline

\B{মেশ} &
\begin{tikzpicture}[scale=0.34,thick]
\foreach \a in {0,72,144,216,288}{\node[circle,draw,inner sep=1.4pt] (n\a) at (\a:1.3){};}
\foreach \a in {0,72,144,216,288}{\foreach \b in {0,72,144,216,288}{\ifdim \a pt<\b pt \draw (n\a)--(n\b);\fi}}
\end{tikzpicture}
&
\B{প্রতিটি কম্পিউটার প্রতিটি ওয়ার্কস্টেশনের সাথে সরাসরি একাধিক পথে যুক্ত থাকে বলে সরাসরি ডেটা আদান-প্রদান করতে পারে; একে পয়েন্ট টু পয়েন্ট বা পিয়ার টু পিয়ার লিংক টপোলজিও বলে। $n$ সংখ্যক নোডের জন্য মোট তারের সংখ্যা $\frac{n(n-1)}{2}$। সুবিধা: দ্রুতগতিতে ডেটা ট্রান্সমিশন, নেটওয়ার্ক সচল থাকে যদি কোনো কম্পিউটার নষ্ট বা বিচ্ছিন্ন হয়, কেন্দ্রীয় ডিভাইসের প্রয়োজন নেই। অসুবিধা: বেশি তার ও লিংক প্রয়োজন, ইনস্টলেশন ও কনফিগারেশন অত্যন্ত জটিল, ব্যয়বহুল।} \\\hline

\B{হাইব্রিড} &
\begin{tikzpicture}[scale=0.34,thick]
\node[circle,fill=black,inner sep=1.6pt] (c) at (0,0){};
\foreach \a in {30,150,270}{\node[circle,draw,inner sep=1.4pt] (n\a) at (\a:1.3){}; \draw (c)--(n\a);}
\draw (c)--(1.3,0.9); \node[circle,draw,inner sep=1.3pt] at (1.3,0.9){};
\end{tikzpicture}
&
\B{বিভিন্ন টপোলজির সমন্বয়ে গড়ে ওঠা টপোলজি; একসাথে বাস ও রিং টপোলজি ব্যবহৃত হতে পারে; ইন্টারনেট এর উপর ভিত্তি করে গঠিত হয়। সুবিধা: হাব/সুইচ যুক্ত করে সম্প্রসারণ করা যায়, ট্রাবলশুটিং সহজতর, একটি টপোলজি নষ্ট হলেও অন্যের উপর প্রভাব পড়ে না। অসুবিধা: রক্ষণাবেক্ষণ খরচ বেশি ও জটিল, ইনস্টলেশন জটিল প্রকৃতির।} \\\hline
\end{tabularx}
\vspace{4pt}


\begin{multicols}{2}
\chsec{ডেটা কমিউনিকেশন মিডিয়া}
\B{যে মাধ্যম দিয়ে ডেটা প্রেরক থেকে প্রাপকের কাছে পৌঁছায় তাকে ডেটা কমিউনিকেশন মিডিয়া বলে। দুই প্রকার: (১) গাইডেড/তারযুক্ত মিডিয়া (২) আনগাইডেড/তারবিহীন মিডিয়া।}

\chsub{}{টুইস্টেড পেয়ার ক্যাবল (Twisted Pair)}
\B{একজোড়া তামার তার একে অপরের সাথে পেঁচিয়ে তৈরি করা হয় বলে এর নাম টুইস্টেড পেয়ার ক্যাবল। দুই প্রকার: আনশিল্ডেড টুইস্টেড পেয়ার (UTP) ও শিল্ডেড টুইস্টেড পেয়ার (STP)।}
\itm{1} \B{UTP:} \B{কোনো ধাতব আচ্ছাদন (শিল্ড) থাকে না; সহজ ও সস্তা, কিন্তু বৈদ্যুতিক হস্তক্ষেপে (Noise) বেশি প্রভাবিত হয়}
\itm{2} \B{STP:} \B{ধাতব শিল্ড দ্বারা আচ্ছাদিত থাকে বলে হস্তক্ষেপ কম হয়, তবে দামে বেশি}
\itm{3} \B{ব্যবহার:} \B{টেলিফোন লাইনে, LAN নেটওয়ার্কে}
\itm{4} \B{সুবিধা:} \B{সহজলভ্য ও সস্তা, ইনস্টলেশন সহজ}
\itm{5} \B{অসুবিধা:} \B{দূরত্ব বাড়লে সংকেত ক্ষয় হয়, বৈদ্যুতিক হস্তক্ষেপে প্রভাবিত হতে পারে}

\chsub{}{কো-এক্সিয়াল ক্যাবল (Coaxial Cable)}
\B{কেন্দ্রে একটি তামার তার এবং তার চারদিকে অন্তরক পদার্থ, ধাতব জালি (শিল্ড) এবং সবার বাইরে প্লাস্টিক আচ্ছাদন দ্বারা তৈরি। দুই প্রকার: থিননেট (Thinnet) ও থিকনেট (Thicknet)।}
\itm{1} \B{থিননেট:} \B{পাতলা ও হালকা, স্বল্প দূরত্বে ব্যবহৃত হয়} \sub{2} \B{থিকনেট:} \B{মোটা ও ভারী, দীর্ঘ দূরত্বে সিগন্যাল বহনে সক্ষম}
\itm{3} \B{ব্যবহার:} \B{ক্যাবল টিভি নেটওয়ার্কে, পুরনো LAN নেটওয়ার্কে}
\itm{4} \B{সুবিধা:} \B{টুইস্টেড পেয়ার এর তুলনায় বেশি দূরত্বে ডেটা প্রেরণ করতে পারে, হস্তক্ষেপ প্রতিরোধী}
\itm{5} \B{অসুবিধা:} \B{ইনস্টলেশন তুলনামূলক জটিল ও ব্যয়বহুল}

\chsub{}{ফাইবার অপটিক ক্যাবল (Fiber Optic Cable)}
\B{আলোর প্রতিফলনের মাধ্যমে ডেটা আদান-প্রদান করা হয়। কাঁচ বা প্লাস্টিকের তৈরি অত্যন্ত সূক্ষ্ম তার দিয়ে গঠিত; মূলত ৩ স্তরে গঠিত — কোর (Core), ক্ল্যাডিং (Cladding) এবং জ্যাকেট (Jacket)।}
\itm{1} \B{কোর:} \B{কেন্দ্রীয় অংশ, যার মধ্য দিয়ে আলোক সংকেত পরিবাহিত হয়}
\itm{2} \B{ক্ল্যাডিং:} \B{কোরকে ঘিরে থাকে, আলোকে কোরের ভেতরে প্রতিফলিত করে রাখে}
\itm{3} \B{জ্যাকেট:} \B{সবচেয়ে বাইরের প্রতিরক্ষামূলক আচ্ছাদন}
\itm{4} \B{প্রকারভেদ:} \B{স্টেপ-ইনডেক্স, গ্রেডেড-ইনডেক্স, সিংগলমোড ও মাল্টিমোড ফাইবার}
\itm{5} \B{সুবিধা:} \B{অনেক দূরত্বে অবিকৃত সংকেত প্রেরণ করা যায়, বৈদ্যুতিক হস্তক্ষেপমুক্ত, উচ্চগতির ব্যান্ডউইথ প্রদান করে, অধিক নিরাপদ}
\itm{6} \B{অসুবিধা:} \B{অত্যন্ত ব্যয়বহুল, ইনস্টলেশন ও রক্ষণাবেক্ষণে বিশেষজ্ঞ প্রয়োজন, তার ভঙ্গুর}
\end{multicols}

\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|>{\centering\arraybackslash}p{0.16\linewidth}|X|X|X|}
\hline
\rowcolor{tblhdr}\B{বিষয়} & \B{টুইস্টেড পেয়ার} & \B{কো-এক্সিয়াল} & \B{ফাইবার অপটিক} \\\hline
\B{গঠন} & \B{দুটি প্যাঁচানো তামার তার} & \B{কেন্দ্রীয় তার + শিল্ড} & \B{কাঁচ/প্লাস্টিক তার} \\\hline
\B{গতি} & \B{সবচেয়ে কম} & \B{মাঝারি} & \B{সবচেয়ে বেশি} \\\hline
\B{দূরত্ব} & \B{সবচেয়ে কম} & \B{মাঝারি} & \B{সবচেয়ে বেশি} \\\hline
\B{খরচ} & \B{সবচেয়ে কম} & \B{মাঝারি} & \B{সবচেয়ে বেশি} \\\hline
\B{হস্তক্ষেপ} & \B{বেশি প্রভাবিত} & \B{কম প্রভাবিত} & \B{প্রভাবমুক্ত} \\\hline
\end{tabularx}
\vspace{4pt}

\noindent
\begin{minipage}{0.31\linewidth}
\centering\scriptsize\B{Twisted Pair}\\
\begin{tikzpicture}[scale=0.5,thick]
\draw[decorate,decoration={coil,aspect=0.3,segment length=3pt,amplitude=2pt}] (0,0.15) -- (2.4,0.15);
\draw[decorate,decoration={coil,aspect=0.3,segment length=3pt,amplitude=2pt}] (0,-0.15) -- (2.4,-0.15);
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.31\linewidth}
\centering\scriptsize\B{Coaxial}\\
\begin{tikzpicture}[scale=0.5,thick]
\draw (0,0) ellipse (0.35 and 0.35);
\draw (0,0) circle (0.15);
\draw (0.35,0)--(2.2,0);
\draw (-0.35,0.35)--(2.2,0.35); \draw (-0.35,-0.35)--(2.2,-0.35);
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.31\linewidth}
\centering\scriptsize\B{Fiber Optic}\\
\begin{tikzpicture}[scale=0.5,thick]
\draw (0,0) rectangle (2.4,0.5);
\draw[dashed] (0,0.25)--(2.4,0.25);
\node[scale=0.4] at (1.2,0.62) {Cladding};
\node[scale=0.4] at (1.2,0.12) {Core};
\end{tikzpicture}
\end{minipage}
\vspace{4pt}


\bigskip\par\noindent\rule{\linewidth}{0.6pt}\par\bigskip
\begin{center}
\noindent{\bfseries\large\B{অধ্যায় ৪ (ওয়েব ডিজাইন পরিচিতি) — বিস্তারিত নোট}}
\end{center}
\vspace{2pt}
\begin{multicols}{2}

\chsec{ওয়েব পেজ, ওয়েবসাইট ও হোম পেজ}
\itm{1} \B{ওয়েব পেজ:} \B{ইন্টারনেটে প্রদর্শিত একক HTML ডকুমেন্ট যা টেক্সট, ছবি, ভিডিও ইত্যাদি ধারণ করতে পারে}
\itm{2} \B{ওয়েবসাইট:} \B{পরস্পর হাইপারলিংকে যুক্ত একগুচ্ছ ওয়েব পেজের সমষ্টি, যা একটি ইউনিক ডোমেইন নামে প্রকাশিত হয়}
\itm{3} \B{হোম পেজ:} \B{ওয়েবসাইটের প্রথম বা প্রধান পেজ, যা থেকে অন্য পেজগুলোতে যাওয়া যায়}
\itm{4} \B{ওয়েবসাইটের ইতিহাস:} \B{টিম বার্নার্স লি ১৯৯০ সালে ওয়েবসাইটের ধারণা প্রবর্তন করেন}
\chsub{}{স্ট্যাটিক ও ডাইনামিক ওয়েবসাইট}
\itm{1} \B{স্ট্যাটিক ওয়েবসাইট:} \B{যার কন্টেন্ট স্থির থাকে, ব্যবহারকারীর ইনপুট অনুযায়ী পরিবর্তিত হয় না; শুধু HTML/CSS দিয়ে তৈরি}
\itm{2} \B{ডাইনামিক ওয়েবসাইট:} \B{যার কন্টেন্ট ব্যবহারকারীর ইনপুট বা সময়ের সাথে পরিবর্তিত হয়; সার্ভার সাইড স্ক্রিপ্ট ও ডেটাবেজ ব্যবহৃত হয়}

\chsec{ওয়েব সার্ভার ও URL}
\itm{1} \B{ওয়েব সার্ভার:} \B{যে সফটওয়্যার/হার্ডওয়্যার ব্যবহারকারীর অনুরোধে ওয়েব পেজ সরবরাহ করে; উদাহরণ: Apache, IIS, GWS (Google Web Server)}
\itm{2} \B{URL (Uniform Resource Locator):} \B{ইন্টারনেটে কোনো নির্দিষ্ট রিসোর্সের ঠিকানা}
\end{multicols}
\vspace{2pt}\noindent\scriptsize\B{URL গঠন:}
\begin{center}
\begin{tikzpicture}[scale=0.62,thick]
\node[scale=0.62] at (0,0) {\LAT{https://}\B{www.example.com}\LAT{/page.html?id=1\#section}};
\draw[decorate,decoration={brace,amplitude=3pt}] (-3.3,-0.15) -- (-1.75,-0.15); \node[scale=0.5] at (-2.5,-0.5){\B{প্রোটোকল}};
\draw[decorate,decoration={brace,amplitude=3pt}] (-1.6,-0.15) -- (0.15,-0.15); \node[scale=0.5] at (-0.7,-0.5){\B{ডোমেইন নেম}};
\draw[decorate,decoration={brace,amplitude=3pt}] (0.2,-0.15) -- (1.55,-0.15); \node[scale=0.5] at (0.9,-0.5){\B{পাথ}};
\draw[decorate,decoration={brace,amplitude=3pt}] (1.6,-0.15) -- (3.4,-0.15); \node[scale=0.5] at (2.5,-0.5){\B{কুয়েরি/ফ্র্যাগমেন্ট}};
\end{tikzpicture}
\end{center}
\vspace{2pt}
\begin{multicols}{2}

\chsub{}{প্রোটোকলের প্রকারভেদ}
\itm{1} \B{HTTP/HTTPS:} \B{ওয়েব পেজ আদান-প্রদানের প্রোটোকল}
\itm{2} \B{FTP:} \B{ফাইল স্থানান্তরের প্রোটোকল} \sub{3} \B{VoIP:} \B{ইন্টারনেটের মাধ্যমে ভয়েস কল}
\itm{4} \B{POP:} \B{মেইল সার্ভার থেকে মেইল ডাউনলোডের প্রোটোকল}
\itm{5} \B{SMTP:} \B{মেইল প্রেরণের প্রোটোকল}

\chsec{WWW, ওয়েব পোর্টাল, সার্চ ইঞ্জিন ও ব্রাউজার}
\itm{1} \B{WWW (World Wide Web):} \B{ইন্টারনেটে হাইপারলিংকের মাধ্যমে সংযুক্ত ওয়েব পেজের সমষ্টি}
\itm{2} \B{ওয়েব পোর্টাল:} \B{একাধিক সেবা এক জায়গায় প্রদানকারী ওয়েবসাইট; যেমন ই-মেইল, খবর, সার্চ}
\itm{3} \B{সার্চ ইঞ্জিন:} \B{ইন্টারনেটে তথ্য খুঁজে দেওয়ার সফটওয়্যার সিস্টেম; যেমন Google, Bing}
\itm{4} \B{ওয়েব ব্রাউজার:} \B{ওয়েব পেজ প্রদর্শনের সফটওয়্যার; যেমন Chrome, Firefox}

\chsec{HTML — মৌলিক ধারণা}
\itm{1} \B{HTML:} \B{HyperText Markup Language; ওয়েব পেজ তৈরির প্রমিত মার্কআপ ভাষা}
\chsub{}{HTML ট্যাগের ধরন}
\itm{1} \B{কন্টেইনার ট্যাগ:} \B{শুরু ও শেষ ট্যাগ উভয়ই থাকে; যেমন} \LAT{<p>...</p>}
\itm{2} \B{এম্পটি/শূন্য ট্যাগ:} \B{শুধু শুরু ট্যাগ থাকে, শেষ ট্যাগ থাকে না; যেমন} \LAT{<br>, <img>}
\chsub{}{এলিমেন্ট, অ্যাট্রিবিউট ও ভ্যালু}
\itm{1} \B{এলিমেন্ট:} \B{একটি সম্পূর্ণ ট্যাগ কাঠামো (শুরু ট্যাগ + কন্টেন্ট + শেষ ট্যাগ)}
\itm{2} \B{অ্যাট্রিবিউট:} \B{ট্যাগের বৈশিষ্ট্য নির্ধারণকারী নাম; শুরু ট্যাগের ভেতরে লেখা হয়}
\itm{3} \B{ভ্যালু:} \B{অ্যাট্রিবিউটের মান, যা উদ্ধৃতি চিহ্নের মধ্যে লেখা হয়}
\chsub{}{হেডিং ট্যাগ ও টেক্সট ফরম্যাটিং}
\itm{1} \B{হেডিং ট্যাগ:} \LAT{<h1>} \B{থেকে} \LAT{<h6>} \B{পর্যন্ত; }\LAT{<h1>}\B{ সবচেয়ে বড় ও }\LAT{<h6>}\B{ সবচেয়ে ছোট}
\itm{2} \B{সুপারস্ক্রিপ্ট/সাবস্ক্রিপ্ট:} \LAT{<sup>} \B{ও} \LAT{<sub>} \B{ট্যাগ ব্যবহার করে টেক্সট উপরে/নিচে দেখানো হয়}
\itm{3} \B{ফন্ট ট্যাগ:} \LAT{<font face="..." color="..." size="...">} \B{ব্যবহার করে টেক্সটের ফন্ট, রং ও আকার নির্ধারণ করা হয় (HTML5-এ বাতিল)}
\end{multicols}


\bigskip\par\noindent\rule{\linewidth}{0.6pt}\par\bigskip
\begin{center}
\noindent{\bfseries\large\B{অধ্যায় ৫ (প্রোগ্রামিং ভাষা) — বিস্তারিত নোট}}
\end{center}
\vspace{2pt}
\begin{multicols}{2}

\chsec{প্রোগ্রাম, প্রোগ্রামিং ও প্রোগ্রামিং ভাষা}
\itm{1} \B{প্রোগ্রাম:} \B{কোনো সমস্যা সমাধানের জন্য ধারাবাহিক নির্দেশনার সমষ্টি, যা কম্পিউটার সম্পাদন করতে পারে}
\itm{2} \B{কম্পিউটার প্রোগ্রামিং:} \B{কোনো নির্দিষ্ট প্রোগ্রামিং ভাষা ব্যবহার করে প্রোগ্রাম রচনা করার প্রক্রিয়া}
\itm{3} \B{প্রোগ্রামিং ভাষা:} \B{যে ভাষার মাধ্যমে মানুষ কম্পিউটারকে নির্দেশ প্রদান করে; উদাহরণ: C, C++, C\#, BASIC, JAVA, FORTRAN, VB, Python}

\chsec{প্রোগ্রামিং ভাষার স্তর}
\B{প্রোগ্রামিং ভাষা মূলত দুই স্তরে বিভক্ত: নিম্ন-স্তরের ভাষা ও উচ্চ-স্তরের ভাষা। নিম্ন-স্তরের ভাষা আবার মেশিন ভাষা ও অ্যাসেম্বলি ভাষায় বিভক্ত।}
\end{multicols}
\begin{center}
\begin{tikzpicture}[scale=0.62,thick,level distance=0.9cm,
level 1/.style={sibling distance=3.2cm},level 2/.style={sibling distance=1.7cm}]
\node[draw,rounded corners,scale=0.6] {\B{প্রোগ্রামিং ভাষা}}
child{node[draw,rounded corners,scale=0.6]{\B{নিম্ন-স্তরের ভাষা}}
  child{node[draw,rounded corners,scale=0.55]{\B{মেশিন ভাষা}}}
  child{node[draw,rounded corners,scale=0.55]{\B{অ্যাসেম্বলি ভাষা}}}
}
child{node[draw,rounded corners,scale=0.6]{\B{উচ্চ-স্তরের ভাষা}}
  child{node[draw,rounded corners,scale=0.5]{\LAT{C/C++/JAVA}}}
  child{node[draw,rounded corners,scale=0.5]{\LAT{BASIC/FORTRAN/VB}}}
};
\end{tikzpicture}
\end{center}
\begin{multicols}{2}

\chsub{}{মেশিন ভাষা (Machine Language)}
\B{কম্পিউটার সরাসরি বোঝে এমন বাইনারি (0, 1) নির্দেশনায় লেখা ভাষা; এতে লেখা কোডকে সোর্স কোড এবং কম্পাইল/অনুবাদের পর সৃষ্ট কোডকে অবজেক্ট কোড বলে।}
\itm{1} \B{সুবিধা:} \B{সরাসরি সম্পাদনযোগ্য বলে দ্রুত কার্যকর হয়, অনুবাদকের প্রয়োজন হয় না, মেমোরি কম লাগে}
\itm{2} \B{অসুবিধা:} \B{লেখা ও ডিবাগ করা অত্যন্ত কঠিন, প্রসেসর নির্ভর (Machine Dependent), ত্রুটি সংশোধন কঠিন, মনে রাখা কঠিন, সময়সাপেক্ষ}

\chsub{}{অ্যাসেম্বলি ভাষা (Assembly Language)}
\B{সংকেত বা প্রতীকী কোড (Mnemonic Code) ব্যবহার করে লেখা ভাষা; যেমন ADD, SUB, MOV।}
\itm{1} \B{সুবিধা:} \B{মেশিন ভাষার তুলনায় সহজবোধ্য, ত্রুটি সংশোধন সহজ}
\itm{2} \B{অসুবিধা:} \B{প্রসেসর নির্ভর, প্রোগ্রাম লেখা তুলনামূলক জটিল}

\chsub{}{উচ্চ-স্তরের ভাষা (High-Level Language)}
\B{মানুষের ভাষার (ইংরেজি) কাছাকাছি সহজবোধ্য শব্দ ও বাক্য দিয়ে লেখা ভাষা; উদাহরণ: C, C++, JAVA, Python, BASIC, FORTRAN, VB।}
\itm{1} \B{সুবিধা:} \B{লেখা সহজ, মেশিন নিরপেক্ষ (Machine Independent), ত্রুটি সংশোধন সহজ, বোঝা সহজ, রক্ষণাবেক্ষণ সহজ}
\itm{2} \B{অসুবিধা:} \B{অনুবাদকের (Compiler/Interpreter) প্রয়োজন হয়, সম্পাদনে তুলনামূলক বেশি সময় লাগে, মেমোরি বেশি প্রয়োজন হয়}

\chsec{অনুবাদক প্রোগ্রাম (Translator/Language Processor)}
\B{উচ্চ বা নিম্ন-স্তরের ভাষায় লেখা প্রোগ্রামকে কম্পিউটারের বোধগম্য মেশিন ভাষায় রূপান্তর করে এমন প্রোগ্রামকে অনুবাদক প্রোগ্রাম বলে। ৩ প্রকার: অ্যাসেম্বলার, কম্পাইলার, ইন্টারপ্রেটার।}
\itm{1} \B{অ্যাসেম্বলার:} \B{অ্যাসেম্বলি ভাষায় লেখা প্রোগ্রামকে মেশিন ভাষায় রূপান্তর করে}
\itm{2} \B{কম্পাইলার:} \B{উচ্চ-স্তরের ভাষায় লেখা সম্পূর্ণ সোর্স কোডকে একবারে মেশিন ভাষায় (অবজেক্ট কোড) রূপান্তর করে; ত্রুটি থাকলে একসাথে সব ত্রুটি দেখায়}
\itm{3} \B{ইন্টারপ্রেটার:} \B{সোর্স কোডের প্রতিটি লাইন একে একে অনুবাদ ও সম্পাদন করে; একটি লাইনে ত্রুটি থাকলে সাথে সাথে দেখায় ও থেমে যায়}
\end{multicols}
\vspace{2pt}
\noindent
\begin{minipage}{0.32\linewidth}
\centering\footnotesize\B{Assembler}\\[3pt]
\begin{tikzpicture}[thick,every node/.style={font=\scriptsize},node distance=6mm]
\node[draw,fill=shape2!40,rounded corners,minimum width=1.7cm,minimum height=0.6cm] (s) {Assembly Code};
\node[draw,fill=shape1!70,rounded corners,minimum width=1.7cm,minimum height=0.6cm,right=of s] (t) {Assembler};
\node[draw,fill=shape3!60,rounded corners,minimum width=1.7cm,minimum height=0.6cm,below=of t] (o) {Machine Code};
\draw[-Latex,thick] (s)--(t); \draw[-Latex,thick] (t)--(o);
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.32\linewidth}
\centering\footnotesize\B{Compiler}\\[3pt]
\begin{tikzpicture}[thick,every node/.style={font=\scriptsize},node distance=6mm]
\node[draw,fill=shape2!40,rounded corners,minimum width=1.7cm,minimum height=0.6cm] (s) {Source Code};
\node[draw,fill=shape1!70,rounded corners,minimum width=1.7cm,minimum height=0.6cm,right=of s] (t) {Compiler};
\node[draw,fill=shape3!60,rounded corners,minimum width=1.7cm,minimum height=0.6cm,below=of t] (o) {Object Code};
\draw[-Latex,thick] (s)--(t); \draw[-Latex,thick] (t)--(o);
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}{0.32\linewidth}
\centering\footnotesize\B{Interpreter}\\[3pt]
\begin{tikzpicture}[thick,every node/.style={font=\scriptsize},node distance=6mm]
\node[draw,fill=shape2!40,rounded corners,minimum width=1.7cm,minimum height=0.6cm] (s) {Line-by-line};
\node[draw,fill=shape1!70,rounded corners,minimum width=1.7cm,minimum height=0.6cm,right=of s] (t) {Interpreter};
\node[draw,fill=shape3!60,rounded corners,minimum width=1.7cm,minimum height=0.6cm,below=of t] (o) {Execute};
\draw[-Latex,thick] (s)--(t); \draw[-Latex,thick] (t)--(o);
\end{tikzpicture}
\end{minipage}
\vspace{4pt}
\noindent\scriptsize\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\rowcolor{tblhdr}\B{কম্পাইলার} & \B{ইন্টারপ্রেটার} \\\hline
\B{সম্পূর্ণ প্রোগ্রাম একবারে অনুবাদ করে} & \B{প্রতি লাইন আলাদাভাবে অনুবাদ করে} \\\hline
\B{সম্পাদন গতি বেশি (Object Code তৈরি হয়)} & \B{সম্পাদন গতি কম (Object Code তৈরি হয় না)} \\\hline
\B{সব ত্রুটি একসাথে দেখায়, সময় বেশি লাগে অনুবাদে} & \B{একটি ত্রুটিতেই থেমে যায়, ডিবাগ সহজ} \\\hline
\B{উদাহরণ:} \LAT{C, C++} & \B{উদাহরণ:} \LAT{Python, BASIC} \B{এর কিছু সংস্করণ} \\\hline
\end{tabularx}
\vspace{3pt}
\begin{multicols}{2}

\chsec{প্রোগ্রাম তৈরির ধাপ}
\B{একটি প্রোগ্রাম তৈরির জন্য নির্দিষ্ট কতগুলো ধাপ অনুসরণ করা হয়: সমস্যা সংজ্ঞায়ন (Problem Definition) $\to$ বিশ্লেষণ (Analysis) $\to$ ডিজাইন (Design) $\to$ কোডিং (Coding) $\to$ বাস্তবায়ন (Implementation) $\to$ ডকুমেন্টেশন (Documentation) $\to$ রক্ষণাবেক্ষণ (Maintenance)।}
\end{multicols}
\begin{center}
\begin{adjustbox}{max width=0.98\linewidth}
\begin{tikzpicture}[thick,every node/.style={font=\scriptsize}]
\foreach \i/\txt/\c [count=\k from 0] in {1/সমস্যা সংজ্ঞায়ন/shape1,2/বিশ্লেষণ/shape2,3/ডিজাইন/shape3,4/কোডিং/shape4,5/বাস্তবায়ন/shape5,6/ডকুমেন্টেশন/shape6,7/রক্ষণাবেক্ষণ/shape1}{
\node[draw,rounded corners,fill=\c!60,minimum width=2.1cm,minimum height=0.7cm] (n\i) at (\k*2.35,0) {\B{\txt}};
}
\foreach \i [count=\j from 2] in {1,2,3,4,5,6}{\draw[-Latex,thick] (n\i)--(n\j);}
\end{tikzpicture}
\end{adjustbox}
\end{center}
\begin{multicols}{2}

\chsec{অ্যালগরিদম ও ফ্লোচার্ট}
\itm{1} \B{অ্যালগরিদম:} \B{কোনো সমস্যা সমাধানের জন্য সসীম সংখ্যক ধাপে বিন্যস্ত সুস্পষ্ট নির্দেশনার সমষ্টি}
\itm{2} \B{উৎপত্তি:} \B{গণিতবিদ আল-খোয়ারিজমির নামের ল্যাটিন উচ্চারণ Algorithmi থেকে Algorithm শব্দের উদ্ভব}
\itm{3} \B{ফ্লোচার্ট:} \B{সমস্যা সমাধানের ধাপগুলো বিভিন্ন প্রতীক ও চিহ্নের মাধ্যমে চিত্রাকারে উপস্থাপন করা হলে তাকে ফ্লোচার্ট বলে}
\chsub{}{ফ্লোচার্টের প্রকারভেদ}
\itm{1} \B{প্রোগ্রাম ফ্লোচার্ট:} \B{কোনো প্রোগ্রামের পর্যায়ক্রমিক ধাপগুলো প্রতীকের মাধ্যমে দেখানো হয়}
\itm{2} \B{সিস্টেম ফ্লোচার্ট:} \B{সম্পূর্ণ সিস্টেমের ডেটা প্রবাহ ও কার্যপ্রণালি প্রতীকের মাধ্যমে দেখানো হয়}
\chsub{}{অ্যালগরিদমের বৈশিষ্ট্য}
\itm{1} \B{সসীমতা:} \B{সসীম সংখ্যক ধাপে সমাপ্ত হতে হয়}
\itm{2} \B{সুনির্দিষ্টতা:} \B{প্রতিটি ধাপ স্পষ্ট ও দ্ব্যর্থহীন হতে হয়}
\itm{3} \B{ইনপুট-আউটপুট:} \B{এক বা একাধিক ইনপুট নিয়ে সুনির্দিষ্ট আউটপুট দিতে হয়}
\itm{4} \B{কার্যকারিতা:} \B{হাতে-কলমে সম্পাদনযোগ্য সহজ পদক্ষেপ হতে হয়}
\end{multicols}
\vspace{4pt}
\noindent\footnotesize\textbf{\B{উদাহরণ --- দুটি সংখ্যার যোগফল নির্ণয়ের অ্যালগরিদম ও ফ্লোচার্ট:}}
\vspace{4pt}
\noindent
\begin{minipage}[t]{0.55\linewidth}
\footnotesize
\B{Step 1:} \LAT{Start}\\
\B{Step 2:} \LAT{A} \B{এবং} \LAT{B} \B{ইনপুট নেয়া}\\
\B{Step 3:} \LAT{SUM = A + B} \B{গণনা করা}\\
\B{Step 4:} \LAT{SUM} \B{প্রদর্শন করা}\\
\B{Step 5:} \LAT{Stop}
\end{minipage}\hfill
\begin{minipage}[t]{0.42\linewidth}
\centering
\begin{tikzpicture}[thick,every node/.style={font=\scriptsize},node distance=6mm]
\node[draw,ellipse,fill=shape1!70,minimum width=2.1cm,minimum height=0.6cm] (s1) {Start};
\node[draw,trapezium,trapezium left angle=70,trapezium right angle=110,fill=shape2!50,minimum width=2.1cm,below=of s1] (s2) {\LAT{Input A, B}};
\node[draw,rectangle,fill=shape3!60,minimum width=2.1cm,minimum height=0.55cm,below=of s2] (s3) {\LAT{SUM = A+B}};
\node[draw,trapezium,trapezium left angle=70,trapezium right angle=110,fill=shape4!60,minimum width=2.1cm,below=of s3] (s4) {\LAT{Print SUM}};
\node[draw,ellipse,fill=shape5!60,minimum width=2.1cm,minimum height=0.6cm,below=of s4] (s5) {Stop};
\draw[-Latex,thick] (s1)--(s2); \draw[-Latex,thick] (s2)--(s3); \draw[-Latex,thick] (s3)--(s4); \draw[-Latex,thick] (s4)--(s5);
\end{tikzpicture}
\end{minipage}




\clearpage
\chsecfull{অতিরিক্ত বিস্তারিত নোট --- সম্পূর্ণ সিলেবাস}
\begin{multicols}{2}
\chsec{মৌলিক সংজ্ঞাবলি}

\textbf{\B{ডাটা বা উপাত্ত :}} \B{কোনো কিছুর সম্পর্কে বিচ্ছিন্ন বা ক্ষুদ্র ক্ষুদ্র ধারণাকে ডাটা বা উপাত্ত বলে।}

\textbf{\B{ইনফরমেশন বা তথ্য :}} \B{পরস্পর সম্পর্কিত একাধিক ডাটা মিলে যদি কোনো কিছুর সম্পর্কে পরিপূর্ণ ধারণা দেয় তখন তাকে ইনফরমেশন বা তথ্য বলে।}

\textbf{\B{তথ্য প্রযুক্তি (Information Technology - IT) :}} \B{কম্পিউটার ও নেটওয়ার্ক ব্যবস্থার মাধ্যমে তথ্য সংগ্রহ, প্রক্রিয়াকরণ, সংরক্ষণ ও বিতরণের সাথে সংশ্লিষ্ট প্রযুক্তি ও ব্যবস্থাকে বলা হয় তথ্য প্রযুক্তি। এই প্রযুক্তিকে সংক্ষেপে বলা হয় আইটি (IT)।}

\textbf{\B{যোগাযোগ প্রযুক্তি :}} \B{যোগাযোগ প্রযুক্তি হলো ডেটা কমিউনিকেশন ব্যবস্থার সাথে সংশ্লিষ্ট প্রযুক্তি। কম্পিউটার কিংবা অন্য কোনো যন্ত্রের সাথে এক বা একাধিক স্থান থেকে অন্য এক বা একাধিক স্থানে কিংবা এক বা একাধিক ডিভাইস থেকে অন্য এক বা একাধিক ডিভাইসে স্থানান্তরের প্রক্রিয়া হলো ডেটা কমিউনিকেশন।}

\textbf{\B{তথ্য ও যোগাযোগ প্রযুক্তি :}} \B{জাতীয় তথ্য ও যোগাযোগ প্রযুক্তি নীতিমালা ২০০৯ অনুযায়ী তথ্য ও যোগাযোগ প্রযুক্তি হলো যেকোনো প্রকারের তথ্যের উৎপত্তি, বিশ্লেষণ, সংরক্ষণ, প্রক্রিয়াকরণ এবং সঞ্চালন প্রক্রিয়ায় ব্যবহৃত সকল প্রকার ইলেকট্রনিক প্রযুক্তিকে বুঝায়।}

\chsub{}{তথ্য ও যোগাযোগ প্রযুক্তির প্রভাব}
\noindent\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|X|X|}
\hline
\rowcolor{tblhdr} \centering\arraybackslash\B{\textbf{অবদান}} & \centering\arraybackslash\B{\textbf{কুফল/নেতিবাচক প্রভাব}} \tabularnewline\hline
\B{i. অতি কম খরচ।} & \B{i. অশ্লীলতা বৃদ্ধি।} \\\hline
\B{ii. দক্ষতা ও কাজের গতি বৃদ্ধি।} & \B{ii. অপরাধ প্রবণতা বৃদ্ধি।} \\\hline
\B{iii. সময় ও আর্থিক সাশ্রয়।} & \B{iii. গোপনীয়তা} \\\hline
\B{iv. তাৎক্ষণিক যোগাযোগের সুবিধা।} & \B{iv. মিথ্যা প্রচারণা।} \\\hline
\B{v. ব্যবসা বাণিজ্য লাভজনক হওয়া।} & \B{v. প্রথা ও সংস্কৃতির বিলুপ্তি।} \\\hline
\B{vi. প্রশিক্ষণ কর্মকাণ্ডে গতিময়তা।} & \B{vi. শারীরিক সমস্যা সৃষ্টি।} \\\hline
\B{vii. মনুষ্য শক্তির অপচয় রোধ} & \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{বিশ্বগ্রাম}
\B{প্রখ্যাত দার্শনিক ও কানাডার টরেন্টো বিশ্ববিদ্যালয়ের ইংরেজি বিভাগের অধ্যাপক মার্শাল ম্যাকলুহান (Marshall Mcluhan) হলেন প্রথম ব্যক্তি, যিনি ১৯৬০ এর দশকের শুরুতে বিশ্বগ্রাম বা Global Village শব্দটিকে সকলের সামনে তুলে ধরে একে জনপ্রিয় করে তোলেন। কানেক্টিভিটি হচ্ছে বিশ্বগ্রামের মূল ভিত্তি। তথ্য বা ডাটা হচ্ছে বিশ্বগ্রামের মূল চালিকা শক্তি।}

\chsub{}{বিশ্বগ্রাম প্রতিষ্ঠার উপাদানসমূহ}
\B{১। হার্ডওয়্যার} \\
\B{২। সফটওয়্যার} \\
\B{৩। নেটওয়ার্ক সংযুক্তি} \\
\B{৪। ডেটা} \\
\B{৫। মানুষের সক্ষমতা}

\chsub{}{বিশ্বগ্রাম প্রতিষ্ঠার লক্ষ্য ও উদ্দেশ্য}
\B{1. পৃথিবীর বিভিন্ন প্রান্তের সম্প্রদায়ের মানুষকে একই সুযোগ সুবিধা সম্বলিত সমাজের অন্তর্ভুক্ত করা।} \\
\B{2. বিশ্বের বিভিন্ন দেশের উদ্ভূত সমস্যা এবং এ সমস্যা থেকে উত্তরণের জন্য জনমত গড়ে তোলা।} \\
\B{3. বিশ্বের বিভিন্ন সম্প্রদায়ের মধ্যে সাংস্কৃতিক তথ্য আদান-প্রদান।} \\
\B{4. পৃথিবীর বিভিন্ন দেশের পেশাজীবীদের মধ্যে পারস্পরিক যোগাযোগ স্থাপন করা।} \\
\B{5. বিশ্বের বিভিন্ন দেশে প্রযুক্তি নির্ভর বিজ্ঞানমনস্ক দক্ষ জনসম্পদ তৈরির মাধ্যমে বিজ্ঞানভিত্তিক নেতৃত্ব গড়ে তোলা।}

\chsec{বিশ্বগ্রামের সুবিধাসমূহ}
\begin{enumerate}
    \item \B{মানুষের কর্ম দক্ষতা ও গতি বৃদ্ধি পায়।}
    \item \B{অনলাইনে কেনাকাটার সুবিধা পাওয়া যায়।}
    \item \B{বিশ্বের প্রতি মুহূর্তের খবর ঘরে বসেই পাওয়া যায়}
    \item \B{বিভিন্ন দেশের সাংস্কৃতিক তথ্যাদি বিনিময় করা যায়।}
    \item \B{যেকোনো বিষয়ে সহজে বিশ্ব জনমত গড়ে তোলা যায়।}
    \item \B{তথ্য প্রযুক্তি ব্যবহার করে মানুষের জীবনযাত্রার মান উন্নত হয়।}
    \item \B{সহজে বিভিন্ন বিষয়ের গবেষণা করা যায় এবং ফলাফল জানা যায়।}
    \item \B{ঘরে বসেই উন্নত চিকিৎসা সেবা পাওয়া যায়।}
    \item \B{উন্নত যোগাযোগ সুবিধা পাওয়া যায়।}
    \item \B{অনলাইন লাইব্রেরি শিক্ষার প্রসার ঘটছে।}
\end{enumerate}

\chsec{বিশ্বগ্রামের অসুবিধাসমূহ}
\begin{enumerate}
    \item \B{অনেক সময় তথ্যের গোপনীয়তা রক্ষা করা যায় না।}
    \item \B{ইন্টারনেটের অবাধ ব্যবহারের কারণে অনৈতিক কাজ দিন দিন বৃদ্ধি পাচ্ছে।}
    \item \B{ইন্টারনেট প্রযুক্তি ব্যবহার করে হ্যাকিং এর মাধ্যমে গোপনীয় তথ্য চুরি হয়ে যায়।}
    \item \B{ব্যাংকের হিসাব হ্যাক করে হ্যাকাররা বিপুল পরিমাণ অর্থ আত্মসাৎ করতে পারে।}
    \item \B{অনেক সময় ইন্টারনেট স্পিড না থাকায় বিভিন্ন প্রয়োজনীয় কাজ যথাসময়ে সম্পন্ন করা যায় না।}
\end{enumerate}

\chsec{বিশ্বগ্রামের প্রধান উপাদানসমূহ}
\itm{$\Rightarrow$} \textbf{\B{যোগাযোগ :}} \B{কথন, লিখন কিংবা অন্য কোনো মাধ্যমের দ্বারা তথ্যের আদান - প্রদানই হলো যোগাযোগ।}
\itm{$\Rightarrow$} \textbf{\B{ইন্টারনেট :}} \B{বিশ্বগ্রাম বা গ্লোবাল ভিলেজ প্রতিষ্ঠার ক্ষেত্রে যে উপাদানটি সবচেয়ে বেশি অবদান রেখেছে সেটি হলো ইন্টারনেট। মূলত ইন্টারনেট না থাকলে এত ব্যাপকভাবে বিশ্ব জনগণের একে অপরের কাছাকাছি আসার সুযোগ সৃষ্টি হতো না।}
\itm{$\Rightarrow$} \textbf{\B{ই-মেইল :}} \B{ই-মেইল হচ্ছে ইলেকট্রনিক মেইল বা বার্তা। অর্থাৎ ইলেকট্রনিক যন্ত্রপাতি ব্যবহার করে ইন্টারনেটের মাধ্যমে নির্ভরযোগ্যভাবে বার্তা আদান প্রদান করার একটি পদ্ধতি হচ্ছে ই-মেইল।}
\itm{$\Rightarrow$} \textbf{\B{টেলিকনফারেন্সিং :}} \B{টেলিযোগাযোগের মাধ্যমে সভা অনুষ্ঠানের প্রক্রিয়াকে টেলিকনফারেন্সিং বলে। এর উদ্ভাবক মরি টারফ।}
\itm{$\Rightarrow$} \textbf{\B{ভিডিও কনফারেন্সিং :}} \B{টেলিকমিউনিকেশন প্রযুক্তি ব্যবহার করে দুই বা ততোধিক ভৌগোলিক অবস্থানে অবস্থানরত ব্যক্তিবর্গের মধ্যে অডিও, ভিডিও সম্প্রচারের মাধ্যমে যোগাযোগ করার প্রক্রিয়াকে ভিডিও কনফারেন্সিং বলে।}
\itm{$\Rightarrow$} \textbf{\B{আউটসোর্সিং :}} \B{তথ্য ও যোগাযোগ প্রযুক্তিকে কাজে লাগিয়ে এক দেশের নাগরিক ভিন্ন ভিন্ন দেশের নাগরিকের বা প্রতিষ্ঠানের পক্ষে দূর থেকে কাজ করে দেওয়ার কার্যক্রমই হলো আউটসোর্সিং।}
\itm{$\Rightarrow$} \textbf{\B{ফ্রিল্যান্সিং :}} \B{তথ্য ও যোগাযোগ প্রযুক্তি ব্যবহার করে কোনো প্রতিষ্ঠানের কাজ খণ্ডকালীন বা চুক্তিভিত্তিক পদ্ধতিতে নিজস্ব স্বাধীনভাবে নিজের দক্ষতা অনুযায়ী সম্পাদন করে অর্থ উপার্জনের প্রক্রিয়াই হলো ফ্রিল্যান্সিং।}
\itm{$\Rightarrow$} \textbf{\B{ই-বুক :}} \B{ই-বুক হলো প্রিন্টকৃত বইয়ের অনলাইন বা ডিজিটাল ভার্সন যা ডাউনলোড করে পড়া যায়।}
\itm{$\Rightarrow$} \textbf{\B{ই-লার্নিং :}} \B{গতানুগতিক শ্রেণিকক্ষে শিক্ষাদানের পরিবর্তে অনলাইনে শিক্ষক শিক্ষার্থীদের মধ্যে ইলেকট্রনিক মাধ্যমে বিশেষত কম্পিউটার, ইন্টারনেট ও ওয়েব ব্যবহার করে শিক্ষা কার্যক্রম পরিচালনা করার পদ্ধতিই হলো ই-লার্নিং।}
\itm{$\Rightarrow$} \textbf{\B{ই-কমার্স :}} \B{পণ্য বা সেবা উৎপাদন, মার্কেটিং, ডেলিভারি এবং মূল্য পরিশোধের অনলাইন প্রক্রিয়াকে ই-কমার্স বলে।}
\itm{$\Rightarrow$} \textbf{\B{টেলিমেডিসিন :}} \B{তথ্য ও যোগাযোগ প্রযুক্তির মাধ্যমে দূরবর্তী রোগীদেরকে বিশেষজ্ঞ চিকিৎসক দ্বারা চিকিৎসা সেবা দেওয়ার ব্যবস্থায় হলো টেলিমেডিসিন।}

\chsec{ভার্চুয়াল রিয়েলিটি / VR - Virtual Reality}
\B{\textbf{ভার্চুয়াল রিয়েলিটি}} \B{হলো হার্ডওয়্যার ও সফটওয়্যারের মাধ্যমে তৈরিকৃত এমন এক ধরনের কৃত্রিম পরিবেশ, যা ব্যবহারকারীদের কাছে উপস্থাপন করা হলে এটিকে বাস্তব পরিবেশ বলে মনে হয়।}

\B{ভার্চুয়াল রিয়েলিটি মূলত ৫ প্রকার।}

\B{\textbf{ভার্চুয়াল রিয়েলিটি :}} \B{প্রকৃত অর্থে বাস্তব নয় কিন্তু বাস্তবের চেতনা উদ্রেককারী বিজ্ঞান নির্ভর কল্পনাকে ভার্চুয়াল রিয়েলিটি বা অনুভবে বাস্তবতা কিংবা কল্পনাবাস্তবতা বলে। ভার্চুয়াল রিয়েলিটি হলো সফটওয়্যার নির্মিত একটি কাল্পনিক পরিবেশ। যেখানে ব্যবহারকারী ঐ পরিবেশে মগ্ন হয়ে বাস্তবের অনুকরণে সৃষ্ট দৃশ্য উপভোগ করেন। সেই সাথে বাস্তবের ন্যায় শ্রবণানুভূতি এবং দৈহিক ও মানসিক ভাবাবেগ, অনুভূতি প্রভৃতির অভিজ্ঞতা অর্জন করতে পারেন। যে ব্যবহারকারীর কাছে বাস্তব জগৎ হিসেবে বিবেচিত হয়। অর্থাৎ, এটি এক ধরনের কম্পিউটার নিয়ন্ত্রিত ত্রিমাত্রিক}
\B{ব্যবস্থা যাতে প্রতিটি নির্মাণ (Modelling) এবং ছদ্মায়ন (Simulation) পদ্ধতি ব্যবহারের মাধ্যমে মানুষ কল্পনার জগতে প্রবেশ করতে পারে। ভার্চুয়াল রিয়েলিটিতে মানুষ যা দেখে তা অনুভব করতে পারে। ভার্চুয়াল রিয়েলিটিতে সৃষ্ট পরিবেশ পুরোপুরি বাস্তব পৃথিবীর মতো মনে হয়। ভার্চুয়াল রিয়েলিটি ব্যবহার সম্পূর্ণ কম্পিউটিং সিস্টেম দ্বারা নির্মিত। ভার্চুয়াল রিয়েলিটিতে কল্পনার জগৎকে যেন হুবহু বাস্তব মনে হয়। এক্ষেত্রে অনেক সময় প্রকৃত বাস্তবতা থেকে বাস্তব অভিজ্ঞতা পাওয়া যায়। ভার্চুয়াল রিয়েলিটির গুরুত্বপূর্ণ তিনটি বিষয় হলো - দৃষ্টি, শব্দ ও স্পর্শ। কল্পনার জগতের সবকিছু দেখতে শুনতে ও অনুভব করতে এ ৩ টি উপাদান ভার্চুয়াল রিয়েলিটির ক্ষেত্রে সবচেয়ে গুরুত্বপূর্ণ ভূমিকা পালন করে।}

\chsec{ভার্চুয়াল রিয়েলিটির নেতিবাচক দিক}
\begin{enumerate}
    \item \B{ভার্চুয়াল রিয়েলিটির নেতিবাচক দিক হলো \LAT{De Humanisation} বা মনুষ্যত্বহীনতা। এর ফলে মানুষ সামাজিকতা থেকে দূরে সরে যাবে। বাস্তব জগতের বদলে ভার্চুয়াল জগতে বন্ধু ও পরিবেশ খুঁজবে।}
    \item \B{মানুষ বাস্তব জগৎ থেকে দূরে সরে যাবে এবং বেশিরভাগ সময় কল্পনার জগতে বিচরণ করবে।}
    \item \B{এটি দৃষ্টিশক্তি ও শ্রবণশক্তির ক্ষতি করে।}
\end{enumerate}

\chsec{$\square$ রোবটিক্স}
\B{রোবট \LAT{(Robot)} শব্দটির বাংলা অর্থ যন্ত্রমানব। রোবট হলো কম্পিউটার প্রোগ্রাম দিয়ে নিয়ন্ত্রিত একটি যন্ত্র, যা স্বয়ংক্রিয়ভাবে কিছু কাজ করতে পারে।}\\
\B{\LAT{Robot} শব্দটি মূলত এসেছে চেক শব্দ \LAT{Robota} থেকে। চেক \LAT{(Czech)} ভাষায় \LAT{robota} শব্দের অর্থ \LAT{'forced labour'} (শ্রমিক)}

\chsec{রোবটকে যেসব বৈশিষ্ট্য দেওয়ার চেষ্টা করা হয় :}
\begin{enumerate}
    \item \B{দর্শনেন্দ্রিয় উপলব্ধি \LAT{(Visual Perception)}}
    \item \B{সংস্পর্শ বা স্পর্শনেন্দ্রিয়গ্রাহ্য সক্ষমতা \LAT{(Tactile Capabilities)}}
    \item \B{নিয়ন্ত্রণ ও ম্যানিপুলেশন দক্ষতা বা নিপুণতা \LAT{(Dexterity)}}
    \item \B{যে কোনো স্থানে দৈহিকভাবে নড়াচড়ার ক্ষমতা \LAT{(Locomotion)}}
\end{enumerate}

\chsec{রোবটিক্স কী ?}
\B{প্রযুক্তির যে শাখায় রোবটের নকশা, গঠন বৈশিষ্ট্য ও কাজ সম্পর্কে আলোচনা করা হয় সেই শাখাকে রোবোটিক্স বা রোবটবিজ্ঞান বলা হয়।}

\chsec{রোবোটিক্স বা রোবটের গুরুত্ব ও ব্যবহার}
\begin{enumerate}
    \item \B{খনি থেকে কোনো কিছু আহরণের ক্ষেত্রে}
    \item \B{দুর্গমস্থানে কাজের ক্ষেত্রে রোবট ব্যবহৃত হয়।}
    \item \B{যানবাহন ও গাড়ির কারখানায় রোবট ব্যবহৃত হয়।}
    \item \B{ইদানিং গৃহস্থলির কাজেও রোবটের ব্যবহার হয়ে থাকে।}
    \item \B{বিরক্তিকর ও একঘেঁয়ে কাজের ক্ষেত্রে রোবট ব্যবহার করা হয়।}
    \item \B{চিকিৎসা ক্ষেত্রে সার্জারির কাজে রোবট ব্যবহার করা হয়।}
    \item \B{বিভিন্ন দেশে রোবটের সাহায্যে নিরাপত্তা ব্যবস্থাপনা নিয়ন্ত্রণ করা হয়।}
    \item \B{বর্তমানে কম্পিউটার এইডেড ম্যানুফ্যাকচারিং \LAT{(CAM)} - এ রোবটকে ব্যাপকভাবে ব্যবহার করা হচ্ছে।}
    \item \B{মহাকাশ স্পেস স্থাপনের জন্য মহাকাশ গবেষণার কাজে মানুষের পরিবর্তে রোবট ব্যবহৃত হয়। যেমন: \LAT{Nasa} র সিকিউরিটি রোবট।}
\end{enumerate}

\chsec{রোবট ব্যবহারের অসুবিধাসমূহ}
\begin{enumerate}
    \item \B{১. রোবট তৈরির প্রাথমিক খরচ খুব বেশি।}
    \item \B{রোবট স্বাধীনভাবে চিন্তা করতে পারে না।}
    \item \B{রোবট ভুল থেকে শিক্ষা গ্রহণ করতে পারে না।}
    \item \B{জটিল সিদ্ধান্ত গ্রহণ করার জন্য রোবট সক্ষম নয়।}
    \item \B{রোবট দিয়ে ইচ্ছেমতো বিভিন্ন কাজ করানো যায় না।}
\end{enumerate}

\chsec{$\square$ ক্রায়োসার্জারী}
\B{ক্রায়োসার্জারী হচ্ছে এমন একটি প্রক্রিয়া যার মাধ্যমে শীতল তাপমাত্রায় শরীরের অস্বাভাবিক ও অসুস্থ টিস্যু ধ্বংস করা হয়।}

\chsec{ক্রায়োসার্জারীর প্রক্রিয়া}
\B{ক্রায়োসার্জারীর ক্ষেত্রে শীতলীকরণের জন্য ক্রায়োজেনিক পদার্থ হিসেবে তরল নাইট্রোজেন, কার্বনডাই অক্সাইড, আর্গন ও ডাই মিথাইল ইথার প্রোপেন ব্যবহৃত হয় এবং হিটিং সোর্স হিসেবে হিলিয়াম ব্যবহার করা হয়। এই প্রক্রিয়ায়}
\B{ব্যবস্থা যাতে প্রতিটি নির্মাণ (Modelling) এবং ছদ্মায়ন (Simulation) পদ্ধতি ব্যবহারের মাধ্যমে মানুষ কল্পনার জগতে প্রবেশ করতে পারে। ভার্চুয়াল রিয়েলিটিতে মানুষ যা দেখে তা অনুভব করতে পারে। ভার্চুয়াল রিয়েলিটিতে সৃষ্ট পরিবেশ পুরোপুরি বাস্তব পৃথিবীর মতো মনে হয়। ভার্চুয়াল রিয়েলিটি ব্যবহার সম্পূর্ণ কম্পিউটিং সিস্টেম দ্বারা নির্মিত। ভার্চুয়াল রিয়েলিটিতে কল্পনার জগৎকে যেন হুবহু বাস্তব মনে হয়। এক্ষেত্রে অনেক সময় প্রকৃত বাস্তবতা থেকে বাস্তব অভিজ্ঞতা পাওয়া যায়। ভার্চুয়াল রিয়েলিটির গুরুত্বপূর্ণ তিনটি বিষয় হলো - দৃষ্টি, শব্দ ও স্পর্শ। কল্পনার জগতের সবকিছু দেখতে শুনতে ও অনুভব করতে এ ৩ টি উপাদান ভার্চুয়াল রিয়েলিটির ক্ষেত্রে সবচেয়ে গুরুত্বপূর্ণ ভূমিকা পালন করে।}

\chsec{ভার্চুয়াল রিয়েলিটির নেতিবাচক দিক}
\begin{enumerate}
    \item \B{ভার্চুয়াল রিয়েলিটির নেতিবাচক দিক হলো \LAT{De Humanisation} বা মনুষ্যত্বহীনতা। এর ফলে মানুষ সামাজিকতা থেকে দূরে সরে যাবে। বাস্তব জগতের বদলে ভার্চুয়াল জগতে বন্ধু ও পরিবেশ খুঁজবে।}
    \item \B{মানুষ বাস্তব জগৎ থেকে দূরে সরে যাবে এবং বেশিরভাগ সময় কল্পনার জগতে বিচরণ করবে।}
    \item \B{এটি দৃষ্টিশক্তি ও শ্রবণশক্তির ক্ষতি করে।}
\end{enumerate}

\chsec{$\square$ রোবটিক্স}
\B{রোবট \LAT{(Robot)} শব্দটির বাংলা অর্থ যন্ত্রমানব। রোবট হলো কম্পিউটার প্রোগ্রাম দিয়ে নিয়ন্ত্রিত একটি যন্ত্র, যা স্বয়ংক্রিয়ভাবে কিছু কাজ করতে পারে।}\\
\B{\LAT{Robot} শব্দটি মূলত এসেছে চেক শব্দ \LAT{Robota} থেকে। চেক \LAT{(Czech)} ভাষায় \LAT{robota} শব্দের অর্থ \LAT{'forced labour'} (শ্রমিক)}

\chsec{রোবটকে যেসব বৈশিষ্ট্য দেওয়ার চেষ্টা করা হয় :}
\begin{enumerate}
    \item \B{দর্শনেন্দ্রিয় উপলব্ধি \LAT{(Visual Perception)}}
    \item \B{সংস্পর্শ বা স্পর্শনেন্দ্রিয়গ্রাহ্য সক্ষমতা \LAT{(Tactile Capabilities)}}
    \item \B{নিয়ন্ত্রণ ও ম্যানিপুলেশন দক্ষতা বা নিপুণতা \LAT{(Dexterity)}}
    \item \B{যে কোনো স্থানে দৈহিকভাবে নড়াচড়ার ক্ষমতা \LAT{(Locomotion)}}
\end{enumerate}

\chsec{রোবটিক্স কী ?}
\B{প্রযুক্তির যে শাখায় রোবটের নকশা, গঠন বৈশিষ্ট্য ও কাজ সম্পর্কে আলোচনা করা হয় সেই শাখাকে রোবোটিক্স বা রোবটবিজ্ঞান বলা হয়।}

\chsec{রোবোটিক্স বা রোবটের গুরুত্ব ও ব্যবহার}
\begin{enumerate}
    \item \B{খনি থেকে কোনো কিছু আহরণের ক্ষেত্রে}
    \item \B{দুর্গমস্থানে কাজের ক্ষেত্রে রোবট ব্যবহৃত হয়।}
    \item \B{যানবাহন ও গাড়ির কারখানায় রোবট ব্যবহৃত হয়।}
    \item \B{ইদানিং গৃহস্থলির কাজেও রোবটের ব্যবহার হয়ে থাকে।}
    \item \B{বিরক্তিকর ও একঘেঁয়ে কাজের ক্ষেত্রে রোবট ব্যবহার করা হয়।}
    \item \B{চিকিৎসা ক্ষেত্রে সার্জারির কাজে রোবট ব্যবহার করা হয়।}
    \item \B{বিভিন্ন দেশে রোবটের সাহায্যে নিরাপত্তা ব্যবস্থাপনা নিয়ন্ত্রণ করা হয়।}
    \item \B{বর্তমানে কম্পিউটার এইডেড ম্যানুফ্যাকচারিং \LAT{(CAM)} - এ রোবটকে ব্যাপকভাবে ব্যবহার করা হচ্ছে।}
    \item \B{মহাকাশ স্পেস স্থাপনের জন্য মহাকাশ গবেষণার কাজে মানুষের পরিবর্তে রোবট ব্যবহৃত হয়। যেমন: \LAT{Nasa} র সিকিউরিটি রোবট।}
\end{enumerate}

\chsec{রোবট ব্যবহারের অসুবিধাসমূহ}
\begin{enumerate}
    \item \B{১. রোবট তৈরির প্রাথমিক খরচ খুব বেশি।}
    \item \B{রোবট স্বাধীনভাবে চিন্তা করতে পারে না।}
    \item \B{রোবট ভুল থেকে শিক্ষা গ্রহণ করতে পারে না।}
    \item \B{জটিল সিদ্ধান্ত গ্রহণ করার জন্য রোবট সক্ষম নয়।}
    \item \B{রোবট দিয়ে ইচ্ছেমতো বিভিন্ন কাজ করানো যায় না।}
\end{enumerate}

\chsec{$\square$ ক্রায়োসার্জারী}
\B{ক্রায়োসার্জারী হচ্ছে এমন একটি প্রক্রিয়া যার মাধ্যমে শীতল তাপমাত্রায় শরীরের অস্বাভাবিক ও অসুস্থ টিস্যু ধ্বংস করা হয়।}

\chsec{ক্রায়োসার্জারীর প্রক্রিয়া}
\B{ক্রায়োসার্জারীর ক্ষেত্রে শীতলীকরণের জন্য ক্রায়োজেনিক পদার্থ হিসেবে তরল নাইট্রোজেন, কার্বনডাই অক্সাইড, আর্গন ও ডাই মিথাইল ইথার প্রোপেন ব্যবহৃত হয় এবং হিটিং সোর্স হিসেবে হিলিয়াম ব্যবহার করা হয়। এই প্রক্রিয়ায়}
\chsec{$\boxtimes$ বায়োইনফরমেটিক্স}
\B{বায়োইনফরমেটিক্স জীববিজ্ঞান, কম্পিউটার সায়েন্স, ইনফরমেশন ইঞ্জিনিয়ারিং, গণিত এবং পরিসংখ্যানের সমন্বয়ে গঠিত একটি বিষয়। এই পদ্ধতি ৪ টি ভিন্ন শাখার উপাদান নিয়ে কাজ করে।}
\begin{enumerate}
    \item \B{\textbf{আণবিক জীববিদ্যা ও মেডিসিন :} ডেটা উৎস বিশ্লেষণের কাজ করে।}
    \item \B{\textbf{ডেটাবেজ :} নিরাপদ ডেটা সংরক্ষণ ও ডেটা রিট্রিভ করা।}
    \item \B{\textbf{প্রোগ্রাম :} উপাত্ত বিশ্লেষণ অ্যালগরিদম যার মাধ্যমে বায়োইনফরমেটিক্স কঠোরভাবে সুনির্দিষ্ট করা হয়।}
    \item \B{\textbf{গণিত ও পরিসংখ্যান :} এর সাহায্যে সম্ভাব্যতা যাচাই করা হয়।}
\end{enumerate}

\chsub{}{বায়োইনফরমেটিক্স এর ব্যবহার}
\begin{enumerate}
    \item \B{জিনোম সিকোয়েন্স, প্রোটিন সিকোয়েন্স ইত্যাদি গঠন উপাদানের ইলেকট্রনিক ডেটাবেজ গঠনে কম্পিউটার প্রযুক্তি ব্যবহৃত হয়।}
    \item \B{মলিকুলার মেডিসিন, জিনথেরাপি, ওষুধ তৈরিতে, বর্জ্য পরিষ্কারকরণে, জলবায়ু পরিবর্তন গবেষণায়।}
    \item \B{বিকল্প শক্তির উৎস সন্ধানে, জীবাণু অস্ত্র তৈরিতে, ডিএনএ ম্যাপিং ও অ্যানালাইসিস, জিন ফাইন্ডিং, প্রোটিনের মিথস্ক্রিয়া পর্যবেক্ষণ এটি ব্যবহৃত হয়।}
\end{enumerate}

\chsub{}{বায়োইনফরমেটিক্স এর সুবিধা}
\begin{enumerate}
    \item \B{আণবিক বংশগতিবিদ্যার উন্নয়নে ব্যাপক ভূমিকা পালন করে।}
    \item \B{জীববিজ্ঞান ভিত্তিক তথ্যের গবেষণাতে তথ্যের সংরক্ষণ ও পুনঃব্যবহার নিশ্চিত করা।}
\end{enumerate}

\chsub{}{বায়োইনফরমেটিক্স এর অসুবিধা}
\begin{enumerate}
    \item \B{জেনেটিক তথ্যের গোপনীয়তা ভঙ্গের আশঙ্কা থাকে।}
    \item \B{যেসব চিকিৎসা বায়োইনফরমেটিক্স নির্ভর সেগুলো সুনিয়ন্ত্রিতভাবে পরিচালনা করা হলে রোগীর বড় ধরনের ক্ষতির সম্ভাবনা থাকে।}
    \item \B{এটি একটি ব্যয়বহুল প্রক্রিয়া।}
\end{enumerate}

\chsec{বায়োমেট্রিক্স ও বায়োইনফরমেটিক্স এর পার্থক্য}
\noindent\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|c|X|X|}
\hline
\rowcolor{tblhdr} & \centering\arraybackslash\B{\textbf{বায়োমেট্রিক্স}} & \centering\arraybackslash\B{\textbf{বায়োইনফরমেটিক্স}} \tabularnewline\hline
\LAT{i} & \B{মানুষের বায়োলজিক্যাল ডেটা যেমন: শারীরিক গঠন, আচার-আচরণ, বৈশিষ্ট্য, গুণাগুণ চিহ্নিত বা সনাক্ত করার প্রযুক্তি হলো বায়োমেট্রিক্স।} & \B{জীববিজ্ঞানের সমস্যাগুলো কম্পিউটেশনাল প্রযুক্তি ব্যবহার করে সমাধান করার প্রক্রিয়াই হলো বায়োইনফরমেটিক্স।} \\\hline
\LAT{ii} & \B{ব্যক্তি সনাক্তকরণ ও নিখুঁত নিরাপত্তার জন্য ব্যবহৃত হয়।} & \B{মলিকুলার বা আণবিক জেনেটিক্স এর ভিজ্যুয়ালাইজেশনকে সম্ভব করে তুলতে ব্যবহৃত হয়।} \\\hline
\LAT{iii} & \B{বায়োমেট্রিক্স প্রযুক্তি ফিঙ্গারপ্রিন্ট, ডিএনএ, চোখের আইরিশ, কণ্ঠস্বর ইত্যাদি পরিমাপ এবং বিশ্লেষণ করে সনাক্তকরণ করা হয়।} & \B{বায়োলজিক্যাল ডেটা অ্যানালাইসিস করার জন্য কম্পিউটার প্রযুক্তি, ইনফরমেশন থিওরি এবং গাণিতিক জ্ঞানকে ব্যবহার করে।} \\\hline
\LAT{iv} & \B{এটি তুলনামূলক কম ব্যয়বহুল ও বেশি ব্যবহৃত হয়।} & \B{এটি অত্যন্ত ব্যয়বহুল। প্রকল্প চালিয়ে যেতে প্রচুর অর্থের প্রয়োজন পড়ে।} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsec{$\boxtimes$ ন্যানো টেকনোলজি}
\B{বিজ্ঞান ও প্রযুক্তি ব্যবহার করে এক থেকে একশ ন্যানো মিটার আকৃতির কোনো কিছু তৈরি করা এবং ব্যবহার করাকে ন্যানো টেকনোলজি বলে। এই আকৃতির কোনো কিছু তৈরি করা হলে তাকে ন্যানো পার্টিকেল বলে। $10^{-9}$ m কে ন্যানো মিটার বলে। ন্যানো টেকনোলজি দুই ভাগে বিভক্ত। যথা :}
\begin{itemize}
    \item \B{\textbf{i. ক্ষুদ্র থেকে বৃহৎ (Bottom to Top) :} ক্ষুদ্র হতে ক্ষুদ্র আণবিক উপাদান থেকে বড় কোনো জিনিস তৈরি করা।}
    \item \B{\textbf{ii. বৃহৎ থেকে ক্ষুদ্র (Top to Bottom) :} বৃহৎ কোনো জিনিসকে ভেঙে ভেঙে ক্ষুদ্র ক্ষুদ্র ভাবে বিভক্ত করা।}
\end{itemize}

\chsub{}{ন্যানো টেকনোলজির ব্যবহার}
\begin{enumerate}
    \item \B{\textbf{কম্পিউটার হার্ডওয়্যার :} প্রসেসর এর উচ্চগতি, দীর্ঘস্থায়িত্ব এবং কম খরচ ইত্যাদি বৈশিষ্ট্য ব্যবহার করা হয়।}
    \item \B{\textbf{চিকিৎসাক্ষেত্রে :} ন্যানো রোবট ব্যবহার করে অপারেশন করা হয়। যেমন: ন্যানো ক্রায়োসার্জারী, ডায়াগনোসিস করা হয়, এন্ডোস্কোপি, কলোনোস্কোপি, এনজিও গ্রাম করা হয়}
    \item \B{\textbf{খাদ্যশিল্পে :} দ্রব্য প্যাকেটিং, খাদ্যের স্বাদ তৈরিতে, গুণাগুণ রক্ষার্থে ব্যবহৃত হয়।}
    \item \B{\textbf{জালানীক্ষেত্রে :} হাইড্রোজেন আয়ন থেকে ফুয়েল তৈরিতে, সৌরবিদ্যুৎ উৎপাদন এর জন্য সৌরকোষ তৈরির কাজে ব্যবহৃত হয়।}
    \item \B{\textbf{যোগাযোগক্ষেত্রে :} হালকা ওজনের ও কম জ্বালানী চাহিদা সম্পন্ন গাড়ি প্রস্তুতকরণে ব্যবহৃত হয়।}
    \item \B{\textbf{খেলাধুলার সামগ্রীক্ষেত্রে :} ক্রিকেট, টেনিস বলের স্থায়িত্ব বৃদ্ধির জন্য ও ফুটবল বা গলফ বলের বাতাসের ভারসাম্য রক্ষার্থে ব্যবহৃত হয়।}
\end{enumerate}
\B{৭. বায়ু ও পানি দূষণ রোধে : শিল্প কারখানার ক্ষতিকর রাসায়নিক বর্জ্যকে ন্যানো পার্টিকেল ব্যবহার করে ক্ষতিকর নয় এমন বস্তুতে রূপান্তর করে পানিতে নিষ্কাশিত করা হয়। গাড়ি ও শিল্প কারখানা নির্গত বিষাক্ত ধোঁয়া ন্যানো পার্টিকেলের সাহায্যে দূষণমুক্ত গ্যাসে পরিণত করে বায়ু দূষণ রোধ করা হয়।}
\begin{enumerate}
\item \B{৮. প্রসাধন শিল্প : প্রসাধনতীতে জিংক অক্সাইড এর ন্যানো পার্টিকেল যুক্ত হওয়ায় ত্বকের ক্যান্সার রোধ সম্ভব হয়েছে। ক্রিম তৈরির কাজে ব্যবহৃত রাসায়নিক পদার্থ তৈরির ক্ষেত্রে ব্যবহৃত হয়।}
\end{enumerate}

\chsub{}{ন্যানো টেকনোলজির সুবিধা}
\B{ন্যানো টেকনোলজি ব্যবহার করে উৎপাদিত পণ্য অত্যন্ত মজবুত, টেকসই, আকারে ছোট ও হালকা হয়।}

\chsub{}{ন্যানো টেকনোলজির অসুবিধা}
\begin{enumerate}
    \item \B{১. ন্যানো পার্টিকেল দিয়ে প্রাণঘাতী অস্ত্র তৈরি, প্রচলিত জ্বালানি গ্যাস, তৈল এর বিকল্প হিসেবে অপব্যবহার, কালোবাজারি এবং মানব শরীরের কোষের গঠন শৈলী পরিবর্তনসহ কোষ মেরে ফেলার মতো ক্ষতিকর প্রযুক্তি হিসেবে ন্যানো টেকনোলজি ব্যবহার করা হয়।}
    \item \B{২. এই প্রযুক্তির ক্ষেত্রে অদক্ষরা কর্মহীন হয়ে পড়ে।}
\end{enumerate}

\chsec{$\boxtimes$ জেনেটিক ইঞ্জিনিয়ারিং}
\begin{itemize}
    \item \B{\LAT{DNA} এর পূর্ণরূপ হলো \LAT{Deoxyribo Nucleic Acid}।}
    \item \B{ডিএনএ এর ভিতর ক্ষুদ্র ক্ষুদ্র অংশ সে প্রাণীর জীবনের বৈশিষ্ট্যকে বহন করে সেগুলোকে জিন বলে। জিন হলো বংশগতির ধারক ও বাহক। মানবদেহে ২০,০০০ - ৩০,০০০ জিন রয়েছে।}
    \item \B{একসেট জিনকে জিনোম বলে। জিনোম হলো জীবের বৈশিষ্ট্যের নকশা বা বিন্যাস।}
    \item \B{গবেষণার মাধ্যমে একটি জিন পরিবর্তন করে সেখানে অন্য জিন লাগানো হয় তাকে রিকম্বিনেন্ট ডিএনএ (\LAT{RDNA}) বলে। এই \LAT{RDNA} সমৃদ্ধ জীব কোষকে \LAT{Genetically Modified Organism (GMO)} বলে।}
    \item \B{\LAT{E.coli} ব্যাকটেরিয়া এবং ইস্ট হতে মানবদেহের ইনসুলিন তৈরি করা হয়, হরমোন বৃদ্ধি করা হয় এবং বামনত্ব বৃদ্ধি করা হয়, ভাইরাসজনিত রোগ, ক্যান্সার, এইডস ইত্যাদি চিকিৎসায় জিন প্রযুক্তি ব্যবহার করা হয়।}
    \item \B{ধান গবেষণায় ইনস্টিটিউট উচ্চ ফলনশীল ব্রি (\LAT{BRRI}) জাতের বিভিন্ন বীজ উদ্ভাবন করা হয়।}
\end{itemize}
\begin{center}
\noindent
\textbf{\LAT{Sub: ICT}} \hfill {\bn\Large\bfseries ২য় অধ্যায়} \hfill \textbf{\B{কমিউনিকেশন সিস্টেমস ও নেটওয়ার্কিং}} \\
\textbf{\LAT{Instructor: Antika Saha}} \hfill \hfill \\
\textbf{\LAT{Prepared By Abu Salman}} \hfill \hfill \\
\textbf{\LAT{Whatsapp: 01627-311647}} \hfill \hfill \\
\vspace{3pt}
\end{center}

\chsec{$\square$ কমিউনিকেশন সিস্টেম}
\B{\textbf{কমিউনিকেশন} শব্দটির অর্থ হলো আদান-প্রদান বা বিনিময়। কমিউনিকেশন অর্থ যোগাযোগ। একজনের সাথে আর একজনের পরস্পর তথ্য বিনিময় বা এক স্থান থেকে অন্য স্থানে বা এক যন্ত্র থেকে অন্য যন্ত্রে তথ্য বিনিময় হচ্ছে কমিউনিকেশন।}

\chsub{}{ডেটা কমিউনিকেশন সিস্টেম}
\B{ডেটা কমিউনিকেশন পদ্ধতিতে বিভিন্ন স্থানে অবস্থিত কম্পিউটার হতে কম্পিউটারে অথবা কম্পিউটার ও অন্য কোন ডিভাইস বা যন্ত্রে ডেটা ও তথ্য আদান প্রদান করা হয়। ডেটা কমিউনিকেশনের প্রধান শর্ত হলো কমিউনিকেশনে ডিভাইস ব্যবহৃত হতে হবে। সব ডেটা কমিউনিকেশনই কমিউনিকেশন কিন্তু সব কমিউনিকেশন ডেটা কমিউনিকেশন নয়।}

\chsub{}{মডেম (Modem)}
\B{ডেটা কমিউনিকেশন সিস্টেমে অ্যানালগ সংকেত ও ডিজিটাল সংকেত এর মধ্যে পারস্পরিক পরিবর্তনের জন্য যে ডিভাইস ব্যবহৃত হয় তাকে মডেম (Modem) বলে।} \\
\LAT{Mo $\rightarrow$ Modulation $\rightarrow$ (Analog $\rightarrow$ Digital) Convert} \\
\LAT{Dem $\rightarrow$ Demodulation $\rightarrow$ (Digital $\rightarrow$ Analog) Convert}

\chsub{}{প্রোটোকল (Protocol)}
\B{প্রোটোকল হলো এক গুচ্ছ নিয়ম-নীতি যা কমিউনিকেশন ডিভাইস গুলো সর্বদা মেনে চলে। যেমন: টিসিপি (TCP) / আইপি (IP), হাইপার টেক্সট ট্রান্সফার প্রোটোকল (HTTP), ফাইল ট্রান্সফার প্রোটোকল (FTP)}

\chsub{}{ডেটা কমিউনিকেশন এর উপাদান}
\B{ডেটা কমিউনিকেশনের মৌলিক উপাদান হলো ৫টি। যথা:}
\begin{enumerate}
    \item \B{উৎস/ সোর্স}
    \item \B{প্রেরক বা ট্রান্সমিটার}
    \item \B{কমিউনিকেশন চ্যানেল/ মাধ্যম/ মিডিয়াম}
    \item \B{রিসিভার/ গ্রাহক/ প্রাপক}
    \item \B{গন্তব্য বা ডেস্টিনেশন}
\end{enumerate}

\B{\textbf{1) উৎস বা সোর্স}} \\
\B{ম্যাসেজ বা বার্তা যে যন্ত্রের সাহায্যে প্রেরকের কাছে পাঠানো হয় তাকে উৎস বা সোর্স বলা হয়। যেমন: মাইক্রোফোন, ক্যামেরা, কি-বোর্ড, কম্পিউটার ও মোবাইল ইত্যাদি।}

\B{\textbf{2) প্রেরক বা ট্রান্সমিটার}} \\
\B{ম্যাসেজ বা বার্তা যে যন্ত্রের সাহায্যে কমিউনিকেশন চ্যানেল বা মাধ্যমে পাঠানো হয় তাকে প্রেরক বা ট্রান্সমিটার বলা হয়। যেমন: বেতার কেন্দ্র, রাউটার, টেলিভিশন ও মডেম ইত্যাদি।}

\B{\textbf{3) কমিউনিকেশন চ্যানেল/ মাধ্যম/ মিডিয়াম}} \\
\B{যার মধ্য দিয়ে ডেটা এক স্থান হতে অন্য স্থানে যায় তাকে কমিউনিকেশন চ্যানেল/ মাধ্যম/ মিডিয়াম বলে। যেমন: বিভিন্ন ধরনের তার বা ক্যাবল, পাবলিক টেলিফোন লাইন, তারবিহীন মাধ্যম এর জন্য রেডিওওয়েভ, মাইক্রোওয়েভ ইত্যাদি।}

\B{\textbf{4) রিসিভার/ গ্রাহক/ প্রাপক}} \\
\B{কমিউনিকেশনের মাধ্যমে ডেটা যার কাছে পাঠানো হয় তাকে গ্রাহক বা প্রাপক বা রিসিভার বলে। যেমন: টেলিফোন এক্সচেঞ্জ, মডেম, রাউটার ইত্যাদি।}

\B{\textbf{5) গন্তব্য বা ডেস্টিনেশন}} \\
\B{গ্রাহক থেকে প্রাপ্ত ডেটা সর্বশেষ যে যন্ত্রে বা ডিভাইসে প্রেরণ করা হয় তাকে গন্তব্য ডেস্টিনেশন বলে। যেমন: লাউড স্পিকার, টেলিফোন ও কম্পিউটার ইত্যাদি।}

\chsec{ডেটা ট্রান্সমিশন স্পীড}
\B{প্রতি সেকেন্ডে এক স্থান থেকে অন্য স্থানে কিংবা এক কম্পিউটার থেকে অন্য কম্পিউটারে যে পরিমাণ ডেটা স্থানান্তরিত হয় তাকে ব্যান্ডউইথ বা ডেটা ট্রান্সমিশন স্পীড বলে। \LAT{bps - bit per second} হচ্ছে ব্যান্ডউইথ এর ক্ষুদ্রতম একক।}

\chsub{}{বিপিএস (bps)}
\B{প্রতি সেকেন্ডে কতটি বিট পরিবাহিত হচ্ছে তার পরিমাণকে বিপিএস বা \LAT{bit per second} বলে।}
\begin{itemize}
    \item \B{\LAT{\textbf{Kbps :}} প্রতি সেকেন্ডে ১,০০০ বিট}
    \item \B{\LAT{\textbf{Mbps :}} প্রতি সেকেন্ডে এক মিলিয়ন (১০,০০,০০০) বিট।}
    \item \B{\LAT{\textbf{Gbps :}} প্রতি সেকেন্ডে এক বিলিয়ন (১,০০,০০,০০,০০০) বিট।}
    \item \LAT{\textbf{1 KB} = 1024 Bytes}
    \item \LAT{\textbf{1 Byte} = 8 bits}
    \item \LAT{\textbf{1 MB} = 1024 KB}
    \item \LAT{\textbf{1 GB} = 1024 MB}
    \item \LAT{\textbf{1 TB} = 1024 GB}
\end{itemize}

\chsec{ডেটা ট্রান্সমিশন মেথড}
\B{যে পদ্ধতিতে এক কম্পিউটার থেকে অন্য কম্পিউটারে ডেটা ট্রান্সমিট হয় তাকে ডেটা ট্রান্সমিশন মেথড বলে Crow}

\chsub{}{প্যারালাল ডেটা ট্রান্সমিশন মেথড}
\B{যে ট্রান্সমিশনে ডেটা সমান্তরালভাবে আদান - প্রদান হয় তাকে প্যারালাল ডেটা ট্রান্সমিশন বলে। একাধিক তারের মধ্য দিয়ে ট্রান্সমিট করা হয়। এ ট্রান্সমিশনে ৮ বিট, ১৬ বিট বা ৩২ বিট ইত্যাদি ডেটা চলাচল করতে পারে। যেমন: তার বা ক্যাবল, ইউএসবি পোর্ট, প্রিন্টারে ডেটা পাঠানোর জন্য এ পদ্ধতি ব্যবহার করা হয়।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.0, yscale=0.45]
    \draw[thick] (0,3.5) circle [x radius=0.6, y radius=2.2];
    \node at (0,5.0) [font=\tiny\bfseries] {\LAT{Byte}};
    \node at (0,3.5) [font=\tiny, align=center] {$b_0, b_1, b_2$ \\ $b_3, b_4, b_5$ \\ $b_6, b_7$};
    
    \draw[thick] (5,3.5) circle [x radius=0.6, y radius=2.2];
    \node at (5,5.0) [font=\tiny\bfseries] {\LAT{Byte}};
    \node at (5,3.5) [font=\tiny, align=center] {$b_0, b_1, b_2$ \\ $b_3, b_4, b_5$ \\ $b_6, b_7$};
    
    \node at (2.5, 6.2) [font=\tiny\bfseries] {\LAT{Parallel Communication}};
    
    \foreach \i in {0,...,7} {
        \draw[-{Stealth[scale=0.8]}] (0.6, \i) -- (4.4, \i);
        \node[draw, circle, fill=white, inner sep=0.5pt, font=\tiny] at (1.5 + \i*0.25, \i) {$b_\i$};
    }
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{প্যারালাল ডেটা ট্রান্সমিশন এর সুবিধা}
\begin{enumerate}
    \item \B{এ পদ্ধতি দ্রুতগতি সম্পন্ন।}
    \item \B{একসাথে অনেক বিট চলাচল করতে পারে।}
    \item \B{ডেটা এক একটি শব্দ বা ওয়ার্ড অনুসারে স্থানান্তরিত হয়।}
\end{enumerate}

\chsub{}{প্যারালাল ডেটা ট্রান্সমিশন এর অসুবিধা}
\begin{enumerate}
    \item \B{দূরত্ব বেশি হলে এটি ব্যবহার করা সম্ভব নয়।}
    \item \B{প্রতিটি বিটের জন্য পৃথক পৃথক তার ব্যবহার করায় এটি অত্যন্ত ব্যয়বহুল।}
\end{enumerate}

\chsub{}{সিরিয়াল ডেটা ট্রান্সমিশন মেথড}
\B{প্রেরক ও প্রাপকের মধ্যে ধারাবাহিকভাবে একটি বিটের পর অপর একটি বিট চলাচল করলে তাকে সিরিয়াল ডেটা ট্রান্সমিশন বলে। ১ বাইট বা ৮ বিটের ডেটা পর্যায়ক্রমে ১ বিট করে আদান - প্রদান করে। যেমন:- মডেম, মাউস, কী-বোর্ড, ইউএসবি (\LAT{USB : Universal Serial Bus}) পোর্ট এবং আরও কিছু যন্ত্রে ডেটা পাঠানোর জন্য এ পদ্ধতি ব্যবহৃত হয়।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.0, yscale=1.0]
    \draw[thick] (0,0) circle [x radius=0.5, y radius=0.6];
    \node at (0,0.3) [font=\tiny\bfseries] {\LAT{Byte}};
    \node at (0,-0.1) [font=\tiny] {$b_0, b_1 \dots b_7$};
    
    \draw[thick] (6,0) circle [x radius=0.5, y radius=0.6];
    \node at (6,0.3) [font=\tiny\bfseries] {\LAT{Byte}};
    \node at (6,-0.1) [font=\tiny] {$b_0, b_1 \dots b_7$};
    
    \node at (3, 0.9) [font=\tiny\bfseries] {\LAT{Serial Communication}};
    
    \draw[-{Stealth[scale=0.8]}] (0.5, 0) -- (5.5, 0);
    
    \foreach \i in {0,...,7} {
        \node[draw, circle, fill=white, inner sep=0.7pt, font=\tiny] at (1.4 + \i*0.4, 0) {$b_\i$};
    }
\end{tikzpicture}
\end{adjustbox}
\end{center}
\chsub{}{সিরিয়াল ডেটা ট্রান্সমিশন এর সুবিধা}
\begin{enumerate}
    \item \B{ডেটা স্থানান্তরের জন্য মাত্র ১টি লাইনের প্রয়োজন হয়।}
    \item \B{কম খরচে ট্রান্সমিশন লাইন অনেক দূর পর্যন্ত বিস্তৃত করা যেতে পারে।}
    \item \B{একটি মাত্র লাইন ব্যবহারের কারণে কোনো সিনক্রোনাইজেশনের প্রয়োজন হয় না।}
\end{enumerate}

\chsub{}{সিরিয়াল ডেটা\B{ট্রান্স}মিশন মেথড এর অসুবিধা}
\begin{enumerate}
    \item \B{এটি ধীরগতি সম্পন্ন।}
    \item \B{একই সময়ে একটি মাত্র বিট স্থানান্তরিত হয়।}
\end{enumerate}

\chsec{সিরিয়াল ও প্যারালাল ডেটা ট্রান্সমিশন মেথডের পার্থক্য}
\noindent\scriptsize
\setlength{\tabcolsep}{2pt}
\begin{tabularx}{\linewidth}{|X|X|X|}
\hline
\rowcolor{tblhdr} & \centering\arraybackslash\B{\textbf{সিরিয়াল}} & \centering\arraybackslash\B{\textbf{প্যারালাল}} \tabularnewline\hline
\centering\arraybackslash\B{\textbf{ডেটা}} & \centering\arraybackslash\B{১ বিট} & \centering\arraybackslash\B{৮/১৬/৩২ বিট} \\\hline
\centering\arraybackslash\B{\textbf{পথ}} & \centering\arraybackslash\B{১টি} & \centering\arraybackslash\B{৮/১৬/৩২টি} \\\hline
\centering\arraybackslash\B{\textbf{গতি}} & \centering\arraybackslash\B{কম} & \centering\arraybackslash\B{বেশি} \\\hline
\centering\arraybackslash\B{\textbf{খরচ}} & \centering\arraybackslash\B{কম} & \centering\arraybackslash\B{বেশি} \\\hline
\end{tabularx}
\setlength{\tabcolsep}{1.4pt}
\normalsize

\chsub{}{ক্লক পালস}
\B{ক্লকের প্রতি পালসে একটি করে বিট প্রেরণ এবং গ্রহণ করা হয়। ক্লক পালস বলতে একটি ক্লক সংকেতের সক্রিয় অবস্থাকে বুঝানো হয়েছে।}

\chsub{}{বিট সিনক্রোনাইজেশন}
\B{সিরিয়াল ডেটা ট্রান্সমিশন পদ্ধতিতে সিগন্যাল পাঠানোর সময় এই ক্লক ব্যবহার করে বিটের শুরু ও শেষ বোঝার জন্য একটি বিশেষ পদ্ধতি ব্যবহৃত হয়, যাকে বিট সিনক্রোনাইজেশন বলে। এর কারণেই প্রাপক সিগন্যাল থেকে ডেটা সনাক্ত এবং পুনরুদ্ধার করতে পারে।}

\B{বিট সিনক্রোনাইজেশন এর উপর ভিত্তি করে সিরিয়াল ডেটা ট্রান্সমিশন তিন ভাগে বিভক্ত। যথা}
\begin{itemize}
    \item \B{i. অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন।}
    \item \B{ii. সিনক্রোনাইজেশন/ সিনক্রোনাস ট্রান্সমিশন।}
    \item \B{iii. আইসোক্রোনাইজেশন/ আইসোক্রোনাস ট্রান্সমিশন।}
\end{itemize}

\chsub{}{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ডেটা ট্রান্সমিশন মেথড}
\B{যে ডেটা ট্রান্সমিশন সিস্টেমে প্রেরক হতে ডেটা প্রাপকের কাছে ক্যারেক্টার (বর্ণ, সংখ্যা বা চিহ্ন) বাই ক্যারেক্টার ট্রান্সমিট হয় তাকে অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন বলে।}

\chsub{}{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ডেটা ট্রান্সমিশন এর প্রক্রিয়া}
\begin{enumerate}
    \item \B{প্রেরক যেকোনো সময় ডেটা ট্রান্সমিট করতে পারবে এবং গ্রাহকও তা গ্রহণ করবে।}
    \item \B{একটি ক্যারেক্টার ট্রান্সমিট হওয়ার পর আরেকটি ক্যারেক্টার ট্রান্সমিট করার মাঝখানের বিরতি সবসময় সমান না হয়েও ভিন্ন ভিন্ন হতে পারে।}
    \item \B{প্রতিটি ক্যারেক্টার এর শুরুতে একটি স্টার্ট বিট এবং শেষে একটি বা দুইটি স্টপ বিট ট্রান্সমিট করা হয়। ফলে প্রতিটি ক্যারেক্টার এর ডেটা ১০/১১ বিটের ডেটায় রূপান্তরিত হয়ে ট্রান্সমিট হয়। এই ট্রান্সমিশনকে স্টার্ট/ স্টপ ট্রান্সমিশন বলা হয়।}
    \item \B{স্টার্ট বিট দেখে গ্রাহক বুঝতে পারে ডেটা আসতে শুরু করেছে এবং ক্লক সেই বিটের সাথে সমন্বয় করে নেয়। স্টপ বিট দেখে গ্রাহক বুঝতে পারে ডেটা পাঠানো শেষ হয়েছে।}
    \item \B{প্রাইমারি স্টোরেজ ডিভাইসের (Ram, Cache, CPU memory) প্রয়োজন হয় না।}
    \item \B{ক্যারেক্টারের ট্রান্সমিশনের সময় বিরতি সমান না হওয়ায় এর ডেটা স্থানান্তরের গতি ধীর হয়।}
\end{enumerate}

\chsub{}{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন মেথডের ব্যবহার}
\begin{enumerate}
    \item \B{কম্পিউটার হতে প্রিন্টারে ডেটা স্থানান্তরে।}
    \item \B{কী-বোর্ড হতে কম্পিউটারে ডেটা স্থানান্তরে।}
\end{enumerate}
\begin{enumerate}
\item \B{৩. পাঞ্চকার্ড রিডার হতে কম্পিউটারে স্থানান্তরে এবং কম্পিউটার হতে পাঞ্চকার্ডে স্থানান্তরে।}
\end{enumerate}

\chsub{}{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন মেথডের সুবিধা}
\begin{enumerate}
    \item \B{প্রেরক যেকোনো সময় ডেটা স্থানান্তর করতে পারেন এবং গ্রাহক তা গ্রহণ করতে পারে।}
    \item \B{এটির ইনস্টলেশন ব্যয় অত্যন্ত কম।}
\end{enumerate}

\chsub{}{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন মেথডের অসুবিধা}
\begin{enumerate}
    \item \B{ডেটা ট্রান্সমিশনে গতি অপেক্ষাকৃত ধীর।}
\end{enumerate}

\chsub{}{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথড}
\B{যে ডেটা ট্রান্সমিশন সিস্টেমে প্রেরক স্টেশনে প্রথমে ডেটাকে কোনো প্রাইমারি স্টোরেজ ডিভাইসে সংরক্ষণ করে নেওয়া হয়। অতঃপর ডেটার ক্যারেক্টার সমূহকে ব্লক বা প্যাকেট বা ফ্রেম আকারে ভাগ করে প্রতিবারে একটি করে ব্লক ট্রান্সমিট করা হয় তাকে সিনক্রোনাইজেশন/ সিনক্রোনাস ট্রান্সমিশন বলে।}

\chsub{}{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের প্রক্রিয়া}
\begin{enumerate}
    \item \B{এই পদ্ধতিতে বিরতিহীনভাবে প্রেরক যন্ত্র থেকে গ্রাহক যন্ত্রে ডেটা পাঠানো হয়। একে বিরতিহীন ডেটা ট্রান্সমিশন বলে।}
    \item \B{যেহেতু প্রেরিত ডেটা ব্যবহার করে গ্রাহক যন্ত্র তার ক্লককে সমন্বিত করে তাই প্রেরণ করার জন্য কোনো ডেটা না থাকলেও আইডল সিকোয়েন্স হিসেবে পূর্ব নির্ধারিত ডেটা পাঠানো হয়।}
    \item \B{প্রতিবার একটি করে ব্লক ক্লকের সাথে সমন্বয় করে সমান বিরতি দিয়ে প্রেরণ করা হয়।}
    \item \B{প্রতি ব্লকের শুরুতে ১ বা ২ বাইটের একটি হেডার ইনফরমেশন এবং ব্লক ডেটার শেষে ১ বা ২ বাইটের একটি ট্রেইলার ইনফরমেশন সিগন্যাল পাঠানো হয়।}
    \item \B{গ্রাহক যন্ত্র হেডার সিগন্যাল ব্যবহার করে প্রেরকের ক্লকের স্পিডের সাথে সিনক্রোনাইজ বা সমন্বিত করে। ট্রেইলার ব্লকের শেষ নির্দেশ করে এবং কোনো কোনো ব্লকের ক্ষেত্রে ব্লকের ভেতরকার ভুল নির্ণয় এবং সংশোধনে সহায়তা করে।}
    \item \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয়।}
\end{enumerate}

\chsub{}{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের ব্যবহার}
\begin{enumerate}
    \item \B{কম্পিউটার হতে কম্পিউটারে ডেটা স্থানান্তরে।}
    \item \B{দূরবর্তী কোনো স্থানে ডেটা স্থানান্তরে।}
    \item \B{একই সাথে অনেকগুলো কম্পিউটারে ডেটা স্থানান্তরের ক্ষেত্রে।}
\end{enumerate}

\chsub{}{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের সুবিধা}
\begin{enumerate}
    \item \B{অবিরাম ট্রান্সমিশন কাজ চলতে থাকার ফলে তার ট্রান্সমিশন গতি অপেক্ষাকৃত বেশি।}
    \item \B{প্রতি ক্যারেক্টারের শুরু ও শেষে স্টার্ট ও স্টপ বিটের প্রয়োজন হয় না।}
    \item \B{প্রতি ক্যারেক্টারের পর টাইম ইন্টারভেল এর প্রয়োজন হয় না।}
    \item \B{তুলনামূলক কম সময় লাগে।}
\end{enumerate}

\chsub{}{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের অসুবিধা}
\begin{enumerate}
    \item \B{১) তুলনামূলকভাবে ব্যয়বহুল।}
\end{enumerate}

\chsub{}{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথড}
\B{অ্যাসিনক্রোনাস ও সিনক্রোনাস এর একটি মিশ্র পদ্ধতি হচ্ছে আইসোক্রোনাইজেশন/ আইসোক্রোনাস।}

\chsub{}{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথডের প্রক্রিয়া}
\begin{enumerate}
    \item \B{সিনক্রোনাস পদ্ধতির স্টার্ট ও স্টপ বিটের মাঝখানে সিনক্রোনাস পদ্ধতিতে ব্লক আকারে ডেটা ট্রান্সফার হয়।}
    \item \B{যখন প্রয়োজন তখন সেই ডেটা ট্রান্সমিট করা যায়।}
    \item \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয় না।}
    \item \B{ডেটা পাঠানোর শুরুতে স্টার্ট সিগন্যাল ও ডেটা পাঠানোর শেষে স্টপ সিগন্যাল পাঠানো হয়।}
\end{enumerate}
\chsub{}{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথডের ব্যবহার}
\B{সাধারণত রিয়াল টাইম অ্যাপ্লিকেশনের ডেটা ট্রান্সফারে এ পদ্ধতি বেশি ব্যবহৃত হয়। যেমন: লাইভ টিভি, সম্প্রচার, স্ট্রিমিং ভিডিও, অডিও বা ভিডিও কলের ক্ষেত্রে ইত্যাদি।}

\chsub{}{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা\B{ট্রান্স}মিশন মেথডের সুবিধা}
\begin{enumerate}
    \item \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয় না।}
    \item \B{যখন প্রয়োজন তখন ডেটা পাঠাতে সক্ষম।}
\end{enumerate}

\chsub{}{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথডের অসুবিধা}
\begin{enumerate}
    \item \B{১) ডেটা পুনঃপ্রেরণ সম্ভব নয় বলে ডেটা প্রেরণের ক্ষেত্রে ভুল ত্রুটি সনাক্ত করা যায় না।}
    \item \B{২) ডেটা ব্লক প্রাপকের নিকট সঠিকভাবে পৌঁছেছে কিনা তা পরীক্ষা করে দেখার উপায় ও ভুল সংশোধনের ব্যবস্থা নেই। এজন্য এটি সকলক্ষেত্রে নির্ভরযোগ্য পদ্ধতি নয়।}
\end{enumerate}

\chsec{$\square$ ডেটা ট্রান্সমিশন মোড}
\B{উৎস থেকে গন্তব্যে ডেটা ট্রান্সফারের ক্ষেত্রে ডেটা প্রবাহের দিককে ডেটা ট্রান্সমিশন মোড বলে।} \\
\B{ডেটা ট্রান্সমিশন মোড ৩ প্রকার। যথা:}
\begin{enumerate}
    \item \B{সিমপ্লেক্স (Simplex)}
    \item \B{হাফ-ডুপ্লেক্স (Half - Duplex)}
    \item \B{ফুল ডুপ্লেক্স (Full - Duplex)}
\end{enumerate}

\chsub{}{সিমপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{সিমপ্লেক্স ডেটা ট্রান্সমিশন মোডে কেবলমাত্র একদিকে ডেটা প্রেরণের ব্যবস্থা থাকে। অর্থাৎ এই ব্যবস্থায় ডেটা গ্রহণ অথবা প্রেরণের যেকোনো একটি সম্ভব। যে প্রান্ত ডেটা প্রেরণ করবে সে প্রান্ত গ্রহণ করতে পারবে না এবং গ্রহণ প্রান্ত প্রেরণ করতে পারে না। যেমন: রেডিও ও টিভি ব্রডকাস্ট, কম্পিউটার থেকে প্রিন্টারে ডেটা প্রেরণ, কী-বোর্ড থেকে কম্পিউটারে ডেটা প্রেরণ ইত্যাদি।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.0, yscale=1.0]
    \draw[thick] (0,0) rectangle (1.2,0.8);
    \node at (0.6,0.5) [font=\tiny\bfseries] {\LAT{Sender}};
    \node at (0.6,0.15) [font=\tiny] {\LAT{Device 1}};
    
    \draw[-{Stealth[scale=0.8]}, thick] (1.5,0.4) -- (3.5,0.4);
    \node at (2.5,0.6) [font=\tiny, scale=0.7] {\LAT{Direction of flow at all time}};
    
    \draw[thick] (3.8,0.0) rectangle (5.0,0.8);
    \node at (4.4,0.5) [font=\tiny\bfseries] {\LAT{Receiver}};
    \node at (4.4,0.15) [font=\tiny] {\LAT{Device 2}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{হাফ ডুপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{হাফ ডুপ্লেক্স ডেটা ট্রান্সমিশন মোডে উভয় দিক থেকে ডেটা প্রেরণের বা গ্রহণের সুযোগ থাকে, তবে তা একই সময় বা যুগপৎ সম্ভব নয়। যেকোনো প্রান্ত একই সময় কেবলমাত্র ডেটা গ্রহণ অথবা প্রেরণ করতে পারে, কিন্তু গ্রহণ এবং প্রেরণ একই সাথে করতে পারে না। যেমন: ওয়াকিটকি}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.0, yscale=1.0]
    \draw[thick] (0,0) rectangle (1.2,0.9);
    \node at (0.6,0.65) [font=\tiny\bfseries] {\LAT{Sender}};
    \node at (0.6,0.45) [font=\tiny\bfseries] {\LAT{Receiver}};
    \node at (0.6,0.15) [font=\tiny] {\LAT{Device 1}};
    
    \draw[-{Stealth[scale=0.8]}, thick] (1.5,0.65) -- (3.5,0.65);
    \node at (2.5,0.8) [font=\tiny, scale=0.7] {\LAT{Direction of flow at time t1}};
    
    \draw[{Stealth[scale=0.8]}-, thick] (1.5,0.25) -- (3.5,0.25);
    \node at (2.5,0.1) [font=\tiny, scale=0.7] {\LAT{Direction of flow at time t2}};
    
    \draw[thick] (3.8,0.0) rectangle (5.0,0.9);
    \node at (4.4,0.65) [font=\tiny\bfseries] {\LAT{Receiver}};
    \node at (4.4,0.45) [font=\tiny\bfseries] {\LAT{Sender}};
    \node at (4.4,0.15) [font=\tiny] {\LAT{Device 2}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{ফুল ডুপ্লেক্স ডেটা ট্রান্সমিশন মোড}
\B{ফুল ডুপ্লেক্স ডেটা ট্রান্সমিশন মোডে একই সময়ে উভয় দিক হতে ডেটা প্রেরণের ব্যবস্থা থাকে। যেকোনো প্রয়োজনে ডেটা প্রেরণ করার সময় ডেটা গ্রহণ অথবা গ্রহণের সময় প্রেরণও করতে পারবে। যেমন: টেলিফোন, মোবাইল}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.0, yscale=1.0]
    \draw[thick] (0,0) rectangle (1.2,0.9);
    \node at (0.6,0.65) [font=\tiny\bfseries] {\LAT{Sender}};
    \node at (0.6,0.45) [font=\tiny\bfseries] {\LAT{Receiver}};
    \node at (0.6,0.15) [font=\tiny] {\LAT{Device 1}};
    
    \draw[-{Stealth[scale=0.8]}, thick] (1.5,0.55) -- (3.5,0.55);
    \draw[{Stealth[scale=0.8]}-, thick] (1.5,0.35) -- (3.5,0.35);
    \node at (2.5,0.75) [font=\tiny, scale=0.7] {\LAT{Direction of flow at all time}};
    
    \draw[thick] (3.8,0.0) rectangle (5.0,0.9);
    \node at (4.4,0.65) [font=\tiny\bfseries] {\LAT{Receiver}};
    \node at (4.4,0.45) [font=\tiny\bfseries] {\LAT{Sender}};
    \node at (4.4,0.15) [font=\tiny] {\LAT{Device 2}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{ডেটা বিতরণ বা ডেলিভারি মোড}
\B{প্রাপকের সংখ্যা ও ডেটা গ্রহণের অধিকারের উপর ভিত্তি করে ডেটা বিতরণ বা ডেলিভারি মোড তিন ভাগে বিভক্ত। যথা:}
\begin{enumerate}
    \item \B{ইউনিকাস্ট}
    \item \B{মাল্টিকাস্ট}
    \item \B{ব্রডকাস্ট}
\end{enumerate}
\chsub{}{ইউনিকাস্ট}
\B{ইউনিকাস্ট ব্যবস্থায় একটি প্রেরক থেকে শুধুমাত্র একটি প্রাপকই ডেটা গ্রহণ করতে পারে। অনেক প্রাপক একসাথে ডেটা গ্রহণ করতে পারে না। এটি \LAT{1 To 1} নামে পরিচিত।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[yscale=0.5]
    \node[draw, circle, fill=black, inner sep=1.5pt] (S) at (0,3) {};
    \node at (-0.6,3) [font=\tiny\bfseries] {\LAT{Sender}};
    
    \foreach \y in {0,...,6} {
        \node[draw, circle, fill=white, inner sep=1.5pt] (R\y) at (2,\y) {};
    }
    
    \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R4);
    
    \node at (1,-1) [font=\tiny\bfseries, align=center] {\LAT{Unicast} \\ \LAT{(one-to-one)}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{মাল্টিকাস্ট}
\B{মাল্টিকাস্ট মোডে নেটওয়ার্কের কোনো একটি নোড থেকে ডেটা প্রেরণ করলে তা নেটওয়ার্কের অধীনস্থ সকল নোডই গ্রহণ করতে পারে না। শুধুমাত্র একটি গ্রুপের সকল সদস্য গ্রহণ করতে পারে। এটি \LAT{1 To N} মোড নামেও পরিচিত।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[yscale=0.5]
    \node[draw, circle, fill=black, inner sep=1.5pt] (S) at (0,3) {};
    
    \foreach \y in {0,...,6} {
        \node[draw, circle, fill=white, inner sep=1.5pt] (R\y) at (2,\y) {};
    }
    
    \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R2);
    \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R3);
    \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R4);
    \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R5);
    
    \node at (1,-1) [font=\tiny\bfseries, align=center] {\LAT{Multicast} \\ \LAT{(one-to-many)}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{ব্রডকাস্ট}
\B{ব্রডকাস্ট মোডে নেটওয়ার্কের কোনো একটি নোড থেকে ডেটা প্রেরণ করলে তা নেটওয়ার্কের অধীনস্থ সকল নোডই গ্রহণ করে। একে \LAT{1 to All} মোডও বলা হয়। এক্ষেত্রে ১টি প্রেরক থেকে নেটওয়ার্কের অধীনস্থ সকল প্রাপক ডেটা গ্রহণ করতে পারে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[yscale=0.5]
    \node[draw, circle, fill=black, inner sep=1.5pt] (S) at (0,3) {};
    
    \foreach \y in {0,...,6} {
        \node[draw, circle, fill=white, inner sep=1.5pt] (R\y) at (2,\y) {};
        \draw[-{Stealth[scale=0.8]}, thick] (S) -- (R\y);
    }
    
    \node at (1,-1) [font=\tiny\bfseries, align=center] {\LAT{Broadcast} \\ \LAT{(one-to-all)}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsec{$\square$ কম্পিউটার নেটওয়ার্ক}
\B{পরস্পর ডেটা আদান - প্রদানের লক্ষ্যে বিভিন্ন কম্পিউটার কোনো যোগাযোগ মাধ্যম দ্বারা একসঙ্গে যুক্ত থাকলে তাকে কম্পিউটার নেটওয়ার্ক বলে। ইন্টারনেট হচ্ছে পৃথিবীর বৃহত্তম কম্পিউটার নেটওয়ার্ক।}

\chsub{}{কম্পিউটার নেটওয়ার্কের উদ্দেশ্য}
\begin{enumerate}
    \item \B{হার্ডওয়্যার রিসোর্স শেয়ার।}
    \item \B{সফটওয়্যার রিসোর্স শেয়ার।}
    \item \B{ইনফরমেশন রিসোর্স শেয়ার।}
\end{enumerate}

\chsub{}{নেটওয়ার্ক ডিভাইস}
\B{কম্পিউটার নেটওয়ার্ক তৈরি করার জন্য কম্পিউটারগুলো যুক্ত করতে যেসব যন্ত্রপাতি ব্যবহার করা হয় সেগুলোকে নেটওয়ার্ক ডিভাইস বলে। নেটওয়ার্ক ডিভাইস গুলো হলো: গেটওয়ে, রাউটার, মডেম, হাব, রিপিটার, সুইচ ও নেটওয়ার্ক ইন্টারফেস কার্ড (\LAT{NIC})}

\chsub{}{হাব}
\B{হাব এক ধরনের নেটওয়ার্কিং ডিভাইস যা এর আওতাধীন ডিভাইসগুলোকে একত্রে সংযুক্ত করে। হাব এর পোর্টগুলোতে কম্পিউটারের নেটওয়ার্কিং পোর্টগুলো সংযুক্ত করা হলে একটি ল্যান তৈরি করা হয়। হাব এর ভেতরে কোনো বুদ্ধিমত্তা নেই। হাব এর কাছে প্রেরিত সিগন্যাল গ্রহণ করার পর তা একই সাথে এর সাথে সংযুক্ত সকল কম্পিউটারে পাঠায়। অর্থাৎ সিগন্যাল ব্রডকাস্ট করে। এক্ষেত্রে সংকেতটি বা সিগন্যালটি যে ডিভাইসের জন্য পাঠানো হয়েছে সে ডিভাইসটি শুধু সংকেত গ্রহণ করে। বাকি ডিভাইসগুলো সংকেত গ্রহণ করা থেকে বিরত থাকে। এর ফলে ডেটা কলিশন বা সংঘর্ষের আশংকা থাকে এবং নেটওয়ার্কের ট্রাফিক বেড়ে যায়।}

\chsub{}{সুইচ}
\B{সুইচ এক ধরণের নেটওয়ার্কিং ডিভাইস। যা এর আওতাধীন ডিভাইসগুলোকে একত্রে সংযুক্ত করে। সুইচের বুদ্ধিমত্তা রয়েছে। সুইচে প্রেরিত সিগন্যাল গ্রহণ করার পর এটি শুধুমাত্র টার্গেট কম্পিউটারে পাঠায়। অর্থাৎ সুইচ সিগন্যাল}
\B{মাল্টিকাস্ট করে। অর্থাৎ সুইচ সিগন্যালকে ইউনিকাস্ট করে। সুইচ নেটওয়ার্ককে ডেটার মধ্যে সংঘর্ষ এড়ানোর জন্য প্রতিটি কম্পিউটারের Mac এড্রেস ব্যবহার করে শুধু নির্দিষ্ট পোর্টে সিগন্যাল পাঠায়। এমনকি দুর্বল হয়ে পড়া সিগন্যালকে অ্যামপ্লিফাই করে গন্তব্য কম্পিউটারে প্রেরণ করে। একটি সুইচ দিয়ে একটি ল্যান তৈরি করা যায়। একাধিক ল্যান তৈরি করা সম্ভব নয়। ডেটা ফিল্টারিং করা যায়।}

\chsub{}{রাউটার}
\B{রাউটার একটি নেটওয়ার্কিং ডিভাইস। যা একই প্রোটোকল ভুক্ত দুই বা ততোধিক ডিভাইসের মধ্যে ডেটার প্যাকেট পৌঁছে দেয়। ভিন্ন ভিন্ন গঠনে একদিক WAN সংযুক্ত করতে রাউটার ব্যবহৃত হয় এবং WAN এর সাথে LAN সংযুক্ত করতে এটি ব্যবহৃত হয়। এটি ডেটা ফিল্টারিং করতে পারে।}

\chsub{}{গেটওয়ে}
\B{ভিন্ন প্রোটোকল বিশিষ্ট নেটওয়ার্কের মধ্যে সংযোগ স্থাপনের জন্য গেটওয়ে ব্যবহার করা হয়। একে প্রোটোকল কনভার্টার বলে। এটি ডেটা ফিল্টারিং করতে পারে।}

\chsub{}{নেটওয়ার্ক}
\B{কম্পিউটার বা অন্য কোনো ডিভাইসকে নেটওয়ার্কে যুক্ত করার জন্য যে ইন্টারফেস কার্ড ব্যবহার করা হয় তাকে নেটওয়ার্ক ইন্টারফেস কার্ড বা NIC বলে।}

\chsec{$\square$ নেটওয়ার্ক টপোলজি (Network Topology)}
\B{লোকাল এরিয়া নেটওয়ার্কভুক্ত কম্পিউটার ও অন্যান্য যন্ত্রপাতির ভৌত সংযোগ বিন্যাস এবং নির্বিঘ্নে ডেটা আদান প্রদানের যুক্তি নির্ভর সু-নিয়ন্ত্রিত পথের পরিকল্পনা এই দুইয়ের সমন্বিত ধারণাই নেটওয়ার্ক টপোলজি। নেটওয়ার্ক টপোলজি ৬ প্রকার যথা:}
\begin{enumerate}
    \item \B{বাস টপোলজি}
    \item \B{স্টার টপোলজি}
    \item \B{রিং টপোলজি}
    \item \B{ট্রি টপোলজি}
    \item \B{মেশ টপোলজি}
    \item \B{হাইব্রিড টপোলজি}
\end{enumerate}

\chsub{}{বাস টপোলজি}
\B{বাস টপোলজিতে একটি সংযোগ লাইনের সাথে সব ধরনের নোড অর্থাৎ কম্পিউটার ও অন্যান্য যন্ত্রপাতি যুক্ত থাকে। এ সংযোগ লাইনকে বাস টপোলজি বলে। যা কো-অ্যাক্সিয়াল ও ফাইবার অপটিক ক্যাবল দ্বারা তৈরি। এ ক্যাবলটি নেটওয়ার্কের মেরুদন্ড হিসেবে কাজ করে। এ লাইনের দুই প্রান্তে দুটি টার্মিনেটর থাকে। ডেটা প্রবাহ দ্বিমুখী। ডেটা ও লাইনের মাধ্যমে প্রবাহিত হয়। শুধুমাত্র প্রাপক কম্পিউটারে ডেটা গ্রহণ করে এবং অন্য গুলো ডেটা গ্রহণ থেকে বিরত থাকবে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[xscale=1.2, yscale=1.0]
    \draw[ultra thick] (-0.5,0) -- (4.5,0);
    
    \draw[thick, fill=black] (-0.5,-0.2) rectangle (-0.4,0.2);
    \draw[thick, fill=black] (4.4,-0.2) rectangle (4.5,0.2);
    
    \foreach \x in {0, 2, 4} {
        \draw[thick] (\x,0) -- (\x,0.6);
        \draw[thick, fill=gray!30] (\x,0.6) circle (0.25);
    }
    
    \foreach \x in {1, 3} {
        \draw[thick] (\x,0) -- (\x,-0.6);
        \draw[thick, fill=gray!30] (\x,-0.6) circle (0.25);
    }
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{বাস টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{কম তার এবং সরল সংগঠনের কারণে বাস টপোলজি ইনস্টলেশন সহজ ও সাশ্রয়ী।}
    \item \B{কানেক্টর বা রিপিটার দ্বারা সহজেই নেটওয়ার্কের ব্যাকবোন বাস এর দৈর্ঘ্য বৃদ্ধি করে নেটওয়ার্কের সম্প্রসারণ ঘটানো যায়।}
    \item \B{নেটওয়ার্কে যে কোনো সময়ে নতুন নতুন ডিভাইস বা কম্পিউটার সংযুক্ত করা যায়।}
    \item \B{কোনো কম্পিউটার বিচ্ছিন্নকরণ বা নষ্ট হলেও সম্পূর্ণ নেটওয়ার্ক অচল হয়ে পড়ে না।}
    \item \B{নেটওয়ার্কে কেন্দ্রীয় কোনো ডিভাইস বা সার্ভারের প্রয়োজন হয় না।}
\end{enumerate}

\chsub{}{বাস টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{ডেটা ট্রান্সমিশন অপেক্ষাকৃত ধীরগতিতে সম্পন্ন হয়।}
\end{enumerate}
\begin{enumerate}
\item \B{২. প্রধান সংযোগ লাইন বা বাস-এ ত্রুটি পরিলক্ষিত হলে সম্পূর্ণ নেটওয়ার্ক অচল হয়ে পড়ে।}
    \item \B{৩. নেটওয়ার্কে কম্পিউটারের সংখ্যা এবং দৈর্ঘ্য বৃদ্ধি পেলে ব্যাপক ট্রাফিক সৃষ্টি হয় এবং গতি হ্রাস পায়।}
    \item \B{৪. ডেটা সংঘর্ষ হওয়ার আশঙ্কা থাকে।}
\end{enumerate}

\chsub{}{রিং টপোলজি}
\B{রিং টপোলজিতে কম্পিউটারের নোডগুলো চক্রাকার পথে পরস্পর সাথে সংযুক্ত হয়ে নেটওয়ার্ক গঠন করে। এই বৃত্তাকার নেটওয়ার্কের ১ম ও সর্বশেষ কম্পিউটার পরস্পরের সাথে যুক্ত থাকে এবং এতে কেন্দ্রীয় কোনো ডিভাইস বা সার্ভার এর প্রয়োজন হয় না। একটি নোড সংকেত পাঠালে তা পরবর্তী নোডের কাছে যায়। সংকেতটি ঐ নোডের জন্য হলে সেটি সে নিজেই গ্রহণ করে অন্যথায় উক্ত নোড সংকেতটিকে পরবর্তী নোডের কাছে প্রেরণ করে। সঠিক নোডে না পৌঁছানো পর্যন্ত বৃত্তাকার নেটওয়ার্ক পথে সংকেতটি পরিভ্রমণ করে এবং এক পর্যায়ে কাঙ্ক্ষিত নোডে পৌঁছায়।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=1.0]
    \foreach \a in {0,60,120,180,240,300} {
        \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N-\a) at (\a:0.9) {};
    }
    \draw[thick] (N-0) -- (N-60) -- (N-120) -- (N-180) -- (N-240) -- (N-300) -- (N-0);
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{রিং টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{এই টপোলজিতে হোস্ট কম্পিউটার বা কেন্দ্রীয় সার্ভারের দরকার হয় না।}
    \item \B{সংকেত প্রবাহ একমুখী হওয়ায় ডেটা কলিশন বা সংঘর্ষ হয় না।}
    \item \B{প্রতিটি কম্পিউটার ডেটা ট্রান্সমিশনে সমান গুরুত্ব পায়।}
    \item \B{তারের পরিমাণ কম প্রয়োজন হয়, তাই বাস্তবায়ন খরচ কম।}
\end{enumerate}

\chsub{}{রিং টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{এই টপোলজিতে সংকেত আদান প্রদান অপেক্ষাকৃত ধীরগতিতে সম্পন্ন হয়।}
    \item \B{একমুখী বৃত্তাকার পথে সংযুক্তির কারণে একটি কম্পিউটার অন্য কম্পিউটারকে সরাসরি ডেটা প্রেরণ করতে সমর্থ হয় না এবং কোনো নোড অকার্যকর হলে সম্পূর্ণ নেটওয়ার্ক অকার্যকর হয়ে পড়ে।}
    \item \B{কোনো নতুন কম্পিউটার সংযোজন বা বিয়োজনে পুরো নেটওয়ার্কের কার্যক্রম ব্যাহত হয়।}
    \item \B{নেটওয়ার্কে কম্পিউটার সংখ্যা বাড়ালে ডেটা ট্রান্সমিশনের সময়ও বেড়ে যায়।}
    \item \B{এই টপোলজি নিয়ন্ত্রণের জন্য জটিল সফটওয়্যারের দরকার হয়।}
\end{enumerate}

\chsub{}{স্টার টপোলজি}
\B{স্টার টপোলজিতে নেটওয়ার্কভুক্ত সকল কম্পিউটার থেকে ক্যাবল বের হয়ে এসে একটি কেন্দ্রীয় স্থানে যুক্ত হয়। এই কেন্দ্রীয় স্থানে এসব ক্যাবল একটি ডিভাইসের সাথে যুক্ত হয় যা হাব বা সুইচ। কোনো কম্পিউটার ডেটা ট্রান্সফার করতে চাইলে তা প্রথমে হাব বা সুইচে পাঠিয়ে দেয়। এরপরে হাব বা সুইচ সেই সিগন্যালকে লক্ষ্যস্থানে পাঠিয়ে দেয়। সংকেত প্রবাহ দ্বিমুখী হয়।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=1.0]
    \node[draw, circle, fill=black, inner sep=0pt, minimum size=0.35cm] (Central) at (0,0) {};
    
    \foreach \a in {18,90,162,234,306} {
        \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N-\a) at (\a:0.95) {};
        \draw[thick] (Central) -- (N-\a);
    }
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{স্টার টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{অপেক্ষাকৃত দ্রুতগতিতে ডেটা আদান-প্রদান হয়।}
    \item \B{সংকেত সংঘর্ষ ঘটার আশঙ্কা কমায়।}
    \item \B{সম্পূর্ণ নেটওয়ার্ক সচল রেখেই যে কোনো সময়ে নেটওয়ার্কে নতুন নোড যুক্ত করা যায়।}
    \item \B{কোনো নোড বিচ্ছিন্ন বা অচল হলেও সম্পূর্ণ নেটওয়ার্ক সচল থাকে।}
    \item \B{সুইচ ব্যবহারের কারণে বাস বা রিং টপোলজির তুলনায় এর ডেটা নিরাপত্তা বেশি।}
    \item \B{কম্পিউটারের সংখ্যা বৃদ্ধি পেলেও ডেটা ট্রান্সমিশনের গতি স্বাভাবিক থাকে।}
\end{enumerate}

\chsub{}{স্টার টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{হাব বা সুইচ বা সার্ভার অচল হলে সম্পূর্ণ নেটওয়ার্ক অকেজো হয়ে পড়ে।}
\end{enumerate}
\begin{enumerate}
\item \B{২. প্রতিটি নোডের জন্য পৃথক পৃথক তারের প্রয়োজন হয়। তাই এতে অপেক্ষাকৃত বাস্তবায়ন ব্যয় বেশি।}
    \item \B{৩. নেটওয়ার্কভুক্ত কম্পিউটারগুলো পরস্পরের মধ্যে সরাসরি তথ্য বা ডেটা আদান-প্রদানে সক্ষম হয় না।}
\end{enumerate}

\chsub{}{ট্রি টপোলজি}
\B{স্টার টপোলজির সম্প্রসারিত রূপই হচ্ছে ট্রি টপোলজি। এ টপোলজিতে একাধিক হাব বা সুইচ ব্যবহার করে সমস্ত কম্পিউটারগুলো একটি বিশেষ স্থানে সংযুক্ত থাকে। এই কেন্দ্রীয় হোস্ট কম্পিউটারের সাথে স্তর বিন্যাস বা হায়ারার্কি অনুসারে বিভিন্ন স্তরের ডিভাইস নেটওয়ার্ক হাব বা সুইচের মাধ্যমে যুক্ত থাকে। এজন্য এটিকে হায়ারার্কিক্যাল টপোলজিও বলা হয়। ডেটা প্রবাহ দ্বিমুখী। যে কম্পিউটারের পরে আর কোনো কম্পিউটার যুক্ত থাকে না সেই কম্পিউটারকে পেরিফেরাল টার্মিনাল বা প্রান্তীয় কম্পিউটার বলে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.9, every node/.style={draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm}]
    \node (Root) at (0,1.2) {};
    
    \node (L2-1) at (-1,0.2) {};
    \node (L2-2) at (1,0.2) {};
    
    \node (L3-1) at (-1.6,-0.8) {};
    \node (L3-2) at (-0.4,-0.8) {};
    \node (L3-3) at (0.4,-0.8) {};
    \node (L3-4) at (1.6,-0.8) {};
    
    \draw[thick] (Root) -- (L2-1);
    \draw[thick] (Root) -- (L2-2);
    \draw[thick] (L2-1) -- (L3-1);
    \draw[thick] (L2-1) -- (L3-2);
    \draw[thick] (L2-2) -- (L3-3);
    \draw[thick] (L2-2) -- (L3-4);
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{ট্রি টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{যে কোনো সময়ে নতুন শাখা সৃষ্টি করে এর নেটওয়ার্ক সহজেই সম্প্রসারিত করা যায়।}
    \item \B{বড় ধরনের নেটওয়ার্ক গঠনে অন্যান্য টপোলজির তুলনায় এটি বেশি সুবিধা প্রদান করে।}
    \item \B{কোনো নোড বিচ্ছিন্ন বা নতুন নোড যুক্ত করা হলে নেটওয়ার্ক কার্যক্রম ব্যাহত হয় না।}
    \item \B{ডেটা নিরাপত্তা সবচেয়ে বেশি।}
    \item \B{নেটওয়ার্কের কোনো শাখা নষ্ট হলে, সম্পূর্ণ নেটওয়ার্ক অচল হয়ে পড়ে না।}
\end{enumerate}

\chsub{}{ট্রি টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{প্রধান কম্পিউটার নষ্ট হলে সমগ্র নেটওয়ার্ক অচল হয়ে পড়ে।}
    \item \B{অন্যান্য টপোলজির তুলনায় জটিল প্রকৃতির।}
    \item \B{বাস্তবায়ন ব্যয় অপেক্ষাকৃত বেশি।}
    \item \B{অন্তর্বর্তী কম্পিউটারগুলো অচল হলে নেটওয়ার্কের অংশবিশেষ অকেজো হয়ে পড়ে।}
\end{enumerate}

\chsub{}{মেশ টপোলজি}
\B{মেশ টপোলজিতে প্রতিটি কম্পিউটার প্রতিটি কম্পিউটারের সাথে একাধিক পথে যুক্ত হতে পারে তাই প্রতিটি ওয়ার্ক স্টেশন সরাসরি যেকোনো ওয়ার্ক স্টেশনের সাথে ডেটা আদান-প্রদান করতে পারে। এখানে কম্পিউটার গুলো শুধু যে অন্য কম্পিউটারগুলো থেকে তথ্য নেয় তা নয় বরং সেটা সে নেটওয়ার্কের অন্য কম্পিউটার এর সাথে বিতরণও করতে পারে। একে পয়েন্ট টু পয়েন্ট অথবা পিয়ার টু পিয়ার লিংক বলা হয় এবং অন্তঃসংযোগ টপোলজি নামেও পরিচিত। $n$ সংখ্যক নোডের জন্য প্রতি নোডে $(n-1)$ টি সংযোগ প্রয়োজন হয়। নেটওয়ার্ক এর মোট তারের সংখ্যা $\frac{n(n-1)}{2}$}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=1.0]
    \foreach \a in {90,162,234,306,18} {
        \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N-\a) at (\a:1.0) {};
    }
    \draw[thick] (N-90) -- (N-162);
    \draw[thick] (N-90) -- (N-234);
    \draw[thick] (N-90) -- (N-306);
    \draw[thick] (N-90) -- (N-18);
    
    \draw[thick] (N-162) -- (N-234);
    \draw[thick] (N-162) -- (N-306);
    \draw[thick] (N-162) -- (N-18);
    
    \draw[thick] (N-234) -- (N-306);
    \draw[thick] (N-234) -- (N-18);
    
    \draw[thick] (N-306) -- (N-18);
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{মেশ টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{অন্যান্য সব ধরনের টপোলজির তুলনায় এতে ডেটা ট্রান্সমিশন দ্রুতগতিতে সম্পন্ন হয়।}
    \item \B{নেটওয়ার্কে কম্পিউটারের সংখ্যা বৃদ্ধি পেলেও ডেটা ট্রান্সমিশনের গতি কমে না।}
    \item \B{নেটওয়ার্কস্থ যেকোনো কম্পিউটার নষ্ট বা বিচ্ছিন্ন হলেও নেটওয়ার্ক সচল থাকে।}
    \item \B{কোনো সংযোগ তার নষ্ট বা বিচ্ছিন্ন হলে বিকল্প সকল কম্পিউটারে ডেটা আদান-প্রদান অব্যাহত থাকে।}
    \item \B{নেটওয়ার্কে কেন্দ্রীয় কোনো ডিভাইস বা সার্ভারের প্রয়োজন হয় না।}
\end{enumerate}

\chsub{}{মেশ টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{বেশি পরিমাণ তার ও অতিরিক্ত লিংক প্রয়োজন হওয়ায় এটি ব্যয়বহুল।}
    \item \B{নেটওয়ার্ক ইনস্টলেশন ও কনফিগারেশন অত্যন্ত জটিল।}
\end{enumerate}
\begin{enumerate}
\item \B{৩. নেটওয়ার্কে কম্পিউটার সংখ্যা বৃদ্ধির সাথে সাথে ব্যয়ের পরিমাণও বেড়ে যায়।}
\end{enumerate}

\chsub{}{হাইব্রিড টপোলজি}
\B{বিভিন্ন টপোলজির একাধিক টপোলজি নিয়ে গড়ে ওঠে হাইব্রিড টপোলজি। এতে একসাথে কোন অংশে বাস টপোলজি কিংবা রিং টপোলজি ব্যবহৃত হতে পারে। হাইব্রিড টপোলজির উপর ভিত্তি করে ইন্টারনেট গঠন করা হয়।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.9]
    \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N1) at (0,1) {};
    \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N2) at (-1,0) {};
    \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N3) at (1,0) {};
    \node[draw, circle, fill=gray!30, thick, inner sep=0pt, minimum size=0.4cm] (N4) at (0,-1) {};
    
    \draw[thick] (N1) -- (N2);
    \draw[thick] (N1) -- (N3);
    \draw[thick] (N2) -- (N4);
    \draw[thick] (N3) -- (N4);
    \draw[thick] (N2) -- (N3);
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{হাইব্রিড টপোলজির সুবিধা}
\begin{enumerate}
    \item \B{এতে হাব বা সুইচ যুক্ত করে প্রয়োজনীয় নেটওয়ার্ক সম্প্রসারণ করা যায়।}
    \item \B{এই নেটওয়ার্কের ট্রাবল শুটিং সহজতর।}
    \item \B{একটি টপোলজি নষ্ট হলে অন্য কোনো টপোলজির উপর প্রভাব পড়ে না।}
    \item \B{যেহেতু এটি মিশ্র টপোলজি তাই এতে ব্যবহৃত টপোলজিগুলোর সুবিধাগুলোও এতে অন্তর্নিহিত থাকে।}
\end{enumerate}

\chsub{}{হাইব্রিড টপোলজির অসুবিধা}
\begin{enumerate}
    \item \B{টপোলজির সংখ্যা বেশির কারণে এর রক্ষণাবেক্ষণ খরচ বেশি এবং রক্ষণাবেক্ষণ প্রক্রিয়া জটিল।}
    \item \B{এই টপোলজির ইনস্টলেশন ও কনফিগারেশন বেশ জটিল প্রকৃতির।}
    \item \B{মিশ্র টপোলজি হিসেবে এতে ব্যবহৃত টপোলজিগুলোর অসুবিধাগুলোও এতে অন্তর্নিহিত থাকে।}
\end{enumerate}

\chsec{$\square$ ডেটা কমিউনিকেশন মাধ্যম}
\B{যার মধ্য দিয়ে ডেটা এক স্থান হতে অন্য স্থানে যায় তাকে কমিউনিকেশন চ্যানেল/ মাধ্যম/ মিডিয়াম বলে। যেমন: বিভিন্ন ধরনের তার বা ক্যাবল, পাবলিক টেলিফোন লাইন, তারবিহীন মাধ্যম এর জন্য রেডিওওয়েভ, মাইক্রোওয়েভ ইত্যাদি।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[
    node distance=1.2cm and 0.4cm,
    block/.style={draw, rectangle, align=center, font=\tiny, inner sep=2pt, minimum height=0.6cm, thick},
    line/.style={draw, -{Stealth[scale=0.8]}, thick}
]
    \node[block, minimum width=2.5cm] (medium) at (0,0) {\B{মাধ্যম (Medium)}};
    
    \node[block, minimum width=3.5cm] (guided) at (-2.8,-1.5) {\B{Guided Media:} \\ তার (\B{Wire/ Cable})};
    \node[block, minimum width=3.5cm] (unguided) at (2.8,-1.5) {\B{Unguided Media:} \\ তারবিহীন (\B{Wireless}) \\ ফ্রিকোয়েন্সি/ তরঙ্গের উপর};
    
    \node[right, font=\tiny, align=left] (glist) at (-4.5,-3.0) {
        $\bullet$ টেলিফোন ক্যাবল \\
        $\bullet$ কো - এক্সিয়াল ক্যাবল \\
        $\bullet$ টুইস্টেড পেয়ার ক্যাবল \\
        $\bullet$ ফাইবার অপটিক্যাল ক্যাবল
    };

    \node[block, minimum width=2.3cm] (radio) at (0.5,-3.8) {রেডিও ওয়েভ \\ (\B{Radio Wave}) \\ \LAT{3 KHz - 300 GHz}};
    \node[block, minimum width=2.3cm] (micro) at (3.0,-3.8) {মাইক্রো ওয়েভ \\ (\B{Micro Wave}) \\ \LAT{300 MHz - 300 GHz}};
    \node[block, minimum width=2.3cm] (infra) at (5.5,-3.8) {ইনফ্রারেড \\ (\B{Infrared}) \\ \LAT{300 GHz - 400 THz}};

    \node[block, minimum width=2.3cm] (wifi) at (0.5,-5.5) {ওয়াই-ফাই \\ \LAT{WLAN} তৈরিতে ব্যবহৃত হয় \\ \LAT{2.4 - 5 GHz} পর্যন্ত};
    \node[block, minimum width=2.3cm] (wimax) at (3.0,-5.5) {ওয়াইম্যাক্স \\ \LAT{WMAN} তৈরিতে ব্যবহৃত হয় \\ \LAT{2 - 66 GHz} পর্যন্ত};
    \node[block, minimum width=2.3cm] (bluetooth) at (5.5,-5.5) {ব্লু-টুথ \\ \LAT{WPAN} তৈরিতে ব্যবহৃত হয় \\ \LAT{2.4 - 2.45 GHz} পর্যন্ত};

    \draw[thick] (medium.south) -- (0,-0.8);
    \draw[thick] (-2.8,-0.8) -- (2.8,-0.8);
    \path[line] (-2.8,-0.8) -- (guided.north);
    \path[line] (2.8,-0.8) -- (unguided.north);
    
    \draw[thick] (guided.south) -- (-2.8,-2.4) -- (-4.7,-2.4);
    \path[line] (-4.7,-2.4) -- (-4.7,-2.7);

    \draw[thick] (unguided.south) -- (2.8,-2.8);
    \draw[thick] (0.5,-2.8) -- (5.5,-2.8);
    \path[line] (0.5,-2.8) -- (radio.north);
    \path[line] (3.0,-2.8) -- (micro.north);
    \path[line] (5.5,-2.8) -- (infra.north);
    
    \path[line] (radio.south) -- (wifi.north);
    \path[line] (micro.south) -- (wimax.north);
    \path[line] (infra.south) -- (bluetooth.north);

\end{tikzpicture}
\end{center}
\chsub{}{তার মাধ্যম (Wired Media)}
\B{এ পদ্ধতিতে তথ্য আদান-প্রদানের ক্ষেত্রে ধাতব তার ব্যবহৃত হয়। নির্দিষ্ট কোনো পথে বৈদ্যুতিক সংকেত পাঠানোর জন্য মাধ্যম হিসেবে কপার বা অ্যালুমিনিয়ামের তার বা ক্যাবল ব্যবহার করে ডেটা কমিউনিকেশনের ব্যবস্থা করা হয়। এটি ক্যাবল গাইডেড মিডিয়া।}

\chsub{}{টুইস্টেড পেয়ার ক্যাবল (Twisted Pair Cable)}
\B{দুটি পরিবাহী তারকে পরস্পর সুষমভাবে পেঁচিয়ে টুইস্টেড পেয়ার ক্যাবল তৈরি করা হয়। টুইস্টেড পেয়ার ক্যাবল ২ ধরনের হয়ে থাকে। যথা:}
\begin{enumerate}
    \item \B{১. আনশিল্ডেড টুইস্টেড পেয়ার ক্যাবল (UTP: Unshielded Twisted Pair)}
    \item \B{২. শিল্ডেড টুইস্টেড পেয়ার ক্যাবল (STP: Shielded Twisted Pair)}
\end{enumerate}

\B{সাধারণ কপার নির্মিত এ সব ক্যাবলে মোট চার জোড়া তার প্রতিটি পৃথক অপরিবাহী পদার্থের আবরণে (ইনসুলেটর) আবৃত থাকে। প্রতি জোড়া তারে একটি কমন রঙের (সাদা রঙের) আরেকটি ভিন্ন রঙের (যেমন: নীল, সবুজ, কমলা ও বাদামি) তারের সাথে পেঁচানো থাকে। প্রতি জোড়া তার পৃথক অপরিবাহী আবরণে আবৃত করা থাকে। টুইস্টেড পেয়ার ক্যাবল ব্যবহার করে 100 মিটারের বেশি দূরত্বে কোনো ডেটা প্রেরণ করা যায় না। ক্যাটাগরির ভিত্তিতে এর ব্যান্ডউইথ 10 Mbps থেকে 1 Gbps পর্যন্ত হতে পারে, তবে দূরত্ব বাড়তে থাকলে ডেটা ট্রান্সফার রেট কমতে থাকে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.85]
    \draw[thick, fill=gray!20] (0,0.5) to[out=0,in=180] (3,0.6) -- (3,-0.6) to[out=180,in=0] (0,-0.5) -- cycle;
    \node at (1.5,0.9) [font=\tiny\bfseries] {আউটার জ্যাকেট};
    
    \draw[thick, fill=gray!50] (3,0.4) -- (4.5,0.4) -- (4.5,-0.4) -- (3,-0.4) -- cycle;
    \node at (3.8,-0.7) [font=\tiny\bfseries] {ফয়েল সিল্ড};
    
    \node at (4.8,0.7) [font=\tiny\bfseries] {পেয়ার সিল্ড};
    \node at (5.5,-0.7) [font=\tiny\bfseries] {ড্রেইন ওয়্যার};
    
    \draw[thick, blue] (4.5,0.2) to[out=20,in=200] (5.5,0.3) to[out=20,in=200] (6.5,0.2);
    \draw[thick, white!60!gray] (4.5,0.3) to[out=-20,in=160] (5.5,0.1) to[out=-20,in=160] (6.5,0.3);
    
    \draw[thick, orange] (4.5,0.0) to[out=10,in=190] (5.7,0.05) to[out=10,in=190] (6.8,0.0);
    \draw[thick, white!60!gray] (4.5,0.1) to[out=-10,in=170] (5.7,-0.05) to[out=-10,in=170] (6.8,0.1);
    
    \draw[thick, green!60!black] (4.5,-0.2) to[out=0,in=180] (5.6,-0.1) to[out=0,in=180] (6.6,-0.2);
    \draw[thick, white!60!gray] (4.5,-0.1) to[out=-30,in=150] (5.6,-0.3) to[out=-30,in=150] (6.6,-0.1);
    
    \draw[ultra thick, yellow!60!black] (6.5,0.2) -- (7,0.2);
    \draw[ultra thick, yellow!60!black] (6.8,0.0) -- (7.3,0.0);
    \draw[ultra thick, yellow!60!black] (6.6,-0.2) -- (7.1,-0.2);
    
    \node at (6.5,0.8) [font=\tiny\bfseries] {টুইস্টেড পেয়ার};
    \node at (7.4,0.3) [font=\tiny\bfseries] {কন্ডাক্টর};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{টুইস্টেড পেয়ার ক্যাবলের সুবিধাসমূহ:}
\begin{enumerate}
    \item \B{কম দূরত্বে যোগাযোগের ক্যাবল হিসেবে টুইস্টেড পেয়ার ক্যাবল ব্যাপকভাবে ব্যবহার হয়।}
    \item \B{সহজে মেরামত করা যায়।}
    \item \B{এটি অন্যান্য ক্যাবলের চেয়ে অনেক সস্তা।}
    \item \B{সহজে স্থাপন করা যায়।}
    \item \B{এটি পুরানো ডেটা প্রেরণ পদ্ধতি।}
    \item \B{অ্যানালগ এবং ডিজিটাল উভয় ধরনের ডেটা প্রেরণের জন্য টুইস্টেড পেয়ার ক্যাবল ব্যবহার হয়।}
\end{enumerate}

\chsub{}{টুইস্টেড পেয়ার ক্যাবলের অসুবিধাসমূহ:}
\begin{enumerate}
    \item \B{বেশি দূরত্বে ডেটা পাঠানোর জন্য ২ কি.মি. পর রিপিটার ব্যবহার করতে হয়।}
    \item \B{ট্রান্সমিশন শব্দে আক্রান্তকরণ বেশি।}
    \item \B{পাখা পাতা হওয়ার কারণে সহজেই জটলা যাওয়ার সম্ভাবনা থাকে।}
    \item \B{সহজেই নয়েজ সিগন্যাল দ্বারা আক্রান্ত হয়।}
    \item \B{এক ক্যাবল ব্যবহার করা হয় ১০০ মিটার দূরত্বের মধ্যে তথ্য প্রেরণের জন্য।}
\end{enumerate}

\chsub{}{টুইস্টেড পেয়ার ক্যাবলের ব্যবহার:}
\begin{enumerate}
    \item \B{টেলিফোন লাইনে এই ক্যাবল ব্যবহার হয়।}
    \item \B{ডিজিটাল সিগন্যালিং ও LAN এর ক্ষেত্রে এ ধরনের ক্যাবল ব্যবহার হয়।}
\end{enumerate}

\chsub{}{কো-অক্সিয়াল ক্যাবল (Co-axial Cable)}
\B{কো-অক্সিয়াল ক্যাবল তামা বা কপার নির্মিত মূলত তিনটি স্তর বিশিষ্ট তারের ক্যাবল, কেন্দ্রস্থলে একটি শক্ত তামার তারের কন্ডাক্টর, সেটিকে বৃত্তাকারে ঘিরে প্লাস্টিকের অপরিবাহী স্তর এবং এই স্তরকে ঘিরে তামার তারের একটি জাল বা শিল্ড (Braided Shield)। অনেক সময় শিল্ড এবং প্লাস্টিক অপরিবাহী স্তরের মাঝে একটি মেটালিক ফয়েলও থাকে। সবশেষে রবারের অপরিবাহী পুরু স্তর এই ক্যাবলটিকে আবৃত করে রাখে। তামার তারের জালি এবং মেটালিক ফয়েলটি একসাথে আউটার কন্ডাক্টর (Outer conductor) হিসেবে বাইরের সকল প্রকার বৈদ্যুতিক প্রভাব থেকে মুক্ত রাখে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.85]
    \draw[thick, fill=gray!20] (0,0.5) to[out=0,in=180] (2.5,0.5) -- (2.5,-0.5) to[out=180,in=0] (0,-0.5) -- cycle;
    \node at (1.25,0.8) [font=\tiny\bfseries] {বাইরের জ্যাকেট};
    
    \draw[thick, fill=gray!60] (2.5,0.4) -- (4.0,0.4) -- (4.0,-0.4) -- (2.5,-0.4) -- cycle;
    \foreach \x in {2.6,2.9,3.2,3.5,3.8} {
        \draw[very thin] (\x,0.4) -- (\x+0.2,-0.4);
        \draw[very thin] (\x+0.2,0.4) -- (\x,-0.4);
    }
    \node at (3.25,-0.7) [font=\tiny\bfseries] {জালির আবরণ};
    
    \draw[thick, fill=gray!40] (4.0,0.3) -- (5.0,0.3) -- (5.0,-0.3) -- (4.0,-0.3) -- cycle;
    \node at (4.5,0.6) [font=\tiny\bfseries] {ফয়েল সিল্ড};
    
    \draw[thick, fill=white] (5.0,0.2) -- (6.5,0.2) -- (6.5,-0.2) -- (5.0,-0.2) -- cycle;
    \node at (5.75,-0.5) [font=\tiny\bfseries] {প্লাস্টিক ইনসুলেটর};
    
    \draw[thick, fill=orange!80!black] (6.5,0.07) -- (7.8,0.07) -- (7.8,-0.07) -- (6.5,-0.07) -- cycle;
    \node at (7.3,0.3) [font=\tiny\bfseries] {কন্ডাক্টর};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\B{নেটওয়ার্কে ব্যবহৃত কো-অক্সিয়াল ক্যাবলকে প্রধানত দু' প্রকারে ভাগ করা হয়। যথা:}

\chsub{}{১. থিননেট (Thinnet):}
\B{যেসব কো-অক্সিয়াল ক্যাবল ব্যবহার করে যে নেটওয়ার্ক গঠিত তাকে বলা হয় থিননেট। থিন কো-অক্সিয়াল ক্যাবলের ব্যাস ০.২৫ ইঞ্চি এবং ক্যাবলের সর্বোচ্চ দৈর্ঘ্য ১৮৫ মিটার পর্যন্ত হতে পারে। এই ধরনের নেটওয়ার্ককে ১০ বেজ ২ (10Base2) নেটওয়ার্কও বলা হয়। এখানে ১০ বলতে ডাটা ট্রান্সমিশন রেট (10 Mbps) এবং ২ বলা ক্যাবলের দৈর্ঘ্য (২০০ মিটার) বুঝায়। এতে BNC কানেক্টর ব্যবহৃত হয়।}

\chsub{}{২. থিকনেট (Thicknet):}
\B{যেসব কো-অক্সিয়াল ক্যাবল তুলনামূলকভাবে মোটা ব্যাস ০.৫ ইঞ্চি এবং যেগুলো কয়েকশ' মিটার দীর্ঘ হতে পারে, সেই ক্যাবল ব্যবহার করে যে নেটওয়ার্ক গঠিত তাকে থিকনেট বলা হয়। এই ধরনের নেটওয়ার্ককে ১০বেজ৫ (10Base5) নেটওয়ার্কও বলা হয়। ক্যাবলের সাথে ডিভাইসসমূহ সংযুক্ত করার জন্য ট্রান্সসিভার এবং অ্যাটাচমেন্ট ট্যাপ ও ড্রপ ক্যাবল প্রয়োজন হয়।}

\chsub{}{কো-অক্সিয়াল ক্যাবল:}
\B{কো-অক্সিয়াল ক্যাবল ব্যবহার করে ডেটা নির্দিষ্ট ছাড়াও সাধারণত ১ (এক) কিলোমিটার পর্যন্ত দূরত্বে ডেটা প্রেরণ করা যায়। এর ডাটা ট্রান্সমিশন রেট ২০০ Mbps পর্যন্ত হয় এবং ডেটা ট্রান্সমিশনের হার অপেক্ষাকৃত কম হয়।}

\chsub{}{সুবিধাসমূহ:}
\begin{enumerate}
    \item \B{সহজে ক্যাবল স্থাপন করা যায়।}
    \item \B{অধিক নিরাপদ।}
    \item \B{দামে কম।}
    \item \B{অধিক দূরত্বে ডেটা প্রেরণ।}
    \item \B{অধিক গতিতে ডেটা প্রেরণ।}
\end{enumerate}

\chsub{}{কো-অক্সিয়াল ক্যাবলের সুবিধা:}
\begin{enumerate}
    \item \B{ফাইবার অপটিক ক্যাবলের তুলনায় দামে সস্তা।}
    \item \B{অ্যানালগ এবং ডিজিটাল উভয় ডেটা ট্রান্সমিশনে এ ক্যাবল ব্যবহার হয়।}
    \item \B{টুইস্টেড পেয়ার ক্যাবলের চেয়ে অধিক দূরত্বে ডেটা পাঠানো যায়।}
\end{enumerate}

\chsub{}{কো-অক্সিয়াল ক্যাবলের অসুবিধা:}
\begin{enumerate}
\item \B{১. ট্রান্সমিশন হার অপেক্ষাকৃত কম হয়।}
    \item \B{২. কো-অক্সিয়াল ক্যাবলের মাধ্যমে নেটওয়ার্ক ডিভাইসের মধ্যে সংযোগ স্থাপন করা কিছুটা কঠিন।}
    \item \B{৩. তারের দৈর্ঘ্যের উপর ডেটা ট্রান্সমিশন হার নির্ভর করে।}
    \item \B{৪. রিপিটার ছাড়া ১ কিলোমিটারের বেশি দূরত্বে ডেটা পাঠানো যায় না।}
\end{enumerate}

\chsub{}{কো-অক্সিয়াল ক্যাবলের ব্যবহার:}
\begin{enumerate}
    \item \B{কো-অক্সিয়াল ক্যাবল প্রধানত ল্যান এরিয়া নেটওয়ার্কের জন্য ব্যবহৃত হয়।}
    \item \B{ক্যাবল টিভি সিস্টেম এর ব্যবহার দেখা যায়।}
\end{enumerate}

\chsub{}{ফাইবার অপটিক ক্যাবল (Fiber Optic Cable)}
\B{ফাইবার অপটিক ক্যাবল তার মাধ্যমের মধ্যে সবচেয়ে শক্তিশালী মাধ্যম। ফাইবার অপটিক ক্যাবল কেন্দ্রে কাঁচের একটি তার দিয়ে তৈরি হয়। সিলিকা, কাঁচ অথবা প্লাস্টিক দিয়ে। কাঁচের তুলনায় প্লাস্টিকের ব্যবহার অনেক বড় সুবিধা হলো যে, এটি ইমপ্রোভেল নয়। এই কারণে ডেটা সিগন্যাল পরিবর্তনশীল অবস্থায় থাকে না। কাঁচের তুলনায় প্লাস্টিকের মধ্য দিয়ে ডেটা প্রক্ষেপিত হয় বলে এর গতি অনেক বেশি হয়।}

\chsub{}{গঠন:}
\B{ফাইবার তৈরির জন্য সোজা বোরো সিলিকেট, সোজা লাইম সিলিকেট, সোজা অ্যালুমিনিয়াম সিলিকেট ইত্যাদি মাটির কম্পাউন্ড কাঁচগুলো বেশি ব্যবহৃত হয়। এসব পদার্থের গুণগত বৈশিষ্ট্যগুলোর মধ্যে বিশেষজ্ঞ হলো: অত্যন্ত নমনীয়তা, স্বচ্ছতা, নিরীক্ষণ, সঠিক প্রতিফলন ক্ষমতা। সাধারণত ফাইবারের জন্য কাঁচের চেয়ে প্লাস্টিকের ব্যবহার বেশি হয়ে থাকে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.9, x={(0.866cm,0.5cm)}, y={(-0.866cm,0.5cm)}, z={(0cm,1cm)}]
    \draw[thick, fill=gray!30] (0,0,0) circle [radius=1.2];
    \draw[thick, fill=gray!40] (0,0,0) -- (0,0,-2) arc [start angle=-180, end angle=0, radius=1.2] -- (0,0,0);
    \draw[thick] (0,0,-2) circle [radius=1.2];
    
    \draw[thick, fill=gray!60] (0,0,0) circle [radius=0.7];
    \draw[thick, fill=gray!70] (0,0,0) -- (0,0,-3.5) arc [start angle=-180, end angle=0, radius=0.7] -- (0,0,0);
    \draw[thick] (0,0,-3.5) circle [radius=0.7];
    
    \draw[thick, fill=black!80] (0,0,0) circle [radius=0.25];
    \draw[thick, fill=black!90] (0,0,0) -- (0,0,-5) arc [start angle=-180, end angle=0, radius=0.25] -- (0,0,0);
    \draw[thick] (0,0,-5) circle [radius=0.25];
    
    \draw[latex-, thick] (1.0,0,-1) -- (3,0,-1) node[right, font=\tiny\bfseries] {Jacket (plastic)};
    \draw[latex-, thick] (0.6,0,-2.5) -- (2.5,0,-2.5) node[right, font=\tiny\bfseries] {Cladding (glass)};
    \draw[latex-, thick] (0.2,0,-4.5) -- (2.0,0,-4.5) node[right, font=\tiny\bfseries] {Core (glass)};
    
    \node at (0,0,-6.2) [font=\tiny\bfseries] {Side view of Single fiber};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\B{ফাইবার অপটিক ক্যাবল তিনটি প্রধান অংশে গঠিত:}
\begin{enumerate}
    \item \B{(i) কোর: ভেতরের ডাই-ইলেকট্রিক কোর যার ব্যাস ৮ থেকে ১০০ মাইক্রোন হয়ে থাকে।}
    \item \B{(ii) ক্ল্যাডিং: কোরের চারপাশে ফাইবারকে আবৃত করে থাকে ক্ল্যাডিং (cladding) বা কেভলার (kevlar) যা এমন এক পদার্থ দিয়ে তৈরি যা আলোকে প্রতিফলন করতে পারে। এর ফলে আলোকে সংহত করে ফাইবার অপটিক ক্যাবলের মধ্যে বাঁকা পথে যেতে পারে।}
    \item \B{(iii) জ্যাকেট: আবরণ হিসেবে কাজ করে।}
\end{enumerate}

\chsub{}{ফাইবার অপটিকের বৈশিষ্ট্য:}
\begin{enumerate}
    \item \B{১. ইলেকট্রিসিটির মতো আলোকে সংহত করে বাইরে ছড়িয়ে পড়ে না বলে এতে ইলেকট্রোম্যাগনেটিক নয়েজ বলতেই চলে।}
    \item \B{২. অ্যাটেন্যুয়েশন না থাকায় দূর গামী ডেটা সিগন্যালকে সহজেই খুবই দক্ষতায় অতিক্ষেপে করতে পারে।}
\end{enumerate}

\chsub{}{ফাইবারের সুবিধাসমূহ:}
\begin{enumerate}
    \item \B{১. উচ্চ ব্যান্ডউইথ সম্পন্ন।}
    \item \B{২. বিদ্যুৎ চৌম্বক প্রভাব (EMI) হতে মুক্ত।}
    \item \B{৩. নির্ভুল ডেটা আদান-প্রদান করে।}
    \item \B{৪. পরিবেশের তাপ-চাপ ইত্যাদি দ্বারা প্রভাবিত হয় না।}
\end{enumerate}
\begin{enumerate}
\item \B{৫. আকারে ছোট, ওজন অত্যন্ত কম এবং সহজে পরিবহনযোগ্য।}
    \item \B{৬. শক্তির ক্ষয় কম।}
    \item \B{৭. ডেটা সংরক্ষণের নিরাপত্তা ও গোপনীয়তা বেশি।}
    \item \B{৮. রিপিটারসমূহ অনেক দূরে দূরে স্থাপন করতে হয় না।}
\end{enumerate}

\chsub{}{ফাইবারের অসুবিধাসমূহ:}
\begin{enumerate}
    \item \B{১. ফাইবার অপটিক ক্যাবল ইনস্টল করা বেশ কঠিন।}
    \item \B{২. একে প্রয়োজনমতো বাঁকানো যায় না বলে ইনস্টলেশন বেশ কঠিন হয়ে পড়ে।}
    \item \B{৩. ফাইবার অপটিক ক্যাবলকে সহজে স্লাইস বা টুকরো করা যায় না। এর স্লাইসিং-এর জন্য দরকার পড়ে ইলেকট্রিক ফিউশন কিংবা কেমিক্যাল এপোক্সি।}
    \item \B{৪. অন্যান্য ক্যাবলের চেয়ে দাম খুবই বেশি।}
    \item \B{৫. অপটিক্যাল ফাইবার স্থাপন ও রক্ষণাবেক্ষণ করার জন্য দক্ষ ও কারিগরি জ্ঞানসম্পন্ন জনবল প্রয়োজন।}
\end{enumerate}

\B{ফাইবার অপটিক ক্যাবলের প্রকারভেদ: ফাইবারের গাঠনিক উপাদানের প্রতিসরাংকের ওপর ভিত্তি করে ফাইবারকে দুভাগে ভাগ করা হয়।}

\B{স্টেপ ইনডেক্স ফাইবার (Step-index fiber): স্টেপ ইনডেক্স ফাইবারের কোরের প্রতিসরাংক সর্বত্র সমান থাকে।}

\B{গ্রেডেড-ইনডেক্স ফাইবার (Graded-index fiber): গ্রেডেড ইনডেক্স ফাইবারের কোরের প্রতিসরাংক কেন্দ্রে সবচেয়ে বেশি এবং এর ব্যাসার্ধ বরাবর কমতে থাকে। কোরের প্রতিসরাংকের ভিন্নতার কারণে এ দু ধরনের ফাইবারের আলোক রশির গতিপথও ভিন্ন হয়।}

\B{কোরের ব্যাস অনুযায়ী ফাইবার অপটিককে আবার দুভাগে ভাগ করা যায়। যথা-}

\B{সিঙ্গেলমোড ফাইবার (Singlemode fiber): কোরের সাইজ ৮/১২৫ মাইক্রন। সিঙ্গেল-মোড ফাইবার অপটিক ক্যাবলে একসাথে কেবল একটি আলোক সংকেত প্রেরণের পথ থাকে এবং সাধারণত লেজার সিগনালিং এর জন্য ব্যবহৃত হয়। সিঙ্গেল মোড ফাইবার অপটিক ক্যাবল ব্যবহার করা হয় দীর্ঘ দূরত্ব অতিক্রম করার জন্য।}

\B{মাল্টিমোড ফাইবার (Multimode fiber): কোরের সাইজ ৬২.৫/১২৫ মাইক্রন। এটি সবচেয়ে বেশি ব্যবহৃত এবং নেটওয়ার্ক অ্যাপ্লিকেশনের উপযোগী। মাল্টিমোড ফাইবারে একই সাথে একাধিক আলোক সংকেত প্রেরণের পথ থাকে এবং এসব পথ দিয়ে সবকটি সিগনাল একই সাথে গন্তব্যে পৌঁছতে পারে।}

\begin{center}
\B{একনজরে বিভিন্ন প্রকার তার (গাইডেড) মাধ্যম} \\[0.2cm]
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|c|c|p{3.5cm}|p{3.5cm}|}
\hline
\textbf{মিডিয়া টাইপ} & \pbox{2cm}{\centering\arraybackslash \textbf{সর্বোচ্চ} \\ \textbf{সেগমেন্ট} \\ \textbf{দৈর্ঘ্য/} \\ \textbf{কভারেজ}} & \textbf{ব্যান্ড উইডথ} & \centering\arraybackslash \textbf{সুবিধা} & \centering\arraybackslash \textbf{অসুবিধা} \tabularnewline \hline
\B{থিকনেট কো-অক্সিয়াল ক্যাবল} & \B{৫০০ মিটার} & \B{10 Mbps} & \B{অন্যান্য কপার ক্যাবলের চেয়ে বেশি ইএমআই প্রতিরোধ ক্ষমতা} & \B{ব্যয়বহুল, সহজে ইনস্টল করা যায় না।} \tabularnewline \hline
\B{থিননেট কো-অক্সিয়াল ক্যাবল} & \B{১৮৫ মিটার} & \B{10 Mbps} & \B{থিকনেট ও ফাইবার অপটিকের চেয়ে কমদামী, সহজে স্থাপনযোগ্য} & \B{ব্যান্ডউইডথ সীমিত, সহজে ব্যবহার করা যায় না।} \tabularnewline \hline
\B{এসটিপি} & \B{১০০ মিটার} & \B{10 Mbps} & \B{ক্রসটক কম হয়, থিননেট ও ইউটিপির চেয়ে বেশি ইএমআই প্রতিরোধি} & \B{ব্যয়বহুল, স্থাপন করা কঠিন} \tabularnewline \hline
\B{ইউটিপি} & \B{১০০ মিটার} & \B{10 Mbps} & \B{সহজে ইনস্টলযোগ্য ও কমদামী} & \B{সীমিত ব্যান্ডউইডথ, খারাপ সিগনাল, ওয়েভ সিগনালের জন্য} \tabularnewline \hline
\B{সিঙ্গেল মোড ফাইবার} & \B{৩ কি.মি.} & \B{100 Mbps - 100 Gbps} & \B{উচ্চগতি, বেশি নিরাপত্তা, ইএমআই প্রতিরোধি} & \B{ব্যয়বহুল, স্থাপন করা কঠিন, কেবল একটি সিগনাল একসাথে ট্রান্সমিট করা যায়।} \tabularnewline \hline
\B{মাল্টিমোড ফাইবার} & \B{২ কি.মি.} & \B{100 Mbps - 9.92 Gbps} & \B{উচ্চগতি, একসাথে একাধিক সিগনাল ট্রান্সমিট করতে পারে, নিরাপদ ও ইএমআই প্রতিরোধি} & \B{ব্যয়বহুল, স্থাপন করতে অসুবিধাজনক এবং ক্রোম্যাটিক ডিসপারশনের শিকার} \tabularnewline \hline
\end{tabular}
\end{adjustbox}
\end{center}
\chsecfull{৩য় অধ্যায় \\ সংখ্যাপদ্ধতি}

\chsub{}{সংখ্যা পদ্ধতি}
\B{বিভিন্ন সাংকেতিক চিহ্ন ব্যবহার করে কোনো সংখ্যা লেখা ও প্রকাশ করার পদ্ধতিকে বলা হয় সংখ্যা পদ্ধতি। সংখ্যাপদ্ধতিকে অবস্থানের উপর নির্ভর করে ২ ভাগে বিভক্ত করা হয়েছে। যথা:}
\begin{enumerate}
    \item \B{i. নন পজিশনাল (অস্থানিক) সংখ্যাপদ্ধতি।}
    \item \B{ii. পজিশনাল (স্থানিক) সংখ্যাপদ্ধতি।}
\end{enumerate}

\chsub{}{নন পজিশনাল সংখ্যা পদ্ধতি}
\B{যে পদ্ধতিতে সংখ্যার মান ব্যবহৃত চিহ্ন বা অংকসমূহের পজিশন বা অবস্থানের উপর নির্ভর করে না তাকে নন পজিশনাল সংখ্যা পদ্ধতি বলে।}
\begin{itemize}
    \item \B{নন পজিশনাল সংখ্যা পদ্ধতির উদাহরণ হলো হায়ারোগ্লিফিক্স (Hieroglyphics)}
\end{itemize}

\chsub{}{পজিশনাল সংখ্যাপদ্ধতি}
\B{যে পদ্ধতিতে সংখ্যার মান ব্যবহৃত চিহ্ন বা অংকসমূহের পজিশন বা অবস্থানের উপর নির্ভর করে তাকে পজিশনাল সংখ্যাপদ্ধতি বলে।}
\begin{itemize}
    \item \B{এই পদ্ধতিতে অংকে (সংখ্যার) ভিন্ন ভিন্ন মান বহন করে।}
    \item \B{এই পদ্ধতিতে সংখ্যাপদ্ধতির বেজ, অংকের অবস্থান এবং রেডিক্স পয়েন্ট একটি গুরুত্বপূর্ণ বিষয়।}
    \item \B{পজিশনাল সংখ্যা পদ্ধতিতে রেডিক্স পয়েন্ট দিয়ে প্রতিটি সংখ্যার পূর্ণাংশ এবং ভগ্নাংশ এই দুই ভাগে বিভক্ত করা হয়।}
\end{itemize}

\chsub{}{সংখ্যা পদ্ধতির বেজ (Base)}
\B{কোনো সংখ্যা পদ্ধতিতে ব্যবহৃত অংক, প্রতীক বা চিহ্নের মোট সংখ্যাকে ঐ সংখ্যা পদ্ধতির বেজ (Base) বলা হয়।}

\chsub{}{পজিশনাল সংখ্যা পদ্ধতি}
\begin{enumerate}
    \item \B{বাইনারি - (0,1) বেজ বা ভিত্তি হলো ২}
    \item \B{অক্টাল - (0,1,2,3,4,5,6,7) বেজ বা ভিত্তি হলো ৮}
    \item \B{হেক্সাডেসিমাল - (0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F) বেজ বা ভিত্তি হলো ১৬}
    \item \B{দশমিক/ ডেসিমাল - (0,1,2,3,4,5,6,7,8,9) বেজ বা ভিত্তি হলো ১০}
\end{enumerate}

\chsub{}{দশমিক বা ডেসিমাল সংখ্যা পদ্ধতি}
\B{ডেসিমাল শব্দের অর্থ হলো ১০ (দশ)। যে সংখ্যা পদ্ধতিতে ১০টি (০,১,২,৩,৪,৫,৬,৭,৮,৯) প্রতীক বা চিহ্ন ব্যবহার করা হয় তাকে দশমিক বা ডেসিমাল সংখ্যা পদ্ধতি বলে। দশমিক বা ডেসিমাল সংখ্যা পদ্ধতিতে ০(শূন্য) থেকে ৯(নয়) পর্যন্ত ১০(দশ) টি প্রতীক বা চিহ্ন বা সংখ্যা ব্যবহার করা হয় বলে এর Base বা ভিত্তি হলো ১০।}
\begin{itemize}
    \item \B{দশমিক সংখ্যা পদ্ধতিকে হিন্দু অ্যারাবিক সংখ্যা পদ্ধতি।}
    \item \B{প্রাচীন ভারতে সর্বপ্রথম দশমিক সংখ্যা পদ্ধতির ব্যবহার শুরু হয়েছিল।}
    \item \B{আমরা সংখ্যা উপস্থাপন ও হিসাব নিকাশের জন্য সাধারণত দশমিক বা ডেসিমাল সংখ্যা পদ্ধতি ব্যবহার করি।}
\end{itemize}

\chsub{}{চিহ্ন যুক্ত সংখ্যা প্রকাশের জন্য ৩টি গঠন রয়েছে।}
\begin{enumerate}
    \item \B{১. প্রকৃত মান গঠন}
    \item \B{২. ১ এর পরিপূরক (1's complement)}
    \item \B{৩. ২ এর পরিপূরক (2's complement) - এই পদ্ধতিকে negotion বলে।}
\end{enumerate}

\chsub{}{প্রকৃত মান গঠন কম্পিউটিং এর জন্য উপযোগী নয়}
\B{প্রকৃত মান গঠন পদ্ধতি হলো সংখ্যার ঋণাত্মক মান গঠনের একটি পদ্ধতি। এই পদ্ধতিতে কোনো সংখ্যার বাইনারি মানের পূর্বের অতিরিক্ত একটি বিট ০ বসালে ধনাত্মক বিবেচিত হয় এবং অতিরিক্ত একটি বিট ১ বসালে ঋণাত্মক বিবেচিত হয়। এই পদ্ধতি ০ এর ক্ষেত্রে প্রয়োগ করলে ০ এর ধনাত্মক এবং ঋণাত্মক দুটি পৃথক অবস্থা পাওয়া যায়। কিন্তু}
\B{এটি গণিতের সাথে বা বাস্তবের সাথে সামঞ্জস্যপূর্ণ নয়। এই কারণে প্রকৃত মান গঠন পদ্ধতি কম্পিউটিং এর জন্য উপযোগী নয়।}

\chsub{}{১ এর পরিপূরক গঠন কম্পিউটিং এর জন্য উপযোগী নয়}
\B{১ এর পরিপূরক গঠন পদ্ধতি হলো সংখ্যার ঋণাত্মক মান গঠনের একটি পদ্ধতি। এই পদ্ধতিতে কোনো সংখ্যার স্বাভাবিক বাইনারি মান ধনাত্মক বিবেচিত হয়। কিন্তু ঋণাত্মক হতে হলে শূন্যের পরিবর্তে ১ এবং এক এর পরিবর্তে শূন্য বসাতে হয়। এ পদ্ধতি শূন্যের উপর প্রয়োগ করলে শূন্যের ধনাত্মক এবং ঋণাত্মক দুটি পৃথক অবস্থা পাওয়া যায়। কিন্তু এটি বাস্তবের সাথে মিল নয়। এই কারণে ১ এর পরিপূরক গঠন পদ্ধতি কম্পিউটিং এর জন্য উপযোগী নয়।}

\chsub{}{২ এর পরিপূরক গঠন কম্পিউটিং এর জন্য উপযোগী}
\B{২ এর পরিপূরক গঠন পদ্ধতি হলো সংখ্যার ঋণাত্মক মান গঠনের একটি পদ্ধতি। এই পদ্ধতিতে কোনো সংখ্যার স্বাভাবিক বাইনারি মান ধনাত্মক বিবেচিত হয়। কিন্তু ঋণাত্মক হতে হলে ১ এর পরিপূরক রূপান্তর করে তার সাথে ১ যোগ করতে হয়। এ পদ্ধতি শূন্যের উপর প্রয়োগ করলে শূন্যের ধনাত্মক ও ঋণাত্মক একই অবস্থা বা মান পাওয়া যায় যেটি বাস্তবের সাথে সামঞ্জস্যপূর্ণ। এই কারণে ২ এর পরিপূরক গঠন পদ্ধতি কম্পিউটিং এর জন্য উপযোগী।}

\chsub{}{রেজিস্টার (Register)}
\B{রেজিস্টার হলো CPU বা মাইক্রোপ্রসেসর এর অভ্যন্তরীণ মেমোরি।}

\chsub{}{কম্পিউটার কোডিং}
\B{কম্পিউটারসহ বিভিন্ন ইলেকট্রনিক্স যন্ত্র বা ডিভাইস ডাটা বা উপাত্ত নিয়ে কাজ করে। এ সমস্ত ডাটা সাধারণত সংখ্যা, বর্ণ বা চিহ্ন নিয়ে গঠিত। কম্পিউটারের অভ্যন্তরীণ সকল কাজ সংগঠিত হয় বাইনারি সংখ্যা (০ ও ১) এর মাধ্যমে। তাই বিভিন্ন সংখ্যা, বর্ণ বা চিহ্নকে আলাদা আলাদাভাবে সিপিইউকে বোঝানোর জন্য ঐ সকল সংখ্যা, বর্ণ বা চিহ্নের আলাদা আলাদাভাবে বাইনারি সংখ্যার মাধ্যমে অদ্বিতীয় (Unique) সংকেত তৈরি করা হয়। এই অদ্বিতীয় সংকেতকে বলা হয় কোড। এই রূপান্তর প্রক্রিয়াকে কোডিং বলে। এই কোডের মাধ্যমেই কম্পিউটার দৈনন্দিন কাজে ব্যবহৃত বিভিন্ন ডাটা যেমন: সংখ্যা, টেক্সট বা বর্ণ, চিহ্ন, অডিও ও ভিডিও ইত্যাদিকে উপস্থাপন করে।}

\begin{center}
\B{কোড / Code} \\[0.2cm]
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{cccc}
\cline{1-4}
\multicolumn{1}{|c|}{\B{অক্টাল কোড / Code}} & \multicolumn{1}{c|}{\B{হেক্সাডেসিমাল কোড / Code}} & \multicolumn{1}{c|}{\B{বিসিডি কোড / BCD Code}} & \multicolumn{1}{c|}{\B{আলফানিউমেরিক কোড / Alphanumeric Code}} \\ \cline{1-4}
 & & & \multicolumn{1}{c}{$\downarrow$} \\
 & & \cline{2-4}
 & & \multicolumn{1}{|c|}{\B{ইবিসিডিক কোড / EBCDIC Code}} & \multicolumn{1}{c|}{\B{অ্যাসকি কোড / ASCII Code}} & \multicolumn{1}{c|}{\B{ইউনি কোড / Uni Code}} \\ \cline{2-4}
\end{tabular}
\end{adjustbox}
\end{center}

\begin{itemize}
    \item \B{BCD Code $\rightarrow$ Binary Coded Decimal}
    \item \B{ASCII (অ্যাসকি) $\rightarrow$ American Standard Code for Information Interchange}
    \item \B{EBCDIC (ইবিসিডিক) $\rightarrow$ Extended Binary Coded Decimal Information Code}
    \item \B{UNI Code $\rightarrow$ Universal Code}
    \item \B{BCD $\rightarrow$ 4bit $\rightarrow$ $2^4 = 16$ টি কোড $\Rightarrow$ Numeric Code}
    \item \B{ASCII $\rightarrow$ 7bit $\rightarrow$ $2^7 = 128$ টি কোড $\Rightarrow$ Alpha Numeric Code}
    \item \B{ASCII $\rightarrow$ 8bit $\rightarrow$ $2^8 = 256$ টি কোড $\Rightarrow$ Alpha Numeric Code}
    \item \B{EBCDIC $\rightarrow$ 8bit $\rightarrow$ $2^8 = 256$ টি কোড $\Rightarrow$ Alpha Numeric Code}
\end{itemize}
\begin{itemize}
    \item \B{UNI Code $\rightarrow$ 16bit $\rightarrow$ $2^{16} = 65536$ টি কোড $\Rightarrow$ Alpha Numeric Code এই কোড দিয়ে পৃথিবীর সব ভাষা কম্পিউটারে ব্যবহার করা হয়।}
\end{itemize}

\chsub{}{IBM (International Business Machine)}
\B{এটি একটি হার্ডওয়্যার নির্মাতা প্রতিষ্ঠান।}

\chsub{}{BCD কোডকে Numeric Code বলা হয়}
\B{BCD এর পুরো নাম Binary Coded Decimal। এই কোডে 4bit ব্যবহার করে $2^4 = 16$টি কোড পাওয়া গেছে। এই কোড ব্যবহার করা হয়েছে শুধু গাণিতিক অংক এবং গাণিতিক চিহ্নের জন্য। কোনো ভাষার কোনো বর্ণের জন্য ব্যবহার করে হয়নি এই কারণে BCD কোডকে Numeric Code বা নাম্বার কোড বলা হয়।}

\chsub{}{ASCII কোডকে Alpha Numeric Code বলা হয়}
\B{ASCII কোড এর পূর্ণরূপ হলো American Standard Code for Information Interchange। এই করে 7bit ব্যবহার করে $2^7 = 128$টি কোড এবং 8bit ব্যবহার করে $2^8 = 256$টি কোড পাওয়া গেছে। এ কোড ব্যবহার করা হয়েছে গাণিতিক অংক ও ইংরেজি বর্ণের জন্য। এই জন্য একে বলা হয় Alpha Numeric Code}

\begin{center}
    \B{\underline{Digital Device}}
\end{center}

\chsub{}{বুলিয়ান অ্যালজেবরা}
\B{যৌক্তিক চলক ও যুক্তি মূলক অপারেশনের সমন্বয়ে গঠিত গণিতকে বুলিয়ান অ্যালজেবরা বলে।}
\begin{align*}
    \text{Present} - 1 &\rightarrow \text{(2v-5v)} \\
    \text{Absent} - 0 &\rightarrow \text{(0v-0.8v)}
\end{align*}

\chsub{}{বুলিয়ান অ্যালজেবরার বৈশিষ্ট্য}
\begin{enumerate}
    \item \B{শুধু ১ ও ০ নিয়ে কাজ করে বিধায় এটি সহজ।}
    \item \B{গণিত ও যুক্তির মধ্যে সম্পর্ক স্থাপনের মাধ্যমে যোগ ও গুণের কাজ করে।}
    \item \B{১ ও ০ দ্বারা কোনো প্রকার প্রতীক, চিহ্ন বা বর্ণ ব্যবহার করা যায় না।}
    \item \B{ইনপুট ও আউটপুটে ০ ও ১ এর মধ্যে যেকোনো একটি পাওয়া যায়।}
    \item \B{এটি যুক্তিমূলক অ্যালজেবরা তাই জ্যামিতি ও ত্রিকোণমিতির সূত্র প্রয়োগ করা যায় না।}
\end{enumerate}

\chsub{}{বুলিয়ান অ্যালজেবরা ও দশমিক অ্যালজেবরার পার্থক্য}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|l|c|l|}
\hline
\multicolumn{2}{|c|}{\B{বুলিয়ান অ্যালজেবরা}} & \multicolumn{2}{c|}{\B{দশমিক অ্যালজেবরা}} \\ \hline
i. & \B{বুলিয়ান অ্যালজেবরায় ০ ও ১ দুইটি অংক ব্যবহৃত হয়।} & i. & \B{দশমিক অ্যালজেবরায় ০ থেকে ৯ যেকোনো একটি অংক ব্যবহৃত হতে পারে।} \\ \hline
ii. & \B{বুলিয়ান চলকের ২টি মান থাকায় গাণিতিক কাজ তুলনামূলক সহজ।} & ii. & \B{দশমিক চলকে গাণিতিক কাজ তুলনামূলক কঠিন।} \\ \hline
iii. & \B{ভগ্নাংশ, লগারিদম, বর্গ, ঋণাত্মক সংখ্যা, কাল্পনিক সংখ্যা ইত্যাদি ব্যবহার করা যায় না।} & iii. & \B{ভগ্নাংশ, লগারিদম, বর্গ, ঋণাত্মক সংখ্যা, কাল্পনিক সংখ্যা ইত্যাদি ব্যবহার করা যায়।} \\ \hline
iv. & \B{শুধুমাত্র পুরক, যোগ ও গুণের কাজ করা যায়।} & iv. & \B{যোগ, বিয়োগ, গুণ ও ভাগ ইত্যাদি কাজ করা যায়।} \\ \hline
v. & \B{জ্যামিতিক বা ত্রিকোণমিতিক সূত্র প্রয়োগ করা যায় না।} & v. & \B{জ্যামিতিক বা ত্রিকোণমিতিক সূত্র প্রয়োগ করা যায়।} \\ \hline
\end{tabular}
\end{adjustbox}

\chsub{}{বুলিয়ান চলক}
\B{বুলিয়ান অ্যালজেবরায় যায় মান সময়ের সাথে পরিবর্তিত হয় তাকে বুলিয়ান চলক বলে। যেমন: A+B এখানে A আর B দুইটি চলক}

\chsub{}{বুলিয়ান ধ্রুবক}
\B{বুলিয়ান অ্যালজেবরায় যার মান সময়ের সাথে অপরিবর্তিত থাকে তাকে বুলিয়ান ধ্রুবক বলে। যেমন: ০ ও ১}

\chsub{}{বুলিয়ান পুরক}
\B{বুলিয়ান অ্যালজেবরায় দুইটি সম্ভাব্য মান ০ ও ১ কে একটি অপরটির পুরক বলা হয়।}
\chsub{}{বুলিয়ান স্বতঃসিদ্ধ (Boolean Postulates)}
\B{বুলিয়ান অ্যালজেবরায় শুধুমাত্র যোগ ও গুণের মাধ্যমেই সমস্ত গাণিতিক কাজ করা হয়। যোগ ও গুণের ক্ষেত্রে বুলিয়ান অ্যালজেবরা কিছু নিয়ম মেনে চলে, এই নিয়মগুলোকে বুলিয়ান স্বতঃসিদ্ধ বলে।}

\chsub{}{১. বুলিয়ান যোগের স্বতঃসিদ্ধ (যৌক্তিক যোগ বা Logical OR):}
\B{বুলিয়ান যোগের স্বতঃসিদ্ধ নিয়মগুলো নিচে দেওয়া হলো:}
\begin{align*}
    0 + 0 &= 0 \\
    0 + 1 &= 1 \\
    1 + 0 &= 1 \\
    1 + 1 &= 1
\end{align*}
\B{যৌক্তিক যোগের ক্ষেত্রে যেকোনো একটি ইনপুট ১ হলে আউটপুট ১ হবে। অন্যথায় আউটপুট ০ হবে।}

\chsub{}{২. বুলিয়ান গুণের স্বতঃসিদ্ধ (যৌক্তিক গুণ বা Logical AND):}
\B{বুলিয়ান গুণের স্বতঃসিদ্ধ নিয়মগুলো নিচে দেওয়া হলো:}
\begin{align*}
    0 \cdot 0 &= 0 \\
    0 \cdot 1 &= 0 \\
    1 \cdot 0 &= 0 \\
    1 \cdot 1 &= 1
\end{align*}
\B{যৌক্তিক গুণের ক্ষেত্রে সবকটি ইনপুট ১ হলে আউটপুট ১ হবে। যেকোনো একটি ইনপুট ০ হলে আউটপুট ০ হবে।}

\chsub{}{দ্বৈত নীতি (Duality Principle)}
\B{বুলিয়ান অ্যালজেবরায় ব্যবহৃত সকল উপপাদ্য বা সমীকরণ যে নীতি বা নিয়ম মেনে একটি বৈধ সমীকরণ থেকে অপর একটি বৈধ সমীকরণ নির্ণয় করা যায় তাকে দ্বৈত নীতি বলে।}
\begin{enumerate}
    \item \B{১. ১ এর পরিবর্তে ০ এবং ০ এর পরিবর্তে ১ ব্যবহার করে।}
    \item \B{২. OR (+) এর পরিবর্তে AND ($\cdot$) এবং AND ($\cdot$) এর পরিবর্তে OR (+) ব্যবহার করে।}
\end{enumerate}

\chsub{}{বুলিয়ান উপপাদ্য (Boolean Theorems)}

\B{১. মৌলিক উপপাদ্য (Basic Theorems):}
\begin{itemize}
    \item \B{(a) $A + 0 = A$} \hspace{2cm} \B{(e) $A \cdot 1 = A$}
    \item \B{(b) $A + 1 = 1$} \hspace{2cm} \B{(f) $A \cdot 0 = 0$}
    \item \B{(c) $A + A = A$} \hspace{2cm} \B{(g) $A \cdot A = A$}
    \item \B{(d) $A + \overline{A} = 1$} \hspace{1.8cm} \B{(h) $A \cdot \overline{A} = 0$}
\end{itemize}

\B{২. বিনিময় উপপাদ্য (Commutative Theorems):}
\begin{itemize}
    \item \B{(a) $A + B = B + A$}
    \item \B{(b) $A \cdot B = B \cdot A$}
\end{itemize}

\B{৩. অনুষঙ্গ উপপাদ্য (Associative Theorems):}
\begin{itemize}
    \item \B{(a) $A + (B + C) = (A + B) + C$}
    \item \B{(b) $A \cdot (B \cdot C) = (A \cdot B) \cdot C$}
\end{itemize}

\B{৪. বিভাজন উপপাদ্য (Distributive Theorems):}
\begin{itemize}
    \item \B{(a) $A \cdot (B + C) = A \cdot B + A \cdot C$}
    \item \B{(b) $A + B \cdot C = (A + B) \cdot (A + C)$}
\end{itemize}

\B{৫. সহায়ক উপপাদ্য (Absorption Theorems):}
\begin{itemize}
    \item \B{(a) $A + A \cdot B = A$}
    \item \B{(b) $A \cdot (A + B) = A$}
    \item \B{(c) $A + \overline{A} \cdot B = A + B$}
\end{itemize}

\B{৬. ডিমরগ্যান উপপাদ্য (De Morgan's Theorems):}
\begin{itemize}
    \item \B{(a) $\overline{A + B} = \overline{A} \cdot \overline{B}$}
    \item \B{(b) $\overline{A \cdot B} = \overline{A} + \overline{B}$}
\end{itemize}

\B{৭. দ্বিপূরণ উপপাদ้য় (Double Complement Theorem):}
\begin{itemize}
    \item \B{$\overline{\overline{A}} = A$}
\end{itemize}
\chsub{}{বুলিয়ান স্বতঃসিদ্ধ}
\B{যোগ ও গুণের জন্য বুলিয়ান অ্যালজেবরার বিশেষ কিছু নিয়ম সত্য বলে মেনে নেওয়া হয়। এই নিয়মগুলোকে বুলিয়ান স্বতঃসিদ্ধ বলে। বুলিয়ান স্বতঃসিদ্ধ ২ ভাগে বিভক্ত। যথা:}
\begin{enumerate}
    \item[i.] \B{যোগের বুলিয়ান স্বতঃসিদ্ধ।}
    \item[ii.] \B{গুণের বুলিয়ান স্বতঃসিদ্ধ।}
\end{enumerate}

\chsub{}{i) যোগের বুলিয়ান স্বতঃসিদ্ধ}
\B{যোগের সময় বুলিয়ান অ্যালজেবরা যে সকল নিয়ম মেনে চলে তাকে যোগের বুলিয়ান স্বতঃসিদ্ধ বলে। নিয়ম}
\begin{align*}
    0+1 &= 1 \\
    0+0 &= 0 \\
    1+0 &= 1 \\
    1+1 &= 1
\end{align*}

\chsub{}{ii) গুণের বুলিয়ান স্বতঃসিদ্ধ}
\B{গুণের সময় বুলিয়ান অ্যালজেবরা যে সকল নিয়ম মেনে চলে তাকে গুণের বুলিয়ান স্বতঃসিদ্ধ বলে। নিয়ম:}
\begin{align*}
    0 \cdot 0 &= 0 \\
    0 \cdot 1 &= 0 \\
    1 \cdot 0 &= 0 \\
    1 \cdot 1 &= 1
\end{align*}

\chsub{}{লজিক গেট}
\B{যে সকল ডিজিটাল ইলেকট্রনিক সার্কিট এক বা একাধিক ইনপুট গ্রহণ করে বুলিয়ান বীজগণিত অনুযায়ী প্রক্রিয়াজাত করে একটি মাত্র আউটপুট প্রদান করে তাকে লজিক গেট বলে। লজিক গেট ২ প্রকার। যথা:}
\begin{enumerate}
    \item \B{মৌলিক গেট}
    \item \B{যৌগিক গেট}
\end{enumerate}

\B{১. মৌলিক গেট ৩টি। যথা: AND, OR, NOT} \\
\B{২. যৌগিক গেট ২ প্রকার}
\begin{enumerate}
    \item[i.] \B{বিশেষ গেট ২টি। যথা: X-OR, X-NOR}
    \item[ii.] \B{সর্বজনীন গেট ২টি। যথা: NOR, NAND}
\end{enumerate}

\chsub{}{মৌলিক গেট}
\B{যে গেটগুলোর মাধ্যমে এককভাবে কোনো বুলিয়ান অপারেশন সম্পাদন করা হয় তাকে মৌলিক গেট বলে।}

\begin{center}
\begin{adjustbox}{max width=\linewidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.18\linewidth}|>{\centering\arraybackslash}p{0.31\linewidth}|>{\centering\arraybackslash}p{0.19\linewidth}|>{\centering\arraybackslash}p{0.25\linewidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{গেট}} & \textbf{\B{রঙিন প্রতীক}} & \textbf{\B{ফাংশন}} & \textbf{\B{সত্য সারণি}} \\\hline
\B{OR} &
\begin{tikzpicture}[scale=0.52,thick,every node/.style={font=\scriptsize}]
\node[or gate US, draw=clrBlue, very thick, fill=white, logic gate inputs=nn, minimum width=1.55cm] (g) at (1.25,0) {};
\draw[-Latex,clrGreen,very thick] (-0.55,0.34) node[left]{A} -- (g.input 1);
\draw[-Latex,clrGreen,very thick] (-0.55,-0.34) node[left]{B} -- (g.input 2);
\draw[-Latex,accent,very thick] (g.output) -- (2.95,0) node[right]{X};
\node[clrBlue,font=\tiny\bfseries] at (1.12,0) {OR};
\end{tikzpicture} &
\LAT{$X=A+B$} &
\begin{tabular}{cc|c}\rowcolor{tblhdr}\textbf{A}&\textbf{B}&\textbf{X}\\\hline\rowcolor{tblalt}0&0&0\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&1\end{tabular} \\\hline
\B{AND} &
\begin{tikzpicture}[scale=0.52,thick,every node/.style={font=\scriptsize}]
\node[and gate US, draw=clrDarkGreen, very thick, fill=white, logic gate inputs=nn, minimum width=1.55cm] (g) at (1.25,0) {};
\draw[-Latex,clrBlue,very thick] (-0.55,0.34) node[left]{A} -- (g.input 1);
\draw[-Latex,clrBlue,very thick] (-0.55,-0.34) node[left]{B} -- (g.input 2);
\draw[-Latex,accent,very thick] (g.output) -- (2.95,0) node[right]{X};
\node[clrDarkGreen,font=\tiny\bfseries] at (1.05,0) {AND};
\end{tikzpicture} &
\LAT{$X=A\cdot B$} &
\begin{tabular}{cc|c}\rowcolor{tblhdr}\textbf{A}&\textbf{B}&\textbf{X}\\\hline\rowcolor{tblalt}0&0&0\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&1\end{tabular} \\\hline
\B{NOT} &
\begin{tikzpicture}[scale=0.55,thick,every node/.style={font=\scriptsize}]
\node[not gate US, draw=clrDarkRed, very thick, fill=white, minimum width=1.35cm] (g) at (1.1,0) {};
\draw[-Latex,clrBlue,very thick] (-0.48,0) node[left]{A} -- (g.input);
\draw[-Latex,accent,very thick] (g.output) -- (2.75,0) node[right]{$\bar{A}$};
\node[clrDarkRed,font=\tiny\bfseries] at (0.92,0) {NOT};
\end{tikzpicture} &
\LAT{$X=\bar{A}$} &
\begin{tabular}{c|c}\rowcolor{tblhdr}\textbf{A}&\textbf{X}\\\hline\rowcolor{tblalt}0&1\\1&0\end{tabular} \\\hline
\end{tabular}
\end{adjustbox}
\end{center}

\chsub{}{যৌগিক গেট}
\begin{center}
\begin{adjustbox}{max width=\linewidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.19\linewidth}|>{\centering\arraybackslash}p{0.22\linewidth}|>{\centering\arraybackslash}p{0.22\linewidth}|>{\centering\arraybackslash}p{0.24\linewidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{গেট}}&\textbf{\B{কাজ}}&\textbf{\B{ফাংশন}}&\textbf{\B{সত্য সারণি}}\\\hline
\B{NAND}&\B{AND + NOT}&\LAT{$X=\overline{A\cdot B}$}&\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&0\end{tabular}\\\hline
\B{NOR}&\B{OR + NOT}&\LAT{$X=\overline{A+B}$}&\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&0\end{tabular}\\\hline
\B{XOR}&\B{ইনপুট ভিন্ন হলে ১}&\LAT{$X=A\oplus B$}&\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&0\\0&1&1\\\rowcolor{tblalt}1&0&1\\1&1&0\end{tabular}\\\hline
\B{XNOR}&\B{ইনপুট একই হলে ১}&\LAT{$X=\overline{A\oplus B}$}&\begin{tabular}{cc|c}\rowcolor{tblhdr}A&B&X\\\hline\rowcolor{tblalt}0&0&1\\0&1&0\\\rowcolor{tblalt}1&0&0\\1&1&1\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}

\chsub{}{অ্যাডার}
\B{বাইনারি যোগের জন্য তৈরি সমবায়িক বর্তনীকে অ্যাডার বলে।}

\chsub{}{হাফ অ্যাডার}
\B{দুটি ইনপুট বিট A ও B যোগ করে Sum এবং Carry তৈরি করে।}
\begin{center}
\begin{adjustbox}{max width=\linewidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.27\linewidth}|>{\centering\arraybackslash}p{0.43\linewidth}|>{\centering\arraybackslash}p{0.22\linewidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{সূত্র}}&\textbf{\B{রঙিন সার্কিট}}&\textbf{\B{সত্য সারণি}}\\\hline
\LAT{$S=A\oplus B$}\par\LAT{$C=A\cdot B$}&
\begin{tikzpicture}[scale=0.50,thick,every node/.style={font=\scriptsize}]
\node[xor gate US, draw=clrBlue, very thick, fill=white, logic gate inputs=nn] (x) at (2.2,0.8) {};
\node[and gate US, draw=clrDarkGreen, very thick, fill=white, logic gate inputs=nn] (a) at (2.2,-0.8) {};
\draw[clrBlue,very thick] (-0.4,1.15) node[left]{A} -- (0.7,1.15) |- (x.input 1);
\draw[clrBlue,very thick] (-0.4,-0.15) node[left]{B} -- (0.7,-0.15) |- (x.input 2);
\draw[clrGreen,very thick] (0.7,1.15) |- (a.input 1);
\draw[clrGreen,very thick] (0.7,-0.15) |- (a.input 2);
\draw[-Latex,accent,very thick] (x.output) -- (4.0,0.8) node[right]{Sum};
\draw[-Latex,clrDarkGreen,very thick] (a.output) -- (4.0,-0.8) node[right]{Carry};
\node[clrBlue,font=\tiny\bfseries] at (2.0,0.8) {XOR};
\node[clrDarkGreen,font=\tiny\bfseries] at (1.95,-0.8) {AND};
\end{tikzpicture}&
\begin{tabular}{cc|cc}\rowcolor{tblhdr}A&B&S&C\\\hline\rowcolor{tblalt}0&0&0&0\\0&1&1&0\\\rowcolor{tblalt}1&0&1&0\\1&1&0&1\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}

\chsub{}{পূর্ণযোগের বর্তনী/ ফুল অ্যাডার}
\B{A, B এবং পূর্ববর্তী ক্যারি $C_{in}$ — এই ৩টি বিট যোগ করে Sum ও $C_{out}$ দেয়।}
\begin{center}
\begin{adjustbox}{max width=\linewidth,center}
\begin{tabular}{|>{\centering\arraybackslash}p{0.25\linewidth}|>{\centering\arraybackslash}p{0.46\linewidth}|>{\centering\arraybackslash}p{0.22\linewidth}|}
\hline
\rowcolor{tblhdr}\textbf{\B{সূত্র}}&\textbf{\B{ডেটা-ফ্লো সার্কিট}}&\textbf{\B{পূর্ণ সত্য সারণি}}\\\hline
\LAT{$S=A\oplus B\oplus C_{in}$}\par\LAT{$C_{out}=AB+AC_{in}+BC_{in}$}&
\begin{tikzpicture}[scale=0.48,thick,every node/.style={font=\scriptsize}]
\node[draw=clrBlue, very thick, fill=shape2!70, rounded corners, minimum width=1.15cm, minimum height=0.62cm] (ha1) at (1.35,0.72) {HA 1};
\node[draw=clrDarkGreen, very thick, fill=shape3!70, rounded corners, minimum width=1.15cm, minimum height=0.62cm] (ha2) at (3.15,0.72) {HA 2};
\node[or gate US, draw=clrOrange, very thick, fill=white, logic gate inputs=nn] (or) at (4.8,-0.42) {};
\draw[-Latex,clrBlue,very thick] (-0.55,1.08) node[left]{A} -- (ha1.west);
\draw[-Latex,clrBlue,very thick] (-0.55,0.36) node[left]{B} -- (ha1.west);
\draw[-Latex,accent,very thick] (ha1.east) -- (ha2.west);
\draw[-Latex,clrPurple,very thick] (-0.55,-0.18) node[left]{$C_{in}$} -| (ha2.south);
\draw[-Latex,accent,very thick] (ha2.east) -- (5.9,0.72) node[right]{Sum};
\draw[-Latex,clrDarkGreen,very thick] (ha1.south) |- (or.input 2);
\draw[-Latex,clrDarkGreen,very thick] (ha2.south) |- (or.input 1);
\draw[-Latex,clrOrange,very thick] (or.output) -- (5.9,-0.42) node[right]{$C_{out}$};
\end{tikzpicture}&
\begin{tabular}{ccc|cc}\rowcolor{tblhdr}A&B{$C_{in}$}&S&{$C_{out}$}\\\hline\rowcolor{tblalt}0&0&0&0&0\\0&0&1&1&0\\\rowcolor{tblalt}0&1&0&1&0\\0&1&1&0&1\\\rowcolor{tblalt}1&0&0&1&0\\1&0&1&0&1\\\rowcolor{tblalt}1&1&0&0&1\\1&1&1&1&1\end{tabular}\\\hline
\end{tabular}
\end{adjustbox}
\end{center}
\vspace{0.5cm}

\begin{enumerate}
    \item[৩.] \B{পাঞ্চকার্ড রিডার হতে কম্পিউটারে স্থানান্তরে এবং কম্পিউটার হতে পাঞ্চকার্ডে স্থানান্তরে।}
\end{enumerate}

\chsub{}{\B{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন মেথডের সুবিধা}}
\begin{enumerate}
    \item[১.] \B{প্রেরক যেকোনো সময় ডেটা স্থানান্তর করতে পারেন এবং গ্রাহক তা গ্রহণ করতে পারে।}
    \item[২.] \B{এটির ইনস্টলেশন ব্যয় অত্যন্ত কম।}
\end{enumerate}

\chsub{}{\B{অ্যাসিনক্রোনাইজেশন/ অ্যাসিনক্রোনাস ট্রান্সমিশন মেথডের অসুবিধা}}
\begin{enumerate}
    \item[১.] \B{ডেটা ট্রান্সমিশনে গতি অপেক্ষাকৃত ধীর।}
\end{enumerate}

\chsub{}{\B{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথড}}
\B{যে ডেটা ট্রান্সমিশন সিস্টেমে প্রেরক স্টেশনে প্রথমে ডেটাকে কোনো প্রাইমারি স্টোরেজ ডিভাইসে সংরক্ষণ করে নেওয়া হয়; অতঃপর ডেটার ক্যারেক্টার সমূহকে ব্লক বা প্যাকেট বা ফ্রেম আকারে ভাগ করে প্রতিবারে একটি করে ব্লক ট্রান্সমিট করা হয় তাকে সিনক্রোনাইজেশন/ সিনক্রোনাস ট্রান্সমিশন বলে।}

\chsub{}{\B{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের প্রক্রিয়া}}
\begin{enumerate}
    \item[১.] \B{এই পদ্ধতিতে বিরতিহীনভাবে প্রেরক যন্ত্র থেকে গ্রাহক যন্ত্রে ডেটা পাঠানো হয়। একে বিরতিহীন ডেটা ট্রান্সমিশন বলে।}
    \item[২.] \B{যেহেতু প্রেরিত ডেটা ব্যবহার করে গ্রাহক যন্ত্র তার ক্লককে সমন্বিত করে তাই প্রেরণ করার জন্য কোনো ডেটা না থাকলেও আইডল সিকোয়েন্স হিসেবে পূর্ব নির্ধারিত ডেটা পাঠানো হয়।}
    \item[৩.] \B{প্রতিবার একটি করে ব্লক ক্লকের সাথে সমন্বয় করে সমান বিরতি দিয়ে প্রেরণ করা হয়।}
    \item[৪.] \B{প্রতি ব্লকের শুরুতে ১ বা ২ বাইটের একটি হেডার ইনফরমেশন এবং ব্লক ডেটার শেষে ১ বা ২ বাইটের একটি ট্রেইলার ইনফরমেশন সিগন্যাল পাঠানো হয়।}
    \item[৫.] \B{গ্রাহক যন্ত্র হেডার সিগন্যাল ব্যবহার করে প্রেরকের ক্লকের স্পিডের সাথে সিনক্রোনাইজ বা সমন্বিত করে। ট্রেইলার ব্লকের শেষ নির্দেশ করে এবং কোনো কোনো ব্লকের ক্ষেত্রে ব্লকের ভেতরকার ভুল নির্ণয় এবং সংশোধনে সহায়তা করে।}
    \item[৬.] \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয়।}
\end{enumerate}

\chsub{}{\B{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের ব্যবহার}}
\begin{enumerate}
    \item[১.] \B{কম্পিউটার হতে কম্পিউটারে ডেটা স্থানান্তরে।}
    \item[২.] \B{দূরবর্তী কোনো স্থানে ডেটা স্থানান্তরে।}
    \item[৩.] \B{একই সাথে অনেকগুলো কম্পিউটারে ডেটা স্থানান্তরের ক্ষেত্রে।}
\end{enumerate}

\chsub{}{\B{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের সুবিধা}}
\begin{enumerate}
    \item[১.] \B{অবিরাম ট্রান্সমিশন কাজ চলতে থাকার ফলে তার ট্রান্সমিশন গতি অপেক্ষাকৃত বেশি।}
    \item[২.] \B{প্রতি ক্যারেক্টারের শুরু ও শেষে স্টার্ট ও স্টপ বিটের প্রয়োজন হয় না।}
    \item[৩.] \B{প্রতি ক্যারেক্টারের পর টাইম ইন্টারভেল এর প্রয়োজন হয় না।}
    \item[৪.] \B{তুলনামূলক কম সময় লাগে।}
\end{enumerate}

\chsub{}{\B{সিনক্রোনাইজেশন/ সিনক্রোনাস ডেটা ট্রান্সমিশন মেথডের অসুবিধা}}
\begin{enumerate}
    \item[১)] \B{তুলনামূলকভাবে ব্যয়বহুল।}
\end{enumerate}

\chsub{}{\B{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথড}}
\B{অ্যাসিনক্রোনাস ও সিনক্রোনাস এর একটি মিশ্র পদ্ধতি হচ্ছে আইসোক্রোনাইজেশন/ আইসোক্রোনাস।}

\chsub{}{\B{আইসোক্রোনাইজেশন/ আইসোক্রোনাস ডেটা ট্রান্সমিশন মেথডের প্রক্রিয়া}}
\begin{enumerate}
    \item[১.] \B{সিনক্রোনাস পদ্ধতির স্টার্ট ও স্টপ বিটের মাঝখানে সিনক্রোনাস পদ্ধতিতে ব্লক আকারে ডেটা ট্রান্সফার হয়।}
    \item[২.] \B{যখন প্রয়োজন তখন সেই ডেটা ট্রান্সমিট করা যায়।}
    \item[৩.] \B{প্রাইমারি স্টোরেজ ডিভাইসের প্রয়োজন হয় না।}
    \item[৪.] \B{ডেটা পাঠানোর শুরুতে স্টার্ট সিগন্যাল ও ডেটা পাঠানোর শেষে স্টপ সিগন্যাল পাঠানো হয়।}
\end{enumerate}

\vspace{0.5cm}

\begin{center}
    \fbox{\rule{0pt}{1.6cm}\hspace{1.6cm}} \\
    \B{\small Sub: ICT} \\
    \B{\small Instructor: Bidyut Kumar Mitra} \\
    \B{\small Prepared By Abu Salman} \\
    \B{\small Student of Cambrian College}
\end{center}
\vspace{-0.5cm}
\begin{center}
    \B{\Large ৪র্থ অধ্যায়} \\[0.2cm]
    \B{\large ওয়েব ডিজাইন পরিচিতি এবং HTML}
\end{center}
\rule{\linewidth}{1pt}

\chsub{}{\B{ওয়েব পেইজ}}
\B{ইন্টারনেট ব্যবহারকারীদের দেখার উপযোগী ইন্টারনেটের সাথে সংযুক্ত বিভিন্ন দেশের সার্ভারে রাখা ফাইলকে ওয়েব পেইজ বলে। ওয়েব পেইজ হলো ওয়ার্ল্ড ওয়াইড ওয়েবের একটি মাল্টিমিডিয়া ভিত্তিক হাইপারটেক্সট ডকুমেন্ট যেখানে টেক্সট, ছবি, অডিও, গ্রাফিক্স ও হাইপারলিংক থাকে।}

\chsub{}{\B{ওয়েবসাইট}}
\B{১৯৯০ সনে ব্রিটিশ পদার্থবিদ টিম বার্নাস লী (Tim Berners lee) সর্বপ্রথম ওয়েবসাইট ডিজাইনের প্রাথমিক ধারণা দেন। ইন্টারনেটের সাথে যথাযথভাবে যুক্ত কোন সার্ভারের বরাদ্দকৃত স্পেস বা লোকেশন যাতে এক বা একাধিক ওয়েব পেইজ একটি সাধারণ ডোমেইন নামের অধীনে রাখা হয় এবং ব্রাউজারের মাধ্যমে প্রদর্শন করা যায় তাকে ওয়েবসাইট বা সংক্ষেপে সাইট বলা হয়। ওয়েবসাইট গুলোকে প্রধানত দুই ভাগে ভাগ করা যায়। যথা:}
\begin{enumerate}
    \item[i.] \B{স্ট্যাটিক ওয়েবসাইট (Static website)}
    \item[ii.] \B{ডাইনামিক ওয়েবসাইট (Dynamic website)}
\end{enumerate}

\chsub{}{\B{i. স্ট্যাটিক ওয়েবসাইট (Static website)}}
\B{ওয়েব ব্রাউজিংয়ের সময় যে সকল ওয়েবসাইটের ডেটার মান পরিবর্তন করা যায় না, তাকে স্ট্যাটিক ওয়েবসাইট বলা হয়।}
\begin{itemize}
    \item \B{এ সকল ওয়েবসাইট কেবলমাত্র HTML দ্বারা তৈরি।}
    \item \B{এতে ডেটাবেজ ব্যবস্থাপনা করার সুযোগ নাই।}
\end{itemize}

\chsub{}{\B{ii. ডাইনামিক ওয়েবসাইট (Dynamic website)}}
\B{ওয়েব ব্রাউজিংয়ের সময় যে সকল ওয়েবসাইটের ডেটার মান পরিবর্তন করা যায়, তাকে ডাইনামিক ওয়েবসাইট বলা হয়।}
\begin{itemize}
    \item \B{এ সকল ওয়েবসাইটে যেকোনো সময় ডেটা ইনসার্ট, এডিট, ডিলিট বা আপডেট করা যায়।}
    \item \B{এ সকল ওয়েবসাইট গুলোতে অনলাইন ডেটাবেজ ব্যবস্থাপনার কাজ পরিচালনা করা যায়।}
    \item \B{এ ধরণের ওয়েবসাইট তৈরিতে PHP, Java Script, ASP. Net ইত্যাদি ব্যবহৃত হয়।}
\end{itemize}

\chsub{}{\B{হোম পেইজ}}
\B{একটি ওয়েবসাইট চালু হলে প্রথম যে পেইজটি প্রদর্শিত হয় তাকে হোম পেইজ বলে। এটিই হলো ওয়েব সাইটের মূল পেইজ যার সাথে অন্যান্য পেইজের লিংক থাকে।}

\chsub{}{\B{ওয়েব সার্ভার}}
\B{যে বিশেষ কম্পিউটারে ওয়েব পেইজগুলো সংরক্ষিত থাকে, তাকে ওয়েব সার্ভার বলে। এটি হল হার্ডওয়্যার, সফটওয়্যার এবং নেটওয়ার্কিং সুবিধার একটি সমন্বিত ব্যবস্থা যার সাহায্যে ইন্টারনেট ব্যবহারকারীকে তাদের চাহিদা অনুসারে ওয়েব সার্ভিস প্রদান করা হয়। বিভিন্ন ধরনের ওয়েব সার্ভার আছে। যেমন:}
\begin{itemize}
    \item \B{লিনাক্স - এর অ্যাপাচি (Apache),}
    \item \B{মাইক্রোসফট - এর আইআইএস (IIS),}
    \item \B{গুগল - এর জিডব্লিউএস (GWS) সার্ভার ইত্যাদি।}
\end{itemize}

\chsub{}{\B{ইউ.আর.এল (URL)}}
\B{URL এর পূর্ণরূপ হচ্ছে Uniform Resource Locator এটি কোনো ওয়েব পেইজের ঠিকানা প্রকাশ করে অর্থাৎ ওয়েব পেইজের অ্যাড্রেসকে URL বলে।}
\begin{itemize}
    \item \B{URL সবসময় ইংরেজি ছোট হাতের অক্ষরে লিখতে হয়।}
    \item \B{প্রতিটি URL মূলতঃ তিনটি অংশ নিয়ে গঠিত।}
\end{itemize}

\vspace{0.3cm}
\begin{center}
\B{https://www.google.com/search} \\[0.1cm]
\begin{tikzpicture}[scale=0.8]
    \draw[thick] (0,0) -- (0,-0.3) -- (1.5,-0.3) -- (1.5,0);
    \node at (0.75,-0.6) {\scriptsize Protocol};
    
    \draw[thick] (2.0,0) -- (2.0,-0.3) -- (5.0,-0.3) -- (5.0,0);
    \node at (3.5,-0.6) {\scriptsize Domain Name};
    
    \draw[thick] (5.5,0) -- (5.5,-0.3) -- (7.0,-0.3) -- (7.0,0);
    \node at (6.25,-0.6) {\scriptsize Server Path};
\end{tikzpicture}
\end{center}

\vspace{0.5cm}

\chsub{}{\B{প্রটোকল (Protocol)}}
\B{যে নিয়মনীতির উপর ভিত্তি করে ইন্টারনেটে ডেটা স্থানান্তর করা হয় সেই নিয়ম নীতিই হলো প্রটোকল। তথ্য আদান-প্রদানের জন্য যোগাযোগের কিছু সমষ্টিই হল প্রটোকল যা ব্রাউজার ও ওয়েব সার্ভারের মধ্যে যোগাযোগের জন্য ব্যবহৃত হয়। বিভিন্ন ধরনের প্রটোকল আছে। যেমন:}
\begin{itemize}
    \item \B{http (hyper text transfer protocol) $\rightarrow$ ওয়েব সাইট ব্রাউজিং আর জন্য ব্যবহৃত হয়।}
    \item \B{FTP (File Transfer Protocol) $\rightarrow$ ফাইল আদান প্রদান এর জন্য ব্যবহৃত হয়।}
    \item \B{VoIP (Voice over Internet Protocol) $\rightarrow$ ইন্টারনেট ব্যবহার করে ফোন করার জন্য ব্যবহৃত হয়।}
    \item \B{POP (Post Office Protocol) $\rightarrow$ মেইল ও ম্যাসেল আদান - প্রদান এর জন্য ব্যবহৃত হয়।}
    \item \B{SMTP (Simple Mail Transfer Protocol) $\rightarrow$ মেইল ও ম্যাসেল আদান - প্রদান এর জন্য ব্যবহৃত হয়।}
\end{itemize}

\chsub{}{\B{www (World Wide Web)}}
\B{ওয়ার্ল্ড ওয়াইড ওয়েব হল পৃথিবীর বিভিন্ন দেশের ওয়েব সার্ভারে সংরক্ষিত ও পরস্পর সংযোগযোগ্য ডকুমেন্ট বা ওয়েব পেইজ। ইন্টারনেটের সাহায্যে ওয়েব ব্রাউজার ব্যবহার করে ওয়েব পেইজগুলি দেখা যায়। সব উন্মুক্ত ওয়েব সাইট গুলিকে সমষ্টিগতভাবে www বলা হয়।}

\chsub{}{\B{ওয়েব পোর্টাল (Web Portal)}}
\B{ওয়েব পোর্টাল হলো একটি ওয়েবসাইট যেখানে অনেকগুলো উৎস থেকে সংগৃহীত তথ্য, বিভিন্ন গুরুত্বপূর্ণ লিংক দেওয়া থাকে এবং বিভিন্ন সার্ভিস বা সেবা পাওয়ার সুযোগ থাকে। যেমন: http://www.bangladesh.govt.bd//}

\chsub{}{\B{সার্চ ইঞ্জিন (Search Engine)}}
\B{সার্চ ইঞ্জিন হলো একটি সফটওয়্যার টুল যা ওয়ার্ল্ড ওয়াইড ওয়েব থেকে যে কোন ইনফরমেশন খুঁজে বের করে। যেমন: Google, Being, Yahoo, Pipilika ইত্যাদি।}

\chsub{}{\B{ওয়েব ব্রাউজার (Web Browser)}}
\B{ওয়েব ব্রাউজার হলো একটি সফটওয়্যার টুল যা ওয়ার্ল্ড ওয়াইড ওয়েব বা ইন্টারনেট থেকে কোন ওয়েব পেইজ বা ওয়েবসাইট খুঁজে বের করে। যেমন: Internet Explorer, Mozilla, Firefox, Opera ইত্যাদি।}

\chsub{}{\B{HTML}}
\B{Hyper Text Markup Language এর সংক্ষিপ্ত রূপ হলো HTML যা World Wide Web (www) ব্রাউজারে তথ্য প্রদর্শন বা ওয়েব পেইজে তথ্য উপস্থাপন ও ফরম্যাট করতে এটি ব্যবহার করা হয়।}
\begin{itemize}
    \item \B{এটি কোনো প্রোগ্রামিং ভাষা নয়।}
    \item \B{এটি হলো স্ক্রিপ্টিং ল্যাঙ্গুয়েজ।}
    \item \B{HTML হলো কতগুলি ট্যাগের সমষ্টি।}
\end{itemize}

\chsub{}{\B{ট্যাগ}}
\B{HTML ভাষায় সংরক্ষিত কিছু শব্দ বা কীওয়ার্ড যা কৌনিক বন্ধনীর মধ্যে রেখে ব্যবহার করা হয় তাকে ট্যাগ বলা হয়। যেমন: <html>, <body>, <head>, <font> ইত্যাদি। ট্যাগ দুই প্রকার। যথা:}
\begin{enumerate}
    \item[i.] \B{কনটেইনার ট্যাগ}
    \item[ii.] \B{এম্পটি ট্যাগ}
\end{enumerate}

\chsub{}{\B{i. কনটেইনার ট্যাগ}}
\B{যে সকল ট্যাগের ক্ষেত্রে শুরু ও শেষ ট্যাগ ব্যবহার করা হয় তাদেরকে কনটেইনার ট্যাগ বলা হয়। যেমন: <html>--------</html>, <body>--------</body> ইত্যাদি।}

\chsub{}{\B{ii. এম্পটি ট্যাগ}}
\B{যে সকল ট্যাগের ক্ষেত্রে শুরু আছে কিন্তু শেষ ট্যাগ ব্যবহার করা হয় না তাদেরকে এম্পটি ট্যাগ বলা হয়। যেমন: <img>, <br>, <hr> ইত্যাদি।}

\vspace{0.5cm}

\chsub{}{\B{এলিমেন্ট}}
\B{HTML ভাষায় শুরুর ট্যাগ এবং সমাপ্তি ট্যাগের মধ্যবর্তী অংশকে এলিমেন্ট বলে।}

\begin{center}
    \B{<b> Bangladesh </b>} \\
    \B{$\underbrace{\hspace{4cm}}_{\text{এলিমেন্ট}}$}
\end{center}

\chsub{}{\B{অ্যাট্রিবিউট}}
\B{ট্যাগের বৈশিষ্ট্যকে অ্যাট্রিবিউট বলা হয়।}
\B{<font face = "arial" color = "red" size = "20">-------</font>}
\B{এখানে, face, color, size হলো অ্যাট্রিবিউট।}

\chsub{}{\B{ভ্যালু}}
\B{অ্যাট্রিবিউটের মানকে ভ্যালু বলা হয়।}
\B{<font face = "arial" color = "red" size = "20">-------</font>}
\B{এখানে, arial, red, 20 হলো ভ্যালু।}

\chsub{}{\B{HTML এর গঠন}}
\begin{itemize}
    \item \B{টেক্সট এডিটর প্রোগ্রাম নোটপ্যাড বা ওয়ার্ডপ্যাড ব্যবহার করতে হবে।}
    \item \B{head অংশে ওয়েবসাইটের title থাকে।}
    \item \B{body অংশে ওয়েবপেইজের সকল এলিমেন্ট যেমন: ছবি, টেক্সট, ভিডিও ইত্যাদি।}
    \item \B{নোটপ্যাডে html কোডটি লিখে .html এক্সটেনশন যুক্ত করে সেভ করতে হবে। যেমন: File Name.html}
\end{itemize}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tikzpicture}[scale=0.85]
    \draw[thick] (0,0) rectangle (6,5.5);
    \node[anchor=west] at (0.2,5.2) {\B{<html>}};
    \node[anchor=west] at (0.5,4.7) {\B{<head>}};
    \node[anchor=west] at (0.8,4.2) {\B{<title>-------</title>}};
    \node[anchor=west] at (0.5,3.7) {\B{</head>}};
    \node[anchor=west] at (0.5,3.1) {\B{<body>}};
    \node[anchor=west] at (0.8,2.5) {\B{........................}};
    \node[anchor=west] at (0.8,1.9) {\B{........................}};
    \node[anchor=west] at (0.5,1.3) {\B{</body>}};
    \node[anchor=west] at (0.2,0.7) {\B{</html>}};
    
    \draw[thick] (-0.2,5.5) -- (-0.5,5.5) -- (-0.5,0) -- (-0.2,0);
    \node[anchor=east] at (-0.6,2.75) {\small\B{Main Section}};
    
    \draw[thick] (6.2,4.9) -- (6.5,4.9) -- (6.5,3.5) -- (6.2,3.5);
    \node[anchor=west] at (6.6,4.2) {\small\B{Head Section}};
    
    \draw[thick] (6.2,3.3) -- (6.5,3.3) -- (6.5,1.1) -- (6.2,1.1);
    \node[anchor=west] at (6.6,2.2) {\small\B{Body Section}};
\end{tikzpicture}
\end{adjustbox}
\end{center}

\chsub{}{\B{হেডিং ট্যাগ}}
\begin{itemize}
    \item \B{হেডিং ট্যাগ ৬ টি।}
    \item \B{<h1> ট্যাগ এর সাইজ সবচেয়ে বড়।}
    \item \B{<h6> ট্যাগ এর সাইজ সবচেয়ে ছোট।}
\end{itemize}

\begin{minipage}{0.5\linewidth}
    \B{<h1>...........................</h1>} \\
    \B{<h2>...........................</h2>} \\
    \B{<h3>...........................</h3>} \\
    \B{<h4>...........................</h4>} \\
    \B{<h5>...........................</h5>} \\
    \B{<h6>...........................</h6>}
\end{minipage}

\chsub{}{\B{টেক্সট ফরম্যাটিং ট্যাগ}}
\begin{itemize}
    \item \B{A<sup>2</sup> = $A^2$}
    \item \B{B<sub>2</sub> = $B_2$}
    \item \B{<font face = "Arial black" color = "red" size="20">----------</font>}
    \begin{itemize}
        \item[\B{$\hookrightarrow$}] \B{Font tag er অ্যাট্রিবিউট ৩ টি। যথা: i. Face \quad ii. Color \quad iii. Size}
    \end{itemize}
\end{itemize}

\chsub{}{\B{HTML লিস্ট}}
\B{একটি ওয়েব পেজকে সুন্দর ও আকর্ষণীয়ভাবে সাজানো এবং তথ্য উপস্থাপনার অন্যতম পদ্ধতি হল লিস্ট। HTML ব্যবহার করে তিন ধরণের লিস্ট তৈরি করা যায়।}
\begin{enumerate}
    \item[১.] \B{UL (Unorder List বা Bulleted List)}
    \item[২.] \B{OL (Order List বা Numbered List)}
    \item[৩.] \B{DL (Definition List)}
\end{enumerate}

\chsub{}{\B{UL (Unorder List বা Bulleted List)}}
\begin{itemize}
    \item \B{UL ট্যাগ এর অ্যাট্রিবিউট ১ টি। যথা: type}
    \item \B{Unorder লিস্টে ৩ ধরনের টাইপ ব্যবহার করা হয়।}
    \begin{itemize}
        \item \B{disk (By default) $\rightarrow$ $\bullet$}
        \item \B{circle (type ="circle") $\rightarrow$ $\circ$}
        \item \B{square (type="square") $\rightarrow$ $\blacksquare$}
    \end{itemize}
\end{itemize}

\vspace{0.3cm}
\begin{center}
\begin{tabular}{|c|c|}
\hline
\B{Ul list type} & \B{ব্রাউজারে প্রদর্শন} \\ \hline
\B{type="disk"} & $\bullet$ \\ \hline
\B{type="circle"} & $\circ$ \\ \hline
\B{type="square"} & $\blacksquare$ \\ \hline
\end{tabular}
\end{center}

\vspace{0.5cm}

\begin{center}
\begin{tabular}{p{0.48\linewidth} | p{0.48\linewidth}}
\hline
\multicolumn{2}{|c|}{\B{Ul ট্যাগের ব্যবহার}} \\ \hline
\centering\arraybackslash \B{কোড} & \centering\arraybackslash \B{ব্রাউজারে প্রদর্শন} \tabularnewline \hline
\begin{verbatim}
<ul>
  <li>Book</li>
  <li>Pencil</li>
</ul>
\end{verbatim} & 
\begin{itemize}
    \item Book
    \item Pencil
\end{itemize} \\ \hline
\begin{verbatim}
<ul type = "circle">
  <li>Book</li>
  <li>Pencil</li>
</ul>
\end{verbatim} & 
\begin{itemize}
    \item[$\circ$] Book
    \item[$\circ$] Pencil
\end{itemize} \\ \hline
\begin{verbatim}
<ul type = "square">
  <li>Book</li>
  <li>Pencil</li>
</ul>
\end{verbatim} & 
\begin{itemize}
    \item[$\blacksquare$] Book
    \item[$\blacksquare$] Pencil
\end{itemize} \\ \hline
\end{tabular}
\hfill
\begin{tabular}{p{0.48\linewidth} | p{0.48\linewidth}}
\hline
\multicolumn{2}{|c|}{\B{Ol ট্যাগের ব্যবহার}} \\ \hline
\centering\arraybackslash \B{কোড} & \centering\arraybackslash \B{ব্রাউজারে প্রদর্শন} \tabularnewline \hline
\begin{verbatim}
<ol>
  <li>Book</li>
  <li>Pencil</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item Book
    \item Pencil
\end{enumerate} \\ \hline
\begin{verbatim}
<ol type = "i">
  <li>Book</li>
  <li>Pencil</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item[i.] Book
    \item[ii.] Pencil
\end{enumerate} \\ \hline
\begin{verbatim}
<ol type = "I">
  <li>Book</li>
  <li>Pencil</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item[I.] Book
    \item[II.] Pencil
\end{enumerate} \\ \hline
\begin{verbatim}
<ol type = "a">
  <li>Book</li>
  <li>Pencil</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item[a.] Book
    \item[b.] Pencil
\end{enumerate} \\ \hline
\begin{verbatim}
<ol type = "A">
  <li>Book</li>
  <li>Pencil</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item[A.] Book
    \item[B.] Pencil
\end{enumerate} \\ \hline
\end{tabular}
\end{center}

\chsub{}{\B{OL (Order List বা Numbered List)}}
\begin{itemize}
    \item \B{OL ট্যাগ এর অ্যাট্রিবিউট ২ টি। যথা: i. type \quad ii. Start}
    \item \B{Order লিস্টে ৫ ধরণের টাইপ ব্যবহার করা হয়।}
    \begin{itemize}
        \item 1, 2, 3 (By default)
        \item i, ii, iii
        \item I, II, III
        \item A, B, C
        \item a, b, c
    \end{itemize}
\end{itemize}

\begin{center}
\begin{tabular}{|c|c|}
\hline
\B{Ol list type} & \B{ব্রাউজারে প্রদর্শন} \\ \hline
type="1" & 1 \\ \hline
type="i" & i \\ \hline
type="I" & I \\ \hline
type="a" & a \\ \hline
type="A" & A \\ \hline
\end{tabular}
\hfill
\begin{tabular}{p{0.48\linewidth} | p{0.48\linewidth}}
\hline
\centering\arraybackslash \B{কোড} & \centering\arraybackslash \B{ব্রাউজারে প্রদর্শন} \tabularnewline \hline
\begin{verbatim}
<ol type= "1" start = "51">
  <li>Salman</li>
  <li>Sabid</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item[51.] Salman
    \item[52.] Sabid
\end{enumerate} \\ \hline
\end{tabular}
\end{center}

\chsub{}{\B{নেস্টেড লিস্ট (Nested List)}}
\begin{center}
\begin{tabular}{p{0.48\linewidth} | p{0.48\linewidth}}
\hline
\centering\arraybackslash \B{কোড} & \centering\arraybackslash \B{ব্রাউজারে প্রদর্শন} \tabularnewline \hline
\begin{verbatim}
<ol>
  <li>Flower</li>
  <li>Fruit</li>
  <ol type= "1" start = "i">
    <li>Mango</li>
    <li>Orange</li>
  </ol>
  <li>Drink</li>
</ol>
\end{verbatim} & 
\begin{enumerate}
    \item Flower
    \item Fruit
    \begin{enumerate}
        \item[i.] Mango
        \item[ii.] Orange
    \end{enumerate}
    \item Drink
\end{enumerate} \\ \hline
\end{tabular}
\hfill
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{3}{|c|}{\B{Roman Number}} \\ \hline
I & = & 1 \\ \hline
V & = & 5 \\ \hline
X & = & 10 \\ \hline
L & = & 50 \\ \hline
C & = & 100 \\ \hline
D & = & 500 \\ \hline
M & = & 1000 \\ \hline
\end{tabular}
\end{center}

\chsub{}{\B{ওয়েব পেইজে চিত্র (Image) সংযোজন}}
\B{ওয়েবপেইজে ইমেজ সংযোজনের জন্য <img> বা <image> ট্যাগ ব্যবহৃত হয়। ইমেজের জন্য তিনটি ফরম্যাট বা টাইপ (.jpg, .png, .gif) ব্যবহার করা হয়। ইমেজ ব্যবহারের সিনট্যাক্স হলো: <img src = "ছবির লোকেশন\ ছবির নাম .ছবির টাইপ"/>}

\vspace{0.3cm}
\begin{center}
\B{Image src= C:\textbackslash Users\textbackslash User\textbackslash Desktop\textbackslash and .png"/>} \\[0.1cm]
\begin{tikzpicture}[scale=0.85]
    \draw[thick] (0,0) -- (0,-0.3) -- (4.2,-0.3) -- (4.2,0);
    \node at (2.1,-0.6) {\scriptsize Location};
    
    \draw[thick] (4.5,0) -- (4.5,-0.3) -- (5.3,-0.3) -- (5.3,0);
    \node at (4.9,-0.6) {\scriptsize Name};
    
    \draw[thick] (5.6,0) -- (5.6,-0.3) -- (6.6,-0.3) -- (6.6,0);
    \node at (6.1,-0.6) {\scriptsize Type};
\end{tikzpicture}
\end{center}

\vspace{0.5cm}

\B{ইমেজের ক্ষেত্রে ৫টি অ্যাট্রিবিউট ব্যবহৃত হয়। যেমন:}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|c|l|}
\hline
\textbf{নং} & \textbf{অ্যাট্রিবিউট} & \multicolumn{1}{c|}{\textbf{বর্ণনা}} \\ \hline
১ & src & প্রদর্শিত চিত্রের সোর্স বা URL বোঝায়। \\ \hline
২ & height & চিত্রের দৈর্ঘ্যের পরিমাপ কিরূপ হবে তা নির্ধারণে ব্যবহৃত হয়। \\ \hline
৩ & align & চিত্রের Alignment বা দিকবিন্যাস নির্ধারণে ব্যবহৃত হয়। \\ \hline
৪ & width & চিত্রের প্রস্থের পরিমাপ কিরূপ তা নির্ধারণে ব্যবহৃত হয়। \\ \hline
৫ & border & প্রদর্শিত চিত্রের চতুর্দিকের বর্ডারের তীক্ষ্ণতা নিয়ন্ত্রণ করতে ব্যবহৃত হয়। \\ \hline
\end{tabular}
\end{adjustbox}
\end{center}

\chsub{}{\B{পেইজ লিংক (Page Link)}}
\begin{itemize}
    \item \B{<a> এংকর ট্যাগ}
\end{itemize}

\vspace{0.2cm}
\begin{center}
\B{<a href = "shafin.html"> Shafin </a>} \\[0.1cm]
\begin{tikzpicture}[scale=0.85]
    \draw[thick] (0,0) -- (0,-0.3) -- (1.6,-0.3) -- (1.6,0);
    \node at (0.8,-0.6) {\scriptsize hyper reference};
    
    \draw[thick] (2.0,0) -- (2.0,-0.3) -- (3.6,-0.3) -- (3.6,0);
    \node at (2.8,-0.6) {\scriptsize page name};
    
    \draw[thick] (4.0,0) -- (4.0,-0.3) -- (5.2,-0.3) -- (5.2,0);
    \node at (4.6,-0.6) {\scriptsize link name};
\end{tikzpicture}
\end{center}

\chsub{}{\B{টেবিল (Table)}}
\begin{itemize}
    \item \B{সারিকে আমরা <tr> টেবিল রো বলি।}
    \item \B{টেবিলে এক একটি সেলগুলোকে <td> টেবিল ডেটা বলি।}
    \item \B{টেবিলে হেডারকে <th> টেবিল হেডার বলি।}
    \item \B{একাধিক কলাম একত্রে করার জন্য rowspan = "1/2/3" ব্যবহৃত হয়।}
    \item \B{একাধিক রো একত্রে করার জন্য rowspan = "1/2/3" ব্যবহৃত হয়।}
    \item \B{টেবিলে খালিঘর প্রদর্শনের জন্য \&nbsp; ব্যবহৃত হবে। (non breaking space) <td>\&nbsp;</td>}
    \item \B{<td> এর ২টি অ্যাট্রিবিউট। যেমন:}
    \begin{enumerate}
        \item[i.] \B{rowspan: যখন কোনো সেল একের অধিক রো জুড়ে থাকে।}
        \item[ii.] \B{colspan: 当ন কোনো সেল একের অধিক কলাম জুড়ে থাকে।}
    \end{enumerate}
\end{itemize}

\vspace{0.5cm}

\begin{enumerate}
    \item[৫.] \B{আকারে ছোট, ওজন অত্যন্ত কম এবং সহজে পরিবহনযোগ্য।}
    \item[৬.] \B{শক্তির ক্ষয় কম।}
    \item[৭.] \B{ডেটা সংরক্ষণের নিরাপত্তা ও গোপনীয়তা বেশি।}
    \item[৮.] \B{রিপিটারসমূহ অনেক দূরে দূরে স্থাপন করতে হয় না।}
\end{enumerate}

\chsub{}{\B{ফাইবার এর অসুবিধাসমূহ:}}
\begin{enumerate}
    \item \B{ফাইবার অপটিক কেবল ইনস্টল করা বেশ কঠিন।}
    \item \B{একে প্রয়োজনমতো বাঁকানো যায় না বলে ইনস্টলেশন বেশ কঠিন হয়ে পড়ে।}
    \item \B{ফাইবার অপটিক কেবলকে সহজে স্লাইস বা টুকরো করা যায় না। এর স্লাইসিং-এর জন্য দরকার পড়ে ইলেকট্রিক ফিউশন কিংবা কেমিক্যাল ইপোক্সি।}
    \item \B{অন্যান্য ক্যাবলের চেয়ে দাম খুবই বেশি।}
    \item \B{অপটিক্যাল ফাইবার স্থাপন ও রক্ষণাবেক্ষণ করার জন্য দক্ষ ও কারিগরি জ্ঞানসম্পন্ন জনবল প্রয়োজন।}
\end{enumerate}

\B{ফাইবার অপটিক ক্যাবলের প্রকারভেদ: ফাইবারের গাঠনিক উপাদানের প্রতিসরাংকের ওপর ভিত্তি করে ফাইবারকে দুভাগে ভাগ করা হয়।}

\B{\iub{স্টেপ ইনডেক্স ফাইবার (Step-index fiber):} স্টেপ ইনডেক্স ফাইবারের কোরের প্রতিসরাংক সর্বত্র সমান থাকে।}

\B{\iub{গ্রেডেড-ইনডেক্স ফাইবার (Graded-index fiber):} গ্রেডেড ইনডেক্স ফাইবারের কোরের প্রতিসরাংক কেন্দ্রে সবচেয়ে বেশি এবং এর ব্যাসার্ধ বরাবর কমতে থাকে। কোরের প্রতিসরাংকের ভিন্নতার কারণে এ দু ধরনের ফাইবারের আলোক রশ্মির গতিপথও ভিন্ন হয়।}

\B{কোরের ব্যাস অনুযায়ী ফাইবার অপটিককে আবার দুভাগে ভাগ করা যায়। যথা-} \\
\B{\textcolor{red}{সিঙ্গেলমোড ফাইবার (Singlemode fiber):} কোর সাইজ ৮/১২৫ মাইক্রন। সিঙ্গেল-মোড ফাইবার অপটিক ক্যাবলে একসাথে কেবল একটি আলোক সংকেত প্রেরণের পথ থাকে এবং সাধারণত লেজার সিগনালিং এর জন্য ব্যবহৃত হয়। সিঙ্গেল মোড ফাইবার অপটিক ক্যাবল ব্যবহার করা হয় দীর্ঘ দূরত্ব অতিক্রম করার জন্য।} \\
\B{\textcolor{red}{মাল্টিমোড ফাইবার (Multimode fiber):} কোর সাইজ ৬২.৫/১২৫ মাইক্রন। এটি সবচেয়ে বেশি ব্যবহৃত এবং নেটওয়ার্ক অ্যাপ্লিকেশনের উপযোগী। মাল্টিমোড ফাইবারে একই সাথে একাধিক আলোক সংকেত প্রেরণের পথ থাকে এবং এসব পথ দিয়ে সবকটি সিগনাল একই সাথে গন্তব্যে পৌঁছতে পারে।}

\vspace{0.4cm}
\begin{center}
\B{একনজরে বিভিন্ন প্রকার তার (গাইডেড) মাধ্যম} \\[0.2cm]
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|c|c|p{3.5cm}|p{3.5cm}|}
\hline
\textbf{মিডিয়া টাইপ} & \textbf{\begin{tabular}[c]{@{}c@{}}সর্বোচ্চ\\ সেগমেন্ট\\ দৈর্ঘ্য/\\ কভারেজ\end{tabular}} & \textbf{ব্যান্ড উইডথ} & \multicolumn{1}{c|}{\textbf{সুবিধা}} & \multicolumn{1}{c|}{\textbf{অসুবিধা}} \\ \hline
\begin{tabular}[c]{@{}c@{}}থিকনেট কো-\\ এক্সিয়াল ক্যাবল\end{tabular} & ৫০০ মিটার & 10 Mbps & অন্যান্য কপার ক্যাবলের চেয়ে বেশি ইএমআই প্রতিরোধ ক্ষমতা। & ব্যয়বহুল, সহজে ইনস্টল করা যায় না। \\ \hline
\begin{tabular}[c]{@{}c@{}}থিননেট কো-\\ এক্সিয়াল ক্যাবল\end{tabular} & ১৮৫ মিটার & 10 Mbps & থিকনেট ও ফাইবার অপটিকের চেয়ে কমদামী, সহজে স্থাপনযোগ্য। & ব্যান্ডউইডথ সীমিত, সবক্ষেত্রে ব্যবহার করা যায় না। \\ \hline
এসটিপি & ১০০ মিটার & 10 Mbps & ক্রসটক কম হয়, থিননেট ও ইউটিপির চেয়ে বেশি ইএমআই প্রতিরোধী। & ব্যয়বহুল, স্থাপন করা কঠিন। \\ \hline
ইউটিপি & ১০০ মিটার & 10 Mbps & সবচেয়ে কমদামী। & সীমিত ব্যান্ডউইডথ, খারাপ সিগনাল, ভয়েস সিগনালের জন্য। \\ \hline
\begin{tabular}[c]{@{}c@{}}সিঙ্গেল মোড\\ ফাইবার\end{tabular} & ৩ কি.মি. & \begin{tabular}[c]{@{}c@{}}100 Mbps -\\ 100 Gbps\end{tabular} & উচ্চগতি, বেশি নিরাপত্তা, ইএমআই প্রতিরোধী। & ব্যয়বহুল, স্থাপন করা কঠিন, কেবল একটি সিগনাল একসাথে ট্রান্সমিট করা যায়। \\ \hline
\begin{tabular}[c]{@{}c@{}}মাল্টিমোড\\ ফাইবার\end{tabular} & ২ কি.মি. & \begin{tabular}[c]{@{}c@{}}100 Mbps -\\ 9.92 Gbps\end{tabular} & উচ্চগতি, একসাথে একাধিক সিগনাল ট্রান্সমিট করতে পারে, নিরাপদ ও ইএমআই প্রতিরোধী। & ব্যয়বহুল, স্থাপন করতে অসুবিধা জনক এবং ক্রোমাটিড ডিসপারশনের শিকার। \\ \hline
\end{tabular}
\end{adjustbox}
\end{center}

\vspace{0.5cm}

\chsub{}{\B{মেশিন ভাষার অসুবিধা}}
\begin{enumerate}
    \item \B{মেশিন ভাষায় প্রোগ্রাম লেখা প্রোগ্রামারদের জন্য কষ্টকর ও সময় সাপেক্ষ।}
    \item \B{মেশিন ভাষায় প্রোগ্রাম লেখার জন্য নির্দেশ তালিকার সাহায্য নিতে হয়।}
    \item \B{কম্পিউটারের অভ্যন্তরীণ গঠন জানা না থাকলে এ ভাষায় প্রোগ্রাম রচনা করা যায় না।}
    \item \B{এ ভাষা মেশিন নির্ভর তাই এক কম্পিউটারের জন্য লেখা প্রোগ্রাম শুধুমাত্র ঐ কম্পিউটারেই চলবে অন্য কম্পিউটারে চালানো যাবে না।}
    \item \B{মেশিন ভাষায় প্রোগ্রাম লিখতে দক্ষ প্রোগ্রামারের দরকার হয়।}
    \item \B{মেশিন ভাষায় লেখা প্রোগ্রাম পরিবর্তন করা কষ্টসাধ্য।}
\end{enumerate}

\chsub{}{\B{অ্যাসেম্বলি ভাষা (Assembly Language)}}
\B{বিভিন্ন সাংকেতিক কোড ব্যবহার করে যে ভাষায় প্রোগ্রাম রচনা করা হয় তাকে অ্যাসেম্বলি ভাষা বলা হয়।}
\begin{itemize}
    \item \B{একে নেমোনিক কোডও বলা হয়।}
    \item \B{এটি ২য় প্রজন্মের ভাষা।}
    \item \B{অ্যাসেম্বলি ভাষাকে আবার মধ্যস্তরের ভাষাও বলা হয়।}
\end{itemize}

\chsub{}{\B{অ্যাসেম্বলি ভাষার সুবিধা}}
\begin{enumerate}
    \item \B{মেশিন ভাষার চেয়ে সহজ}
    \item \B{ভুল নির্ণয় করা এবং সংশোধন করা সহজ।}
    \item \B{মেশিন নির্ভর নয় অর্থাৎ যেকোনো কম্পিউটারে কাজ করে।}
\end{enumerate}

\chsub{}{\B{অ্যাসেম্বলি ভাষার অসুবিধা}}
\begin{enumerate}
    \item \B{এই ভাষার প্রোগ্রাম কম্পিউটার সরাসরি বুঝতে পারে না।}
    \item \B{এই ভাষার প্রোগ্রামকে মেশিনের ভাষায় রূপান্তরের জন্য অনুবাদক প্রোগ্রামের প্রয়োজন হয়।}
    \item \B{উচ্চস্তরের ভাষার চেয়ে কঠিন।}
\end{enumerate}

\chsub{}{\B{উচ্চস্তরের ভাষা (High Level Language)}}
\B{মানুষের ব্যবহৃত ভাষার শব্দাবলী ব্যবহার করে যে সকল ভাষায় প্রোগ্রাম রচনা করা যায়, তাকে উচ্চস্তরের ভাষা বা হাই লেভেল ভাষা বলা হয়। উচ্চস্তরের ভাষায় ইংরেজি শব্দ ব্যবহার করে প্রোগ্রাম রচনা করা হয়। উচ্চস্তরের ভাষায় লিখিত প্রোগ্রাম কম্পিউটার সরাসরি বুঝতে পারে না। তাই এ সকল ভাষার প্রোগ্রামকে মেশিনের ভাষায় রূপান্তরের প্রয়োজন হয়।}

\B{কয়েকটি উচ্চস্তরের প্রোগ্রামিং ভাষার নাম হলো:}
\begin{itemize}
    \item \B{বেসিক (BASIC - Beginner's All-Purpose Symbolic Instruction Code),}
    \item \B{ফোরট্রান (FORTRAN - Formula Translation),}
    \item \B{কোবল (COBOL - Common Business Oriented Language),}
    \item \B{অ্যালগল (Algol - Algorithmic Language),}
    \item \B{প্যাস্কেল (Pascal),}
    \item \B{সি (C), সি++ (C++)}
\end{itemize}

\chsub{}{\B{উচ্চস্তরের ভাষার সুবিধা}}
\begin{enumerate}
    \item \B{মানুষের ব্যবহৃত ভাষায় শব্দাবলী ব্যবহার করে প্রোগ্রাম রচনা করা যায় বলে উচ্চস্তর ভাষায় প্রোগ্রাম রচনা করা অনেক সহজ।}
    \item \B{এ ভাষায় প্রোগ্রাম রচনা করতে সময় কম লাগে।}
    \item \B{সহজে প্রোগ্রামের ত্রুটি সংশোধন ও পরিবর্তন করা যায়।}
    \item \B{এ ভাষায় প্রোগ্রাম সংক্ষিপ্ত আকারের হয়।}
    \item \B{এ ভাষা যন্ত্র নির্ভর নয় তাই এক কম্পিউটারের জন্য তৈরি প্রোগ্রাম অন্য কম্পিউটারে ব্যবহার করা যায়।}
\end{enumerate}

\vspace{0.5cm}
\begin{center}
2
\end{center}
\chsub{}{\B{উচ্চস্তরের ভাষার অসুবিধা}}
\begin{enumerate}
    \item \B{এ ভাষার প্রোগ্রাম কম্পিউটার সরাসরি বুঝতে পারে না।}
    \item \B{এ সকল ভাষার প্রোগ্রামকে মেশিনের ভাষায় রূপান্তরের জন্য অনুবাদক প্রোগ্রামের প্রয়োজন হয়।}
    \item \B{প্রোগ্রাম পরিচালনার জন্য কম্পিউটারে বেশি মেমোরির প্রয়োজন হয়।}
\end{enumerate}

\chsub{}{\B{অনুবাদক প্রোগ্রাম}}
\B{যে সকল প্রোগ্রাম সোর্স কোডকে অবজেক্ট কোডে রূপান্তরিত করে তাকে অনুবাদক প্রোগ্রাম বলে।}

\chsub{}{\B{অনুবাদক প্রোগ্রামের প্রকারভেদ}}
\B{অনুবাদক প্রোগ্রাম সাধারণত তিন ধরণের হয়ে থাকে। যেমন:}
\begin{enumerate}
    \item[i.] \B{অ্যাসেম্বলার (Assembler)}
    \item[ii.] \B{কম্পাইলার (Compiler)}
    \item[iii.] \B{ইন্টারপ্রেটার}
\end{enumerate}
\B{আবার এমন অনুবাদক প্রোগ্রাম আছে যা এক ধরণের উচ্চস্তরের ভাষার প্রোগ্রামকে অন্য একটি উচ্চস্তরের ভাষায় অনুবাদ করতে পারে। এই ধরণের অনুবাদককে Language Converter বলা হয়। যেমন:}
\begin{itemize}
    \item \B{FORTRAN to Ada Translator}
    \item \B{Pascal to C Translator ইত্যাদি।}
\end{itemize}

\chsub{}{\B{অনুবাদক প্রোগ্রামের প্রয়োজনীয়তা}}
\B{কম্পিউটারের নিজস্ব ভাষা হলো মেশিন ভাষা। এ ভাষার প্রোগ্রাম কম্পিউটার সরাসরি বুঝতে পারে। কিন্তু অ্যাসেম্বলি ও উচ্চ স্তরের ভাষার প্রোগ্রাম কম্পিউটার সরাসরি বুঝতে পারে না। তাই অনুবাদক প্রোগ্রাম ব্যবহার করে অ্যাসেম্বলি ও উচ্চস্তরের ভাষার প্রোগ্রামকে মেশিন ভাষায় রূপান্তর করার প্রয়োজন হয়।}

\begin{center}
\begin{tikzpicture}[node distance=1.5cm, align=center]
    \node (source) [draw, thick, minimum width=2.5cm, minimum height=0.8cm] {\B{সোর্স কোড}};
    \node (trans) [draw, thick, right=1.5cm of source, minimum width=2.5cm, minimum height=0.8cm] {\B{অনুবাদক প্রোগ্রাম}};
    \node (obj) [draw, thick, right=1.5cm of trans, minimum width=2.5cm, minimum height=0.8cm] {\B{অবজেক্ট কোড}};
    
    \draw[->, thick] (source) -- (trans);
    \draw[->, thick] (trans) -- (obj);
    
    \node[draw, ellipse, below=0.5cm of source, text width=3cm, font=\small] {\B{অ্যাসেম্বলি ভাষা ও উচ্চস্তরের ভাষায় লিখিত প্রোগ্রাম}};
    \node[draw, ellipse, below=0.5cm of obj, text width=3cm, font=\small] {\B{মেশিন ভাষায় লিখিত প্রোগ্রাম}};
    
    \draw[->, thick] (source) -- ++(0,-0.5) -| (obj);
\end{tikzpicture} \end{center}

\chsub{}{\B{অ্যাসেম্বলার (Assembler)}}
\B{অ্যাসেম্বলি ভাষার প্রোগ্রামকে মেশিন ভাষার প্রোগ্রামে অনুবাদের জন্য যে অনুবাদক প্রোগ্রাম ব্যবহৃত তাকে অ্যাসেম্বলার বলা হয়।}
\B{অ্যাসেম্বলারের প্রধান কাজ হলো:-}
\begin{itemize}
    \item \B{অ্যাসেম্বলি ভাষার প্রোগ্রাম বা নেমোনিক কোডকে অবজেক্ট প্রোগ্রামে রূপান্তরিত হয়।}
    \item \B{প্রোগ্রামের নির্দেশ পরীক্ষা করা ও ভুল শনাক্ত করা।}
    \item \B{নির্দেশ ও ডেটা মেমোরিতে সংরক্ষণ করা।}
\end{itemize}

\begin{center}
\begin{tikzpicture}[node distance=1cm, align=center]
    \node (asm) [draw, thick, minimum width=3cm, minimum height=0.8cm] {\B{অ্যাসেম্বলি ভাষার প্রোগ্রাম \\ বা নেমোনিক কোড}};
    \node (assembler) [draw, thick, right=1cm of asm, minimum width=2.5cm, minimum height=0.8cm] {\B{অ্যাসেম্বলার}};
    \node (obj) [draw, thick, right=1cm of assembler, minimum width=3cm, minimum height=0.8cm] {\B{মেশিন ভাষার প্রোগ্রাম বা \\ অবজেক্ট কোড}};
    
    \draw[->, thick] (asm) -- (assembler);
    \draw[->, thick] (assembler) -- (obj);
\end{tikzpicture}
\end{center}

\chsub{}{\B{কম্পাইলার}}
\B{কম্পাইলার একটি অনুবাদক প্রোগ্রাম। এটি উচ্চস্তরের ভাষার প্রোগ্রামকে মেশিন ভাষায় রূপান্তর করে।}
\begin{itemize}
    \item \B{কম্পাইলার সম্পূর্ণ প্রোগ্রামকে একসাথে অনুবাদ করে।}
    \item \B{বর্তমানে সকল উচ্চস্তরের প্রোগ্রামের ভাষায় কম্পাইলার ব্যবহৃত হয়।}
\end{itemize}

\vspace{0.5cm}
\begin{center}
3
\end{center}
\begin{center}
\begin{tikzpicture}[node distance=1cm, align=center]
    \node (source) [draw, thick, minimum width=3cm, minimum height=0.8cm] {\B{উচ্চতর ভাষার প্রোগ্রাম বা \\ উৎস প্রোগ্রাম}};
    \node (comp) [draw, thick, right=1cm of source, minimum width=2.5cm, minimum height=0.8cm] {\B{কম্পাইলার}};
    \node (obj) [draw, thick, right=1cm of comp, minimum width=3cm, minimum height=0.8cm] {\B{মেশিন ভাষার প্রোগ্রাম বা \\ অবজেক্ট কোড}};
    
    \draw[->, thick] (source) -- (comp);
    \draw[->, thick] (comp) -- (obj);
\end{tikzpicture}
\end{center}

\chsub{}{\B{কম্পাইলারের বৈশিষ্ট্য}}
\begin{itemize}
    \item \B{কম্পাইলার সম্পূর্ণ প্রোগ্রামকে একসাথে অনুবাদ করে।}
    \item \B{অনুবাদকৃত প্রোগ্রাম একসাথে মেমোরিতে সংরক্ষণ করে।}
    \item \B{কম্পাইলার প্রোগ্রাম নির্বাহের জন্য ইন্টারপ্রেটার অপেক্ষা কম সময় লাগে।}
    \item \B{কম্পাইলার প্রোগ্রামের সকল ভুলের তালিকা একসাথে প্রকাশ করে।}
    \item \B{কম্পাইলারের সাহায্যে ডিবাগিংয়ে বেশি সময়ের প্রয়োজন হয়।}
    \item \B{একবার অনুবাদকৃত প্রোগ্রাম পরবর্তীতে অনুবাদ ছাড়াই ব্যবহার করা যায়।}
\end{itemize}

\chsub{}{\B{ইন্টারপ্রেটার (Interpreter)}}
\B{ইন্টারপ্রেটার হলো একটি অনুবাদক প্রোগ্রাম। এটি উচ্চস্তরের ভাষায় লিখিত প্রোগ্রামকে মেশিন ভাষায় রূপান্তরিত করে।}
\begin{itemize}
    \item \B{ইন্টারপ্রেটার সম্পূর্ণ প্রোগ্রামকে একসাথে অনুবাদ না করে এক লাইন করে অনুবাদ করে।}
\end{itemize}

\begin{center}
\begin{tikzpicture}[node distance=1cm, align=center]
    \node (source) [draw, thick, minimum width=3cm, minimum height=0.8cm] {\B{উচ্চতর ভাষার প্রোগ্রাম বা \\ উৎস প্রোগ্রাম}};
    \node (inter) [draw, thick, right=1cm of source, minimum width=2.5cm, minimum height=0.8cm] {\B{ইন্টারপ্রেটার}};
    \node (obj) [draw, thick, right=1cm of inter, minimum width=3cm, minimum height=0.8cm] {\B{মেশিন ভাষার প্রোগ্রাম বা \\ অবজেক্ট কোড}};
    
    \draw[->, thick] (source) -- (inter);
    \draw[->, thick] (inter) -- (obj);
\end{tikzpicture}
\end{center}

\chsub{}{\B{ইন্টারপ্রেটার ও কম্পাইলারের পার্থক্য}}
\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|p{5cm}|c|p{5cm}|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{কম্পাইলার}} & \textbf{নং} & \multicolumn{1}{c|}{\textbf{ইন্টারপ্রেটার}} \\ \hline
১ & কম্পাইলার সম্পূর্ণ প্রোগ্রামকে একসাথে মেশিন ভাষায় অনুবাদ করে। & ১ & ইন্টারপ্রেটার প্রোগ্রামের একটি করে লাইন মেশিন ভাষায় অনুবাদ করে। \\ \hline
২ & অনুবাদকৃত প্রোগ্রাম একসাথে মেমোরিতে সংরক্ষিত হয়। & ২ & অনুবাদকৃত প্রোগ্রামের প্রতিটি লাইন আলাদাভাবে মেমোরিতে সংরক্ষণ করে। \\ \hline
৩ & প্রোগ্রাম নির্বাহের জন্য ইন্টারপ্রেটার অপেক্ষা কম সময়ের প্রয়োজন হয়। & ৩ & প্রোগ্রাম নির্বাহের জন্য কম্পাইলার অপেক্ষা বেশি সময়ের প্রয়োজন হয়। \\ \hline
৪ & কম্পাইলার সকল ভুলের তালিকা একসাথে প্রকাশ করে এবং ভুল সংশোধনের পর সম্পূর্ণ প্রোগ্রামকে মেশিন ভাষায় রূপান্তর করে। & ৪ & প্রতিটি লাইনের ভুল পৃথকভাবে প্রকাশ করে। \\ \hline
\end{tabular}
\end{adjustbox}
\end{center}

\chsub{}{\B{প্রোগ্রাম তৈরির ধাপ}}
\B{একটি পূর্ণাঙ্গ প্রোগ্রাম রচনার জন্য বেশ কতগুলি ধাপ পর্যায়ক্রমে অনুসরণ করতে হয়। প্রোগ্রাম তৈরির জন্য অনুসরণীয় পর্যায়ক্রমিক ধাপগুলো হলো:}

\begin{minipage}{0.65\linewidth}
\begin{itemize}
    \item \B{প্রোগ্রাম ডিজাইন}
    \begin{enumerate}
        \item \B{অ্যালগরিদম}
        \item \B{ফ্লোচার্ট}
        \item \B{প্রোগ্রাম কোডিং}
    \end{enumerate}
    \item \B{অ্যালগরিদম (Algorithm)} \\
    \B{অ্যালগরিদম শব্দের অর্থ হলো ধাপে ধাপে সমস্যা সমাধান করা। কোন প্রোগ্রামিং সমস্যার সমাধানের জন্য কতগুলি যৌক্তিক ও ধারাবাহিক ধাপ অনুসরণ করতে হয়। এই ধাপগুলোর লিখিত বর্ণনাকে অ্যালগরিদম বলে।}
    \begin{itemize}
        \item \B{অ্যালগরিদম শব্দটি এসেছে আরবীয় গণিতবিদ মুসা আল খরিজমি এর নাম থেকে।}
    \end{itemize}
\end{itemize}
\end{minipage}
\hfill
\begin{minipage}{0.3\linewidth}
\begin{center}
\begin{tikzpicture}[node distance=0.5cm, align=center]
    \node (s1) [draw, thick, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize সমস্যা নির্ধারণ};
    \node (s2) [draw, thick, below=of s1, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize সমস্যা বিশ্লেষণ};
    \node (s3) [draw, thick, below=of s2, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize প্রোগ্রাম ডিজাইন};
    \node (s4) [draw, thick, below=of s3, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize প্রোগ্রাম কোডিং};
    \node (s5) [draw, thick, below=of s4, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize প্রোগ্রাম বাস্তবায়ন};
    \node (s6) [draw, thick, below=of s5, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize প্রোগ্রাম ডকুমেন্টেশন};
    \node (s7) [draw, thick, below=of s6, minimum width=2.5cm, minimum height=0.6cm] {\scriptsize প্রোগ্রাম রক্ষণাবেক্ষণ};
    
    \draw[->, thick] (s1) -- (s2);
    \draw[->, thick] (s2) -- (s3);
    \draw[->, thick] (s3) -- (s4);
    \draw[->, thick] (s4) -- (s5);
    \draw[->, thick] (s5) -- (s6);
    \draw[->, thick] (s6) -- (s7);
\end{tikzpicture}
\end{center}
\end{minipage}

\vspace{0.5cm}
\begin{center}
4
\end{center}
\chsub{}{\B{ফ্লোচার্ট (Flow Chart)}}
\B{কোন একটি প্রোগ্রাম কীভাবে কাজ করবে তা চিত্রের মাধ্যমে প্রকাশ করাই হলো ফ্লোচার্ট। অ্যালগরিদমের চিত্রভিত্তিক উপস্থাপনাকে ফ্লোচার্ট বলে। ফ্লোচার্টে কোনো প্রোগ্রামের কার্যাবলী বিশেষ কিছু চিত্রের মাধ্যমে তুলে ধরা হয়।}

\B{ফ্লোচার্ট ২ প্রকার। যথা:-}
\begin{enumerate}
    \item \B{প্রোগ্রাম ফ্লোচার্ট:} \B{প্রোগ্রামের কাজ কীভাবে অগ্রসর হবে তা দেখানো হয়।}
    \item \B{সিস্টেম ফ্লোচার্ট:} \B{একটি সিস্টেমের বিভিন্ন উপাদান ও এর পরিবর্তনগুলো তুলে ধরা হয়।}
\end{enumerate}

\chsub{}{\B{প্রোগ্রাম ফ্লোচার্টে ব্যবহৃত গুরুত্বপূর্ণ চিত্রসমূহ}}

\begin{center}
\begin{adjustbox}{max width=\linewidth}
\begin{tabular}{|c|c|p{7cm}|}
\hline
\textbf{চিত্রের নাম} & \textbf{প্রতীক} & \multicolumn{1}{c|}{\textbf{ব্যবহার}} \\ \hline
\begin{tabular}[c]{@{}c@{}}প্রান্তিক চিহ্ন\\ (Terminator)\end{tabular} & \ovalnode{oval}{ } & \B{উপবৃত্তাকার চিহ্ন: প্রোগ্রামের শুরু ও শেষ বুঝতে এই চিহ্নটি ব্যবহার করা হয়।} \\ \hline
\begin{tabular}[c]{@{}c@{}}ইনপুট/আউটপুট\\ চিহ্ন (I/O)\end{tabular} & \parallelogramnode{para}{ } & \B{সামান্তরিক চিহ্ন: প্রোগ্রামে ডেটা ইনপুট এবং প্রোগ্রামের ফলাফল (আউটপুট) প্রদর্শনের ক্ষেত্রে এ চিহ্নটি ব্যবহার করা হয়।} \\ \hline
\begin{tabular}[c]{@{}c@{}}প্রক্রিয়াকরণ চিহ্ন\\ (Process)\end{tabular} & \rectanglenode{rect}{ } & \B{আয়তাকার চিহ্ন: ডেটা প্রক্রিয়াকরণ এবং কোনো চলকের প্রাথমিক মান নির্ধারণের জন্য এ চিহ্নটি ব্যবহার করা হয়।} \\ \hline
\begin{tabular}[c]{@{}c@{}}সিদ্ধান্ত\\ (Decision)\end{tabular} & \diamondnode{diam}{ } & \B{রম্বসাকৃতির চিহ্ন: যুক্তিমুলক বা সিদ্ধান্তমুলক কাজের ক্ষেত্রে বা দুটি রাশির মানের তুলনা করার জন্য এ চিহ্নটি ব্যবহার করা হয়।} \\ \hline
\begin{tabular}[c]{@{}c@{}}সংযোজন\\ (Connector)\end{tabular} & \circlenode{circ}{ } & \B{বৃত্ত: প্রোগ্রামের উন্মুক্ত প্রান্ত বা শাখাকে সংযোজনের ক্ষেত্রে এটি ব্যবহার করা হয়।} \\ \hline
\begin{tabular}[c]{@{}c@{}}প্রবাহ রেখা\\ (Flow line)\end{tabular} & \rightarrownode{arr}{ } & \B{তীর: প্রোগ্রামের প্রবাহের দিক নির্দেশ করার জন্য ব্যবহার করা হয়।} \\ \hline
\end{tabular}
\end{adjustbox}
\end{center}

\vspace{0.5cm}

\end{multicols}

\end{document}
"""

import subprocess, os, shutil, urllib.request, hashlib, sys

def run(cmd):
    return subprocess.run(cmd, shell=True, executable="/bin/bash").returncode

os.makedirs("fonts", exist_ok=True)
os.makedirs("logs", exist_ok=True)

font_sources = {
    "NotoSerifBengali-Regular.ttf": [
        "https://github.com/google/fonts/raw/main/ofl/notoserifbengali/NotoSerifBengali%5Bwdth%2Cwght%5D.ttf",
        "https://github.com/googlefonts/noto-fonts/raw/main/unhinted/slim-variable-ttf/NotoSerifBengali%5Bwdth%2Cwght%5D.ttf",
    ],
    "NotoSerifBengali-Bold.ttf": [
        "https://github.com/google/fonts/raw/main/ofl/notoserifbengali/NotoSerifBengali%5Bwdth%2Cwght%5D.ttf",
        "https://github.com/googlefonts/noto-fonts/raw/main/unhinted/slim-variable-ttf/NotoSerifBengali%5Bwdth%2Cwght%5D.ttf",
    ],
}

def good_font(path):
    if not os.path.exists(path) or os.path.getsize(path) < 100000:
        return False
    with open(path, "rb") as fh:
        head = fh.read(4)
    return head in (b"\x00\x01\x00\x00", b"OTTO", b"ttcf", b"true")

for name, urls in font_sources.items():
    path = os.path.join("fonts", name)
    if good_font(path):
        continue
    if os.path.exists(path):
        os.remove(path)
    last_error = None
    for url in urls:
        try:
            print("downloading", name)
            urllib.request.urlretrieve(url, path)
            if good_font(path):
                break
        except Exception as exc:
            last_error = exc
    if not good_font(path):
        raise RuntimeError("font download failed: " + name + " " + str(last_error))

with open("logs/font_hashes.log", "w", encoding="utf-8") as fh:
    for name in sorted(font_sources):
        path = os.path.join("fonts", name)
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
        fh.write(name + "\t" + str(os.path.getsize(path)) + "\t" + digest + "\n")

tex_content = TEX.replace("\u200d", "")

with open("ict_fixed.tex", "w", encoding="utf-8") as fh:
    fh.write(tex_content)

if not shutil.which("xelatex") and shutil.which("apt-get"):
    run("apt-get update -qq --allow-unauthenticated >>logs/apt.log 2>&1; "
        "apt-get install -y --no-install-recommends texlive-xetex texlive-fonts-recommended "
        "texlive-latex-extra texlive-pictures texlive-lang-other texlive-latex-recommended "
        "lmodern fonts-freefont-otf fonts-dejavu >>logs/apt.log 2>&1")

run("fc-cache -f ./fonts >>logs/fontcache.log 2>&1")

if not shutil.which("xelatex"):
    raise RuntimeError("xelatex not found after setup")

passes = []
for i in range(1, 3):
    code = run("xelatex -halt-on-error -file-line-error -interaction=nonstopmode "
               "ict_fixed.tex >logs/xelatex_pass" + str(i) + ".log 2>&1")
    passes.append(code)
    if code != 0:
        raise RuntimeError("xelatex failed; see logs/xelatex_pass" + str(i) + ".log")

print("PDF ready:", os.path.exists("ict_fixed.pdf"), "passes:", passes)
