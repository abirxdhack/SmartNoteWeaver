TEX = r"""

\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{newunicodechar}
\usepackage[margin=1.0cm, top=1.5cm, bottom=1.5cm, headsep=6pt, footskip=22pt]{geometry}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{pifont}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{array}
\usepackage[hidelinks]{hyperref}
\usepackage[protrusion=false]{microtype}
\usepackage{balance}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{tikz}
\usepackage{ucharclasses}
\usepackage{needspace}


\definecolor{tkzA}{RGB}{198,40,40}
\definecolor{tkzB}{RGB}{25,118,210}
\definecolor{tkzC}{RGB}{46,125,50}
\definecolor{tkzD}{RGB}{123,31,162}
\definecolor{tkzE}{RGB}{230,81,0}
\definecolor{tkzF}{RGB}{2,119,189}
\definecolor{tkzG}{RGB}{136,14,79}
\definecolor{tkzH}{RGB}{51,105,30}
\tikzset{
  every path/.style={line join=round,line cap=round},
}
\usetikzlibrary{
  arrows.meta,
  calc,
  shadings,
  decorations.pathmorphing,
  3d,
  perspective
}

\setlength{\arrayrulewidth}{0.3pt}
\setlength{\tabcolsep}{1.5pt}
\renewcommand{\arraystretch}{1.13}

\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}


\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyhead[L]{\small\B{পদার্থবিজ্ঞান — সম্পূর্ণ সূত্র, সংজ্ঞা ও চিত্র}}
\fancyhead[R]{\small\textbf{By Abir Arafat Chawdhury [Mr. Introvert]}}
\fancyfoot[L]{\small\B{HSC পদার্থবিজ্ঞান রিভিশন}}
\fancyfoot[C]{\small\textbf{\thepage}}
\fancyfoot[R]{\small\textit{Mr. Introvert Notes}}
\setlength{\headheight}{16pt}
\setlength{\headsep}{6pt}
\setlength{\footskip}{18pt}


\setlength{\emergencystretch}{25pt}
\hbadness=10000
\vbadness=10000
\sloppy
\raggedcolumns
\tolerance=9999
\emergencystretch=25pt

\defaultfontfeatures{Ligatures=TeX}

\setmainfont{Latin Modern Roman}

\newfontfamily\lat[
  Ligatures=TeX
]{Latin Modern Roman}

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

\newunicodechar{°}{\ensuremath{^\circ}}
\newunicodechar{।}{{\bn ।}}

\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{85,85,85}
\definecolor{p1bg}{RGB}{20,60,120}
\definecolor{p2bg}{RGB}{0,0,0}

\newcommand{\B}[1]{{\bn #1}}
\setTransitionTo{Bengali}{\begingroup\bn}
\setTransitionFrom{Bengali}{\endgroup}
\newcommand{\LAT}[1]{{\lat #1}}

\newcommand{\srcnote}{%
\textsuperscript{{\lat\tiny BP}}%
}

\newcommand{\chsec}[1]{%
  \needspace{8\baselineskip}%
  \vspace{2pt}%
  \noindent
  \colorbox{sectionbg}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      \centering
      {\color{white}\B{\small\bfseries #1}}%
    }%
  }%
  \nopagebreak\vspace{1pt}\par\nopagebreak
}

\newcommand{\chsub}[2]{%
  \needspace{6\baselineskip}%
  \vspace{2pt}%
  \noindent
  \colorbox{subsecbg}{%
    \parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
      {\color{white}%
      \LAT{\bfseries\footnotesize #1}%
      \hspace{3pt}%
      \B{\bfseries\footnotesize #2}}%
    }%
  }%
  \nopagebreak\vspace{1pt}\par\nopagebreak
}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8pt}

\setlist[enumerate]{
  nosep,
  leftmargin=*,
  topsep=0pt
}

\setlist[itemize]{
  nosep,
  leftmargin=0pt,
  topsep=0pt,
  label={},
  itemsep=0pt,
  parsep=0pt
}

\newcommand{\itm}[1]{%
\par\noindent\textbf{{\lat #1.}}\;%
}

\newcommand{\sub}[1]{%
\textbf{({\lat #1})}%
}

\begin{document}

\begin{multicols}{2}

\noindent
\colorbox{p1bg}{%
\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
\centering
{\color{white}\B{\large\bfseries পদার্থবিজ্ঞান প্রথম পত্র}}
}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: ভৌত জগৎ ও পরিমাপ}

\chsub{}{বিভিন্ন ভৌত রাশির সংকেত, একক ও মাত্রা}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.184\linewidth}|>{\raggedright\arraybackslash}p{0.156\linewidth}|>{\raggedright\arraybackslash}p{0.092\linewidth}|>{\raggedright\arraybackslash}p{0.092\linewidth}|>{\raggedright\arraybackslash}p{0.11\linewidth}|>{\raggedright\arraybackslash}p{0.138\linewidth}|}
\hline
\rowcolor{tblhdr} \B{নাম} & \B{ইংরেজি} & \B{সংকেত} & \B{SI একক} & \B{সংকেত} & \B{মাত্রা} \\
\hline
\B{দৈর্ঘ্য} & length & {\lat $l$} & \B{মিটার} & {\lat m} & {\lat $L$} \\
\hline
\B{ভর} & mass & {\lat $m$} & \B{কিলোগ্রাম} & {\lat kg} & {\lat $M$} \\
\hline
\B{সময়} & time & {\lat $t$} & \B{সেকেন্ড} & {\lat s} & {\lat $T$} \\
\hline
\B{সরণ} & displacement & {\lat $s$} & \B{মিটার} & {\lat m} & {\lat $L$} \\
\hline
\B{ক্ষেত্রফল} & area & {\lat $A$} & \B{মিটার\textsuperscript{2}} & {\lat m$^2$} & {\lat $L^2$} \\
\hline
\B{আয়তন} & volume & {\lat $V$} & \B{মিটার\textsuperscript{3}} & {\lat m$^3$} & {\lat $L^3$} \\
\hline
\B{বেগ/দ্রুতি} & velocity,speed & {\lat $v$} & \B{মি/সে} & {\lat ms$^{-1}$} & {\lat $LT^{-1}$} \\
\hline
\B{ত্বরণ} & acceleration & {\lat $a$} & \B{মি/সে\textsuperscript{2}} & {\lat ms$^{-2}$} & {\lat $LT^{-2}$} \\
\hline
\B{ভরবেগ} & momentum & {\lat $p$} & \B{কি.গ্রা.মি/সে} & {\lat kg.ms$^{-1}$} & {\lat $MLT^{-1}$} \\
\hline
\B{বল} & force & {\lat $F$} & \B{নিউটন} & {\lat N} & {\lat $MLT^{-2}$} \\
\hline
\B{কাজ} & work & {\lat $W$} & \B{জুল} & {\lat J} & {\lat $ML^2T^{-2}$} \\
\hline
\B{ক্ষমতা} & power & {\lat $P$} & \B{ওয়াট} & {\lat W} & {\lat $ML^2T^{-3}$} \\
\hline
\B{শক্তি} & energy & {\lat $E$} & \B{জুল} & {\lat J} & {\lat $ML^2T^{-2}$} \\
\hline
\B{ঘনত্ব} & density & {\lat $\rho$} & \B{কি.গ্রা/মি\textsuperscript{3}} & {\lat kgm$^{-3}$} & {\lat $ML^{-3}$} \\
\hline
\B{চাপ} & pressure & {\lat $p$} & \B{প্যাসকেল} & {\lat Pa} & {\lat $ML^{-1}T^{-2}$} \\
\hline
\B{দোলনকাল} & time period & {\lat $T$} & \B{সেকেন্ড} & {\lat s} & {\lat $T$} \\
\hline
\B{তরঙ্গদৈর্ঘ্য} & wave length & {\lat $\lambda$} & \B{মিটার} & {\lat m} & {\lat $L$} \\
\hline
\B{কম্পাঙ্ক} & frequency & {\lat $f$} & \B{হার্জ} & {\lat Hz} & {\lat $T^{-1}$} \\
\hline
\B{তাপমাত্রা} & temperature & {\lat $\theta,T$} & \B{কেলভিন} & {\lat K} & {\lat $\theta$} \\
\hline
\end{tabular}
\normalsize

\chsub{}{পদার্থবিজ্ঞানে ব্যবহৃত বিভিন্ন যন্ত্রের নাম ও ব্যবহার}

\noindent\textbf{\B{থার্মোমিটার:}} \B{উষ্ণতা মাপার জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{অ্যানিরয়েড ব্যারোমিটার:}} \B{বায়ুর কোনো একটি পরিবর্তী প্রভাব উৎপন্ন করতে ব্যবহৃত হয়।}\par
\noindent\textbf{\B{অ্যানিমোমিটার:}} \B{বায়ুমণ্ডলের চাপ বৃদ্ধি ও গ্যাসের পরিসরণের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{অ্যাক্টিনোমিটার:}} \B{বিদ্যুৎ-চুম্বকীয় তরঙ্গের তীব্রতা পরিমাপের কাজে ব্যবহৃত হয়।}\par
\noindent\textbf{\B{ট্যাকোমিটার:}} \B{উড়োজাহাজে, মোটর গাড়ির ইন্টার্নাল কম্বাশন ইঞ্জিনের আবর্তন গতির পরিমাপ।}\par
\noindent\textbf{\B{ডায়নামোমিটার:}} \B{বলের মান পরিমাপ করার জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{ভার্নিয়ার ক্যালিপার:}} \B{কোনো জিনিসের ক্ষুদ্র দৈর্ঘ্য নির্দেশ।}\par
\noindent\textbf{\B{ডায়ালেটোমিটার:}} \B{বস্তুর বেগ নির্ধারণে ব্যবহৃত হয়।}\par
\noindent\textbf{\B{সরল লোলক:}} \B{ব্যবহার্য: (i) অভিকর্ষীয় ত্বরণের মান নির্ণয় (ii) পাহাড়ের উচ্চতা নির্ণয় (iii) সময় নির্ধারণের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{সাইফন:}} \B{পানি বা অন্য কোনো তরল পদার্থকে না ঢেলে কিংবা নাড়াচাড়া না করে উচ্চ স্থানে অবস্থিত কোনো পাত্র হতে নিম্ন স্থানে অবস্থিত কোনো পাত্রে স্থানান্তরের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{নিরেক্স এর সাইফন:}} \B{কোনো শব্দের কম্পাঙ্ক অথবা বিভিন্ন শব্দের কম্পাঙ্ক তথা তীক্ষ্ণতা তুলনা করার জন্য এটি ব্যবহৃত হয়।}\par
\noindent\textbf{\B{পিসমোমিটার:}} \B{ভূমিকম্পের মাত্রা নির্ণয় করা হয়।}\par
\noindent\textbf{\B{সুর শলাকা:}} \B{শব্দ বিজ্ঞানের বিভিন্ন পরীক্ষায় সুর-শলাকা ব্যবহৃত হয়। এটির একটি বিশেষ ধর্ম হচ্ছে এটি একটি মাত্র কম্পাঙ্কবিশিষ্ট শব্দ সৃষ্টি করতে পারে।}\par
\noindent\textbf{\B{সোনোমিটার:}} \B{শব্দের কম্পাঙ্ক নির্ধারণের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্ক্রু-গজ:}} \B{ব্যবহার্য: (i) খুব ছোট দৈর্ঘ্য (ii) তারের ব্যাস (iii) পাতলা পাতের প্রকৃত অতি সূক্ষ্মভাবে মাপার জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্টপ-ওয়াচ:}} \B{পরীক্ষাগারে সময় নির্ধারণের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্পিডোমিটার:}} \B{দ্রুতি পরিমাপের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্পিরিট লেভেল:}} \B{তিতির: তরলের সমতলচক্রীলতার ধর্মের উপর ভিত্তি করে তৈরি; ব্যবহার্য: কোনো তল অনুভূমিক কিনা তা নির্ণয় করার জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্প্রিং নিক্তি:}} \B{সরাসরি ভার নির্ধারণের জন্য ব্যবহৃত।}\par
\noindent\textbf{\B{ফেরোমিটার:}} \B{পাতলা পাতের প্রকৃত পরিমাণের জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{স্লাইড ক্যালিপার:}} \B{ব্যবহার্য: (i) কোনো জিনিসের দৈর্ঘ্য (ii) গোলক বা সিলিন্ডারের ব্যাস (iii) ফাঁপা টিউবের ভিতরের ও বাইরের ব্যাস মাপার জন্য ব্যবহৃত হয়।}\par
\noindent\textbf{\B{হাইগ্রোমিটার:}} \B{আপেক্ষিক আর্দ্রতা নির্ণয়ের জন্য ব্যবহৃত হয়।}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{শতকরা ক্রটি:}} {\lat $= \dfrac{\text{\B{\text{\B{প্রকৃত মান}}}} - \text{\B{\text{\B{পরীক্ষালব্ধ মান}}}}}{\text{\B{\text{\B{প্রকৃত মান}}}}} \times 100\%$}

\itm{2} \textbf{\B{গড় মান:}} {\lat $A = \dfrac{x_1 + x_2 + x_3 + \cdots + x_n}{n}$}

\itm{3} \textbf{\B{গড় বিচ্যুতি বা গড় ভুল:}} {\lat $d = \dfrac{d_1 + d_2 + d_3 + \cdots + d_n}{n}$}

\itm{4} \textbf{\B{প্রমাণ বিচ্যুতি:}} {\lat $D = \dfrac{\sqrt{d_1^2 + d_2^2 + d_3^2 + \cdots + d_n^2}}{n} = \dfrac{\sqrt{\Sigma d^2}}{n}$}

\itm{5} \textbf{\B{ভার্নিয়ার ধ্রুবক ও পাঠ:}} {\lat $VC=\dfrac{s}{n}$;\; $L=M+VC\times V$}
\begin{itemize}
  \item[] \B{এখানে} {\lat $s$} = \B{প্রধান স্কেলের ক্ষুদ্রতম এক ঘর,} {\lat $n$} = \B{ভার্নিয়ার ভাগ সংখ্যা,} {\lat $M$} = \B{প্রধান স্কেল পাঠ,} {\lat $V$} = \B{ভার্নিয়ার স্কেল পাঠ।}
\end{itemize}

\itm{6} \textbf{\B{স্ক্রু-গজ:}} {\lat $LC=\dfrac{p}{n}$;\; $D=L+LC\times C$}
\begin{itemize}
  \item[] {\lat $p$} = \B{পিচ,} {\lat $n$} = \B{বৃত্তাকার স্কেলের ভাগ সংখ্যা,} {\lat $L$} = \B{রৈখিক স্কেল পাঠ,} {\lat $C$} = \B{বৃত্তাকার স্কেল পাঠ।}
\end{itemize}

\itm{7} \textbf{\B{ত্রুটি:}} {\lat $\Delta x=x-y$;\; $\dfrac{\Delta x}{x}=\dfrac{x-y}{x}$;\; $\%\,\text{error}=\dfrac{\Delta x}{x}\times100\%$}
\par\noindent{\lat $\bar{x}=\dfrac{\sum x}{n}$;\; $d_n=x_n-\bar{x}$;\; $d=\sqrt{\dfrac{\sum d^2}{n}}$;\; $\bar d=\dfrac{\sum |d|}{n}$}

\itm{8} \textbf{\B{আনুপাতিক ত্রুটি:}} {\lat $x=\dfrac{u^pv^q}{w^r}$} \B{হলে}
{\lat $\dfrac{\Delta x}{x}=p\dfrac{\Delta u}{u}+q\dfrac{\Delta v}{v}+r\dfrac{\Delta w}{w}$}

\itm{9} \textbf{\B{স্ফেরোমিটার:}} {\lat $R=\dfrac{d^2}{6h}+\dfrac{h}{2}$};\; {\lat $d$}=\B{তিন পায়ের গড় দূরত্ব,} {\lat $h$}=\B{উচ্চতা/নিম্নতা।}

\chsec{অধ্যায়-২: ভেক্টর}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{লব্ধির মান ও দিক (সামান্তরিক সূত্র):}} {\lat $R = \sqrt{P^2 + Q^2 + 2PQ\cos\alpha}$};\; \B{দিক:} {\lat $\tan\theta = \dfrac{Q\sin\alpha}{P + Q\cos\alpha}$};\; {\lat $\tan\beta = \dfrac{P\sin\alpha}{Q + P\cos\alpha}$}

\itm{2} \textbf{\B{ভেক্টর যোগের বিভিন্ন গাণিতিক নিয়মাবলী:}}
\begin{itemize}
    \item \B{বিনিময় সূত্র (Commutative Law):} {\lat $\vec{A} + \vec{B} = \vec{B} + \vec{A}$}
    \item \B{সংযোগ সূত্র (Associative Law):} {\lat $(\vec{A} + \vec{B}) + \vec{C} = \vec{A} + (\vec{B} + \vec{C})$}
    \item \B{বণ্টন সূত্র (Distributive Law):} {\lat $m(\vec{A} + \vec{B}) = m\vec{A} + m\vec{B}$}
\end{itemize}

\itm{3} \textbf{\B{ভেক্টর যোগের ত্রিভুজ ও বহুভুজ বিধি:}}
\begin{itemize}
    \item \B{ত্রিভুজ বিধি:} {\lat $\vec{R} = \vec{P} + \vec{Q}$}
    \item \B{বহুভুজ বিধি:} {\lat $\vec{R} = \vec{P} + \vec{Q} + \vec{S} + \vec{T} + \vec{U}$}
\end{itemize}

\itm{4} \textbf{\B{লব্ধির সর্বোচ্চ ও সর্বনিম্ন মান:}} {\lat $R_{\max} = P + Q$} \; [{\lat $\alpha = 0^\circ$} হলে];\; {\lat $R_{\min} = P \sim Q$} \; [{\lat $\alpha = 180^\circ$} হলে]

\itm{5} \textbf{\B{পরস্পর লম্ব ভেক্টরের ক্ষেত্রে লব্ধির বিশেষ সম্পর্ক:}} \B{যদি} {\lat $\alpha = 90^\circ$} \B{হয়, তবে} {\lat $2R_{\text{P}}^2 = R_{\max}^2 + R_{\min}^2$}

\itm{6} \textbf{\B{দুটি সমান মানের ভেক্টরের লব্ধি:}} \B{যদি} {\lat $P = Q$} \B{হয়, তবে লব্ধি} {\lat $R = 2P\cos\left(\dfrac{\alpha}{2}\right)$} \B{এবং লব্ধির দিক} {\lat $\theta = \dfrac{\alpha}{2}$}

\itm{7} \textbf{\B{দুটি ভেক্টরের বিয়োগ বা অন্তরফল:}} {\lat $\vec{R} = \vec{P} - \vec{Q} \implies R = \sqrt{P^2 + Q^2 - 2PQ\cos\alpha}$}

\itm{8} \textbf{\B{লম্বাংশ উপপাদ্য (Component Theorem):}} {\lat $R\cos\theta = P\cos\alpha + Q\cos\beta$};\; {\lat $R\sin\theta = P\sin\alpha + Q\sin\beta$}

\itm{9} \textbf{\B{ভেক্টরের সাইন সূত্র (Sine Rule):}} {\lat $\dfrac{P}{\sin\alpha} = \dfrac{Q}{\sin\beta} = \dfrac{R}{\sin(\alpha+\beta)}$}

\itm{10} \textbf{\B{ত্রিমাত্রিক কার্তেসীয় স্থানাঙ্ক ব্যবস্থায় ভেক্টর ও তার মান:}} {\lat $\vec{A} = A_x\hat{i} + A_y\hat{j} + A_z\hat{k}$};\; \B{মান:} {\lat $|\vec{A}| = A = \sqrt{A_x^2 + A_y^2 + A_z^2}$}

\itm{11} \textbf{\B{দিক বরাবর একক ভেক্টর:}} {\lat $\hat{a} = \dfrac{\vec{A}}{A} = \dfrac{A_x\hat{i} + A_y\hat{j} + A_z\hat{k}}{\sqrt{A_x^2 + A_y^2 + A_z^2}}$}

\itm{12} \textbf{\B{উপাংশ আকারে দুটি ভেক্টরের যোগফল:}} {\lat $\vec{A} + \vec{B} = (A_x + B_x)\hat{i} + (A_y + B_y)\hat{j} + (A_z + B_z)\hat{k}$}

\itm{13} \textbf{\B{স্কেলার বা ডট গুণফল:}} {\lat $\vec{A}\cdot\vec{B} = AB\cos\theta = A_x B_x + A_y B_y + A_z B_z$};\; \B{মধ্যবর্তী কোণ:} {\lat $\theta = \cos^{-1}\left(\dfrac{\vec{A}\cdot\vec{B}}{AB}\right)$}

\itm{14} \textbf{\B{আয়ত একক ভেক্টরের ডট গুণফল:}} {\lat $\hat{i}\cdot\hat{i} = \hat{j}\cdot\hat{j} = \hat{k}\cdot\hat{k} = 1$};\; {\lat $\hat{i}\cdot\hat{j} = \hat{j}\cdot\hat{k} = \hat{k}\cdot\hat{i} = 0$}

\itm{15} \textbf{\B{ভেক্টর বা ক্রস গুণফল:}} {\lat $\vec{A}\times\vec{B} = (AB\sin\theta)\hat{\eta}$};\; \B{মান:} {\lat $|\vec{A}\times\vec{B}| = AB\sin\theta = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k}\\ A_x & A_y & A_z\\ B_x & B_y & B_z\end{vmatrix}$}

\itm{16} \textbf{\B{আয়ত একক ভেক্টরের ক্রস গুণফল:}} {\lat $\hat{i}\times\hat{i} = \hat{j}\times\hat{j} = \hat{k}\times\hat{k} = \vec{0}$}
\par\noindent{\lat $\hat{i}\times\hat{j} = \hat{k};\; \hat{j}\times\hat{k} = \hat{i};\; \hat{k}\times\hat{i} = \hat{j}$};\; {\lat $\hat{j}\times\hat{i} = -\hat{k};\; \hat{k}\times\hat{j} = -\hat{i};\; \hat{i}\times\hat{k} = -\hat{j}$}

\itm{17} \textbf{\B{লম্ব অভিক্ষেপ (Scalar Projection):}}
\begin{itemize}
    \item \B{$\vec{A}$-এর উপর $\vec{B}$-এর লম্ব অভিক্ষেপ:} {\lat $B\cos\theta = \dfrac{\vec{A}\cdot\vec{B}}{A}$}
    \item \B{$\vec{B}$-এর উপর $\vec{A}$-এর লম্ব অভিক্ষেপ:} {\lat $A\cos\theta = \dfrac{\vec{A}\cdot\vec{B}}{B}$}
\end{itemize}

\itm{18} \textbf{\B{উপাংশ বা অংশক (Vector Projection):}}
\begin{itemize}
    \item \B{$\vec{A}$-এর উপর $\vec{B}$-এর উপাংশ:} {\lat $(B\cos\theta)\hat{a} = \left(\dfrac{\vec{A}\cdot\vec{B}}{A}\right)\times\dfrac{\vec{A}}{A} = \dfrac{(\vec{A}\cdot\vec{B})\vec{A}}{A^2}$}
    \item \B{$\vec{B}$-এর উপর $\vec{A}$-এর উপাংশ:} {\lat $(A\cos\theta)\hat{b} = \left(\dfrac{\vec{A}\cdot\vec{B}}{B}\right)\times\dfrac{\vec{B}}{B} = \dfrac{(\vec{A}\cdot\vec{B})\vec{B}}{B^2}$}
\end{itemize}

\itm{19} \textbf{\B{ভেক্টরের দিক কোসাইন (Direction Cosines):}} {\lat $\cos\alpha = \dfrac{A_x}{A}$};\; {\lat $\cos\beta = \dfrac{A_y}{A}$};\; {\lat $\cos\gamma = \dfrac{A_z}{A}$}
\par\noindent\B{দিক কোসাইনের সম্পর্কসমূহ:} {\lat $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$};\; {\lat $\sin^2\alpha + \sin^2\beta + \sin^2\gamma = 2$}

\itm{20} \textbf{\B{ভেক্টরদ্বয় পরস্পর লম্ব বা সমান্তরাল হওয়ার শর্ত:}}
\begin{itemize}
    \item \B{পরস্পর লম্ব হওয়ার শর্ত:} {\lat $\vec{A}\cdot\vec{B} = 0 \implies A_x B_x + A_y B_y + A_z B_z = 0$}
    \item \B{পরস্পর সমান্তরাল হওয়ার শর্ত:} {\lat $\vec{A}\times\vec{B} = \vec{0} \implies \dfrac{A_x}{B_x} = \dfrac{A_y}{B_y} = \dfrac{A_z}{B_z}$}
\end{itemize}

\itm{21} \textbf{\B{ভেক্টরের সাহায্যে জ্যামিতিক ক্ষেত্রফল নির্ণয়:}}
\begin{itemize}
    \item \B{কোনো ত্রিভুজের দুটি সন্নিহিত বাহু $\vec{P}$ ও $\vec{Q}$ হলে ক্ষেত্রফল, $\Delta = \tfrac{1}{2}|\vec{P}\times\vec{Q}| = \tfrac{1}{2}PQ\sin\theta$}
    \item \B{কোনো সামান্তরিকের দুটি সন্নিহিত বাহু $\vec{P}$ ও $\vec{Q}$ হলে ক্ষেত্রফল, $\Delta = |\vec{P}\times\vec{Q}| = PQ\sin\theta$}
    \item \B{কোনো সামান্তরিকের দুটি কর্ণ $\vec{P}$ ও $\vec{Q}$ হলে ক্ষেত্রফল, $\Delta = \tfrac{1}{2}|\vec{P}\times\vec{Q}| = \tfrac{1}{2}PQ\sin\theta$}
\end{itemize}

\itm{22} \textbf{\B{ঘনবস্তুর আয়তন ও তিনটি ভেক্টরের সমতলীয় হওয়ার শর্ত:}}
\begin{itemize}
    \item \B{সামান্তরিকীয় ঘনবস্তুর তিনটি ধার $\vec{A}, \vec{B}, \vec{C}$ হলে আয়তন, $V = \vec{A}\cdot(\vec{B}\times\vec{C}) = \vec{B}\cdot(\vec{C}\times\vec{A}) = \vec{C}\cdot(\vec{A}\times\vec{B})$}
    \item \B{তিনটি ভেক্টর একই সমতলে থাকার (সমতলীয়) শর্ত:} {\lat $\vec{A}\cdot(\vec{B}\times\vec{C}) = 0$}
\end{itemize}

---

\chsub{}{নদী-নৌকা ও বৃষ্টি সংক্রান্ত বিশেষ সূত্রাবলি}

\itm{23} \textbf{\B{নদী-নৌকার সাধারণ গতিশীলতার সমীকরণসমূহ:}}
\begin{itemize}
    \item \B{লব্ধি বেগ ($W$):} {\lat $W = \sqrt{u^2 + v^2 + 2uv\cos\alpha}$} \; [{\lat $u=$} স্রোতের বেগ, {\lat $v=$} নৌকার বেগ, {\lat $\alpha=$} মধ্যবর্তী কোণ]
    \item \B{নদী পারাপারে প্রয়োজনীয় সময় ($t$):} {\lat $t = \dfrac{s}{W} = \dfrac{s_x}{u+v\cos\alpha} = \dfrac{d}{v\sin\alpha}$} \; [{\lat $d=$} নদীর প্রস্থ]
    \item \B{নদী পার হতে পাড় বরাবর অতিক্রান্ত দূরত্ব (অনুভূমিক সরণ):} {\lat $x = (u + v\cos\alpha)t$}
    \item \B{নৌকা কর্তৃক অতিক্রান্ত প্রকৃত বা লব্ধি দূরত্ব ($s$):} {\lat $s = \sqrt{x^2 + d^2} = Wt$}
\end{itemize}

\itm{24} \textbf{\B{সর্বনিম্ন দূরত্বে বা সোজাসুজি (লম্বালম্বি) নদী পার হওয়ার শর্ত (Shortest Path):}}
\begin{itemize}
    \item \B{পাড় বরাবর অতিক্রান্ত দূরত্ব:} {\lat $x = 0$}
    \item \B{নৌকা চালনার প্রয়োজনীয় কোণ:} {\lat $\alpha = \cos^{-1}\left(-\dfrac{u}{v}\right)$} \; [এখানে অবশ্যই নূন্যতম শর্ত হলো: {\lat $v > u$}]
    \item \B{নদী পার হতে প্রয়োজনীয় সময়:} {\lat $t = \dfrac{d}{\sqrt{v^2-u^2}} = \dfrac{d}{v\sin\alpha}$}
    \item \B{মোট প্রকৃত অতিক্রান্ত দূরত্ব:} {\lat $s = d$}
    \item \B{স্রোতের সাথে লব্ধি বেগের কোণ:} {\lat $\theta = 90^\circ$}
\end{itemize}

\itm{25} \textbf{\B{সর্বনিম্ন সময়ে নদী পার হওয়ার শর্ত (Shortest Time):}}
\begin{itemize}
    \item \B{নৌকা চালনার প্রয়োজনীয় কোণ:} {\lat $\alpha = 90^\circ$} \; [স্রোতের সাথে ঠিক লম্বালম্বিভাবে রওনা দিলে]
    \item \B{প্রয়োজনীয় সর্বনিম্ন সময়:} {\lat $t_{\min} = \dfrac{d}{v}$}
    \item \B{পাড় বরাবর অতিক্রান্ত দূরত্ব:} {\lat $x = \dfrac{ud}{v}$}
    \item \B{মোট প্রকৃত অতিক্রান্ত দূরত্ব (লব্ধি সরণ):} {\lat $s = \sqrt{x^2 + d^2}$}
    \item \B{স্রোতের সাথে উৎপন্ন লব্ধি কোণ:} {\lat $\theta = \tan^{-1}\left(\dfrac{v}{u}\right)$}
\end{itemize}

\itm{26} \textbf{\B{বৃষ্টি ও ছাতা সংক্রান্ত আপেক্ষিক বেগ:}}
\begin{itemize}
    \item \B{পথচারীর সাপেক্ষে বৃষ্টির আপেক্ষিক বেগ:} {\lat $\vec{v} = \vec{v}_r - \vec{v}_m \implies v = \sqrt{v_r^2 + v_m^2}$} \; [{\lat $\vec{v}_r=$} বৃষ্টির বেগ, {\lat $\vec{v}_m=$} মানুষের বেগ]
    \item \B{বৃষ্টির হাত থেকে বাঁচতে উলম্বের সাথে ছাতা ধরার কোণ:} {\lat $\theta = \tan^{-1}\left(\dfrac{v_m}{v_r}\right)$}
\end{itemize}

---

\chsub{}{ভেক্টর ক্যালকুলাস (গ্রেডিয়েন্ট, ডাইভারজেন্স ও কার্ল)}

\itm{27} \textbf{\B{অবস্থান ভেক্টরের সাপেক্ষে বেগ ও ত্বরণ:}} {\lat $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$};\; \B{বেগ:} {\lat $\vec{v} = \dfrac{d\vec{r}}{dt}$};\; \B{ত্বরণ:} {\lat $\vec{a} = \dfrac{d\vec{v}}{dt} = \dfrac{d^2\vec{r}}{dt^2}$}

\itm{28} \textbf{\B{ভেক্টর ডিফারেনশিয়াল অপারেটর (ডেল):}} {\lat $\nabla = \dfrac{\partial}{\partial x}\hat{i} + \dfrac{\partial}{\partial y}\hat{j} + \dfrac{\partial}{\partial z}\hat{k}$}

\itm{29} \textbf{\B{গ্রেডিয়েন্ট (Gradient):}} {\lat $\text{Grad}(\phi) = \nabla\phi = \dfrac{\partial\phi}{\partial x}\hat{i} + \dfrac{\partial\phi}{\partial y}\hat{j} + \dfrac{\partial\phi}{\partial z}\hat{k}$} \; [এখানে $\phi$ একটি স্কেলার ক্ষেত্র]

\itm{30} \textbf{\B{ডাইভারজেন্স (Divergence):}} {\lat $\text{div}(\vec{A}) = \nabla\cdot\vec{A} = \dfrac{\partial A_x}{\partial x} + \dfrac{\partial A_y}{\partial y} + \dfrac{\partial A_z}{\partial z}$} \; [এখানে $\vec{A}$ একটি ভেক্টর ক্ষেত্র]

\itm{31} \textbf{\B{কার্ল (Curl):}} {\lat $\text{curl}(\vec{A}) = \nabla\times\vec{A} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k}\\ \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z}\\ A_x & A_y & A_z\end{vmatrix}$}

\itm{32} \textbf{\B{সোলেনয়ডাল ও অঘূর্ণনশীল হওয়ার গাণিতিক শর্ত:}}
\begin{itemize}
    \item \B{সোলেনয়ডাল (Solenoidal) হওয়ার শর্ত:} \B{যদি কোনো ভেক্টর ক্ষেত্রের ডাইভারজেন্স শূন্য হয়;} {\lat $\text{div}(\vec{V}) = 0 \implies \nabla\cdot\vec{V} = 0$}
    \item \B{অঘূর্ণনশীল (Irrotational) হওয়ার শর্ত:} \B{যদি কোনো ভেক্টর ক্ষেত্রের কার্ল শূন্য ভেক্টর হয়;} {\lat $\text{curl}(\vec{V}) = \vec{0} \implies \nabla\times\vec{V} = \vec{0}$}
\end{itemize}

---

\chsub{}{ভেক্টর ক্যালকুলাস অপারেটরের ইনপুট ও আউটপুট ছক}

\noindent\small
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.25\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|}
\hline
\rowcolor{tblhdr} \B{অপারেটর (Element)} & \B{প্রয়োগকৃত রাশি (Input)} & \B{ফলাফল রাশি (Output)} \\
\hline
\B{গ্রেডিয়েন্ট (Gradient)} & স্কেলার রাশি (Scalar) & ভেক্টর রাশি (Vector) \\
\hline
\B{ডাইভারজেন্স (Divergence)} & ভেক্টর রাশি (Vector) & স্কেলার রাশি (Scalar) \\
\hline
\B{কার্ল (Curl)} & ভেক্টর রাশি (Vector) & ভেক্টর রাশি (Vector) \\
\hline
\end{tabular}
\normalsize

\chsub{}{দুটি ভেক্টরের লব্ধির সারণি (সামান্তরিক সূত্র)}

\noindent\scriptsize
\begingroup
\setlength{\tabcolsep}{1.2pt}
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{|>{\centering\arraybackslash}p{0.095\linewidth}|>{\centering\arraybackslash}p{0.07\linewidth}|>{\raggedright\arraybackslash}p{0.27\linewidth}|>{\raggedright\arraybackslash}p{0.195\linewidth}|>{\centering\arraybackslash}p{0.222\linewidth}|}
\hline
\rowcolor{tblhdr} \B{মান} & \B{কোণ} & \B{লব্ধির মান (R)} & \B{লব্ধির দিক ($\theta$)} & \B{সামান্তরিকের আকার} \\
\hline
$P\!\ne\!Q$ & $0°$ & $R = P + Q$ \B{(সর্বোচ্চ)} & $\theta=0°$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=2pt]
\draw[->,thick] (0,0) -- node[above,font=\tiny]{$P$} (1.15,0);
\draw[->,thick] (1.15,0) -- node[above,font=\tiny]{$Q$} (2.0,0);
\draw[->,red,thick] (0,-0.28) -- node[below,font=\tiny,red]{$R$} (2.0,-0.28);
\node[below left,font=\tiny] at (0,0) {$O$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $0°$ & $R = 2P$ \B{বা} $2Q$ & $\theta=0°$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=2pt]
\draw[->,thick] (0,0) -- node[above,font=\tiny]{$P$} (1.0,0);
\draw[->,thick] (1.0,0) -- node[above,font=\tiny]{$Q$} (2.0,0);
\draw[->,red,thick] (0,-0.28) -- node[below,font=\tiny,red]{$R$} (2.0,-0.28);
\node[below left,font=\tiny] at (0,0) {$O$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $30°$ & $R^2\!=\!P^2\!+\!Q^2\!+\!\sqrt{3}PQ$ & $\tan\theta\!=\!\dfrac{Q}{2P\!+\!\sqrt{3}Q}$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=6pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.50,0);
\coordinate (B) at (0.779,0.450);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.32,0) arc(0:30:0.32);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.65!(C)$) {$R$};
\node[font=\tiny] at (0.44,0.08) {$30°$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $30°$ & $R^2\!=\!2P^2\!+\!\sqrt{3}P^2$ & $\theta\!=\!15°$ \B{(রম্বস)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=6pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.20,0);
\coordinate (B) at (1.039,0.600);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.32,0) arc(0:30:0.32);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.65!(C)$) {$R$};
\node[font=\tiny] at (0.44,0.08) {$30°$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $45°$ & $R^2\!=\!P^2\!+\!Q^2\!+\!\sqrt{2}PQ$ & $\tan\theta\!=\!\dfrac{Q}{\sqrt{2}P\!+\!Q}$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=6pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.50,0);
\coordinate (B) at (0.636,0.636);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.28,0) arc(0:45:0.28);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.65!(C)$) {$R$};
\node[font=\tiny] at (0.32,0.16) {$45°$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $45°$ & $R^2\!=\!2P^2\!+\!\sqrt{2}P^2$ & $\theta\!=\!22.5°$ \B{(রম্বস)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=6pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.20,0);
\coordinate (B) at (0.849,0.849);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.28,0) arc(0:45:0.28);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.65!(C)$) {$R$};
\node[font=\tiny] at (0.32,0.16) {$45°$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $60°$ & $R^2\!=\!P^2\!+\!Q^2\!+\!PQ$ & $\tan\theta\!=\!\dfrac{\sqrt{3}Q}{2P\!+\!Q}$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.50,0);
\coordinate (B) at (0.450,0.779);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.26,0) arc(0:60:0.26);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.60!(C)$) {$R$};
\node[font=\tiny] at (0.22,0.22) {$60°$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $60°$ & $R\!=\!\sqrt{3}P$ \B{বা} $\sqrt{3}Q$ & $\theta\!=\!30°$ \B{(রম্বস)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.20,0);
\coordinate (B) at (0.600,1.039);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.26,0) arc(0:60:0.26);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.60!(C)$) {$R$};
\node[font=\tiny] at (0.22,0.22) {$60°$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $90°$ & $R\!=\!\sqrt{P^2\!+\!Q^2}$ & $\tan\theta\!=\!\dfrac{Q}{P}$ \B{(আয়তক্ষেত্র)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.50,0);
\coordinate (B) at (0,0.90);
\coordinate (C) at (1.50,0.90);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.20,0)--(0.20,0.20)--(0,0.20);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.60!(C)$) {$R$};
\node[font=\tiny] at (0.27,0.10) {$90°$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $90°$ & $R\!=\!\sqrt{2}P$ \B{বা} $\sqrt{2}Q$ & $\theta\!=\!45°$ \B{(বর্গক্ষেত্র)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.20,0);
\coordinate (B) at (0,1.20);
\coordinate (C) at (1.20,1.20);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.20,0)--(0.20,0.20)--(0,0.20);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.60!(C)$) {$R$};
\node[font=\tiny] at (0.27,0.10) {$90°$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $120°$ & $R^2\!=\!P^2\!+\!Q^2\!-\!PQ$ & $\tan\theta\!=\!\dfrac{\sqrt{3}Q}{2P\!-\!Q}$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.50,0);
\coordinate (B) at (-0.450,0.779);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[above left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.28,0) arc(0:120:0.28);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.62!(C)$) {$R$};
\node[font=\tiny] at (0.06,0.28) {$120°$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $120°$ & $R\!=\!P$ \B{বা} $Q$ & $\theta\!=\!60°$ \B{(রম্বস)} &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=8pt]
\coordinate (O) at (0,0);
\coordinate (A) at (1.20,0);
\coordinate (B) at (-0.600,1.039);
\coordinate (C) at ($(A)+(B)$);
\draw[thin] (A)--(C)--(B);
\draw[thin] (O)--(A);
\draw[thin] (O)--(B);
\draw[->,thick] (O) -- node[below,font=\tiny]{$P$} (A);
\draw[->,thick] (O) -- node[above left,font=\tiny]{$Q$} (B);
\draw[->,red,thick] (O)--(C);
\draw[thin] (0.28,0) arc(0:120:0.28);
\node[below left,font=\tiny] at (O) {$O$};
\node[above,font=\tiny] at (B) {$B$};
\node[above right,font=\tiny] at (C) {$C$};
\node[right,font=\tiny,red] at ($(O)!0.62!(C)$) {$R$};
\node[font=\tiny] at (0.06,0.28) {$120°$};
\end{tikzpicture} \\
\hline
$P\!\ne\!Q$ & $180°$ & $R\!=\!P\!-\!Q$ \B{(}$P\!>\!Q$\B{)} & $\theta=0°$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=2pt]
\draw[->,thick] (0,0) -- node[above,font=\tiny]{$P$} (1.40,0);
\draw[->,thick,gray!70!black] (1.40,0) -- node[above,font=\tiny]{$Q$} (0.50,0);
\draw[->,red,thick] (0,-0.28) -- node[below,font=\tiny,red]{$R$} (0.50,-0.28);
\node[below left,font=\tiny] at (0,0) {$O$};
\end{tikzpicture} \\
\hline
$P\!=\!Q$ & $180°$ & $R = 0$ \B{(সর্বনিম্ন)} & $\theta=0°$ &
\begin{tikzpicture}[scale=0.68,>=Stealth,baseline=2pt]
\draw[->,thick] (0,0) -- node[above,font=\tiny]{$P$} (1.10,0);
\draw[->,thick,gray!70!black] (1.10,0) -- node[above,font=\tiny]{$Q$} (0,0);
\node[red,font=\tiny] at (0.55,-0.26) {$R=0$};
\node[below left,font=\tiny] at (0,0) {$O$};
\end{tikzpicture} \\
\hline
\end{tabular}
\endgroup

\noindent\scriptsize\B{লব্ধির সর্বোচ্চ মান নির্ণয়:} {\lat $R=\sqrt{P^2+Q^2+2PQ\cos\alpha}$} \B{সর্বোচ্চ হয় যখন} {\lat $\cos\alpha=1$} \B{অর্থাৎ} {\lat $\alpha=0°$}\B{।}
\normalsize

\chsub{}{ভেক্টর অধ্যায়ের অতিরিক্ত সূত্র ও চিত্রধারণা}
\itm{9} \B{ত্রিভুজ বিধি:} {\lat $\vec R=\vec P+\vec Q$};\; \B{সামান্তরিক বিধি:} {\lat $\vec R=\vec P+\vec Q$};\; \B{বহুভুজ বিধি:} {\lat $\vec R=\vec P+\vec Q+\vec S+\vec T+\vec U$}
\itm{10} \B{সমান দুই ভেক্টর} {\lat $P$} \B{, কোণ} {\lat $\alpha$}\B{:} {\lat $R=2P\cos(\alpha/2)$;\; $\theta=\alpha/2$};\; \B{অন্তর:} {\lat $\vec R=\vec P-\vec Q$}
\itm{11} \B{লম্ব উপাংশ:} {\lat $R\cos\theta=P\cos\alpha+Q\cos\beta$;\; $R\sin\theta=P\sin\alpha+Q\sin\beta$}
\itm{12} \B{ভেক্টরের সাইন সূত্র:} {\lat $\dfrac{R}{\sin(\alpha+\beta)}=\dfrac{P}{\sin\beta}=\dfrac{Q}{\sin\alpha}$}
\itm{13} \B{দিক কোসাইন:} {\lat $\cos\alpha=\dfrac{A_x}{A}$, $\cos\beta=\dfrac{A_y}{A}$, $\cos\gamma=\dfrac{A_z}{A}$;\; $\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$}
\itm{14} \B{ক্ষেত্রফল/আয়তন:} {\lat $\Delta_{\triangle}=\tfrac12|\vec P\times\vec Q|$;\; $\Delta_{\parallel}=|\vec P\times\vec Q|$;\; $V=\vec A\cdot(\vec B\times\vec C)$}
\itm{15} \B{ভেক্টর ক্যালকুলাস:} {\lat $\operatorname{grad}\phi=\nabla\phi$;\; $\operatorname{div}\vec A=\nabla\cdot\vec A$;\; $\operatorname{curl}\vec A=\nabla\times\vec A$}
\itm{16} \B{নদী-নৌকা:} {\lat $t=\dfrac{d}{v\sin\alpha}$};\; \B{সর্বনিম্ন পথ:} {\lat $\alpha=\cos^{-1}(-u/v)$, $t=d/\sqrt{v^2-u^2}$};\; \B{সর্বনিম্ন সময়:} {\lat $\alpha=90°$, $t=d/v$, $x=ud/v$}
\itm{17} \B{বৃষ্টি:} {\lat $v=\sqrt{v_r^2+v_m^2}$;\; $\theta=\tan^{-1}(v_m/v_r)$}

\chsec{অধ্যায়-৩: গতিবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বেগ:}} {\lat $v = \dfrac{ds}{dt}$}

\itm{2} \textbf{\B{ত্বরণ:}} {\lat $a = \dfrac{dv}{dt}$}

\itm{3} \textbf{\B{দূরত্ব:}} {\lat $s = vt$}\, \B{বা}\, {\lat $x = x_0 + v_x t$}

\itm{4} \textbf{\B{বেগ:}} {\lat $v = v_0 \pm at$};\; {\lat $v_x = v_{x_0} \pm a_x t$}

\itm{5} \textbf{\B{দূরত্ব:}} {\lat $s = v_0 t \pm \tfrac{1}{2}at^2$}

\itm{6} \textbf{\B{বেগ:}} {\lat $v^2 = v_0^2 \pm 2as$}

\itm{7} \textbf{\B{$t$-তম সেকেন্ডে দূরত্ব:}} {\lat $s_t = v_0 \pm \dfrac{2t-1}{2}\cdot a$}

\itm{8} \textbf{\B{প্রাসের গতি পথের সমীকরণ:}}
{\lat $y = v_{y0}t - \tfrac{1}{2}gt^2$}\; \B{বা,}\; {\lat $y = (v_0\sin\theta_0)t - \tfrac{1}{2}gt^2$}
\[y = (\tan\theta_0)x - \dfrac{g}{2(v_0\cos\theta_0)^2}\cdot x^2\]

\itm{9} \textbf{\B{সর্বাধিক উচ্চতা:}} {\lat $H = \dfrac{v_{y0}^2}{2g} = \dfrac{(v_0\sin\theta_0)^2}{2g}$}

\itm{10} \textbf{\B{পাল্লা:}} {\lat $R = \dfrac{v_0^2\sin 2\theta}{g}$}

\itm{11} \textbf{\B{বিচরণকাল:}} {\lat $T = \dfrac{2\,v_0\sin\theta_0}{g}$}

\itm{12} \textbf{\B{কৌণিক বেগ:}} {\lat $\omega = \dfrac{\theta}{t} = \dfrac{d\theta}{dt}$}

\itm{13} \textbf{\B{কৌণিক বেগ:}} {\lat $\omega = \dfrac{2\pi N}{t}$}

\itm{14} \textbf{\B{রৈখিক রূপ:}} {\lat $v = \omega r$}

\itm{15} \textbf{\B{ভেক্টর রূপ:}} {\lat $\vec{v} = \vec{\omega}\times\vec{r}$}

\itm{16} \textbf{\B{রৈখিক তুরণ ও কৌণিক তুরণের মধ্যে সম্পর্ক:}} {\lat $a = \alpha r$}

\itm{17} \textbf{\B{কেন্দ্রমুখী তুরণ:}} {\lat $a_c = \dfrac{v^2}{r} = \omega^2 r$}

\itm{18} \textbf{\B{গতির সূত্রসমূহ:}} {\lat $v=u+at$;\; $s=ut+\tfrac12at^2$;\; $v^2=u^2+2as$;\; $s=\tfrac{u+v}{2}t$}

\itm{19} \textbf{\B{পতনশীল/উর্ধ্বে নিক্ষিপ্ত:}} \B{নিচে} {\lat $v=u+gt$, $h=ut+\tfrac12gt^2$, $v^2=u^2+2gh$};\; \B{উপরে} {\lat $v=u-gt$, $h=ut-\tfrac12gt^2$, $v^2=u^2-2gh$}

\itm{20} \textbf{\B{প্রাস:}} {\lat $v_x=u\cos\theta$;\; $v_y=u\sin\theta-gt$;\; $x=(u\cos\theta)t$;\; $y=(u\sin\theta)t-\tfrac12gt^2$}
\par\noindent{\lat $R=\dfrac{u^2\sin2\theta}{g}$;\; $H=\dfrac{u^2\sin^2\theta}{2g}$;\; $T=\dfrac{2u\sin\theta}{g}$;\; $\tan\theta=\dfrac{4H}{R}$;\; $gT^2=8H$}

\chsec{অধ্যায়-৪: নিউটনিয়ান বলবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{ভরবেগ:}} {\lat $\vec{P} = m\vec{v}$}

\itm{2} \textbf{\B{বল (সাধারণ সমীকরণ):}} {\lat $\vec{F} = \dfrac{d\vec{p}}{dt} = \dfrac{d}{dt}(m\vec{v}) = m\dfrac{d\vec{v}}{dt} + \vec{v}\dfrac{dm}{dt}$}

\itm{3} \textbf{\B{বল (ভর স্থির থাকলে, $\dfrac{dm}{dt} = 0$):}} {\lat $\vec{F} = m\vec{a}$}

\itm{4} \textbf{\B{বল (বেগ স্থির থাকলে, $\dfrac{d\vec{v}}{dt} = 0$):}} {\lat $\vec{F} = \vec{v}\dfrac{dm}{dt}$}

\itm{5} \textbf{\B{ঘাতবল ও বলের ঘাত:}} {\lat $\vec{J} = \vec{F}t = \Delta\vec{p} = m\vec{v} - m\vec{v_0}$}

\itm{6} \textbf{\B{বন্দুকের পশ্চাৎবেগ:}} {\lat $MV = -mv$}

\itm{7} \textbf{\B{ভরবেগের নিত্যতা সূত্র (সংঘর্ষের পূর্বে ও পরে):}} {\lat $m_1\vec{u_1} + m_2\vec{u_2} = m_1\vec{v_1} + m_2\vec{v_2}$}

\itm{8} \textbf{\B{ভরবেগ ও গতিশক্তির সম্পর্ক:}} {\lat $E_k = \dfrac{p^2}{2m}$;\; $p = \sqrt{2mE_k}$}

\itm{9} \textbf{\B{এক-মাত্রিক স্থিতিস্থাপক সংঘর্ষের ক্ষেত্রে শেষ বেগ:}}
{\lat $v_1 = \dfrac{(m_1-m_2)u_1 + 2m_2u_2}{m_1+m_2}$};\; {\lat $v_2 = \dfrac{(m_2-m_1)u_2 + 2m_1u_1}{m_1+m_2}$}

\itm{10} \textbf{\B{স্থিতিস্থাপক সংঘর্ষে আপেক্ষিক বেগের সম্পর্ক:}} {\lat $u_1 - u_2 = v_2 - v_1 \implies u_1 + v_1 = u_2 + v_2$}

\itm{11} \textbf{\B{স্থিতি ঘর্ষণ গুণাঙ্ক:}} {\lat $\mu_s = \dfrac{F_s}{R} = \tan\theta$} \; [এখানে, $\theta = $ স্থিতি কোণ/নিশ্চল কোণ]

\itm{12} \textbf{\B{গতিয় ঘর্ষণ গুণাঙ্ক:}} {\lat $\mu_k = \dfrac{F_k}{R}$}

\itm{13} \textbf{\B{রৈখিক ও কৌণিক উপাদানের সম্পর্ক:}} {\lat $\text{\text{\B{রৈখিক উপাদান}}} = \text{\text{\B{কৌণিক উপাদান}}} \times r$} \; (যেমন: $s = \theta r$, $v = \omega r$, $a_t = \alpha r$)

\itm{14} \textbf{\B{কৌণিক বেগ:}} {\lat $\omega = \dfrac{\theta}{t} = 2\pi f = \dfrac{2\pi}{T}$}

\itm{15} \textbf{\B{কৌণিক সরণ ও ঘূর্ণন গতিবিদ্যার সমীকরণসমূহ:}} {\lat $\theta = \left(\dfrac{\omega + \omega_0}{2}\right)t = \omega_0 t + \tfrac{1}{2}\alpha t^2$};\; {\lat $\omega = \omega_0 + \alpha t$};\; {\lat $\omega^2 = \omega_0^2 + 2\alpha\theta$}

\itm{16} \textbf{\B{কৌণিক ভরবেগ:}} {\lat $\vec{L} = \vec{r} \times \vec{P} \implies L = rp\sin\theta = I\omega$}

\itm{17} \textbf{\B{কৌণিক ভরবেগের নিত্যতা সূত্র:}} {\lat $I_1\omega_1 = I_2\omega_2 = \dots = I_n\omega_n$}

\itm{18} \textbf{\B{টর্ক:}} {\lat $\vec{\tau} = \vec{r} \times \vec{F} \implies \tau = rF\sin\theta = I\alpha$}

\itm{19} \textbf{\B{দ্বন্দ্বের ভ্রামক:}} {\lat $C = \text{\text{\B{বল }}} (F) \times \text{\text{\B{বলদ্বয়ের মধ্যবর্তী দূরত্ব }}} (d)$}

\itm{20} \textbf{\B{কেন্দ্রমুখী বল ও কেন্দ্রমুখী ত্বরণ:}} {\lat $F_c = \dfrac{mv^2}{r} = m\omega^2 r = ma_c$};\; {\lat $a_c = \dfrac{v^2}{r} = \omega^2 r$}

\itm{21} \textbf{\B{স্পর্শকীয় ত্বরণ ও নিট ত্বরণ:}} {\lat $a_t = \alpha r = \dfrac{dv}{dt}$};\; {\lat $a = \sqrt{a_c^2 + a_t^2}$};\; \B{দিক:} {\lat $\theta = \tan^{-1}\left(\dfrac{a_c}{a_t}\right)$}

\itm{22} \textbf{\B{রকেটের ঊর্ধ্বমুখী ধাক্কা ও কার্যকর নিট বল:}} {\lat $F_T = v_r\dfrac{dm}{dt}$};\; {\lat $F_{\text{net}} = F_T - F_g = v_r\dfrac{dm}{dt} - Mg$}

\itm{23} \textbf{\B{রকেটের ত্বরণ:}} {\lat $a = \dfrac{v_r}{M}\left(\dfrac{dm}{dt}\right)$} \; [মহাশূন্যে];\; {\lat $a = \dfrac{v_r}{M}\left(\dfrac{dm}{dt}\right) - g$} \; [পৃথিবীর আকর্ষণে]

\itm{24} \textbf{\B{রকেটের বেগ:}} {\lat $v = u - gt + v_r \ln\left(\dfrac{m_0}{m}\right)$}

\itm{25} \textbf{\B{লিফটের প্রতিক্রিয়া বল:}} {\lat $R = m(g+a)$} \; [ওঠার ক্ষেত্রে];\; {\lat $R = m(g-a)$} \; [নামার ক্ষেত্রে]

\itm{26} \textbf{\B{রাস্তার ব্যাংকিং কোণ (নতিকোণ):}} {\lat $\tan\theta = \dfrac{v^2}{rg}$};\; {\lat $\sin\theta = \dfrac{h}{d}$} \; [এখানে, $h = $ উচ্চতা, $d = $ রাস্তার প্রস্থ]

\itm{27} \textbf{\B{ব্যাংকিং না থাকলে নিরাপদ বেগের শর্ত:}} {\lat $\mu_s = \dfrac{v^2}{rg} \implies v = \sqrt{\mu_s rg}$}

\itm{28} \textbf{\B{উল্লম্ব তলে ঘূর্ণনশীল বস্তুর ক্ষেত্রে টান ($T$):}}
\begin{itemize}
    \item \B{সর্বোচ্চ বিন্দুতে টান:} {\lat $T = \dfrac{mv^2}{r} - mg$}
    \item \B{সর্বনিম্ন বিন্দুতে টান:} {\lat $T = \dfrac{mv^2}{r} + mg$}
    \item \B{যেকোনো বিন্দুতে টান:} {\lat $T = \dfrac{mv^2}{r} + mg \cos\theta$} \; [এখানে, $\theta = $ উলম্বের সাথে উৎপন্ন কোণ]
\end{itemize}

\itm{29} \textbf{\B{আনুভূমিক তলে ঘূর্ণনরত বস্তুর যেকোনো বিন্দুতে টান:}} {\lat $T = \dfrac{mv^2}{r}$}

\itm{30} \textbf{\B{জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধ:}} {\lat $I = \Sigma mr^2 = MK^2$};\; {\lat $K = \sqrt{\dfrac{I}{M}}$}

\itm{31} \textbf{\B{লম্ব অক্ষ উপপাদ্য:}} {\lat $I_z = I_x + I_y$};\; {\lat $I_x = I_y + I_z$};\; {\lat $I_y = I_z + I_x$}

\itm{32} \textbf{\B{সমান্তরাল অক্ষ উপপাদ্য:}} {\lat $I = I_G + Mh^2$} \; [এখানে, $h = $ অক্ষদ্বয়ের মধ্যবর্তী দূরত্ব]

\itm{33} \textbf{\B{ঘূর্ণন গতিশক্তি ও মোট গতিশক্তি:}} {\lat $E_r = \tfrac{1}{2}I\omega^2$};\; {\lat $E_t = E_k + E_r = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2$}

---

\chsub{}{বিভিন্ন জ্যামিতিক বস্তুর জড়তার ভ্রামক}

\noindent\small
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.20\linewidth}|>{\raggedright\arraybackslash}p{0.45\linewidth}|>{\raggedright\arraybackslash}p{0.27\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বস্তুর ধরন} & \B{অক্ষ} & \B{জড়তার ভ্রামক ($I$)} \\
\hline
\B{সরু সুষম দণ্ড} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = \tfrac{1}{12}ML^2$} \; [{\lat $L=$} দৈর্ঘ্য] \\
\hline
\B{আয়তাকার পাত} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = \tfrac{1}{12}M(L^2 + b^2)$} \\
\hline
\B{আয়তাকার পাত} & দৈর্ঘ্যের সমান্তরাল অক্ষের সাপেক্ষে & {\lat $I = \tfrac{1}{12}Mb^2$} \; [{\lat $b=$} প্রস্থ] \\
\hline
\B{আয়তাকার পাত} & প্রস্থের সমান্তরাল অক্ষের সাপেক্ষে & {\lat $I = \tfrac{1}{12}ML^2$} \\
\hline
\B{বৃত্তাকার চাকতি} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = \tfrac{1}{2}Mr^2$} \; [{\lat $r=$} ব্যাসার্ধ] \\
\hline
\B{বৃত্তাকার চাকতি} & প্রান্তগামী স্পর্শক & {\lat $I = \tfrac{5}{4}Mr^2$} \\
\hline
\B{বৃত্তাকার চাকতি} & ব্যাসের সাপেক্ষে & {\lat $I = \tfrac{1}{4}Mr^2$} \\
\hline
\B{পাতলা রিং/বলয়} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = Mr^2$} \\
\hline
\B{পাতলা রিং/বলয়} & ব্যাসের সাপেক্ষে & {\lat $I = \tfrac{1}{2}Mr^2$} \\
\hline
\B{পাতলা রিং/বলয়} & স্পর্শকের সাপেক্ষে & {\lat $I = \tfrac{3}{2}Mr^2$} \\
\hline
\B{ফাঁপা সিলিন্ডার} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = Mr^2$} \\
\hline
\B{নিরেট সিলিন্ডার} & ভারকেন্দ্রগামী লম্ব অক্ষ & {\lat $I = \tfrac{1}{2}Mr^2$} \\
\hline
\B{ফাঁপা গোলক} & কেন্দ্র বরাবর অক্ষ & {\lat $I = \tfrac{2}{3}Mr^2$} \\
\hline
\B{নিরেট গোলক} & কেন্দ্র বরাবর অক্ষ & {\lat $I = \tfrac{2}{5}Mr^2$} \\
\hline
\end{tabular}
\normalsize

---

\chsub{}{নিউটনের গতিসূত্র}

\B{১৬৮৭ খ্রিষ্টাব্দে বিখ্যাত বিজ্ঞানী স্যার আইজ্যাক নিউটন ভর, গতি ও বেগের মধ্যে সম্পর্ক সূচক তিনটি সূত্র প্রতিপাদন করেন।}

\textbf{\B{১ম সূত্র:}} \B{বাহ্যিক বল প্রয়োগে বস্তু অবস্থার পরিবর্তন করতে বাধা না পেলে স্থির বস্তু চিরকাল স্থিরই থাকবে এবং গতিশীল বস্তু সমবেগে সরলপথে চলতে থাকবে।}

\textbf{\B{২য় সূত্র:}} \B{বস্তুর ভরবেগের পরিবর্তনের হার তার ওপর প্রযুক্ত বলের সমানুপাতিক এবং বল যেদিকে ক্রিয়া করে বস্তুর ভরবেগের পরিবর্তনও সেদিক ঘটে।}

\textbf{\B{৩য় সূত্র:}} \B{প্রতিটি ক্রিয়ার একটি সমান ও বিপরীত প্রতিক্রিয়া আছে।}

\chsub{}{ভরবেগের নিত্যতা সূত্র}

\B{"একাধিক বস্তুতে ক্রিয়া ও প্রতিক্রিয়া বল ছাড়া ভিন্ন কোনো বল না থাকলে যে কোনো একদিকে এদের মোট ভরবেগের কোনো পরিবর্তন ঘটে না।" এর নাম ভরবেগের নিত্যতা সূত্র। একে ভরবেগের সংরক্ষণ নিয়মও বলা হয়।}

\chsub{}{বলের ত্রিভুজ সূত্র}

\B{"যদি কোনো বস্তুর উপর একই সময়ে ক্রিয়ারত তিনটি বলের মান ও দিক একটি ত্রিভুজের তিনটি বাহু দ্বারা একইক্রমে সূচিত হয়, তবে এদের লব্ধি শূন্য হবে।"}

\chsub{}{নিউটনের মহাকর্ষ সূত্র}

\B{সপ্তদশ শতাব্দীতে বিখ্যাত বিজ্ঞানী স্যার আইজ্যাক নিউটন আপেলের পতন ও গ্রহ-উপগ্রহের গতি পর্যবেক্ষণ করে সূত্র প্রদান করেন।}

\B{"এই মহাবিশ্বের যেকোনো দুটি বস্তুকণা পরস্পরকে এদের সংযোজক সরলরেখা বরাবর একটি বল দ্বারা আকর্ষণ করে। এই আকর্ষণ বলের মান বস্তুকণা দুটির ভরের গুণফলের সমানুপাতিক এবং এদের মধ্যবর্তীদূরত্বের বর্গের ব্যস্তানুপাতিক।"}

\chsub{}{পড়ন্ত বস্তুর সূত্র}

\B{কোনো বস্তুকে অভিকর্ষ বলের প্রভাবে মুক্তভাবে পড়তে দিলে বস্তুটির গতি তিনটি সূত্র মানিয়া চলে। ১৫৮৯ সালে বিজ্ঞানী গ্যালিলিও এই সূত্র তিনটি আবিষ্কার করেন।}

\textbf{\B{১ম সূত্র:}} \B{বাধাহীন পথে যাত্রা করা সকল বস্তু নিশ্চল অবস্থা হতে যাত্রা করে সমান দ্রুততায় নিচে নামে। অর্থাৎ সমান সময়ে সমান দূরত্ব অতিক্রম করে।}

\textbf{\B{২য় সূত্র:}} \B{বাধাহীন পথে পড়ন্ত বস্তুর নির্দিষ্ট সময়ে প্রাপ্ত বেগ ঐ সময়ের সমানুপাতিক। কোনো পড়ন্ত বস্তু} {\lat $t$} \B{সময়ে} {\lat $v$} \B{বেগ প্রাপ্ত হলে গাণিতিকভাবে পাই,} {\lat $v \propto t$}\B{.}

\textbf{\B{৩য় সূত্র:}} \B{বাধাহীন পথে পড়ন্ত বস্তুর নির্দিষ্ট সময়ে অতিক্রান্ত দূরত্ব ঐ সময়ের বর্গের সমানুপাতিক। কোনো পড়ন্ত বস্তু} {\lat $t$} \B{সময়ে} {\lat $h$} \B{দূরত্ব অতিক্রম করলে গাণিতিকভাবে পাই,} {\lat $h \propto t^2$}\B{.}

\chsub{}{কেপলারের সূত্র}

\B{গ্রহতলি কোনো এক বলের প্রভাবে সূর্যের চারদিকে ঘুরছে। ১৬০৯ খ্রিষ্টাব্দে বিখ্যাত জ্যোতির্বিদ জন কেপলার গ্রহতলির ঘূর্ণনের তিনটি সূত্র বিবৃত করেন।}

\textbf{\B{১ম সূত্র (কক্ষের সূত্র):}} \B{প্রতিটি গ্রহ সূর্যকে উপবৃত্তের ফোকাসে রেখে একটি উপবৃত্তাকার পথে প্রদক্ষিণ করছে।}

\textbf{\B{২য় সূত্র (ক্ষেত্রফলের সূত্র):}} \B{গ্রহ এবং সূর্যের সংযোগকারী সরলরেখা সমান সময়ে সমান ক্ষেত্রফল অতিক্রম করে।}

\textbf{\B{৩য় সূত্র (সময়ের সূত্র বা আবর্তনকালের সূত্র):}} \B{প্রতিটি গ্রহের পরিক্রমণ কালের বর্গ সূর্য হতে তার গড় দূরত্বের ঘনফলের সমানুপাতিক। অর্থাৎ,} {\lat $T^2 \propto \bar{r}^3$}\B{.}

\chsec{অধ্যায়-৫: কাজ, ক্ষমতা ও শক্তি}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{কাজ:}} {\lat $W = FS$}

\itm{2} \textbf{\B{কাজ:}} {\lat $W = FS\cos\theta = \vec{F}\cdot\vec{S}$}

\itm{3} \textbf{\B{স্থিতিশক্তি:}} {\lat $E_p = mgh$}

\itm{4} \textbf{\B{গতিশক্তি:}} {\lat $E_k = \tfrac{1}{2}mv^2$}

\itm{5} \textbf{\B{ক্ষমতা:}} {\lat $P = \dfrac{W}{t} = \dfrac{FS}{t} = \dfrac{mgs}{t}$}

\itm{6} \textbf{\B{ক্ষমতা:}} {\lat $P = Fv$}

\itm{7} \textbf{\B{কাজ:}} {\lat $W = \tfrac{1}{2}mv^2 - \tfrac{1}{2}mv_0^2$}

\itm{8} \textbf{\B{কাজ:}} {\lat $W = mgh$}

\itm{9} \textbf{\B{স্প্রিং দ্বারা কৃত কাজ বা স্থিতিশক্তি:}} {\lat $U = \tfrac{1}{2}kx^2$}

\itm{10} \textbf{\B{স্প্রিং:}} {\lat $K=F/x$;\; $W=\tfrac12Kx^2=\tfrac12Fx$;\; $W=\tfrac12K(x_f^2-x_i^2)$}
\itm{11} \textbf{\B{স্প্রিং বিভাজন:}} \B{সমান} {\lat $n$} \B{ভাগে কাটলে} {\lat $K'=nK$};\; {\lat $m:n$} \B{অনুপাতে} {\lat $K_m=\dfrac{m+n}{m}K$, $K_n=\dfrac{m+n}{n}K$}
\itm{12} \textbf{\B{স্প্রিং সমবায়:}} \B{শ্রেণি} {\lat $\dfrac1{K_s}=\dfrac1{K_1}+\dfrac1{K_2}+\cdots+\dfrac1{K_n}$};\; \B{সমান্তরাল} {\lat $K_p=K_1+K_2+\cdots+K_n$}
\itm{13} \textbf{\B{মহাকর্ষ বলের বিরুদ্ধে কাজ:}} {\lat $W=GMm\left(\dfrac1{r_1}-\dfrac1{r_2}\right)$};\; \B{কাজ-শক্তি:} {\lat $W=\Delta E_k=\tfrac12m(v^2-u^2)$}
\itm{14} \textbf{\B{ক্ষমতা:}} {\lat $P_{avg}=\dfrac{W}{t}=Fv=\dfrac{mgh}{t}=\tau\omega=2\pi f\tau$;\; $P_{inst}=\dfrac{dW}{dt}$}
\itm{15} \textbf{\B{কর্মদক্ষতা:}} {\lat $\eta=\dfrac{P_{out}}{P_{in}}=\dfrac{W_{out}}{W_{in}}\times100\%$};\; {\lat $1\,HP=746\,W$}
\itm{16} \textbf{\B{শক্তি শর্টকাট:}} \B{ভূমি হতে} {\lat $x$} \B{উচ্চতায়} {\lat $K=nU\Rightarrow x=h/(n+1)$;\; $U=nK\Rightarrow x=nh/(n+1)$}

\chsec{অধ্যায়-৬: মহাকর্ষ ও অভিকর্ষ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{মহাকর্ষ বল:}} {\lat $F = G\dfrac{m_1 m_2}{d^2}$}

\itm{2} \textbf{\B{মহাকর্ষ ধ্রুবক:}} {\lat $G = \dfrac{F\cdot d^2}{m_1 m_2}$}

\itm{3} \textbf{\B{$h$ উচ্চতায় অভিকর্ষজ তুরণ:}} {\lat $g = \dfrac{GM}{(R+h)^2}$}

\itm{4} \textbf{\B{অভিকর্ষজ তুরণ:}} {\lat $g = \dfrac{GM}{R^2}$}

\itm{5} \textbf{\B{পৃথিবীর ঘনত্ব:}} {\lat $\rho = \dfrac{3g}{4\pi RG}$}

\itm{6} \textbf{\B{মুক্তিবেগ:}} {\lat $V_E = \sqrt{2gR}$}

\itm{7} \textbf{\B{উপগ্রহের বেগ:}} {\lat $V = \sqrt{\dfrac{GM}{R+h}}$}

\itm{8} \textbf{\B{বিভব:}} {\lat $V = -\dfrac{GM}{r}$}

\itm{9} \textbf{\B{উচ্চতা/গভীরতায়} $g$\B{:}} {\lat $g_h=\dfrac{GM}{(R+h)^2}=\dfrac{gR^2}{(R+h)^2}$;\; $h\ll R$ \B{হলে} $g_h=g(1-2h/R)$}
\par\noindent{\lat $g_d=g(1-d/R)=\dfrac{4}{3}\pi\rho G(R-d)$};\; \B{কেন্দ্র হতে} {\lat $r$} \B{দূরত্বে} {\lat $g=\dfrac{4}{3}\pi\rho Gr$}

\itm{10} \textbf{\B{উচ্চতা নির্ণয়:}} \B{ভূপৃষ্ঠের} {\lat $g$} \B{এর} {\lat $1/n$} \B{গুণ হলে} {\lat $h=(\sqrt n-1)R$}

\itm{11} \textbf{\B{অক্ষাংশের প্রভাব:}} {\lat $g_\lambda=g-\omega^2R\cos^2\lambda$};\; \B{মেরুতে} {\lat $g_\lambda=g$}\B{, বিষুবরেখায়} {\lat $g_\lambda=g-\omega^2R$}

\itm{12} \textbf{\B{মহাকর্ষীয় প্রাবল্য/বিভবশক্তি:}} {\lat $E=F/m=GM/r^2$;\; $V=-GM/r$;\; $U=-GMm/r$}

\itm{13} \textbf{\B{পড়ন্ত বস্তুর অনুপাত:}} {\lat $v_1/v_2=t_1/t_2$;\; $h_1/h_2=t_1^2/t_2^2$;\; $v_1^2/v_2^2=h_1/h_2$}

\itm{14} \textbf{\B{কেপলার:}} {\lat $T^2\propto r^3$;\; $\dfrac{T_1^2}{T_2^2}=\dfrac{r_1^3}{r_2^3}$;\; $\dfrac{dA}{dt}=\dfrac{L}{2m}$;\; $v_1r_1=v_2r_2$}

\itm{15} \textbf{\B{কৃত্রিম উপগ্রহ:}} {\lat $v=\sqrt{\dfrac{GM}{R+h}}=\sqrt{\dfrac{gR^2}{R+h}}=\sqrt{g_h(R+h)}=\dfrac{2\pi(R+h)}{T}$}
\par\noindent{\lat $T=2\pi(R+h)\sqrt{\dfrac{R+h}{GM}}$;\; $h=\left(\dfrac{GMT^2}{4\pi^2}\right)^{1/3}-R$}
\par\noindent{\lat $E_k=\dfrac{GMm}{2(R+h)}$;\; $E_p=-\dfrac{GMm}{R+h}$;\; $E=-\dfrac{GMm}{2(R+h)}$}

\itm{16} \textbf{\B{মুক্তিবেগ ও কক্ষপথ:}} {\lat $v_e=\sqrt{\dfrac{2GM}{R}}=\sqrt{2gR}$;\; $v_e(h)=\sqrt{\dfrac{2GM}{R+h}}=\sqrt{2g_h(R+h)}$}
\par\noindent\B{যদি} {\lat $v^2<v_e^2/2$} \B{তবে ফিরে আসে; } {\lat $v^2=v_e^2/2$} \B{বৃত্তাকার; } {\lat $v_e^2>v^2>v_e^2/2$} \B{উপবৃত্তাকার; } {\lat $v^2=v_e^2$} \B{পরাবৃত্তাকার; } {\lat $v^2>v_e^2$} \B{অধিবৃত্তাকার।}
\itm{17} \textbf{\B{ভেক্টর রূপ:}} {\lat $\vec F_{21}=-G\dfrac{m_1m_2}{r_{12}^3}\vec r_{12}$};\; {\lat $T^2=\dfrac{4\pi^2}{GM}R^3$}

\chsec{অধ্যায়-৭: পদার্থের গাঠনিক ধর্ম}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{ইয়ং-এর গুণাঙ্ক:}} {\lat $Y = \dfrac{FL}{Al}$}

\itm{2} \textbf{\B{ইয়ং-এর গুণাঙ্ক:}} {\lat $Y = \dfrac{MgL}{\pi r^2 l}$}

\itm{3} \textbf{\B{কাজ:}} {\lat $W = \tfrac{1}{2}\dfrac{YAl^2}{L}$}

\itm{4} \textbf{\B{একক আয়তনে কৃতকাজ:}} {\lat $= \tfrac{1}{2}\times\text{\B{\text{\B{পীড়ন}}}}\times\text{\B{\text{\B{বিকৃতি}}}} = \tfrac{1}{2}\times\dfrac{YAl^2}{L}$}

\itm{5} \textbf{\B{পয়সনের অনুপাত:}} {\lat $\sigma = \dfrac{\text{\B{\text{\B{পার্শ্ব বিকৃতি}}}}}{\text{\B{\text{\B{দৈর্ঘ্য বিকৃতি}}}}}$}

\itm{6} \textbf{\B{দৃঢ়তার গুণাঙ্ক:}} {\lat $n = \dfrac{F}{A\theta}$}

\itm{7} \textbf{\B{আয়তন গুণাঙ্ক:}} {\lat $K = \dfrac{\text{\B{\text{\B{আয়তন পীড়ন}}}}}{\text{\B{\text{\B{আয়তন বিকৃতি}}}}}$}

\itm{8} \textbf{\B{পৃষ্ঠটান:}} {\lat $S = \dfrac{F}{L}$}\; \B{আবার, পৃষ্ঠ শক্তি,} {\lat $S = \dfrac{W}{\Delta A}$}

\itm{9} \textbf{\B{পৃষ্ঠটান:}} {\lat $S = \dfrac{r\!\left(h + \dfrac{r}{3}\right)\rho g}{2\cos\theta}$}

\itm{10} \textbf{\B{পৃষ্ঠটান:}} {\lat $S = \dfrac{hrpg}{2\cos\theta}$}

\itm{11} \textbf{\B{পৃষ্ঠটান:}} {\lat $S = S_0(1-\alpha t)$}

\itm{12} \textbf{\B{সান্দ্র বল:}} {\lat $F = \eta A\dfrac{dv}{dx}$}

\itm{13} \textbf{\B{সান্দ্র বল:}} {\lat $F = 6\pi\eta v$}

\itm{14} \textbf{\B{সান্দ্রাঙ্ক:}} {\lat $\eta = \dfrac{2}{9}\dfrac{r^2(\rho-\sigma)g}{v}$}

\chsub{}{সরল দোলকের সূত্র}

\B{কোনো একটি সরল দোলক দোলনের সময় এর দোলনকাল চারটি সূত্র মেনে চলে; বিজ্ঞানী গ্যালিলিও এই সূত্রগুলো আবিষ্কার করেন।}

\textbf{\B{১ম সূত্র-সমকাল সূত্র:}} \B{কোনো স্থানে নির্দিষ্ট দৈর্ঘ্যবিশিষ্ট কোনো একটি সরল দোলকের বিস্তার ৪° এর মধ্যে থাকলে এর প্রতিটি দোলনের জন্য সমান সময় লাগবে।}

\textbf{\B{২য় সূত্র-দৈর্ঘ্যের সূত্র:}} \B{বিস্তার ৪° এর মধ্যে থাকলে কোনো নির্দিষ্ট স্থানে সরল দোলকের দোলনকাল এর কার্যকর দৈর্ঘ্যের বর্গমূলের সমানুপাতিক। যদি,} {\lat $T$} \B{দোলনকাল এবং} {\lat $L$} \B{কার্যকর দৈর্ঘ্য হয়, তবে দৈর্ঘ্যের সূত্রমতে,} {\lat $T \propto \sqrt{L}$}\B{.}

\textbf{\B{৩য় সূত্র-তুরণের সূত্র:}} \B{বিস্তার ৪° এর মধ্যে থাকলে নির্দিষ্ট দৈর্ঘ্যবিশিষ্ট কোনো একটি সরল দোলকের দোলনকাল ঐ স্থানের অভিকর্ষীয় তুরণের বর্গমূলের ব্যস্তানুপাতিক। দোলনকাল} {\lat $T$}\B{, অভিকর্ষীয় তুরণ} {\lat $g$} \B{হলে, তুরণের সূত্রমতে,} {\lat $T \propto \dfrac{1}{\sqrt{g}}$}\B{.}

\textbf{\B{৪র্থ সূত্র-ভরের সূত্র:}} \B{বিস্তার ৪° এর বেশি না হলে এবং কার্যকর দৈর্ঘ্য স্থির থাকলে কোনো স্থানে সরল দোলকের দোলনকাল দোলক পিণ্ডের ভর, আকৃতি বা উপাদানের উপর নির্ভর করে না।}

\chsub{}{শক্তির নিত্যতার সূত্র}

\B{শক্তি অবিনশ্বর, এটি কেবল এক রূপ হতে অন্য এক বা একাধিক রূপে পরিবর্তিত হতে পারে। রূপান্তরের আগে ও পরে মোট শক্তির পরিমাণ নির্দিষ্ট ও অপরিবর্তনীয়।}

\B{পড়ন্ত বস্তুর ক্ষেত্রে:} \B{বিনা বাধায় উচ্চ থেকে নিচে পড়ন্ত বস্তুর যেকোনো মুহূর্তে স্থিতি এবং গতি শক্তির সমষ্টি সমান।}

\chsub{}{গতি শক্তি থেকে প্রাপ্ত সূত্র}

\noindent\textbf{(i)} \B{নির্দিষ্ট ভরের কোনো বস্তুর গতিশক্তি বেগের বর্গের সমানুপাতিক।}\par
\noindent\textbf{(ii)} \B{নির্দিষ্ট ভরের কোনো বস্তুর ঘূর্ণন গতিশক্তি কৌণিক বেগের বর্গের সমানুপাতিক।}

\chsub{}{হুকের সূত্র}

\B{স্থিতিস্থাপক সীমার মধ্যে বস্তুর উপর প্রযুক্ত পীড়ন এর বিকৃতির সমানুপাতিক। গাণিতিকভাবে লেখা যায়:}
\noindent\B{পীড়ন} $\propto$ \B{বিকৃতি}\par
\noindent\B{বা, পীড়ন = ধ্রুবক $\times$ বিকৃতি}\par
\noindent\B{বা, $\dfrac{\text{\text{\B{পীড়ন}}}}{\text{\text{\B{বিকৃতি}}}}$ = ধ্রুবক}

\chsub{}{পয়সনের অনুপাত}

\B{বস্তুর পার্শ্ব বিকৃতি ও দৈর্ঘ্য বিকৃতির অনুপাত একটি ধ্রুব রাশি। অর্থাৎ $\dfrac{\text{\text{\B{পার্শ্ব বিকৃতি}}}}{\text{\text{\B{দৈর্ঘ্য বিকৃতি}}}}$ = ধ্রুবক। এই ধ্রুবককে সিগমা ($\sigma$) দ্বারা প্রকাশ করা হয়। এটি পয়সনের অনুপাত।}

\chsub{}{বয়েলের সূত্র}

\B{"স্থির তাপমাত্রায় একটি নির্দিষ্ট ভরের গ্যাসের আয়তন তার চাপের ব্যস্তানুপাতিক।" গাণিতিকভাবে: কোনো গ্যাসের আয়তন $V$ এবং চাপ $P$ হলে,}
\[V \propto \tfrac{1}{P}\; \text{\B{(স্থির তাপমাত্রায়)}} \implies PV = k\; \text{\B{(এখানে k একটি ধ্রুবক)}}\]

\chsub{}{অ্যাভোগাড্রোর প্রকল্প}

\B{সমান তাপমাত্রা ও চাপে একই আয়তনের বিভিন্ন গ্যাসে সমান সংখ্যক অণু থাকবে।}

\chsub{}{চার্লসের সূত্র}

\B{স্থির চাপে কোনো নির্দিষ্ট ভরের গ্যাসের আয়তন এর পরম তাপমাত্রার সমানুপাতিক।}

\chsub{}{পরম শূন্যে চার্লসের সূত্র}

\B{স্থির চাপে কোনো নির্দিষ্ট ভরের গ্যাসের আয়তন 0°C হতে প্রতি ডিগ্রি সেন্টিগ্রেড তাপমাত্রা পরিবর্তনের জন্য 0°C এর আয়তনের নির্দিষ্ট ভাগ $1/273 = 0.00366$ অংশ পরিবর্তিত হয়।}

\chsub{}{চাপীয় সূত্র}

\B{"স্থির আয়তনে কোনো নির্দিষ্ট ভরের গ্যাসের চাপ 0°C হতে প্রতি ডিগ্রি সেন্টিগ্রেড তাপমাত্রা পরিবর্তনের জন্য গ্যাসের 0°C এর চাপের একটি নির্দিষ্ট ভাগ $1/273 = 0.00366$ অংশ পরিবর্তিত হয়।"}

\chsub{}{পরম শূন্যে চাপের সূত্র}

\B{নির্দিষ্ট আয়তনে একটি নির্দিষ্ট ভরের কোনো গ্যাসের চাপ এর পরম তাপমাত্রার সমানুপাতিক।}

\chsub{}{গ্যাসের ঘনত্বের সূত্র}

\noindent\textbf{(i)} \B{স্থির চাপে কোনো নির্দিষ্ট ভরের গ্যাসের ঘনত্ব এর পরম তাপমাত্রার ব্যস্তানুপাতিক।}\par
\noindent\textbf{(ii)} \B{স্থির তাপমাত্রায় কোনো নির্দিষ্ট ভরের গ্যাসের চাপ এর ঘনত্বের সমানুপাতিক।}

\chsub{}{তানাতারের আড় কম্পনের সূত্র}

\B{টানা তারের সূত্রগুলো আবিষ্কার করেন বিজ্ঞানী মারিসিন। এই সূত্রগুলোকে মারিসিন সূত্রও বলা হয়।}

\textbf{\B{(i) দৈর্ঘ্যের সূত্র:}} \B{কোনো কম্পমান তারের দৈর্ঘ্য $l$ ও প্রতি একক দৈর্ঘ্যের ভর $m$ স্থির থাকলে, তারের কম্পাঙ্ক $n$ এর দৈর্ঘ্য $l$ এর ব্যস্তানুপাতিক হবে। অর্থাৎ দৈর্ঘ্য বাড়ালে কম্পাঙ্ক বাড়বে এবং দৈর্ঘ্য বাড়ালে কম্পাঙ্ক কমবে।} {\lat $\therefore n \propto \dfrac{1}{l}$} \B{যখন $T$ ও $m$ স্থির থাকে।}

\textbf{\B{(ii) টানের সূত্র:}} \B{কোনো কম্পমান তারের দৈর্ঘ্য $l$ ও প্রতি একক দৈর্ঘ্যের ভর $m$ অপরিবর্তিত থাকলে, তারের কম্পাঙ্ক $n$ এর টান $T$-এর বর্গমূলের সমানুপাতে পরিবর্তিত হবে। অর্থাৎ টান চার গুণ হইলে কম্পাঙ্ক দ্বিগুণ হবে।} {\lat $\therefore n \propto \sqrt{T}$} \B{যখন $l$ ও $m$ স্থির থাকে।}

\textbf{\B{(iii) ভরের সূত্র:}} \B{কোনো কম্পমান তারের দৈর্ঘ্য $l$ ও টান $T$ স্থির থাকলে, তারের কম্পাঙ্ক $n$ এর একক দৈর্ঘ্যের ভর $m$ এর বর্গমূলের ব্যস্তানুপাতে পরিবর্তিত হবে।} {\lat $\therefore n \propto \dfrac{1}{\sqrt{m}}$} \B{যখন $l$ ও $T$ স্থির থাকে।}

\B{ভরের সূত্রটিকে দুইভাবে প্রকাশ করা যায়:}

\textbf{\B{(ক) ব্যাসার্ধের সূত্র:}} \B{কোনো কম্পমান তারের দৈর্ঘ্য $l$, টান $T$ ও ঘনত্ব $\rho$ স্থির থাকলে, তারের কম্পাঙ্ক $n$ এর ব্যাসার্ধ $r$ এর ব্যস্তানুপাতিক।}

\textbf{\B{(খ) ঘনত্বের সূত্র:}} \B{কোনো কম্পমান তারের দৈর্ঘ্য $l$, টান $T$ ও ব্যাসার্ধ $r$ স্থির থাকলে, তারের কম্পাঙ্ক $n$ এর ঘনত্ব $\rho$ এর বর্গমূলের ব্যস্তানুপাতিক।}

\chsec{অধ্যায়-৮: পর্যায়বৃত্ত গতি}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{সরল ছন্দিত গতির স্মরণের সমীকরণ:}} {\lat $x = A\sin\omega t$}

\itm{2} \textbf{\B{সরল ছন্দিত গতির স্মরণের সমীকরণ (আদি দশা সহ):}} {\lat $x = A\sin(\omega t + \delta)$}

\itm{3} \textbf{\B{সরল ছন্দিত গতির ব্যবকলনীয় সমীকরণ:}} {\lat $\dfrac{d^2x}{dt^2} + \omega^2 x = 0$}

\itm{4} \textbf{\B{প্রত্যয়নী বল:}} {\lat $F = -kx$}

\itm{5} \textbf{\B{প্রত্যয়নী বলের মান:}} {\lat $F = kx = mg$}

\itm{6} \textbf{\B{কৌণিক কম্পাঙ্ক:}} {\lat $\omega = \sqrt{\dfrac{k}{m}} = \sqrt{\dfrac{g}{l}}$}

\itm{7} \textbf{\B{কৌণিক কম্পাঙ্ক ও পর্যায়কাল/কম্পাঙ্ক সম্পর্ক:}} {\lat $\omega = \dfrac{2\pi}{T} = 2\pi f$}

\itm{8} \textbf{\B{সরল ছন্দিত গতির বেগ:}} {\lat $v = \omega\sqrt{A^2-x^2}$}

\itm{9} \textbf{\B{সরল ছন্দিত গতির বেগ (সময় সাপেক্ষে):}} {\lat $v = A\omega\cos(\omega t+\delta)$}

\itm{10} \textbf{\B{সর্বোচ্চ বেগ:}} {\lat $V_{\max} = \omega A$}

\itm{11} \textbf{\B{সরল ছন্দিত গতির ত্বরণ:}} {\lat $a = -\omega^2 x$}

\itm{12} \textbf{\B{সরল ছন্দিত গতির ত্বরণ (সময় সাপেক্ষে):}} {\lat $a = -A\omega^2\sin(\omega t+\delta)$}

\itm{13} \textbf{\B{সর্বাধিক ত্বরণ (মান):}} {\lat $a_{\max} = \omega^2 A$}

\itm{14} \textbf{\B{গতিশক্তি:}} {\lat $E_k = \tfrac{1}{2}k(A^2-x^2) = \tfrac{1}{2}m\omega^2(A^2-x^2)$}

\itm{15} \textbf{\B{গতিশক্তি (সময় সাপেক্ষে):}} {\lat $E_k = \tfrac{1}{2}kA^2\cos^2(\omega t+\delta)$}

\itm{16} \textbf{\B{স্থিতিশক্তি / বিভবশক্তি:}} {\lat $U = \tfrac{1}{2}kx^2 = \tfrac{1}{2}m\omega^2 x^2$}

\itm{17} \textbf{\B{স্থিতিশক্তি (সময় সাপেক্ষে):}} {\lat $U = \tfrac{1}{2}kA^2\sin^2(\omega t+\delta)$}

\itm{18} \textbf{\B{মোট যান্ত্রিক শক্তি:}} {\lat $E = \tfrac{1}{2}kA^2 = \tfrac{1}{2}m\omega^2 A^2$}

\itm{19} \textbf{\B{গড় গতিশক্তি:}} {\lat $E_{avg} = \tfrac{1}{4}kA^2$}

\itm{20} \textbf{\B{কম্পাঙ্ক:}} {\lat $f = \dfrac{1}{T} = \dfrac{1}{2\pi}\sqrt{\dfrac{k}{m}}$}

\itm{21} \textbf{\B{স্প্রিং এর দোলনকাল (সাধারণ সূত্র):}} {\lat $T = 2\pi\sqrt{\dfrac{m}{k}}$}

\itm{22} \textbf{\B{আনুভূমিক স্প্রিং এর পর্যায়কাল:}} {\lat $T = 2\pi\sqrt{\dfrac{m}{k}}$}

\itm{23} \textbf{\B{উলম্ব স্প্রিং এর পর্যায়কাল:}} {\lat $T = 2\pi\sqrt{\dfrac{e}{g}}$}

\itm{24} \textbf{\B{সরল দোলকের কার্যকর দৈর্ঘ্য:}} {\lat $L = l + r = l + \dfrac{d}{2}$}

\itm{25} \textbf{\B{সরল দোলকের দোলনকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{L}{g}}$}

\chsec{অধ্যায়-৯: তরঙ্গ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{কম্পাঙ্ক:}} {\lat $f = \dfrac{1}{T}$}

\itm{2} \textbf{\B{বেগ:}} {\lat $V = f\lambda = C$}

\itm{3} \textbf{\B{দুইটি মাধ্যমের ক্ষেত্রে:}} {\lat $\dfrac{V_A}{V_B} = \dfrac{\lambda_A}{\lambda_B}$}

\itm{4} \textbf{\B{একই মাধ্যমের ক্ষেত্রে:}} {\lat $\dfrac{\lambda_1}{\lambda_2} = \dfrac{f_2}{f_1}$}

\itm{5} \textbf{\B{উপরিপাতনের নীতি:}} {\lat $y = y_1 \pm y_2$}

\itm{6} \textbf{\B{তরঙ্গের সমীকরণ:}} {\lat $y = a\sin 2\pi ft$}

\itm{7} \textbf{\B{তরঙ্গের সমীকরণ:}} {\lat $y = a\sin(\omega t-\phi)$}

\itm{8} \textbf{\B{তরঙ্গের সমীকরণ:}} {\lat $y = a\sin 2\pi\!\left(\dfrac{t}{T} - \dfrac{x}{\lambda}\right)$}

\itm{9} \textbf{\B{তরঙ্গের সমীকরণ:}} {\lat $y = a\sin\dfrac{2\pi}{\lambda}(vt-x)$}

\itm{10} \textbf{\B{স্থির তরঙ্গের সমীকরণ:}} {\lat $y = 2a\sin\dfrac{2\pi t}{T}\cos\dfrac{2\pi x}{\lambda}$}

\itm{11} \textbf{\B{শব্দাঙ্ক:}} {\lat $s = k\log I$}

\itm{12} {\lat $\dfrac{ds}{dI} = \dfrac{k}{I}$}

\itm{13} {\lat $I = 1.26\,I_0$}

\itm{14} \textbf{\B{শব্দমাত্রার পার্থক্য বা তীব্রতা লেভেল,}} {\lat $L = 10\log_{10}\!\left(\dfrac{I}{I_0}\right)$} \B{decibel} {\lat $= -10\log_{10}\!\left(\dfrac{P}{P_0}\right)$} \B{dB}

\itm{15} \textbf{\B{বিটের সংখ্যা:}} {\lat $N = f_1 - f_2$}

\itm{16} \textbf{\B{তারের বেগ:}} {\lat $v = \sqrt{\dfrac{T}{m}}$}

\itm{17} \textbf{\B{তারের কম্পাঙ্ক:}} {\lat $f = \dfrac{1}{2l}\sqrt{\dfrac{T}{m}} = \dfrac{1}{2l}\sqrt{\dfrac{T}{\pi r\rho}}$}

\chsub{}{বিভিন্ন উৎসের তীব্রতা, তীব্রতা লেভেল ও মন্তব্য}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.35\linewidth}|>{\raggedright\arraybackslash}p{0.166\linewidth}|>{\raggedright\arraybackslash}p{0.166\linewidth}|>{\raggedright\arraybackslash}p{0.184\linewidth}|}
\hline
\rowcolor{tblhdr} \B{শব্দ উৎস} & \B{তীব্রতা Wm\textsuperscript{-2}} & \B{তীব্রতা লেভেল $\beta$ (dB)} & \B{মন্তব্য} \\
\hline
& {\lat $10^{-12}$} & {\lat 0} & \B{শ্রাব্যতার প্রারম্ভিক সীমা} \\
\hline
\B{স্বাভাবিক শ্বাস-প্রশ্বাস} & {\lat $10^{-11}$} & {\lat 10} & \B{কিছিৎ শাব্দ} \\
\hline
\B{পাতার মর্মর ধ্বনি} & {\lat $10^{-10}$} & {\lat 20} & \\
\hline
\B{নির্জন রাস্তা/ফিস ফিস কথা} & {\lat $10^{-9}$} & {\lat 30} & \\
\hline
\B{লাইব্রেরি} & {\lat $10^{-8}$} & {\lat 40} & \B{খুব শান্ত} \\
\hline
\B{শান্ত অফিস/ক্লাসরুম} & {\lat $10^{-7}$} & {\lat 50} & \B{শান্ত} \\
\hline
\B{স্বাভাবিক কথোপকথন} & {\lat $10^{-6}$} & {\lat 60} & \\
\hline
\B{ব্যস্ত সড়ক} & {\lat $10^{-5}$} & {\lat 70} & \\
\hline
\B{সাধারণ কারখানা/কোলাহলপূর্ণ অফিস} & {\lat $10^{-4}$} & {\lat 80} & \B{সার্বক্ষণিক শ্রবণে ক্ষতির মাত্রাতিরিক্ত ক্ষতি} \\
\hline
\B{মোটর সাইকেল বা ভারী-ট্রাক} & {\lat $10^{-3}$} & {\lat 90} & \\
\hline
\B{পাতাল রেল} & {\lat $10^{-2}$} & {\lat 100} & \\
\hline
\B{ভারী নির্মাণ ছল} & {\lat $10^{-1}$} & {\lat 110} & \\
\hline
\B{মাইক্রোফোনে ব্যান্ড সংগীত} & {\lat $10^{0}$} & {\lat 120} & \B{ক্ষতি মাত্রার আরম্ভ} \\
\hline
\B{মেশিন গান} & {\lat $10^{1}$} & {\lat 130} & \\
\hline
\B{জেট বিমান} & {\lat $10^{3}$} & {\lat 150} & \\
\hline
\B{বড় রকেট ইঞ্জিন} & {\lat $10^{6}$} & {\lat 180} & \\
\hline
\end{tabular}
\normalsize

\chsub{}{বিভিন্ন সুর বিরামের নাম}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.166\linewidth}|>{\raggedright\arraybackslash}p{0.322\linewidth}|}
\hline
\rowcolor{tblhdr} \B{সুর বিরাম} & \B{নাম} \\
\hline
{\lat 1:1} & \B{সমায়ন (Unison)} \\
\hline
{\lat 2:1} & \B{অষ্টক (Octave)} \\
\hline
{\lat 3:1} & \B{পঞ্চম (Fifth)} \\
\hline
{\lat 5:4} & \B{গুরু তৃতীয়ক (Major third)} \\
\hline
{\lat 6:5} & \B{লঘু তৃতীয়ক (Minor third)} \\
\hline
{\lat 3:2} & \B{গুরু পঞ্চম (Major fifth)} \\
\hline
{\lat 5:3} & \B{গুরু ষষ্ঠক (Major sixth)} \\
\hline
{\lat 8:5} & \B{লঘু ষষ্ঠক (Minor sixth)} \\
\hline
{\lat 8:9} & \B{গুরু সুর (Major tone)} \\
\hline
{\lat 10:9} & \B{লঘু সুর (Minor tone)} \\
\hline
{\lat 16:15} & \B{অর্ধ সুর (Semi tone)} \\
\hline
\end{tabular}
\normalsize

\chsec{অধ্যায়-১০: আদর্শ গ্যাস ও গ্যাসের গতিতত্ত্ব}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বয়েলের সূত্র:}} {\lat $P_1 V_1 = P_2 V_2$}

\itm{2} \textbf{\B{চার্লসের সূত্র:}} {\lat $V_\theta = V_0\!\left(1 + \gamma_p \Delta\theta\right)$}

\itm{3} \textbf{\B{চার্লসের সূত্র:}} {\lat $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$}

\itm{4} \textbf{\B{চাপের সূত্র:}} {\lat $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$}

\itm{5} \textbf{\B{গ্যাসের সমন্বয় সূত্র:}} {\lat $PV = RT$}

\itm{6} \textbf{\B{গ্যাসের সমন্বয় সূত্র:}} {\lat $PV = nRT$}

\itm{7} \textbf{\B{গ্যাসের সমন্বয় সূত্র:}} {\lat $\dfrac{P_1V_1}{T_1} = \dfrac{P_2V_2}{T_2}$}

\itm{8} \textbf{\B{গড় মুক্ত পথ:}} {\lat $\lambda = \dfrac{1}{n\pi\sigma^2}$} \B{[ক্লসিয়াসের সূত্র]}

\itm{9} \textbf{\B{গড় মুক্ত পথ:}} {\lat $\lambda = \dfrac{1}{\sqrt{2}\,n\pi\sigma^2}$} \B{[ম্যাক্সওয়েলের সূত্র]}

\itm{10} \textbf{\B{গ্যাসের গতি তত্ত্বের সূত্র:}} {\lat $PV = \tfrac{1}{3}mn\bar{c^2}$}

\itm{11} \textbf{\B{গ্যাসের গতি তত্ত্বের সূত্র:}} {\lat $P = \tfrac{1}{3}\rho\bar{c^2}$}

\itm{12} \textbf{\B{গ্যাসের গতি তত্ত্বের সূত্র:}} {\lat $PV = \tfrac{2}{3}E$}

\itm{13} \textbf{\B{মূল গড় বর্গবেগ:}} {\lat $c_r \propto \sqrt{T}$}

\itm{14} \textbf{\B{মূল গড় বর্গবেগ:}} {\lat $c_r = \sqrt{\dfrac{3P}{\rho}}$}

\itm{15} \textbf{\B{আপেক্ষিকতা অর্জন:}} {\lat $R = \dfrac{f}{F}\times100\%$}

\itm{16} \textbf{\B{গ্রেশিয়ারের সূত্র:}} {\lat $(\theta_1 - \theta) = G(\theta_1 - \theta_2)$}

\chsub{}{স্থিতিস্থাপক গুণাঙ্কের তালিকা}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.202\linewidth}|>{\raggedright\arraybackslash}p{0.221\linewidth}|>{\raggedright\arraybackslash}p{0.221\linewidth}|>{\raggedright\arraybackslash}p{0.202\linewidth}|}
\hline
\rowcolor{tblhdr} \B{পদার্থের নাম} & \B{ইয়ং-এর গুণাঙ্ক Y (Nm\textsuperscript{-2})} & \B{আয়তন গুণাঙ্ক K (Nm\textsuperscript{-2})} & \B{দৃঢ়তার গুণাঙ্ক n (Nm\textsuperscript{-2})} \\
\hline
\B{অ্যালুমিনিয়াম} & {\lat $7.0\times10^{10}$} & {\lat $7.7\times10^{10}$} & {\lat $2.6\times10^{10}$} \\
\hline
\B{পিতল (60\% তামা)} & {\lat $10\times10^{10}$} & {\lat $11\times10^{10}$} & {\lat $3.5\times10^{10}$} \\
\hline
\B{তামা} & {\lat $13\times10^{10}$} & {\lat $14\times10^{10}$} & {\lat $4.8\times10^{10}$} \\
\hline
\B{কাচ} & {\lat $6.0\times10^{10}$} & {\lat $3.7\times10^{10}$} & {\lat $3.1\times10^{10}$} \\
\hline
\B{লোহা (পেটা)} & {\lat $20\times10^{10}$} & {\lat $17\times10^{10}$} & {\lat $8.0\times10^{10}$} \\
\hline
\B{লোহা (ঢালাই)} & {\lat $11.5\times10^{10}$} & {\lat $9.0\times10^{10}$} & {\lat $4.6\times10^{10}$} \\
\hline
\B{সীসা} & {\lat $1.6\times10^{10}$} & {\lat $4.6\times10^{10}$} & {\lat $0.56\times10^{10}$} \\
\hline
\B{নিকেল} & {\lat $20\times10^{10}$} & {\lat $1.6\times10^{10}$} & {\lat $7.9\times10^{10}$} \\
\hline
\B{ইস্পাত} & {\lat $20\times10^{10}$} & {\lat $17\times10^{10}$} & {\lat $8.4\times10^{10}$} \\
\hline
\B{রূপা} & {\lat $7.8\times10^{10}$} & {\lat $10.9\times10^{10}$} & {\lat $2.8\times10^{10}$} \\
\hline
\B{ব্রোঞ্জ} & {\lat $9.7\times10^{10}$} & {\lat $11.2\times10^{10}$} & {\lat $3.4\times10^{10}$} \\
\hline
\B{টাংস্টেন} & {\lat $35\times10^{10}$} & {\lat $20\times10^{10}$} & {\lat $15\times10^{10}$} \\
\hline
\B{প্ল্যাটিনাম} & {\lat $16.8\times10^{10}$} & {\lat $22.8\times10^{10}$} & {\lat $6.1\times10^{10}$} \\
\hline
\B{সোনা} & {\lat $7.8\times10^{10}$} & {\lat $17.0\times10^{10}$} & {\lat $2.7\times10^{10}$} \\
\hline
\B{কংক্রিট} & {\lat $2.0\times10^{10}$} & --- & --- \\
\hline
\B{কাঠ (ওক)} & {\lat $1.1\times10^{10}$} & --- & --- \\
\hline
\B{রাবার} & {\lat $0.05\times10^{8}$} & --- & --- \\
\hline
\B{হাড় (মানব)} & {\lat $1.4\times10^{10}$} & --- & {\lat $0.8\times10^{10}$} \\
\hline
\B{নাইলন} & {\lat $0.5\times10^{10}$} & --- & --- \\
\hline
\B{পানি} & --- & {\lat $0.21\times10^{10}$} & --- \\
\hline
\B{পারদ} & --- & {\lat $2.8\times10^{10}$} & --- \\
\hline
\B{পেট্রোলিয়াম} & --- & {\lat $0.14\times10^{10}$} & --- \\
\hline
\B{গ্লিসারিন} & --- & {\lat $0.40\times10^{10}$} & --- \\
\hline
\B{ইথাইল অ্যালকোহল} & --- & {\lat $0.11\times10^{10}$} & --- \\
\hline
\B{বায়ু} & --- & {\lat $1.015\times10^5$} & --- \\
\hline
\end{tabular}
\normalsize


\chsub{}{কয়েকটি বস্তুর জড়তার ভ্রামক ও চক্রগতির ব্যাসার্ধের রাশিমালা}

\noindent\scriptsize
\begingroup
\setlength{\tabcolsep}{1.4pt}
\renewcommand{\arraystretch}{1.34}
\begin{tabular}{|>{\raggedright\arraybackslash}p{0.304\linewidth}|>{\centering\arraybackslash}p{0.178\linewidth}|>{\raggedright\arraybackslash}p{0.184\linewidth}|>{\raggedright\arraybackslash}p{0.18\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বস্তু ও ঘূর্ণন অক্ষের প্রকৃতি} & \B{গ্রাফিক চিত্র} & \B{জড়তার ভ্রামক} & \B{চক্রগতির ব্যাসার্ধ} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের সরু ও সুষম দণ্ডের ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=white,rounded corners=1.4pt] (-2.2,-0.13) rectangle (2.2,0.13);\draw (-2.2,0) circle (0.13);\draw (2.2,0) circle (0.13);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-2.2,-0.55)--(2.2,-0.55) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{12}ML^2$} & {\lat $K=\dfrac{L}{\sqrt{12}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের সরু ও সুষম দণ্ডের প্রান্তবিন্দুগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=white,rounded corners=1.4pt] (0,-0.13) rectangle (4.1,0.13);\draw (0,0) circle (0.13);\draw (4.1,0) circle (0.13);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (0,-0.55)--(4.1,-0.55) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\end{tikzpicture} & {\lat $I=\dfrac{1}{3}ML^2$} & {\lat $K=\dfrac{L}{\sqrt{3}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের ও R ব্যাসার্ধের নিরেট সিলিন্ডারের নিজ অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (-1.8,-0.45)--(1.8,-0.45);\draw[fill=white] (-1.8,0.45)--(1.8,0.45);\draw[fill=white] (-1.8,0) ellipse (0.28 and 0.45);\draw[fill=white] (1.8,0) ellipse (0.28 and 0.45);\draw[dashed,->] (-2.35,0)--(2.45,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[->,thin] (1.8,0)--(1.8,0.45) node[midway,right,font=\tiny]{$R$};\draw[<->] (-1.8,-0.75)--(1.8,-0.75) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\end{tikzpicture} & {\lat $I=\dfrac{1}{2}MR^2$} & {\lat $K=\dfrac{R}{\sqrt{2}}$} \\
\hline
\B{M ভরের, $R_1$ অন্তর্ব্যাসার্ধ ও $R_2$ বহির্ব্যাসার্ধবিশিষ্ট ফাঁপা সিলিন্ডারের নিজ অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw (-1.8,-0.55)--(1.8,-0.55) (-1.8,0.55)--(1.8,0.55);\draw (-1.8,0) ellipse (0.33 and 0.55);\draw (1.8,0) ellipse (0.33 and 0.55);\draw (-1.8,0) ellipse (0.18 and 0.31);\draw (1.8,0) ellipse (0.18 and 0.31);\draw[dashed,->] (-2.35,0)--(2.45,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[<-,thin,shorten <=1pt] (-1.8,0.55)--(-1.25,0.7) node[right,font=\tiny]{$R_2$};\draw[<-,thin,shorten <=1pt] (-1.8,0.31)--(-1.25,0.18) node[right,font=\tiny]{$R_1$};\end{tikzpicture} & {\lat $I=\dfrac{1}{2}M(R_1^2+R_2^2)$} & {\lat $K=\sqrt{\dfrac{R_1^2+R_2^2}{2}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের ও R ব্যাসার্ধের নিরেট সিলিন্ডারের দৈর্ঘ্যের সঙ্গে লম্ব ভরকেন্দ্রগামী অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (-1.8,-0.45)--(1.8,-0.45);\draw[fill=white] (-1.8,0.45)--(1.8,0.45);\draw[fill=white] (-1.8,0) ellipse (0.28 and 0.45);\draw[fill=white] (1.8,0) ellipse (0.28 and 0.45);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.8,-0.75)--(1.8,-0.75) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\draw[->,thin] (2.15,0)--(2.15,0.45) node[midway,right,font=\tiny]{$R$};\end{tikzpicture} & {\lat $I=\dfrac{1}{4}MR^2+\dfrac{1}{12}ML^2$} & {\lat $K=\sqrt{\dfrac{R^2}{4}+\dfrac{L^2}{12}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (0,0) ellipse (1.7 and 0.48);\draw[dashed,->] (0,-1.12)--(0,1.18) node[above,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.7,0) node[right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{2}MR^2$} & {\lat $K=\dfrac{R}{\sqrt{2}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির পৃষ্ঠের অভিলম্বভাবে গমনকারী স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white,rotate=14] (0,0) ellipse (1.7 and 0.58);\draw[dashed,->] (-1.9,-1.0)--(-1.9,1.1) node[above,font=\tiny]{\B{অক্ষ}};\draw[->,rotate=14] (0,0)--(1.7,0) node[right,font=\tiny]{$R$};\end{tikzpicture} & {\lat $I=\dfrac{3}{2}MR^2$} & {\lat $K=\sqrt{\dfrac{3}{2}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (0,0) ellipse (1.65 and 0.48);\draw[dashed,->] (-1.9,0)--(1.95,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.65,0) node[above right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{4}MR^2$} & {\lat $K=\dfrac{R}{2}$} \\
\hline
\end{tabular}

\vspace{1pt}
\begin{tabular}{|>{\raggedright\arraybackslash}p{0.304\linewidth}|>{\centering\arraybackslash}p{0.178\linewidth}|>{\raggedright\arraybackslash}p{0.184\linewidth}|>{\raggedright\arraybackslash}p{0.18\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বস্তু ও ঘূর্ণন অক্ষের প্রকৃতি} & \B{গ্রাফিক চিত্র} & \B{জড়তার ভ্রামক} & \B{চক্রগতির ব্যাসার্ধ} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার রিং-এর ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick] (0,0) ellipse (1.65 and 0.48);\draw[dashed,->] (0,-1.12)--(0,1.18) node[above,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.65,0) node[right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=MR^2$} & {\lat $K=R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার রিং-এর যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick] (0,0) ellipse (1.65 and 0.48);\draw[dashed,->] (-1.9,0)--(1.95,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.65,0) node[above right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{2}MR^2$} & {\lat $K=\dfrac{R}{\sqrt{2}}$} \\
\hline
\B{M ভরের, a দৈর্ঘ্যের ও b প্রস্থের আয়তাকার পাতের ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (-1.65,-0.85) rectangle (1.65,0.85);\draw[dashed,->] (0,-1.15)--(0,1.15) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.65,-1.05)--(1.65,-1.05) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$a$};\draw[<->] (1.85,-0.85)--(1.85,0.85) node[midway,right,font=\tiny]{$b$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{12}M(a^2+b^2)$} & {\lat $K=\sqrt{\dfrac{a^2+b^2}{12}}$} \\
\hline
\B{M ভরের, a দৈর্ঘ্যের ও b প্রস্থের আয়তাকার পাতের প্রস্থের সমান্তরাল ভরকেন্দ্রগামী অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=white] (-1.65,-0.85) rectangle (1.65,0.85);\draw[dashed,->] (-1.9,0)--(1.95,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.65,-1.05)--(1.65,-1.05) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$a$};\end{tikzpicture} & {\lat $I=\dfrac{1}{12}Ma^2$} & {\lat $K=\dfrac{a}{\sqrt{12}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের নিরেট গোলকের যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\shade[ball color=white] (0,0) circle (1.05);\draw[dashed,->] (0,-1.35)--(0,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{2}{5}MR^2$} & {\lat $K=\sqrt{\dfrac{2}{5}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের নিরেট গোলকের স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\shade[ball color=white] (0,0) circle (1.05);\draw[dashed,->] (-1.27,-1.35)--(-1.27,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{7}{5}MR^2$} & {\lat $K=\sqrt{\dfrac{7}{5}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা ফাঁপা গোলকের যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=white] (0,0) circle (1.05);\draw[dashed,->] (0,-1.35)--(0,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{2}{3}MR^2$} & {\lat $K=\sqrt{\dfrac{2}{3}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা ফাঁপা গোলকের স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=white] (0,0) circle (1.05);\draw[dashed,->] (-1.27,-1.35)--(-1.27,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{5}{3}MR^2$} & {\lat $K=\sqrt{\dfrac{5}{3}}R$} \\
\hline
\end{tabular}
\endgroup
\normalsize

\chsec{পরিশিষ্ট: পদার্থবিজ্ঞানের বৈজ্ঞানিক সূত্রসমূহ (সংজ্ঞা)}

\chsub{}{গতি সমীকরণ থেকে প্রাপ্ত সূত্রসমূহ}

\noindent\textbf{(i)} \B{স্থির অবস্থান থেকে সমত্বরণে গতিশীল বস্তুর প্রাপ্ত বেগ সময়ের সমানুপাতিক।} {\lat $(v \propto t)$}\par
\noindent\textbf{(ii)} \B{স্থির অবস্থান থেকে সমত্বরণে গতিশীল বস্তু অতিক্রান্ত দূরত্ব সময়ের বর্গের সমানুপাতিক।} {\lat $(S \propto t^2)$}\par
\noindent\textbf{(iii)} \B{স্থির অবস্থান থেকে সমত্বরণে গতিশীল বস্তু অতিক্রান্ত দূরত্ব বেগের বর্গের সমানুপাতিক।} {\lat $(S \propto v^2)$}\par
\noindent\textbf{(iv)} \B{স্থির অবস্থান থেকে সমত্বরণে গতিশীল বস্তু কোনো মুহূর্তে প্রাপ্ত বেগ, অতিক্রান্ত দূরত্বের বর্গমূলের সমানুপাতিক।} {\lat $(v \propto \sqrt{S})$}

\chsub{}{মৌলিক বলসমূহ}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.160\linewidth}|>{\raggedright\arraybackslash}p{0.150\linewidth}|>{\raggedright\arraybackslash}p{0.100\linewidth}|>{\raggedright\arraybackslash}p{0.108\linewidth}|>{\raggedright\arraybackslash}p{0.160\linewidth}|>{\raggedright\arraybackslash}p{0.178\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বলের প্রকার} & \B{প্রভাবিত কণা} & \B{পাল্লা} & \B{আপেক্ষিক সবলতা} & \B{বিনিময় কণা} & \B{ভূমিকা} \\
\hline
\B{সবল নিউক্লীয়} & \B{হ্যাড্রন ও নিউট্রন} & {\lat $10^{-15}$\,m} & {\lat $10^{38}$} & \B{মেসন} & \B{নিউক্লিয়াসে গাঁথুনি} \\
\hline
\B{তাড়িত চৌম্বক বল} & \B{আধানযুক্ত কণা} & \B{অসীম} & {\lat $10^{36}$} & \B{ফোটন} & \B{পরমাণু/অণু গঠন} \\
\hline
\B{দুর্বল বল} & \B{লেপটন} & {\lat $10^{-18}$\,m} & {\lat $10^{25}$} & {\lat W} \B{ও} {\lat Z} \B{বোসন} & {\lat $\beta$}\B{-ক্ষয়ের জন্য দায়ী} \\
\hline
\B{মহাকর্ষ বল} & \B{সমস্ত পদার্থ} & \B{অসীম} & {\lat 1} & \B{গ্র্যাভিটন} & \B{সংসক্তি} \\
\hline
\end{tabular}
\normalsize

\chsub{}{বিভিন্ন গ্রহ/উপগ্রহের মুক্তিবেগের মান}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.258\linewidth}|>{\raggedright\arraybackslash}p{0.166\linewidth}|>{\raggedright\arraybackslash}p{0.258\linewidth}|>{\raggedright\arraybackslash}p{0.166\linewidth}|}
\hline
\rowcolor{tblhdr} \B{গ্রহ/উপগ্রহের নাম} & \B{মুক্তি বেগ ($V_e$)} & \B{গ্রহ/উপগ্রহের নাম} & \B{মুক্তি বেগ ($V_e$)} \\
\hline
\B{পৃথিবী} & {\lat $11.2$\,km\,s$^{-1}$} & \B{মঙ্গল} & {\lat $5.0$\,km\,s$^{-1}$} \\
\hline
\B{চাঁদ} & {\lat $2.4$\,km\,s$^{-1}$} & \B{শুক্র} & {\lat $10.3$\,km\,s$^{-1}$} \\
\hline
\B{বুধ} & {\lat $4.3$\,km\,s$^{-1}$} & \B{বৃহস্পতি} & {\lat $59.5$\,km\,s$^{-1}$} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-ক: গুরুত্বপূর্ণ আবিষ্কার ও তত্ত্বসমূহ}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.495\linewidth}|>{\raggedright\arraybackslash}p{0.368\linewidth}|}
\hline
\rowcolor{tblhdr} \B{আবিষ্কার/প্রবর্তন} & \B{আবিষ্কারক/প্রবর্তক} \\
\hline
\B{পড়ন্ত বস্তু সূত্র} & \B{গ্যালিলিও} \\
\hline
\B{বস্তু ভর, বল ও গতি সংক্রান্ত সূত্রাবলি} & \B{স্যার আইজ্যাক নিউটন} \\
\hline
\B{সরল দোলকের সূত্রাবলি} & \B{গ্যালিলিও} \\
\hline
\B{পৃষ্ঠটানের আণবিক তত্ত্ব} & \B{ল্যাপ্লাস} \\
\hline
\B{প্রাস্তিক বেগের সমীকরণ} & \B{স্টোকস} \\
\hline
\B{তাপের যান্ত্রিক/গতি/আণবিক মতবাদ} & \B{ড. জুল} \\
\hline
\B{প্লাটিনাম থার্মোমিটার} & \B{সিমেন} \\
\hline
\B{পূর্ণ বিকিরণ পাইরোমিটার} & \B{ফেরী} \\
\hline
\B{তাপগতিবিদ্যা প্রথম সূত্র} & \B{জুল} \\
\hline
\B{তাপগতিবিদ্যা দ্বিতীয় সূত্র} & \B{ক্লসিয়াস এবং কেলভিন} \\
\hline
\B{বিদ্যুৎ} & \B{ফ্যারাডে} \\
\hline
\B{সীবেক ক্রিয়া} & \B{সীবেক} \\
\hline
\B{থমসন ক্রিয়া} & \B{স্যার উইলিয়াম থমসন} \\
\hline
\B{তড়িৎ চুম্বকীয় তরঙ্গ} & \B{জেমস ক্লার্ক ম্যাক্সওয়েল} \\
\hline
\B{কোয়ান্টাম তত্ত্ব বা ভেজকবনাদ} & \B{প্ল্যাঙ্ক} \\
\hline
\B{যৌগিক অণুবীক্ষণ যন্ত্র ও গ্যালিলিও দূরবীক্ষণ যন্ত্র আবিষ্কার করেন} & \B{গ্যালিলিও} \\
\hline
\B{প্রতিফলক দূরবীক্ষণ যন্ত্র} & \B{স্যার আইজ্যাক নিউটন} \\
\hline
\B{প্রতিসরণ দূরবীক্ষণ যন্ত্র} & \B{গ্রেগরি (সর্ব প্রথম)} \\
\hline
\B{দূরবীক্ষণ যন্ত্র} & \B{হারসেল} \\
\hline
\B{নভো দূরবীক্ষণ যন্ত্র} & \B{জ্যোতির্বিদ কেপলার} \\
\hline
\B{এক্স-রে বা রনজেন রশ্মি আবিষ্কার করেন} & \B{অধ্যাপক উইল হেলম রনজেন} \\
\hline
\B{ধনরশ্মি আবিষ্কার করেন} & \B{গোল্ডস্টাইন} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-ব: আবিষ্কারক (অতিরিক্ত)}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.495\linewidth}|>{\raggedright\arraybackslash}p{0.368\linewidth}|}
\hline
\rowcolor{tblhdr} \B{আবিষ্কার/প্রবর্তন} & \B{আবিষ্কারক/প্রবর্তক} \\
\hline
\B{তাপ গতিবিদ্যার প্রথম সূত্র} & \B{জুল} \\
\hline
\B{তাপ গতিবিদ্যার দ্বিতীয় সূত্র} & \B{ক্লসিয়াস এবং কেলভিন} \\
\hline
\B{বিদ্যুৎ} & \B{ফ্যারাডে} \\
\hline
\B{সীবেক ক্রিয়া} & \B{সীবেক} \\
\hline
\B{থমসন ক্রিয়া} & \B{স্যার উইলিয়াম থমসন} \\
\hline
\B{তড়িৎ চুম্বকীয় তরঙ্গ} & \B{জেমস ক্লার্ক ম্যাক্সওয়েল} \\
\hline
\B{কোয়ান্টাম তত্ত্ব বা ভেজকবনাদ} & \B{প্ল্যাঙ্ক} \\
\hline
\B{যৌগিক অণুবীক্ষণ যন্ত্র} & \B{গ্যালিলিও} \\
\hline
\B{প্রতিফলক দূরবীক্ষণ যন্ত্র} & \B{স্যার আইজ্যাক নিউটন} \\
\hline
\B{প্রতিসরণ দূরবীক্ষণ যন্ত্র} & \B{গ্রেগরি (সর্ব প্রথম)} \\
\hline
\B{দূরবীক্ষণ যন্ত্র} & \B{হারসেল} \\
\hline
\B{নভো দূরবীক্ষণ যন্ত্র} & \B{জ্যোতির্বিদ কেপলার} \\
\hline
\B{এক্স-রে} & \B{অধ্যাপক উইল হেলম রনজেন} \\
\hline
\B{ধনরশ্মি} & \B{গোল্ডস্টাইন} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-খ: ভৌত ধ্রুবকসমূহের মান}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.221\linewidth}|>{\raggedright\arraybackslash}p{0.055\linewidth}|>{\raggedright\arraybackslash}p{0.221\linewidth}|>{\raggedright\arraybackslash}p{0.313\linewidth}|}
\hline
\rowcolor{tblhdr} \B{রাশি} & \B{সংকেত} & \B{হিসাবে ব্যবহৃত মান} & \B{বিস্তৃতমান} \\
\hline
\B{শূন্য মাধ্যমের চৌম্বক প্রবেশ্যতা} & {\lat $\mu_0$} & {\lat $4\pi\times10^{-7}$\,H\,m$^{-1}$} & \\
\hline
\B{শূন্য মাধ্যমে তড়িৎ ভেদনযোগ্যতা} & {\lat $\varepsilon_0$} & {\lat $8.854\times10^{-12}$\,F\,m$^{-1}$} & \\
\hline
\B{শূন্য মাধ্যমে আলোর দ্রুতি} & {\lat $c$} & {\lat $3\times10^8$\,ms$^{-1}$} & {\lat $(2.997925\pm0.000003)\times10^8$\,ms$^{-1}$} \\
\hline
\B{প্ল্যাঙ্কের ধ্রুবক} & {\lat $h$} & {\lat $6.63\times10^{-34}$\,Js} & {\lat $(6.6256\pm0.0005)\times10^{-34}$\,Js} \\
\hline
\B{ইলেকট্রনের চার্জ} & {\lat $e$} & {\lat $-1.60\times10^{-19}$\,C} & {\lat $(1.60210\pm0.00007)\times10^{-19}$\,C} \\
\hline
\B{ইলেকট্রনের ভর} & {\lat $m_e$} & {\lat $9.11\times10^{-31}$\,kg} & {\lat $(9.1091\pm0.0004)\times10^{-31}$\,kg} \\
\hline
\B{ইলেকট্রনের আধান ও ভর অনুপাত} & {\lat $e/m_e$} & {\lat $1.759\times10^{11}$\,C\,kg$^{-1}$} & \\
\hline
\B{প্রোটনের ভর} & {\lat $m_p$} & {\lat $1.67\times10^{-27}$\,kg} & \\
\hline
\B{নিউট্রনের ভর} & {\lat $m_n$} & {\lat $1.675\times10^{-27}$\,kg} & \\
\hline
\B{একীভূত পারমাণবিক ভর একক} & {\lat $m_u$} & {\lat $1.66\times10^{-27}$\,kg} & \\
\hline
\B{অ্যাভোগাড্রো ধ্রুবক} & {\lat $N_A$} & {\lat $6.023\times10^{23}$\,mol$^{-1}$} & {\lat $(6.02252\pm0.00028)\times10^{23}$\,mol$^{-1}$} \\
\hline
\B{মোলার গ্যাস ধ্রুবক} & {\lat $R$} & {\lat $8.31\,JK^{-1}\,mol^{-1}$} & {\lat $(8.3143\pm0.0012)\,JK^{-1}\,mol^{-1}$} \\
\hline
\B{ফারাডে ধ্রুবক} & {\lat $F$} & {\lat $96500$\,C\,mol$^{-1}$} & \\
\hline
\B{বোলজম্যানের ধ্রুবক} & {\lat $K$} & {\lat $1.38\times10^{-23}$\,JK$^{-1}$} & {\lat $(1.38054\pm0.00018)\times10^{-23}$\,JK$^{-1}$} \\
\hline
\B{স্টিফানের একক} & {\lat $\sigma$} & {\lat $5.67\times10^{-8}$\,Wm$^{-2}$K$^{-4}$} & {\lat $(5.6697\pm0.0029)\times10^{-8}$\,Wm$^{-2}$K$^{-4}$} \\
\hline
\B{মহাকর্ষীয় ধ্রুবক} & {\lat $G$} & {\lat $6.673\times10^{-11}$\,Nm$^2$kg$^{-2}$} & {\lat $(6.670\pm0.015)\times10^{-11}$\,Nm$^2$kg$^{-2}$} \\
\hline
\B{পারদের ঘনত্ব (0°C)} & & {\lat $1.36\times10^4$\,kgm$^{-3}$} & \\
\hline
\B{পারদের ঘনত্ব (20°C)} & & {\lat $1.355\times10^4$\,kgm$^{-3}$} & \\
\hline
\B{বায়ুর ঘনত্ব (0°C)} & & {\lat $1.293$\,kgm$^{-3}$} & \\
\hline
\B{বায়ুর ঘনত্ব (20°C)} & & {\lat $1.204$\,kgm$^{-3}$} & \\
\hline
\B{বায়ুতে শব্দের দ্রুতি (0°C)} & & {\lat $331.5$\,ms$^{-1}$} & \\
\hline
\B{বায়ুতে শব্দের দ্রুতি (20°C)} & & {\lat $343.6$\,ms$^{-1}$} & \\
\hline
\B{প্রমাণ বায়ুমণ্ডলীয় চাপ} & & {\lat $760$\,mmHg $=.76$\,mHg} & \\
\hline
\B{প্রমাণ বায়ুমণ্ডলীয় চাপ} & & {\lat $1.013\times10^5$\,Pa} & \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-গ: গ্রিক বর্ণমালা}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.202\linewidth}|>{\raggedright\arraybackslash}p{0.055\linewidth}|>{\raggedright\arraybackslash}p{0.055\linewidth}|>{\raggedright\arraybackslash}p{0.202\linewidth}|>{\raggedright\arraybackslash}p{0.055\linewidth}|>{\raggedright\arraybackslash}p{0.055\linewidth}|}
\hline
\rowcolor{tblhdr} \B{উচ্চারণ} & \B{বড় হাতের} & \B{ছোট হাতের} & \B{উচ্চারণ} & \B{বড় হাতের} & \B{ছোট হাতের} \\
\hline
\B{আলফা (alpha)} & {\lat A} & {\lat $\alpha$} & \B{নিউ (nu)} & {\lat N} & {\lat $\nu$} \\
\hline
\B{বিটা (beta)} & {\lat B} & {\lat $\beta$} & \B{জাই (xi)} & {\lat $\Xi$} & {\lat $\xi$} \\
\hline
\B{গামা (gamma)} & {\lat $\Gamma$} & {\lat $\gamma$} & \B{অমাইক্রন (omicron)} & {\lat O} & {\lat o} \\
\hline
\B{ডেল্টা (delta)} & {\lat $\Delta$} & {\lat $\delta$} & \B{পাই (pi)} & {\lat $\Pi$} & {\lat $\pi$} \\
\hline
\B{এপ্সাইলন (epsilon)} & {\lat E} & {\lat $\varepsilon$} & \B{রো (rho)} & {\lat P} & {\lat $\rho$} \\
\hline
\B{জিটা (zeta)} & {\lat Z} & {\lat $\zeta$} & \B{সিগমা (sigma)} & {\lat $\Sigma$} & {\lat $\sigma$} \\
\hline
\B{ইটা (eta)} & {\lat H} & {\lat $\eta$} & \B{টাও (tau)} & {\lat T} & {\lat $\tau$} \\
\hline
\B{থিটা (theta)} & {\lat $\Theta$} & {\lat $\theta$} & \B{আপসাইলন (upsilon)} & {\lat Y} & {\lat $\upsilon$} \\
\hline
\B{আয়োটা (iota)} & {\lat I} & {\lat $\iota$} & \B{ফাই (phi)} & {\lat $\Phi$} & {\lat $\phi,\varphi$} \\
\hline
\B{কাপ্পা (kappa)} & {\lat K} & {\lat $\kappa$} & \B{কাই (chi)} & {\lat X} & {\lat $\chi$} \\
\hline
\B{লেম্বডা (lambda)} & {\lat $\Lambda$} & {\lat $\lambda$} & \B{সাই (psi)} & {\lat $\Psi$} & {\lat $\psi$} \\
\hline
\B{মিউ (mu)} & {\lat M} & {\lat $\mu$} & \B{ওমেগা (omega)} & {\lat $\Omega$} & {\lat $\omega$} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-ঘ: দেশের সূচক, তাদের নাম ও উদাহরণ}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.202\linewidth}|>{\raggedright\arraybackslash}p{0.092\linewidth}|>{\raggedright\arraybackslash}p{0.074\linewidth}|>{\raggedright\arraybackslash}p{0.478\linewidth}|}
\hline
\rowcolor{tblhdr} \B{উপসর্গ} & \B{উৎপাদক} & \B{সংকেত} & \B{উদাহরণ} \\
\hline
\B{এক্সা (exa)} & {\lat $10^{18}$} & {\lat E} & \B{১ এক্সা মিটার = 1Em = $10^{18}$ m} \\
\hline
\B{পেটা (peta)} & {\lat $10^{15}$} & {\lat P} & \B{১ পেটা মিটার = 1Pm = $10^{15}$ m} \\
\hline
\B{টেরা (tera)} & {\lat $10^{12}$} & {\lat T} & \B{১ টেরা গ্রাম 1Tg = $10^{12}$ g} \\
\hline
\B{গিগা (giga)} & {\lat $10^9$} & {\lat G} & \B{১ গিগা জুল 1GJ = $10^9$ J} \\
\hline
\B{মেগা (mega)} & {\lat $10^6$} & {\lat M} & \B{১ মেগা ওয়াট = 1MW = $10^6$ W} \\
\hline
\B{কিলো (kilo)} & {\lat $10^3$} & {\lat k} & \B{১ কিলোভোল্ট = 1kV = $10^3$ V} \\
\hline
\B{হেক্টো (hecto)} & {\lat $10^2$} & {\lat h} & \B{১ হেক্টো প্যাসকেল = 1hPa = $10^2$ Pa} \\
\hline
\B{ডেকা (deca)} & {\lat $10^{1}$} & {\lat da} & \B{১ ডেকা নিউটন = daN = 10 N} \\
\hline
\B{ডেসি (deci)} & {\lat $10^{-1}$} & {\lat d} & \B{১ ডেসি ওহ্ম = 1d$\Omega$ = $10^{-1}\,\Omega$} \\
\hline
\B{সেন্টি (centi)} & {\lat $10^{-2}$} & {\lat c} & \B{১ সেন্টিমিটার = 1 cm = $10^{-2}$ m} \\
\hline
\B{মিলি (mili)} & {\lat $10^{-3}$} & {\lat m} & \B{১ মিলি আম্পিয়ার = 1 mA = $10^{-3}$ A} \\
\hline
\B{মাইক্রো (micro)} & {\lat $10^{-6}$} & {\lat $\mu$} & \B{১ মাইক্রো ভোল্ট = $1\,\mu$V = $10^{-6}$ V} \\
\hline
\B{ন্যানো (nano)} & {\lat $10^{-9}$} & {\lat n} & \B{১ ন্যানো সেকেন্ড = 1 ns = $10^{-9}$ s} \\
\hline
\B{পিকো (pico)} & {\lat $10^{-12}$} & {\lat p} & \B{১ পিকো ফারাডে = 1 pF = $10^{-12}$ F} \\
\hline
\B{ফেমটো (femto)} & {\lat $10^{-15}$} & {\lat f} & \B{১ ফেমটো মিটার = 1 fm = $10^{-15}$ m} \\
\hline
\B{অটো (atto)} & {\lat $10^{-18}$} & {\lat a} & \B{১ অটোওয়াট = 1aW = $10^{-18}$ W} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-ঙ: মহাশূন্যযানের নাম ও সাফল্য}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.276\linewidth}|>{\raggedright\arraybackslash}p{0.607\linewidth}|}
\hline
\rowcolor{tblhdr} \B{মহাশূন্যযানের নাম} & \B{সাফল্যের প্রকৃতি} \\
\hline
\B{স্পুটনিক–I} (4.10.1957) & \B{মহাশূন্যে পাঠানো প্রথম কৃত্রিম উপগ্রহ।} \\
\hline
\B{স্পুটনিক–II} (3.11.1957) & \B{জীবন্ত কুকুর বহনকারী প্রথম মহাশূন্য যান।} \\
\hline
\B{স্কোর} (18.12.1958) & \B{মহাশূন্যে পাঠানো প্রথম যোগাযোগ উপগ্রহ।} \\
\hline
\B{লুনা–III} (4.10.1959) & \B{প্রথম উপগ্রহ যা চাঁদের অদৃশ্যমান অংশের ছবি পাঠায়।} \\
\hline
\B{ভস্টক-I} (12.4.1961) & \B{মানুষের নিয়ে যাওয়া প্রথম মহাশূন্য যাত্রা।} \\
\hline
\B{ভস্টক–6} (4.12.1963) & \B{প্রথম মহিলা মহাশূন্যচারীবাহী মহাশূন্য যান। এ মহিলা ছিলেন সোভিয়েট ইউনিয়নের ভেলেন্টিনা তেরেস্কোভা।} \\
\hline
\B{ইনটেলসেট-I} (6.4.1965) & \B{বাণিজ্যিক কাজে ব্যবহারের জন্য পাঠানো প্রথম যোগাযোগ উপগ্রহ।} \\
\hline
\end{tabular}
\normalsize


\chsec{পরিশিষ্ট-ঠ: গত বছরের নোট থেকে অতিরিক্ত সূত্রসমূহ (১ম পত্র)}

\chsub{}{পরিমাপ ও ত্রুটি (অতিরিক্ত)}

\itm{1} \textbf{\B{ভার্নিয়ার ধ্রুবক:}} {\lat $V.C = \dfrac{l}{n}$}

\itm{2} \textbf{\B{ভার্নিয়ার ক্যালিপার্স দ্বারা পরিমাপকৃত দৈর্ঘ্য বা ব্যাস:}} {\lat $D = L + V.C \times V$}

\itm{3} \textbf{\B{স্ক্রুগজের লঘিষ্ঠ গণন:}} {\lat $LC = \dfrac{l}{n}$}

\itm{4} \textbf{\B{স্ক্রুগজ দ্বারা পরিমাপকৃত ব্যাস বা পুরুত্ব:}} {\lat $D = L + LC \times C$}

\itm{5} \textbf{\B{পরিমাপের গড় মান:}} {\lat $\bar x = \dfrac{\sum x}{n}$}

\itm{6} \textbf{\B{পরিমাপের বিচ্যুতি:}} {\lat $d_n = x_n - \bar x$}

\itm{7} \textbf{\B{প্রমাণ বিচ্যুতি:}} {\lat $d = \sqrt{\dfrac{\sum d^2}{n}}$}

\itm{8} \textbf{\B{গড় বিচ্যুতি:}} {\lat $\bar d = \dfrac{\sum|d|}{n}$}

\itm{9} \textbf{\B{পরম ত্রুটি:}} {\lat $\Delta x = x - y$}

\itm{10} \textbf{\B{আপেক্ষিক ত্রুটি:}} {\lat $\dfrac{\Delta x}{x} = \dfrac{x - y}{x}$}

\itm{11} \textbf{\B{শতকরা ত্রুটি:}} {\lat $\% = \dfrac{\Delta x}{x} \times 100\%$}

\itm{12} \textbf{\B{সূচকযুক্ত রাশির আনুপাতিক বা আপেক্ষিক ত্রুটি ($x = u^pv^q/w^r$ হলে):}} {\lat $\dfrac{\Delta x}{x} = p\dfrac{\Delta u}{u} + q\dfrac{\Delta v}{v} + r\dfrac{\Delta w}{w}$}

\itm{13} \textbf{\B{স্ফেরোমিটার দ্বারা গোলীয় তলের বক্রতার ব্যাসার্ধ:}} {\lat $R = \dfrac{d^2}{6h} + \dfrac{h}{2}$}


\chsub{}{ভেক্টর (অতিরিক্ত)}

\itm{1} \textbf{\B{ত্রিভুজ বা সামান্তরিক সূত্র (লব্ধি ভেক্টর):}} {\lat $\vec R = \vec P + \vec Q$}

\itm{2} \textbf{\B{বহুভুজ সূত্র (লব্ধি ভেক্টর):}} {\lat $\vec R = \vec P + \vec Q + \vec S + \vec T + \vec U$}

\itm{3} \textbf{\B{ভেক্টরের বণ্টন নিয়ম:}} {\lat $\vec A(\vec B + \vec C) = \vec A\vec B + \vec A\vec C$}

\itm{4} \textbf{\B{ভেক্টরের বিনিময় নিয়ম:}} {\lat $\vec A + \vec B = \vec B + \vec A$}

\itm{5} \textbf{\B{ভেক্টরের সংযোগ নিয়ম:}} {\lat $(\vec A + \vec B) + \vec C = \vec A + (\vec B + \vec C)$}

\itm{6} \textbf{\B{লব্ধি ভেক্টরের মান:}} {\lat $R = \sqrt{P^2 + Q^2 + 2PQ\cos\alpha}$}

\itm{7} \textbf{\B{$P$ ভেক্টরের সাথে লব্ধির উৎপন্ন কোণ (দিক):}} {\lat $\theta = \tan^{-1}\left(\dfrac{Q\sin\alpha}{P + Q\cos\alpha}\right)$}

\itm{8} \textbf{\B{$Q$ ভেক্টরের সাথে লব্ধির উৎপন্ন কোণ (দিক):}} {\lat $\beta = \tan^{-1}\left(\dfrac{P\sin\alpha}{Q + P\cos\alpha}\right)$}

\itm{9} \textbf{\B{সর্বোচ্চ লব্ধি:}} {\lat $R_{\max} = P + Q$}

\itm{10} \textbf{\B{সর্বনিম্ন লব্ধি:}} {\lat $R_{\min} = P \sim Q$}

\itm{11} \textbf{\B{ভেক্টরদ্বয় লম্বভাবে ক্রিয়া করলে লব্ধির সাথে সম্পর্ক:}} {\lat $2R_P^2 = R_{\max}^2 + R_{\min}^2$}

\itm{12} \textbf{\B{দুটি সমান মানের ভেক্টরের লব্ধির মান:}} {\lat $R = 2P\cos\left(\dfrac{\alpha}{2}\right)$}

\itm{13} \textbf{\B{দুটি সমান মানের ভেক্টরের লব্ধির দিক:}} {\lat $\theta = \dfrac{\alpha}{2}$}

\itm{14} \textbf{\B{লব্ধির অনুভূমিক লম্ব উপাংশ:}} {\lat $R\cos\theta = P\cos\alpha + Q\cos\beta$}

\itm{15} \textbf{\B{লব্ধির উলম্ব লম্ব উপাংশ:}} {\lat $R\sin\theta = P\sin\alpha + Q\sin\beta$}

\itm{16} \textbf{\B{ভেক্টরের সাইন সূত্র (ল্যামির সূত্র রূপ):}} {\lat $\dfrac{P}{\sin\alpha} = \dfrac{Q}{\sin\beta} = \dfrac{R}{\sin(\alpha+\beta)}$}

\itm{17} \textbf{\B{ত্রিমাত্রিক স্থানাঙ্ক ব্যবস্থায় ভেক্টরের মান:}} {\lat $|\vec A| = \sqrt{A_x^2 + A_y^2 + A_z^2}$}

\itm{18} \textbf{\B{একক ভেক্টর:}} {\lat $\hat a = \dfrac{\vec A}{A}$}

\itm{19} \textbf{\B{ডট গুণন (স্কেলার গুণন):}} {\lat $\vec P \cdot \vec Q = PQ\cos\theta$}

\itm{20} \textbf{\B{ক্রস গুণন (ভেক্টর গুণন):}} {\lat $\vec P \times \vec Q = PQ\sin\theta \, \hat\eta$}

\itm{21} \textbf{\B{আয়ত একক ভেক্টরের ডট গুণন:}} {\lat $\hat i \cdot \hat i = \hat j \cdot \hat j = \hat k \cdot \hat k = 1$}

\itm{22} \textbf{\B{আয়ত একক ভেক্টরের ক্রস গুণন:}} {\lat $\hat i \times \hat j = \hat k, \; \hat j \times \hat k = \hat i, \; \hat k \times \hat i = \hat j$}

\itm{23} \textbf{\B{X-অক্ষের সাথে দিক কোসাইন:}} {\lat $\cos\alpha = \dfrac{A_x}{|\vec A|}$}

\itm{24} \textbf{\B{দিক কোসাইনের বর্গের সমষ্টির সম্পর্ক:}} {\lat $\cos^2\alpha + \cos^2\beta + \cos^2\gamma = 1$}

\itm{25} \textbf{\B{দিক সাইনের বর্গের সমষ্টির সম্পর্ক:}} {\lat $\sin^2\alpha + \sin^2\beta + \sin^2\gamma = 2$}

\itm{26} \textbf{\B{$\vec A$ ভেক্টরের দিকে $\vec B$ ভেক্টরের স্কেলার অভিক্ষেপ:}} {\lat $B\cos\theta = \dfrac{\vec A \cdot \vec B}{A}$}

\itm{27} \textbf{\B{$\vec B$ ভেক্টরের দিকে $\vec A$ ভেক্টরের স্কেলার অভিক্ষেপ:}} {\lat $A\cos\theta = \dfrac{\vec A \cdot \vec B}{B}$}

\itm{28} \textbf{\B{দুটি ভেক্টর সমান্তরাল হওয়ার শর্ত (উপাংশের অনুপাত):}} {\lat $\dfrac{A_x}{B_x} = \dfrac{A_y}{B_y} = \dfrac{A_z}{B_z}$}

\itm{29} \textbf{\B{দুটি ভেক্টর পরস্পর লম্ব হওয়ার শর্ত:}} {\lat $\vec A \cdot \vec B = 0$}

\itm{30} \textbf{\B{দুটি ভেক্টর পরস্পর সমান্তরাল হওয়ার শর্ত (ক্রস গুণন):}} {\lat $\vec A \times \vec B = 0$}

\itm{31} \textbf{\B{সন্নিহিত বাহুদ্বয় দ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল:}} {\lat $\Delta = \tfrac{1}{2}|\vec P \times \vec Q|$}

\itm{32} \textbf{\B{সন্নিহিত বাহুদ্বয় দ্বারা গঠিত সামান্তরিকের ক্ষেত্রফল:}} {\lat $|\vec P \times \vec Q|$}

\itm{33} \textbf{\B{কর্ণদ্বয় দ্বারা গঠিত সামান্তরিকের ক্ষেত্রফল:}} {\lat $\tfrac{1}{2}|\vec P \times \vec Q|$}

\itm{34} \textbf{\B{তিনটি ভেক্টর দ্বারা গঠিত ঘনবস্তুর আয়তন:}} {\lat $V = \vec A \cdot (\vec B \times \vec C)$}

\itm{35} \textbf{\B{তিনটি ভেক্টর একই সমতলে থাকার শর্ত (সমতলীয়):}} {\lat $\vec A \cdot (\vec B \times \vec C) = 0$}

\itm{36} \textbf{\B{তাৎক্ষণিক বেগ:}} {\lat $\vec v = \dfrac{d\vec r}{dt}$}

\itm{37} \textbf{\B{তাৎক্ষণিক ত্বরণ:}} {\lat $\vec a = \dfrac{d^2\vec r}{dt^2}$}

\itm{38} \textbf{\B{স্কেলার ক্ষেত্রের গ্রেডিয়েন্ট:}} {\lat $\nabla\varphi$}

\itm{39} \textbf{\B{ভেক্টর ক্ষেত্রের ডাইভারজেন্স:}} {\lat $\nabla \cdot \vec A$}

\itm{40} \textbf{\B{ভেক্টর ক্ষেত্রের কার্ল:}} {\lat $\nabla \times \vec A$}

\itm{41} \textbf{\B{ভেক্টর ক্ষেত্রটি সলিনয়ডাল (Solenoidal) হওয়ার শর্ত:}} {\lat $\nabla \cdot \vec v = 0$}

\itm{42} \textbf{\B{ভেক্টর ক্ষেত্রটি অঘূর্ণনশীল (Irrotational) হওয়ার শর্ত:}} {\lat $\nabla \times \vec v = 0$}

\itm{43} \textbf{\B{নদী-নৌকা: সর্বনিম্ন পথে নদী পার হতে নৌকা চালানোর কোণ:}} {\lat $\alpha = \cos^{-1}\left(-\dfrac{u}{v}\right)$}

\itm{44} \textbf{\B{নদী-নৌকা: সর্বনিম্ন পথে নদী পার হতে প্রয়োজনীয় সময়:}} {\lat $t = \dfrac{d}{\sqrt{v^2 - u^2}}$}

\itm{45} \textbf{\B{নদী-নৌকা: সর্বনিম্ন পথে পারাপারে অতিক্রান্ত দূরত্ব:}} {\lat $s = d$}

\itm{46} \textbf{\B{নদী-নৌকা: সর্বনিম্ন পথে লব্ধি বেগের দিক (তীরের সাথে কোণ):}} {\lat $\theta = 90^\circ$}

\itm{47} \textbf{\B{নদী-নৌকা: সর্বনিম্ন সময়ে নদী পার হতে নৌকা চালানোর কোণ:}} {\lat $\alpha = 90^\circ$}

\itm{48} \textbf{\B{নদী-নৌকা: সর্বনিম্ন পারাপার সময়:}} {\lat $t = \dfrac{d}{v}$}

\itm{49} \textbf{\B{নদী-নৌকা: সর্বনিম্ন সময়ে পারাপারে নদীর তীর বরাবর সরণ:}} {\lat $x = \dfrac{ud}{v}$}

\itm{50} \textbf{\B{নদী-নৌকা: সর্বনিম্ন সময়ে পারাপারে মোট অতিক্রান্ত দূরত্ব:}} {\lat $s = \sqrt{x^2 + d^2}$}

\itm{51} \textbf{\B{নদী-নৌকা: সর্বনিম্ন সময়ে লব্ধি বেগের দিক (তীরের সাথে কোণ):}} {\lat $\theta = \tan^{-1}\left(\dfrac{v}{u}\right)$}

\itm{52} \textbf{\B{বৃষ্টি ও পথচারীর লব্ধি/আপেক্ষিক বেগ:}} {\lat $v = \sqrt{v_r^2 + v_m^2}$}

\itm{53} \textbf{\B{উলম্বের সাথে ছাতা ধরার কোণ:}} {\lat $\theta = \tan^{-1}\left(\dfrac{v_m}{v_r}\right)$}

\chsub{}{গতিবিদ্যা (অতিরিক্ত)}

\itm{1} \textbf{\B{সমবেগ:}} {\lat $s = vt$}

\itm{2} \textbf{\B{$t$-তম সেকেন্ডে অতিক্রান্ত দূরত্ব:}} {\lat $S_{th} = u + \tfrac{1}{2}a(2t-1)$}

\itm{3} \textbf{\B{প্রাসের যেকোনো সময়ে অনুভূমিক বেগ:}} {\lat $v_x = u\cos\theta$}

\itm{4} \textbf{\B{প্রাসের যেকোনো সময়ে উলম্ব বেগ:}} {\lat $v_y = u\sin\theta - gt$}

\itm{5} \textbf{\B{প্রাসের যেকোনো সময়ে লব্ধি বেগ:}} {\lat $v = \sqrt{v_x^2 + v_y^2}$}

\itm{6} \textbf{\B{প্রাসের যেকোনো সময়ে অনুভূমিক সরণ (অবস্থান):}} {\lat $x = (u\cos\theta)t$}

\itm{7} \textbf{\B{প্রাসের যেকোনো সময়ে উলম্ব সরণ (অবস্থান):}} {\lat $y = (u\sin\theta)t - \tfrac{1}{2}gt^2$}

\itm{8} \textbf{\B{প্রাসের অনুভূমিক পাল্লা:}} {\lat $R = \dfrac{u^2\sin2\theta}{g}$}

\itm{9} \textbf{\B{প্রাসের সর্বাধিক উচ্চতা:}} {\lat $H = \dfrac{u^2\sin^2\theta}{2g}$}

\itm{10} \textbf{\B{প্রাসের বিচরণকাল (উড্ডয়নকাল):}} {\lat $T = \dfrac{2u\sin\theta}{g}$}

\itm{11} \textbf{\B{প্রাসের নিক্ষেপণ কোণ, সর্বাধিক উচ্চতা ও অনুভূমিক পাল্লার সম্পর্ক:}} {\lat $\tan\theta = \dfrac{4H}{R}$}

\itm{12} \textbf{\B{প্রাসের বিচরণকাল ও সর্বাধিক উচ্চতার সম্পর্ক:}} {\lat $gT^2 = 8H$}

\itm{13} \textbf{\B{পরন্ত বা নিক্ষিপ্ত বস্তুর শেষ বেগ, আদি বেগ ও উচ্চতার সম্পর্ক:}} {\lat $v^2 = u^2 \pm 2gh$}

\itm{14} \textbf{\B{পরন্ত বা নিক্ষিপ্ত বস্তুর উচ্চতা, আদি বেগ ও সময়ের সম্পর্ক:}} {\lat $h = ut \pm \tfrac{1}{2}gt^2$}

\itm{15} \textbf{\B{পরন্ত বা নিক্ষিপ্ত বস্তুর শেষ বেগ, আদি বেগ ও সময়ের সম্পর্ক:}} {\lat $v = u \pm gt$}

\chsub{}{নিউটনিয়ান বলবিদ্যা (অতিরিক্ত)}

\itm{1} \textbf{\B{বল (সাধারণ রূপ):}} {\lat $F = \dfrac{dp}{dt} = m\dfrac{dv}{dt} + v\dfrac{dm}{dt}$}

\itm{2} \textbf{\B{গতিশক্তি ও ভরবেগের সম্পর্ক (গতিশক্তি):}} {\lat $E_K = \dfrac{P^2}{2m}$}

\itm{3} \textbf{\B{গতিশক্তি ও ভরবেগের সম্পর্ক (ভরবেগ):}} {\lat $P = \sqrt{2mE_K}$}

\itm{4} \textbf{\B{বলের ঘাত (বল ও সময়ের গুণফল):}} {\lat $J = Ft$}

\itm{5} \textbf{\B{বলের ঘাত (ভরবেগের পরিবর্তন):}} {\lat $J = m(v-u)$}

\itm{6} \textbf{\B{ভরবেগের সংরক্ষণশীলতা নীতি (সংঘর্ষ):}} {\lat $m_1u_1 + m_2u_2 = m_1v_1 + m_2v_2$}

\itm{7} \textbf{\B{স্থিতিস্থাপক সংঘর্ষে প্রথম বস্তুর শেষ বেগ:}} {\lat $v_1 = \dfrac{(m_1-m_2)u_1 + 2m_2u_2}{m_1+m_2}$}

\itm{8} \textbf{\B{স্থিতিস্থাপক সংঘর্ষে দ্বিতীয় বস্তুর শেষ বেগ:}} {\lat $v_2 = \dfrac{(m_2-m_1)u_2 + 2m_1u_1}{m_1+m_2}$}

\itm{9} \textbf{\B{স্থিতিস্থাপক সংঘর্ষে আপেক্ষিক বেগ:}} {\lat $u_1 - u_2 = v_2 - v_1$}

\itm{10} \textbf{\B{স্থিতিস্থাপক সংঘর্ষে বেগের সমষ্টির সম্পর্ক:}} {\lat $u_1 + v_1 = u_2 + v_2$}

\itm{11} \textbf{\B{স্থিতি ঘর্ষণ গুণাঙ্ক ও ঘর্ষণ কোণ:}} {\lat $\mu_S = \dfrac{F_S}{R} = \tan\theta$}

\itm{12} \textbf{\B{গতিয় ঘর্ষণ গুণাঙ্ক:}} {\lat $\mu_K = \dfrac{F_K}{R}$}

\itm{13} \textbf{\B{রাস্তায় ব্যাংকিং কোণ (উচ্চতা ও প্রস্থ সাপেক্ষে):}} {\lat $\sin\theta = \dfrac{h}{d}$}

\itm{14} \textbf{\B{রাস্তায় ব্যাংকিং কোণ ও নিরাপদ বেগ:}} {\lat $\tan\theta = \dfrac{v^2}{rg}$}

\itm{15} \textbf{\B{ব্যাংকিং না থাকলে ঘর্ষণ গুণাঙ্ক ও নিরাপদ বেগ:}} {\lat $\mu_s = \dfrac{v^2}{rg}$}

\itm{16} \textbf{\B{জড়তার ভ্রামক:}} {\lat $I = \sum mr^2 = MK^2$}

\itm{17} \textbf{\B{চক্রগতির ব্যাসার্ধ:}} {\lat $K = \sqrt{\dfrac{I}{M}}$}

\itm{18} \textbf{\B{ঘূর্ণন গতিশক্তি:}} {\lat $E_r = \tfrac{1}{2}I\omega^2$}

\itm{19} \textbf{\B{মোট গতিশক্তি (চলন ও ঘূর্ণন):}} {\lat $E_t = \tfrac{1}{2}mv^2 + \tfrac{1}{2}I\omega^2$}

\itm{20} \textbf{\B{জড়তার ভ্রামকের লম্ব অক্ষ উপপাদ্য:}} {\lat $I_z = I_x + I_y$}

\itm{21} \textbf{\B{জড়তার ভ্রামকের সমান্তরাল অক্ষ উপপাদ্য:}} {\lat $I = I_G + Mh^2$}

\itm{22} \textbf{\B{কৌণিক বেগ:}} {\lat $\omega = 2\pi f = \dfrac{\theta}{t}$}

\itm{23} \textbf{\B{কৌণিক ভরবেগ:}} {\lat $L = I\omega = r\times p$}

\itm{24} \textbf{\B{টর্ক বা বলের ভ্রামক:}} {\lat $\tau = r\times F = I\alpha$}

\itm{25} \textbf{\B{কেন্দ্রমুখী বল:}} {\lat $F = \dfrac{mv^2}{r} = m\omega^2 r$}

\itm{26} \textbf{\B{কেন্দ্রমুখী ত্বরণ:}} {\lat $a_c = \dfrac{v^2}{r} = \omega^2 r$}

\itm{27} \textbf{\B{স্পর্শকীয় ত্বরণ:}} {\lat $a_t = \alpha r$}

\itm{28} \textbf{\B{লব্ধি ত্বরণ:}} {\lat $a = \sqrt{a_c^2 + a_t^2}$}

\itm{29} \textbf{\B{রকেটের ঊর্ধ্বমুখী ধাক্কা:}} {\lat $F_r = V_r\dfrac{dm}{dt}$}

\itm{30} \textbf{\B{রকেটের লব্ধি ত্বরণ:}} {\lat $a = \dfrac{V_r}{M}\dfrac{dm}{dt} - g$}

\itm{31} \textbf{\B{যেকোনো সময়ে রকেটের বেগ:}} {\lat $v = u - gt + V_r\ln\left(\dfrac{m_0}{M}\right)$}

\itm{32} \textbf{\B{লিফটের প্রতিক্রিয়া বল / আপাত ওজন:}} {\lat $R = m(g \pm a)$}

\itm{33} \textbf{\B{কৌণিক গতির প্রথম সমীকরণ:}} {\lat $\omega = \omega_0 + \alpha t$}

\itm{34} \textbf{\B{কৌণিক গতির দ্বিতীয় সমীকরণ:}} {\lat $\omega^2 = \omega_0^2 + 2\alpha\theta$}

\itm{35} \textbf{\B{কৌণিক গতির তৃতীয় সমীকরণ:}} {\lat $\theta = \omega_0 t + \tfrac{1}{2}\alpha t^2$}

\itm{36} \textbf{\B{উলম্ব বৃত্তে ঘূর্ণনে সর্বোচ্চ টান:}} {\lat $T = \dfrac{mv^2}{r} - mg$}

\itm{37} \textbf{\B{উলম্ব বৃত্তে ঘূর্ণনে সর্বনিম্ন টান:}} {\lat $T = \dfrac{mv^2}{r} + mg$}

\itm{38} \textbf{\B{উলম্ব বৃত্তে ঘূর্ণনে যেকোনো বিন্দুতে টান:}} {\lat $T = \dfrac{mv^2}{r} + mg\cos\theta$}

\chsub{}{কাজ, শক্তি ও ক্ষমতা (অতিরিক্ত)}

\itm{1} \textbf{\B{কৃতকাজ (ধ্রুব বল দ্বারা):}} {\lat $W = \vec F \cdot \vec S = FS \cos\theta$}

\itm{2} \textbf{\B{কৃতকাজ (ভর, ত্বরণ ও সরণ সাপেক্ষে):}} {\lat $W = mas$}

\itm{3} \textbf{\B{পরিবর্তনশীল বল দ্বারা কৃতকাজ:}} {\lat $W = \int F(x) \, dx$}

\itm{4} \textbf{\B{গতিশক্তি:}} {\lat $E_K = \tfrac{1}{2}mv^2$}

\itm{5} \textbf{\B{গতিশক্তি ও ভরবেগের সম্পর্ক:}} {\lat $E_K = \dfrac{p^2}{2m}$}

\itm{6} \textbf{\B{স্থিতিশক্তি / বিভবশক্তি (অভিকর্ষজ):}} {\lat $E_P = mgh$}

\itm{7} \textbf{\B{মহাকর্ষীয় বিভবশক্তি:}} {\lat $E_P = -\dfrac{GMm}{r}$}

\itm{8} \textbf{\B{স্প্রিং ধ্রুবক:}} {\lat $K = \dfrac{F}{x}$}

\itm{9} \textbf{\B{স্প্রিং-এর সঞ্চিত শক্তি / কৃতকাজ:}} {\lat $W = \tfrac{1}{2}Kx^2 = \tfrac{1}{2}Fx$}

\itm{10} \textbf{\B{স্প্রিং-এর সরণ পরিবর্তনের ফলে কৃতকাজ:}} {\lat $W = \tfrac{1}{2}K(x_f^2-x_i^2)$}

\itm{11} \textbf{\B{স্প্রিং সমান $n$ ভাগে বিভাজনের ক্ষেত্রে স্প্রিং ধ্রুবক:}} {\lat $K' = nK$}

\itm{12} \textbf{\B{স্প্রিংকে $m:n$ অনুপাতে বিভাজনের ক্ষেত্রে $m$ অংশের স্প্রিং ধ্রুবক:}} {\lat $K_m = \dfrac{m+n}{m}K$}

\itm{13} \textbf{\B{স্প্রিংকে $m:n$ অনুপাতে বিভাজনের ক্ষেত্রে $n$ অংশের স্প্রিং ধ্রুবক:}} {\lat $K_n = \dfrac{m+n}{n}K$}

\itm{14} \textbf{\B{স্প্রিং-এর শ্রেণি সমবায়:}} {\lat $\dfrac{1}{K_s} = \sum \dfrac{1}{K_i}$}

\itm{15} \textbf{\B{স্প্রিং-এর সমান্তরাল সমবায়:}} {\lat $K_p = \sum K_i$}

\itm{16} \textbf{\B{মহাকর্ষ বলের বিরুদ্ধে কৃতকাজ:}} {\lat $W = GMm\left(\dfrac{1}{r_1}-\dfrac{1}{r_2}\right)$}

\itm{17} \textbf{\B{কাজ-শক্তি উপপাদ্য:}} {\lat $W = \tfrac{1}{2}m(v^2-u^2)$}

\itm{18} \textbf{\B{ক্ষমতা (সাধারণ সূত্র):}} {\lat $P = \dfrac{W}{t}$}

\itm{19} \textbf{\B{ক্ষমতা (বল ও বেগ সাপেক্ষে):}} {\lat $P = F \cdot V$}

\itm{20} \textbf{\B{ক্ষমতা (টর্ক ও কৌণিক বেগ সাপেক্ষে):}} {\lat $P = \tau\omega$}

\itm{21} \textbf{\B{ক্ষমতা (কম্পাঙ্ক ও সময় সাপেক্ষে):}} {\lat $P = 2\pi ft$}

\itm{22} \textbf{\B{তাৎক্ষণিক ক্ষমতা:}} {\lat $P = \dfrac{dW}{dt}$}

\itm{23} \textbf{\B{কুয়ার মোটর খালি করার ক্ষমতা:}} {\lat $P = \dfrac{\pi r^2 h\rho gh}{t}$}

\itm{24} \textbf{\B{কুয়া খালি করার ক্ষেত্রে গড় গভীরতা / ভরকেন্দ্রের সরণ:}} {\lat $h = \text{\text{\B{খালি}}} + \dfrac{\text{\text{\B{ভরা}}}}{2}$}

\itm{25} \textbf{\B{কর্মদক্ষতা (ক্ষমতা সাপেক্ষে):}} {\lat $\eta = \dfrac{P_{out}}{P_{in}}$}

\itm{26} \textbf{\B{কর্মদক্ষতা (কাজ সাপেক্ষে):}} {\lat $\eta = \dfrac{W_{out}}{W_{in}}$}

\itm{27} \textbf{\B{কর্মদক্ষতা (শক্তি সাপেক্ষে):}} {\lat $\eta = \dfrac{E_{out}}{E_{in}}$}

\itm{28} \textbf{\B{অশ্বক্ষমতা (HP) ও ওয়াট (W) এর সম্পর্ক:}} {\lat $1\,\text{HP} = 746\,\text{W}$}

\itm{29} \textbf{\B{যে উচ্চতায় গতিশক্তি বিভবশক্তির $n$ গুণ ($E_K=nE_P$):}} {\lat $x = \dfrac{h}{n+1}$}

\itm{30} \textbf{\B{যে উচ্চতায় বিভবশক্তি গতিশক্তির $n$ গুণ ($E_P=nE_K$):}} {\lat $x = \dfrac{nh}{n+1}$}

\itm{31} \textbf{\B{ঘনকাকৃতির স্তম্ভ একটির ওপর আরেকটি সাজাতে কৃতকাজ:}} {\lat $W = \dfrac{n(n-1)}{2}mgh$}

\itm{32} \textbf{\B{তক্তা ভেদ করার ক্ষেত্রে অতিক্রান্ত দূরত্ব বা অবশিষ্ট সরণ (বেগ $v=u/n$ হলে):}} {\lat $x = \dfrac{s}{n^2-1}$}

\itm{33} \textbf{\B{প্রবেশযোগ্য তক্তা সংখ্যার সাথে বেগের সম্পর্ক:}} {\lat $v^2 \propto \text{\B{\text{\B{তক্তা সংখ্যা}}}}$}

\itm{34} \textbf{\B{হাতুড়ি-পেরেক সংক্রান্ত গড় প্রতিরোধ্য বল (গতিশক্তি ও বিভবশক্তি সহ):}} {\lat $F = \dfrac{\tfrac{1}{2}mv^2+mgx}{x}$}

\itm{35} \textbf{\B{হাতুড়ি-পেরেক সংক্রান্ত গড় প্রতিরোধ্য বল (শুধুমাত্র গতিশক্তি বিবেচনায়):}} {\lat $F = \dfrac{\tfrac{1}{2}mv^2}{x}$}

\itm{36} \textbf{\B{হাতুড়ি-পেরেক সংক্রান্ত গড় প্রতিরোধ্য বল (নির্দিষ্ট উচ্চতা $h$ থেকে পতনের ক্ষেত্রে):}} {\lat $F = \dfrac{mg(h+x)}{x}$}

\itm{37} \textbf{\B{হাতুড়ি-পেরেক সংক্রান্ত গড় প্রতিরোধ্য বল (বিভবশক্তি বিয়োগের ক্ষেত্রে):}} {\lat $F = \dfrac{\tfrac{1}{2}mv^2-mgx}{x}$}

\itm{38} \textbf{\B{$h$ উচ্চতা থেকে $x\%$ শক্তি হারিয়ে $n$ বার বাউন্সের পর উচ্চতা:}} {\lat $h_n = \left(1-\dfrac{x}{100}\right)^n h$}

\chsub{}{মহাকর্ষ ও অভিকর্ষ (অতিরিক্ত)}

\itm{1} \textbf{\B{মহাকর্ষীয় বল:}} {\lat $F = \dfrac{Gm_1m_2}{r^2}$}

\itm{2} \textbf{\B{ভূপৃষ্ঠে অভিকর্ষজ ত্বরণ:}} {\lat $g = \dfrac{GM}{R^2}$}

\itm{3} \textbf{\B{উচ্চতায় অভিকর্ষজ ত্বরণ (প্রকৃত সূত্র):}} {\lat $g_h = \dfrac{gR^2}{(R+h)^2}$}

\itm{4} \textbf{\B{উচ্চতায় অভিকর্ষজ ত্বরণ (আসন্ন সূত্র):}} {\lat $g_h \approx g\left(1-\dfrac{2h}{R}\right)$}

\itm{5} \textbf{\B{অভিকর্ষজ ত্বরণ $n$ গুণ হ্রাস পেলে উচ্চতা:}} {\lat $h = (\sqrt{n}-1)R$}

\itm{6} \textbf{\B{গভীরতায় অভিকর্ষজ ত্বরণ (সাধারণ সূত্র):}} {\lat $g_d = \left(1-\dfrac{d}{R}\right)g$}

\itm{7} \textbf{\B{গভীরতায় অভিকর্ষজ ত্বরণ (ঘনত্ব সাপেক্ষে):}} {\lat $g_d = \tfrac{4}{3}\pi\rho G(R-d)$}

\itm{8} \textbf{\B{নির্দিষ্ট অক্ষাংশে অভিকর্ষজ ত্বরণ:}} {\lat $g_\lambda = g - \omega^2 R\cos^2\lambda$}

\itm{9} \textbf{\B{মেরু অঞ্চলে অভিকর্ষজ ত্বরণ:}} {\lat $g_\lambda = g$}

\itm{10} \textbf{\B{বিষুব অঞ্চলে অভিকর্ষজ ত্বরণ:}} {\lat $g_\lambda = g - \omega^2 R$}

\itm{11} \textbf{\B{মহাকর্ষীয় প্রাবল্য:}} {\lat $E = \dfrac{F}{m} = \dfrac{GM}{r^2}$}

\itm{12} \textbf{\B{মহাকর্ষীয় বিভব:}} {\lat $V = -\dfrac{GM}{r}$}

\itm{13} \textbf{\B{মহাকর্ষীয় স্থিতিশক্তি:}} {\lat $U = -\dfrac{GMm}{r}$}

\itm{14} \textbf{\B{পড়ন্ত বস্তুর দ্বিতীয় সূত্র:}} {\lat $\dfrac{v_1}{v_2} = \dfrac{t_1}{t_2}$}

\itm{15} \textbf{\B{পড়ন্ত বস্তুর তৃতীয় সূত্র:}} {\lat $\dfrac{h_1}{h_2} = \dfrac{t_1^2}{t_2^2}$}

\itm{16} \textbf{\B{পড়ন্ত বস্তুর বেগ ও উচ্চতার সম্পর্ক:}} {\lat $\dfrac{v_1^2}{v_2^2} = \dfrac{h_1}{h_2}$}

\itm{17} \textbf{\B{কেপলারের তৃতীয় সূত্র (আবর্তনকাল):}} {\lat $T^2 \propto r^3$}

\itm{18} \textbf{\B{কেপলারের দ্বিতীয় সূত্র (ক্ষেত্রফলীয় বেগ):}} {\lat $\dfrac{dA}{dt} = \dfrac{L}{2m}$}

\itm{19} \textbf{\B{কেপলারের দ্বিতীয় সূত্র (ধ্রুবক রূপ):}} {\lat $\dfrac{A_i}{t_i} = \text{\B{\text{\B{ধ্রুব}}}}$}

\itm{20} \textbf{\B{অনুসূর ও অপসূর বিন্দুতে বেগ ও দূরত্বের সম্পর্ক:}} {\lat $v_1r_1 = v_2r_2$}

\itm{21} \textbf{\B{কৃত্রিম উপগ্রহের কক্ষীয় বেগ:}} {\lat $v = \sqrt{\dfrac{GM}{R+h}} = \sqrt{\dfrac{gR^2}{R+h}}$}

\itm{22} \textbf{\B{কৃত্রিম উপগ্রহের আবর্তনকাল:}} {\lat $T = 2\pi(R+h)\sqrt{\dfrac{R+h}{GM}}$}

\itm{23} \textbf{\B{কৃত্রিম উপগ্রহের উচ্চতা:}} {\lat $h = \left(\dfrac{GMT^2}{4\pi^2}\right)^{1/3}-R$}

\itm{24} \textbf{\B{কৃত্রিম উপগ্রহের গতিশক্তি:}} {\lat $E_k = \dfrac{GMm}{2(R+h)}$}

\itm{25} \textbf{\B{কৃত্রিম উপগ্রহের বিভবশক্তি:}} {\lat $E_p = -\dfrac{GMm}{R+h}$}

\itm{26} \textbf{\B{কৃত্রিম উপগ্রহের মোট শক্তি:}} {\lat $E = -\dfrac{GMm}{2(R+h)}$}

\itm{27} \textbf{\B{ভূপৃষ্ঠে মুক্তিবেগ:}} {\lat $v_e = \sqrt{\dfrac{2GM}{R}} = \sqrt{2gR}$}

\itm{28} \textbf{\B{$h$ উচ্চতায় মুক্তিবেগ:}} {\lat $v_e = \sqrt{\dfrac{2GM}{R+h}}$}

\itm{29} \textbf{\B{ভূপৃষ্ঠের নিকটবর্তী উপগ্রহের পর্যায়কালের বর্গ:}} {\lat $T^2 = \dfrac{4\pi^2}{GM}R^3$}

\itm{30} \textbf{\B{মহাকর্ষীয় বলের ভেক্টর রূপ:}} {\lat $\vec F_{21} = -\dfrac{Gm_1m_2\vec r_{12}}{r_{12}^3}$}

\itm{31} \textbf{\B{উৎক্ষেপণ বেগ $v^2 < \dfrac{v_e^2}{2}$ হলে কক্ষপথ:}} \B{উপবৃত্তাকার (ভূপৃষ্ঠে ফিরে আসবে)}

\itm{32} \textbf{\B{উৎক্ষেপণ বেগ $v^2 = \dfrac{v_e^2}{2}$ হলে কক্ষপথ:}} \B{বৃত্তাকার}

\itm{33} \textbf{\B{উৎক্ষেপণ বেগ $\dfrac{v_e^2}{2} < v^2 < v_e^2$ হলে কক্ষপথ:}} \B{উপবৃত্তাকার}

\itm{34} \textbf{\B{উৎক্ষেপণ বেগ $v^2 = v_e^2$ হলে কক্ষপথ:}} \B{পরাবৃত্তাকার (মুক্তি পাবে)}

\itm{35} \textbf{\B{ওজনহীনতার জন্য পৃথিবীর প্রয়োজনীয় কৌণিক বেগ:}} {\lat $\omega = \sqrt{\dfrac{g}{R}}$}

\itm{36} \textbf{\B{পৃথিবীর ব্যাস বরাবর সুড়ঙ্গে বস্তুর দোলনকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{R}{g}}$}

\itm{37} \textbf{\B{নিরেট গোলকের অভ্যন্তরে বিভব:}} {\lat $V = -\dfrac{GM(3a^2-r^2)}{2a^3}$}

\itm{38} \textbf{\B{নিরেট গোলকের অভ্যন্তরে প্রাবল্য:}} {\lat $E = \dfrac{GMr}{a^3}$}

\itm{39} \textbf{\B{পুরু ফাঁপা গোলকের অভ্যন্তরে বিভব:}} {\lat $V = -2\pi G\rho(a^2-r^2)$}

\itm{40} \textbf{\B{পুরু ফাঁপা গোলকের অভ্যন্তরে প্রাবল্য:}} {\lat $E = 0$}

\itm{41} \textbf{\B{পুরু ফাঁপা গোলকের দেয়ালের পুরুত্বের অভ্যন্তরে প্রাবল্য:}} {\lat $E = \dfrac{GM(r^3-b^3)}{r^2(a^3-b^3)}$}

\chsub{}{পদার্থের গাঠনিক ধর্ম (অতিরিক্ত)}

\itm{1} \textbf{\B{হুকের সূত্র:}} \B{পীড়ন / বিকৃতি = ধ্রুব}

\itm{2} \textbf{\B{পীড়ন:}} {\lat $P = \dfrac{F}{A} = \rho lg$}

\itm{3} \textbf{\B{ইয়ং-এর গুণাঙ্ক:}} {\lat $Y = \dfrac{FL}{Al} = \dfrac{mgL}{\pi r^2 l}$}

\itm{4} \textbf{\B{আয়তন গুণাঙ্ক:}} {\lat $K = \dfrac{PV}{v}$}

\itm{5} \textbf{\B{সংনম্যতা:}} {\lat $c = \dfrac{1}{K}$}

\itm{6} \textbf{\B{পয়সনের অনুপাত:}} {\lat $\sigma = \dfrac{dr/r}{dl/l}$}

\itm{7} \textbf{\B{পয়সনের অনুপাতের তাত্ত্বিক সীমা:}} {\lat $-1 < \sigma < 1/2$}

\itm{8} \textbf{\B{পয়সনের অনুপাতের বাস্তব সীমা:}} {\lat $0 < \sigma < 1/2$}

\itm{9} \textbf{\B{ধাতুর ক্ষেত্রে পয়সনের অনুপাত:}} {\lat $0.2 < \sigma < 0.4$}

\itm{10} \textbf{\B{কৃন্তন বিকৃতি:}} {\lat $\theta = \dfrac{x}{h}$}

\itm{11} \textbf{\B{কৃন্তন গুণাঙ্ক / দৃঢ়তার গুণাঙ্ক:}} {\lat $\eta = \dfrac{F}{A\theta}$}

\itm{12} \textbf{\B{দৈর্ঘ্য প্রসারণে কৃতকাজ:}} {\lat $W = \tfrac{1}{2}\dfrac{YAl^2}{L} = \tfrac{1}{2}Fl$}

\itm{13} \textbf{\B{প্রতি একক আয়তনে সঞ্চিত শক্তি:}} {\lat $U = \tfrac{1}{2}\times$ \B{পীড়ন} $\times$ \B{বিকৃতি} $= \tfrac{1}{2}Y(\text{\B{\text{\B{বিকৃতি}}}})^2$}

\itm{14} \textbf{\B{আয়তন বিকৃতিতে কৃতকাজ:}} {\lat $W = \tfrac{1}{2}\dfrac{Bv^2}{V}$}

\itm{15} \textbf{\B{কৃন্তন বিকৃতিতে কৃতকাজ:}} {\lat $W = \tfrac{1}{2}\dfrac{\eta Ax^2}{h}$}

\itm{16} \textbf{\B{পৃষ্ঠটান:}} {\lat $T = \dfrac{F}{l}$}

\itm{17} \textbf{\B{সাবানের ফিল্মের পৃষ্ঠটান:}} {\lat $T = \dfrac{F}{2l}$}

\itm{18} \textbf{\B{কৈশিক নলে পৃষ্ঠটান (সূক্ষ্ম সমীকরণ):}} {\lat $T = \dfrac{hg\left(r+\dfrac{r}{3}\right)}{2\cos\theta}$}

\itm{19} \textbf{\B{কৈশিক নলে পৃষ্ঠটান (সাধারণ সমীকরণ):}} {\lat $T \approx \dfrac{hgr}{2\cos\theta}$}

\itm{20} \textbf{\B{পৃষ্ঠটানের দরুন উর্ধ্বমুখী বল:}} {\lat $F = 2\pi rT\cos\theta$}

\itm{21} \textbf{\B{পৃষ্ঠটানের ওপর তাপমাত্রার প্রভাব:}} {\lat $T_t = T_0(1-\alpha t)$}

\itm{22} \textbf{\B{তরল ফোঁটার অভ্যন্তরে অতিরিক্ত চাপ:}} {\lat $\Delta p = \dfrac{2T}{R}$}

\itm{23} \textbf{\B{সাবান বুদবুদের অভ্যন্তরে অতিরিক্ত চাপ:}} {\lat $\Delta p = \dfrac{4T}{R}$}

\itm{24} \textbf{\B{সান্দ্রবল (নিউটনীয় সমীকরণ):}} {\lat $F = \eta A \dfrac{dv}{dy}$}

\itm{25} \textbf{\B{স্টোকসের সূত্র (সান্দ্রবল):}} {\lat $F = 6\pi\eta r v_t$}

\itm{26} \textbf{\B{প্রান্তবেগ / টার্মিনাল বেগ:}} {\lat $v_t = \tfrac{2}{9}\dfrac{r^2(\rho-\sigma)g}{\eta}$}

\itm{27} \textbf{\B{গ্যাসের সান্দ্রতার সাথে তাপমাত্রার সম্পর্ক:}} {\lat $\eta \propto \sqrt{T}$}

\itm{28} \textbf{\B{তরলের সান্দ্রতার সাথে তাপমাত্রার সম্পর্ক:}} {\lat $\log\eta = A + \dfrac{B}{T}$}

\itm{29} \textbf{\B{ক্ষুদ্র ফোঁটা একীভবনে বড় ফোঁটার ব্যাসার্ধ:}} {\lat $R = rN^{1/3}$}

\itm{30} \textbf{\B{তরল ফোঁটা ভেঙে ক্ষুদ্র ফোঁটায় পরিণত করতে কৃতকাজ:}} {\lat $W = 4\pi(Nr^2-R^2)T$}

\itm{31} \textbf{\B{সাবান বুদবুদের ক্ষেত্রে কৃতকাজ:}} {\lat $W = 8\pi(R^2-r^2)T$}

\itm{32} \textbf{\B{পৃষ্ঠশক্তি:}} {\lat $E = \dfrac{W}{\Delta A}$}

\chsub{}{পর্যায়বৃত্ত গতি (অতিরিক্ত)}

\itm{1} \textbf{\B{সাম্যাবস্থানে ($x = 0$ বিন্দুতে) সর্বোচ্চ বেগ:}} {\lat $v = V_{\max} = \omega A$}

\itm{2} \textbf{\B{সাম্যাবস্থানে ($x = 0$ বিন্দুতে) সর্বনিম্ন ত্বরণ:}} {\lat $a = 0$}

\itm{3} \textbf{\B{সর্বোচ্চ বিস্তারে ($x = A$ বিন্দুতে) সর্বনিম্ন বেগ:}} {\lat $v = 0$}

\itm{4} \textbf{\B{সর্বোচ্চ বিস্তারে ($x = A$ বিন্দুতে) সর্বোচ্চ ত্বরণ (মান):}} {\lat $a = a_{\max} = \omega^2 A$}

\itm{5} \textbf{\B{স্প্রিং এর শ্রেণি সমবায়:}} {\lat $\dfrac{1}{K_s} = \dfrac{1}{K_1} + \dfrac{1}{K_2} + \dots + \dfrac{1}{K_n}$}

\itm{6} \textbf{\B{স্প্রিং এর সমান্তরাল সমবায়:}} {\lat $K_p = K_1 + K_2 + \dots + K_n$}

\itm{7} \textbf{\B{লিফট ত্বরণে উপরে উঠলে দোলনকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{L}{g+a}}$}

\itm{8} \textbf{\B{লিফট ত্বরণে নিচে নামলে দোলনকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{L}{g-a}}$}

\itm{9} \textbf{\B{দোলনকাল নির্দিষ্ট শতাংশ বৃদ্ধি করতে পরিবর্তিত কার্যকর দৈর্ঘ্য:}} {\lat $L_2 = \left(1+\dfrac{x}{100}\right)^2 L_1$}

\itm{10} \textbf{\B{নির্দিষ্ট কোণে ছেড়ে দিলে অন্য অবস্থানে দোলকের বেগ:}} {\lat $v = \sqrt{2gL(\cos\theta_2-\cos\theta_1)}$}

\itm{11} \textbf{\B{দষা পার্থক্য, পথ পার্থক্য ও সময় পার্থক্যের সম্পর্ক:}} {\lat $\dfrac{\Delta\delta}{2\pi} = \dfrac{\Delta x}{\lambda} = \dfrac{\Delta t}{T}$}

\itm{12} \textbf{\B{লব্ধি তরঙ্গের বিস্তার:}} {\lat $A = \sqrt{A_1^2+A_2^2+2A_1A_2\cos\delta}$}

\itm{13} \textbf{\B{পাহাড়ের উচ্চতা নির্ণয়:}} {\lat $h = \left(\dfrac{T'}{T}-1\right)R$}

\itm{14} \textbf{\B{খনির গভীরতা নির্ণয়:}} {\lat $d = \left(1-\dfrac{T^2}{T_d^2}\right)R$}

\itm{15} \textbf{\B{দোলকঘড়ি নির্দিষ্ট সেকেন্ড ধীরে চললে দোলনকাল:}} {\lat $T = \dfrac{86400\times 2}{86400-n}$}

\itm{16} \textbf{\B{দোলকঘড়ি নির্দিষ্ট সেকেন্ড দ্রুত চললে দোলনকাল:}} {\lat $T = \dfrac{86400\times 2}{86400+n}$}

\itm{17} \textbf{\B{পৃথিবী ও চাঁদে দোলনকালের সম্পর্ক:}} {\lat $\dfrac{T_m}{T_e} = \sqrt{\dfrac{g_e}{g_m}}$}

\chsub{}{তরঙ্গ (অতিরিক্ত)}

\itm{1} \textbf{\B{তরঙ্গের বেগ, কম্পাঙ্ক ও তরঙ্গদৈর্ঘ্যের সম্পর্ক:}} {\lat $V = n\lambda$}

\itm{2} \textbf{\B{পর্যায়কাল ও কম্পাঙ্কের সম্পর্ক:}} {\lat $T = \dfrac{1}{n}$}

\itm{3} \textbf{\B{একই সুরশলাকার ক্ষেত্রে বিভিন্ন মাধ্যমে বেগ ও তরঙ্গদৈর্ঘ্যের সম্পর্ক:}} {\lat $\dfrac{V_1}{V_2} = \dfrac{\lambda_1}{\lambda_2}$}

\itm{4} \textbf{\B{একই মাধ্যমে বিভিন্ন তরঙ্গের তরঙ্গদৈর্ঘ্য ও কম্পাঙ্কের সম্পর্ক:}} {\lat $\dfrac{\lambda_1}{\lambda_2} = \dfrac{n_2}{n_1}$}

\itm{5} \textbf{\B{অগ্রগামী তরঙ্গের সমীকরণ:}} {\lat $y = A\sin(\omega t - x) = A\sin\tfrac{2\pi}{\lambda}(vt - x)$}

\itm{6} \textbf{\B{তরঙ্গের তীব্রতা ও বিস্তারের সম্পর্ক:}} {\lat $I \propto a^2$}

\itm{7} \textbf{\B{তরঙ্গের তীব্রতার সাধারণ সমীকরণ:}} {\lat $I = 2\pi^2 n^2 A^2 \rho v$}

\itm{8} \textbf{\B{গোলকাকার উৎস হতে নির্গত তরঙ্গের তীব্রতা ও দূরত্বের সম্পর্ক:}} {\lat $I = \dfrac{P}{4\pi r^2}$}

\itm{9} \textbf{\B{শব্দের তীব্রতা লেভেল (শব্দোচ্চতা):}} {\lat $\beta = 10\log\left(\dfrac{I}{I_0}\right) \text{ dB}$}

\itm{10} \textbf{\B{বীটের পর্যায়কাল:}} {\lat $T = \dfrac{1}{n_1 \sim n_2}$}

\itm{11} \textbf{\B{প্রতি সেকেন্ডে উৎপন্ন বীট সংখ্যা:}} {\lat $N = n_1 \sim n_2$}

\itm{12} \textbf{\B{টানটান তারের আড় কম্পনের মৌলিক কম্পাঙ্ক:}} {\lat $n = \dfrac{1}{2l}\sqrt{\dfrac{T}{m}}$}

\itm{13} \textbf{\B{তারের ব্যাসার্ধ ও ঘনত্বের সাপেক্ষে আড় কম্পনের কম্পাঙ্ক:}} {\lat $n = \dfrac{1}{2lr}\sqrt{\dfrac{T}{\pi\rho}}$}

\itm{14} \textbf{\B{একমুখ বন্ধ নলে উৎপন্ন তরঙ্গের কম্পাঙ্ক:}} {\lat $N_n = \dfrac{v(2n+1)}{4l}$}

\itm{15} \textbf{\B{একমুখ বন্ধ নলে উৎপন্ন তরঙ্গের তরঙ্গদৈর্ঘ্য:}} {\lat $\lambda_n = \dfrac{4l}{2n+1}$}

\itm{16} \textbf{\B{খোলামুখ নলে উৎপন্ন তরঙ্গের কম্পাঙ্ক:}} {\lat $N_n = \dfrac{v(n+1)}{2l}$}

\itm{17} \textbf{\B{খোলামুখ নলে উৎপন্ন তরঙ্গের তরঙ্গদৈর্ঘ্য:}} {\lat $\lambda_n = \dfrac{2l}{n+1}$}

\itm{18} \textbf{\B{তরঙ্গের শক্তি ঘনত্ব (একক আয়তনে শক্তি):}} {\lat $E = 2\pi^2\rho n^2 a^2$}


\chsub{}{আদর্শ গ্যাস (অতিরিক্ত)}

\itm{1} \textbf{\B{বয়েলের সূত্র:}} {\lat $P_1V_1 = P_2V_2$}

\itm{2} \textbf{\B{চার্লসের সূত্র:}} {\lat $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$}

\itm{3} \textbf{\B{চাপীয় সূত্র বা গেইলুসাকের সূত্র:}} {\lat $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$}

\itm{4} \textbf{\B{স্থির চাপে তাপমাত্রা বৃদ্ধিতে আয়তনের সমীকরণ:}} {\lat $V_\theta = V_0(1+\gamma_p\Delta\theta)$}

\itm{5} \textbf{\B{স্থির আয়তনে তাপমাত্রা বৃদ্ধিতে চাপের সমীকরণ:}} {\lat $P_\theta = P_0(1+\gamma_v\Delta\theta)$}

\itm{6} \textbf{\B{আদর্শ গ্যাসের অবস্থার সমীকরণ:}} {\lat $PV = nRT$}

\itm{7} \textbf{\B{গ্যাসের মোল সংখ্যা নির্ণয়:}} {\lat $n = \dfrac{w}{M} = \dfrac{PV}{RT}$}

\itm{8} \textbf{\B{বাস্তব গ্যাসের জন্য ভ্যান্ডার ওয়ালস সমীকরণ:}} {\lat $\left(P + \dfrac{n^2a}{V^2}\right)(V - nb) = nRT$}

\itm{9} \textbf{\B{গ্যাসের অণুর গড় বর্গবেগের বর্গমূল (RMS বেগ):}} {\lat $C_{rms} = \sqrt{\dfrac{3RT}{M}} = \sqrt{\dfrac{3kT}{m}} = \sqrt{\dfrac{3P}{\rho}}$}

\itm{10} \textbf{\B{গ্যাসের অণুর গড় বেগ:}} {\lat $C_{avg} = \sqrt{\dfrac{8RT}{\pi M}}$}

\itm{11} \textbf{\B{গ্যাসের অণুর সবচেয়ে সম্ভাব্য বেগ:}} {\lat $C_{mp} = \sqrt{\dfrac{2RT}{M}}$}

\itm{12} \textbf{\B{গ্যাসের বিভিন্ন বেগের অনুপাত:}} {\lat $C_{rms} : C_{avg} : C_{mp} = 1.22 : 1.12 : 1$}

\itm{13} \textbf{\B{গ্যাসের চাপের সমীকরণ:}} {\lat $P = \dfrac{1}{3}\rho c^2$}

\itm{14} \textbf{\B{চাপ ও একক আয়তনে গতিশক্তির সম্পর্ক:}} {\lat $P = \dfrac{2}{3}E_K$}

\itm{15} \textbf{\B{$n$ মোল গ্যাসের মোট গতিশক্তি:}} {\lat $E_K = \dfrac{f}{2}nRT$}

\itm{16} \textbf{\B{১টি গ্যাস অণুর গতিশক্তি:}} {\lat $E_K = \dfrac{f}{2}kT$}

\itm{17} \textbf{\B{গ্যাস মিশ্রণের লব্ধি চাপ:}} {\lat $P = \dfrac{P_1V_1 + P_2V_2}{V_1 + V_2}$}

\itm{18} \textbf{\B{এক-পরমাণুক গ্যাসের স্বাধীনতার মাত্রা:}} {\lat $f = 3$}

\itm{19} \textbf{\B{দ্বি-পরমাণুক গ্যাসের স্বাধীনতার মাত্রা:}} {\lat $f = 5$}

\itm{20} \textbf{\B{বহু-পরমাণুক গ্যাসের স্বাধীনতার মাত্রা:}} {\lat $f = 6$}

\itm{21} \textbf{\B{ম্যাক্সওয়েলের গড় মুক্তপথ:}} {\lat $\lambda = \dfrac{1}{\sqrt2 n\pi\sigma^2}$}

\itm{22} \textbf{\B{ক্রুসিয়াসের গড় মুক্তপথ:}} {\lat $\lambda = \dfrac{1}{n\pi\sigma^2}$}

\itm{23} \textbf{\B{বোল্টজম্যানের গড় মুক্তপথ:}} {\lat $\lambda = \dfrac{3}{4n\pi\sigma^2}$}

\itm{24} \textbf{\B{গড় মুক্তপথের সাথে চাপ, ঘনত্ব ও তাপমাত্রার সম্পর্ক:}} {\lat $\lambda \propto \dfrac{1}{P}, \; \lambda \propto \dfrac{1}{\rho}, \; \lambda \propto T$}

\itm{25} \textbf{\B{একক সময়ে অণুর গড় সংঘর্ষ বা ধাক্কার সংখ্যা:}} {\lat $N = \dfrac{1}{t_{rms}}$}

\itm{26} \textbf{\B{গ্লেশারের সূত্রের সাহায্যে শিশিরাঙ্ক নির্ণয়:}} {\lat $\theta = \theta_1 - G(\theta_1 - \theta_2)$}

\itm{27} \textbf{\B{আপেক্ষিক আর্দ্রতা:}} {\lat $R = \dfrac{f}{F} \times 100\%$}

\itm{28} \textbf{\B{বায়ু বুদবুদের আয়তন $n$ গুণ হলে হ্রদের গভীরতা:}} {\lat $h = \dfrac{(n-1)P}{\rho g}$}

\itm{29} \textbf{\B{বায়ু বুদবুদের পৃষ্ঠের ক্ষেত্রফল $n$ গুণ হলে হ্রদের গভীরতা:}} {\lat $h = \dfrac{(n^2-1)P}{\rho g}$}

\itm{30} \textbf{\B{বায়ু বুদবুদের ব্যাসার্ধ $n$ গুণ হলে হ্রদের গভীরতা:}} {\lat $h = \dfrac{(n^3-1)P}{\rho g}$}

\chsec{পরিশিষ্ট-ড: গত বছরের নোট থেকে অতিরিক্ত সূত্রসমূহ (২য় পত্র)}

\chsub{}{তাপগতিবিদ্যা (অতিরিক্ত)}

\itm{1} \textbf{\B{যেকোনো থার্মোমিটরের ক্ষেত্রে তাপমাত্রা পরিমাপের সাধারণ সমীকরণ:}} {\lat $\theta = \dfrac{X_\theta - X_{ice}}{X_{steam} - X_{ice}} \times N + \theta_{ice}$}

\itm{2} \textbf{\B{পানির ত্রৈধ বিন্দুর সাপেক্ষে তাপমাত্রা নির্ণয়:}} {\lat $T = \dfrac{X_T}{X_{tp}} \times 273.16$}

\itm{3} \textbf{\B{বিভিন্ন তাপমাত্রা স্কেলের মধ্যে পারস্পরিক সম্পর্ক:}} {\lat $\dfrac{C}{5} = \dfrac{F-32}{9} = \dfrac{K-273}{5} = \dfrac{R_n-491.67}{9} = \dfrac{R}{4}$}

\itm{4} \textbf{\B{ত্রুটিপূর্ণ থার্মোমিটারের সমীকরণ (সঠিক স্কেলের সাথে সম্পর্ক):}} {\lat $\dfrac{S-M}{B-M} = \dfrac{C}{100} = \dfrac{F-32}{180} = \dfrac{K-273}{100}$}

\itm{5} \textbf{\B{অভ্যন্তরীণ শক্তির পরিবর্তন:}} {\lat $dU = \tfrac{f}{2}nRT$}

\itm{6} \textbf{\B{তাপগতিবিদ্যার প্রথম সূত্র:}} {\lat $dQ = dU + dW$}

\itm{7} \textbf{\B{সমচাপ প্রক্রিয়ায় সম্পাদিত কাজ:}} {\lat $dW = PdV = nRdT$}

\itm{8} \textbf{\B{সমচাপ প্রক্রিয়ায় এনট্রপির পরিবর্তন:}} {\lat $dS = nC_p\ln\left(\dfrac{T_2}{T_1}\right)$}

\itm{9} \textbf{\B{সমআয়তন প্রক্রিয়ায় সম্পাদিত কাজ:}} {\lat $dW = 0$}

\itm{10} \textbf{\B{সমআয়তন প্রক্রিয়ায় গৃহিত বা বর্জিত তাপ:}} {\lat $dQ = nC_v dT$}

\itm{11} \textbf{\B{সমআয়তন প্রক্রিয়ায় এনট্রপির পরিবর্তন:}} {\lat $dS = nC_v\ln\left(\dfrac{T_2}{T_1}\right)$}

\itm{12} \textbf{\B{সমোষ্ণ প্রক্রিয়ায় সম্পাদিত কাজ:}} {\lat $dW = nRT\ln\left(\dfrac{V_2}{V_1}\right)$}

\itm{13} \textbf{\B{সমোষ্ণ প্রক্রিয়ায় এনট্রপির পরিবর্তন:}} {\lat $dS = nR\ln\left(\dfrac{V_2}{V_1}\right)$}

\itm{14} \textbf{\B{রুদ্ধতাপীয় প্রক্রিয়ায় চাপ ও আয়তনের সম্পর্ক:}} {\lat $PV^\gamma = \text{\text{\B{ধ্রুব}}}$}

\itm{15} \textbf{\B{রুদ্ধতাপীয় প্রক্রিয়ায় তাপমাত্রা ও আয়তনের সম্পর্ক:}} {\lat $TV^{\gamma-1} = \text{\text{\B{ধ্রুব}}}$}

\itm{16} \textbf{\B{রুদ্ধতাপীয় প্রক্রিয়ায় সম্পাদিত কাজ:}} {\lat $W = \dfrac{nR(T_1 - T_2)}{\gamma - 1} = \dfrac{P_1V_1 - P_2V_2}{\gamma - 1}$}

\itm{17} \textbf{\B{রুদ্ধতাপীয় প্রক্রিয়ায় এনট্রপির পরিবর্তন:}} {\lat $dS = 0$}

\itm{18} \textbf{\B{মোলার আপেক্ষিক তাপদ্বয়ের সম্পর্ক (মেয়রের সমীকরণ):}} {\lat $R = C_p - C_v$}

\itm{19} \textbf{\B{স্থির চাপে মোলার আপেক্ষিক তাপ (স্বাধীনতার মাত্রার সাপেক্ষে):}} {\lat $C_p = \left(\tfrac{f}{2} + 1\right)R$}

\itm{20} \textbf{\B{স্থির আয়তনে মোলার আপেক্ষিক তাপ (স্বাধীনতার মাত্রার সাপেক্ষে):}} {\lat $C_v = \tfrac{f}{2}R$}

\itm{21} \textbf{\B{মোলার আপেক্ষিক তাপদ্বয়ের অনুপাত ($\gamma$):}} {\lat $\gamma = 1 + \dfrac{2}{f}$}

\itm{22} \textbf{\B{তাপমাত্রা পরিবর্তনে প্রয়োজনীয় তাপ:}} {\lat $Q = ms\Delta T$}

\itm{23} \textbf{\B{অবস্থা পরিবর্তনে প্রয়োজনীয় তাপ (গলনের আপেক্ষিক সুপ্ততাপ):}} {\lat $Q = ml_f$}

\itm{24} \textbf{\B{অবস্থা পরিবর্তনে প্রয়োজনীয় তাপ (বাষ্পীভবনের আপেক্ষিক সুপ্ততাপ):}} {\lat $Q = ml_v$}

\itm{25} \textbf{\B{সমোষ্ণ রেখার ঢাল:}} {\lat $-\left(\dfrac{P}{V}\right)$}

\itm{26} \textbf{\B{রুদ্ধতাপীয় রেখার ঢাল:}} {\lat $-\left(\dfrac{\gamma P}{V}\right)$}

\itm{27} \textbf{\B{গ্যাস মিশ্রণের লব্ধি আপেক্ষিক তাপের অনুপাত ($\gamma_{mix}$):}} {\lat $\dfrac{n_{mix}}{\gamma_{mix}-1} = \sum\dfrac{n_i}{\gamma_i-1}$}

\itm{28} \textbf{\B{গ্যাস মিশ্রণের লব্ধি তাপমাত্রা:}} {\lat $T_{mix} = \dfrac{\sum n_iT_i}{\sum n_i}$}

\itm{29} \textbf{\B{গ্যাস মিশ্রণের লব্ধি চাপ:}} {\lat $P_{mix} = \dfrac{\sum n_iP_i}{\sum n_i}$}

\itm{30} \textbf{\B{কার্নো ইঞ্জিনে সম্পাদিত মোট কাজ:}} {\lat $W = Q_1 - Q_2$}

\itm{31} \textbf{\B{কার্নো চক্রে গৃহীত বা বর্জিত তাপ ও তাপমাত্রার সম্পর্ক:}} {\lat $\dfrac{Q_1}{T_1} = \dfrac{Q_2}{T_2}$}

\itm{32} \textbf{\B{কার্নো ইঞ্জিনের কর্মদক্ষতা ($\eta$):}} {\lat $\eta = 1 - \dfrac{T_2}{T_1} = 1 - \dfrac{Q_2}{Q_1}$}

\itm{33} \textbf{\B{কার্নো চক্রে আয়তনের সম্পর্ক (সমোষ্ণ প্রসারণ ও সংকোচন):}} {\lat $\dfrac{V_2}{V_1} = \dfrac{V_3}{V_4}$}

\itm{34} \textbf{\B{তাপমাত্রা পরিবর্তনের ফলে এনট্রপির পরিবর্তন:}} {\lat $dS = ms\ln\left(\dfrac{T_f}{T_i}\right)$}

\itm{35} \textbf{\B{রেফ্রিজারেটরের কার্যকৃতসহগ (COP):}} {\lat $\psi = \dfrac{Q_2}{W} = \dfrac{T_2}{T_1 - T_2}$}

\chsub{}{স্থির তড়িৎ (অতিরিক্ত)}

\itm{1} \textbf{\B{আধানের কোয়ান্টায়ন:}} {\lat $Q = ne$}

\itm{2} \textbf{\B{কুলম্ব ও esu আধানের এককের সম্পর্ক:}} {\lat $1\,\text{C} = 3 \times 10^9\,\text{esu}$}

\itm{3} \textbf{\B{কুলম্বের সূত্র (মধ্যবর্তী বল):}} {\lat $F = K\dfrac{q_1q_2}{r^2}$}

\itm{4} \textbf{\B{কুলম্বের ধ্রুবক:}} {\lat $K = \dfrac{1}{4\pi\epsilon_0} = 9 \times 10^9$}

\itm{5} \textbf{\B{কুলম্বের সূত্রের ভেক্টর রূপ:}} {\lat $\vec F = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{q_1q_2}{r^3}\vec r$}

\itm{6} \textbf{\B{তড়িৎ ক্ষেত্রের প্রাবল্য:}} {\lat $E = \dfrac{F}{q} = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{Q}{r^2}$}

\itm{7} \textbf{\B{তড়িৎ ক্ষেত্রে আধানের সাম্যাবস্থা:}} {\lat $mg = qE$}

\itm{8} \textbf{\B{দুটি আধানের সংযোগকারী রেখায় লব্ধি প্রাবল্য শূন্য হওয়ার বিন্দুর দূরত্ব:}} {\lat $x = \dfrac{d}{\sqrt{q_2/q_1} \pm 1}$}

\itm{9} \textbf{\B{তড়িৎ প্রাবল্য ও বিভবের সম্পর্ক (সমান্তরাল পাতের ক্ষেত্রে):}} {\lat $E = -\dfrac{dV}{dr} = \dfrac{V}{d} = \dfrac{\sigma}{\epsilon_0}$}

\itm{10} \textbf{\B{দুটি তড়িৎ ক্ষেত্রের লব্ধি প্রাবল্য:}} {\lat $E = \sqrt{E_1^2 + E_2^2 + 2E_1E_2\cos\theta}$}

\itm{11} \textbf{\B{আধানের তলমাত্রিক ঘনত্ব:}} {\lat $\sigma = \dfrac{Q}{A}$}

\itm{12} \textbf{\B{আহিত গোলকের পৃষ্ঠে আধানের তলমাত্রিক ঘনত্ব:}} {\lat $\sigma = \dfrac{Q}{4\pi r^2}$}

\itm{13} \textbf{\B{তড়িৎ ক্ষেত্রে আধান স্থানান্তরের কৃতকাজ (দূরত্বের সাপেক্ষে):}} {\lat $W = \dfrac{Qq}{4\pi\epsilon_0 K}\left(\dfrac{1}{x_i} - \dfrac{1}{x_f}\right)$}

\itm{14} \textbf{\B{তড়িৎ ক্ষেত্রে আধান স্থানান্তরের কৃতকাজ (বিভব পার্থক্যের সাপেক্ষে):}} {\lat $W = q(V_f - V_i)$}

\itm{15} \textbf{\B{বিন্দু আধানের জন্য কোনো বিন্দুতে তড়িৎ বিভব:}} {\lat $V = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{Q}{r}$}

\itm{16} \textbf{\B{আহিত গোলকের পৃষ্ঠে বা অভ্যন্তরে বিভব:}} {\lat $V = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{q}{R}$}

\itm{17} \textbf{\B{আহিত গোলকের বাইরে কোনো বিন্দুতে বিভব:}} {\lat $V = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{q}{r}$}

\itm{18} \textbf{\B{তড়িৎ ফ্লাক্স ও গাউসের সূত্র:}} {\lat $\phi = \oint\vec E \cdot d\vec A = \dfrac{q}{\epsilon_0}$}

\itm{19} \textbf{\B{সমান্তরাল পাতের ক্ষেত্রে বিভব ও প্রাবল্যের সম্পর্ক:}} {\lat $V = Ed$}

\itm{20} \textbf{\B{ফাঁপা পরিবাহী গোলকের অভ্যন্তরে তড়িৎ প্রাবল্য:}} {\lat $E = 0$}

\itm{21} \textbf{\B{গোলকের পৃষ্ঠে তড়িৎ প্রাবল্য:}} {\lat $E = \dfrac{Q}{4\pi\epsilon_0 R^2}$}

\itm{22} \textbf{\B{নিরেট অপরিবাহী গোলকের অভ্যন্তরে কোনো বিন্দুতে তড়িৎ প্রাবল্য:}} {\lat $E = \dfrac{Qr}{4\pi\epsilon_0 R^3}$}

\itm{23} \textbf{\B{ধারকত্ব (সাধারণ সমীকরণ):}} {\lat $C = \dfrac{Q}{V}$}

\itm{24} \textbf{\B{গোলাকার পরিবাহীর ধারকত্ব:}} {\lat $C = 4\pi\epsilon_0 kR$}

\itm{25} \textbf{\B{সমান্তরাল পাত ধারকের ধারকত্ব:}} {\lat $C = \dfrac{K\epsilon_0 A}{d}$}

\itm{26} \textbf{\B{পাতের মাঝে আংশিক ডাই-ইলেকট্রিক ($t$ পুরুত্বের) থাকলে লব্ধি ধারকত্ব:}} {\lat $C_{eq} = \dfrac{\epsilon_0 A}{(d-t) + t/K}$}

\itm{27} \textbf{\B{ধারকের শ্রেণি সমবায়:}} {\lat $\dfrac{1}{C_s} = \sum\dfrac{1}{C_i}$}

\itm{28} \textbf{\B{ধারকের সমান্তরাল সমবায়:}} {\lat $C_p = \sum C_i$}

\itm{29} \textbf{\B{$n$ সংখ্যক সমান ধারকের ক্ষেত্রে শ্রেণি ও সমান্তরাল সমবায়:}} {\lat $C_s = \dfrac{C}{n}, \; C_p = nC$}

\itm{30} \textbf{\B{শ্রেণি সমবায়ে বিভব বিভাজন নীতি (দুটি ধারকের জন্য):}} {\lat $V_1 = \dfrac{C_2}{C_1 + C_2}V$}

\itm{31} \textbf{\B{সমান্তরাল সমবায়ে আধান বিভাজন নীতি (দুটি ধারকের জন্য):}} {\lat $Q_1 = \dfrac{C_1}{C_1 + C_2}Q$}

\itm{32} \textbf{\B{ধারকে সঞ্চিত মোট শক্তি:}} {\lat $U = \tfrac12 QV = \tfrac12 CV^2 = \dfrac{Q^2}{2C}$}

\itm{33} \textbf{\B{ধারকের প্রতি একক আয়তনে সঞ্চিত শক্তি (শক্তি ঘনত্ব):}} {\lat $u = \tfrac12 K\epsilon_0 E^2$}

\itm{34} \textbf{\B{ধারকদ্বয়কে সংযুক্ত করলে সাধারণ বিভব:}} {\lat $V = \dfrac{C_1V_1 + C_2V_2}{C_1 + C_2}$}

\itm{35} \textbf{\B{আধানের সংরক্ষণশীলতা নীতি (সংযোগের পূর্বে ও পরে মোট আধান):}} {\lat $Q_1 + Q_2 = Q_1' + Q_2'$}

\itm{36} \textbf{\B{তড়িৎ দ্বিমেরু ভ্রামক:}} {\lat $\vec P = q(2\vec l)$}

\itm{37} \textbf{\B{দ্বিমেরুর জন্য যেকোনো বিন্দুতে তড়িৎ প্রাবল্য:}} {\lat $E_p = \dfrac{1}{4\pi\epsilon_0 K}\dfrac{P}{r^3}\sqrt{1+3\cos^2\theta}$}

\itm{38} \textbf{\B{দ্বিমেরুর জন্য যেকোনো বিন্দুতে তড়িৎ বিভব:}} {\lat $V_p = \dfrac{P\cos\theta}{4\pi\epsilon_0 K r^2}$}

\itm{39} \textbf{\B{দ্বিমেরুর অক্ষস্থিত কোনো বিন্দুতে প্রাবল্য ($\theta=0^\circ$ হলে):}} {\lat $E = \dfrac{2P}{4\pi\epsilon_0 K r^3}$}

\itm{40} \textbf{\B{দ্বিমেরুর লম্ব সমদ্বিখণ্ডকের ওপর কোনো বিন্দুতে প্রাবল্য ($\theta=90^\circ$ হলে):}} {\lat $E = \dfrac{P}{4\pi\epsilon_0 K r^3}$}

\itm{41} \textbf{\B{অসীম দীর্ঘ সরল পরিবাহী তার হতে দূরত্বের সাপেক্ষে তড়িৎ প্রাবল্য:}} {\lat $E = \dfrac{\lambda}{2\pi\epsilon_0 r}$}

\chsub{}{চল তড়িৎ (অতিরিক্ত)}

\itm{1} \textbf{\B{তড়িৎ প্রবাহের সাধারণ সমীকরণ:}} {\lat $I = \dfrac{Q}{t}$}

\itm{2} \textbf{\B{ইলেকট্রনের তাড়ন বেগ (Drift Velocity):}} {\lat $v = \dfrac{I}{neA}$}

\itm{3} \textbf{\B{তড়িৎ প্রবাহ ঘনত্ব:}} {\lat $J = \dfrac{I}{A} = nve$}

\itm{4} \textbf{\B{তাপের যান্ত্রিক তুল্যাঙ্ক:}} {\lat $J = \dfrac{W}{H}$}

\itm{5} \textbf{\B{তড়িৎ ক্ষমতা:}} {\lat $P = VI = I^2R = \dfrac{V^2}{R}$}

\itm{6} \textbf{\B{তড়িৎ শক্তি বা কৃতকাজ:}} {\lat $W = VIt$}

\itm{7} \textbf{\B{রোধের সাধারণ সমীকরণ (আপেক্ষিক রোধের সাপেক্ষে):}} {\lat $R = \rho \dfrac{L}{A}$}

\itm{8} \textbf{\B{তাপমাত্রার সাথে রোধের পরিবর্তনের সমীকরণ:}} {\lat $R_\theta = R_0(1+\alpha\theta)$}

\itm{9} \textbf{\B{রোধের উষ্ণতা গুণাঙ্ক:}} {\lat $\alpha = \dfrac{R_\theta - R_0}{R_0\theta}$}

\itm{10} \textbf{\B{তাত্ক্ষণিক তড়িৎ প্রবাহ:}} {\lat $I = \dfrac{dq}{dt}$}

\itm{11} \textbf{\B{মোট প্রবাহিত আধান (নির্দিষ্ট সময়ের ব্যবধানে):}} {\lat $q = \int I \, dt$}

\itm{12} \textbf{\B{পরিবাহীর দৈর্ঘ্য কেটে বা জোড়া দিয়ে $n$ গুণ করলে নতুন রোধ:}} {\lat $R' = nR$}

\itm{13} \textbf{\B{পরিবাহীকে টেনে দৈর্ঘ্য $n$ গুণ করলে নতুন রোধ:}} {\lat $R' = n^2R$}

\itm{14} \textbf{\B{রোধের শ্রেণি সমবায়:}} {\lat $R_s = \sum R_i$}

\itm{15} \textbf{\B{রোধের সমান্তরাল সমবায়:}} {\lat $\dfrac{1}{R_p} = \sum \dfrac{1}{R_i}$}

\itm{16} \textbf{\B{$n$ সংখ্যক সমান রোধের শ্রেণি সমবায়:}} {\lat $R_s = nR$}

\itm{17} \textbf{\B{$n$ সংখ্যক সমান রোধের সমান্তরাল সমবায়:}} {\lat $R_p = \dfrac{R}{n}$}

\itm{18} \textbf{\B{তড়িৎচালক শক্তি ও বিভব পার্থক্যের সম্পর্ক:}} {\lat $E = V + Ir = I(R + r)$}

\itm{19} \textbf{\B{কোষের অভ্যন্তরীণ রোধের জন্য হারানো বিভব (নষ্ট ভোল্ট):}} {\lat $V_{lost} = Ir$}

\itm{20} \textbf{\B{বিভব বিভাজন নীতি (Voltage Divider Law - VDL):}} {\lat $V_1 = \dfrac{R_1}{R_1 + R_2}V$}

\itm{21} \textbf{\B{প্রবাহ বিভাজন নীতি (Current Divider Law - CDL):}} {\lat $I_1 = \dfrac{R_2}{R_1 + R_2}I$}

\itm{22} \textbf{\B{কার্শফের প্রথম সূত্র বা প্রবাহ সূত্র (KCL):}} {\lat $\sum I = 0$}

\itm{23} \textbf{\B{কার্শফের দ্বিতীয় সূত্র বা বিভব সূত্র (KVL):}} {\lat $\sum V = \sum IR$}

\itm{24} \textbf{\B{তড়িৎ কোষের শ্রেণি সমবায়:}} {\lat $I_s = \dfrac{nE}{R + nr}$}

\itm{25} \textbf{\B{তড়িৎ কোষের সমান্তরাল সমবায় ($m$ সংখ্যক কোষের জন্য):}} {\lat $I_p = \dfrac{mE}{mR + r}$}

\itm{26} \textbf{\B{তড়িৎ কোষের মিশ্র সমবায়:}} {\lat $I = \dfrac{mnE}{mR + nr}$}

\itm{27} \textbf{\B{মিশ্র সমবায়ে সর্বোচ্চ প্রবাহ পাওয়ার শর্ত:}} {\lat $mR = nr$}

\itm{28} \textbf{\B{হুইটস্টোন ব্রিজের সাম্যাবস্থার শর্ত ($I_g = 0$ হলে):}} {\lat $\dfrac{P}{Q} = \dfrac{R}{S}$}

\itm{29} \textbf{\B{মিটার ব্রিজের ক্ষেত্রে অজানা রোধ নির্ণয়:}} {\lat $\dfrac{P}{Q} = \dfrac{l}{100 - l}$}

\itm{30} \textbf{\B{শান্টের মধ্য দিয়ে প্রবাহিত তড়িৎপ্রবাহ:}} {\lat $I_s = \dfrac{G}{G + S}I$}

\itm{31} \textbf{\B{গ্যালভানোমিটারের মধ্য দিয়ে প্রবাহিত তড়িৎপ্রবাহ:}} {\lat $I_g = \dfrac{S}{G + S}I$}

\itm{32} \textbf{\B{অ্যামিটারের পাল্লা $n$ গুণ করতে প্রয়োজনীয় শান্টের রোধ:}} {\lat $S = \dfrac{G}{n - 1}$}

\itm{33} \textbf{\B{ভোল্টমিটারের পাল্লা $n$ গুণ করতে শ্রেণি সমবায়ে যুক্ত প্রয়োজনীয় উচ্চ রোধ:}} {\lat $S = G(n - 1)$}

\itm{34} \textbf{\B{পটেনশিওমিটারের সাহায্যে কোষের তড়িৎচালক শক্তি পরিমাপ:}} {\lat $E = \dfrac{I \cdot l \cdot R}{L}$}

\itm{35} \textbf{\B{পটেনশিওমিটারের সাহায্যে কোষের অভ্যন্তরীণ রোধ নির্ণয়:}} {\lat $r = \left(\dfrac{l_1}{l_2} - 1\right)R$}


\chsub{}{চৌম্বক ক্রিয়া ও চুম্বকত্ব (অতিরিক্ত)}

\itm{1} \textbf{\B{গতিশীল আধানের ওপর প্রযুক্ত চৌম্বক বল (চৌম্বক লরেঞ্জ বল):}} {\lat $\vec F = q\vec v \times \vec B = qvB\sin\theta$}

\itm{2} \textbf{\B{তড়িৎবাহী কুণ্ডলীর মধ্য দিয়ে অতিক্রান্ত চৌম্বক ফ্লাক্স:}} {\lat $\phi = NAB\cos\theta$}

\itm{3} \textbf{\B{চৌম্বক ক্ষেত্রের একক টেসলা ও গাউসের মধ্যে সম্পর্ক:}} {\lat $1\,\text{T} = 10^4\,\text{G}$}

\itm{4} \textbf{\B{বায়ো-সাভার্টের সূত্র (ক্ষুদ্র অংশের জন্য চৌম্বক ক্ষেত্র):}} {\lat $B = \dfrac{\mu_0}{4\pi}\int\dfrac{Idl\sin\alpha}{r^2}$}

\itm{5} \textbf{\B{অসীম দৈর্ঘ্যের সোজা পরিবাহী তারের দরুণ চৌম্বক ক্ষেত্র:}} {\lat $B = \dfrac{\mu_0 I}{2\pi a}$}

\itm{6} \textbf{\B{বৃত্তাকার কুণ্ডলীর কেন্দ্রে সৃষ্ট চৌম্বক ক্ষেত্র:}} {\lat $B = \dfrac{\mu_0 nI}{2r}$}

\itm{7} \textbf{\B{অ্যাম্পিয়ারের সার্কিটাল সূত্র:}} {\lat $\oint\vec B \cdot d\vec l = \mu_0 I$}

\itm{8} \textbf{\B{লরেঞ্জ বল (তড়িৎ ও চৌম্বক বলের সমষ্টি):}} {\lat $\vec F = q(\vec E + \vec v \times \vec B)$}

\itm{9} \textbf{\B{দুটি সমান্তরাল পরিবাহী তারের প্রতি একক দৈর্ঘ্যে প্রযুক্ত বল:}} {\lat $\dfrac{F}{l} = \dfrac{\mu_0 I_aI_b}{2\pi d}$}

\itm{10} \textbf{\B{হল বিভব (Hall Voltage):}} {\lat $V_H = Ed = \dfrac{BI}{ntq}$}

\itm{11} \textbf{\B{চৌম্বক ক্ষেত্রের তীব্রতায় স্থাপিত তড়িৎবাহী লুপের ওপর প্রযুক্ত টর্ক:}} {\lat $\tau = NIAB\sin\alpha$}

\itm{12} \textbf{\B{চৌম্বক দ্বিমেরু ভ্রামক:}} {\lat $\vec M = NIA$}

\itm{13} \textbf{\B{দুটি লুপের চৌম্বক ভ্রামক সমান হওয়ার শর্ত:}} {\lat $I_1A_1 = I_2A_2$}

\itm{14} \textbf{\B{ইলেকট্রনের স্পিন বা কক্ষীয় চৌম্বক ভ্রামক:}} {\lat $\vec\mu_l = -\dfrac{e}{2m}\vec S$}

\itm{15} \textbf{\B{ইলেকট্রনের মোট চৌম্বক ভ্রামক:}} {\lat $\vec\mu = -\dfrac{e}{2m}(\vec L + 2\vec S)$}

\itm{16} \textbf{\B{দণ্ড চৌম্বকের চৌম্বক ভ্রামক:}} {\lat $\vec M = m \times 2\vec l$}

\itm{17} \textbf{\B{চৌম্বক অনুপ্রবণতা বা চৌম্বক প্রবণতা:}} {\lat $\chi_m = \dfrac{I}{H}$}

\itm{18} \textbf{\B{চৌম্বকায়ন তীব্রতা (Intensity of Magnetization):}} {\lat $I = \dfrac{m}{A}$}

\itm{19} \textbf{\B{চৌম্বক আবেশ ও চৌম্বক ক্ষেত্রের তীব্রতার সম্পর্ক:}} {\lat $B = \mu H$}

\itm{20} \textbf{\B{ফেরোচৌম্বক পদার্থের আপেক্ষিক চৌম্বক প্রবেশ্যতা:}} {\lat $\mu \gg 1$}

\itm{21} \textbf{\B{প্যারাচৌম্বক পদার্থের আপেক্ষিক চৌম্বক প্রবেশ্যতা:}} {\lat $\mu > 1$}

\itm{22} \textbf{\B{ডায়াচৌম্বক পদার্থের আপেক্ষিক চৌম্বক প্রবেশ্যতা:}} {\lat $\mu < 1$}

\itm{23} \textbf{\B{ভূ-চৌম্বক ক্ষেত্রের লব্ধি তীব্রতা:}} {\lat $I = \sqrt{H^2 + V^2}$}

\itm{24} \textbf{\B{ভূ-চৌম্বক ক্ষেত্রের অনুভূমিক উপাংশ:}} {\lat $H = I\cos\delta$}

\itm{25} \textbf{\B{ভূ-চৌম্বক ক্ষেত্রের উলম্ব উপাংশ:}} {\lat $V = I\sin\delta$}

\itm{26} \textbf{\B{ভূ-চৌম্বক ক্ষেত্রের উপাংশদ্বয়ের অনুপাত ও বিনতি কোণের সম্পর্ক:}} {\lat $\dfrac{H}{V} = \cot\delta$}

\chsub{}{তড়িৎ চৌম্বক আবেশ ও AC (অতিরিক্ত)}

\itm{1} \textbf{\B{ফ্যারাডের আবেশ সূত্র (আবিষ্ট তড়িৎচালক শক্তি):}} {\lat $E = N \dfrac{d\phi}{dt}$}

\itm{2} \textbf{\B{স্বকীয় আবেশের ক্ষেত্রে আবিষ্ট তড়িৎচালক শক্তি:}} {\lat $E = -L \dfrac{di}{dt}$}

\itm{3} \textbf{\B{চৌম্বক ফ্লাক্স ও স্বকীয় আবেশ গুণাঙ্কের সম্পর্ক:}} {\lat $\phi = Li$}

\itm{4} \textbf{\B{সোলেনয়েডের স্বকীয় আবেশ গুণাঙ্ক:}} {\lat $L = \dfrac{\mu N^2A}{l}$}

\itm{5} \textbf{\B{ট্রান্সফরমারের তড়িৎচালক শক্তি ও পাকসংখ্যার সম্পর্ক:}} {\lat $\dfrac{E_s}{E_p} = \dfrac{n_s}{n_p}$}

\itm{6} \textbf{\B{ট্রান্সফরমারের তড়িৎপ্রবাহ ও পাকসংখ্যার সম্পর্ক:}} {\lat $\dfrac{I_p}{I_s} = \dfrac{n_s}{n_p}$}

\itm{7} \textbf{\B{আদর্শ ট্রান্সফরমারের ক্ষেত্রে ক্ষমতা (ইনপুট ও আউটপুট ক্ষমতা সমান):}} {\lat $E_pI_p = E_sI_s$}

\itm{8} \textbf{\B{ঘূর্ণনশীল কুণ্ডলীতে মোট তড়িৎ চৌম্বক ফ্লাক্স:}} {\lat $\phi_N = NAB\cos\omega t$}

\itm{9} \textbf{\B{পরিবর্তী তড়িৎচালক শক্তির তাত্ক্ষণিক সমীকরণ:}} {\lat $E = E_0\sin\omega t$}

\itm{10} \textbf{\B{পরিবর্তী তড়িৎচালক শক্তির সর্বোচ্চ মান (শীর্ষ মান):}} {\lat $E_0 = NAB\omega$}

\itm{11} \textbf{\B{তড়িৎচালক শক্তির বর্গ-মূল-গড়-বর্গ মান (RMS মান):}} {\lat $E_{rms} = \dfrac{E_0}{\sqrt{2}}$}

\itm{12} \textbf{\B{তড়িৎপ্রবাহের বর্গ-মূল-গড়-বর্গ মান (RMS মান):}} {\lat $I_{rms} = \dfrac{I_0}{\sqrt{2}}$}

\itm{13} \textbf{\B{পরিবর্তী প্রবাহ (AC) বর্তনীতে ক্ষয়িত গড় ক্ষমতা:}} {\lat $P = I_{rms}^2 R$}

\chsub{}{জ্যামিতিক আলোকবিদ্যা (অতিরিক্ত)}

\itm{1} \textbf{\B{স্নেলের সূত্র (প্রতিসরণের সাধারণ সূত্র):}} {\lat $\mu_a\sin i = \mu_b\sin r$}

\itm{2} \textbf{\B{লেন্স প্রস্তুতকারকের সমীকরণ:}} {\lat $\dfrac{1}{f} = (\mu-1)\left(\dfrac{1}{r_1}-\dfrac{1}{r_2}\right)$}

\itm{3} \textbf{\B{আপেক্ষিক প্রতিসরণাঙ্ক ও আলোর বেগের সম্পর্ক:}} {\lat $^a\mu_b = \dfrac{c_a}{c_b} = \dfrac{\mu_b}{\mu_a}$}

\itm{4} \textbf{\B{লেন্সের সাধারণ সমীকরণ:}} {\lat $\dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f}$}

\itm{5} \textbf{\B{লেন্সের রৈখিক বিবর্ধন:}} {\lat $m = -\dfrac{v}{u}$}

\itm{6} \textbf{\B{লেন্সের ক্ষমতা:}} {\lat $P = \dfrac{1}{f}$}

\itm{7} \textbf{\B{দূরবীক্ষণ যন্ত্রের (টেলিস্কোপ) বিবর্ধন ক্ষমতা:}} {\lat $m = f_0\left(\dfrac{1}{f} + \dfrac{1}{f_e}\right)$}

\itm{8} \textbf{\B{আলোকীয় যন্ত্রের বিশ্লেষণ ক্ষমতা (Resolving Power):}} {\lat $R = \dfrac{2a\sin\theta}{\lambda}$}

\itm{9} \textbf{\B{সরল অণুবীক্ষণ যন্ত্রের বিবর্ধন ক্ষমতা (স্পষ্ট দর্শনের ন্যূনতম দূরত্বে):}} {\lat $m = 1 + \dfrac{D}{f}$}

\itm{10} \textbf{\B{দূরবীক্ষণ যন্ত্রের নলের দৈর্ঘ্য (স্পষ্ট দর্শনের ন্যূনতম দূরত্বের ক্ষেত্রে):}} {\lat $L = f_0 + \dfrac{Df_e}{D+f_e}$}

\itm{11} \textbf{\B{লেন্স সমবায়ের তুল্য ফোকাস দূরত্ব:}} {\lat $\dfrac{1}{F} = \sum\dfrac{1}{f_i}$}

\itm{12} \textbf{\B{লেন্স সমবায়ের তুল্য ক্ষমতা:}} {\lat $P = \sum P_i$}

\itm{13} \textbf{\B{প্রিজমের চ্যুতি কোণ:}} {\lat $\delta = i_1 + i_2 - A$}

\itm{14} \textbf{\B{প্রিজম কোণ:}} {\lat $A = r_1 + r_2$}

\itm{15} \textbf{\B{প্রিজমের উপাদানের প্রতিসরণাঙ্ক (ন্যূনতম চ্যুতির ক্ষেত্রে):}} {\lat $\mu = \dfrac{\sin\dfrac{A+\delta_m}{2}}{\sin\dfrac{A}{2}}$}

\itm{16} \textbf{\B{সরু প্রিজমের ক্ষেত্রে চ্যুতি কোণ:}} {\lat $\delta = A(\mu-1)$}

\itm{17} \textbf{\B{প্রিজমের উপাদানের বিচ্ছুরণ ক্ষমতা:}} {\lat $\omega = \dfrac{\delta_v-\delta_r}{\delta} = \dfrac{\mu_v-\mu_r}{\mu-1}$}

\chsub{}{ভৌত আলোকবিদ্যা (অতিরিক্ত)}

\itm{1} \textbf{\B{তরঙ্গের সমীকরণ (সরণ):}} {\lat $y = A\sin(\omega t - 2\pi x/\lambda)$}

\itm{2} \textbf{\B{তাড়িৎচৌম্বক তরঙ্গের তড়িৎক্ষেত্রের সমীকরণ:}} {\lat $E = E_0\sin(ct - x)$}

\itm{3} \textbf{\B{তাড়িৎচৌম্বক তরঙ্গের চৌম্বকক্ষেত্রের সমীকরণ:}} {\lat $B = B_0\sin(ct - x)$}

\itm{4} \textbf{\B{তড়িৎক্ষেত্র ও চৌম্বকক্ষেত্রের বিস্তারের সম্পর্ক:}} {\lat $E = Bc$}

\itm{5} \textbf{\B{আলোর বেগ এবং মাধ্যমের প্রবেশ্যতা ও তড়িৎভেদ্যতার সম্পর্ক:}} {\lat $c = \dfrac{1}{\sqrt{\mu\epsilon}}$}

\itm{6} \textbf{\B{গঠনমূলক ব্যতিচারের ক্ষেত্রে পথ পার্থক্য:}} {\lat $\Delta x = n\lambda$}

\itm{7} \textbf{\B{গঠনমূলক ব্যতিচারের ক্ষেত্রে দশা পার্থক্য:}} {\lat $\Delta\delta = 2n\pi$}

\itm{8} \textbf{\B{ধ্বংসাত্মক ব্যতিচারের ক্ষেত্রে পথ পার্থক্য:}} {\lat $\Delta x = (2n-1)\dfrac{\lambda}{2}$}

\itm{9} \textbf{\B{ধ্বংসাত্মক ব্যতিচারের ক্ষেত্রে দশা পার্থক্য:}} {\lat $\Delta\delta = (2n-1)\pi$}

\itm{10} \textbf{\B{ইয়ংয়ের দ্বী-চিড় পরীক্ষায় $n$-তম উজ্জ্বল ডোরার দূরত্ব:}} {\lat $x_n = \dfrac{n\lambda D}{d}$}

\itm{11} \textbf{\B{$n$-তম অন্ধকার ডোরার দূরত্ব:}} {\lat $x_n = \dfrac{(2n-1)\lambda D}{2d}$}

\itm{12} \textbf{\B{ডোরা ব্যবধান (পরপর দুটি উজ্জ্বল বা অন্ধকার ডোরার মধ্যবর্তী দূরত্ব):}} {\lat $\Delta x = \dfrac{\lambda D}{d}$}

\itm{13} \textbf{\B{ডোরার কৌণিক ব্যবধান বা কৌণিক প্রস্থ:}} {\lat $\Delta\theta = \dfrac{\lambda}{d}$}

\itm{14} \textbf{\B{ব্যতিচারের ক্ষেত্রে ডোরার উপরিপাতন বা তরঙ্গদৈর্ঘ্যের সম্পর্ক:}} {\lat $N_1\lambda_1 = N_2\lambda_2$}

\itm{15} \textbf{\B{উপরিপাতিত তরঙ্গের লব্ধি বিস্তার:}} {\lat $A = \sqrt{A_1^2 + A_2^2 + 2A_1A_2\cos\delta}$}

\itm{16} \textbf{\B{উপরিপাতিত তরঙ্গের লব্ধি তীব্রতা:}} {\lat $I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\delta$}

\itm{17} \textbf{\B{একক চিড় অপবর্তনের ক্ষেত্রে পথ পার্থক্য:}} {\lat $a\sin\theta = \Delta x$}

\itm{18} \textbf{\B{অপবর্তনে গৌণ চরম বিন্দুর (উজ্জ্বল) শর্ত:}} {\lat $\Delta x = (2n+1)\dfrac{\lambda}{2}$}

\itm{19} \textbf{\B{অপবর্তনে গৌণ অবম বিন্দুর (অন্ধকার) শর্ত:}} {\lat $\Delta x = n\lambda$}

\itm{20} \textbf{\B{অপবর্তন গ্রেটিং ধ্রুবক:}} {\lat $d = a+b = \dfrac{1}{N}$}

\itm{21} \textbf{\B{অপবর্তন গ্রেটিংয়ের সাধারণ সমীকরণ (পথ পার্থক্য):}} {\lat $d\sin\theta = \Delta x$}

\itm{22} \textbf{\B{ম্যালুসের সূত্র (একাধিক পোলারাইজারের মধ্য দিয়ে নির্গত আলোর তীব্রতা):}} {\lat $I_n = I_0\cos^2\theta_1\cdots\cos^2\theta_n$}

\itm{23} \textbf{\B{$n$ সংখ্যক পোলারাইজারের ক্ষেত্রে লব্ধি তীব্রতা:}} {\lat $I_n = I_0\cos^2\dfrac{\theta}{2}$}

\itm{24} \textbf{\B{সমবর্তন কোণ ও প্রতিসরণ কোণের সম্পর্ক:}} {\lat $r + i_p = 90^\circ$}

\itm{25} \textbf{\B{ব্রুস্টারের সূত্র (প্রতিসরণাঙ্ক ও সমবর্তন কোণ):}} {\lat $\tan i_p = \dfrac{\mu_2}{\mu_1}$}

\itm{26} \textbf{\B{পয়েন্টিং ভেক্টর (তাড়িৎচৌম্বক তরঙ্গের শক্তি প্রবাহের হার):}} {\lat $\vec S = \vec E \times \vec H$}

\chsub{}{আধুনিক পদার্থবিজ্ঞান (অতিরিক্ত)}

\itm{1} \textbf{\B{বিপরীত লরেঞ্জ রূপান্তর (স্থান বা অবস্থান):}} {\lat $x = \dfrac{x' + vt'}{\sqrt{1 - v^2/c^2}}$}

\itm{2} \textbf{\B{বিপরীত লরেঞ্জ রূপান্তর (সময়):}} {\lat $t = \dfrac{t' + vx'/c^2}{\sqrt{1 - v^2/c^2}}$}

\itm{3} \textbf{\B{আপেক্ষিক বেগ সংযোজন সূত্র:}} {\lat $V_x = \dfrac{V_x' + V}{1 + V_x'V/c^2}$}

\itm{4} \textbf{\B{লরেঞ্জ বেগ রূপান্তর সমীকরণ:}} {\lat $V_x' = \dfrac{V_x - V}{1 - V_xV/c^2}$}

\itm{5} \textbf{\B{দৈর্ঘ্য সংকোচন (Length Contraction):}} {\lat $L_r = L_0\sqrt{1 - v^2/c^2}$}

\itm{6} \textbf{\B{ভরের আপেক্ষিকতা (Mass Relativity):}} {\lat $m_r = \dfrac{m_0}{\sqrt{1 - v^2/c^2}}$}

\itm{7} \textbf{\B{কাল দীর্ঘায়ন (Time Dilation):}} {\lat $t_r = \dfrac{t_0}{\sqrt{1 - v^2/c^2}}$}

\itm{8} \textbf{\B{গতিশীল অবস্থায় ক্ষেত্রফল সংকোচন:}} {\lat $A_r = A_0\sqrt{1 - v^2/c^2}$}

\itm{9} \textbf{\B{গতিশীল অবস্থায় ঘনত্বের পরিবর্তন:}} {\lat $\rho_r = \dfrac{\rho_0}{1 - v^2/c^2}$}

\itm{10} \textbf{\B{গতিশীল অবস্থায় আয়তন সংকোচন:}} {\lat $v_r = v_0\sqrt{1 - v^2/c^2}$}

\itm{11} \textbf{\B{আপেক্ষিক গতিশক্তি:}} {\lat $E_k = (m - m_0)c^2$}

\itm{12} \textbf{\B{নিশ্চল শক্তি বা স্থির ভর শক্তি:}} {\lat $U = m_0c^2$}

\itm{13} \textbf{\B{আইনস্টাইনের মোট ভর-শক্তি সমীকরণ:}} {\lat $E = mc^2$}

\itm{14} \textbf{\B{শক্তি ও ভরবেগের সম্পর্কযুক্ত সমীকরণ:}} {\lat $E^2 = P^2c^2 + m_0^2c^4$}

\itm{15} \textbf{\B{ফোটনের শক্তি:}} {\lat $E = hf = \dfrac{hc}{\lambda}$}

\itm{16} \textbf{\B{আইনস্টাইনের আলোক-তড়িৎ সমীকরণ (Photoelectric Equation):}} {\lat $E = \phi + E_{k,max}$}

\itm{17} \textbf{\B{ধাতুর কার্যাপেক্ষক (Work Function):}} {\lat $\phi = hf_0 = \dfrac{hc}{\lambda_0}$}

\itm{18} \textbf{\B{নির্গমন ইলেকট্রনের সর্বোচ্চ গতিশক্তি ও নিবৃত্তি বিভবের সম্পর্ক:}} {\lat $E_{k,max} = \dfrac{1}{2}mv_{max}^2 = V_se$}

\itm{19} \textbf{\B{এক্স-রে (X-ray) উৎপাদনের ক্ষেত্রে সর্বোচ্চ শক্তি ও ন্যূনতম তরঙ্গদৈর্ঘ্য:}} {\lat $E_{k,max} = hf_{max} = \dfrac{hc}{\lambda_{min}}$}

\itm{20} \textbf{\B{কম্পটন ক্রিয়া বা কম্পটন সরণ (Compton Shift):}} {\lat $\lambda' = \lambda + \dfrac{h}{m_0c}(1 - \cos\theta)$}

\itm{21} \textbf{\B{স্টিফান-বোলৎজম্যান সূত্র (কৃষ্ণবস্তুর বিকিরণ ক্ষমতা):}} {\lat $P = \sigma eAT^4$}

\itm{22} \textbf{\B{পারিপার্শ্বিকের উপস্থিতিতে কৃষ্ণবস্তুর নীট বিকিরণ হার:}} {\lat $P = \sigma eA(T_B^4 - T_E^4)$}

\itm{23} \textbf{\B{স্টিফান-বোলৎজম্যান ধ্রুবক:}} {\lat $\sigma = 5.67 \times 10^{-8} \, \text{W}\,\text{m}^{-2}\,\text{K}^{-4}$}

\itm{24} \textbf{\B{ডি-ব্রগলি তরঙ্গদৈর্ঘ্য (পদার্থ তরঙ্গ):}} {\lat $\lambda = \dfrac{h}{mv}$}

\itm{25} \textbf{\B{হাইজেনবার্গের অনিশ্চয়তা নীতি:}} {\lat $\Delta x \cdot \Delta p \geq \dfrac{h}{4\pi}$}

\chsub{}{পরমাণু মডেল ও নিউক্লিয়ার (অতিরিক্ত)}

\itm{1} \textbf{\B{বোর মডেল অনুযায়ী $n$-তম কক্ষপথের ব্যাসার্ধের সাধারণ সমীকরণ:}} {\lat $r_n = \dfrac{h^2\epsilon_0 n^2}{\pi mze^2}$}

\itm{2} \textbf{\B{কক্ষপথের ব্যাসার্ধ নির্ণয়ের শর্টকাট সমীকরণ (অ্যাংস্ট্রম এককে):}} {\lat $r_n = (0.53\,\text{\AA})\dfrac{n^2}{z}$}

\itm{3} \textbf{\B{$n$-তম কক্ষপথে ইলেকট্রনের বেগের সাধারণ সমীকরণ:}} {\lat $V_n = \dfrac{ze^2}{2h\epsilon_0 n}$}

\itm{4} \textbf{\B{কক্ষপথে ইলেকট্রনের বেগ নির্ণয়ের শর্টকাট সমীকরণ:}} {\lat $V_n = (2.18\times10^6)\dfrac{z}{n}\,\text{ms}^{-1}$}

\itm{5} \textbf{\B{$n$-তম কক্ষপথে ইলেকট্রনের স্থিতিশক্তি (Potential Energy):}} {\lat $E_p = -\dfrac{z^2me^4}{4h^2\epsilon_0^2 n^2}$}

\itm{6} \textbf{\B{$n$-তম কক্ষপথে ইলেকট্রনের গতিশক্তি (Kinetic Energy):}} {\lat $E_k = +\dfrac{z^2me^4}{8h^2\epsilon_0^2 n^2}$}

\itm{7} \textbf{\B{$n$-তম কক্ষপথে ইলেকট্রনের মোট শক্তি (Total Energy):}} {\lat $E = -\dfrac{z^2me^4}{8h^2\epsilon_0^2 n^2}$}

\itm{8} \textbf{\B{কক্ষপথে মোট শক্তি নির্ণয়ের শর্টকাট সমীকরণ (eV এককে):}} {\lat $E = -13.6\dfrac{z^2}{n^2}\,\text{eV}$}

\itm{9} \textbf{\B{$n$-তম কক্ষপথে ইলেকট্রনের আবর্তনকাল (Time Period):}} {\lat $T_n = \dfrac{4h^3\epsilon_0^2 n^3}{z^2me^4}$}

\itm{10} \textbf{\B{প্রথম কক্ষপথের সাপেক্ষে $n$-তম কক্ষপথের ব্যাসার্ধের সম্পর্ক:}} {\lat $r_n = n^2 r_1$}

\itm{11} \textbf{\B{প্রথম কক্ষপথের সাপেক্ষে $n$-তম কক্ষপথে বেগের সম্পর্ক:}} {\lat $V_n = \dfrac{V_1}{n}$}

\itm{12} \textbf{\B{প্রথম কক্ষপথের সাপেক্ষে $n$-তম কক্ষপথে মোট শক্তির সম্পর্ক:}} {\lat $E_n = \dfrac{E_1}{n^2}$}

\itm{13} \textbf{\B{প্রথম কক্ষপথের সাপেক্ষে $n$-তম কক্ষপথে আবর্তনকালের সম্পর্ক:}} {\lat $T_n = n^3 T_1$}

\itm{14} \textbf{\B{ইলেকট্রনের কক্ষপথ স্থানান্তরে নির্গত বা শোষিত শক্তি:}} {\lat $\Delta E = E_2 - E_1 = \dfrac{hc}{\lambda} = h\nu$}

\itm{15} \textbf{\B{রিদবার্গ সমীকরণ (নির্গত বিকিরণের তরঙ্গদৈর্ঘ্য নির্ণয়):}} {\lat $\dfrac{1}{\lambda} = R_Hz^2\left(\dfrac{1}{n_1^2} - \dfrac{1}{n_2^2}\right)$}

\itm{16} \textbf{\B{রিদবার্গ ধ্রুবক (Rydberg Constant):}} {\lat $R_H = 1.09678\times10^7\,\text{m}^{-1}$}

\itm{17} \textbf{\B{হাইড্রোজেন বর্ণালীর বিভিন্ন সিরিজসমূহের নিম্নতম কক্ষপথ ($n_1$):}} {\lat $\text{Lyman: } n_1=1,\; \text{Balmer: } n_1=2,\; \text{Paschen: } n_1=3,\; \text{Brackett: } n_1=4,\; \text{Pfund: } n_1=5,\; \text{Humphreys: } n_1=6$}

\itm{18} \textbf{\B{নিউক্লিয়াসের ব্যাসার্ধ ও ভরসংখ্যার সম্পর্ক:}} {\lat $r = r_0 A^{1/3}$}

\itm{19} \textbf{\B{নিউক্লিয়ার ব্যাসার্ধের ধ্রুবক (Fermi Constant):}} {\lat $r_0 = 1.2\times10^{-15}\,\text{m}$}

\itm{20} \textbf{\B{তেজস্ক্রিয় ক্ষয়ের হার (সক্রিয়তার সূত্র):}} {\lat $\dfrac{dN}{dt} = -\lambda N$}

\itm{21} \textbf{\B{তেজস্ক্রিয় ক্ষয়ের সূচকীয় সূত্র (অবশিষ্ট পরমাণুর সংখ্যা):}} {\lat $N = N_0 e^{-\lambda t}$}

\itm{22} \textbf{\B{তেজস্ক্রিয় পদার্থের অর্ধায়ু (Half-life):}} {\lat $T_{1/2} = \dfrac{0.693}{\lambda}$}

\itm{23} \textbf{\B{তেজস্ক্রিয় পদার্থের গড় আয়ু (Mean life):}} {\lat $\tau = \dfrac{1}{\lambda}$}

\itm{24} \textbf{\B{যেকোনো সময়ে তেজস্ক্রিয়তার সক্রিয়তা (Activity):}} {\lat $A = A_0 e^{-\lambda t}$}

\itm{25} \textbf{\B{নিউক্লিয়াসের ভরত্রুটি (Mass Defect):}} {\lat $\Delta m = Zm_p + (A-Z)m_n - m_{Nu}$}

\itm{26} \textbf{\B{নিউক্লিয়াসের মোট বন্ধন শক্তি (Binding Energy):}} {\lat $\text{B.E.} = \Delta mc^2$}

\itm{27} \textbf{\B{প্রতি নিউক্লিয়ন গড় বন্ধন শক্তি:}} {\lat $\dfrac{\text{B.E.}}{A}$}

\chsub{}{সেমিকন্ডাক্টর ও লজিক (অতিরিক্ত)}

\itm{1} \textbf{\B{ডায়োডের গতীয় রোধ:}} {\lat $R = \dfrac{\Delta V}{\Delta I}$}

\itm{2} \textbf{\B{ট্রানজিস্টরের ক্ষেত্রে বিভিন্ন তড়িৎপ্রবাহের সম্পর্ক:}} {\lat $I_E = I_C + I_B$}

\itm{3} \textbf{\B{সাধারণ-নিঃসারক (CE) বিন্যাসে প্রবাহ লাভ (Beta):}} {\lat $\beta = \dfrac{I_C}{I_B}$}

\itm{4} \textbf{\B{সাধারণ-ভূমি (CB) বিন্যাসে প্রবাহ বিবর্ধন গুণক (Alpha):}} {\lat $\alpha = \dfrac{I_C}{I_E}$}

\itm{5} \textbf{\B{প্রবাহ বিবর্ধন গুণক ($\alpha$) ও প্রবাহ লাভের ($\beta$) সম্পর্ক:}} {\lat $\alpha = \dfrac{\beta}{1+\beta}$}

\itm{6} \textbf{\B{প্রবাহ লাভ ($\beta$) ও প্রবাহ বিবর্ধন গুণকের ($\alpha$) সম্পর্ক:}} {\lat $\beta = \dfrac{\alpha}{1-\alpha}$}

\itm{7} \textbf{\B{ভর-ক্রিয়া সূত্র (সহজাত অর্ধপরিবাহীতে আধান বাহকের ঘনত্ব):}} {\lat $n_i^2 = np$}

\itm{8} \textbf{\B{বুলিয়ান অ্যালজেব্রার মৌলিক শতসিদ্ধসমূহ (যোগ ও গুণ):}} {\lat $A+0=A;\; A+\bar A=1;\; A+A=A;\; A+1=1;\; A\cdot 1=A;\; A\cdot\bar A=0;\; A\cdot 0=0;\; A\cdot A=A$}

\itm{9} \textbf{\B{ডি মরগ্যানের প্রথম সূত্র:}} {\lat $\overline{A+B} = \bar A \cdot \bar B$}

\itm{10} \textbf{\B{ডি মরগ্যানের দ্বিতীয় সূত্র:}} {\lat $\overline{A \cdot B} = \bar A + \bar B$}


\chsub{}{জ্যোতির্বিজ্ঞান (অতিরিক্ত)}

\itm{1} \textbf{\B{হাবলের সূত্র (গ্যালাক্সির বেগ ও দূরত্বের সম্পর্ক):}} {\lat $V = Hd$}

\itm{2} \textbf{\B{হাবল ধ্রুবক (Hubble Constant):}} {\lat $H = 55\,\text{km}\,\text{s}^{-1}/\text{Mpc}$}

\itm{3} \textbf{\B{মহাবিশ্বের সংকট ঘনত্ব (Critical Density):}} {\lat $\rho_c = \dfrac{3H^2}{8\pi G}$}

\itm{4} \textbf{\B{মহাজাগতিক বস্তু বা গোলকাকার নক্ষত্রের গড় ঘনত্ব:}} {\lat $\rho = \dfrac{M}{\frac{4}{3}\pi R^3}$}

\itm{5} \textbf{\B{সোয়ার্জশাইল্ড ব্যাসার্ধ (ব্ল্যাকহোলের ঘটনা দিগন্তের ব্যাসার্ধ):}} {\lat $R_s = \dfrac{2GM}{c^2}$}

\itm{6} \textbf{\B{আলোর ক্ষেত্রে ডপলার ক্রিয়া (বেগ ও তরঙ্গদৈর্ঘ্যের পরিবর্তন):}} {\lat $\dfrac{V}{c} = \dfrac{\Delta \lambda}{\lambda}$}

\itm{7} \textbf{\B{কোনো গ্রহ বা মহাজাগতিক বস্তুর মুক্তিবেগ (Escape Velocity):}} {\lat $v_e = \sqrt{\dfrac{2GM}{R}}$}

\itm{8} \textbf{\B{কৃত্রিম উপগ্রহের কক্ষপথীয় বেগ (Orbital Velocity):}} {\lat $V = \sqrt{\dfrac{GM}{R+h}}$}

\itm{9} \textbf{\B{কৃত্রিম উপগ্রহের আবর্তনকাল বা পর্যায়কাল:}} {\lat $T = 2\pi(R+h)\sqrt{\dfrac{R+h}{GM}}$}

\itm{10} \textbf{\B{কেপলারের তৃতীয় সূত্র (আবর্তনকালের সূত্র):}} {\lat $T^2 \propto R^3$}

\end{multicols}

\vspace{4pt}
\begin{center}
\noindent
{\bn\large\bfseries পদার্থবিজ্ঞান ২য় পত্র — সম্পূর্ণ সূত্র, সংজ্ঞা ও চিত্র}\hfill
{\normalfont\small \textbf{By Abir Arafat Chawdhury  [Mr. Introvert ]}}
\vspace{3pt}
\end{center}

\begin{multicols}{2}

\noindent\colorbox{p2bg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{পদার্থবিজ্ঞান দ্বিতীয় পত্র}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: তাপগতিবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তাপমাত্রা স্কেলের রূপান্তর ও ত্রুটিপূর্ণ থার্মোমিটার:}}
\begin{itemize}
    \item[] \B{স্কেলের পারস্পরিক রূপান্তর:} {\lat $\dfrac{C}{5}=\dfrac{F-32}{9}=\dfrac{K-273}{5}=\dfrac{R_n-491.67}{9}=\dfrac{R}{4}$}
    \item[] \B{কেলভিন ও সেলসিয়াস সম্পর্ক:} {\lat $K=C+273$}
    \item[] \B{র্যাঙ্কিন ও ফারেনহাইট সম্পর্ক:} {\lat $R(^\circ\text{Rk})=F+459.67$}
    \item[] \B{স্কেলের এক ভাগের সম্পর্ক:} {\lat $1^\circ\text{C}=\tfrac{9}{5}{}^\circ\text{F}$}
    \item[] \B{তাপমাত্রার ব্যবধানের মধ্যে সম্পর্ক:} {\lat $\dfrac{\Delta C}{5}=\dfrac{\Delta F}{9}=\dfrac{\Delta K}{5}=\dfrac{\Delta R_n}{9}=\dfrac{\Delta R}{4}$}
    \item[] \B{ত্রুটিপূর্ণ থার্মোমিটারের ক্ষেত্রে:} {\lat $\dfrac{X-M}{B-M}=\dfrac{C}{100}=\dfrac{F-32}{180}=\dfrac{K-273}{100}$}
    \item[] {\lat $C$} = \B{সেলসিয়াস স্কেলে তাপমাত্রা}
    \item[] {\lat $F$} = \B{ফারেনহাইট স্কেলে তাপমাত্রা}
    \item[] {\lat $K$} = \B{কেলভিন স্কেলে তাপমাত্রা}
    \item[] {\lat $R_n$} = \B{র্যাঙ্কিন স্কেলে তাপমাত্রা}
    \item[] {\lat $R$} = \B{রোমার স্কেলে তাপমাত্রা}
    \item[] {\lat $B$} = \B{বাষ্পবিন্দু (Steam point)}
    \item[] {\lat $M$} = \B{বরফবিন্দু (Ice point)}
\end{itemize}

\itm{2} \textbf{\B{থার্মোমেট্রিক ধর্ম থেকে তাপমাত্রা (মৌলিক ব্যবধানসহ):}} {\lat $\theta=\dfrac{X_\theta-X_{\rm ice}}{X_{\rm steam}-X_{\rm ice}}\times N + \theta_{\rm ue}$}
\begin{itemize}
    \item[] {\lat $X_\theta$} = \B{যেকোনো তাপমাত্রায় থার্মোমেট্রিক ধর্মের মান}
    \item[] {\lat $X_{\rm ice}$ বা $X_0$} = \B{বরফবিন্দু তাপমাত্রায় থার্মোমেট্রিক ধর্মের মান}
    \item[] {\lat $X_{\rm steam}$ বা $X_{100}$} = \B{বাষ্পবিন্দু তাপমাত্রায় থার্মোমেট্রিক ধর্মের মান}
    \item[] {\lat $N$} = \B{মৌলিক ব্যবধান}
    \item[] {\lat $\theta_{\rm ue}$} = \B{নিম্ন স্থির বিন্দু বা বরফবিন্দু}
    \item[] \B{সেলসিয়াস স্কেলে (মৌলিক রূপ):} {\lat $\theta = \dfrac{X-X_0}{X_{100}-X_0}\times100$}
    \item[] \B{সেলসিয়াস স্কেলে (বিন্দুসহ):} {\lat $\theta=\dfrac{X_\theta-X_{\rm ice}}{X_{\rm steam}-X_{\rm ice}}\times100+0^\circ\text{C}$}
    \item[] \B{ফারেনহাইট স্কেলে:} {\lat $\theta=\dfrac{X_\theta-X_{\rm ice}}{X_{\rm steam}-X_{\rm ice}}\times180+32^\circ\text{F}$}
    \item[] \B{কেলভিন স্কেলে:} {\lat $\theta=\dfrac{X_\theta-X_{\rm ice}}{X_{\rm steam}-X_{\rm ice}}\times100+273\text{ K}$}
    \item[] \B{রোধ থার্মোমিটার:} {\lat $\theta=\dfrac{R_\theta-R_0}{R_{100}-R_0}\times100$}
    \item[] \B{পারদ/দৈর্ঘ্য থার্মোমিটার:} {\lat $\theta=\dfrac{l_\theta-l_{\rm ice}}{l_{\rm steam}-l_{\rm ice}}\times100$}
\end{itemize}

\itm{3} \textbf{\B{স্থির বিন্দু ও স্থির আয়তন গ্যাস থার্মোমিটার (গে-লুসাক / রেনোর সূত্র):}}
\begin{itemize}
    \item[] \B{পানির ত্রৈধবিন্দু (সেলসিয়াস):} {\lat $0.01^\circ\text{C}$}
    \item[] \B{পানির ত্রৈধবিন্দু (কেলভিন):} {\lat $273.16\text{ K}$}
    \item[] \B{একটি স্থির বিন্দুর সাহায্যে অজ্ঞাত তাপমাত্রা:} {\lat $T=\dfrac{X_T}{X_{\rm tr}}\times273.16\text{ K}$}
    \item[] \B{স্থির আয়তন গ্যাস থার্মোমিটারে তাপমাত্রা:} {\lat $T=\dfrac{P_T}{P_{\rm tr}}\times273.16\text{ K}$}
    \item[] {\lat $X_T$} = \B{পরিমাপ্য তাপমাত্রায় থার্মোমেট্রিক ধর্ম}
    \item[] {\lat $P_T$} = \B{পরিমাপ্য তাপমাত্রায় গ্যাসের চাপ}
    \item[] {\lat $X_{\rm tr}$} = \B{পানির ত্রৈধবিন্দুতে থার্মোমেট্রিক ধর্ম}
    \item[] {\lat $P_{\rm tr}$} = \B{পানির ত্রৈধবিন্দুতে গ্যাসের চাপ}
\end{itemize}

\itm{4} \textbf{\B{গৃহীত-বর্জিত তাপ, ধারণক্ষমতা, সুপ্ততাপ ও ধ্রুবকসমূহ:}}
\begin{itemize}
    \item[] \B{তাপমাত্রা পরিবর্তনের জন্য গৃহীত/বর্জিত তাপ:} {\lat $Q=ms\Delta\theta=ms\Delta T=ms(T_f-T_i)$}
    \item[] \B{তাপ ধারণক্ষমতা:} {\lat $C=mc$}
    \item[] \B{অবস্থার পরিবর্তনের জন্য (গলনের সুপ্ততাপ):} {\lat $Q_{\rm latent}=mL_f$}
    \item[] \B{অবস্থার পরিবর্তনের জন্য (বাষ্পীভবনের সুপ্ততাপ):} {\lat $Q_{\rm latent}=mL_v$}
    \item[] \B{যান্ত্রিক সমতা ও কাজের সম্পর্ক:} {\lat $W=JQ$}
    \item[] {\lat $Q$} = \B{তাপশক্তি} {\lat [J]}
    \item[] {\lat $m$} = \B{ভর} {\lat [kg]}
    \item[] {\lat $\Delta T$ বা $\Delta\theta$} = \B{তাপমাত্রার পরিবর্তন}
    \item[] {\lat $T_i$} = \B{আদি তাপমাত্রা}
    \item[] {\lat $T_f$} = \B{শেষ তাপমাত্রা}
    \item[] {\lat $c$ বা $s$} = \B{আপেক্ষিক তাপ} {\lat [$\text{J}/(\text{kg}\cdot\text{K})$]}
    \item[] {\lat $C$} = \B{তাপ ধারণক্ষমতা}
    \item[] {\lat $L_f$} = \B{বরফ গলনের সুপ্ততাপ}
    \item[] {\lat $L_v$} = \B{বাষ্পীভবনের সুপ্ততাপ}
    \item[] \B{পানির আপেক্ষিক তাপ ($s_{\rm water}$):} {\lat $4200\text{ J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$}
    \item[] \B{বরফের আপেক্ষিক তাপ ($s_{\rm ice}$):} {\lat $2100\text{ J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$}
    \item[] \B{জলীয় বাষ্পের আপেক্ষিক তাপ ($s_{\rm steam}$):} {\lat $2000\text{ J}\cdot\text{kg}^{-1}\cdot\text{K}^{-1}$}
    \item[] \B{বরফ গলনের সুপ্ততাপের মান ($L_f$):} {\lat $336000\text{ J}\cdot\text{kg}^{-1}$}
    \item[] \B{বাষ্পীভবনের সুপ্ততাপের মান ($L_v$):} {\lat $2260000\text{ J}\cdot\text{kg}^{-1}$}
    \item[] \B{যান্ত্রিক সমতা ধ্রুবক ($J$):} {\lat $4.2\text{ J/cal}$}
\end{itemize}

\itm{5} \textbf{\B{গ্যাসের সূত্রসমূহ ও আদেশ গ্যাস:}}
\begin{itemize}
    \item[] \B{বয়েলের সূত্র:} {\lat $P_1V_1=P_2V_2$}
    \item[] \B{চার্লসের সূত্র:} {\lat $\dfrac{V_1}{T_1}=\dfrac{V_2}{T_2}$}
    \item[] \B{চাপের সূত্র (গে-লুসাক):} {\lat $\dfrac{P_1}{T_1}=\dfrac{P_2}{T_2}$}
    \item[] \B{গ্যাসের সম্মিলিত সূত্র:} {\lat $\dfrac{P_1V_1}{T_1}=\dfrac{P_2V_2}{T_2}$}
    \item[] \B{আদর্শ গ্যাসের সমীকরণ (মোল সংখ্যায়):} {\lat $PV=nRT$}
    \item[] \B{আদর্শ গ্যাসের সমীকরণ (অণু সংখ্যায়):} {\lat $PV=NkT$}
    \item[] \B{ডালটনের আংশিক চাপ সূত্র:} {\lat $P=P_1+P_2+\cdots$}
    \item[] \B{গ্যাস মিশ্রণের সমীকরণ (ভর ও মোলার ভরসহ):} {\lat $PV=\left(\dfrac{m_1}{M_1}+\dfrac{m_2}{M_2}\right)RT$}
    \item[] \B{অ্যাভোগাড্রো সূত্র:} \B{সমান $P,T$-তে সমান আয়তনে সমান সংখ্যক অণু থাকে}
    \item[] {\lat $P$} = \B{চাপ}
    \item[] {\lat $V$} = \B{আয়তন}
    \item[] {\lat $T$} = \B{পরম তাপমাত্রা} {\lat [K]}
    \item[] {\lat $n$} = \B{মোল সংখ্যা}
    \item[] {\lat $N$} = \B{অণু সংখ্যা}
    \item[] \B{সার্বজনীন গ্যাস ধ্রুবক ($R$):} {\lat $8.314\text{ J/mol}\cdot\text{K}$}
    \item[] \B{বোলৎজম্যান ধ্রুবক ($k$):} {\lat $1.38\times10^{-23}\text{ J/K}$}
\end{itemize}

\itm{6} \textbf{\B{গ্যাস মিশ্রণের বিশেষ সমীকরণাবলি (Gas Mixture Charts):}}
\begin{itemize}
    \item[] \B{মিশ্রণের রুদ্ধতাপীয় অনুপাত ($\gamma_{\rm mix}$):} {\lat $\dfrac{\sum n}{\gamma_{\rm mix}-1}=\dfrac{n_1}{\gamma_1-1}+\dfrac{n_2}{\gamma_2-1}+\cdots$}
    \item[] \B{মিশ্রণের মোলার আপেক্ষিক তাপের অনুপাত:} {\lat $\gamma_{\rm mix} = \dfrac{C_{p,\rm mix}}{C_{v,\rm mix}}$}
    \item[] \B{মিশ্রণের তাপমাত্রা:} {\lat $T_{\rm mix}=\dfrac{n_1T_1+n_2T_2+\cdots}{\sum n}\text{ (K)}$}
    \item[] \B{মিশ্রণের চাপ:} {\lat $P_{\rm mix}=\dfrac{n_1P_1+n_2P_2+\cdots}{\sum n}\text{ (Pa)}$}
    \item[] \B{মোট মোলসংখ্যা:} {\lat $\sum n = n_1 + n_2 + \cdots$}
\end{itemize}

\itm{7} \textbf{\B{মোলার আপেক্ষিক তাপ ও স্বাধীনতার মাত্রা:}}
\begin{itemize}
    \item[] \B{মেয়ারের সূত্র:} {\lat $C_p-C_v=R$ \;\; [একক: $\text{J}\cdot\text{mol}^{-1}\cdot\text{K}^{-1}$]}
    \item[] \B{স্থির আয়তনে মোলার আপেক্ষিক তাপ ও স্বাধীনতার মাত্রা:} {\lat $C_v=\dfrac{f}{2}R$}
    \item[] \B{স্থির চাপে মোলার আপেক্ষিক তাপ ও স্বাধীনতার মাত্রা:} {\lat $C_p=\left(\dfrac{f}{2}+1\right)R$}
    \item[] \B{আপেক্ষিক তাপের অনুপাত ও স্বাধীনতার মাত্রা:} {\lat $\gamma=\dfrac{C_p}{C_v}=1+\dfrac{2}{f}$}
    \item[] \B{একপরমাণুক গ্যাস (Monoatomic):} {\lat $f=3$}
    \item[] \B{একপরমাণুক গ্যাসের ক্ষেত্রে $C_v$ এর মান:} {\lat $C_v=\tfrac{3}{2}R$}
    \item[] \B{একপরমাণুক গ্যাসের ক্ষেত্রে $C_p$ এর মান:} {\lat $C_p=\tfrac{5}{2}R$}
    \item[] \B{একপরমাণুক গ্যাসের ক্ষেত্রে $\gamma$ এর মান:} {\lat $\gamma=\tfrac{5}{3}=1.67$}
    \item[] \B{দ্বিপরমাণুক গ্যাস (Diatomic):} {\lat $f=5$}
    \item[] \B{দ্বিপরমাণুক গ্যাসের ক্ষেত্রে $C_v$ এর মান:} {\lat $C_v=\tfrac{5}{2}R$}
    \item[] \B{দ্বিপরমাণুক গ্যাসের ক্ষেত্রে $C_p$ এর মান:} {\lat $C_p=\tfrac{7}{2}R$}
    \item[] \B{দ্বিপরমাণুক গ্যাসের ক্ষেত্রে $\gamma$ এর মান:} {\lat $\gamma=\tfrac{7}{5}=1.4$}
    \item[] \B{বহুপরমাণুক / ত্রিপরমাণুক গ্যাস (Polyatomic):} {\lat $f=6$}
    \item[] \B{বহুপরমাণুক গ্যাসের ক্ষেত্রে $C_v$ এর মান:} {\lat $C_v=3R$}
    \item[] \B{বহুপরমাণুক গ্যাসের ক্ষেত্রে $C_p$ এর মান:} {\lat $C_p=4R$}
    \item[] \B{বহুপরমাণুক গ্যাসের ক্ষেত্রে $\gamma$ এর মান:} {\lat $\gamma=\tfrac{4}{3}=1.33$}
    \item[] \B{অভ্যন্তরীণ শক্তি (আদি রূপ):} {\lat $dU=\dfrac{f}{2}nRdT$}
    \item[] \B{অভ্যন্তরীণ শক্তির পরিবর্তন (আপেক্ষিক তাপ দিয়ে):} {\lat $\Delta U=nC_v\Delta T$}
    \item[] \B{অভ্যন্তরীণ শক্তির পরিবর্তন (স্বাধীনতার মাত্রা সহ):} {\lat $\Delta U=\tfrac{f}{2}nR\Delta T$}
\end{itemize}

\itm{8} \textbf{\B{গ্যাসের গতিতত্ত্ব ও বেগ:}}
\begin{itemize}
    \item[] \B{গ্যাসের গতিতত্ত্বের মূল সমীকরণ:} {\lat $P=\tfrac{1}{3}\rho\overline{c^2}$}
    \item[] \B{গতিতত্ত্বের সমীকরণ (অণু ও ভরসহ):} {\lat $P=\tfrac{1}{3}\dfrac{Nm}{V}\overline{c^2}$}
    \item[] \B{মূল-গড়-বর্গ বেগ ($c_{\rm rms}$ মোলার ভর দিয়ে):} {\lat $c_{\rm rms}=\sqrt{\dfrac{3RT}{M}}$}
    \item[] \B{মূল-গড়-বর্গ বেগ ($c_{\rm rms}$ অণুর ভর দিয়ে):} {\lat $c_{\rm rms}=\sqrt{\dfrac{3kT}{m}}$}
    \item[] \B{মূল-গড়-বর্গ বেগ ($c_{\rm rms}$ ঘনত্ব ও চাপ দিয়ে):} {\lat $c_{\rm rms}=\sqrt{\dfrac{3P}{\rho}}$}
    \item[] \B{গড় বেগ ($\bar c$ মোলার ভর দিয়ে):} {\lat $\bar c=\sqrt{\dfrac{8RT}{\pi M}}$}
    \item[] \B{গড় বেগ ($\bar c$ অণুর ভর দিয়ে):} {\lat $\bar c=\sqrt{\dfrac{8kT}{\pi m}}$}
    \item[] \B{সবচেয়ে সম্ভাব্যতম বেগ ($c_p$ মোলার ভর দিয়ে):} {\lat $c_p=\sqrt{\dfrac{2RT}{M}}$}
    \item[] \B{সবচেয়ে সম্ভাব্যতম বেগ ($c_p$ অণুর ভর দিয়ে):} {\lat $c_p=\sqrt{\dfrac{2kT}{m}}$}
    \item[] \B{বেগত্রয়ের অনুপাত:} {\lat $c_p:\bar c:c_{\rm rms}=\sqrt 2:\sqrt{8/\pi}:\sqrt 3$}
    \item[] \B{একটি অণুর গড় গতিশক্তি:} {\lat $E_k=\tfrac{3}{2}kT$}
    \item[] \B{$f$ স্বাধীনতা মাত্রায় মোট গতিশক্তি:} {\lat $E=\tfrac{f}{2}kT$}
    \item[] \B{গড় মুক্তপথ (ক্লসিয়াস/ম্যাক্সওয়েল রূপ):} {\lat $\lambda=\dfrac{1}{\sqrt 2\,\pi d^2 n}$}
    \item[] \B{গড় মুক্তপথ (চাপ ও তাপমাত্রা দিয়ে):} {\lat $\lambda=\dfrac{kT}{\sqrt 2\,\pi d^2 P}$}
    \item[] \B{অ্যাভোগাড্রো সংখ্যা ($N_A$):} {\lat $6.022\times10^{23}\text{ mol}^{-1}$}
    \item[] {\lat $\rho$} = \B{ঘনত্ব}
    \item[] {\lat $M$} = \B{মোলার ভর}
    \item[] {\lat $d$} = \B{অণু ব্যাস}
    \item[] {\lat $f$} = \B{স্বাধীনতার মাত্রা}
\end{itemize}

\itm{9} \textbf{\B{তাপগতিবিদ্যার ৪টি মূল সূত্র:}}
\begin{itemize}
    \item[] \B{০-তম সূত্র:} \B{তাপীয় সাম্য সকর্মক (transitive)}
    \item[] \B{১ম সূত্র (ডিফারেনশিয়াল রূপ):} {\lat $dQ = dU + dW$}
    \item[] \B{১ম সূত্র (সসীম পরিবর্তন রূপ):} {\lat $\Delta Q=\Delta U+\Delta W$}
    \item[] {\lat $dQ$ বা $\Delta Q$} = \B{গৃহীত/বর্জিত তাপ}
    \item[] {\lat $dU$ বা $\Delta U$} = \B{অভ্যন্তরীণ শক্তির পরিবর্তন}
    \item[] {\lat $dW$ বা $\Delta W$} = \B{কাজ}
    \item[] \B{২য় সূত্র (ক্লসিয়াস/কেলভিন বিবৃতি):} \B{বদ্ধ চক্রে} {\lat $\oint \dfrac{dQ}{T}\le0$}
    \item[] \B{৩য় সূত্র:} {\lat $T\to0\text{ K}$} \B{তে এন্ট্রপি} {\lat $\to0$}
\end{itemize}

\itm{10} \textbf{\B{বিভিন্ন তাপগতীয় প্রক্রিয়ায় কৃতকাজ ও পরিবর্তন:}}
\begin{itemize}
    \item[] \B{১. সমচাপ প্রক্রিয়া ($P$ constant):} {\lat $dQ=dU+P dV$}
    \item[] \B{সমচাপ প্রক্রিয়ায় কৃতকাজ:} {\lat $dW=P\Delta V=nR\Delta T$}
    \item[] \B{সমচাপ প্রক্রিয়া বৈশিষ্ট্য:} \B{চার্লসের সূত্র প্রযোজ্য।}
    \item[] \B{২. সমইউষ্ণ প্রক্রিয়া ($V$ constant):} {\lat $dW=0$}
    \item[] \B{সমআয়তন প্রক্রিয়ায় তাপ ও শক্তি:} {\lat $dQ=dU=nC_v dT$}
    \item[] \B{সমআয়তন প্রক্রিয়া বৈশিষ্ট্য:} \B{চাপের সূত্র প্রযোজ্য।}
    \item[] \B{৩. সমউষ্ণ প্রক্রিয়া ($T$ constant):} {\lat $dU=0$}
    \item[] \B{সমউষ্ণ প্রক্রিয়ায় তাপ ও কাজের সম্পর্ক:} {\lat $dQ=dW$}
    \item[] \B{সমউষ্ণ প্রক্রিয়ার কৃতকাজ (আয়তন দিয়ে):} {\lat $W=nRT\ln\dfrac{V_2}{V_1}$}
    \item[] \B{সমউষ্ণ প্রক্রিয়ার কৃতকাজ (চাপ দিয়ে):} {\lat $W=nRT\ln\dfrac{P_1}{P_2}$}
    \item[] \B{সমউষ্ণ প্রক্রিয়ার মোট তাপ:} {\lat $Q=W$}
    \item[] \B{সমউষ্ণ প্রক্রিয়া বৈশিষ্ট্য:} \B{বয়েলের সূত্র প্রযোজ্য।}
    \item[] \B{৪. রুদ্ধতাপীয় প্রক্রিয়া ($Q$ constant):} {\lat $dQ=0$}
    \item[] \B{রুদ্ধতাপীয় প্রক্রিয়ায় কাজ ও শক্তি:} {\lat $dW=-dU$}
    \item[] \B{অবস্থার সমীকরণ (চাপ ও আয়তন):} {\lat $PV^\gamma=\text{const}$}
    \item[] \B{অবস্থার সমীকরণ (তাপমাত্রা ও আয়তন):} {\lat $TV^{\gamma-1}=\text{const}$}
    \item[] \B{অবস্থার সমীকরণ (তাপমাত্রা ও চাপ):} {\lat $T^\gamma P^{1-\gamma}=\text{const}$}
    \item[] \B{রুদ্ধতাপীয় কৃতকাজ (মোলার আপেক্ষিক তাপ দিয়ে):} {\lat $W=nC_v(T_1-T_2)$}
    \item[] \B{রুদ্ধতাপীয় কৃতকাজ (তাপমাত্রা দিয়ে):} {\lat $W=\dfrac{nR(T_1-T_2)}{\gamma-1}$}
    \item[] \B{রুদ্ধতাপীয় কৃতকাজ (চাপ ও আয়তন দিয়ে):} {\lat $W=\dfrac{P_1V_1-P_2V_2}{\gamma-1}$}
    \item[] \B{সমউষ্ণ রেখার ঢাল:} {\lat $-\left(\dfrac{P}{V}\right)$}
    \item[] \B{রুদ্ধতাপীয় রেখার ঢাল:} {\lat $-\gamma\left(\dfrac{P}{V}\right)$}
    \item[] {\lat $\gamma=C_p/C_v$} = \B{আপেক্ষিক তাপের অনুপাত}
\end{itemize}

\itm{11} \textbf{\B{কার্নো ইঞ্জিন ও এন্ট্রপির পরিবর্তন:}}
\begin{itemize}
    \item[] \B{কর্মদক্ষতা (তাপমাত্রা দিয়ে):} {\lat $\eta=\left(1-\dfrac{T_2}{T_1}\right)\times100\%$}
    \item[] \B{কর্মদক্ষতা (তাপশক্তি দিয়ে):} {\lat $\eta=\left(1-\dfrac{Q_2}{Q_1}\right)\times100\%$}
    \item[] \B{কর্মদক্ষতা (কাজ ও তাপ দিয়ে):} {\lat $\eta=\dfrac{W}{Q_1}\times100\%$}
    \item[] \B{মোট কৃতকাজ:} {\lat $W=Q_1-Q_2$}
    \item[] \B{কার্নো চক্রের চার ধাপের কাজ:} {\lat $W = W_1+W_2-W_3-W_4$}
    \item[] \B{প্রত্যাগামী চক্রের অনুপাত:} {\lat $\dfrac{Q_1}{T_1}=\dfrac{Q_2}{T_2}$}
    \item[] \B{প্রত্যাগামী চক্রের সমাকলন রূপ:} {\lat $\oint \dfrac{dQ}{T}=0$}
    \item[] \B{কার্নো চক্রের আয়তনের সম্পর্ক:} {\lat $\dfrac{V_2}{V_1}=\dfrac{V_3}{V_4}$}
    \item[] \B{এন্ট্রপির সাধারণ সমীকরণ:} {\lat $\Delta S=\dfrac{\Delta Q}{T}$}
    \item[] \B{তাপমাত্রা পরিবর্তনে এন্ট্রপির পরিবর্তন:} {\lat $\Delta S=ms\ln\left(\dfrac{T_f}{T_i}\right)$}
    \item[] \B{অবস্থা পরিবর্তনে এন্ট্রপির পরিবর্তন:} {\lat $\Delta S = \dfrac{mL}{T}$}
    \item[] \B{সমউষ্ণ প্রক্রিয়ায় এন্ট্রপির পরিবর্তন:} {\lat $dS=nR\ln\left(\dfrac{V_2}{V_1}\right)$}
    \item[] \B{সমচাপ প্রক্রিয়ায় এন্ট্রপির পরিবর্তন:} {\lat $dS=nC_p\ln\left(\dfrac{T_f}{T_i}\right)$}
    \item[] \B{সমআয়তন প্রক্রিয়ায় এন্ট্রপির পরিবর্তন:} {\lat $dS=nC_v\ln\left(\dfrac{T_f}{T_i}\right)$}
    \item[] \B{রুদ্ধতাপীয় প্রক্রিয়ায় এন্ট্রপির পরিবর্তন:} {\lat $dS=0$}
    \item[] \B{অপ্রত্যাগামী চক্রে মোট এন্ট্রপির পরিবর্তন:} {\lat $\Delta S>0$}
    \item[] {\lat $Q_1$} = \B{উৎস থেকে গৃহীত তাপ}
    \item[] {\lat $T_1$} = \B{উৎসের তাপমাত্রা (K)}
    \item[] {\lat $Q_2$} = \B{গ্রাহকে বর্জিত তাপ}
    \item[] {\lat $T_2$} = \B{গ্রাহকের তাপমাত্রা (K)}
    \item[] {\lat $W_1, W_2, W_3, W_4$} = \B{কার্নো চক্রের চার ধাপে সম্পন্ন কৃতকাজ}
\end{itemize}

\itm{12} \textbf{\B{কার্নো রেফ্রিজারেটর ও হিট পাম্প:}}
\begin{itemize}
    \item[] \B{রেফ্রিজারেটরের কাজের সমীকরণ:} {\lat $W=Q_1-Q_2$}
    \item[] \B{রেফ্রিজারেটরের তাপমাত্রা অনুপাত:} {\lat $\dfrac{Q_1}{T_1}=\dfrac{Q_2}{T_2}$}
    \item[] \B{রেফ্রিজারেটরের কার্যকৃত্ব গুণাঙ্ক ($\psi$):} {\lat $\psi = \dfrac{Q_2}{W}$}
    \item[] \B{রেফ্রিজারেটরের কার্যকৃত্ব গুণাঙ্ক ($\beta$ তাপশক্তি দিয়ে):} {\lat $\beta = \dfrac{Q_2}{Q_1-Q_2}$}
    \item[] \B{রেফ্রিজারেটরের কার্যকৃত্ব গুণাঙ্ক ($\beta$ তাপমাত্রা দিয়ে):} {\lat $\beta = \dfrac{T_2}{T_1-T_2}$}
    \item[] \B{হিট পাম্পের কার্যকৃত্ব গুণাঙ্ক ($\beta'$ তাপশক্তি দিয়ে):} {\lat $\beta'=\dfrac{Q_1}{W}$}
    \item[] \B{হিট পাম্পের কার্যকৃত্ব গুণাঙ্ক ($\beta'$ তাপমাত্রা দিয়ে):} {\lat $\beta'=\dfrac{T_1}{T_1-T_2}$}
    \item[] \B{হিট পাম্প ও রেফ্রিজারেটরের COP সম্পর্ক:} {\lat $\beta'=1+\beta$}
    \item[] {\lat $W$} = \B{কম্প্রেসার কর্তৃক প্রযুক্ত তড়িৎশক্তি (J)}
    \item[] {\lat $Q_1$} = \B{পরিবেশে বর্জিত তাপ (J)}
    \item[] {\lat $Q_2$} = \B{খাবার বা হিমাঙ্ক হতে গৃহীত তাপ (J)}
    \item[] {\lat $T_1$} = \B{পরিবেশের তাপমাত্রা (K)}
    \item[] {\lat $T_2$} = \B{হিমাঙ্কের তাপমাত্রা (K)}
\end{itemize}

\itm{13} \textbf{\B{তাপ পরিবহন ও বিকিরণ:}}
\begin{itemize}
    \item[] \B{তাপ পরিবহন সমীকরণ:} {\lat $\dfrac{Q}{t}=k_{\rm th}A\dfrac{\Delta T}{l}$}
    \item[] \B{স্টেফান-বোলৎজম্যান সূত্র:} {\lat $E=\sigma T^4$}
    \item[] \B{স্টেফান-বোলৎজম্যান ধ্রুবক ($\sigma$):} {\lat $\sigma=5.67\times10^{-8}\text{ W/m}^2\text{K}^4$}
    \item[] \B{নিউটনের শীতলীকরণ সূত্র:} {\lat $\dfrac{dT}{dt}=-k(T-T_0)$}
    \item[] \B{ভিয়েনের সরণ সূত্র:} {\lat $\lambda_{\max}T=2.898\times10^{-3}\text{ m}\cdot\text{K}$}
    \item[] \B{কার্শফের সূত্র:} \B{ভালো শোষক $=$ ভালো বিকীর্ণক}
    \item[] {\lat $k_{\rm th}$} = \B{তাপ পরিবাহিতা}
    \item[] {\lat $A$} = \B{ক্ষেত্রফল}
    \item[] {\lat $l$} = \B{পুরুত্ব}
\end{itemize}

\chsec{অধ্যায়-২: স্থির তড়িৎ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{কোন বস্তুর মোট আধান/চার্জ,}} {\lat $Q = \pm ne$}
\begin{itemize}
    \item[] {\lat $n = \pm 1, \pm 2, \pm 3, \dots$};\; {\lat $e = 1.6 \times 10^{-19} \text{ C}$ (একটি ইলেকট্রনের আধান)}
    \item[] {\lat $1 \text{ C} = 3 \times 10^9 \text{ esu}$};\; {\lat $1 \text{ esu} = 3.33 \times 10^{-10} \text{ C}$}
\end{itemize}

\itm{2} \textbf{\B{কুলম্বের সূত্র ও ডাইইলেক্ট্রিক ধ্রুবক,}} {\lat $F = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{q_1 q_2}{r^2} = 9 \times 10^9 \dfrac{q_1 q_2}{K r^2}$}
\begin{itemize}
    \item[] \B{শূন্য বা বায়ু মাধ্যমের জন্য ($K=1$):} {\lat $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1 q_2}{r^2} = 9 \times 10^9 \dfrac{q_1 q_2}{r^2}$}
    \item[] \B{আপেক্ষিক ভেদনযোগ্যতা (ডাইইলেক্ট্রিক ধ্রুবক):} {\lat $K = \dfrac{\varepsilon_m}{\varepsilon_0}$}
    \item[] {\lat $F$} = \B{কুলম্ব বল} {\lat [N]};\; {\lat $q_1, q_2$} = \B{চার্জদ্বয়} {\lat [C]};\; {\lat $r$} = \B{মধ্যবর্তী দূরত্ব} {\lat [m]}
    \item[] {\lat $\varepsilon_0 = 8.854 \times 10^{-12} \text{ C}^2\text{N}^{-1}\text{m}^{-2} \text{ \text{\B{বা }}F/m} (\text{\B{শূন্য মাধ্যমের ভেদনযোগ্যতা}})$}
    \item[] {\lat $\varepsilon_m$} = \B{অন্য যেকোনো মাধ্যমের ভেদনযোগ্যতা}
\end{itemize}

\itm{3} \textbf{\B{কুলম্ব বলের ভেক্টর রূপ,}} {\lat $\vec{F} = \dfrac{1}{4\pi\varepsilon_0 K} \dfrac{q_1 q_2}{r^3} \vec{r}$}
\begin{itemize}
    \item[] {\lat $\vec{r}$} = \B{অবস্থান ভেক্টর};\; {\lat $r = |\vec{r}|$} = \B{দূরত্বের মান}
\end{itemize}

\itm{4} \textbf{\B{তড়িৎ প্রাবল্য ও বলের সম্পর্ক,}} {\lat $E = \dfrac{F}{q} \implies F = qE$}
\begin{itemize}
    \item[] {\lat $E$} = \B{তড়িৎ প্রাবল্য} {\lat [NC$^{-1}$ বা V/m]};\; {\lat $q$} = \B{আধান বা চার্জ} {\lat [C]}
\end{itemize}

\itm{5} \textbf{\B{তড়িৎ ক্ষেত্রের তীব্রতা (বিন্দু চার্জের জন্য),}} {\lat $E = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{r^2}$}
\begin{itemize}
    \item[] \B{শূন্য মাধ্যমের জন্য ($K=1$):} {\lat $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}$}
\end{itemize}

\itm{6} \textbf{\B{প্রাবল্যের সাম্যাবস্থা (ভারসাম্য অবস্থা),}} {\lat $mg = qE$}
\begin{itemize}
    \item[] {\lat $m$} = \B{বস্তুর ভর} {\lat [kg]};\; {\lat $g = 9.8 \text{ ms}^{-2}$} = \B{অভিকর্ষজ ত্বরণ}
\end{itemize}

\itm{7} \textbf{\B{নিরপেক্ষ বিন্দু বা শূন্য প্রাবল্য বিন্দুর অবস্থান নির্ধারণ,}}
\begin{itemize}
    \item[] \B{সমধর্মী চার্জের ক্ষেত্রে (+ এবং + অথবা - এবং -):} {\lat $x = \dfrac{d}{\sqrt{\dfrac{q_2}{q_1}} + 1}$}
    \item[] \B{বিপরীতধর্মী চার্জের ক্ষেত্রে (+ এবং -):} {\lat $x = \dfrac{d}{\sqrt{\dfrac{q_2}{q_1}} - 1}$}
    \item[] {\lat $d$} = \B{চার্জদ্বয়ের মধ্যবর্তী দূরত্ব} {\lat [m]};\; {\lat $x$} = \B{$q_1$ চার্জ হতে নিরপেক্ষ বিন্দুর দূরত্ব} {\lat [m]} (এখানে {\lat $q_2 > q_1$})
\end{itemize}

\itm{8} \textbf{\B{বিভব ও প্রাবল্যের সম্পর্ক,}} {\lat $E = -\dfrac{dV}{dr} = -\dfrac{V}{d}$}
\begin{itemize}
    \item[] \B{সমান্তরাল পাতের ক্ষেত্রে বিভব:} {\lat $V = Ed$}
\end{itemize}

\itm{9} \textbf{\B{লব্ধি তড়িৎ প্রাবল্য,}} {\lat $E = \sqrt{E_1^2 + E_2^2 + 2E_1E_2\cos\theta}$}
\begin{itemize}
    \item[] {\lat $\theta$} = \B{$\vec{E}_1$ ও $\vec{E}_2$ প্রাবল্য ভেক্টরের মধ্যবর্তী কোণ}
\end{itemize}

\itm{10} \textbf{\B{তলমাত্রিক ঘনত্ব (আধানের পৃষ্ঠ ঘনত্ব),}} {\lat $\sigma = \dfrac{Q}{A} = \dfrac{Q}{4\pi R^2}$}
\begin{itemize}
    \item[] {\lat $\sigma$} = \B{তলমাত্রিক ঘনত্ব} {\lat [Cm$^{-2}$]};\; {\lat Q} = \B{মোট চার্জ};\; {\lat R} = \B{গোলকের ব্যাসার্ধ} {\lat [m]}
\end{itemize}

\itm{11} \textbf{\B{আধান স্থানান্তরে বাহ্যিক এজেন্ট দ্বারা কৃতকাজ,}} {\lat $W = \dfrac{Qq}{4\pi\varepsilon_0}\left(\dfrac{1}{x_1} - \dfrac{1}{x_2}\right)$}
\begin{itemize}
    \item[] \B{বিভব পার্থক্যের সাপেক্ষে কাজ:} {\lat $W = \Delta V \cdot q = q(V_f - V_i)$}
    \item[] {\lat $x_1$} = \B{আদি অবস্থান};\; {\lat $x_2$} = \B{শেষ অবস্থান};\; {\lat $V_i, V_f$} = \B{আদি ও শেষ বিভব} {\lat [V]}
\end{itemize}

\itm{12} \textbf{\B{তড়িৎ বিভব (বিন্দু চার্জের জন্য),}} {\lat $V = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{r}$}
\begin{itemize}
    \item[] {\lat $V$} = \B{বিভব} {\lat [V \B{বা} JC$^{-1}$]};\; {\lat Q} = \B{উৎস চার্জ} {\lat [C]};\; {\lat r} = \B{দূরত্ব} {\lat [m]}
\end{itemize}

\itm{13} \textbf{\B{তড়িৎ ফ্লাক্স,}} {\lat $\Phi_E = \vec{E}\cdot\vec{A} = AE\cos\theta$}
\begin{itemize}
    \item[] {\lat $\vec{A}$} = \B{ক্ষেত্রফল ভেক্টর};\; {\lat $\theta$} = \B{$\vec{E}$ ও $\vec{A}$ এর মধ্যবর্তী কোণ}
\end{itemize}

\itm{14} \textbf{\B{চার্জিত গোলকের ক্ষেত্রে বিভব ও প্রাবল্যের বিভিন্ন শর্তসমূহ,}}
\begin{itemize}
    \item[] \B{পৃষ্ঠে ও অভ্যন্তরে বিভব:} {\lat $V = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{R}$}
    \item[] \B{বাহিরে বিভব ($r > R$):} {\lat $V = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{r}$}
    \item[] \B{অভ্যন্তরে প্রাবল্য:} {\lat $E = 0$ (ফাঁপা গোলকের ভেতর)}
    \item[] \B{পৃষ্ঠে প্রাবল্য:} {\lat $E = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{R^2}$}
    \item[] \B{বাহিরে প্রাবল্য ($r > R$):} {\lat $E = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{Q}{r^2}$}
    \item[] {\lat R} = \B{গোলকের ব্যাসার্ধ} {\lat [m]};\; {\lat r} = \B{কেন্দ্র হতে বিন্দুর দূরত্ব} {\lat [m]}
\end{itemize}

\itm{15} \textbf{\B{ধারকত্ব,}} {\lat $C = \dfrac{Q}{V}$}
\begin{itemize}
    \item[] \B{বিচ্ছিন্ন পরিবাহী গোলকের ধারকত্ব:} {\lat $C = 4\pi\varepsilon_0 K R$}
    \item[] {\lat $C$} = \B{ধারকত্ব} {\lat [Farad (F)]};\; {\lat Q} = \B{আধান};\; {\lat V} = \B{বিভব পার্থক্য}
\end{itemize}

\itm{16} \textbf{\B{ধারকের সমবায় (তুল্য ধারকত্ব),}}
\begin{itemize}
    \item[] \B{শ্রেণী সমবায় (Series):} {\lat $\dfrac{1}{C_s} = \dfrac{1}{C_1} + \dfrac{1}{C_2} + \dots + \dfrac{1}{C_n}$}
    \item[] \B{সমান্তরাল সমবায় (Parallel):} {\lat $C_p = C_1 + C_2 + \dots + C_n$}
    \item[] \B{$n$ সংখ্যক একই মানের ($C$) ধারকের ক্ষেত্রে:} 
    \item[] \B{শ্রেণীতে শ্রেণীভুক্ত হলে:} {\lat $C_s = \dfrac{C}{n}$};\; \B{সমান্তরালে যুক্ত হলে:} {\lat $C_p = nC$}
\end{itemize}

\itm{17} \textbf{\B{সমান্তরাল পাত ধারক ও ডাইইলেক্ট্রিক প্রভাব,}} {\lat $C = \dfrac{K\varepsilon_0 A}{d}$}
\begin{itemize}
    \item[] \B{পাতদ্বয়ের মাঝে $t$ পুরুত্বের ও $K$ ডাইইলেক্ট্রিকের মাধ্যম আংশিক রাখলে:} {\lat $C_{eq} = \dfrac{\varepsilon_0 A}{(d-t) + \dfrac{t}{K}}$}
    \item[] {\lat A} = \B{পাতের ক্ষেত্রফল} {\lat [m$^2$]};\; {\lat d} = \B{পাতদ্বয়ের মধ্যবর্তী দূরত্ব} {\lat [m]}
\end{itemize}

\itm{18} \textbf{\B{শ্রেণী সমবায়ে বিভব বিভাজন পদ্ধতি,}}
\begin{itemize}
    \item[] {\lat $V_1 = \dfrac{C_2}{C_1 + C_2}V$};\; {\lat $V_2 = \dfrac{C_1}{C_1 + C_2}V$}
    \item[] {\lat V} = \B{মোট প্রয়োগকৃত বিভব};\; {\lat $V_1, V_2$} = \B{যথাক্রমে $C_1, C_2$ এর প্রান্তীয় বিভব}
\end{itemize}

\itm{19} \textbf{\B{সমান্তরাল সমবায়ে আধান বিভাজন পদ্ধতি,}}
\begin{itemize}
    \item[] {\lat $Q_1 = \dfrac{C_1}{C_1 + C_2}Q$};\; {\lat $Q_2 = \dfrac{C_2}{C_1 + C_2}Q$}
    \item[] {\lat Q} = \B{মোট আধান};\; {\lat $Q_1, Q_2$} = \B{যথাক্রমে $C_1, C_2$ তে সঞ্চিত আধান}
\end{itemize}

\itm{20} \textbf{\B{ধারকের সঞ্চিত শক্তি ও শক্তি ঘনত্ব,}}
\begin{itemize}
    \item[] \B{মোট সঞ্চিত শক্তি:} {\lat $U = \dfrac{1}{2}QV = \dfrac{1}{2}CV^2 = \dfrac{Q^2}{2C}$}
    \item[] \B{একক আয়তনের সঞ্চিত শক্তি (শক্তি ঘনত্ব):} {\lat $u = \dfrac{U}{V} = \dfrac{1}{2}K\varepsilon_0 E^2$}
    \item[] {\lat U} = \B{সঞ্চিত শক্তি} {\lat [J]};\; {\lat u} = \B{শক্তি ঘনত্ব} {\lat [Jm$^{-3}$]};\; {\lat V} = \B{আয়তন} {\lat [m$^3$]}
\end{itemize}

\itm{21} \textbf{\B{ধারকের সংযোগ ও আধান বন্টন (সাধারণ বিভব),}}
\begin{itemize}
    \item[] \B{সংযোগের পূর্বে মোট আধান:} {\lat $Q_1 = C_1V_1,\; Q_2 = C_2V_2$}
    \item[] \B{সংযোগের পরে মোট আধান:} {\lat $Q_1' = C_1V,\; Q_2' = C_2V$}
    \item[] \B{সাধারণ বিভব:} {\lat $V = \dfrac{C_1V_1 + C_2V_2}{C_1 + C_2}$}
    \item[] \B{আধান সংরক্ষণশীলতা নীতি নীতি:} {\lat $Q_1 + Q_2 = Q_1' + Q_2'$}
\end{itemize}

\itm{22} \textbf{\B{তড়িৎ দ্বিমেরু ভ্রামক,}} {\lat $\vec{p} = q \cdot (2\vec{l})$}
\begin{itemize}
    \item[] {\lat $\vec{p}$} = \B{দ্বিমেরু ভ্রামক} {\lat [C$\cdot$m]};\; {\lat 2l} = \B{দ্বিমেরুর মধ্যবর্তী দূরত্ব} {\lat [m]}
\end{itemize}

\itm{23} \textbf{\B{দ্বিমেরুর জন্য যেকোনো বিন্দুতে প্রাবল্য ও বিভব,}}
\begin{itemize}
    \item[] \B{তড়িৎ প্রাবল্য:} {\lat $E_p = \dfrac{1}{4\pi\varepsilon_0 K} \cdot \dfrac{p}{r^3}\sqrt{1 + 3\cos^2\theta}$}
    \item[] \B{তড়িৎ বিভব:} {\lat $V_p = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{p\cos\theta}{r^2}$}
    \item[] {\lat r} = \B{দ্বিমেরুর কেন্দ্র হতে বিন্দুর দূরত্ব} {\lat [m]};\; {\lat $\theta$} = \B{দ্বিমেরুর অক্ষের সাথে উৎপন্ন কোণ}
\end{itemize}

\itm{24} \textbf{\B{দ্বিমেরুর নির্দিষ্ট অবস্থানের জন্য শর্তসমূহ,}}
\begin{itemize}
    \item[] \B{লম্ব দ্বিখণ্ডকের উপর ({\lat $\theta = 90^\circ$}):} {\lat $V = 0$};\; {\lat $E = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{p}{r^3}$}
    \item[] \B{অক্ষের উপর ({\lat $\theta = 0^\circ$}):} {\lat $V = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{p}{r^2}$};\; {\lat $E = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{2p}{r^3}$}
\end{itemize}

\itm{25} \textbf{\B{গাউসের সূত্র ও সুষম আধানের জন্য প্রয়োগ,}} 
\begin{itemize}
    \item[] \B{তড়িৎ ফ্লাক্স:} {\lat $\Phi_E = \oint \vec{E}\cdot d\vec{A} = \dfrac{q}{\varepsilon_0}$}
    \item[] \B{সুষমভাবে চার্জিত অসীম দৈর্ঘ্যের সোজা তারের জন্য প্রাবল্য:} {\lat $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$}
    \item[] {\lat $\lambda = \dfrac{Q}{L}$} = \B{রৈখিক চার্জ ঘনত্ব (একক দৈর্ঘ্যের আধান)} {\lat [Cm$^{-1}$]};\; {\lat r} = \B{তার হতে লম্ব দূরত্ব} {\lat [m]}
\end{itemize}


\chsec{অধ্যায়-৩: চল তড়িৎ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তড়িৎ প্রবাহ,}} {\lat $I=Q/t=nqAv_d$}
\begin{itemize}
    \item[] \B{প্রবাহ ঘনত্ব:} {\lat $J=I/A=\sigma E$}
    \item[] {\lat $I$} = \B{প্রবাহ} {\lat [A]};\; {\lat $n$} = \B{মুক্ত ইলেকট্রন ঘনত্ব};\; {\lat $v_d$} = \B{অপবাহ বেগ}
\end{itemize}

\itm{2} \textbf{\B{ওহমের সূত্র,}} {\lat $V=IR$;\; $R=\dfrac{\rho l}{A}$;\; $\sigma=1/\rho$}
\begin{itemize}
    \item[] {\lat $R$} = \B{রোধ} {\lat [$\Omega$]};\; {\lat $\rho$} = \B{আপেক্ষিক রোধ};\; {\lat $\sigma$} = \B{পরিবাহিতা}
\end{itemize}

\itm{3} \textbf{\B{তাপমাত্রা প্রভাব,}} {\lat $R_T=R_0(1+\alpha T)$;\; $\alpha=\dfrac{R_\theta-R_0}{R_0\theta}$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{রোধের তাপমাত্রা সহগ};\; {\lat $R_0,R_\theta$} = \B{0$^\circ$C ও $\theta^\circ$C-এ রোধ}
\end{itemize}

\itm{4} \textbf{\B{রোধের সমন্বয়:}}
\begin{itemize}
    \item[] \B{সিরিজ:} {\lat $R=R_1+R_2+\cdots+R_n$}
    \item[] \B{সমান্তরাল:} {\lat $\dfrac{1}{R_p}=\dfrac{1}{R_1}+\dfrac{1}{R_2}+\cdots+\dfrac{1}{R_n}$};\; \B{দুটি:} {\lat $R=\dfrac{R_1R_2}{R_1+R_2}$}
\end{itemize}

\itm{5} \textbf{\B{শক্তি ও ক্ষমতা,}} {\lat $W=VIt=I^2Rt=V^2t/R$;\; $P=VI=I^2R=V^2/R$}
\begin{itemize}
    \item[] \B{দক্ষতা:} {\lat $\eta=\dfrac{P_{\rm out}}{P_{\rm in}}\times100\%$}
\end{itemize}

\itm{6} \textbf{\B{জুলের তাপীয় সূত্র,}} {\lat $H=I^2Rt$ J $=0.24\,I^2Rt$ cal}
\begin{itemize}
    \item[] \B{সমান $R,t$:} {\lat $H\propto I^2$};\; \B{সমান $I,t$:} {\lat $H\propto R$};\; \B{সমান $I,R$:} {\lat $H\propto t$}
\end{itemize}

\itm{7} \textbf{\B{ফ্যারাডের তড়িৎবিশ্লেষণ:}}
\begin{itemize}
    \item[] \B{১ম সূত্র:} {\lat $m=Zit$}
    \item[] \B{২য় সূত্র:} {\lat $m_1/m_2=E_1/E_2$};\; {\lat $m=\dfrac{E\cdot Q}{F}$};\; {\lat $F=96500$ C/mol}
    \item[] {\lat $Z$} = \B{তড়িৎ-রসায়নিক সমতা};\; {\lat $E$} = \B{রাসায়নিক সমতা}
\end{itemize}

\itm{8} \textbf{\B{কির্শফের সূত্র:}}
\begin{itemize}
    \item[] {\lat (KCL)}: {\lat $\sum I_{\rm in}=\sum I_{\rm out}$}
    \item[] {\lat (KVL)}: {\lat $\sum\varepsilon=\sum IR$}
\end{itemize}

\itm{9} \textbf{\B{হুইটস্টোন সেতু (সাম্য),}} {\lat $\dfrac{P}{Q}=\dfrac{R}{S}$}
\begin{itemize}
    \item[] \B{মিটার সেতু:} {\lat $X=R\cdot\dfrac{100-l}{l}$}
\end{itemize}

\itm{10} \textbf{\B{পোটেনশিওমিটার:}}
\begin{itemize}
    \item[] {\lat $\dfrac{\varepsilon_1}{\varepsilon_2}=\dfrac{l_1}{l_2}$};\; \B{অভ্যন্তরীণ রোধ:} {\lat $r=R\!\left(\dfrac{l_1-l_2}{l_2}\right)$}
    \item[] \B{বিভাজক:} {\lat $V_{\rm out}=V_{\rm in}\cdot\dfrac{R_2}{R_1+R_2}$}
\end{itemize}

\itm{11} \textbf{\B{কোষ,}} {\lat $\varepsilon=V+Ir=I(R+r)$}
\begin{itemize}
    \item[] \B{শর্ট সার্কিট:} {\lat $I_{\rm sc}=\varepsilon/r$};\; \B{সর্বোচ্চ পাওয়ার:} {\lat $r=R$}
\end{itemize}

\itm{12} \textbf{\B{কোষের সমন্বয়:}}
\begin{itemize}
    \item[] \B{$n$ শ্রেণিতে:} {\lat $I=\dfrac{n\varepsilon}{R+nr}$}
    \item[] \B{$m$ সমান্তরালে:} {\lat $I=\dfrac{\varepsilon}{R+r/m}=\dfrac{m\varepsilon}{mR+r}$}
    \item[] \B{মিশ্র ($m$ সারি, $n$ শ্রেণিতে):} {\lat $I=\dfrac{mn\varepsilon}{mR+nr}$}
\end{itemize}

\chsec{অধ্যায়-৪: চৌম্বকবিদ্যা ও তড়িৎচৌম্বক আবেশ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বায়ো-সাভার্ট সূত্র (Biot-Savart Law):}}
\begin{itemize}
    \item[] \B{বায়ো-সাভার্ট সমীকরণ (ক্ষুদ্র অংশের জন্য):} {\lat $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2}$} %
    \item[] {\lat $dB$} = \B{ক্ষুদ্র পরিবাহী অংশের জন্য কোনো বিন্দুতে উৎপন্ন চৌম্বক ক্ষেত্র (T)} %
    \item[] {\lat $I$} = \B{পরিবাহীর মধ্য দিয়ে প্রবাহিত তড়িৎ প্রবাহ (A)} %
    \item[] {\lat $dl$} = \B{পরিবাহীর অত্যন্ত ক্ষুদ্র দৈর্ঘ্য (m)} %
    \item[] {\lat $r$} = \B{পরিবাহীর আল্পাংশ (dl) হতে ওই বিন্দুর দূরত্ব (m)} %
    \item[] {\lat $\theta$} = \B{তড়িৎ প্রবাহের দিক এবং দূরত্বের মধ্যবর্তী কোণ} %
    \item[] {\lat $\mu_0$} = \B{শূন্যস্থানের চৌম্বক ভেদ্যতা ($4\pi \times 10^{-7} \text{ T m A}^{-1}$)} %
\end{itemize}

\itm{2} \textbf{\B{বিভিন্ন পরিবাহীর জন্য চৌম্বক ক্ষেত্র (Magnetic Field for Different Conductors):}}
\begin{itemize}
    \item[] \B{অসীম দৈর্ঘ্যের সোজা তারের জন্য:} {\lat $B = \dfrac{\mu_0 I}{2\pi r}$} %
    \item[] \B{সীমিত দৈর্ঘ্যের সোজা তারের জন্য:} {\lat $B = \dfrac{\mu_0 I}{4\pi r}(\sin\theta_1+\sin\theta_2)$}
    \item[] \B{বৃত্তাকার কুণ্ডলীর কেন্দ্রে:} {\lat $B = \dfrac{\mu_0 I}{2R}$};\; \B{$N$ সংখ্যক পাকের জন্য:} {\lat $B = \dfrac{\mu_0 NI}{2R}$} %
    \item[] \B{বৃত্তাকার কুণ্ডলীর অক্ষের ওপর কোনো বিন্দুতে:} {\lat $B = \dfrac{\mu_0 NIR^2}{2(R^2+x^2)^{3/2}}$}
    \item[] \B{দীর্ঘ সোলেনয়েডের অভ্যন্তরে:} {\lat $B = \mu_0 nI = \mu_0 \dfrac{N}{l}I$}
    \item[] \B{টরয়েডের অভ্যন্তরে:} {\lat $B = \dfrac{\mu_0 NI}{2\pi r}$}
    \item[] {\lat $B$} = \B{চৌম্বক ফ্লাক্স ঘনত্ব বা চৌম্বক ক্ষেত্র (T)} %
    \item[] {\lat $R$} = \B{বৃত্তাকার কুণ্ডলীর ব্যাসার্ধ (m)} %
    \item[] {\lat $x$} = \B{কেন্দ্র হতে অক্ষের ওপর নির্দিষ্ট বিন্দুর দূরত্ব (m)}
    \item[] {\lat $n$} = \B{সোলেনয়েডের একক দৈর্ঘ্যে পাকসংখ্যা ($n = N/l$)}
    \item[] {\lat $l$} = \B{সোলেনয়েডের দৈর্ঘ্য (m)}
\end{itemize}

\itm{3} \textbf{\B{অ্যাম্পেয়ারের সূত্র (Ampere's Law):}}
\begin{itemize}
    \item[] \B{অ্যাম্পেয়ারের সূত্র:} {\lat $\oint\vec B\cdot d\vec l=\mu_0 I_{\rm enc}$} %
    \item[] {\lat $\oint\vec B\cdot d\vec l$} = \B{বদ্ধ পথ বরাবর চৌম্বক ক্ষেত্রের রেখাকলন (Line integral)} %
    \item[] {\lat $I_{\rm enc}$} = \B{বদ্ধ পথ দ্বারা আবদ্ধ মোট তড়িৎ প্রবাহ (A)} %
\end{itemize}

\itm{4} \textbf{\B{চৌম্বক বল ও লোরেন্ৎজ বল (Magnetic Force and Lorentz Force):}}
\begin{itemize}
    \item[] \B{লোরেন্ৎজ বল (তড়িৎ ও চৌম্বক ক্ষেত্রের যৌথ সমবায়):} {\lat $\vec F=q(\vec E + \vec v\times\vec B)$} %
    \item[] \B{গতিশীল আধানের ওপর চৌম্বক বল:} {\lat $\vec F=q(\vec v\times\vec B) \implies F = qvB\sin\theta$} %
    \item[] \B{চৌম্বক ক্ষেত্রের লম্বদিকে আধানের বৃত্তীয় গতি (ব্যাসার্ধ):} {\lat $r=\dfrac{mv}{qB}$}
    \item[] \B{ঘূর্ণন কম্পাঙ্ক:} {\lat $f=\dfrac{qB}{2\pi m}$}
    \item[] \B{তড়িৎবাহী তারের ওপর ক্রিয়াশীল চৌম্বক বল:} {\lat $\vec F=I(\vec l\times\vec B) \implies F = IlB\sin\theta$}
    \item[] \B{দুটি সমান্তরাল তারের প্রতি একক দৈর্ঘ্যে বল:} {\lat $F/l=\dfrac{\mu_0 I_1 I_2}{2\pi d}$} %
    \item[] {\lat $q$} = \B{আধানের পরিমাণ (C)} %
    \item[] {\lat $v$} = \B{আধানের বেগ ($\text{ms}^{-1}$)} %
    \item[] {\lat $m$} = \B{আহিত কণার ভর (kg)}
    \item[] {\lat $l$} = \B{চৌম্বক ক্ষেত্রের ভেতরে অবস্থিত তারের দৈর্ঘ্য (m)} %
    \item[] {\lat $d$} = \B{দুটি সমান্তরাল তারের মধ্যবর্তী লম্ব দূরত্ব (m)} %
\end{itemize}

\itm{5} \textbf{\B{হল প্রভাব (Hall Effect):}}
\begin{itemize}
    \item[] \B{হল বিভব (Hall Voltage):} {\lat $V_H=Bvd = \dfrac{BI}{ntq}$} %
    \item[] \B{হল গুণাঙ্ক (Hall Coefficient):} {\lat $R_H=1/(nq)$}
    \item[] {\lat $V_H$} = \B{হল বিভব পার্থক্য (V)} %
    \item[] {\lat $d$} = \B{পরিবাহীর প্রস্থ বা দুই প্রান্তের দূরত্ব (m)} %
    \item[] {\lat $t$} = \B{পরিবাহীর বেধ বা পুরুত্ব (m)} %
    \item[] {\lat $n$} = \B{একক আয়তনে মুক্ত আধানের সংখ্যা ($\text{m}^{-3}$)} %
\end{itemize}

\itm{6} \textbf{\B{চৌম্বক ভ্রামক ও টর্ক (Magnetic Moment and Torque):}}
\begin{itemize}
    \item[] \B{কুণ্ডলীর চৌম্বক দ্বিপদ ভ্রামক:} {\lat $\vec m=NI\vec A$} %
    \item[] \B{চৌম্বক ক্ষেত্রে কুণ্ডলীর ওপর প্রযুক্ত টর্ক:} {\lat $\tau = mB\sin\theta = NIAB\sin\theta$} %
    \item[] \B{চৌম্বক দ্বিপদের স্থিতিশক্তি:} {\lat $U=-\vec m\cdot\vec B = -mB\cos\theta$}
    \item[] {\lat $\vec m$} = \B{চৌম্বক ভ্রামক ভেক্টর ($\text{A m}^2$)} %
    \item[] {\lat $\vec A$} = \B{কুণ্ডলীর ক্ষেত্রফল ভেক্টর ($\text{m}^2$)} %
    \item[] {\lat $\tau$} = \B{টর্ক বা বিক্ষেপক দ্বন্দ্ব ($\text{N m}$)} %
\end{itemize}

\itm{7} \textbf{\B{গ্যালভানোমিটারের রূপান্তর (Galvanometer Conversion):}}
\begin{itemize}
    \item[] \B{অ্যামিটারে রূপান্তর (সমান্তরাল শান্ট রোধ):} {\lat $S = \dfrac{I_g G}{I-I_g} = \dfrac{G}{n-1}$};\; \B{প্রবাহ গুণক:} {\lat $n=I/I_g$}
    \item[] \B{ভোল্টমিটারে রূপান্তর (শ্রেণীতে উচ্চ রোধ):} {\lat $R_h = \dfrac{V}{I_g}-G$}
    \item[] {\lat $G$} = \B{গ্যালভানোমিটারের অভ্যন্তরীণ রোধ ($\Omega$)}
    \item[] {\lat $I_g$} = \B{গ্যালভানোমিটারের পূর্ণ স্কেল বিক্ষেপ প্রবাহ (A)}
    \item[] {\lat $S$} = \B{শান্ট রোধের মান ($\Omega$)}
    \item[] {\lat $I$} = \B{অ্যামিটার দ্বারা পরিমাপযোগ্য প্রধান উচ্চ প্রবাহ (A)}
    \item[] {\lat $R_h$} = \B{শ্রেণীবদ্ধভাবে যুক্ত উচ্চ রোধের মান ($\Omega$)}
    \item[] {\lat $V$} = \B{ভোল্টমিটার দ্বারা পরিমাপযোগ্য সর্বোচ্চ বিভব পার্থক্য (V)}
\end{itemize}

\itm{8} \textbf{\B{চৌম্বক পদার্থ ও প্রবণতা (Magnetic Materials and Susceptibility):}}
\begin{itemize}
    \item[] \B{চৌম্বক আবেশ সমীকরণ:} {\lat $B=\mu H$};\; \B{মাধ্যমের ক্ষেত্রে:} {\lat $B=\mu_0(H+I)=\mu_0\mu_r H$} %
    \item[] \B{চৌম্বক প্রবণতা (Susceptibility):} {\lat $\chi_m=I/H=\mu_r-1$} %
    \item[] \B{কুরির সূত্র (প্যারাচৌম্বক পদার্থের জন্য):} {\lat $\chi_m = \dfrac{C}{T}$}
    \item[] {\lat $H$} = \B{চৌম্বক তীব্রতা বা বলক্ষেত্র ($\text{A m}^{-1}$)} %
    \item[] {\lat $I$} = \B{পদার্থের চৌম্বকায়ন তীব্রতা ($\text{A m}^{-1}$)} %
    \item[] {\lat $\mu_r$} = \B{পদার্থের আপেক্ষিক চৌম্বক প্রবেশ্যতা} %
    \item[] {\lat $\chi_m$} = \B{চৌম্বক প্রবণতা (এককহীন)} %
    \item[] {\lat $T$} = \B{পরম তাপমাত্রা (K)}
\end{itemize}

\itm{9} \textbf{\B{ভূ-চৌম্বকত্ব (Earth's Magnetism):}}
\begin{itemize}
    \item[] \B{ভূ-চৌম্বক ক্ষেত্রের অনুভূমিক উপাংশ:} {\lat $H=I_e\cos\delta$} %
    \item[] \B{ভূ-চৌম্বক ক্ষেত্রের উল্লম্ব উপাংশ:} {\lat $V=I_e\sin\delta$} %
    \item[] \B{বিনতি কোণের সাথে সম্পর্ক:} {\lat $V/H=\tan\delta$} %
    \item[] \B{মোট ভূ-চৌম্বক তীব্রতা:} {\lat $I_e = \sqrt{H^2+V^2}$} %
    \item[] {\lat $I_e$} = \B{কোনো স্থানে পৃথিবীর মোট চৌম্বক তীব্রতা ($\text{A m}^{-1}$ বা T)} %
    \item[] {\lat $\delta$} = \B{বিনতি কোণ (Angle of dip)} %
\end{itemize}

\itm{10} \textbf{\B{তড়িৎচৌম্বক আবেশ ও ফ্যারাডের সূত্র (Electromagnetic Induction \& Faraday's Law):}}
\begin{itemize}
    \item[] \B{ফ্যারাডের ২য় সূত্র ও লেঞ্জের সূত্র (আবিষ্ট ভোল্টেজ):} {\lat $\varepsilon=-N\dfrac{d\Phi}{dt}=-N\dfrac{\Phi_2-\Phi_1}{t}$} %
    \item[] \B{চৌম্বক ফ্লাক্স:} {\lat $\Phi=\vec B \cdot \vec A = BA\cos\theta$} %
    \item[] \B{গতিশীল সোজা পরিবাহীতে আবিষ্ট তড়িচ্চালক শক্তি:} {\lat $\varepsilon=Blv\sin\theta$}
    \item[] {\lat $\varepsilon$} = \B{আবিষ্ট তড়িচ্চালক শক্তি বা ভোল্টেজ (V)} %
    \item[] {\lat $\Phi$} = \B{চৌম্বক ফ্লাক্স, এর একক ওয়েবার (Wb)} %
    \item[] {\lat $\theta$} = \B{ক্ষেত্রের দিক এবং তলের অভিলম্বের মধ্যবর্তী কোণ} %
    \item[] {\lat $l$} = \B{চৌম্বক ক্ষেত্রে গতিশীল পরিবাহী তারের দৈর্ঘ্য (m)}
    \item[] {\lat $v$} = \B{পরিবাহীর গতিবেগ ($\text{ms}^{-1}$)}
\end{itemize}

\itm{11} \textbf{\B{আবেশ গুণাঙ্ক ও সঞ্চিত শক্তি (Inductance and Stored Energy):}}
\begin{itemize}
    \item[] \B{স্বকীয় আবেশ গুণাঙ্ক সমীকরণ:} {\lat $\Phi=LI \implies \varepsilon=-L\dfrac{dI}{dt}$} %
    \item[] \B{দীর্ঘ সোলেনয়েডের স্বকীয় আবেশ গুণাঙ্ক:} {\lat $L=\mu_0 n^2 Al=\dfrac{\mu_0 N^2A}{l}$} %
    \item[] \B{পারস্পরিক আবেশ গুণাঙ্ক সমীকরণ:} {\lat $\varepsilon_2=-M\dfrac{dI_1}{dt}$};\; \B{যুগ্মন ধ্রুবক:} {\lat $M=k\sqrt{L_1L_2}$}
    \item[] \B{আবেশকে (ইন্ডাক্টর) সঞ্চিত চৌম্বক শক্তি:} {\lat $U=\dfrac{1}{2}LI^2$}
    \item[] {\lat $L$} = \B{স্বকীয় আবেশ গুণাঙ্ক, একক হেনরি (H)} %
    \item[] {\lat $M$} = \B{পারস্পরিক আবেশ গুণাঙ্ক (H)}
    \item[] {\lat $k$} = \B{যুগ্মন গুণাঙ্ক (Coupling coefficient, $0 \le k \le 1$)}
    \item[] {\lat $U$} = \B{কুণ্ডলীতে সঞ্চিত শক্তি (J)}
\end{itemize}

\itm{12} \textbf{\B{পরিবর্তী প্রবাহ ও রূপান্তরক (Alternating Current and Transformer):}}
\begin{itemize}
    \item[] \B{তাৎক্ষণিক এসি ভোল্টেজ ও প্রবাহ:} {\lat $E = E_0\sin\omega t$};\; {\lat $I = I_0\sin\omega t$} %
    \item[] \B{সর্বোচ্চ ভোল্টেজ (শীর্ষ মান):} {\lat $E_0 = NAB\omega = E_{\max}$} %
    \item[] \B{আরএমএস (RMS) বা আপাত মান:} {\lat $E_{\rm rms}=\dfrac{1}{\sqrt{2}}E_0$};\; {\lat $I_{\rm rms}=\dfrac{1}{\sqrt{2}}I_0$} %
    \item[] \B{রূপান্তরক বা ট্রান্সফরমারের সূত্র:} {\lat $\dfrac{E_s}{E_p}=\dfrac{N_s}{N_p}=\dfrac{I_p}{I_s}$} %
    \item[] \B{আদর্শ ট্রান্সফরমারের ক্ষমতা:} {\lat $P = E_p I_p = E_s I_s = I_{\rm rms}^2 R$} %
    \item[] {\lat $I_0, E_0$} = \B{যথাক্রমে প্রবাহ ও তড়িচ্চালক শক্তির শীর্ষ মান (Peak value)} %
    \item[] {\lat $\omega$} = \B{কৌণিক কম্পাঙ্ক ($\text{rad s}^{-1}$), যেখানে $\omega = 2\pi f$} %
    \item[] {\lat $p, s$} = \B{যথাক্রমে মুখ্য কুণ্ডলী (Primary) ও গৌণ কুণ্ডলী (Secondary)} %
    \item[] {\lat $N_p, N_s$} = \B{মুখ্য ও গৌণ কুণ্ডলীর পাকসংখ্যা} %
\end{itemize}


\chsec{অধ্যায়-৫: পরিবর্তী প্রবাহ (AC)}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তাৎক্ষণিক মান,}} {\lat $e=E_0\sin\omega t$;\; $i=I_0\sin(\omega t\pm\phi)$}

\itm{2} \textbf{\B{rms ও গড় মান:}} {\lat $E_{\rm rms}=E_0/\sqrt 2$;\; $E_{\rm avg}=2E_0/\pi$}

\itm{3} \textbf{\B{প্রতিবন্ধক:}}
\begin{itemize}
    \item[] {\lat $X_L=\omega L=2\pi fL$};\; {\lat $X_C=1/(\omega C)$}
    \item[] \B{RLC:} {\lat $Z=\sqrt{R^2+(X_L-X_C)^2}$;\; $\tan\phi=\dfrac{X_L-X_C}{R}$}
\end{itemize}

\itm{4} \textbf{\B{অনুনাদ,}} {\lat $f_0=\dfrac{1}{2\pi\sqrt{LC}}$;\; $Q=\dfrac{\omega_0 L}{R}$}

\itm{5} \textbf{\B{ক্ষমতা:}}
\begin{itemize}
    \item[] \B{প্রকৃত:} {\lat $P=E_{\rm rms}I_{\rm rms}\cos\phi$};\; {\lat $S^2=P^2+Q^2$}
\end{itemize}

\itm{6} \textbf{\B{ট্রান্সফর্মার,}} {\lat $\dfrac{V_s}{V_p}=\dfrac{N_s}{N_p}=\dfrac{I_p}{I_s}$}

\itm{7} \textbf{\B{AC জেনারেটর,}} {\lat $\varepsilon=NBA\omega\sin\omega t$;\; $\varepsilon_0=NBA\omega$}

\chsec{অধ্যায়-৬: জ্যামিতিক আলোকবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{আলোর বেগ ও প্রতিসরণাঙ্ক (Speed of Light and Refractive Index):}}
\begin{itemize}
    \item[] \B{ম্যাক্সওয়েল সম্পর্ক (শূন্যস্থানে আলোর বেগ):} {\lat $c = \dfrac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3 \times 10^8 \text{ ms}^{-1}$}
    \item[] \B{মাধ্যমের প্রতিসরণাঙ্ক ও আলোর বেগের সম্পর্ক:} {\lat $_a\mu_b = \dfrac{c_a}{c_b} = \dfrac{\mu_b}{\mu_a}$}
    \item[] {\lat $c_a, c_b$} = \B{$a$ ও $b$ মাধ্যমে আলোর বেগ ($\text{ms}^{-1}$)}
    \item[] {\lat $\mu_a, \mu_b$} = \B{$a$ ও $b$ মাধ্যমের পরম প্রতিসরণাঙ্ক}
    \item[] {\lat $\mu_0$} = \B{শূন্যস্থানের চৌম্বকভেদ্যতা}
    \item[] {\lat $\varepsilon_0$} = \B{শূন্যস্থানের তড়িৎ ভেদনযোগ্যতা}
\end{itemize}

\itm{2} \textbf{\B{প্রতিফলন ও প্রতিসরণ (Reflection and Refraction):}}
\begin{itemize}
    \item[] \B{প্রতিফলনের সূত্র:} {\lat $i = r$}
    \item[] \B{স্নেলের সূত্র (সাধারণ রূপ):} {\lat $\mu_a \sin i = \mu_b \sin r$}
    \item[] \B{প্রতিসরণাঙ্কের সমীকরণ:} {\lat $\mu = \dfrac{c}{v} = \dfrac{\sin i}{\sin r}$}
    \item[] \B{পূর্ণ অভ্যন্তরীণ প্রতিফলন ও ক্রান্তি কোণ:} {\lat $\sin\theta_c = \dfrac{1}{\mu} = \dfrac{\mu_1}{\mu_2}$}
    \item[] {\lat $i$} = \B{আপাতন কোণ}
    \item[] {\lat $r$} = \B{প্রতিফলন কোণ / প্রতিসরণ কোণ}
    \item[] {\lat $v$} = \B{কোনো নির্দিষ্ট মাধ্যমে আলোর বেগ ($\text{ms}^{-1}$)}
    \item[] {\lat $\theta_c$} = \B{ক্রান্তি কোণ বা সংকট কোণ (Critical angle)}
\end{itemize}

\itm{3} \textbf{\B{গোলকীয় দর্পণ ও সাধারণ লেন্স (Spherical Mirror and General Lens):}}
\begin{itemize}
    \item[] \B{গাউসের সাধারণ সমীকরণ (দর্পণ ও লেন্স):} {\lat $\dfrac{1}{u} + \dfrac{1}{v} = \dfrac{1}{f}$}
    \item[] \B{বক্রতার ব্যাসার্ধ ও ফোকাস দূরত্ব:} {\lat $f = \dfrac{R}{2}$}
    \item[] \B{রৈখিক বিবর্ধন:} {\lat $m = -\dfrac{v}{u}$} বা {\lat $|m| = \left|\dfrac{v}{u}\right|$}
    \item[] {\lat $u$} = \B{লক্ষ্যবস্তুর দূরত্ব (m)}
    \item[] {\lat $v$} = \B{প্রতিবিম্বের দূরত্ব (m)}
    \item[] {\lat $f$} = \B{ফোকাস দূরত্ব (m)}
    \item[] {\lat $R$} = \B{বক্রতার ব্যাসার্ধ (m)}
\end{itemize}

\itm{4} \textbf{\B{লেন্স প্রস্তুতকারকের সূত্র ও ক্ষমতা (Lens Maker's Formula and Power):}}
\begin{itemize}
    \item[] \B{লেন্স নির্মাতা সমীকরণ:} {\lat $\dfrac{1}{f} = (\mu - 1)\!\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right) = \left(\dfrac{\mu_2}{\mu_1} - 1\right)\!\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$}
    \item[] \B{লেন্সের ক্ষমতা:} {\lat $P = \dfrac{1}{f}$}
    \item[] \B{লেন্সের সমবায় (তুল্য ফোকাস দূরত্ব):} {\lat $\dfrac{1}{F} = \dfrac{1}{f_1} + \dfrac{1}{f_2} + \dfrac{1}{f_3} + \dots$}
    \item[] \B{তুল্য ক্ষমতা:} {\lat $P = P_1 + P_2 + P_3 + \dots$}
    \item[] {\lat $\mu$} = \B{পার্শ্ববর্তী মাধ্যমের সাপেক্ষে লেন্সের উপাদানের প্রতিসরণাঙ্ক}
    \item[] {\lat $R_1, R_2$} = \B{যথাক্রমে ১ম ও ২য় গোলকীয় পৃষ্ঠের বক্রতার ব্যাসার্ধ (m)}
    \item[] {\lat $P$} = \B{লেন্সের ক্ষমতা, এর একক ডায়াপ্টার (D)}
    \item[] {\lat $F$} = \B{তুল্য লেন্সের ফোকাস দূরত্ব (m)}
\end{itemize}

\itm{5} \textbf{\B{প্রিজম ও আলোর বিচ্ছুরণ (Prism and Dispersion of Light):}}
\begin{itemize}
    \item[] \B{প্রিজম কোণ:} {\lat $A = r_1 + r_2$}
    \item[] \B{বিচ্যুতি কোণ:} {\lat $\delta = i_1 + i_2 - A$}
    \item[] \B{ন্যূনতম বিচ্যুতি কোণে প্রতিসরণাঙ্ক:} {\lat $\mu = \dfrac{\sin\!\left(\dfrac{A+\delta_m}{2}\right)}{\sin\!\left(\dfrac{A}{2}\right)}$}
    \item[] \B{বিক্ষেপণ বা বিচ্ছুরণ ক্ষমতা:} {\lat $\omega = \dfrac{\mu_v-\mu_r}{\mu_y-1}$}
    \item[] {\lat $A$} = \B{প্রিজম কোণ}
    \item[] {\lat $\delta_m$} = \B{ন্যূনতম বিচ্যুতি কোণ}
    \item[] {\lat $r_1, r_2$} = \B{যথাক্রমে প্রিজমের প্রথম ও দ্বিতীয় পৃষ্ঠের প্রতিসরণ কোণ}
    \item[] {\lat $\mu_v, \mu_r, \mu_y$} = \B{যথাক্রমে বেগুনী, লাল ও হলুদ (মধ্যরশ্মি) বর্ণের প্রতিসরণাঙ্ক}
\end{itemize}

\itm{6} \textbf{\B{আলোকীয় যন্ত্রপাতি (Optical Instruments):}}
\begin{itemize}
    \item[] \B{সরল অণুবীক্ষণ যন্ত্রের বিবর্ধন:} {\lat $m = 1 + \dfrac{D}{f}$}
    \item[] \B{জটিল অণুবীক্ষণ যন্ত্রের বিবর্ধন:} {\lat $m \approx -\dfrac{L}{f_o}\!\left(1 + \dfrac{D}{f_e}\right)$}
    \item[] \B{নভো দূরবীক্ষণ যন্ত্র (অসীম দূরত্বের ফোকাসিং):}
    \begin{itemize}
        \item[] \B{বিবর্ধন:} {\lat $m = -\dfrac{f_o}{f_e}$}
        \item[] \B{নলের দৈর্ঘ্য:} {\lat $L = f_o + f_e$}
    \end{itemize}
    \item[] \B{নভো দূরবীক্ষণ যন্ত্র (স্পষ্ট দর্শনের ন্যূনতম দূরত্বে ফোকাসিং):}
    \begin{itemize}
        \item[] \B{বিবর্ধন:} {\lat $m = \dfrac{f_o}{f_e}\!\left(1 + \dfrac{f_e}{D}\right)$}
        \item[] \B{নলের দৈর্ঘ্য:} {\lat $L = f_o + \dfrac{D \cdot f_e}{D + f_e}$}
    \end{itemize}
    \item[] {\lat $D$} = \B{স্পষ্ট দৃষ্টির ন্যূনতম দূরত্ব (স্বাভাবিক চোখের জন্য $D = 25\text{ cm} = 0.25\text{ m}$)}
    \item[] {\lat $f_o$} = \B{অভিলক্ষ্যের (Objective) ফোকাস দূরত্ব (m)}
    \item[] {\lat $f_e$} = \B{অভিনেত্রের (Eyepiece) ফোকাস দূরত্ব (m)}
    \item[] {\lat $L$} = \B{দূরবীক্ষণ বা অণুবীক্ষণ যন্ত্রের নলের দৈর্ঘ্য (m)}
\end{itemize}

\itm{7} \textbf{\B{লেন্সের বিশ্লেষণ ক্ষমতা (Resolving Power of Lens):}}
\begin{itemize}
    \item[] \B{বিশ্লেষণী ক্ষমতা সমীকরণ:} {\lat $R = \dfrac{2\mu \sin\theta}{\lambda}$}
    \item[] {\lat $\lambda$} = \B{ব্যবহৃত আলোর তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $\mu$} = \B{মাধ্যমের প্রতিসরণাঙ্ক}
    \item[] {\lat $\theta$} = \B{অভিলক্ষ্যের ব্যাসার্ধ কর্তৃক লক্ষ্যবস্তুতে উৎপন্ন অর্ধ-কৌণিক কোণ}
\end{itemize}


\chsec{অধ্যায়-৭: ভৌত আলোকবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তরঙ্গ ও তড়িচ্চুম্বকীয় বিকিরণ (Waves and Electromagnetic Radiation):}}
\begin{itemize}
    \item[] \B{অগ্রগামী তরঙ্গের সমীকরণ:} {\lat $y = A \sin(\omega t - \frac{2\pi}{\lambda}x) = A \sin \frac{2\pi}{\lambda}(vt - x)$}
    \item[] \B{তড়িৎক্ষেত্র সমীকরণ:} {\lat $E = E_0 \sin(ct - x)$}
    \item[] \B{চৌম্বকক্ষেত্র সমীকরণ:} {\lat $B = B_0 \sin(ct - x)$}
    \item[] \B{তড়িৎ ও চৌম্বকক্ষেত্রের সম্পর্ক:} {\lat $E_0 = c B_0$}
    \item[] \B{কোনো মাধ্যমে আলোর বেগ:} {\lat $c = \dfrac{1}{\sqrt{\mu\epsilon}}$}
    \item[] \B{দশা পার্থক্য, পথ পার্থক্য ও সময়ের সম্পর্ক:} {\lat $\dfrac{\Delta \delta}{2\pi} = \dfrac{\Delta x}{\lambda} = \dfrac{\Delta t}{T}$}
    \item[] {\lat $A$} = \B{বিস্তার (m)}
    \item[] {\lat $\omega$} = \B{কৌণিক কম্পাঙ্ক ($\text{s}^{-1}$)}
    \item[] {\lat $\lambda$} = \B{তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $E_0, B_0$} = \B{তড়িৎক্ষেত্র ও চৌম্বকক্ষেত্রের সর্বোচ্চ মান}
    \item[] {\lat $\mu$} = \B{মাধ্যমের চৌম্বকভেদ্যতা}
    \item[] {\lat $\epsilon$} = \B{তড়িৎ ভেদনযোগ্যতা}
    \item[] {\lat $\Delta \delta$} = \B{দশা পার্থক্য (rad)}
    \item[] {\lat $\Delta x$} = \B{পথ পার্থক্য (m)}
    \item[] {\lat $\Delta t$} = \B{সময়ের পার্থক্য (s)}
    \item[] {\lat $T$} = \B{পর্যায়কাল (s)}
\end{itemize}

\itm{2} \textbf{\B{সুসংগত উৎস ও ব্যতিচার (Coherent Sources and Interference):}}
\begin{itemize}
    \item[] \B{সুসংগত উৎসের শর্ত (কম্পাঙ্ক):} {\lat $f_1 = f_2$}
    \item[] \B{সুসংগত উৎসের শর্ত (দশা পার্থক্য):} {\lat $\Delta \delta = \text{constant}$}
    \item[] \B{গঠনমূলক ব্যতিচার (পথ পার্থক্য):} {\lat $\Delta x = n\lambda$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
    \item[] \B{গঠনমূলক ব্যতিচার (দশা পার্থক্য):} {\lat $\Delta \delta = 2n\pi$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
    \item[] \B{ধ্বংসাত্মক ব্যতিচার (পথ পার্থক্য):} {\lat $\Delta x = (2n-1)\dfrac{\lambda}{2}$} \; {\lat $[n = 1, 2, 3, \dots]$} বা {\lat $\Delta x = (2n+1)\dfrac{\lambda}{2}$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
    \item[] \B{ধ্বংসাত্মক ব্যতিচার (দশা পার্থক্য):} {\lat $\Delta \delta = (2n-1)\pi$} \; {\lat $[n = 1, 2, 3, \dots]$} বা {\lat $\Delta \delta = (2n+1)\pi$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
\end{itemize}

\itm{3} \textbf{\B{ইয়ং এর দ্বি-চির পরীক্ষা (Young's Double Slit Experiment):}}
\begin{itemize}
    \item[] \B{কেন্দ্র হতে $n$ তম উজ্জ্বল ডোরার (চরমের) দূরত্ব:} {\lat $x_n = \dfrac{n\lambda D}{d}$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
    \item[] \B{কেন্দ্র হতে $n$ তম অন্ধকার ডোরার (অবমের) দূরত্ব:} {\lat $x_n = (2n-1)\dfrac{\lambda D}{2d}$} \; {\lat $[n = 1, 2, 3, \dots]$}
    \item[] \B{পরপর দুটি উজ্জ্বল বা অন্ধকার ডোরার মধ্যবর্তী দূরত্ব (ডোরা ব্যবধান):} {\lat $\Delta x = \dfrac{\lambda D}{d}$}
    \item[] \B{ডোরা প্রস্থ:} {\lat $x = \dfrac{\lambda D}{2d}$}
    \item[] \B{ডোরার কৌণিক দূরত্ব সমীকরণ:} {\lat $\tan\theta_n \approx \sin\theta_n = \dfrac{x_n}{D}$}
    \item[] \B{ডোরাসংখ্যা ও তরঙ্গদৈর্ঘ্যের সম্পর্ক:} {\lat $N_1\lambda_1 = N_2\lambda_2$}
    \item[] \B{আলোর কৌণিক ব্যবধান:} {\lat $\Delta \theta = \dfrac{\lambda}{d}$}
    \item[] {\lat $\lambda$} = \B{আলোক তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $D$} = \B{চির হতে পর্দার দূরত্ব (m)}
    \item[] {\lat $d$} = \B{চিরদ্বয়ের মধ্যবর্তী দূরত্ব (m)}
    \item[] {\lat $\theta_n$} = \B{কেন্দ্র হতে $n$ তম ডোরা বা অবমের কৌণিক দূরত্ব}
    \item[] {\lat $N_1, N_2$} = \B{ডোরার সংখ্যা}
    \item[] {\lat $\lambda_1, \lambda_2$} = \B{তরঙ্গদৈর্ঘ্য (m)}
\end{itemize}

\itm{4} \textbf{\B{আলোর তীব্রতা ও বিস্তার (Light Intensity and Amplitude):}}
\begin{itemize}
    \item[] \B{লব্ধি বিস্তার:} {\lat $A = \sqrt{A_1^2 + A_2^2 + 2A_1A_2\cos\phi}$}
    \item[] \B{লব্ধি বিস্তারের দিক:} {\lat $\tan\theta = \dfrac{A_2\sin\phi}{A_1 + A_2\cos\phi}$}
    \item[] \B{লব্ধি তীব্রতা:} {\lat $I = I_1 + I_2 + 2\sqrt{I_1I_2}\cos\delta$}
    \item[] \B{সর্বোচ্চ ও সর্বনিম্ন বিস্তার:} {\lat $A_{\max} = A_1 + A_2$};\; {\lat $A_{\min} = A_1 - A_2$}
    \item[] {\lat $A_1, A_2$} = \B{১ম ও ২য় তরঙ্গের বিস্তার (m)}
    \item[] {\lat $\delta$} = \B{১ম ও ২য় তরঙ্গের তীব্রতার দশা পার্থক্য}
    \item[] {\lat $\phi$} = \B{$A$ ও $A_1$ এর মধ্যবর্তী দশা পার্থক্য}
\end{itemize}

\itm{5} \textbf{\B{পাতলা পর্দা (Thin Film Interference):}}
\begin{itemize}
    \item[] \B{গঠনমূলক ব্যতিচার:} {\lat $2\mu t\cos r=(2n-1)\dfrac{\lambda}{2}$}
    \item[] \B{ধ্বংসাত্মক ব্যতিচার:} {\lat $2\mu t\cos r=n\lambda$}
    \item[] {\lat $\mu$} = \B{পাতলা পর্দার প্রতিসরণাঙ্ক}
    \item[] {\lat $t$} = \B{পর্দার পুরুত্ব (m)}
    \item[] {\lat $r$} = \B{প্রতিসরণ কোণ}
\end{itemize}

\itm{6} \textbf{\B{নিউটনের বলয় (Newton's Rings):}}
\begin{itemize}
    \item[] \B{অন্ধকার বলয়ের ব্যাসার্ধ:} {\lat $r_n=\sqrt{n\lambda R}$}
    \item[] \B{তরঙ্গদৈর্ঘ্য নির্ণয় সমীকরণ:} {\lat $\lambda=\dfrac{D_n^2-D_m^2}{4R(n-m)}$}
    \item[] {\lat $r_n$} = \B{$n$ তম বলয়ের ব্যাসার্ধ (m)}
    \item[] {\lat $D_n, D_m$} = \B{$n$ ও $m$ তম বলয়ের ব্যাস (m)}
    \item[] {\lat $R$} = \B{প্ল্যানো-কনভেক্স লেন্সের বক্রতার ব্যাসার্ধ (m)}
\end{itemize}

\itm{7} \textbf{\B{একক চিরের দরুণ অপবর্তন (Single Slit Diffraction):}}
\begin{itemize}
    \item[] \B{অপবর্তন সমীকরণ:} {\lat $a\sin\theta = \Delta x$}
    \item[] \B{গৌণ চরমের জন্য পথ পার্থক্য:} {\lat $\Delta x = (2n+1)\dfrac{\lambda}{2}$} \; {\lat $[n = 1, 2, 3, \dots]$}
    \item[] \B{গৌণ অবমের জন্য পথ পার্থক্য:} {\lat $\Delta x = n\lambda$} \; {\lat $[n = 1, 2, 3, \dots]$}
    \item[] {\lat $a$} = \B{চিরের প্রস্থ (m)}
    \item[] {\lat $\Delta x$} = \B{পথ পার্থক্য (m)}
\end{itemize}

\itm{8} \textbf{\B{অপবর্তন গ্রেটিং (Diffraction Grating):}}
\begin{itemize}
    \item[] \B{গ্রেটিং ধ্রুবক সমীকরণ:} {\lat $d = a+b = \dfrac{1}{N}$}
    \item[] \B{গ্রেটিং অপবর্তন সমীকরণ:} {\lat $d\sin\theta = \Delta x$}
    \item[] \B{চরমের জন্য পথ পার্থক্য:} {\lat $\Delta x = n\lambda$} \; {\lat $[n = 1, 2, 3, \dots]$}
    \item[] \B{অবমের জন্য পথ পার্থক্য:} {\lat $\Delta x = (2n+1)\dfrac{\lambda}{2}$} \; {\lat $[n = 0, 1, 2, 3, \dots]$}
    \item[] {\lat $a$} = \B{রেখাছিদ্রের প্রস্থ (m)}
    \item[] {\lat $b$} = \B{রেখাছিদ্রের মধ্যে ব্যবধান (m)}
    \item[] {\lat $N$} = \B{একক দৈর্ঘ্যে চির বা ছিদ্রের সংখ্যা}
\end{itemize}

\itm{9} \textbf{\B{আলোর সমবর্তন (Polarization of Light):}}
\begin{itemize}
    \item[] \B{ম্যালাসের সূত্র (একাধিক পোলারাইজার):} {\lat $I_n = \dfrac{I_0}{2}\cos^2\theta_1\cdot\cos^2\theta_2\dots\cos^2\theta_n$}
    \item[] \B{১টি পোলারাইজার ও অ্যানালাইজারের ক্ষেত্রে:} {\lat $I_1 = \dfrac{I_0}{2}\cos^2\theta$}
    \item[] \B{ব্রুস্টারের সূত্র (প্রতিসরণ দ্বারা সমবর্তন):} {\lat $\tan i_p = \dfrac{\mu_2}{\mu_1}$}
    \item[] \B{সমবর্তন কোণ ও প্রতিসরণ কোণের সম্পর্ক:} {\lat $r + i_p = 90^\circ$}
    \item[] {\lat $I_n$} = \B{$n$ টি পোলারাইজার অতিক্রমের পর তীব্রতা ($\text{Wm}^{-2}$)}
    \item[] {\lat $\dfrac{I_0}{2}$} = \B{তল সমবর্তিত আলোর তীব্রতা ($\text{Wm}^{-2}$)}
    \item[] {\lat $\theta$} = \B{পোলারাইজার ও অ্যানালাইজারের মধ্যবর্তী কোণ}
    \item[] {\lat $r$} = \B{প্রতিসরণ কোণ}
    \item[] {\lat $i_p$} = \B{সমবর্তন কোণ}
    \item[] {\lat $\mu_2$} = \B{২য় মাধ্যমের প্রতিসরণাঙ্ক}
    \item[] {\lat $\mu_1$} = \B{১ম মাধ্যমের প্রতিসরণাঙ্ক}
\end{itemize}

\itm{10} \textbf{\B{পয়েন্টিং ভেক্টর (Poynting Vector):}}
\begin{itemize}
    \item[] \B{পয়েন্টিং ভেক্টর সমীকরণ:} {\lat $\vec{S} = \dfrac{1}{\mu_0}(\vec{E} \times \vec{B}) = E \times H$}
    \item[] {\lat $\vec{E}$} = \B{তড়িৎক্ষেত্র ($\text{Nc}^{-1}$)}
    \item[] {\lat $\vec{B}$} = \B{চৌম্বকক্ষেত্র (T)}
    \item[] {\lat $H$} = \B{চৌম্বক তীব্রতা}
\end{itemize}


\chsec{অধ্যায়-৮: আধুনিক পদার্থবিজ্ঞানের সূচনা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{আপেক্ষিকতা (Theory of Relativity):}}
\begin{itemize}
    \item[] \B{দৈর্ঘ্য সংকোচন (Length Contraction):} {\lat $L=L_0\sqrt{1-v^2/c^2}$}
    \item[] \B{কাল প্রসারণ (Time Dilation):} {\lat $t=\gamma t_0$}
    \item[] \B{ভরবৃদ্ধি (Mass Variation):} {\lat $m=\gamma m_0$}
    \item[] \B{লরেঞ্জ রূপান্তর গুণক ($\gamma$):} {\lat $\gamma=\dfrac{1}{\sqrt{1-v^2/c^2}}$}
    \item[] \B{ভর-শক্তি সমতুল্যতা (মোট শক্তি):} {\lat $E=mc^2$}
    \item[] \B{নিশ্চল শক্তি (Rest Energy):} {\lat $E_0=m_0c^2$}
    \item[] \B{আপেক্ষিক গতিশক্তি ($E_k$):} {\lat $E_k=(m-m_0)c^2$}
    \item[] \B{ভরবেগ ও শক্তির সম্পর্ক:} {\lat $E^2=(pc)^2+(m_0c^2)^2$}
    \item[] \B{আপেক্ষিক ভরবেগ:} {\lat $p=mv=\gamma m_0 v$}
    \item[] {\lat $L_0$} = \B{আদি দৈর্ঘ্য বা নিশ্চল দৈর্ঘ্য (m)}
    \item[] {\lat $L$} = \B{গতিশীল দৈর্ঘ্য (m)}
    \item[] {\lat $t_0$} = \B{নিশ্চল সময় বা মৌলিক সময় (s)}
    \item[] {\lat $t$} = \B{গতিশীল সময় (s)}
    \item[] {\lat $m_0$} = \B{নিশ্চল ভর (kg)}
    \item[] {\lat $m$} = \B{গতিশীল ভর (kg)}
    \item[] {\lat $v$} = \B{বস্তু বা কাঠামোর আপেক্ষিক বেগ ($\text{ms}^{-1}$)}
    \item[] {\lat $c$} = \B{শূন্যস্থানে আলোর বেগ} $= 3\times10^8\,\text{ms}^{-1}$
    \item[] {\lat $p$} = \B{আপেক্ষিক ভরবেগ ($\text{kg}\cdot\text{ms}^{-1}$)}
\end{itemize}

\itm{2} \textbf{\B{আলোক-তড়িৎ ক্রিয়া (Photoelectric Effect):}}
\begin{itemize}
    \item[] \B{আপতিত ফোটনের শক্তি:} {\lat $E=hf=\dfrac{hc}{\lambda}$}
    \item[] \B{ধাতুর কার্যাপেক্ষক (Work Function):} {\lat $\phi=hf_0=\dfrac{hc}{\lambda_0}$}
    \item[] \B{আইনস্টাইনের আলোক-তড়িৎ সমীকরণ (সর্বোচ্চ গতিশক্তি):} {\lat $E_k^{\max}=hf-\phi$}
    \item[] \B{গতিশক্তি ও নিবৃত্তি বিভবের সম্পর্ক:} {\lat $E_k^{\max}=\dfrac{1}{2}m_e v_{\max}^2=eV_s$}
    \item[] \B{ফোটনের ভরবেগ:} {\lat $p=\dfrac{E}{c}=\dfrac{h}{\lambda}$}
    \item[] {\lat $E$} = \B{আপতিত ফোটনের শক্তি (J)}
    \item[] {\lat $\phi$} = \B{ধাতুর কার্যাপেক্ষক (J)}
    \item[] {\lat $E_k^{\max}$} = \B{নির্গত ফটো-ইলেকট্রনের সর্বোচ্চ গতিশক্তি (J)}
    \item[] {\lat $f$} = \B{আপতিত আলোর কম্পাঙ্ক (Hz)}
    \item[] {\lat $f_0$} = \B{সূচনা কম্পাঙ্ক (Threshold Frequency) (Hz)}
    \item[] {\lat $\lambda$} = \B{আপতিত আলোর তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $\lambda_0$} = \B{সূচনা তরঙ্গদৈর্ঘ্য (Threshold Wavelength) (m)}
    \item[] {\lat $v_{\max}$} = \B{ফটো-ইলেকট্রনের সর্বোচ্চ বেগ ($\text{ms}^{-1}$)}
    \item[] {\lat $V_s$} = \B{নিবৃত্তি বিভব বা স্টপিং পটেনশিয়াল (V)}
    \item[] {\lat $e$} = \B{ইলেকট্রনের আধান} $= 1.6\times10^{-19}\,\text{C}$
    \item[] {\lat $m_e$} = \B{ইলেকট্রনের নিশ্চল ভর} $= 9.11\times10^{-31}\,\text{kg}$
    \item[] {\lat $h$} = \B{প্লাঙ্ক ধ্রুবক} $= 6.626\times10^{-34}\,\text{J}\cdot\text{s}$
\end{itemize}

\itm{3} \textbf{\B{এক্স-রে উৎপাদন (X-Ray Production):}}
\begin{itemize}
    \item[] \B{সর্বোচ্চ গতিশক্তি ও এক্স-রে ফোটনের সম্পর্ক:} {\lat $E_{k\max}=hf_{\max}=\dfrac{hc}{\lambda_{\min}}$}
    \item[] \B{প্রযুক্ত বিভব ও কাট-অফ তরঙ্গদৈর্ঘ্য:} {\lat $eV=\dfrac{hc}{\lambda_{\min}}$}
    \item[] \B{কাট-অফ (সর্বনিম্ন) তরঙ্গদৈর্ঘ্য সমীকরণ:} {\lat $\lambda_{\min}=\dfrac{hc}{eV}$}
    \item[] {\lat $f_{\max}$} = \B{এক্স-রে টিউবের সর্বোচ্চ কম্পাঙ্ক (Hz)}
    \item[] {\lat $\lambda_{\min}$} = \B{এক্স-রে ফোটনের সর্বনিম্ন বা কাট-অফ তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $V$} = \B{এক্স-রে টিউবে প্রযুক্ত উচ্চ বিভবভেদ (V)}
\end{itemize}

\itm{4} \textbf{\B{কম্পটন প্রভাব (Compton Effect):}}
\begin{itemize}
    \item[] \B{বিক্ষিপ্ত আলোর তরঙ্গদৈর্ঘ্য সমীকরণ:} {\lat $\lambda'=\lambda+\dfrac{h}{m_0 c}(1-\cos\theta)$}
    \item[] \B{কম্পটন তরঙ্গদৈর্ঘ্য সরণ:} {\lat $\Delta\lambda = \lambda'-\lambda = \dfrac{h}{m_0 c}(1-\cos\theta)$}
    \item[] \B{কম্পটন তরঙ্গদৈর্ঘ্য (ধ্রুবক মান):} {\lat $\lambda_c = \dfrac{h}{m_0 c} \approx 2.426\times10^{-12}\,\text{m}$}
    \item[] {\lat $\lambda$} = \B{আপতিত ফোটনের আদি তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $\lambda'$} = \B{বিক্ষিপ্ত ফোটনের শেষ তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $\Delta\lambda$} = \B{তরঙ্গদৈর্ঘ্যের পরিবর্তন বা কম্পটন সরণ (m)}
    \item[] {\lat $m_0$} = \B{ইলেকট্রনের নিশ্চল ভর (kg)}
    \item[] {\lat $\theta$} = \B{ফোটনের বিক্ষেপণ বা বিচ্ছুরণ কোণ (Scattering Angle)}
    \item[] {\lat $h$} = \B{প্লাঙ্ক ধ্রুবক} $= 6.626\times10^{-34}\,\text{J}\cdot\text{s}$
\end{itemize}

\itm{5} \textbf{\B{দ্য ব্রোগলি বা বস্তু তরঙ্গ (De Broglie Wave):}}
\begin{itemize}
    \item[] \B{তরঙ্গদৈর্ঘ্য (ভরবেগের মাধ্যমে):} {\lat $\lambda=\dfrac{h}{p}$}
    \item[] \B{তরঙ্গদৈর্ঘ্য (ভর ও বেগের মাধ্যমে):} {\lat $\lambda=\dfrac{h}{\text{mv}}$}
    \item[] \B{তরঙ্গদৈর্ঘ্য (গতিশক্তির মাধ্যমে):} {\lat $\lambda=\dfrac{h}{\sqrt{2mE_k}}$}
    \item[] \B{ইলেকট্রনের জন্য বিভবভেদের মাধ্যমে শর্টকাট:} {\lat $\lambda=\dfrac{h}{\sqrt{2meV}}$}
    \item[] {\lat $\lambda$} = \B{দ্য ব্রোগলি তরঙ্গদৈর্ঘ্য বা বস্তু তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $p$} = \B{কণার রৈখিক ভরবেগ ($\text{kg}\cdot\text{ms}^{-1}$)}
    \item[] {\lat $v$} = \B{কণার বেগ ($\text{ms}^{-1}$)}
    \item[] {\lat $E_k$} = \B{কণার গতিশক্তি (J)}
\end{itemize}

\itm{6} \textbf{\B{হাইজেনবার্গ অনিশ্চয়তা নীতি (Heisenberg Uncertainty Principle):}}
\begin{itemize}
    \item[] \B{অবস্থান ও ভরবেগের অনিশ্চয়তা সমীকরণ:} {\lat $\Delta x\cdot\Delta p\ge\dfrac{h}{4\pi}$}
    \item[] {\lat $\Delta x$} = \B{অবস্থানের অনিশ্চয়তা (m)}
    \item[] {\lat $\Delta p$} = \B{ভরবেগের অনিশ্চয়তা ($\text{kg}\cdot\text{ms}^{-1}$)}
\end{itemize}

\itm{7} \textbf{\B{কৃষ্ণবস্তুর বিকিরণ ও তাপগতিবিদ্যা (Blackbody Radiation):}}
\begin{itemize}
    \item[] \B{ভীনের সরণ সূত্র (সর্বোচ্চ তীব্রতার তরঙ্গদৈর্ঘ্য):} {\lat $\lambda_{\max}T = b$}
    \item[] \B{ভীনের ধ্রুবক ($b$):} {\lat $b = 2.898\times10^{-3}\,\text{m}\cdot\text{K}$}
    \item[] \B{স্টিফেন-বোল্টজম্যান সূত্র (বিকিরণ ক্ষমতা):} {\lat $P=\sigma eAT^4$}
    \item[] \B{পরিবেশের তাপমাত্রা সহ নেট বিকিরণ ক্ষমতা:} {\lat $P=\sigma eA(T_B^4-T_E^4)$}
    \item[] {\lat $\sigma$} = \B{স্টিফেন-বোল্টজম্যান ধ্রুবক} $= 5.67\times10^{-8}\,\text{W}\cdot\text{m}^{-2}\cdot\text{K}^{-4}$
    \item[] {\lat $e$} = \B{কৃষ্ণবস্তুর নির্গমন গুণাঙ্ক (Emissivity)} [\B{আদর্শ কৃষ্ণবস্তুর জন্য} {\lat $e=1$}]
    \item[] {\lat $A$} = \B{কৃষ্ণবস্তুর পৃষ্ঠতলের ক্ষেত্রফল ($\text{m}^2$)}
    \item[] {\lat $T_B$} বা {\lat $T$} = \B{বস্তুর পরম তাপমাত্রা (K)}
    \item[] {\lat $T_E$} = \B{পরিবেশের পরম তাপমাত্রা (K)}
\end{itemize}

\chsec{অধ্যায়-৯: পরমাণুর মডেল ও নিউক্লিয়ার পদার্থবিজ্ঞান}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বোর মডেল ও কক্ষপথের সমীকরণসমূহ:}}
\begin{itemize}
    \item[] \B{কোয়ান্টাইজেশন (কৌণিক ভরবেগ):} {\lat $mvr_n=n\dfrac{h}{2\pi}$}
    \item[] \B{কক্ষপথের ব্যাসার্ধ (সাধারণ সূত্র):} {\lat $r_n=\dfrac{h^2 \epsilon_0 n^2}{\pi m Z e^2}$}
    \item[] \B{কক্ষপথের ব্যাসার্ধ (তাত্ত্বিক শর্টকাট):} {\lat $r_n=n^2 r_1$}
    \item[] \B{কক্ষপথের ব্যাসার্ধ (মানসহ শর্টকাট):} {\lat $r_n=(0.53\,\text{\AA})\dfrac{n^2}{Z}$}
    \item[] \B{কক্ষপথে ইলেকট্রনের বেগ (সাধারণ সূত্র):} {\lat $V_n=\dfrac{Z e^2}{2 h \epsilon_0 n}$}
    \item[] \B{কক্ষপথে ইলেকট্রনের বেগ (তাত্ত্বিক শর্টকাট):} {\lat $V_n=\dfrac{V_1}{n}$}
    \item[] \B{কক্ষপথে ইলেকট্রনের বেগ (মানসহ শর্টকাট):} {\lat $V_n=(2.18\times10^6\,\text{ms}^{-1})\times\dfrac{Z}{n}$}
    \item[] \B{ইলেকট্রনের স্থিতিশক্তি ($E_p$):} {\lat $E_p=-\dfrac{Z^2 m e^4}{4 h^2 \epsilon_0^2 n^2}$}
    \item[] \B{ইলেকট্রনের গতিশক্তি ($E_k$):} {\lat $E_k=+\dfrac{Z^2 m e^4}{8 h^2 \epsilon_0^2 n^2}$}
    \item[] \B{ইলেকট্রনের মোট শক্তি (সাধারণ সূত্র):} {\lat $E_n=-\dfrac{Z^2 m e^4}{8 h^2 \epsilon_0^2 n^2}$}
    \item[] \B{ইলেকট্রনের মোট শক্তি (তাত্ত্বিক শর্টকাট):} {\lat $E_n=\dfrac{E_1}{n^2}$}
    \item[] \B{ইলেকট্রনের মোট শক্তি (মানসহ শর্টকাট):} {\lat $E_n=-\dfrac{13.6\,Z^2}{n^2}\,\text{eV}$}
    \item[] \B{ইলেকট্রনের পর্যায়কাল ($T_n$):} {\lat $T_n=\dfrac{4 h^3 \epsilon_0^2 n^3}{Z^2 m e^4}$}
    \item[] \B{ইলেকট্রনের পর্যায়কাল (তাত্ত্বিক শর্টকাট):} {\lat $T_n=n^3\times T_1$}
    \item[] \B{হাইড্রোজেনের ১ম কক্ষপথের ব্যাসার্ধ ($r_1$ বা $a_0$):} {\lat $r_1=0.53\,\text{\AA}$}
    \item[] \B{হাইড্রোজেনের ১ম কক্ষপথে ইলেকট্রনের বেগ ($V_1$):} {\lat $V_1=2.18\times10^6\,\text{ms}^{-1}$}
    \item[] \B{হাইড্রোজেনের ১ম কক্ষপথে মোট শক্তি ($E_1$):} {\lat $E_1=-13.6\,\text{eV}$}
    \item[] \B{হাইড্রোজেনের ১ম কক্ষপথে পর্যায়কাল ($T_1$):} {\lat $T_1=1.51\times10^{-16}\,\text{s}$}
    \item[] \B{কক্ষপথ স্থানান্তরে নিঃসৃত বা শোষিত শক্তি:} {\lat $\Delta E = E_2 - E_1$}
    \item[] \B{শক্তির সাথে কম্পাঙ্ক ও তরঙ্গদৈর্ঘ্যের সম্পর্ক:} {\lat $\Delta E = h\nu = \dfrac{hc}{\lambda}$}
    \item[] \B{নিঃসৃত ফোটনের তরঙ্গদৈর্ঘ্য (রিডবার্গ সমীকরণ):} {\lat $\dfrac{1}{\lambda}=R_HZ^2\left(\dfrac{1}{n_1^2}-\dfrac{1}{n_2^2}\right)$}
    \item[] {\lat $h$} = \B{প্লাঙ্ক ধ্রুবক} $= 6.626\times10^{-34}\,\text{J}\cdot\text{s}$
    \item[] {\lat $\epsilon_0$} = \B{শূন্যস্থানের ভেদনযোগ্যতা} $= 8.854\times10^{-12}\,\text{C}^2\text{N}^{-1}\text{m}^{-2}$
    \item[] {\lat $R_H$} = \B{রিডবার্গ ধ্রুবক} $= 1.09678\times10^7\,\text{m}^{-1}$
    \item[] {\lat $n$} = \B{কক্ষপথ নম্বর} $(1, 2, 3, \dots)$
    \item[] {\lat $m$} = \B{ইলেকট্রনের ভর (Kg)}
    \item[] {\lat $Z$} = \B{পারমাণবিক সংখ্যা}
    \item[] {\lat $e$} = \B{ইলেকট্রনের আধান বা চার্জ} $= 1.6\times10^{-19}\,\text{C}$
    \item[] {\lat $\nu$} = \B{নিঃসৃত বিকিরণের কম্পাঙ্ক (Hz)}
    \item[] {\lat $\lambda$} = \B{নিঃসৃত বিকিরণের তরঙ্গদৈর্ঘ্য (m)}
    \item[] {\lat $n_1$} = \B{নিম্নতর কক্ষপথের স্তর}
    \item[] {\lat $n_2$} = \B{উচ্চতর কক্ষপথের স্তর}
\end{itemize}

\itm{2} \textbf{\B{হাইড্রোজেন বর্ণালীর সিরিজসমূহ:}}
\begin{itemize}
    \item[] \B{লাইম্যান সিরিজ:} {\lat $n_1=1$}, \;\; {\lat $n_2=2,3,4,\dots,\infty$}
    \item[] \B{বামার সিরিজ:} {\lat $n_1=2$}, \;\; {\lat $n_2=3,4,5,\dots,\infty$}
    \item[] \B{প্যাশেন সিরিজ:} {\lat $n_1=3$}, \;\; {\lat $n_2=4,5,6,\dots,\infty$}
    \item[] \B{ব্র্যাকেট সিরিজ:} {\lat $n_1=4$}, \;\; {\lat $n_2=5,6,7,\dots,\infty$}
    \item[] \B{ফান্ড সিরিজ:} {\lat $n_1=5$}, \;\; {\lat $n_2=6,7,8,\dots,\infty$}
    \item[] \B{হামফ্রিজ সিরিজ:} {\lat $n_1=6$}, \;\; {\lat $n_2=7,8,9,\dots,\infty$}
\end{itemize}

\itm{3} \textbf{\B{X-রে (রঞ্জন রশ্মি):}}
\begin{itemize}
    \item[] \B{মোসেলির সূত্র:} {\lat $\sqrt f=a(Z-b)$}
    \item[] \B{ব্র্যাগের সূত্র:} {\lat $2d\sin\theta=n\lambda$}
    \item[] \B{কাট-অফ (সর্বনিম্ন) তরঙ্গদৈর্ঘ্য:} {\lat $\lambda_{\min}=\dfrac{hc}{eV}$}
\end{itemize}

\itm{4} \textbf{\B{নিউক্লিয়াসের গঠন, ভরত্রুটি ও বন্ধনশক্তি:}}
\begin{itemize}
    \item[] \B{নিউক্লিয়াসের ব্যাসার্ধ:} {\lat $R=R_0 A^{1/3}$}
    \item[] \B{ফেরমি ধ্রুবক ($R_0$):} {\lat $R_0=1.2\times10^{-15}\,\text{m}$}
    \item[] \B{ভরত্রুটি (Mass Defect):} {\lat $\Delta m=[Z m_p + (A-Z)m_n] - m_{\text{Nu}}$}
    \item[] \B{বন্ধনশক্তি (Binding Energy):} {\lat $E_b=\Delta m \cdot c^2$}
    \item[] \B{বন্ধনশক্তি (MeV এককে শর্টকাট):} {\lat $E_b=\Delta m \times 931.5\,\text{MeV}$}
    \item[] \B{নিউক্লিয়নের গড় বন্ধনশক্তি:} {\lat $\bar E_b = \dfrac{E_b}{A}$}
    \item[] {\lat $A$} = \B{ভর সংখ্যা (মোট নিউক্লিয়ন সংখ্যা)}
    \item[] {\lat $Z$} = \B{পারমাণবিক সংখ্যা (প্রোটন সংখ্যা)}
    \item[] {\lat $m_p$} = \B{একটি মুক্ত প্রোটনের ভর (Kg)}
    \item[] {\lat $m_n$} = \B{একটি মুক্ত নিউট্রনের ভর (Kg)}
    \item[] {\lat $m_{\text{Nu}}$} = \B{নিউক্লিয়াসের প্রকৃত ভর (Kg)}
\end{itemize}

\itm{5} \textbf{\B{তেজস্ক্রিয়তা ও ক্ষয় সূত্রাবলি:}}
\begin{itemize}
    \item[] \B{তেজস্ক্রিয় ক্ষয়ের হার:} {\lat $\dfrac{dN}{dt} = -\lambda N$}
    \item[] \B{ক্ষয় সূত্র (পরমাণুর সংখ্যায়):} {\lat $N=N_0 e^{-\lambda t}$}
    \item[] \B{ক্ষয় সূত্র (মোল সংখ্যায়):} {\lat $n=n_0 e^{-\lambda t}$}
    \item[] \B{ক্ষয় সূত্র (ভর এককে):} {\lat $m=m_0 e^{-\lambda t}$}
    \item[] \B{ক্ষয় সূত্র (তেজস্ক্রিয়তার হার বা সক্রিয়তা):} {\lat $A=A_0 e^{-\lambda t}$}
    \item[] \B{সক্রিয়তার সাধারণ সমীকরণ:} {\lat $A=\lambda N$}
    \item[] \B{অর্ধায়ু (Half-life):} {\lat $T_{1/2}=\dfrac{\ln 2}{\lambda}=\dfrac{0.693}{\lambda}$}
    \item[] \B{গড় আয়ু (Mean life):} {\lat $\tau=\dfrac{1}{\lambda}$}
    \item[] \B{কুঁড়ি ও বেকেরেল সম্পর্ক:} {\lat $1\,\text{Ci} = 3.7\times10^{10}\,\text{Bq}$}
    \item[] {\lat $\lambda$} = \B{অবক্ষয় ধ্রুবক বা ক্ষয় ধ্রুবক}
    \item[] {\lat $t$} = \B{অতিবাহিত সময়}
    \item[] {\lat $N_0$} = \B{$t=0$ সময়ে অক্ষত পরমাণুর সংখ্যা}
    \item[] {\lat $N$} = \B{$t$ সময় পর অক্ষত পরমাণুর সংখ্যা}
    \item[] {\lat $n_0$} = \B{$t=0$ সময়ে আদি মোল সংখ্যা}
    \item[] {\lat $n$} = \B{$t$ সময় পর অক্ষত মোল সংখ্যা}
    \item[] {\lat $m_0$} = \B{$t=0$ সময়ে আদি ভর (Kg)}
    \item[] {\lat $m$} = \B{$t$ সময় পর অক্ষত ভর (Kg)}
    \item[] {\lat $A_0$} = \B{$t=0$ সময়ে আদি তেজস্ক্রিয়তার হার}
    \item[] {\lat $A$} = \B{$t$ সময় পর তেজস্ক্রিয়তার হার}
\end{itemize}

\itm{6} \textbf{\B{তেজস্ক্রিয় বিঘটন (Decay Modes):}}
\begin{itemize}
    \item[] \B{$\alpha$-ক্ষয় (Alpha Decay):} {\lat ${}^A_ZX\to{}^{A-4}_{Z-2}Y+{}^4_2\text{He}$}
    \item[] \B{$\beta^-$-ক্ষয় (Beta-minus Decay):} {\lat ${}^A_ZX\to{}^A_{Z+1}Y+e^-+\bar\nu_e$}
    \item[] \B{$\beta^+$-ক্ষয় (Beta-plus Decay):} {\lat ${}^A_ZX\to{}^A_{Z-1}Y+e^++\nu_e$}
\end{itemize}

\itm{7} \textbf{\B{নিউক্লিয়ার বিক্রিয়া ও ভর-শক্তি সমতুল্যতা:}}
\begin{itemize}
    \item[] \B{নিউক্লিয়ার ফিশন বিক্রিয়া:} {\lat ${}^{235}_{92}\text{U} + {}^1_0\text{n} \to {}^{141}_{56}\text{Ba} + {}^{92}_{36}\text{Kr} + 3\,{}^1_0\text{n} + \text{\text{\B{শক্তি}}}$}
    \item[] \B{নিউক্লিয়ার ফিউশন বিক্রিয়া:} {\lat ${}^2_1\text{H} + {}^3_1\text{H} \to {}^4_2\text{He} + {}^1_0\text{n} + 17.6\,\text{MeV}$}
    \item[] \B{পারমাণবিক ভর একক ও শক্তির সম্পর্ক:} {\lat $1\,\text{u} = 931.5\,\text{MeV}$}
\end{itemize}

\chsec{অধ্যায়-১০: সেমিকন্ডাক্টর ও ইলেকট্রনিক্স}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{সেমিকন্ডাক্টরের তড়িৎ প্রবাহ ও আধান ঘনত্ব:}}
\begin{itemize}
    \item[] \B{তড়িৎ প্রবাহ ঘনত্ব:} {\lat $J=e(n\mu_e+p\mu_h)E$}
    \item[] \B{আধানের সাম্যাবস্থা (Mass Action Law):} {\lat $np=n_i^2$}
\end{itemize}

\itm{2} \textbf{\B{ডায়োড ও রেক্টিফিকেশন (একমুখীমুখীকরণ):}}
\begin{itemize}
    \item[] \B{অর্ধতরঙ্গ রেক্টিফায়ারের গড় ভোল্টেজ:} {\lat $V_{\rm dc}=\dfrac{V_m}{\pi}$}
    \item[] \B{পূর্ণতরঙ্গ রেক্টিফায়ারের গড় ভোল্টেজ:} {\lat $V_{\rm dc}=\dfrac{2V_m}{\pi}$}
\end{itemize}

\itm{3} \textbf{\B{জেনার ডায়োড ভোল্টেজ রেগুলেটর:}}
\begin{itemize}
    \item[] \B{সিরিজ রোধের সমীকরণ:} {\lat $R_s=\dfrac{V_s-V_Z}{I_Z+I_L}$}
\end{itemize}

\itm{4} \textbf{\B{ট্রানজিস্টর ও প্রবাহ গুণাঙ্কসমূহ:}}
\begin{itemize}
    \item[] \B{প্রবাহের মূল সমীকরণ:} {\lat $I_E=I_B+I_C$}
    \item[] \B{প্রবাহ লাভ বা আলফা ($\alpha$):} {\lat $\alpha=\dfrac{I_C}{I_E}$}
    \item[] \B{প্রবাহ বিবর্ধক গুণক বা বিটা ($\beta$):} {\lat $\beta=\dfrac{I_C}{I_B}$}
    \item[] \B{আলফা থেকে বিটা রূপান্তর:} {\lat $\beta=\dfrac{\alpha}{1-\alpha}$}
    \item[] \B{বিটা থেকে আলফা রূপান্তর:} {\lat $\alpha=\dfrac{\beta}{1+\beta}$}
    \item[] \B{ভোল্টেজ লাভ (Voltage Gain):} {\lat $A_v=-\beta \dfrac{R_C}{r_{be}}$}
\end{itemize}

\itm{5} \textbf{\B{লজিক গেট ও বুলিয়ান অ্যালজেব্রা:}}
\begin{itemize}
    \item[] \B{AND গেটের সমীকরণ:} {\lat $Y=A\cdot B$}
    \item[] \B{OR গেটের সমীকরণ:} {\lat $Y=A+B$}
    \item[] \B{NOT গেটের সমীকরণ:} {\lat $Y=\bar A$}
    \item[] \B{NAND গেটের সমীকরণ:} {\lat $Y=\overline{AB}$}
    \item[] \B{NOR গেটের সমীকরণ:} {\lat $Y=\overline{A+B}$}
    \item[] \B{XOR গেটের সমীকরণ:} {\lat $Y=A\bar B+\bar AB$}
    \item[] \B{ডি-মর্গানের ১ম সূত্র:} {\lat $\overline{AB}=\bar A+\bar B$}
    \item[] \B{ডি-মর্গানের ২য় সূত্র:} {\lat $\overline{A+B}=\bar A\bar B$}
\end{itemize}

\itm{6} \textbf{\B{Operational Amplifier (অপ-অ্যাম্প):}}
\begin{itemize}
    \item[] \B{ইনভার্টিং বিবর্ধকের ভোল্টেজ লাভ:} {\lat $A_v=-\dfrac{R_f}{R_1}$}
    \item[] \B{নন-ইনভার্টিং বিবর্ধকের ভোল্টেজ লাভ:} {\lat $A_v=1+\dfrac{R_f}{R_1}$}
    \item[] \B{সামিং (যোগফল) বিবর্ধকের আউটপুট:} {\lat $V_o=-R_f\left(\dfrac{V_1}{R_1}+\dfrac{V_2}{R_2}\right)$}
    \item[] \B{ইন্টিগ্রেটর (সমাকলনকারী) আউটপুট:} {\lat $V_o=-\dfrac{1}{RC}\int V_{\rm in}\,dt$}
\end{itemize}

\chsec{অধ্যায়-১১: জ্যোতির্বিজ্ঞান ও মহাকর্ষ-শক্তি}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{মহাকর্ষীয় বিভবশক্তি,}} {\lat $U=-\dfrac{GMm}{R}$}

\itm{2} \textbf{\B{মুক্তিবেগ,}} {\lat $v_e=\sqrt{\dfrac{2GM}{R}}=\sqrt{2gR}$};\; \B{পৃথিবী:} {\lat $\approx11.2$ km/s}

\itm{3} \textbf{\B{সোয়ার্জচাইল্ড ব্যাসার্ধ,}} {\lat $R_s=\dfrac{2GM}{c^2}$}

\itm{4} \textbf{\B{হাবলের সূত্র,}} {\lat $v=H\cdot d$};\; \B{ডপলার:} {\lat $\dfrac{v}{c}=\dfrac{\Delta\lambda}{\lambda}$}

\itm{5} \textbf{\B{কেপলারের ৩য় সূত্র,}} {\lat $T^2\propto R^3$;\; $T^2=\dfrac{4\pi^2}{GM}R^3$}

\itm{6} \textbf{\B{কক্ষীয় বেগ,}} {\lat $v_o=\sqrt{GM/R}$}

\chsec{পরিশিষ্ট-ক: গুরুত্বপূর্ণ ধ্রুবকসমূহ}

\noindent
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.46\linewidth}|>{\raggedright\arraybackslash}p{0.414\linewidth}|}
\hline
\rowcolor{tblhdr} \B{১.} {\lat $c=3\times10^8$ m/s} & \B{২.} {\lat $h=6.626\times10^{-34}$ J$\cdot$s} \\
\hline
\B{৩.} {\lat $\hbar=1.055\times10^{-34}$ J$\cdot$s} & \B{৪.} {\lat $e=1.6\times10^{-19}$ C} \\
\hline
\B{৫.} {\lat $m_e=9.11\times10^{-31}$ kg} & \B{৬.} {\lat $m_p=1.673\times10^{-27}$ kg} \\
\hline
\B{৭.} {\lat $m_n=1.675\times10^{-27}$ kg} & \B{৮.} {\lat $1$ u $=1.661\times10^{-27}$ kg} \\
\hline
\B{৯.} {\lat $\varepsilon_0=8.85\times10^{-12}$ F/m} & \B{১০.} {\lat $\mu_0=4\pi\times10^{-7}$ H/m} \\
\hline
\B{১১.} {\lat $k_B=1.38\times10^{-23}$ J/K} & \B{১২.} {\lat $N_A=6.022\times10^{23}$ mol$^{-1}$} \\
\hline
\B{১৩.} {\lat $1$ eV $=1.6\times10^{-19}$ J} & \B{১৪.} {\lat $G=6.674\times10^{-11}$} \\
\hline
\B{১৫.} {\lat $g=9.8$ m/s$^2$} & \B{১৬.} {\lat $R=8.314$ J/mol$\cdot$K} \\
\hline
\B{১৭.} {\lat $\sigma=5.67\times10^{-8}$ W/m$^2$K$^4$} & \B{১৮.} {\lat $hc=1240$ eV$\cdot$nm} \\
\hline
\B{১৯.} {\lat $F=96500$ C/mol} & \B{২০.} {\lat $R_H=1.097\times10^7$ m$^{-1}$} \\
\hline
\B{২১.} {\lat $\lambda_c=2.43\times10^{-12}$ m} & \B{২২.} {\lat $a_0=0.529$ \AA} \\
\hline
\B{২৩.} {\lat $1$ Ci $=3.7\times10^{10}$ Bq} & \B{২৪.} \B{প্রমাণ বায়ুচাপ} {\lat $=1.013\times10^5$ Pa} \\
\hline
\B{২৫.} \B{শব্দের বেগ (0°C)} {\lat $=331$ m/s} & \B{২৬.} \B{শব্দের বেগ (20°C)} {\lat $=343$ m/s} \\
\hline
\B{২৭.} \B{পারদের ঘনত্ব (0°C)} {\lat $1.36\times10^4$ kg/m$^3$} & \B{২৮.} \B{বায়ুর ঘনত্ব (20°C)} {\lat $1.204$ kg/m$^3$} \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-খ: আবিষ্কারক / প্রবর্তক}

\noindent
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.506\linewidth}|>{\raggedright\arraybackslash}p{0.368\linewidth}|}
\hline
\rowcolor{tblhdr} \B{পড়ন্ত বস্তুর সূত্র} & \B{গ্যালিলিও} \\
\hline
\B{গতিসূত্র, মহাকর্ষ} & \B{স্যার আইজ্যাক নিউটন} \\
\hline
\B{সরল দোলকের সূত্রাবলি} & \B{গ্যালিলিও} \\
\hline
\B{পৃষ্ঠটানের আণবিক তত্ত্ব} & \B{ল্যাপ্লাস} \\
\hline
\B{প্লাবিতার সমীকরণ (স্টোকস)} & \B{স্টোকস} \\
\hline
\B{তাপের যান্ত্রিক/গতি/আণবিক মতবাদ} & \B{ড. জুল} \\
\hline
\B{প্লাটিনাম থার্মোমিটার} & \B{সিমেন্স} \\
\hline
\B{পূর্ণ বিকিরণ পাইরোমিটার} & \B{ফেরি} \\
\hline
\B{তাপগতিবিদ্যা ১ম সূত্র} & \B{জুল} \\
\hline
\B{তাপগতিবিদ্যা ২য় সূত্র} & \B{ক্লসিয়াস, কেলভিন} \\
\hline
\B{তড়িৎচুম্বকীয় আবেশ} & \B{ফ্যারাডে} \\
\hline
\B{সীবেক ক্রিয়া} & \B{সীবেক} \\
\hline
\B{থমসন ক্রিয়া} & \B{স্যার উইলিয়াম থমসন} \\
\hline
\B{তড়িৎচুম্বকীয় তত্ত্ব} & \B{জেমস ক্লার্ক ম্যাক্সওয়েল} \\
\hline
\B{কোয়ান্টাম তত্ত্ব} & \B{প্ল্যাঙ্ক} \\
\hline
\B{যৌগিক অণুবীক্ষণ যন্ত্র} & \B{গ্যালিলিও} \\
\hline
\B{প্রতিফলক দূরবীক্ষণ যন্ত্র} & \B{স্যার আইজ্যাক নিউটন} \\
\hline
\B{প্রতিসরাঙ্ক দূরবীক্ষণ যন্ত্র} & \B{গ্রেগরি (সর্বপ্রথম)} \\
\hline
\B{দূরবীক্ষণ যন্ত্র} & \B{হারসেল} \\
\hline
\B{নভো-দূরবীক্ষণ যন্ত্র} & \B{জ্যোতির্বিদ কেপলার} \\
\hline
\B{এক্স-রে} & \B{অধ্যাপক উইল হেলম রনজেন} \\
\hline
\B{ধনরশ্মি} & \B{গোল্ডস্টাইন} \\
\hline
\B{তেজস্ক্রিয়তা} & \B{হেনরি বেকেরেল} \\
\hline
\B{নিউট্রন} & \B{চ্যাডউইক} \\
\hline
\B{ইলেকট্রন} & \B{জে. জে. থমসন} \\
\hline
\B{প্রোটন} & \B{রাদারফোর্ড} \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-গ: গ্রিক বর্ণমালা}

\noindent
\noindent\scriptsize \begin{tabular}{|l|l|l|l|}
\hline
\rowcolor{tblhdr} \B{আলফা} {\lat $\alpha\,A$} & \B{বিটা} {\lat $\beta\,B$} & \B{গামা} {\lat $\gamma\,\Gamma$} & \B{ডেল্টা} {\lat $\delta\,\Delta$} \\
\hline
\B{এপ্সাইলন} {\lat $\varepsilon\,E$} & \B{জিটা} {\lat $\zeta\,Z$} & \B{ইটা} {\lat $\eta\,H$} & \B{থিটা} {\lat $\theta\,\Theta$} \\
\hline
\B{আয়োটা} {\lat $\iota\,I$} & \B{কাপ্পা} {\lat $\kappa\,K$} & \B{ল্যাম্বডা} {\lat $\lambda\,\Lambda$} & \B{মিউ} {\lat $\mu\,M$} \\
\hline
\B{নিউ} {\lat $\nu\,N$} & \B{ক্সাই} {\lat $\xi\,\Xi$} & \B{ওমিক্রন} {\lat $o\,O$} & \B{পাই} {\lat $\pi\,\Pi$} \\
\hline
\B{রো} {\lat $\rho\,P$} & \B{সিগমা} {\lat $\sigma\,\Sigma$} & \B{টাউ} {\lat $\tau\,T$} & \B{উপসাইলন} {\lat $\upsilon\,\Upsilon$} \\
\hline
\B{ফাই} {\lat $\phi\,\Phi$} & \B{কাই} {\lat $\chi\,X$} & \B{সাই} {\lat $\psi\,\Psi$} & \B{ওমেগা} {\lat $\omega\,\Omega$} \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-ঘ: SI উপসর্গ ও সূচক}

\noindent
\noindent\scriptsize \begin{tabular}{|l|l|l|}
\hline
\rowcolor{tblhdr} \B{এক্সা} (E) {\lat $10^{18}$} & \B{পেটা} (P) {\lat $10^{15}$} & \B{টেরা} (T) {\lat $10^{12}$} \\
\hline
\B{গিগা} (G) {\lat $10^9$} & \B{মেগা} (M) {\lat $10^6$} & \B{কিলো} (k) {\lat $10^3$} \\
\hline
\B{হেক্টো} (h) {\lat $10^2$} & \B{ডেকা} (da) {\lat $10$} & \B{ডেসি} (d) {\lat $10^{-1}$} \\
\hline
\B{সেন্টি} (c) {\lat $10^{-2}$} & \B{মিলি} (m) {\lat $10^{-3}$} & \B{মাইক্রো} ({\lat $\mu$}) {\lat $10^{-6}$} \\
\hline
\B{ন্যানো} (n) {\lat $10^{-9}$} & \B{পিকো} (p) {\lat $10^{-12}$} & \B{ফেমটো} (f) {\lat $10^{-15}$} \\
\hline
\B{অ্যাটো} (a) {\lat $10^{-18}$} & & \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-ঙ: ভৌত রাশি, একক ও মাত্রা}

\noindent\footnotesize
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.313\linewidth}|>{\raggedright\arraybackslash}p{0.092\linewidth}|>{\raggedright\arraybackslash}p{0.166\linewidth}|>{\raggedright\arraybackslash}p{0.276\linewidth}|}
\hline
\rowcolor{tblhdr} \B{রাশি} & \B{সংকেত} & \B{একক} & \B{মাত্রা} \\
\hline
\B{তড়িৎ প্রাবল্য} & {\lat $E$} & {\lat N\,C$^{-1}$} & {\lat $MLT^{-3}I^{-1}$} \\
\hline
\B{তড়িৎ বিভব} & {\lat $V$} & {\lat V} & {\lat $ML^2T^{-3}I^{-1}$} \\
\hline
\B{তড়িচ্চালক বল} & {\lat $E$} & {\lat V} & {\lat $ML^2T^{-3}I^{-1}$} \\
\hline
\B{রোধ} & {\lat $R$} & {\lat $\Omega$} & {\lat $ML^2T^{-3}I^{-2}$} \\
\hline
\B{আপেক্ষিক রোধ} & {\lat $\rho$} & {\lat $\Omega\,$m} & {\lat $ML^3T^{-3}I^{-2}$} \\
\hline
\B{পরিবাহিতা} & {\lat $\sigma$} & {\lat $\Omega^{-1}$m$^{-1}$} & {\lat $M^{-1}L^{-3}T^3I^2$} \\
\hline
\B{পরিবাহকত্ব} & {\lat $G$} & {\lat S} & {\lat $M^{-1}L^{-2}T^3I^2$} \\
\hline
\B{দৈর্ঘ্য} & {\lat $l$} & {\lat m} & {\lat $L$} \\
\hline
\B{ভর} & {\lat $m$} & {\lat kg} & {\lat $M$} \\
\hline
\B{সময়} & {\lat $t$} & {\lat s} & {\lat $T$} \\
\hline
\B{ক্ষেত্রফল} & {\lat $A$} & {\lat m$^2$} & {\lat $L^2$} \\
\hline
\B{আয়তন} & {\lat $V$} & {\lat m$^3$} & {\lat $L^3$} \\
\hline
\B{বেগ} & {\lat $v$} & {\lat m/s} & {\lat $LT^{-1}$} \\
\hline
\B{ভরবেগ} & {\lat $p$} & {\lat kg$\cdot$m/s} & {\lat $MLT^{-1}$} \\
\hline
\B{বল} & {\lat $F$} & {\lat N} & {\lat $MLT^{-2}$} \\
\hline
\B{কাজ/শক্তি} & {\lat $W,E$} & {\lat J} & {\lat $ML^2T^{-2}$} \\
\hline
\B{ক্ষমতা} & {\lat $P$} & {\lat W} & {\lat $ML^2T^{-3}$} \\
\hline
\B{কম্পাঙ্ক} & {\lat $f$} & {\lat Hz} & {\lat $T^{-1}$} \\
\hline
\B{তরঙ্গদৈর্ঘ্য} & {\lat $\lambda$} & {\lat m} & {\lat $L$} \\
\hline
\B{তাপমাত্রা} & {\lat $T,\theta$} & {\lat K} & {\lat $\theta$} \\
\hline
\B{তাপ} & {\lat $Q$} & {\lat J} & {\lat $ML^2T^{-2}$} \\
\hline
\B{তাপ ধারণক্ষমতা} & {\lat $C$} & {\lat J/K} & {\lat $ML^2T^{-2}\theta^{-1}$} \\
\hline
\B{আপেক্ষিক তাপ} & {\lat $s,c$} & {\lat J/kg$\cdot$K} & {\lat $L^2T^{-2}\theta^{-1}$} \\
\hline
\B{সুপ্ততাপ} & {\lat $L$} & {\lat J/kg} & {\lat $L^2T^{-2}$} \\
\hline
\B{তাপ পরিবাহিতা} & {\lat $K$} & {\lat W/m$\cdot$K} & {\lat $MLT^{-3}\theta^{-1}$} \\
\hline
\B{প্রবাহ} & {\lat $I$} & {\lat A} & {\lat $I$} \\
\hline
\B{চার্জ} & {\lat $q,Q$} & {\lat C} & {\lat $IT$} \\
\hline
\B{চৌম্বক ফ্লাক্স} & {\lat $\Phi$} & {\lat Wb} & {\lat $ML^2T^{-2}I^{-1}$} \\
\hline
\B{চৌম্বক ক্ষেত্র} & {\lat $B$} & {\lat T} & {\lat $MT^{-2}I^{-1}$} \\
\hline
\B{আবেশ} & {\lat $L,M$} & {\lat H} & {\lat $ML^2T^{-2}I^{-2}$} \\
\hline
\B{ধারকত্ব} & {\lat $C$} & {\lat F} & {\lat $M^{-1}L^{-2}T^4I^2$} \\
\hline
\end{tabular}
\normalsize

\chsec{পরিশিষ্ট-চ: বিভিন্ন বস্তুর আপেক্ষিক রোধ}

\textbf{\B{আপেক্ষিক রোধ}} {\lat ($\Omega\cdot$m, $\times10^{-8}$):} \B{তামা} {\lat 1.78}\B{; অ্যালুমিনিয়াম} {\lat 2.94}\B{; পিতল} {\lat 4.1}\B{; রূপা} {\lat 1.66}\B{; টিন} {\lat 3.5--11.3}\B{; সীসা} {\lat 20.8}\B{; ইস্পাত} {\lat 19.9--25.6}\B{; টাংস্টেন} {\lat 5.5}\B{; মাইকা} {\lat $9\times10^{-8}$}\B{; দস্তা} {\lat 6.10}\B{; ইউরেকা/কনস্ট্যান্টান} {\lat 49}\B{; ম্যাঙ্গানিজ} {\lat 44}\B{; জার্মান রূপা} {\lat 27}\B{; সোনা} {\lat 2.42}\B{; পারদ} {\lat 95}\B{; প্লাটিনাম} {\lat 11}\B{; নাইক্রোম} {\lat 110}\B{.}

\chsec{পরিশিষ্ট-ছ: বিভিন্ন বস্তুর প্রতিসরাঙ্ক (সোডিয়াম আলো)}

\B{শূন্যমাধ্যম} {\lat 1.00000}\B{; বায়ু (STP)} {\lat 1.00029}\B{; পানি (20°C)} {\lat 1.33}\B{; কেরোসিন} {\lat 1.44}\B{; গ্লিসারিন} {\lat 1.47}\B{; কাচ (ক্রাউন)} {\lat 1.48--1.61}\B{; কাচ (ফ্লিন্ট)} {\lat 1.53--1.96}\B{; হীরা} {\lat 2.41}\B{; বরফ} {\lat 1.31}\B{; সালফিউরিক অ্যাসিড} {\lat 1.43}\B{; প্যারাফিন মোম} {\lat 1.44}\B{; ক্লোরোফর্ম} {\lat 1.45}\B{; মাইকা} {\lat 1.5--1.60}\B{; কানাডা বালসাম} {\lat 1.53}\B{; কোয়ার্টজ} {\lat 1.54--1.553}\B{.}

\chsec{পরিশিষ্ট-জ: ভূ-চৌম্বক প্রাবল্যের অনুভূমিক উপাংশ ($H$ in $\mu$T)}

\B{ঢাকা} {\lat 37.1}\B{; রাজশাহী} {\lat 37.0}\B{; কলকাতা} {\lat 37.2}\B{; দিল্লি} {\lat 34.0}\B{; মুম্বাই} {\lat 36.5}\B{; লন্ডন} {\lat 18.0}\B{; করাচি} {\lat 34.6}\B{; লাহোর} {\lat 35.0}\B{.}

\chsec{পরিশিষ্ট-ঝ: মৌলিক বল}

\noindent
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.202\linewidth}|>{\raggedright\arraybackslash}p{0.12\linewidth}|>{\raggedright\arraybackslash}p{0.138\linewidth}|>{\raggedright\arraybackslash}p{0.12\linewidth}|>{\raggedright\arraybackslash}p{0.248\linewidth}|}
\hline
\rowcolor{tblhdr} \B{বলের প্রকার} & \B{সবলতা} & \B{পাল্লা} & \B{কণা} & \B{ভূমিকা} \\
\hline
\B{সবল নিউক্লীয়} & {\lat $1$} & {\lat $10^{-15}$ m} & \B{গ্লুয়ন/মেসন} & \B{নিউক্লিয়াসে গাঁথুনি} \\
\hline
\B{তড়িৎচৌম্বক} & {\lat $10^{-2}$} & \B{অসীম} & \B{ফোটন} & \B{পরমাণু/অণু গঠন} \\
\hline
\B{দুর্বল নিউক্লীয়} & {\lat $10^{-18}$} & {\lat $10^{-18}$ m} & {\lat W, Z} \B{বোসন} & \B{$\beta$-ক্ষয়} \\
\hline
\B{মহাকর্ষ} & {\lat $10^{-39}$} & \B{অসীম} & \B{গ্র্যাভিটন} & \B{সংসক্তি} \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-ঞ: গুরুত্বপূর্ণ মহাশূন্যযান}

\noindent
\noindent\scriptsize \begin{tabular}{|>{\raggedright\arraybackslash}p{0.276\linewidth}|>{\raggedright\arraybackslash}p{0.598\linewidth}|}
\hline
\rowcolor{tblhdr} \B{স্পুটনিক-১} (4.10.1957) & \B{মহাশূন্যে প্রথম কৃত্রিম উপগ্রহ} \\
\hline
\B{স্পুটনিক-২} (3.11.1957) & \B{জীবন্ত কুকুর বহনকারী প্রথম মহাশূন্যযান} \\
\hline
\B{স্কোর} (18.12.1958) & \B{প্রথম যোগাযোগ উপগ্রহ} \\
\hline
\B{লুনা-৩} (4.10.1959) & \B{প্রথম উপগ্রহ যা চাঁদের অদৃশ্য অংশের ছবি পাঠায়} \\
\hline
\B{ভস্টক-১} (12.4.1961) & \B{মানুষের নিয়ে প্রথম মহাশূন্য যাত্রা} \\
\hline
\B{ভস্টক-৬} (4.12.1963) & \B{প্রথম মহিলা মহাশূন্যচারী বহনকারী যান (ভ্যালেন্টিনা তেরেস্কোভা)} \\
\hline
\B{ইনটেলস্যাট-১} (6.4.1965) & \B{বাণিজ্যিক কাজে ব্যবহৃত প্রথম যোগাযোগ উপগ্রহ} \\
\hline
\end{tabular}

\chsec{পরিশিষ্ট-ট: গুরুত্বপূর্ণ শর্টকাট ও অতিরিক্ত সূত্রাবলি}

\chsub{}{গতিবিদ্যা শর্টকাট}
\itm{1} \B{সর্বোচ্চ পাল্লা:} {\lat $\theta=45°$} \B{হলে} {\lat $R_{\max}=v_0^2/g$}
\itm{2} \B{প্রাস ও পাল্লা:} {\lat $R=v_0^2\sin2\theta/g$;\; $H=v_0^2\sin^2\theta/(2g)$;\; $R=4H\cot\theta$}
\itm{3} \B{একই পাল্লার দুই কোণ:} {\lat $\theta_1+\theta_2=90°$}
\itm{4} \B{সমান্তরে নিক্ষিপ্ত বস্তু (উচ্চতা $h$):} {\lat $t=\sqrt{2h/g}$;\; $R=v_0\sqrt{2h/g}$}
\itm{5} \B{আপেক্ষিক বেগ:} {\lat $\vec v_{AB}=\vec v_A-\vec v_B$}

\chsub{}{বলবিদ্যা শর্টকাট}
\itm{6} \B{কাজ-শক্তি উপপাদ্য:} {\lat $W_{\rm net}=\Delta E_k=\tfrac{1}{2}mv^2-\tfrac{1}{2}mv_0^2$}
\itm{7} \B{ঘূর্ণনশীল বস্তুর গতিশক্তি:} {\lat $E_k=\tfrac{1}{2}I\omega^2+\tfrac{1}{2}mv_{cm}^2$}
\itm{8} \B{রোলিং বস্তু:} {\lat $v_{cm}=\omega R$;\; $a_{cm}=\alpha R$}
\itm{9} \B{ঘূর্ণনে কাজ-শক্তি:} {\lat $W=\tau\theta=\Delta(\tfrac{1}{2}I\omega^2)$}
\itm{10} \B{ঘাত-ভরবেগ:} {\lat $\vec J=\vec F\Delta t=\Delta\vec p=m(\vec v-\vec v_0)$}

\chsub{}{তরঙ্গ ও শব্দ শর্টকাট}
\itm{11} \B{সুস্বর স্ট্যান্ডিং ওয়েভ (খোলা পাইপ):} {\lat $f_n=\dfrac{nv}{2L}$;\; $n=1,2,3,\ldots$}
\itm{12} \B{বদ্ধ পাইপ:} {\lat $f_n=\dfrac{(2n-1)v}{4L}$;\; $n=1,2,3,\ldots$}
\itm{13} \B{তারের মৌলিক কম্পাঙ্ক:} {\lat $f_1=\dfrac{1}{2L}\sqrt{T/\mu}$;\; $\mu=m/L$}
\itm{14} \B{বায়ুতে শব্দের বেগ:} {\lat $v=\sqrt{\gamma P/\rho}=\sqrt{\gamma RT/M}$}
\itm{15} \B{ডপলার (উভয়ই গতিশীল):} {\lat $f'=f\dfrac{v\pm v_0}{v\mp v_s}$}

\chsub{}{তড়িৎচৌম্বক শর্টকাট}
\itm{16} \B{RC সার্কিট:} {\lat $\tau=RC$;\; $V_C=V_0(1-e^{-t/\tau})$;\; $I=I_0e^{-t/\tau}$}
\itm{17} \B{RL সার্কিট:} {\lat $\tau=L/R$;\; $I=I_0(1-e^{-t/\tau})$}
\itm{18} \B{LC দোলন:} {\lat $\omega_0=1/\sqrt{LC}$;\; $U_L+U_C=\text{const}$}
\itm{19} \B{ম্যাক্সওয়েলের সমীকরণ (সংক্ষেপ):} {\lat $\nabla\cdot\vec E=\rho/\varepsilon_0$;\; $\nabla\cdot\vec B=0$;\; $\nabla\times\vec E=-\partial\vec B/\partial t$;\; $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\partial\vec E/\partial t$}
\itm{20} \B{EM তরঙ্গ তীব্রতা:} {\lat $I=\tfrac{1}{2}\varepsilon_0cE_0^2=\tfrac{E_0B_0}{2\mu_0}$}

\chsub{}{আলোকবিদ্যা শর্টকাট}
\itm{21} \B{আলোক-তড়িৎ শর্টকাট:} {\lat $eV_s=hf-\phi$;\; $\lambda_{\rm threshold}=hc/\phi$}
\itm{22} \B{হাইড্রোজেন বর্ণালী:} \B{লাইমান} {\lat ($n_1=1$)}\B{, বামার} {\lat ($n_1=2$)}\B{, প্যাশেন} {\lat ($n_1=3$)}
\itm{23} \B{কোহেরেন্ট উৎস প্রয়োজনীয় শর্ত:} \B{একই কম্পাঙ্ক, স্থির দশা পার্থক্য, প্রায় সমান বিস্তার}
\itm{24} \B{ব্রুস্টার কোণ:} {\lat $\tan\theta_B=n_{21}$} \B{(প্রতিসরণ সূচক)}

\chsub{}{আধুনিক পদার্থবিজ্ঞান শর্টকাট}
\itm{25} \B{ভর-শক্তি রূপান্তর:} {\lat $1$ u $=931.5$ MeV};\; {\lat $1$ eV $=1.6\times10^{-19}$ J}
\itm{26} \B{তেজস্ক্রিয়তার পরিমাণ:} {\lat $N=N_0/2^{t/T_{1/2}}$;\; $A=A_0e^{-\lambda t}$}
\itm{27} \B{ফোটনের শক্তি-তরঙ্গদৈর্ঘ্য:} {\lat $E=hc/\lambda=1240/\lambda\,(\text{nm})$ eV}
\itm{28} \B{সন্নিবেশ প্রভাব:} {\lat $\Delta\lambda=2.43\times10^{-12}(1-\cos\theta)$ m}
\itm{29} \B{বোর ব্যাসার্ধ:} {\lat $r_n=n^2\times0.529\,\text{\AA}/Z$};\; \B{শক্তি:} {\lat $E_n=-13.6\,Z^2/n^2$ eV}

\chsub{}{মাত্রা বিশ্লেষণ শর্টকাট}
\noindent\scriptsize
\begin{tabular}{|>{\raggedright\arraybackslash}p{0.30\linewidth}|>{\raggedright\arraybackslash}p{0.55\linewidth}|}
\hline
\rowcolor{tblhdr} \B{রাশি} & \B{মাত্রা} \\
\hline
\B{কৌণিক বেগ} {\lat $\omega$} & {\lat $T^{-1}$} \\
\hline
\B{কৌণিক ত্বরণ} {\lat $\alpha$} & {\lat $T^{-2}$} \\
\hline
\B{টর্ক} {\lat $\tau$} & {\lat $ML^2T^{-2}$} \\
\hline
\B{কৌণিক ভরবেগ} {\lat $L$} & {\lat $ML^2T^{-1}$} \\
\hline
\B{জড়তার ভ্রামক} {\lat $I$} & {\lat $ML^2$} \\
\hline
\B{পৃষ্ঠটান} {\lat $S$} & {\lat $MT^{-2}$} \\
\hline
\B{সান্দ্রতা} {\lat $\eta$} & {\lat $ML^{-1}T^{-1}$} \\
\hline
\B{চাপ} {\lat $P$} & {\lat $ML^{-1}T^{-2}$} \\
\hline
\B{গ্র্যাভিটেশনাল ধ্রুবক} {\lat $G$} & {\lat $M^{-1}L^3T^{-2}$} \\
\hline
\B{প্ল্যাঙ্কের ধ্রুবক} {\lat $h$} & {\lat $ML^2T^{-1}$} \\
\hline
\end{tabular}
\normalsize

\end{multicols}


\clearpage
\begin{multicols*}{2}
\chsec{পরিশিষ্ট-শ: ১ম পত্রের অতিরিক্ত সার-সংক্ষেপ ও সংজ্ঞা}
\chsec{সার-সংক্ষেপ | Summary}

\begin{description}
    \item[ভৌত রাশি:] ভৌত জগতের রাশিিসমূহ হলো ভৌত রাশি। 
    \item[পদার্থবিজ্ঞান:] বিজ্ঞানের যে শাখায় পদার্থ ও শক্তি এবং এদের মিথস্ক্রিয়া সম্পর্কে আলোচনা করা হয় তাকে পদার্থবিজ্ঞান বলে। 
    \item[পদার্থবিজ্ঞানের মূলনীতি:] ভরের, জড়বেগের এবং শক্তির সংরক্ষণশীলতা নীতি হচ্ছে পদার্থবিজ্ঞানের মূলনীতি। 
    \item[বিজ্ঞান:] পরীক্ষা-নিরীক্ষা, পর্যবেক্ষণ ও পদ্ধতিগতভাবে লব্ধ সুশৃঙ্খল ও সুবব্ধ জ্ঞান এবং জ্ঞান অর্জনের প্রক্রিয়া হলো বিজ্ঞান। 
    \item[স্বীকার্য:] স্বীকার্য হলো একটি প্রস্তাবনা যার প্রমাণের প্রয়োজন হয় না, নিজে থেকেই প্রতিষ্ঠিত অথবা সত্য বলে স্বীকার করার কোনো সুনির্দিষ্ট উদ্দেশ্য থাকে এবং এটি অন্য একটি প্রস্তাবনা প্রমাণের জন্য ব্যবহৃত হয়। 
    \item[ধারণা:] ধারণা হলো কোনো বিশেষেভাবে নির্দিষ্ট আকস্মিক ঘটনা হতে উদ্ভূত সাধারণ কল্পনা, প্রমাণের ওপর নির্ভরশীল নয় এমন কোনো কিছু সম্পর্কে সার্বিক উপলব্ধি বা বোধগম্যতা হলো ধারণা। 
    \item[অনুকল্প:] কোনো পর্যবেক্ষণ, ঘটনা বা বৈজ্ঞানিক সমস্যার জন্য একটি সম্ভাব্য ব্যাখ্যা যা আরও অনুসন্ধানের মাধ্যমে যাচাই করা যায়, তাই অনুকল্প। 
    \item[নীতি:] নীতি হচ্ছে নিয়ম বা আইন যা সাধারণত মেনে চলতে পারে বা ইচ্ছানুযায়ী মেনে চলতে পারে বা কোনো কিছু অপরিহার্য পরিপন্হী। 
    \item[স্থান:] স্থান হলো বস্তু কর্তৃক অধিকৃত অঞ্চল। 
    \item[মৌলিক রাশি:] যেসব রাশি মূল অর্থাৎ স্বাধীন বা নিরপেক্ষ, যেগুলো অন্য রাশির ওপর নির্ভর করে না বরং অন্যান্য রাশি এদের ওপর নির্ভর করে তাদেরকে মৌলিক রাশি বলে। 
    \item[মৌলিক একক:] যেসব মৌলিক ভৌত রাশির একক অনপেক্ষ বা পরস্পরের ওপর নির্ভরশীল নয় তাদেরকেই বলা হয় মৌলিক একক। 
    \item[লব্ধ একক:] যেসব ভৌত রাশির একক স্বাধীন বা নিরপেক্ষ নয় অন্য কোনো মৌলিক রাশির এককের ওপর নির্ভর করে এবং একক বা একাধিক মৌলিক রাশির গুণফল বা ভাগফল থেকে উৎপন্ন হয় তাই হলো লব্ধ একক। 
    \item[পরিমাপ:] কোনো কিছুর পরিমাপ নির্ণয় করাই হলো পরিমাপ। অর্থাৎ আমাদের দৈনন্দিন জীবনের মাপজোখের বিষয়টি হলো পরিমাপ। 
    \item[ভর্নিয়ার স্কেল:] মূল বা প্রধান স্কেলের ক্ষুদ্রতম ভাগের ভগ্নাংশের নির্ভুল পরিমাপের জন্য প্রধান স্কেলের পাশে আর একটি সচল স্কেল ব্যবহার করা হয়। এটিই ভর্নিয়ার স্কেল। 
    \item[স্ক্রু গজ:] যে পরিমাপ যন্ত্রে একটি সমবাসাঠের মাইক্রোমিটার স্ক্রু থাকে সেটিই স্ক্রু গজ। 
    \item[বৈজ্ঞানিক প্রতীক:] কোনো সংখ্যাকে ১০ এর যেকোনো ঘাত এবং ১ থেকে ১০ এর মধ্যে অপসংখ্যার গুণফল হিসেবে প্রকাশ করা হলে তাকে বৈজ্ঞানিক প্রতীক বলে। 
    \item[মাত্রা:] কোনো একটি রাশি এবং তার মৌলিক এককের মধ্যে সম্পর্ক স্থাপনের জন্য যে সংকেত ব্যবহার করা হয় তাকে উক্ত রাশির মাত্রা বলে। 
    \item[মাত্রা সমীকরণ:] যে সমীকরণ মৌলিক একক এবং লব্ধ এককের মধ্যে সম্পর্ক স্থাপন করে তাকে মাত্রা সমীকরণ বলে। 
    \item[পিচট ত্রুটি:] স্ক্রু গজ যন্ত্র ক্রমাগত ব্যবহারের ফলে স্ক্রু ক্ষয় হয়ে আলগা হয়ে পড়ে এবং স্ক্রুকে উভয়দিকে একই পরিমাণ ঘুরালে সমান দূরত্ব অতিক্রম করে না, তাই পিচট ত্রুটি। 
    \item[ভর্নিয়ার ধ্রুবক:] প্রধান স্কেলের ক্ষুদ্রতম এক ভাগের চেয়ে ভর্নিয়ার স্কেলের এক ভাগ কতটুকু ছোট তার পরিমাণ হলো ভর্নিয়ার ধ্রুবক। 
    \item[লঘিষ্ঠ গণন:] স্ক্রু-নাট নীতির ওপর ভিত্তি করে গঠিত যন্ত্রগুলোর বৃত্তাকার স্কেলের একভাগ ঘুরালে স্ক্রুটি যতটুকু সরে আসে তাকে লঘিষ্ঠ গণন বলে। অর্থাৎ পিচকে বৃত্তাকার স্কেলের ভাগ সংখ্যা দ্বারা ভাগ করলে লঘিষ্ঠ গণন পাওয়া যায়। 
    \item[সম্ভাব্য ত্রুটি:] কোনো ধ্রুব রাশির সঠিক মান যে সীমার মধ্যে অবস্থান করতে পারে তাকে সম্ভাব্য ত্রুটি বলে। 
    \item[লেভেল ত্রুটি:] ভিক্ষেপী চৌদক মান যন্ত্র নিক্তি ইত্যাদি যন্ত্রে যন্ত্রটি বা যন্ত্রের পাতাতন অনুভূমিককে না থাকলে যন্ত্রের পাঠে যে ভুল হয় তাই লেভেল ত্রুটি। 
    \item[পরম ত্রুটি:] কোনো ভৌত রাশির পরিমাপে প্রকৃত মান এবং পরিমাপকৃত মানের পার্থক্যকে পরম ত্রুটি বলে। 
    \item[পিচ:] স্ক্রু গজের বৃত্তাকার স্কেলটি একবার ঘুরালে এটি রৈখিক স্কেল বরাবর যতটুকু দূরত্ব অতিক্রম করে তাই স্ক্রুর পিচ। 
    \item[স্ফেরোমিটার:] যে যন্ত্রের সাহায্যে গোলীয় তল তথা গোলকের বক্রতার ব্যাসার্ধ পরিমাপ করে গোলকের আয়তন ও গোলক পৃষ্ঠের ক্ষেত্রফল পরিমাপ করা যায় তাই স্ফেরোমিটার। 
\end{description}
\end{multicols*}

\clearpage

\chsec{পরিশিষ্ট-ষ: ২য় পত্রের বিস্তারিত সংজ্ঞা, ছক ও পার্থক্যসমূহ}

\noindent \textbf{সমোষ্ণ ও রুদ্ধতাপীয় প্রক্রিয়ার মধ্যে পার্থক্য :} \\[0.5em]
\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|p{6.5cm}|c|p{6.5cm}|}
\hline
\multicolumn{2}{|c|}{\textbf{সমোষ্ণ প্রক্রিয়া}} & \multicolumn{2}{c|}{\textbf{রুদ্ধতাপীয় প্রক্রিয়া}} \\ \hline
\textbf{১.} & এ পরিবর্তনে প্রয়োজন মত তাপ প্রয়োগ অথবা প্রত্যাহার করতে হয়। & \textbf{১.} & এ পরিবর্তনে তাপ প্রয়োগ বা প্রত্যাহার করতে হয় না। \\ \hline
\textbf{২.} & এ পরিবর্তনে তাপমাত্রা $T = \text{ধ্রুবক}$ অর্থাৎ $\Delta T = 0$ & \textbf{২.} & এ পরিবর্তনে তাপ $Q = \text{ধ্রুবক}$ অর্থাৎ $\Delta Q = 0$ \\ \hline
\textbf{৩.} & এই প্রক্রিয়ায় সিস্টেমটি হবে আবদ্ধ সিস্টেম। & \textbf{৩.} & এ প্রক্রিয়ায় সিস্টেমটি হবে বিচ্ছিন্ন সিস্টেম। \\ \hline
\textbf{৪.} & এ পরিবর্তনে পাত্রটি তাপের সুপরিবাহী হওয়া প্রয়োজন। & \textbf{৪.} & এ পরিবর্তনে পাত্রটি তাপের কুপরিবাহী হওয়া প্রয়োজন। \\ \hline
\textbf{৫.} & এটি ধীর প্রক্রিয়া। & \textbf{৫.} & এটি দ্রুত প্রক্রিয়া। \\ \hline
\textbf{৬.} & এ পরিবর্তনে পাত্রের চারপাশের মাধ্যমের তাপগ্রাহিতা উচ্চ হতে হয়। & \textbf{৬.} & এ পরিবর্তনের পাত্রের চারপাশের মাধ্যমের তাপগ্রাহিতা নিম্ন হতে হয়। \\ \hline
\textbf{৭.} & অভ্যন্তরীণ শক্তি $U = \text{ধ্রুবক}$ অর্থাৎ $\Delta U = 0$ & \textbf{৭.} & অভ্যন্তরীণ শক্তি $U \neq \text{ধ্রুবক}$ অর্থাৎ $\Delta U \neq 0$ \\ \hline
\textbf{৮.} & গ্যাসের আপেক্ষিক তাপ অসীম হবে। & \textbf{৮.} & গ্যাসের আপেক্ষিক তাপ শূন্য হবে। \\ \hline
\textbf{৯.} & এ প্রক্রিয়া $PV = \text{ধ্রুবক}$ সূত্র মেনে চলে। & \textbf{৯.} & এ প্রক্রিয়া $PV^{\gamma} = \text{ধ্রুবক}$ সূত্র মেনে চলে। \\ \hline
\textbf{১০.} & সমোষ্ণ লেখ অপেক্ষাকৃত কম খাড়া, এ রেখার ঢাল $\frac{dP}{dV} = -\frac{P}{V}$ & \textbf{১০.} & রুদ্ধতাপীয় লেখ অপেক্ষাকৃত বেশি খাড়া, এ রেখার ঢাল $\frac{dP}{dV} = -\gamma \left(\frac{P}{V}\right)$ \\ \hline
\end{tabular}
}



\bigskip

\begin{itemize}
    \item[\ding{226}] কার্নো ইঞ্জিনের দক্ষতা $45\%$ এবং উৎসের তাপমাত্রা $300\text{ K}$ হলে গ্রাহকের তাপমাত্রা $165\text{ K}$।
    \item[\ding{226}] এনট্রপি বিশৃঙ্খলাতা পরিমাণ নির্দেশ করে।
    \item[\ding{226}] $0\ ^\circ\text{C}$ তাপমাত্রার $0.01\text{ kg}$ পানিকে $10\ ^\circ\text{C}$ তাপমাত্রায় উন্নীত করলে এনট্রপির পরিবর্তন $1.5\text{ J K}^{-1}$।
    \item[\ding{226}] $0\ ^\circ\text{C}$ তাপমাত্রার $600\text{ g}$ বরফকে শুধুমাত্র গলানো হলে, এনট্রপির পরিবর্তন $738.4\text{ J K}^{-1}$।
    \item[\ding{226}] ফারেনহাইট ও সেলসিয়াস স্কেল $-40^\circ$ তাপমাত্রায় একই পাঠ দেয়।
    \item[\ding{226}] কাজ ও তাপের মধ্যে সম্পর্ক স্থাপন করে বিজ্ঞানী জুল সর্বপ্রথম তাপগতিবিদ্যার প্রথম সূত্রটি আবিষ্কার করেন। সূত্রটি শক্তির সংরক্ষণশীলতার সূত্রের বিশেষ রূপ।
    \item[\ding{226}] সমচাপ প্রক্রিয়ায় $dP = 0$, সমোষ্ণ প্রক্রিয়ায় $dT = 0$।
    \item[\ding{226}] রুদ্ধতাপ প্রক্রিয়ার ক্ষেত্রে চাপের পরিবর্তন খুব দ্রুত সংগঠিত করতে হয়। অর্থাৎ এটি দ্রুত প্রক্রিয়া।
    \item[\ding{226}] রুদ্ধতাপ প্রক্রিয়ায় তাপের পরিমাণ স্থির থাকে কিন্তু তাপমাত্রার পরিবর্তন ঘটে।
    \item[\ding{226}] কোনো পদার্থের এক মোল এর উষ্ণতা এক কেলভিন বৃদ্ধি করতে প্রয়োজনীয় তাপকে বলা হয় ঐ পদার্থের মোলার আপেক্ষিক তাপ। মোলার আপেক্ষিক তাপের একক $\text{J mol}^{-1}\text{ K}^{-1}$।
    \item[\ding{226}] সেলসিয়াস স্কেলে মৌলিক ব্যবধানকে সমান $100$ ভাগে ভাগ করা হয়েছে।
    \item[\ding{226}] $dU$ এর মান ঋণাত্মক হয় যখন সিস্টেমের অন্তঃস্থ শক্তি হ্রাস পায়।
    \item[\ding{226}] সিস্টেম দ্বারা ও সিস্টেমের উপর কাজ সম্পাদিত হলে $dW$ এর মান যথাক্রমে ধনাত্মক ও ঋণাত্মক হয়।
    \item[\ding{226}] রুদ্ধতাপীয় সংকোচনে সিস্টেমটির উষ্ণতা বাড়ে এবং প্রসারণে সিস্টেমটির উষ্ণতা কমে।
    \item[\ding{226}] এক পারমাণবিক, দ্বিপারমাণবিক ও বহুপারমাণবিক গ্যাসের ক্ষেত্রে $\gamma$ (গামা) এর মান যথাক্রমে $1.67, 1.41$ ও $1.33$।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & তাপমাত্রা, $\theta = \frac{X_\theta - X_{\text{ice}}}{X_{\text{steam}} - X_{\text{ice}}} \times 100^\circ\text{C}$ & $\theta =$ তাপমাত্রা & \\
 & \phantom{তাপমাত্রা,} $\theta = \frac{X_\theta - X_{\text{ice}}}{X_{\text{steam}} - X_{\text{ice}}} \times 180^\circ\text{F} + 32^\circ\text{F}$ & \begin{tabular}[c]{@{}l@{}}$X_\theta = \theta$ তাপমাত্রায় উষ্ণতামিতিক ধর্মের\\ মান\end{tabular} & \\ \cline{3-3}
 & দৈর্ঘ্য, চাপ, আয়তন, রোধ ও তড়িৎচালক শক্তির ক্ষেত্রে, & \begin{tabular}[c]{@{}l@{}}$X_{\text{steam}} =$ ঊর্ধ্ব স্থির বিন্দুতে\\ উষ্ণতামিতিক মান\end{tabular} & \\
 & (i) পারদ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{l_\theta - l_0}{l_{100} - l_0} \times 100^\circ\text{C}$ & & \\
\textbf{১.} & (ii) স্থির আয়তন গ্যাস থার্মোমিটারের ক্ষেত্রে, & & কেলভিন ($\text{K}$) \\
 & $\theta = \frac{P_\theta - P_0}{P_{100} - P_0} \times 100^\circ\text{C}$ & & \\ \cline{3-3}
 & (iii) স্থির চাপ গ্যাস থার্মোমিটারের ক্ষেত্রে, & \begin{tabular}[c]{@{}l@{}}$X_{\text{ice}} =$ নিম্ন স্থির বিন্দুতে উষ্ণতামিতিক\\ মান\end{tabular} & \\
 & $\theta = \frac{V_\theta - V_0}{V_{100} - V_0} \times 100^\circ\text{C}$ & & \\
 & (iv) রোধ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{R_\theta - R_0}{R_{100} - R_0} \times 100^\circ\text{C}$ & & \\
 & (v) তাপ তড়িৎ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{E_\theta - E_0}{E_{100} - E_0} \times 100^\circ\text{C}$ & & \\ \hline
 & পানির ত্রৈধ বিন্দুর সাপেক্ষে তাপমাত্রা, $T = \frac{X}{X_{\text{tr}}} \times 273.16\text{ K}$ & $T =$ তাপমাত্রা & কেলভিন ($\text{K}$) \\ \cline{3-4}
 & (i) পারদ থার্মোমিটার : $T = \frac{l}{l_{\text{tr}}} \times 273.16\text{ K}$ & & \\
\textbf{২.} & (ii) স্থির আয়তন গ্যাস থার্মোমিটার : $T = \frac{P}{P_{\text{tr}}} \times 273.16\text{ K}$ & & \\
 & (iii) স্থির চাপ গ্যাস থার্মোমিটার : $T = \frac{V}{V_{\text{tr}}} \times 273.16\text{ K}$ & $R =$ রোধ & ওহম ($\Omega$) \\
 & (iv) রোধ থার্মোমিটার : $T = \frac{R}{R_{\text{tr}}} \times 273.16\text{ K}$ & & \\
 & (v) তাপযুগল থার্মোমিটার : $T = \frac{E}{E_{\text{tr}}} \times 273.16\text{ K}$ & & \\ \hline
\end{tabular}
}

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{তাপ :} যা সিস্টেমের মধ্যে প্রবেশ করলে বা সিস্টেম হতে নির্গত হলে সিস্টেমের তাপগতীয় চলরাশির পরিবর্তন ঘটে তাই তাপ।

\noindent \textbf{তাপমাত্রা :} তাপমাত্রা হচ্ছে এমন একটি মৌলিক রাশি, যা দ্বারা কোনো বস্তু কতটুকু ঠান্ডা বা গরম তা জানা যায়।

\noindent \textbf{উষ্ণতামিতিক ধর্ম :} তাপমাত্রা পরিমাপে উপযোগী পদার্থের যেসব ধর্ম কাজে লাগানো হয়, পদার্থের ঐ ধর্মগুলোকে উষ্ণতামিতিক ধর্ম বলে।

\noindent \textbf{পানির ত্রৈধ বিন্দু :} $4.58\text{ mm}$ পারদ চাপে যে তাপমাত্রায় বিশুদ্ধ বরফ, পানি ও জলীয় বাষ্প একই তাপীয় সাম্যে থাকে তাকে পানির ত্রৈধ বিন্দু বলে।

\noindent \textbf{থার্মোমিটার :} যে যন্ত্রের সাহায্যে কোনো বস্তুর তাপমাত্রা সঠিকভাবে পরিমাপ করা যায় এবং বিভিন্ন বস্তুর তাপমাত্রার পার্থক্য নির্ণয় করা যায় তাকে থার্মোমিটার বলে।

\noindent \textbf{আপেক্ষিক তাপ :} $1\text{ kg}$ ভরের কোনো বস্তুর তাপমাত্রা $1\text{ K}$ বৃদ্ধি করতে প্রয়োজনীয় তাপকে ঐ বস্তুর আপেক্ষিক তাপ বলে।

\noindent \textbf{উষ্ণতা :} তাপমাত্রা হচ্ছে এমন একটি মৌলিক রাশি, যা দ্বারা কোনো বস্তু কতটুকু ঠান্ডা বা গরম তা জানা যায়।

\noindent \textbf{তাপীয় সমতা :} ভিন্ন তাপমাত্রার দুটি বস্তু পরস্পর তাপীয় সংস্পর্শে আসার পর যখন সমতাপমাত্রায় উপনীত হয় তখন ঐ অবস্থাই হলো তাপীয় সমতা।

\noindent \textbf{মৌলিক ব্যবধান :} তাপমাত্রার বিভিন্ন স্কেলের ঊর্ধ্ব স্থিরাঙ্ক ও নিম্ন স্থিরাঙ্ক মধ্যবর্তী তাপমাত্রার ব্যবধানই মৌলিক ব্যবধান।

\noindent \textbf{তাপগতীয় চলক :} তাপগতিবিদ্যার তাপমাত্রা, চাপ ও আয়তনই তাপগতীয় চলক।

\noindent \textbf{তাপগতিবিদ্যার ১ম সূত্র :} তাপগতিবিদ্যার প্রথম সূত্রটি হলো— যখন যান্ত্রিক শক্তিকে সম্পূর্ণরূপে তাপে বা তাপশক্তিকে সম্পূর্ণরূপে কাজে রূপান্তরিত করা হয় তখন যান্ত্রিক শক্তি ও তাপ পরস্পরের সমানুপাতিক হয়।

\noindent \textbf{তাপগতিবিদ্যা :} পদার্থবিজ্ঞানের যে শাখায় তাপ ও যান্ত্রিক কাজের সম্পর্ক সম্বন্ধে আলোচনা করা হয় তাকে তাপগতিবিদ্যা বলে।

\noindent \textbf{তাপীয় সিস্টেম :} পরীক্ষা-নিরীক্ষার সময় আমরা জড় জগতের যে নির্দিষ্ট তাপীয় অংশ বিবেচনা করি তাই তাপীয় সিস্টেম।

\noindent \textbf{রুদ্ধতাপীয় প্রক্রিয়া :} যে তাপগতীয় প্রক্রিয়ায় সিস্টেম থেকে তাপ বাইরে যায় না বা বাইরে থেকে কোনো তাপ সিস্টেমে আসে না তাই রুদ্ধতাপীয় প্রক্রিয়া।

\noindent \textbf{সমচাপ প্রক্রিয়া :} যে তাপগতীয় প্রক্রিয়ায় সিস্টেমের চাপের কোনো পরিবর্তন হয় না তাই সমচাপ প্রক্রিয়া।

\noindent \textbf{সমতাপীয় প্রক্রিয়ার :} যে প্রক্রিয়ায় সিস্টেম থেকে তাপ বাইরে যায় না বা বাইরে থেকে কোনো তাপ সিস্টেমে আসে না তাকে সমতাপীয় প্রক্রিয়া বলে।

\noindent \textbf{উন্মুক্ত সিস্টেম :} যে সিস্টেম তার পরিবেশের সাথে শক্তি বিনিময় করতে পারে তাকে উন্মুক্ত সিস্টেম বলে।

\noindent \textbf{বিচ্ছিন্ন সিস্টেম :} যে সিস্টেম পরিবেশ দ্বারা মোটেই প্রভাবিত হয় না অর্থাৎ পরিবেশের সাথে ভর বা শক্তি কোনো কিছুই বিনিময় করে না তাকে বিচ্ছিন্ন সিস্টেম বলে।

\noindent \textbf{মোলার আপেক্ষিক তাপ :} এক মোল কোনো গ্যাসের তাপমাত্রা এক কেলভিন বৃদ্ধি করতে যে পরিমাণ তাপের প্রয়োজন হয় তাকে ঐ গ্যাসের মোলার আপেক্ষিক তাপ বলে।

\noindent \textbf{মোলার তাপধারণ ক্ষমতা :} এক মোল গ্যাসের তাপমাত্রা এক কেলভিন বৃদ্ধি করতে প্রয়োজনীয় তাপকে ঐ গ্যাসের মোলার তাপধারণ ক্ষমতা বা মোলার আপেক্ষিক তাপ বলে।

\noindent \textbf{অন্তঃস্থ শক্তি :} বস্তুর অভ্যন্তরস্থ অণু, পরমাণু ও মৌলিক কণাসমূহের রৈখিক গতি, স্পন্দন গতি ও ঘূর্ণনগতি এবং তাদের মধ্যকার বলের কারণে উদ্ভূত শক্তিই অন্তঃস্থ শক্তি।

\noindent \textbf{তরলীকরণ :} বাষ্পচাপ পদ্ধতিতে রাসায়নিক পদার্থকে বাষ্প থেকে তরলে রূপান্তরের প্রক্রিয়াকে তরলীকরণ বা কনডেনসেশন বলে।

\noindent \textbf{মেয়ারের প্রকল্প :} কোনো নির্দিষ্ট পরিমাণ গ্যাসের অভ্যন্তরীণ শক্তি শুধুমাত্র এর তাপমাত্রার উপর নির্ভর করে। এর চাপ বা আয়তনের উপর নির্ভর করে না। এটিই মেয়ারের প্রকল্প।

\noindent \textbf{তাপের যান্ত্রিক সমতা :} একক তাপ উৎপন্ন করতে যে পরিমাণ কাজ করতে হয় বা একক তাপ দ্বারা যে পরিমাণ কাজ করা যায় তাকে তাপের যান্ত্রিক সমতা বলে।

\noindent \textbf{তাপগতিবিদ্যার ২য় সূত্র :} তাপগতিবিদ্যার ২য় সূত্রটি হলো— বাইরের কোনো শক্তির সাহায্য ছাড়া কোনো স্বয়ংক্রিয় যন্ত্রের পক্ষে নিম্ন তাপমাত্রার কোনো বস্তু হতে উচ্চ তাপমাত্রার কোনো বস্তুতে তাপের স্থানান্তর সম্ভব নয়।

প্রত্যাপ্যামী প্রক্রিয়া : যে প্রক্রিয়া বিপরীতমুখী হয়ে প্রত্যাবর্তন করতে পারে অর্থাৎ সম্মুখগামী প্রক্রিয়ার কার্যনির্বাহক বস্তুটির প্রতিটি স্তর পশ্চাৎগামী প্রক্রিয়ায় প্রতিটি স্তরের সাথে সর্বতোভাবে মিলে যায়, তাকে প্রত্যাপ্যামী প্রক্রিয়া বলা হয়।
অপ্রত্যাবর্তী প্রক্রিয়া : যে প্রক্রিয়া বিপরীতমুখী হয়ে প্রত্যাবর্তন করতে পারে না তাকে অপ্রত্যাবর্তী প্রক্রিয়া বলে।
কার্নো চক্র : যে বিশেষ প্রক্রিয়ায় কাজ করলে একটি আদর্শ তাপ ইঞ্জিন তথা কার্নো ইঞ্জিন অবিরাম শক্তি সরবরাহ করতে পারে তাই কার্নো চক্র।
তাপ ইঞ্জিন : যে যন্ত্র তাপশক্তির বিনিময়ে কাজ করতে পারে তাকে তাপ ইঞ্জিন বলে।
কার্যকৃত সহণ : কার্যকৃত সহণ হলো রেফ্রিজারেটর হতে অপসারিত তাপ ও কম্প্রেসার কর্তৃক সরবরাহকৃত যান্ত্রিক কাজের অনুপাত।
রেফ্রিজারেটর : যে যন্ত্রের সাহায্যে পরিবেশ অপেক্ষা কম তাপমাত্রা সৃষ্টি করা যায় এবং তাপমাত্রা সর্বদা স্থির অবস্থায় রাখা যায় তাকে রেফ্রিজারেটর বলে।
\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}
\ding{226} তাপমাত্রা পরিমাপে উপযোগী পদার্থের ধর্মসমূহকে উচ্চতামিতিক ধর্ম বলা হয়।
\ding{226} কোনো বস্তুর অণুগুলোর গতিশক্তি বৃদ্ধি পেলে তাপমাত্রার বৃদ্ধি পায়।
\ding{226} স্থির আয়তন গ্যাস থার্মোমিটারে ব্যবহৃত উচ্চতামিতিক পদার্থ গ্যাস।
\ding{226} রিক্রিয়াল পাইরোমিটারে উচ্চতামিতিক পদার্থ হিসেবে কৃষ্ণকায় পাত ব্যবহার করা হয়।
\ding{226} থার্মোকপল দ্বারা   থেকে   পরিসরের তাপমাত্রা পরিমাপ করা যায়।
\ding{226}   তাপমাত্রা সেন্টিগ্রেড স্কেলের দ্বিগুণ।
\ding{226} মানবদেহের তাপমাত্রা   হলে সেলসিয়াস স্কেলে এর মান   ।
\ding{226} 200 m উঁচু জলপ্রপাতের তলদেশ ও শীর্ষ দেশের তাপমাত্রার ব্যবধান   ।
\ding{226} ভিন্ন তাপমাত্রার দুটি বস্তুর পরস্পরের সংস্পর্শে থেকে সম তাপমাত্রায় উপনীত হওয়াকে তাপীয় সমতা বলা হয়।
\ding{226} প্রমাণ চাপে যে তাপমাত্রায় বিতক বরফ গলতে শুরু করে তাকে বরফ বিন্দু বলে।
\ding{226} ফারেনহাইট স্কেল প্রবর্তন করেন জি.ডি. ফারেনহাইট।
\ding{226} তাপমাত্রা পরিমাপের সেলসিয়াস স্কেল প্রবর্তন করেন অ্যান্ডার্স সেলসিয়াস।
\ding{226} কেলভিন স্কেলে বরফ বিন্দুর মান   ।
\ding{226} সেলসিয়াস স্কেলের 100 ভাগ ফারেনহাইট স্কেলের 180 ভাগের সমান।
\ding{226} মানবদেহে তাপমাত্রা পরিমাপের জন্য ব্যবহৃত থার্মোমিটার ফারেনহাইট স্কেলে দাপ্তরিত থাকে।
\ding{226} তাপগতিবিদ্যার 1ম সূত্র সর্বপ্রথম জুল আবিষ্কার করেন।
\ding{226} 20 cal তাপ সম্পূর্ণরূপে যান্ত্রিক শক্তিকে রূপান্তরিত হলে 84 J জুল যান্ত্রিক শক্তি উৎপন্ন হবে।
\ding{226} কোনো ব্যবস্থা দ্রুত আয়তনে 500 J তাপ বর্জন করলে ব্যবস্থাটির অন্তঃস্থ শক্তির পরিবর্তন   ।
\ding{226} দ্বিপারমাণবিক গ্যাসের ক্ষেত্রে   এর মান 1.40।
\ding{226}   হলে সিস্টেমে গ্যাসের স্বাভাবিক সংখ্যা 3।
\ding{226} অক্সিজেনের স্থির আয়তনে মোলার তাপধারণ ক্ষমতা   ।
\ding{226} যে তাপগতীয় প্রক্রিয়ায় চাপের কোনো পরিবর্তন হয় না তাকে সমচাপ প্রক্রিয়া বলে।
\ding{226} রুদ্ধতাপ প্রক্রিয়ায় দ্বি-পরমাণু গ্যাসের চাপ 0.5% বৃদ্ধি করা হলে গ্যাসের আয়তন 0.36% কমবে।
\ding{226} 1 mol গ্যাসের তাপমাত্রা 1 K বৃদ্ধি করতে প্রয়োজনীয় তাপকে মোলার তাপধারণ ক্ষমতা বলে।
\ding{226} মোলার আপেক্ষিক তাপের একক   ।
\ding{226} গ্যাসকে হঠাৎ সংকুচিত করে তার আয়তন এক তৃতীয়াংশ করা হলে চূড়ান্ত তাপমাত্রা   ।
\ding{226} ফুটন্ত পানি বাষ্পে পরিণত হওয়ার সময় পানির আপেক্ষিক-তাপ   ।
\ding{226} 6 cal তাপশক্তিকে কাজে পরিণত করলে 33.6 J জুল কাজ হবে।
\ding{226} রেফ্রিজারেট স্থান থেকে আগত উষ্ণ বাষ্প কম্প্রেসারে প্রেরণ করা হয়।
\ding{226} একটি কার্নো ইঞ্জিন পানির বাষ্পবিন্দু ও বরফ বিন্দুর মধ্যে কাজ করলে এর দক্ষতা 26.81%।
\ding{226} একটি তাপ ইঞ্জিন   ও   এর মধ্যে কার্যত হলে এর কর্মদক্ষতা 22.3%।
\ding{226} কোনো তাপ ইঞ্জিন থেকে তাপ বর্জিত না হলে ইঞ্জিনের দক্ষতা 100% হবে।

\ding{226} কার্নো ইঞ্জিনের দক্ষতা 45% এবং উৎসের তাপমাত্রা 300 K হলে গ্রাহকের তাপমাত্রা 165 K।
\ding{226} এন্ট্রপি বিশৃঙ্খলতা পরিমাণ নির্দেশ করে।
\ding{226} 0 °C তাপমাত্রার 0.01 kg পানিকে 10 °C তাপমাত্রায় উত্তীর্ণ করলে এন্ট্রপির পরিবর্তন   ।
\ding{226} 0 °C তাপমাত্রার 600 g বরফকে শুধুমাত্র গলানো হলে, এন্ট্রপির পরিবর্তন   ।
\ding{226} ফারেনহাইট ও সেলসিয়াস স্কেল - 40° তাপমাত্রায় একই পাঠ দেয়।
\ding{226} কাজ ও তাপের মধ্যে সম্পর্ক স্থাপন করে বিজ্ঞানী জুল সর্বপ্রথম তাপগতিবিদ্যার প্রথম সূত্রটি আবিষ্কার করেন। সূত্রটি শক্তির সংরক্ষণশীলতার সূত্রের বিশেষ রূপ।
\ding{226} সমচাপ প্রক্রিয়ায়   , সমোষ্ণ প্রক্রিয়ায়   ।
\ding{226} রুদ্ধতাপ প্রক্রিয়ার ক্ষেত্রে তাপের পরিবর্তন খুব দ্রুত সংঘটিত করতে হয়। অর্থাৎ এটি দ্রুত প্রক্রিয়া।
\ding{226} রুদ্ধতাপ প্রক্রিয়ায় তাপের পরিমাণ স্থির থাকে কিন্তু তাপমাত্রার পরিবর্তন ঘটে।
\ding{226} কোনো পদার্থের এক মোল এর উষ্ণতা এক কেলভিন বৃদ্ধি করতে প্রয়োজনীয় তাপকে বলা হয় ঐ পদার্থের মোলার আপেক্ষিক তাপ। মোলার আপেক্ষিক তাপের একক   ।
\ding{226} সেলসিয়াস স্কেলে মৌলিক ব্যবধানকে সমান 100 ভাগে ভাগ করা হয়েছে।
\ding{226}   এর মান ঋণাত্মক হয় যখন সিস্টেমের অন্তঃস্থ শক্তি হ্রাস পায়।
\ding{226} সিস্টেম দ্বারা ও সিস্টেমের উপর কাজ সম্পাদিত হলে   এর মান যথাক্রমে ধনাত্মক ও ঋণাত্মক হয়।
\ding{226} রুদ্ধতাপীয় সঙ্কোচনে সিস্টেমটির উষ্ণতা বাড়ে এবং প্রসারণে সিস্টেমটির উষ্ণতা কমে।
\ding{226} এক পারমাণবিক, দ্বিপারমাণবিক ও বহুপারমাণবিক গ্যাসের ক্ষেত্রে   (গামা) এর মান যথাক্রমে 1.67, 1.41 ও 1.33।

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\begin{tabular}{|c|l|l|c|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \textbf{একক} \\ \hline
 & তাপমাত্রা, $\theta = \frac{X_\theta - X_{\text{ice}}}{X_{\text{steam}} - X_{\text{ice}}} \times 100^\circ\text{C}$ & $\theta = \text{তাপমাত্রা}$ & \\
 & \phantom{তাপমাত্রা,} $\theta = \frac{X_\theta - X_{\text{ice}}}{X_{\text{steam}} - X_{\text{ice}}} \times 180^\circ\text{F} + 32^\circ\text{F}$ & $X_\theta = \theta$ তাপমাত্রায় উষ্ণতামিতিক ধর্মের & \\
 & দৈর্ঘ্য, চাপ, আয়তন, রোধ ও তড়িৎচালক শক্তির ক্ষেত্রে, & মান & \\ \cline{3-3}
 & (i) পারদ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{l_\theta - l_0}{l_{100} - l_0} \times 100^\circ\text{C}$ & \begin{tabular}[c]{@{}l@{}}$X_{\text{steam}} = \text{উর্ধ্ব স্থির বিন্দুতে}$\\ \phantom{$X_{\text{steam}} =$} $\text{উষ্ণতামিতিক মান}$\end{tabular} & \\
\textbf{১.} & (ii) স্থির আয়তন গ্যাস থার্মোমিটারের ক্ষেত্রে, & & কেলভিন ($\text{K}$) \\
 & $\theta = \frac{P_\theta - P_0}{P_{100} - P_0} \times 100^\circ\text{C}$ & & \\ \cline{3-3}
 & (iii) স্থির চাপ গ্যাস থার্মোমিটারের ক্ষেত্রে, & \begin{tabular}[c]{@{}l@{}}$X_{\text{ice}} = \text{নিম্ন স্থির বিন্দুতে উষ্ণতামিতিক}$\\ \phantom{$X_{\text{ice}} =$} $\text{মান}$\end{tabular} & \\
 & $\theta = \frac{V_\theta - V_0}{V_{100} - V_0} \times 100^\circ\text{C}$ & & \\
 & (iv) রোধ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{R_\theta - R_0}{R_{100} - R_0} \times 100^\circ\text{C}$ & & \\
 & (v) তাপ তড়িৎ থার্মোমিটারের ক্ষেত্রে, $\theta = \frac{E_\theta - E_0}{E_{100} - E_0} \times 100^\circ\text{C}$ & & \\ \hline
 & পানির ত্রৈধ বিন্দুর সাপেক্ষে তাপমাত্রা, $T = \frac{X}{X_{\text{tr}}} \times 273.16\text{ K}$ & $T = \text{তাপমাত্রা}$ & কেলভিন ($\text{K}$) \\ \cline{3-4}
 & (i) পারদ থার্মোমিটার : $T = \frac{l}{l_{\text{tr}}} \times 273.16\text{ K}$ & & \\
\textbf{২.} & (ii) স্থির আয়তন গ্যাস থার্মোমিটার : $T = \frac{P}{P_{\text{tr}}} \times 273.16\text{ K}$ & & \\
 & (iii) স্থির চাপ গ্যাস থার্মোমিটার : $T = \frac{V}{V_{\text{tr}}} \times 273.16\text{ K}$ & $R = \text{রোধ}$ & ওহম ($\Omega$) \\
 & (iv) রোধ থার্মোমিটার : $T = \frac{R}{R_{\text{tr}}} \times 273.16\text{ K}$ & & \\
 & (v) তাপযুগল থার্মোমিটার : $T = \frac{E}{E_{\text{tr}}} \times 273.16\text{ K}$ & & \\ \hline
\end{tabular}


\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $C = \text{সেন্টিগ্রেড স্কেলে পাঠ}$ & ডিগ্রি সেলসিয়াস ($^\circ\text{C}$) \\ \cline{3-4} 
\textbf{৩.} & তাপমাত্রা স্কেলের সম্পর্ক, $\frac{C}{5} = \frac{F - 32}{9} = \frac{K - 273}{5}$ & $F = \text{ফারেনহাইট স্কেলে পাঠ}$ & ডিগ্রি ফারেনহাইট ($^\circ\text{F}$) \\ \cline{3-4} 
 & & $K = \text{কেলভিন স্কেলে পাঠ}$ & কেলভিন ($\text{K}$) \\ \hline
 & ত্রুটিপূর্ণ থার্মোমিটারের ক্ষেত্রে, & $S = \text{ত্রুটিপূর্ণ স্কেলের তাপমাত্রা}$ & ডিগ্রি সেলসিয়াস ($^\circ\text{C}$) \\ \cline{3-3}
\textbf{৪.} & $\frac{S - M}{B - M} = \frac{C}{100} = \frac{F - 32}{180}$ & $B = \text{ঊর্ধ্ব স্থিরাঙ্ক}$ & বা ডিগ্রি ফারেনহাইট \\ \cline{3-3}
 & & $M = \text{নিম্ন স্থিরাঙ্ক}$ & ($^\circ\text{F}$) \\ \hline
\textbf{৫.} & কৃতকাজ, $W = JQ$ & $J = \text{তাপীয় সমতা}$ & জুল-ক্যালরি ($\text{J cal}^{-1}$) \\ \cline{3-4} 
 & & $Q = \text{তাপ}$ & ক্যালরি ($\text{cal}$) \\ \hline
 & অভ্যন্তরীণ শক্তির পরিবর্তন, $\Delta U = \Delta Q + \Delta W$ & $dQ = \text{গৃহীত তাপ শক্তি}$ & \\
\textbf{৬.} & বা, $dQ = dU + dW = dU + P\,dV$ & $dU = \text{অভ্যন্তরীণ শক্তির পরিবর্তন}$ & জুল ($\text{J}$) \\
 & & $dW = \text{সম্পন্ন কাজ}$ & \\ \hline
\textbf{৭.} & সমচাপ প্রক্রিয়ায় কাজ, $W = P(V_2 - V_1)$ & $P = \text{চাপ}$ & $\text{Nm}^{-2}$ \\ \cline{3-4} 
 & & $V = \text{আয়তন}$ & $\text{m}^3$ \\ \hline
 & সমোষ্ণ প্রক্রিয়ার ক্ষেত্রে : $dW = dQ$ এবং $P_1V_1 = P_2V_2$ & $P = \text{চাপ}$ & $\text{Nm}^{-2}$ \\ \cline{3-4} 
 & রুদ্ধতাপীয় প্রক্রিয়ার ক্ষেত্রে : & $V = \text{আয়তন}$ & $\text{m}^3$ \\ \cline{3-4} 
\textbf{৮.} & (i) $dW = -dQ$; (ii) $P_1V_1^\gamma = P_2V_2^\gamma$ & & \\
 & (iii) $T_1V_1^{\gamma-1} = T_2V_2^{\gamma-1}$; (iv) $T_1P_1^{\frac{1-\gamma}{\gamma}} = T_2P_2^{\frac{1-\gamma}{\gamma}}$ & $T = \text{তাপমাত্রা}$ & $\text{K}$ \\ \hline
\textbf{৯.} & $C_p - C_v = R$ এবং $\gamma = \frac{C_p}{C_v}$ & $C_p = \text{স্থির চাপে মোলার আপেক্ষিক তাপ}$ & $\text{J mol}^{-1}\text{K}^{-1}$ \\ \cline{3-4} 
 & & $C_v = \text{স্থির আয়তনে মোলার আপেক্ষিক তাপ}$ & $\text{J mol}^{-1}\text{K}^{-1}$ \\ \hline
 & (i) সমোষ্ণ প্রসারণে কাজ : $W = RT \ln \frac{V_2}{V_1}$ & & \\
 & (ii) সমোষ্ণ সংকোচনে কাজ : $W = -RT \ln \frac{V_2}{V_1}$ & $T_1 = \text{তাপ উৎসের তাপমাত্রা}$ & \\
\textbf{১০.} & (iii) রুদ্ধতাপীয় প্রসারণে কাজ, & $T_2 = \text{তাপগ্রাহকের তাপমাত্রা}$ & কেলভিন ($\text{K}$) \\
 & \phantom{(iii)} $W = \frac{R}{\gamma - 1}(T_1 - T_2) = C_v(T_1 - T_2)$ & & \\
 & (iv) রুদ্ধতাপীয় সংকোচনে কাজ, & & \\
 & \phantom{(iv)} $W = \frac{R}{\gamma - 1}(T_2 - T_1) = C_v(T_2 - T_1)$ & & \\ \hline
\textbf{১১.} & কার্যকৃত সহগ, $K = \frac{Q_2}{Q_1 - Q_2}$ & $Q_1 = \text{উৎস হতে গৃহীত তাপ}$ & জুল ($\text{J}$) \\ \cline{3-3}
 & & $Q_2 = \text{উৎস কর্তৃক বর্জিত তাপ}$ & \\ \hline
 & (i) ইঞ্জিনের দক্ষতা, $\eta = \left(1 - \frac{Q_2}{Q_1}\right) \times 100\%$ & $T_1 = \text{তাপ উৎসের তাপমাত্রা}$ & কেলভিন ($\text{K}$) \\ \cline{3-4} 
\textbf{১২.} & (ii) ইঞ্জিনের দক্ষতা, $\eta = \left(1 - \frac{T_2}{T_1}\right) \times 100\%$ & $T_2 = \text{তাপগ্রাহকের তাপমাত্রা}$ & \\ \cline{3-4} 
 & & $Q_1 = \text{উৎস হতে গৃহীত তাপ}$ & জুল ($\text{J}$) \\ \cline{3-3}
 & (iii) কার্নো প্রত্যাগামী $\frac{Q_1}{T_1} = \frac{Q_2}{T_2}$ & $Q_2 = \text{উৎস কর্তৃক বর্জিত তাপ}$ & \\ \hline
 & (i) একই তাপমাত্রায় এনট্রপির পরিবর্তন, & $dQ = \text{তাপমাত্রার পরিবর্তন}$ & কেলভিন ($\text{K}$) \\ \cline{3-4} 
 & $     dS = \frac{dQ}{T}$; $dQ = mL_f$ বা $dQ = mL_v$ & $dS = \text{এনট্রপির পরিবর্তন}$ & জুল/কেলভিন ($\text{JK}^{-1}$) \\ \cline{3-4} 
\textbf{১৩.} & (ii) ভিন্ন তাপমাত্রায় এনট্রপির পরিবর্তন, & & \\
 & $     \Delta S = ms \int_{T_1}^{T_2} \frac{dT}{T} = ms \ln \frac{T_2}{T_1}$ & $L_f = \text{আপেক্ষিক সুপ্ততাপ}$ & জুল/কেজি ($\text{Jkg}^{-1}$) \\ \hline
\end{tabular}
}

\noindent \textbf{কয়েকটি বস্তুর ডাই ইলেকট্রিক ধ্রুবক :} \\

\bigskip

\begin{tabular}{|l|c|l|c|}
\hline
\multicolumn{1}{|c|}{\textbf{বস্তুর নাম}} & \textbf{ডাই-ইলেকট্রিক ধ্রুবক (K)} & \multicolumn{1}{c|}{\textbf{বস্তুর নাম}} & \textbf{ডাই ইলেকট্রিক ধ্রুবক (K)} \\ \hline
শূন্য (বস্তুর উপস্থিতি নেই) & $1.0$ & পলিথিন & $2.3$ \\ \hline
হাইড্রোজেন ($1$ বায়ু চাপে) & $1.000264$ & পলিভিনাইল ক্লোরাইড & $3.18$ \\ \hline
অক্সিজেন ($1$ বায়ু চাপে) & $1.00055$ & & \\ \hline
বাতাস ($1$ বায়ু চাপে) & $1.0059$ & ইবোনাইট & $2.69 - 3.4$ \\ \hline
বাতাস ($100$ বায়ু চাপে) & $1.0548$ & অ্যাম্বার & $2.7$ \\ \hline
মোম & $2.1 - 2.5$ & মাইলার & $3.1$ \\ \hline
টেফলন & $2.1$ & মাইকা & $3 - 6$ \\ \hline
রবার & $2 - 3.0$ & বরফ & $3$ \\ \hline
কাগজ & $2 - 3.5$ & কাচ & $3 - 3.7$ \\ \hline
মোমযুক্ত কাগজ & $2.2$ & & \\ \hline
গন্ধক & $3.8 - 4.3$ & কাচ (ক্রাউন) & $3 - 7$ \\ \hline
কাঠ & $5$ & অ্যামোনিয়া (তরল) & $25$ \\ \hline
সোডিয়াম ক্লোরাইড & $6.12$ & ইথাইল অ্যালকোহল & $26.8$ \\ \hline
চিনামাটি & $6 - 8$ & জার্মেনিয়াম & $16$ \\ \hline
কাচ (ফ্লিন্ট) & $7 - 10$ & গ্লিসারিন & $42.5$ \\ \hline
বেনজিন & $2.28$ & পানি & $80.4$ \\ \hline
\end{tabular}

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}
বিন্দু চার্জের জন্য কুলম্বের সূত্র : কুলম্বের সূত্রটি হলো— নির্দিষ্ট মাধ্যমে দুটি বিন্দু আধানের মধ্যে ক্রিয়াশীল আকর্ষণ বা বিকর্ষণ বলের মান আধানদ্বয়ের গুণফলের সমানুপাতিক, এদের মধ্যবর্তী দূরত্বের বর্গের ব্যস্তানুপাতিক এবং এই বল আধানদ্বয়ের সংযোজক সরলরেখা বরাবর ক্রিয়া করে।
তড়িৎ বিভব : অসীম দূর থেকে একক ধনাত্মক আধানকে তড়িৎ ক্ষেত্রের কোনো বিন্দুতে আনতে কৃতকাজের পরিমাণই হলো তড়িৎ বিভব।
চার্জের তল ঘনত্ব : কোনো চার্জিত পরিবাহী পৃষ্ঠের যেকোনো বিন্দুর চারপাশে একক ক্ষেত্রফলে যে পরিমাণ চার্জ বর্তমান থাকে তাকে ঐ বিন্দুতে ঐ পরিবাহীর চার্জের তল ঘনত্ব বলে।
তড়িৎ তীব্রতা : তড়িৎ ক্ষেত্রের কোনো বিন্দুতে একটি একক ধনাত্মক চার্জ স্থাপন করলে তার উপর যে বল প্রযুক্ত হয়, তাকে ঐ তড়িৎ ক্ষেত্রের জন্য উক্ত বিন্দুর তড়িৎ তীব্রতা বলে।
বিন্দু চার্জ : আহিত বা চার্জিত বস্তুর আকার যখন খুবই ক্ষুদ্র হয় তখন ঐ চার্জিত বস্তুর চার্জকে বিন্দু চার্জ বলে।
তড়িৎ আবেশ : চার্জিত বস্তুর উপস্থিতিতে অচার্জিত পরিবাহী ক্ষণস্থায়ীভাবে চার্জিত হওয়াই তড়িৎ আবেশ।
তড়িৎক্ষেত্র : একটি আহিত বস্তুর চারদিকে যে অঞ্চলব্যাপী তার প্রভাব বজায় থাকে সেই অঞ্চলকে ঐ আহিত বস্তুর তড়িৎ বলক্ষেত্র বা তড়িৎক্ষেত্র বলে।
তড়িৎ প্রাবল্য : কোনো বিন্দুতে একক আধান বা চার্জের উপর ক্রিয়াশীল বলই তড়িৎ ক্ষেত্রের প্রাবল্য।
স্থির তড়িৎ : স্থির আধান বা প্রভাবের ক্রিয়াই স্থির তড়িৎ।
তড়িৎ বলরেখা : তড়িৎক্ষেত্রে স্থাপিত একটি একক ধনাত্মক চার্জ স্থাপন করলে এটি যে পথে পরিভ্রমণ করে তাকে তড়িৎ বলরেখা বলে।
১ কুলম্ব আধানের : দুটি সম মানের চার্জ শূন্য মাধ্যমে ১ মিটার দূরে অবস্থান করে পরস্পরের ওপর   N বল প্রয়োগ করলে ঐ চার্জ দুটির প্রত্যেককে ১ কুলম্ব বলে।
সমবিভব তল : যে চার্জিত তলের প্রতিটি বিন্দুর বিভব সমান তাকে সমবিভব তল বলে।
তড়িৎ দ্বিমেরু : এক জোড়া সমান ও বিপরীত বিন্দু আধান অল্প দূরত্বে অবস্থিত থাকলে তাকে তড়িৎ দ্বিমেরু বলে।
তড়িৎ দ্বিমেরু ভ্রামক : কোনো একটি তড়িৎ দ্বিমেরুর যেকোনো একটি আধানের পরিমাণ এবং তাদের মধ্যবর্তী দূরত্বের গুণফলকে দ্বিমেরু ভ্রামক বলে।
বদ্ধ আধান : আবিষ্ট পরিবাহকের যে প্রান্ত আবেশী বস্তুর নিকটে থাকে সেই প্রান্তে যে আধানের সমষ্টি হয় তাই বদ্ধ আধান।
আধানের নিত্যতা : আধানের সৃষ্টি বা বিনাশ নেই তা শুধু এক বস্তু থেকে অন্য বস্তুতে স্থানান্তরিত হয় এবং জগতের মোট আধান সর্বদা একই থাকে এটিই আধানের নিত্যতা।
চার্জের কোয়ান্টায়ন : পরমাণু তথা যেকোনো বস্তুর ন্যূনতম চার্জ ইলেকট্রনের চার্জের পূর্ণসংখ্যার গুণিতক হিসেবে চার্জিত হতে পারে এবং চার্জের মান কখনো ভগ্নাংশ হবে না। একে চার্জের কোয়ান্টায়ন বলে।
এক ইলেকট্রন ভোল্ট : ১ ভোল্ট বিভব পার্থক্যে কোনো ইলেকট্রনকে গতিশীল করতে সম্পন্ন কাজের পরিমাণকে এক ইলেকট্রন ভোল্ট (eV) বলা হয়।
পোলার ডাই ইলেকট্রিক : যেসব ডাই ইলেকট্রিক পদার্থের কোনো অণুর ঋনাত্মক আধানের কেন্দ্র ধনাত্মক আধানের কেন্দ্রের সাথে সমাপতিত হয় না সেই সকল ডাই ইলেকট্রিক পদার্থকে পোলার ডাই ইলেকট্রিক পদার্থ বলে।
পর্যবেক্ষণাত্মক দ্রবক : দুটি বিন্দু চার্জের মধ্যে নির্দিষ্ট দূরত্বের শূন্যস্থানে ক্রিয়াশীল বল ও ঐ দুই চার্জের মধ্যে একই দূরত্বে অন্য কোনো মাধ্যমে ক্রিয়াশীল বলের অনুপাতকে ঐ মাধ্যমের তড়িৎ মাধ্যমাক বা পর্যবেক্ষণাত্মক দ্রবক বলে।
আপেক্ষিক ভেদনযোগ্যতা : কোনো মাধ্যমের ভেদনযোগ্যতা ও শূন্য মাধ্যমের ভেদনযোগ্যতার অনুপাতই হলো আপেক্ষিক ভেদনযোগ্যতা।
অস্তরিত অপরিবাহী : তড়িৎ সংক্রান্ত কাজে যে সকল পদার্থ সংযোজক হিসেবে ব্যবহৃত হয় সেগুলোই অস্তরিত অপরিবাহী।
ভেদন যোগ্যতা : মাধ্যমের যে ধর্ম ঐ মাধ্যমে স্থাপিত দুটি চার্জের মধ্যে কুলম্ব বলকে প্রভাবিত করে তাকে ঐ মাধ্যমের ভেদন যোগ্যতা বলে।



\bigskip

\noindent \textbf{তড়িৎ মাধ্যম :} যে সমস্ত পদার্থের মধ্য দিয়ে চার্জ বা তড়িৎ প্রবাহিত হয় বা প্রবাহিত হতে চায়, তাদেরই তড়িৎ মাধ্যম বলে।

\noindent \textbf{অতি পরিবাহিতা :} অতি নিম্ন তাপমাত্রায় কিছু কিছু পদার্থের রোধ শূন্যে নেমে আসে। এসব পদার্থকে বলা হয় অতিপরিবাহী এবং পদার্থের এ ধর্মকে বলা হয় অতি পরিবাহিতা।

\noindent \textbf{দ্বিতড়িৎ ধ্রুবক :} একই দূরত্বে দুটি নির্দিষ্ট বিন্দু চার্জের মধ্যে শূন্য মাধ্যমে ক্রিয়াশীল তড়িৎ বল এবং কোনো দ্বিতড়িৎ মাধ্যমে ক্রিয়াশীল তড়িৎ বলের অনুপাতকে ঐ মাধ্যমের দ্বিতড়িৎ ধ্রুবক বলে।

\noindent \textbf{ধারক কাকে :} কাছাকাছি স্থাপিত দুটি পরিবাহীর মধ্যবর্তী স্থানে অন্তরক পদার্থ রেখে তড়িৎ আধানরূপে শক্তি সঞ্চয় করে রাখার যান্ত্রিক কৌশলকে ধারক বলে।

\noindent \textbf{ধারকের সমবায় :} একাধিক ধারককে একত্রে সংযুক্ত করে ব্যবহার করাকে ধারকের সমবায় বলে।

\noindent \textbf{ফ্যারাড :} কোনো ধারককে এক কুলম্ব চার্জ প্রদান করলে যদি এর বিভব এক ভোল্ট বৃদ্ধি পায় তবে উক্ত ধারকের ধারকত্বকে এক ফ্যারাড বা সংক্ষেপে ফ্যারাড বলে।

\noindent \textbf{তুল্য ধারকত্ব :} ধারকের সমবায়ের পরিবর্তে যে একটি মাত্র ধারক ব্যবহার করলে সমবায়ের বিভব পার্থক্য ও আধানের কোনো পরিবর্তন হয় না তার ধারকত্বকে সমবায়ের তুল্য ধারকত্ব বলে।

\noindent \textbf{গসিয়ান তল :} সুষমভাবে চার্জিত একটি গোলকের গোলকীয় তলের প্রত্যেক বিন্দুতে যদি তড়িৎপ্রাবল্য মানে সমান এবং লম্ব অভিমুখে ক্রিয়াশীল থাকে তবে এ প্রকারের গোলকীয় তলকে গাউসিয়ান তল বলে।

\noindent \textbf{তড়িৎ ফ্লাক্স :} কোনো তড়িৎক্ষেত্রের সাথে লম্বভাবে অবস্থিত বা কল্পিত কোনো তলের মধ্য দিয়ে অতিক্রান্ত মোট প্রবাহরেখা হলো তড়িৎ ফ্লাক্স।

\noindent \textbf{গসের সূত্র :} গসের সূত্রটি হলো— কোনো বদ্ধ তলের উপর স্থির তড়িৎ ক্ষেত্রের মোট অভিলম্ব আবেশ বা ফ্লাক্স ঐ তল দ্বারা বেষ্টিত মোট চার্জের $\frac{1}{\epsilon_0}$ গুণ।

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[\ding{226}] শূন্যস্থানে কুলম্ব ধ্রুবকের মান $9 \times 10^9$।
    \item[\ding{226}] এস. আই. পদ্ধতিতে আধানের একক কুলম্ব।
    \item[\ding{226}] বায়ুতে $5 \times 10^{-4}\text{ C}$ এবং $8 \times 10^{-4}\text{ C}$ মানের দুটি চার্জের মধ্যবর্তী দূরত্ব $2\text{ m}$ হলে, এদের মধ্যবর্তী ক্রিয়াশীল বল $900\text{ N}$।
    \item[\ding{226}] $- 1 \times 10^{-6}\text{ C}$ এবং $3 \times 10^{-6}\text{ C}$ চার্জদ্বয়কে পরস্পর হতে $15\text{ cm}$ দূরে রাখা হলে তাদের মধ্যে আকর্ষণ বলের মান $1.2\text{ N}$।
    \item[\ding{226}] $1\text{ \AA}$ দূরত্বে অবস্থিত দুটি ইলেকট্রনের মধ্যকার বলের মান $2.304 \times 10^{-8}$ নিউটন।
    \item[\ding{226}] শূন্য মাধ্যমে দুইটি ইলেকট্রনের মধ্যকার কুলম্ব বল এবং মহাকর্ষ বলের অনুপাত $4.2 \times 10^{42}$।
    \item[\ding{226}] একটি বস্তুর চার্জ $+ 5\text{ C}$ হলে এতে ইলেকট্রন সংখ্যা $3.125 \times 10^{19}$।
    \item[\ding{226}] কোনো একটি আহিত বস্তুর আধানের জন্য গ্রহণযোগ্য মান ইলেকট্রনিক আধানের গুণিতক হবে।
    \item[\ding{226}] $10\text{ C}$ বিন্দু আধান হতে শূন্য মাধ্যমে $1\text{ m}$ দূরত্বের বিন্দুতে বিভবের মান $9 \times 10^{10}\text{ V}$।
    \item[\ding{226}] $4$ পরা বৈদ্যুতিক ধ্রুবকের কোনো মাধ্যমে রক্ষিত $0.25\text{ C}$ আধান হতে $10\text{ m}$ দূরত্বের বিন্দুতে তড়িৎ বিভবের মান $5.625 \times 10^7\text{ V}$।
    \item[\ding{226}] $2.58 \times 10^{-10}\text{ C}$ এর পরখ আধানের ওপর $1.35\text{ N}$ বল প্রয়োগকারী তড়িৎ ক্ষেত্রের মান $5.23 \times 10^9\text{ N C}^{-1}$।
    \item[\ding{226}] ধনাত্মক আধানের আহিত একটি বস্তুকে ভূমির সাথে সংযুক্ত করলে নিষ্ক্রিয় হবে।
    \item[\ding{226}] কোনো নিঃসসঙ্গ চার্জ হতে $10\text{ cm}$ দূরে $100\text{ V}$ বিভব সৃষ্টি হলে ঐ চার্জটির পরিমাণ $1.1 \times 10^{-9}\text{ C}$।
    \item[\ding{226}] $2 \times 10^{-9}\text{ C}$ চার্জ থেকে $0.1\text{ m}$ দূরত্বে বৈদ্যুতিক প্রাবল্যের মান $1800\text{ N/C}$।
    \item[\ding{226}] একটি সুষম তড়িৎ ক্ষেত্রে $5\text{ cm}$ ব্যবধানে অবস্থিত দুটি বিন্দুর বিভব পার্থক্য $100\text{ V}$ হলে তড়িৎ ক্ষেত্রের প্রাবল্য $2000\text{ Vm}^{-1}$।
    \item[\ding{226}] $2\text{ eV}$ জুলের সমান $3.2 \times 10^{-19}\text{ J}$।
    \item[\ding{226}] $30$ ভোল্টের একটি ব্যাটারির এক প্রান্ত হতে অন্য প্রান্তে $60\text{ C}$ চার্জকে পরিবাহিত করতে $1800\text{ J}$ পরিমাণ কাজ করতে হয়।
    \item[\ding{226}] $100\text{ C}$ চার্জ হতে $3\text{ m}$ দূরে বৈদ্যুতিক প্রাবল্য $3 \times 10^{11}\text{ N C}^{-1}$।
    \item[\ding{226}] $r$ ব্যাসার্ধের গোলকীয় তলের কেন্দ্রে $8.854 \times 10^{-8}\text{ C}$ চার্জ রাখা হলে উক্ত তল থেকে নিঃসৃত তড়িৎ ফ্লাক্সের মান $10^4$।
    \item[\ding{226}] $2\sqrt{2}\text{ m}$ বাহুবিশিষ্ট একটি বর্গক্ষেত্রের চার কোণায় $2 \times 10^{-9}\text{ C}$ চার্জ থাকলে উহার কেন্দ্রে বিভব $36\text{ V}$।
    \item[\ding{226}] বায়ুতে $50\text{ C}$ চার্জ হতে $2\text{ m}$ দূরত্বে কোন বিন্দুতে তড়িৎ প্রাবল্যের মান $11.25 \times 10^{10}\text{ N C}^{-1}$।
\end{itemize}

\bigskip
\bigskip


\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] $6.2\text{ g}$ ভরের একটি অ্যালুমিনিয়াম মুদ্রায় মোট ধনাত্মক চার্জের পরিমাণ $2.879 \times 10^5\text{ C}$।
    \item[$\blacktriangleright$] $100\text{ C}$ চার্জ থেকে $0.5\text{ m}$ দূরে তড়িৎ বিভব $18 \times 10^{11}\text{ volt}$।
    \item[$\blacktriangleright$] তড়িৎ বলরেখা একটি সমবিভব তলকে লম্বভাবে ছেদ করে।
    \item[$\blacktriangleright$] ইলেকট্রন ও প্রোটনের মৌলিক ধর্ম আধান।
    \item[$\blacktriangleright$] $20^\circ\text{C}$ তাপমাত্রায় পানির পরাবৈদ্যুতিক ধ্রুবক $80.4$।
    \item[$\blacktriangleright$] পরিবাহীতে চার্জ সঞ্চিত রাখার যান্ত্রিক প্রক্রিয়ার নাম ধারক।
    \item[$\blacktriangleright$] এস আই পদ্ধতিতে ধারকত্বের একক ফ্যারাড।
    \item[$\blacktriangleright$] কোনো পরিবাহীর বিভব $1$ ভোল্ট বাড়াতে $1$ কুলম্ব চার্জের প্রয়োজন হলে ঐ পরিবাহীর ধারকত্বের মান $1\text{ F}$।
    \item[$\blacktriangleright$] $2.5\text{ }\mu\text{F}$ ধারকত্ব বিশিষ্ট একটি ধারককে $20\text{ V}$ ব্যাটারির সাথে সংযুক্ত করা হলে এতে $50 \times 10^{-6}\text{ C}$ পরিমাণ চার্জ সঞ্চিত হবে।
    \item[$\blacktriangleright$] পৃথিবীর ব্যাসার্ধ $6400\text{ km}$ হলে, পৃথিবীর ধারকত্ব $711\text{ }\mu\text{F}$।
    \item[$\blacktriangleright$] $2.5\text{ }\mu\text{F}$ ধারকত্ববিশিষ্ট একটি ধারককে $20\text{ V}$ ব্যাটারির সাথে যুক্ত করা হলে, এতে $50\text{ }\mu\text{C}$ চার্জ সংযুক্ত হবে।
    \item[$\blacktriangleright$] $5\text{ }\mu\text{F}$, $10\text{ }\mu\text{F}$ এবং $15\text{ }\mu\text{F}$ তিনটি ধারককে শ্রেণি সমবায়ে সংযুক্ত করলে তুল্যধারকত্ব $2.73\text{ }\mu\text{F}$ হবে।
    \item[$\blacktriangleright$] বায়ুতে $10.76\text{ m}$ দূরবর্তী $15\text{ m}^2$ ক্ষেত্রফলের পরিবাহীর ধারকত্ব $12.34\text{ pF}$।
    \item[$\blacktriangleright$] $6\text{ }\mu\text{F}$ একটি ধারককে $9.04\text{ V}$ ব্যাটারি দ্বারা চার্জিত করলে এতে $2.43 \times 10^{-4}\text{ J}$ পরিমাণ শক্তি সঞ্চিত হবে।
    \item[$\blacktriangleright$] শূন্য মাধ্যমে তড়িৎ ভেদনযোগ্যতা, $\epsilon_0 = 8.854 \times 10^{-12}\text{ C}^2\text{N}^{-1}\text{m}^{-2}$।
    \item[$\blacktriangleright$] একটি সমান্তরাল পাতধারকের ধারকত্ব বৃদ্ধি করতে হলে এর পাতদ্বয়কে সঠিকভাবে সমান্তরাল রাখতে হবে।
    \item[$\blacktriangleright$] একটি চার্জিত রিং এর কেন্দ্রে কোন চার্জ রাখলে ঐ চার্জের উপর নিট বল শূন্য হবে।
    \item[$\blacktriangleright$] একই দূরত্বে দুটি চার্জের মধ্যকার ক্রিয়াশীল বল নির্ভর করে চার্জ দুটির মানের উপর এবং মধ্যবর্তী মাধ্যমের উপর।
    \item[$\blacktriangleright$] ঘর্ষণের ফলে নতুন কোনো চার্জের উৎপত্তি হয় না, শুধু চার্জের আদান-প্রদান হয়।
    \item[$\blacktriangleright$] একটি চার্জিত গোলকের অভ্যন্তরে তড়িৎ প্রাবল্য শূন্য হবে।
    \item[$\blacktriangleright$] পরিবাহীর বক্র অংশে সঞ্চিত চার্জের পরিমাণ সবচেয়ে বেশি।
    \item[$\blacktriangleright$] তড়িৎ ক্ষেত্রে দূরত্বের সাপেক্ষে বিভবের অন্তরক সহগকে তড়িৎ প্রাবল্য বলে।
    \item[$\blacktriangleright$] একটি ইলেকট্রন বা প্রোটনের চার্জের পরিমাণ $1.6 \times 10^{-19}\text{ C}$।
    \item[$\blacktriangleright$] পরিবাহীতে চার্জ সঞ্চিত রাখার যান্ত্রিক প্রক্রিয়ার নাম ধারক। আবিষ্কারক ভ্যান মুসেন।
    \item[$\blacktriangleright$] সমান্তরাল পাত ধারকের পাতদ্বয়ের মধ্যবর্তী দূরত্ব বাড়ালে ধারকত্ব কমে যায়।
    \item[$\blacktriangleright$] সুষম তড়িৎ ক্ষেত্রে সর্বত্র প্রাবল্যের মান ও দিক অভিন্ন এবং তড়িৎ বলরেখা সমান্তরাল হয়।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $F = \text{বল}$ & নিউটন ($\text{N}$) \\ \cline{3-4} 
 & & $q_1 \text{ ও } q_2 = \text{বিন্দু আধান}$ & কুলম্ব ($\text{C}$) \\ \cline{3-4} 
\textbf{১.} & কুলম্ব বল : $F = \frac{1}{4\pi\epsilon_0} \cdot \frac{q_1q_2}{d^2}$ & $d = \text{আধানদ্বয়ের মধ্যবর্তী দূরত্ব}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & & $\frac{1}{4\pi\epsilon_0} = \text{ধ্রুব মান} = 9 \times 10^9$ & নিউটন মিটার$^2$/কুলম্ব$^2$ ($\text{Nm}^2\text{C}^{-2}$) \\ \hline
 & & $E = \text{তড়িৎ প্রাবল্য}$ & \begin{tabular}[c]{@{}l@{}}নিউটন/কুলম্ব ($\text{N/C}$)\\ বা ভোল্ট/মিটার ($\text{V/m}$)\end{tabular} \\ \cline{3-4} 
\textbf{২.} & তড়িৎ প্রাবল্য : $E = \frac{1}{4\pi\epsilon_0} \cdot \frac{q}{r^2}$ & $r = \text{দূরত্ব}$ & মিটার ($\text{m}$) \\ \hline
 & & $\sigma = \text{চার্জের তলমাত্রিক ঘনত্ব}$ & কুলম্ব/মিটার$^2$ ($\text{C/m}^2$) \\ \cline{3-4} 
 & চার্জের তলমাত্রিক ঘনত্ব : $\sigma = \frac{Q}{A} = \frac{Q}{4\pi r^2}$ & $A = \text{পরিবাহীর বহিঃপৃষ্ঠের ক্ষেত্রফল}$ & বর্গমিটার ($\text{m}^2$) \\ \cline{3-4} 
\textbf{৩.} & $\sigma_1 : \sigma_2 = r_2^2 : r_1^2$ ; যখন $Q_1 = Q_2$ & $4\pi r^2 = \text{গোলকের পৃষ্ঠের ক্ষেত্রফল}$ & বর্গমিটার ($\text{m}^2$) \\ \cline{3-4} 
 & $\frac{\sigma_1}{\sigma_2} = \frac{Q_1}{Q_2} \cdot \frac{r_2^2}{r_1^2}$ ; যখন $Q_1 \neq Q_2$ & $r = \text{গোলকের ব্যাসার্ধ}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & & $Q = \text{চার্জ}$ & কুলম্ব ($\text{C}$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip



\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $r = \text{দূরত্ব}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{৪.} & তড়িৎ বিভব : $V = \frac{1}{4\pi\epsilon_0} \cdot \frac{q}{r}$ & $V = \text{তড়িৎ বিভব}$ & ভোল্ট ($\text{V}$) \\ \cline{3-4} 
 & & $r = \text{পরিবাহী গোলকের ব্যাসার্ধ}$ & মিটার ($\text{m}$) \\ \hline
 & & $P = \text{দ্বিমেরু ভ্রামক}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & তড়িৎ দ্বিমেরুর লম্ব দ্বিখণ্ডকের উপর কোনো বিন্দুতে & $2l = \text{দ্বিমেরুর দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{৫.} & প্রাবল্য : $E = \frac{1}{4\pi\epsilon_0} \cdot \frac{P}{\left(r^2 + l^2\right)^{\frac{3}{2}}}$ & $E = \text{তড়িৎ প্রাবল্য}$ & \begin{tabular}[c]{@{}l@{}}নিউটন/কুলম্ব ($\text{N/C}$)\\ বা ভোল্ট/মিটার ($\text{V/m}$)\end{tabular} \\ \cline{3-4} 
 & & $r = \text{দূরত্ব}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৬.} & গোলাকার পরিবাহীর ধারকত্ব : $C = 4\pi\epsilon_0 r$ & $r = \text{গোলকের ব্যাসার্ধ}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & & $\epsilon_0 = \text{তড়িৎভেদ্যনযোগ্যতা}$ & \begin{tabular}[c]{@{}l@{}}কুলম্ব$^2$/নিউটন-মিটার$^2$\\ ($\text{C}^2\text{N}^{-1}\text{m}^{-2}$)\end{tabular} \\ \hline
 & সমান্তরাল পাত ধারকের ধারকত্ব : & $C = \text{ধারকত্ব}$ & ফ্যারাড ($\text{F}$) \\ \cline{3-4} 
 & (i) দুটি পাতের ক্ষেত্রে, $C = \frac{\epsilon_0 A}{d}$ & $A = \text{প্রত্যেক পাতের ক্ষেত্রফল}$ & মিটার$^2$ ($\text{m}^2$) \\ \cline{3-4} 
\textbf{৭.} & (ii) $n$-সংখ্যক পাতের ক্ষেত্রে, $C = \frac{(n-1)\epsilon_0 A}{d}$ & $d = \text{সমান্তরাল দুটি পাতের দূরত্ব}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & \phantom{(ii)} [প্রতিটি পাত পরস্পর থেকে $d$ দূরে অবস্থিত] & & \\
 & (iii) $t$ বেধযুক্ত $K$ পরাবৈদ্যুতিক মাধ্যমের ক্ষেত্রে দুটি & $k = \text{পরাবৈদ্যুতিক ধ্রুবক}$ & \\
 & সমান্তরাল পাত ধারকের ধারকত্ব : $C = \frac{\epsilon_0 A}{(d-t) + \frac{t}{K}}$ & & \\ \hline
\textbf{৮.} & \begin{tabular}[c]{@{}l@{}}সমান্তরাল সমবায়ের ক্ষেত্রে তুল্য ধারকত্ব :\\ $C_p = C_1 + C_2 + C_3 + .......... + C_n$\end{tabular} & \begin{tabular}[c]{@{}l@{}}$C_p = \text{সমান্তরাল সমবায়ে যুক্ত}$\\ \text{ধারকগুলোর ধারকত্ব}\end{tabular} & ফ্যারাডে ($\text{F}$) \\ \hline
\textbf{৯.} & \begin{tabular}[c]{@{}l@{}}শ্রেণি সমবায়ের ক্ষেত্রে তুল্য ধারকত্ব :\\ $\frac{1}{C_s} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + .......... + \frac{1}{C_n}$\end{tabular} & \begin{tabular}[c]{@{}l@{}}$C_s = \text{শ্রেণি সমবায়ে যুক্ত}$\\ \text{ধারকগুলোর ধারকত্ব}\end{tabular} & ফ্যারাডে ($\text{F}$) \\ \hline
 & & $C = \text{ধারকত্ব}$ & ফ্যারাডে ($\text{F}$) \\ \cline{3-4} 
\textbf{১০.} & ধারকে সঞ্চিত শক্তি : & $V = \text{বিভব পার্থক্য}$ & ভোল্ট ($\text{V}$) \\ \cline{3-4} 
 & $U = \frac{1}{2}CV^2 = \frac{1}{2}QV = \frac{1}{2}\frac{Q^2}{C}$ & $U = \text{সঞ্চিত শক্তি}$ & জুল ($\text{J}$) \\ \cline{3-4} 
 & & $Q = \text{আধান}$ & কুলম্ব ($\text{C}$) \\ \hline
 & ধারকের একক আয়তনে সঞ্চিত শক্তি : & $V = \text{তড়িৎ বিভব}$ & ভোল্ট ($\text{V}$) \\ \cline{3-4} 
\textbf{১১.} & $U = \frac{1}{2}K\epsilon_0 E^2$ , $E = \frac{V}{d}$ & & \\
 & ($\text{আয়তন} = Ad = \text{পাতের ক্ষেত্রফল} \times \text{পাতদ্বয়ের}$ & $d = \text{সমান্তরাল দুটি পাতের দূরত্ব}$ & মিটার ($\text{m}$) \\
 & $\text{মধ্যবর্তী দূরত্ব}$) & & \\ \hline
\textbf{১২.} & সমান্তরাল দুটি পাত ধারকের পাতদ্বয়ের মধ্যবর্তী & $F = \text{কুলম্ব বল}$ & নিউটন ($\text{N}$) \\ \cline{3-4} 
 & আকর্ষণ বল : $F = \frac{1}{2} \cdot \frac{Q^2}{\epsilon_0 KA}$ & $\epsilon_0 = \text{শূন্যস্থানের ভেদন যোগ্যতা}$ & \begin{tabular}[c]{@{}l@{}}ফ্যারাডে/মিটার ($\text{F/m}$) বা\\ কুলম্ব$^2$/নিউটন মিটার$^2$ ($\text{C}^2/\text{N-m}^2$)\end{tabular} \\ \hline
\end{tabular}
}

\bigskip
\bigskip


\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{অর্ধ পরিবাহী :} সাধারণ তাপমাত্রায় যে সকল পদার্থের যোজন ব্যান্ড প্রায় পূর্ণ এবং পরিবহন ব্যান্ড প্রায় খালি থাকে এবং এ দুটি ব্যান্ডের মধ্যে নিষিদ্ধ শক্তি ব্যবধান $2\text{ eV}$ এর চেয়ে কম থাকে তাদেরকে অর্ধপরিবাহী বলে।

\noindent \textbf{তাড়ন বেগ :} তাড়ন বেগ হলো কোনো কণা যেমন ইলেকট্রনের সেই বেগ যা সে তড়িৎক্ষেত্রের কারণে লাভ করে।

\noindent \textbf{ওহমের সূত্র :} ও'মের সূত্রটি হলো— তাপমাত্রা স্থির থাকলে কোনো পরিবাহীর মধ্যদিয়ে যে পরিমাণ তড়িৎ প্রবাহিত হয়, তা সেই পরিবাহীর দুই প্রান্তের বিভব পার্থক্যের সমানুপাতিক।

\noindent \textbf{এক অ্যাম্পিয়ার প্রবাহ :} শূন্য মাধ্যমে $1\text{ m}$ দূরত্বে অবস্থিত অসীম দৈর্ঘ্যের এবং উপেক্ষণীয় প্রস্থচ্ছেদের দুটি সমান্তরাল সরল পরিবাহীর প্রত্যেকটিতে যে পরিমাণ প্রবাহ চললে পরস্পরের মধ্যে প্রতি মিটার দৈর্ঘ্যে $2 \times 10^{-7}\text{ N}$ বল উৎপন্ন হয় তাই এক অ্যাম্পিয়ার।

\noindent \textbf{আপেক্ষিক রোধ :} একক দৈর্ঘ্য ও একক প্রস্থচ্ছেদের ক্ষেত্রফল বিশিষ্ট কোনো পরিবাহীর রোধকে আপেক্ষিক রোধ বলে।

\noindent \textbf{অতি পরিবাহিতা :} অতি নিম্ন তাপমাত্রায় কিছু কিছু পদার্থের রোধ শূন্যে নেমে আসে। এসব পদার্থকে বলা হয় অতিপরিবাহী এবং পদার্থের এ ধর্মকে বলা হয় অতি পরিবাহিতা।

\noindent \textbf{প্রবাহ ঘনত্ব :} কোনো পরিবাহকের প্রতি একক প্রস্থচ্ছেদের ক্ষেত্রফলের মধ্য দিয়ে প্রবাহিত প্রবাহকে প্রবাহ ঘনত্ব বলে।

\noindent \textbf{অ্যাম্পিয়ারের সূত্র :} অ্যাম্পিয়ারের সূত্রটি হলো— কোনো তড়িৎবাহী পরিবাহীকে কেন্দ্র করে কাল্পনিক কোনো বদ্ধ রেখা বা লুপের ওপর $\vec{B} \cdot d\vec{l}$ এর রৈখিক যোগজীকরণ ঐ পরিবাহীতে প্রবাহিত তড়িৎ প্রবাহমাত্রা $i$ এবং $\mu_0$ এর গুণফল সমান।

\noindent \textbf{রোধের উষ্ণতা গুণাঙ্ক :} প্রতি কেলভিন তাপমাত্রা বৃদ্ধিতে একক রোধ বিশিষ্ট কোনো পরিবাহীর রোধের যে বৃদ্ধি ঘটে তাকে ঐ পরিবাহীর রোধের উষ্ণতা গুণাঙ্ক বলে।

\noindent \textbf{রোধ :} পরিবাহীর যে ধর্মের জন্য এর মধ্যদিয়ে তড়িৎ প্রবাহ বাধাগ্রস্ত হয় তাকে ঐ পরিবাহীর রোধ বলে।

\noindent \textbf{রোধের দৈর্ঘ্যের সূত্র :} রোধের দৈর্ঘ্যের সূত্রটি হলো নির্দিষ্ট তাপমাত্রায় নির্দিষ্ট উপাদানের পরিবাহকের প্রস্থচ্ছেদের ক্ষেত্রফল স্থির থাকলে পরিবাহকের রোধ দৈর্ঘ্যের সমানুপাতিক পরিবর্তিত হয়।

\noindent \textbf{ওহম মিটার :} যে যন্ত্রের সাহায্যে রোধ নির্ণয় করা হয়, তাকে ওহম মিটার বলে।

\noindent \textbf{রোধাঙ্ক :} কোনো নির্দিষ্ট তাপমাত্রার একক দৈর্ঘ্যের ও একক প্রস্থচ্ছেদের ক্ষেত্রফলের কোনো পরিবাহীর রোধকে বা একক বাহুবিশিষ্ট কোনো ঘনকের রোধকে ঐ তাপমাত্রায় ঐ পরিবাহীর উপাদানের আপেক্ষিক রোধ বা রোধাঙ্ক বলে।

\noindent \textbf{১ ওহম রোধ :} যে পরিবাহকের দুই প্রান্তের বিভব পার্থক্য এক ভোল্ট হলে তার মধ্য দিয়ে $1$ অ্যাম্পিয়ার তড়িৎ প্রবাহ চলে সেই পরিবাহকের রোধকে এক ওহম বলে।

\noindent \textbf{স্লাইডিং রোধ :} বিভব বিভাজকে $R_1$ ও $R_2$ এর পরিবর্তে এমন রোধ যুক্ত করা যায় যার মান পরিবর্তন করে $V_1$ এর মান শূন্য থেকে $V_2$ পর্যন্ত পাওয়া সম্ভব। একে স্লাইডিং রোধ বলে।

\noindent \textbf{মুক্ত ইলেকট্রন :} পরমাণুর সর্ববহিঃস্থ শক্তিস্তরের ইলেকট্রনের সাথে নিউক্লিয়াসের আকর্ষণ বল অনেক কম থাকে বলে এর ইলেকট্রন সহজেই পরমাণু থেকে মুক্ত হয়ে তড়িৎ পরিবহনে অংশ নেয়। এদের মুক্ত ইলেকট্রন বলে।

\noindent \textbf{জুলের প্রথম সূত্র :} জুলের প্রথম সূত্রটি হলো— বিদ্যুৎবাহী পরিবাহী রোধ $R$ এবং বিদ্যুৎ প্রবাহকাল $t$ অপরিবর্তিত থাকলে পরিবাহীতে বিদ্যুৎ প্রবাহের দরুন উদ্ভূত তাপ প্রবাহমাত্রার বর্গের সমানুপাতিক।

\noindent \textbf{তাপ উৎপাদন সম্পর্কিত জুলের দ্বিতীয় সূত্র :} তাপ উৎপাদন সম্পর্কিত জুলের দ্বিতীয় সূত্রটি হলো— বিদ্যুৎবাহী পরিবাহীর রোধ এবং বিদ্যুৎ প্রবাহমাত্রা অপরিবর্তিত থাকলে পরিবাহীতে বিদ্যুৎ প্রবাহের দরুন উদ্ভূত তাপ প্রবাহকালের সমানুপাতিক।

\noindent \textbf{জুলের রোধের সূত্র :} জুলের রোধের সূত্রটি হলো— তড়িৎ প্রবাহমাত্রা এবং তড়িৎ প্রবাহকাল অপরিবর্তিত থাকলে পরিবাহীতে তড়িৎ প্রবাহের দরুন উদ্ভূত তাপ পরিবাহীর রোধের সমানুপাতিক।

\noindent \textbf{B.O.T. unit :} এক কিলোওয়াট ক্ষমতা সম্পন্ন কোনো যন্ত্র এক ঘণ্টা ধরে যে বৈদ্যুতিক শক্তি ব্যয় করে তাকে কিলোওয়াট ঘণ্টা বা $1\text{ B.O.T unit}$ বলে।

\noindent \textbf{কিলোওয়াট ঘণ্টা :} এক কিলোওয়াট ক্ষমতা সম্পন্ন কোনো যন্ত্র এক ঘণ্টা কাজ করলে যে শক্তি ব্যয় হয়, তাই কিলোওয়াট-ঘণ্টা।

\noindent \textbf{বর্তনী :} তড়িৎ প্রবাহ চলার সম্পূর্ণ পথকে তড়িৎ বর্তনী বলে।

\bigskip
\bigskip


\bigskip

\noindent \textbf{চৌম্বক প্রাবল্য বা চৌম্বক তীব্রতা :} শূন্যস্থানে বায়ু মাধ্যমে কোনো চৌম্বক ক্ষেত্রে একক ক্ষেত্রফলের মধ্য দিয়ে অতিক্রান্ত চৌম্বক বলরেখার সংখ্যা বা ফ্লাক্সকে চৌম্বক ক্ষেত্রের প্রাবল্য বা তীব্রতা বলে।

\noindent \textbf{চুম্বকায়ন বা চুম্বকায়ন তীব্রতা :} কোনো চৌম্বক পদার্থের প্রতি একক আয়তনের চৌম্বক ভ্রামককে চুম্বকায়ন বলে।

\noindent \textbf{চৌম্বক সম্পৃক্তি :} চুম্বকায়নের পর চৌম্বক পদার্থ যে নির্দিষ্ট সীমার উপরে তার চুম্বকত্ব প্রাপ্ত হয় না তাকে চৌম্বক সম্পৃক্তি বলে।

\noindent \textbf{চৌম্বক প্রবেশ্যতা :} কোনো চৌম্বক ক্ষেত্রে স্থাপিত চৌম্বক পদার্থের উপর চৌম্বক আবেশ ও চৌম্বক প্রাবল্যের অনুপাতকে চৌম্বক প্রবেশ্যতা বলে।

\noindent \textbf{চৌম্বক প্রবণতা বা চৌম্বক গ্রাহিতা :} কোনো চৌম্বক পদার্থকে কত সহজে চুম্বকিত করা যায় তা যে ধর্মের দ্বারা নির্ণীত হয় তাকে পদার্থটির চৌম্বক প্রবণতা বলা হয়।

\noindent \textbf{কুরীবিন্দু (Curie Point) :} যে তাপমাত্রায় কোনো একটি চুম্বকের চুম্বকত্ব সম্পূর্ণরূপে লোপ পায়, তাকে উক্ত চুম্বকের উপাদানের কুরীবিন্দু বলে।

\noindent \textbf{চৌম্বক ধারকত্ব বা ধারণ ক্ষমতা :} চুম্বকনকারী বল সরিয়ে নিলেও চৌম্বক পদার্থের চুম্বকত্ব ধরে রাখার যে ক্ষমতা থাকে, তাকে চৌম্বক ধারকত্ব বলে।

\noindent \textbf{চৌম্বক নিগ্রাহিতা বা সহনশীলতা :} চুম্বকত্ব হ্রাসের কারণগুলো উপস্থিত থাকা সত্ত্বেও পদার্থের চুম্বকত্ব ধরে রাখার ক্ষমতাকে চৌম্বক সহনশীলতা বলে।

\noindent \textbf{প্যাারাচৌম্বক পদার্থ :} যেসব পদার্থকে চৌম্বক ক্ষেত্রে স্থাপন করলে, চুম্বকনকারী ক্ষেত্রের দিকে দুর্বল চৌম্বকত্ব লাভ করে সেসব পদার্থকে প্যারাচৌম্বক পদার্থ বলে।

\noindent \textbf{ডায়াচৌম্বক পদার্থ :} যেসব পদার্থকে চৌম্বক ক্ষেত্রে স্থাপন করা হলে চুম্বকনকারী ক্ষেত্রের বিপরীত দিকে সামান্য চুম্বকত্ব লাভ করে তাদেরকে ডায়াচৌম্বক পদার্থ বলে।

\noindent \textbf{ফেরোচৌম্বক পদার্থ :} যেসব পদার্থকে চৌম্বক ক্ষেত্রে স্থাপন করা হলে চুম্বকনকারী ক্ষেত্রের দিকে শক্তিশালী চুম্বকত্ব লাভ করে তাদেরকে ফেরোচৌম্বক পদার্থ বলে।

\noindent \textbf{তড়িৎচুম্বক :} একটি দীর্ঘ অন্তরীত পরিবাহী তারকে যদি একটি কুপরিবাহী লম্বা চোঙের গায়ে এমনভাবে জড়ানো হয়, যাতে প্রতিটি বৃত্তাকার পাকই চোঙের অক্ষের সাথে লম্বভাবে থাকে, তবে ঐ তারের কুণ্ডলীকে সলিনয়েড বলে।

\noindent \textbf{স্থায়ী চুম্বক :} কোনো চুম্বক পদার্থকে চুম্বকে পরিণত করার পর চুম্বকত্ব প্রদানকারী শক্তিকে অপসারণ করলেও যদি চুম্বকত্ব অনেকদিন স্থায়ী হয়, তবে ঐ চুম্বককে স্থায়ী চুম্বক বলে।

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] শূন্য মাধ্যমে চৌম্বক প্রবেশ্যতার মান $4\pi \times 10^{-7}\text{ TmA}^{-1}$।
    \item[$\blacktriangleright$] চৌম্বক ক্ষেত্র $\text{B}$ এর মানের একক, $\text{Tesla}$, $\text{Weber m}^{-2}$, $\text{NA}^{-1}\text{m}^{-1}$।
    \item[$\blacktriangleright$] চৌম্বক ফ্লাক্সের একক ওয়েবার ($\text{Wb}$)। চৌম্বক ফ্লাক্স ঘনত্বের একক $\text{Wb m}^{-2} = \text{T}$।
    \item[$\blacktriangleright$] ওয়েরস্টেড তড়িৎ প্রবাহের চৌম্বক ক্রিয়া আবিষ্কার করেন।
    \item[$\blacktriangleright$] আদিতে ব্যবহৃত চৌম্বক প্রাবল্যের একক $1\text{ Gauss} = 10^{-4}\text{ Tesla}$, $1\text{ Oersted} = 10^{-4}\text{ T}$।
    \item[$\blacktriangleright$] চৌম্বক পদার্থের প্রতি একক আয়তনে চৌম্বক ভ্রামককে চুম্বকায়ন তীব্রতা বলে।
    \item[$\blacktriangleright$] অ্যাম্পিয়ারের সূত্রানুযায়ী, $\oint \vec{B} \cdot d\vec{l} = \mu_0 \text{I}$।
    \item[$\blacktriangleright$] চার্জের গতিশীলতায় সৃষ্টি হয় তড়িৎ প্রবাহ ও চৌম্বক ক্ষেত্র।
    \item[$\blacktriangleright$] চৌম্বক ক্ষেত্রে গতিশীল একটি চার্জের উপর ক্রিয়াশীল বল, $\vec{F} = q\left(\vec{v} \times \vec{B}\right)$।
    \item[$\blacktriangleright$] হল ক্রিয়ার সাহায্যে নির্ণয় করা যায় প্রবাহ সৃষ্টিকারী চার্জের প্রকৃতি।
    \item[$\blacktriangleright$] চৌম্বক ভ্রামক $\vec{M}$ এবং চৌম্বক ক্ষেত্র $\vec{B}$ হলে টর্ক, $\vec{\tau} = \vec{M} \times \vec{B}$।
    \item[$\blacktriangleright$] লুপের ক্ষেত্রফল যত বেশি হবে চৌম্বক ভ্রামক তত বেশি হবে।
\end{itemize}

\bigskip
\bigskip



\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] ইলেকট্রনের ঘূর্ণনের দিক তড়িৎ প্রবাহের বিপরীত দিকে।
    \item[$\blacktriangleright$] স্পিনের মান দুই ধরনের হতে পারে। যথা, স্পিনের সঠিক মান $+\frac{1}{2}$ অথবা $-\frac{1}{2}$।
    \item[$\blacktriangleright$] বিনতি, বিচ্যুতি এবং ভূ-চৌম্বক ক্ষেত্রের অনুভূমিক উপাংশ হলো পৃথিবীর ভূ-চুম্বকত্বের উপাদান।
    \item[$\blacktriangleright$] ঢাকার বিনতি $31^\circ\text{ N}$।
    \item[$\blacktriangleright$] বিষুবরেখার বিনতির মান $0^\circ$।
    \item[$\blacktriangleright$] বিনতির সর্বোচ্চ ও সর্বনিম্ন মান $90^\circ$ ও $0^\circ$।
    \item[$\blacktriangleright$] প্যারাচৌম্বক পদার্থের ক্ষেত্রে $\mu > 1$ ও $\text{k} < 1$ হবে।
    \item[$\blacktriangleright$] ডায়াচৌম্বক পদার্থের চৌম্বক প্রবেশ্যতার মান $\mu < 1$।
    \item[$\blacktriangleright$] ডায়াচৌম্বক ও প্যারাচৌম্বক পদার্থে কুরী বিন্দু পাওয়া যায় না।
    \item[$\blacktriangleright$] পানি, পারদ, সোনা, তামা, কাচ ইত্যাদি ডায়াচৌম্বক পদার্থ।
    \item[$\blacktriangleright$] নিকেল ফেরাইট, ফেরোসোফেরিক অক্সাইড ($\text{Fe}_3\text{O}_4$) একটি ফেরিচৌম্বক পদার্থ।
    \item[$\blacktriangleright$] হিসটেরেসিসের ফলে শক্তির অপচয় ঘটে ও বস্তুর তাপমাত্রা বৃদ্ধি পায়।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $\text{I} = \text{তড়িৎ প্রবাহ}$ & অ্যাম্পিয়ার ($\text{A}$) \\ \cline{3-4} 
\textbf{১.} & বায়ো-স্যাভার্ট সূত্র : $\text{dB} = \frac{\mu_0}{4\pi}\frac{\text{Id}l \sin\theta}{\text{r}^2}$ & $\text{B} = \text{চৌম্বক ক্ষেত্র}$ & টেসলা ($\text{T}$) \\ \cline{3-4} 
 & & $l = \text{তারের দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
\textbf{২.} & ঋজু তারের ক্ষেত্রে, $\text{B} = \frac{\mu_0\text{I}}{2\pi\text{a}}$ & $\text{a} = \text{লম্ব দূরত্ব}$ & মিটার ($\text{m}$) \\ \hline
 & & $\text{N} = \text{পাকসংখ্যা}$ & ঘূর্ণন/সে. \\ \cline{3-4} 
\textbf{৩.} & বৃত্তাকার কুণ্ডলীর তারের ক্ষেত্রে, $\text{B} = \frac{\mu_0\text{I}}{2\text{r}}\text{N}$ & $\text{r} = \text{ব্যাসার্ধ}$ & মিটার ($\text{m}$) \\ \hline
 & & $\text{F} = \text{চৌম্বক বল}$ & নিউটন \\ \cline{3-4} 
 & চৌম্বক বল, $\text{F} = \text{qvB} \sin\theta$ & $\text{q} = \text{আধান}$ & কুলম্ব ($\text{C}$) \\ \cline{3-4} 
\textbf{৪.} & \phantom{চৌম্বক বল, }$\text{F} = \text{qvB}$, যখন, $\theta = 90^\circ$ & $\text{v} = \text{ইলেকট্রনের বেগ}$ & মি./সে. ($\text{m s}^{-1}$) \\ \cline{3-4} 
 & & $\text{B} = \text{চৌম্বক ক্ষেত্র}$ & টেসলা ($\text{T}$) \\ \hline
 & & $l = \text{তারের দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{৫.} & তড়িৎবাহী তারে ক্রিয়াশীল বল, $\text{F} = \text{IlB} \sin\theta$ & \begin{tabular}[c]{@{}l@{}}$\theta = \text{পরিবাহীর}$\\ $\text{মধ্যবিন্দুতে সৃষ্ট কোণ}$\end{tabular} & ডিগ্রি ($^\circ$) \\ \hline
 & & $\text{d} = \text{পরিবাহকের প্রস্থ}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{৬.} & দুটি সমমুখী সমান্তরাল তারের একক দৈর্ঘ্যে ক্রিয়াশীল বল, $\text{F} = \frac{\mu_0\text{I}_1\text{I}_2}{2\pi\text{d}}$ & $\text{I}_1, \text{I}_2 = \text{তড়িৎপ্রবাহ}$ & অ্যাম্পিয়ার ($\text{A}$) \\ \hline
 & & $\text{V}_\text{H} = \text{হল বিভব}$ & ভোল্ট ($\text{V}$) \\ \cline{3-4} 
\textbf{৭.} & হল বিভব, $\text{V}_\text{H} = \text{vBd}$ & $\text{v} = \text{চার্জের বেগ}$ & মি./সে. ($\text{m s}^{-1}$) \\ \hline
 & & $\tau = \text{টর্ক}$ & নিউটন-মি. ($\text{N-m}$) \\ \cline{3-4} 
\textbf{৮.} & টর্ক, $\tau = \text{NIAB} \sin\theta$ & $\text{A} = \text{বর্তনীর ক্ষেত্রফল}$ & মিটার$^2$ ($\text{m}^2$) \\ \cline{3-4} 
 & & $\text{B} = \text{চৌম্বক ফ্লাক্স ঘনত্ব}$ & টেসলা ($\text{T}$) \\ \hline
 & চৌম্বক ক্ষেত্রে অনুভূমিক ও উলম্ব উপাংশ, & $\text{H} = \text{অনুভূমিক উপাংশ}$ & টেসলা ($\text{T}$) \\ \cline{3-4} 
\textbf{৯.} & $\text{H} = \text{B} \cos\delta$, \qquad $\text{V} = \text{B} \sin\delta$, & $\text{V} = \text{উলম্ব উপাংশ}$ & টেসলা ($\text{T}$) \\ \cline{3-4} 
 & $\text{V} = \text{H} \tan\delta$, \qquad $\text{V}^2 + \text{H}^2 = \text{B}^2$ & $\delta = \text{বিনতি কোণ}$ & ডিগ্রি ($^\circ$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip


\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{তড়িৎ চৌম্বকীয় আবেশ :} একটি গতিশীল চুম্বক বা একটি গতিশীল তড়িৎবাহী কুণ্ডলীর সাহায্যে অন্য একটি বদ্ধ বর্তনীতে ক্ষণস্থায়ী তড়িৎচালক বল তথা তড়িৎ প্রবাহ উৎপন্ন হওয়ার পদ্ধতি হলো তড়িৎ চৌম্বকীয় আবেশ।

\noindent \textbf{চৌম্বক ফ্লাক্স :} কোনো তলের ক্ষেত্রফল এবং ঐ তলের লম্ব বরাবর চৌম্বক ক্ষেত্রের উপাংশের গুণফলকে ঐ তলের সাথে সংশ্লিষ্ট চৌম্বক ফ্লাক্স বলে।

\noindent \textbf{ওয়েবার :} ওয়েবার হচ্ছে চৌম্বক ফ্লাক্সের একক। এক পাকের একটি কুণ্ডলীর সাথে সংশ্লিষ্ট যে পরিমাণ চৌম্বক ফ্লাক্স এক সেকেন্ডে সুষমভাবে হ্রাস পেয়ে শূন্যতে নেমে আসলে ঐ কুণ্ডলী এক ভোল্ট তড়িৎচালক বল আবিষ্ট হয়, সে পরিমাণ চৌম্বক ফ্লাক্সই এক ওয়েবার বা সংক্ষেপে শুধু ওয়েবার।

\noindent \textbf{ফ্লাক্স ঘনত্ব :} কোনো বিন্দুর চারপাশে একক ক্ষেত্রফল দিয়ে অতিক্রমকারী চৌম্বক ফ্লাক্সকে ঐ বিন্দুতে ঐ তলের লম্ব বরাবর ফ্লাক্স ঘনত্ব বলে।

\noindent \textbf{আবিষ্ট তড়িৎচালক বল :} কোনো বদ্ধ বর্তনীতে তড়িৎ চৌম্বকীয় আবেশে সৃষ্ট ক্ষণস্থায়ী তড়িৎচালক শক্তিই আবিষ্ট তড়িৎচালক শক্তি।

\noindent \textbf{লেঞ্জ-এর সূত্র :} লেঞ্জ-এর সূত্রটি হলো— যেকোনো তড়িৎচৌম্বক আবেশের বেলায় আবিষ্ট তড়িৎচালক শক্তি বা প্রবাহের দিক এমন হয় যে তা সৃষ্টি হওয়া মাত্রই যে কারণে সৃষ্টি হয় সেই কারণকেই বাধা দেয়।

\noindent \textbf{স্বকীয় আবেশ গুণাঙ্ক :} কোনো কুণ্ডলীতে একক তড়িৎ প্রবাহিত হলে কুণ্ডলীতে সংযুক্ত মোট চৌম্বক ফ্লাক্সকে ঐ কুণ্ডলীর স্বকীয় আবেশ গুণাঙ্ক বলে।

\noindent \textbf{পারস্পরিক আবেশ গুণাঙ্ক :} কোনো মুখ্য কুণ্ডলীতে তড়িৎপ্রবাহ একক হারে পরিবর্তিত হলে গৌণ কুণ্ডলীতে যে আবিষ্ট তড়িৎচালক শক্তি উৎপন্ন হয় তাকে পারস্পরিক আবেশ গুণাঙ্ক বলে।

\noindent \textbf{স্বকীয় আবেশ :} একটি মাত্র বদ্ধ কুণ্ডলীতে অসম তড়িৎ প্রবাহের দরুন চৌম্বক ফ্লাক্সের পরিবর্তনের ফলে অথবা কোনো চৌম্বক ক্ষেত্রে বদ্ধ কুণ্ডলীর গতির ফলে যে তড়িৎ চৌম্বক আবেশ ঘটে, তাই স্বকীয় আবেশ।

\noindent \textbf{পারস্পরিক আবেশ :} পাশাপাশি অবস্থিত দুটি কুণ্ডলীর যেকোনো একটিতে তড়িৎ প্রবাহের পরিবর্তন ঘটলে অপরটিতে তড়িৎচালক বল আবিষ্ট হয়। এ ঘটনা পারস্পরিক আবেশ বলে।

\noindent \textbf{হেনরি :} কোনো কুণ্ডলীতে তড়িৎ প্রবাহ প্রতি সেকেন্ডে এক অ্যাম্পিয়ার হারে পরিবর্তিত হলে যদি ঐ কুণ্ডলীতে এক ভোল্ট তড়িৎচালক বল আবিষ্ট হয়, তাহলে ঐ কুণ্ডলীর স্বকীয় আবেশ গুণাঙ্ককে এক হেনরি বলে।

\noindent \textbf{আবেশহীন কুণ্ডলী :} যে কুণ্ডলীর মধ্যে তড়িৎ প্রবাহ পরিবর্তন করা হলে তাতে তড়িৎচালক বল আবিষ্ট হয় না তাকে আবেশহীন কুণ্ডলী বলে।

\noindent \textbf{একমুখী প্রবাহ :} সময়ের সাথে যে প্রবাহের দিক অপরিবর্তিত থাকে তাই একমুখী প্রবাহ।

\noindent \textbf{দিক পরিবর্তী প্রবাহ :} যে প্রবাহের দিক বা অভিমুখ একটি নির্দিষ্ট সময় অন্তর অন্তর সুষমভাবে পরিবর্তিত হতে থাকে, তাকে দিক পরিবর্তী প্রবাহ বলে।

\noindent \textbf{মুখ্য ও গৌণ কুণ্ডলী :} তড়িৎবাহী কুণ্ডলীকে মুখ্য কুণ্ডলী এবং যে তারের কুণ্ডলীতে আবিষ্ট তড়িৎ প্রবাহ উৎপন্ন হয় তাকে গৌণ কুণ্ডলী বলে।

\noindent \textbf{একমুখী প্রবাহ ডায়নামো :} যে ডায়নামোর সাহায্যে একমুখী তড়িৎ প্রবাহ পাওয়া যায় তাকে একমুখী প্রবাহ ডায়নামো বলে।

\noindent \textbf{মোটর :} যে যন্ত্রের সাহায্যে তড়িৎ শক্তিকে যান্ত্রিক শক্তিতে রূপান্তর করে তাকে মোটর বলা হয়।

\noindent \textbf{বৈদ্যুতিক যন্ত্রপাতি :} তড়িৎবিজ্ঞানে আমরা যেসব যন্ত্রপাতি ব্যবহার করি, তাদের বৈদ্যুতিক যন্ত্রপাতি বলে।

\noindent \textbf{ডায়নামো :} যে যন্ত্র যান্ত্রিক শক্তিকে তড়িৎ শক্তিতে রূপান্তর করে তাকে জেনারেটর বা ডায়নামো বলে।

\noindent \textbf{ট্রান্সফরমার :} যে যন্ত্রের সাহায্যে পরিবর্তী বিভবকে অপেক্ষাকৃত উচ্চ বা নিম্ন বিভবে পরিণত করা যায় তাকে রূপান্তরক বা ট্রান্সফরমার বলে।

\noindent \textbf{শীর্ষ গুণাঙ্ক :} প্রবাহের শীর্ষমান এবং বর্গমূল গড় বর্গমানের অনুপাতই শীর্ষ গুণাঙ্ক।

\noindent \textbf{প্রবাহের কম্পাঙ্ক :} পরিবর্তী তড়িৎচালক শক্তি বা প্রবাহ প্রতি সেকেন্ডে যত সংখ্যক পরিবর্তী চক্র সম্পন্ন করে, তাকে উক্ত তড়িৎচালক বল বা প্রবাহের কম্পাঙ্ক বলে।

\noindent \textbf{বিস্তার :} যেকোনো অভিমুখে তড়িৎচালক শক্তি বা প্রবাহের সর্বোচ্চ মানকে বিস্তার বা শীর্ষমান বলে।

\noindent \textbf{কার্যকর প্রবাহ :} পরিবাহী প্রবাহের গড়বর্গের বর্গমূল মানকে কার্যকর প্রবাহ বলে।

\noindent \textbf{আকৃতি গুণাঙ্ক :} দিক পরিবর্তী তড়িৎচালক শক্তি বা প্রবাহমাত্রার গড় বর্গের বর্গমূল মান এবং গড় মানের অনুপাতকে আকৃতি গুণাঙ্ক বলে।

\bigskip
\bigskip



\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] চৌম্বক আবেশ চৌম্বক ফ্লাক্স ঘনত্ব।
    \item[$\blacktriangleright$] তাড়িতচৌম্বকীয় আবেশ আবিষ্কার করেন মাইকেল ফ্যারাডে।
    \item[$\blacktriangleright$] তড়িৎ প্রবাহ দুই প্রকার।
    \item[$\blacktriangleright$] $10\text{A}$ বিদ্যুৎ প্রবাহিত একটি লম্বা সোজা তার থেকে $0.05\text{ m}$ দূরে চৌম্বক ফ্লাক্স ঘনত্ব $4 \times 10^{-4}\text{ T}$।
    \item[$\blacktriangleright$] $4 \times 10^{-5}\text{ T}$ এর চৌম্বক ক্ষেত্রের সাথে $0.4\text{ m}^2$ ক্ষেত্রের একটি তল $30^\circ$ কোণ উৎপন্ন করে। তলের মধ্য দিয়ে অতিক্রান্ত ফ্লাক্সের পরিমাণ $8 \times 10^{-6}\text{ Wb}$।
    \item[$\blacktriangleright$] $\text{B}$ চৌম্বক ক্ষেত্রে $\text{A}$ ক্ষেত্রফলের কোনো কুণ্ডলী অবস্থিত হলে চৌম্বক ফ্লাক্স $\phi = \text{B.A} \cos \theta$।
    \item[$\blacktriangleright$] মাইকেল ফ্যারাডে 1831 সালে তাড়িতচৌম্বকীয় আবেশ আবিষ্কার করেন।
    \item[$\blacktriangleright$] ফ্যারাডের দ্বিতীয় সূত্রের গাণিতিক রূপ দেন নিউম্যান।
    \item[$\blacktriangleright$] ফ্যারাডে তড়িৎ চৌম্বকীয় আবেশের দুটি সূত্র আবিষ্কার করেছেন।
    \item[$\blacktriangleright$] যে যন্ত্রের সাহায্যে বিভব পার্থক্যের মান পরিবর্তন করা যায় তাকে ট্রান্সফরমার বলে।
    \item[$\blacktriangleright$] কোনো তড়িৎকোষবিহীন কুণ্ডলীর দিকে একটি দণ্ডচুম্বক সরাতে যদি $5\text{ J}$ কাজ করতে হয় তাহলে এতে $5\text{ J}$ পরিমাণ তড়িৎ শক্তি উৎপন্ন হয়।
    \item[$\blacktriangleright$] কোন কুণ্ডলীতে $0.5\text{ A/s}$ হারে প্রবাহমাত্রার পরিবর্তনের দ্বারা যদি $1$ ভোল্ট তড়িৎচালক বল আবিষ্ট হয় তাহলে ঐ কুণ্ডলীর স্বাবেশ গুণাঙ্ক $2\text{ H}$।
    \item[$\blacktriangleright$] $\text{N}$ পাক সংখ্যার কুণ্ডলীর প্রতি পাকের সাথে জড়িত ফ্লাক্স সংশ্লেষ $\phi$ হলে কুণ্ডলীর মোট ফ্লাক্সের পরিমাণ $\text{N}\phi$।
    \item[$\blacktriangleright$] পারস্পরিক আবেশ গুণাঙ্কের একক হেনরী।
    \item[$\blacktriangleright$] একটা কুণ্ডলীতে তড়িৎ প্রবাহের পরিবর্তনের হার $30\text{ A.s}^{-1}$ হলে $8\text{V}$ তড়িৎচালক বল আবিষ্ট হয়। কুণ্ডলীর স্বকীয় আবেশ গুণাঙ্ক $267\text{ mH}$।
    \item[$\blacktriangleright$] কোন মুখ্য কুণ্ডলীতে $0.05\text{ s}$ এ তড়িৎ প্রবাহমাত্রা $6\text{ A}$ থেকে $1\text{ A}$ এ আনলে গৌণ কুণ্ডলীতে $5\text{ V}$ তড়িৎচালক শক্তি আবিষ্ট হয়। কুণ্ডলীর পারস্পরিক আবেশ গুণাঙ্ক $0.05\text{ H}$।
    \item[$\blacktriangleright$] $0.02\text{ m}$ ব্যাসার্ধের এবং $10$ পাকের একটি গোলাকার কুণ্ডলীর বায়ু মাধ্যমে স্বাবেশ গুণাঙ্কের মান $3.94\text{ }\mu\text{H}$।
    \item[$\blacktriangleright$] ঘূর্ণায়মান কোনো বস্তুর কম্পাঙ্ক $20\text{ Hz}$ হলে এর কৌণিক কম্পাঙ্ক $125\text{ rad s}^{-1}$।
    \item[$\blacktriangleright$] কোনো কুণ্ডলী পূর্ণ একবার ঘুরলে $\theta$ এর মান $0^\circ$ থেকে $360^\circ$ হয়।
    \item[$\blacktriangleright$] একটি ট্রান্সফরমার মুখ্য কুণ্ডলীর পাক সংখ্যা $30$, ভোল্টেজ $210\text{ V}$, এর গৌণ কুণ্ডলীর ভোল্টেজ $700\text{ V}$ হলে, পাকসংখ্যা $100$।
    \item[$\blacktriangleright$] একটি দিক পরিবর্তী প্রবাহ $\text{I} = 50 \sin 200\pi\text{t}$, শীর্ষমানে পৌঁছাতে $2.5 \times 10^{-3}\text{ s}$ সময় লাগবে।
    \item[$\blacktriangleright$] যে যন্ত্রের সাহায্যে যান্ত্রিক শক্তিকে পরিবর্তী তড়িৎ শক্তিতে পরিণত করা যায় তাকে জেনারেটর বলে।
    \item[$\blacktriangleright$] বাংলাদেশে যে দিক পরিবর্তী বিদ্যুৎ সরবরাহ করা হয় তার কম্পাঙ্ক $50\text{ Hz}$।
    \item[$\blacktriangleright$] তড়িৎ প্রবাহের শীর্ষমান $7\text{ A}$ হলে মূল গড় বর্গ প্রবাহের মান $4.95\text{ A}$।
    \item[$\blacktriangleright$] দিক পরিবর্তী প্রবাহের বর্গমূলীয় গড় মান শীর্ষমানের শতকরা $70.70\%$ ভাগ।
    \item[$\blacktriangleright$] কোনো দিক পরিবর্তী তড়িৎচালক বলের গড় বর্গমূল মান $20\text{ volt}$ হলে শীর্ষমান $28.2\text{ volt}$।
    \item[$\blacktriangleright$] কোনো বিশুদ্ধ রোধ $\text{R}$ এর মধ্যে দিয়ে $\text{I}$ মানের সমপ্রবাহ চললে প্রতি সেকেন্ডে তাপ উৎপাদনের হার $\text{I}^2\text{R}$।
    \item[$\blacktriangleright$] পূর্ণ চক্রের জন্য দিক পরিবর্তী প্রবাহের গড় বর্গের বর্গমূল মানের সমীকরণ $\text{I}_{\text{rms}} = 0.707\text{ I}_0$।
    \item[$\blacktriangleright$] কোন পর্যায়বৃত্ত তড়িৎচালক বলের শীর্ষমান $30\text{ V}$ হলে এর গড় তড়িৎচালক বলের মান $19.11\text{ V}$।
    \item[$\blacktriangleright$] সাইন সদৃশ কোন তরঙ্গের শীর্ষমান ও গড় বর্গের বর্গমূলের অনুপাত $1.41$।
    \item[$\blacktriangleright$] কোনো পরিবর্তী উৎসের তড়িৎচালক শক্তির সর্বোচ্চ মান $100\text{ V}$ হলে কার্যকর মান $70.7\text{ V}$।
    \item[$\blacktriangleright$] কোন দিক পরিবর্তিত তড়িৎচালক শক্তির শীর্ষ মান $20\text{ V}$ হলে তার গড় বর্গের বর্গমূলের মান $14.14\text{ V}$।
    \item[$\blacktriangleright$] অর্ধচক্রের জন্য প্রবাহের গড় মান $1.6\text{ A}$ হলে শীর্ষ মান $2.512\text{ A}$।
    \item[$\blacktriangleright$] কোনো পর্যায়বৃত্ত তড়িৎচালক বলের শীর্ষমান $20\text{V}$ হলে এর গড় তড়িৎচালক বল $12.74\text{ V}$।
    \item[$\blacktriangleright$] মাইকেল ফ্যারাডে 1831 সালে তড়িৎ চৌম্বকীয় আবেশ আবিষ্কার করেন।
\end{itemize}

\bigskip
\bigskip


\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{ফার্মাটের নীতি :} ফার্মাটের নীতিটি হলো— একটি নির্দিষ্ট বিন্দু হতে অপর একটি নির্দিষ্ট বিন্দুতে পরিভ্রমণকালে আলোক রশ্মি এমন একটি পথ অনুসরণ করে যা অতিক্রমণীয় সময় নিকটবর্তী অন্যান্য পথের তুলনায় হয় সর্বনিম্ন বা অবম নতুবা সর্বোচ্চ বা চরম অথবা অপরিবর্তিত তথা স্থির থাকে।

\noindent \textbf{আলোক পথ :} কোনো মাধ্যমে একটি নির্দিষ্ট জ্যামিতিক পথ অতিক্রম করতে আলোকের যে সময় লাগে ঠিক সেই সময়ে শূন্য বা বায়ু মাধ্যমের মধ্যদিয়ে আলোক যে পরিমাণ পথ অতিক্রম করতে পারে সে পথকে আলোক পথ বলে।

\noindent \textbf{আলোর প্রতিসরণ :} আলোকরশ্মি একস্বচ্ছ মাধ্যম থেকে অন্য স্বচ্ছ মাধ্যমে গমনের সময় মাধ্যমদ্বয়ের বিভেদতলে তীর্যকভাবে আপতিত হলে আপতিত রশ্মির দিক পরিবর্তন হয়। আলোকরশ্মির এ দিক পরিবর্তন হওয়াকে আলোর প্রতিসরণ বলে।

\noindent \textbf{দ্বি-প্রতিসরণ :} এমন কতগুলো কেলাস আছে যাদের মধ্যদিয়ে আলোক রশ্মি গমন করলে এটি দুটি প্রতিসৃত রশ্মিতে বিভক্ত হয়। এ পদ্ধতিকে দ্বৈত বা দ্বি-প্রতিসরণ বলে।

\noindent \textbf{লেন্স :} দুটি গোলীয় অথবা একটি গোলীয় ও একটি সমতল অথবা দুটি বেলনাকৃতি অথবা একটি বেলনাকৃতি ও একটি সমতল পৃষ্ঠ দ্বারা সীমাবদ্ধ কোনো স্বচ্ছ প্রতিসারক মাধ্যমকে লেন্স বলে।

\noindent \textbf{উন্মেষ :} লেন্সের প্রধান ছেদের প্রান্তদ্বয় বক্রতার কেন্দ্রে যে কোণ সৃষ্টি করে তাকে লেন্সের উন্মেষ বলে।

\noindent \textbf{লেন্সের বক্রতার কেন্দ্র :} লেন্সের কোনো পৃষ্ঠ যে গোলকের অংশ সেই গোলকের কেন্দ্রকে লেন্সের ঐ পৃষ্ঠের বক্রতার কেন্দ্র বলে।

\noindent \textbf{ফোকাস তল :} কোনো লেন্সের প্রধান ফোকাসের মধ্য দিয়ে প্রধান অক্ষের উপর যে সমতল কল্পনা করা যায় তাকে ফোকাস তল বলে।

\noindent \textbf{বক্রতার ব্যাসার্ধ :} লেন্সের কোনো পৃষ্ঠ যে গোলকের অংশ সেই গোলকের ব্যাসার্ধকে লেন্সের ঐ পৃষ্ঠের বক্রতার ব্যাসার্ধ বলে। লেন্সে দুটি বক্রতার ব্যাসার্ধ থাকে। এদেরকে $r_1$ এবং $r_2$ দ্বারা সূচিত করা হয়।

\noindent \textbf{প্রধান ফোকাস :} গোলীয় দর্পণে আপতিত প্রধান অক্ষের নিকটবর্তী সমান্তরাল রশ্মিগুচ্ছ প্রতিফলনের পর প্রধান অক্ষের উপর যে বিন্দুতে মিলিত হয় বা যে বিন্দু থেকে অপসৃত হয় বলে মনে হয় তাকে প্রধান ফোকাস বলে।

\noindent \textbf{ফোকাস দূরত্ব :} আলোক কেন্দ্র থেকে প্রধান ফোকাস বা দ্বিতীয় প্রধান ফোকাস পর্যন্ত দূরত্বই হলো ফোকাস দূরত্ব।

\noindent \textbf{লেন্সের ক্ষমতা :} লেন্সের ক্ষমতা বলতে একটি লেন্স আপতিত আলোক রশ্মিকে কতখানি অভিসারিত বা অপসারিত করতে পারে তাকে বোঝায়। অর্থাৎ কোন লেন্সের ফোকাস দূরত্বের বিপরীত সংখ্যাকে লেন্সের ক্ষমতা বলে।

\noindent \textbf{অবতল দর্পণ :} কোনো গোলকের অবতল পৃষ্ঠ যদি প্রতিফলকরূপে কাজ করে অর্থাৎ আলোর নিয়মিত প্রতিফলন যদি গোলীয় দর্পণের অবতল পৃষ্ঠ হতে সংঘটিত হয় তবে সে দর্পণকে অবতল দর্পণ বলে।

\noindent \textbf{সমতল দর্পণ :} কোনো সমতল পৃষ্ঠ যদি মসৃণ হয় এবং তাতে আলোর নিয়মিত প্রতিফলন ঘটে তবে তাকে সমতল দর্পণ বলে।

\noindent \textbf{কৌণিক বিবর্ধন :} বিম্ব দ্বারা সৃষ্ট দৃষ্টিকোণ ও বস্তু দ্বারা সৃষ্ট দৃষ্টিকোণের অনুপাতই কৌণিক বিবর্ধন।

\noindent \textbf{বিবর্ধন :} প্রতিবিম্বের দৈর্ঘ্য এবং লক্ষ্যবস্তুর দৈর্ঘ্যের অনুপাতকে রৈখিক বিবর্ধন বা বিবর্ধন বলে। আবার, প্রতিবিম্বের দূরত্ব এবং লক্ষ্যবস্তুর দূরত্বের অনুপাতকেও বিবর্ধন বলে।

\noindent \textbf{বিবর্ধক :} বিবর্ধক বা অ্যাম্প্লিফায়ার এক ধরনের ইলেকট্রনিক ডিভাইস বা কৌশল যার ইনপুট বর্তনীতে দুর্বল সংকেত প্রয়োগ করে বহিঃবর্তনী হতে বহুগুণ বিবর্ধিত সংকেত পাওয়া যায়।

\noindent \textbf{ডায়াপ্টার :} ডায়াপ্টার হলো লেন্সের ক্ষমতার একক।

\noindent \textbf{অণুবীক্ষণ যন্ত্র :} যে যন্ত্রের সাহায্যে চোখের নিকটবর্তী অতিক্ষুদ্র বস্তুকে বড় করে দেখা যায় তা হলো অণুবীক্ষণ যন্ত্র।

\noindent \textbf{দেহ নল :} অণুবীক্ষণ যন্ত্রের বাহুর সাথে একটি ফাঁপা নল লাগানো থাকে, এ ফাঁপা নলটিই হলো দেহ নল।

\noindent \textbf{নোজ পিস বা লেন্স ধারক :} দেহ নলের নিচের প্রান্তে একটি ধাতব চাক্তি সংযুক্ত থাকে যা নোজ পিস বা লেন্স ধারক নামে পরিচিত।

\noindent \textbf{দূরবীক্ষণ যন্ত্র :} দূরের বস্তুকে ভালোভাবে পর্যবেক্ষণের জন্য যে আলোক যন্ত্র ব্যবহৃত হয়, তাকে দূরবীক্ষণ যন্ত্র বলে।

\noindent \textbf{দৃষ্টিকোণ :} একটি বস্তু চোখে যে কোণ উৎপন্ন করে তাকে দৃষ্টিকোণ বা বীক্ষণ কোণ বলে।

\noindent \textbf{অভিনেত্র :} অণুবীক্ষণ বা দূরবীক্ষণ যন্ত্রের যে লেন্সটির পশ্চাতে বা পেছনে চোখ রাখতে হয় সেই লেন্সই অভিনেত্ৰ।

\noindent \textbf{অভিলক্ষ্য :} অণুবীক্ষণ বা দূরবীক্ষণ যন্ত্রের ক্ষেত্রে লক্ষ্যবস্তুর দিকে যে লেন্সটি থাকে তাকে অভিলক্ষ্য বলা হয়।

\noindent \textbf{প্রিজম কোণ :} প্রতিসারক তলদ্বয় যে কোণে পরস্পরকে ছেদ করে তাকে প্রিজম কোণ বলে।

\noindent \textbf{বর্ণালি :} সাদা আলোক রশ্মি বিচ্ছুরণের ফলে পর্দার উপর বিভিন্ন রঙের যে পট্টি পাওয়া যায় তাই বর্ণালি।

\bigskip
\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] শূন্য মাধ্যমে আলোর বেগ $3 \times 10^8\text{ ms}^{-1}$।
    \item[$\blacktriangleright$] ফার্মাটের নীতির প্রস্তাবনা করেন পিয়ারে ফার্মাট।
    \item[$\blacktriangleright$] একটি পুকুরের আপাত গভীরতা $12\text{ ফুট}$। পানির প্রতিসরাঙ্ক $\frac{4}{3}$ হলে পুকুরের প্রকৃত গভীরতা $16\text{ ফুট}$।
    \item[$\blacktriangleright$] আলোকরশ্মি বায়ু থেকে কাচে $60^\circ$ কোণে আপতিত হলে $35.26^\circ$ কোণে প্রতিসৃত হবে।
    \item[$\blacktriangleright$] একটি জলাশয়ের প্রকৃত গভীরতা $6\text{ m}$। পানির প্রতিসরাঙ্ক $\frac{4}{3}$ হলে আপাত গভীরতা $4.5\text{ m}$।
    \item[$\blacktriangleright$] এক টুকরা প্লাস্টিকের মধ্যে আলোর গতিবেগ $2 \times 10^8\text{ m/s}$ হলে plastic-এর পরম প্রতিসরাঙ্ক $1.5$।
    \item[$\blacktriangleright$] বায়ু থেকে কোন মাধ্যমে আলোকরশ্মি প্রবেশের পর আলোর বেগ $15\%$ হ্রাস পেলে মাধ্যমের প্রতিসরাঙ্ক $1.18$।
    \item[$\blacktriangleright$] লক্ষ্যবস্তু প্রধান ও বক্রতার কেন্দ্রের মধ্যে থাকলে বিম্ব অসীমে গঠিত হয়।
    \item[$\blacktriangleright$] একটি উভোত্তল লেন্সের বক্রতার ব্যাসার্ধ যথাক্রমে $30\text{ cm}$ এবং $20\text{ cm}$ হলে ফোকাস দূরত্ব $-23.1\text{ cm}$।
    \item[$\blacktriangleright$] $4\text{ D}$ ক্ষমতার একটি কাচ লেন্স এর পৃষ্ঠ পানিতে ডুবালে লেন্সটির ফোকাস দূরত্ব $25\text{ cm}$।
    \item[$\blacktriangleright$] লেন্সের দুটি প্রধান ফোকাস থাকে।
    \item[$\blacktriangleright$] $10\text{ cm}$ ফোকাস দূরত্বের অবতল লেন্সের ক্ষমতা $-10\text{ d}$।
    \item[$\blacktriangleright$] একটি উত্তল লেন্সের ক্ষমতা $\frac{1}{\text{x}}$ ডায়োপ্টার হলে, তার ফোকাস দূরত্ব $\text{x m}$।
    \item[$\blacktriangleright$] $1.6$ প্রতিসরাঙ্কের সমতল উত্তল লেন্সের বক্রতার ব্যাসার্ধ $60\text{ cm}$ হলে এর ক্ষমতা $2\text{ D}$।
    \item[$\blacktriangleright$] $\text{f}$ ফোকাস দূরত্বের দুটি সম উত্তল ও অবতল লেন্সের সংযোগের জন্য ফোকাস দূরত্ব $\infty$ হবে।
    \item[$\blacktriangleright$] $25\text{ cm}$ ফোকাস দূরত্বের একটি অবতল লেন্সের ক্ষমতা $\frac{1}{\text{F}_1} = -\sum \frac{1}{\text{f}_1}$।
    \item[$\blacktriangleright$] একটি বিবর্ধক কাচের ফোকাস দূরত্ব $0.15\text{ m}$, চোখ ও কাচের মধ্যবর্তী দূরত্ব $0.10\text{ m}$ হলে বিবর্ধন $2.0$।
    \item[$\blacktriangleright$] একটি জটিল অণুবীক্ষণ যন্ত্রের অভিলক্ষ্য ও অভিনেত্রের বিবর্ধন যথাক্রমে $54$ ও $9$ হলে যন্ত্রের মোট বিবর্ধন $486$।
    \item[$\blacktriangleright$] দূরবীক্ষণ যন্ত্র সাধারণতঃ দুই ধরনের।
    \item[$\blacktriangleright$] নভোদূরবীক্ষণ যন্ত্রের অভিনেত্রের লেন্স ছোট এবং খাটো দিয়ে তৈরি।
    \item[$\blacktriangleright$] একটি নভোদূরবীক্ষণ যন্ত্রের লেন্স দুটির ক্ষমতা $0.5\text{ D}$ এবং $20\text{ D}$। যন্ত্রটির বিবর্ধন ক্ষমতা $40$।
    \item[$\blacktriangleright$] একটি নভো দূরবীক্ষণ যন্ত্রের বিবর্ধন ক্ষমতা $20$ এবং দৈর্ঘ্য $16\text{ cm}$ হলে অভিলক্ষ্য লেন্সের ফোকাস দূরত্ব $15.24\text{ cm}$।
    \item[$\blacktriangleright$] $85^\circ$ প্রিজম কোণবিশিষ্ট একটি প্রিজমের ন্যূনতম চ্যুতিও $38^\circ$ হলে প্রতিসরাঙ্ক $1.535$।
    \item[$\blacktriangleright$] $1.6$ প্রতিসরাঙ্কবিশিষ্ট সরু প্রিজমের ভেতর দিয়ে যাওয়ার সময় আলোকরশ্মির $6^\circ$ চ্যুতি ঘটলে প্রিজম কোণ $10^\circ$ হবে?
    \item[$\blacktriangleright$] যে মাধ্যমে আলোর বিচ্ছুরণ ঘটে তাকে বিচ্ছুরক মাধ্যম বলে।
    \item[$\blacktriangleright$] লাল আলোর চেয়ে বেগুনী আলোর ক্ষেত্রে চ্যুতি $1.8$ গুণ বেশি।
    \item[$\blacktriangleright$] পাতলা প্রিজমের ক্ষেত্রে চ্যুতি কোণ, $\delta = \text{A}(\mu - 1)$ হবে।
    \item[$\blacktriangleright$] গ্যালিলিও সরল অণুবীক্ষণ যন্ত্র আবিষ্কার করেন।
    \item[$\blacktriangleright$] জটিল অণুবীক্ষণ যন্ত্রে চূড়ান্ত বিম্ব অবাস্তব ও উল্টো হয়।
    \item[$\blacktriangleright$] ফার্মাটের নীতির সাহায্যে আলোর সরল রৈখিক গতি, প্রতিফলন ও প্রতিসরণ-এর সূত্র ব্যাখ্যা করা যায়।
    \item[$\blacktriangleright$] প্রিজমের ক্ষেত্রে, আপতিত রশ্মি ও নির্গত রশ্মির অন্তর্ভূক্ত কোণকে চ্যুতি কোণ বলে।
    \item[$\blacktriangleright$] জটিল অণুবীক্ষণ যন্ত্রে দুটি উত্তল লেন্স থাকে।
    \item[$\blacktriangleright$] উত্তল লেন্সের ক্ষেত্রে যখন $\text{u} > \text{f}$ তখন প্রতিবিম্ব বাস্তব আবার যখন $\text{u} < \text{f}$ তখন প্রতিবিম্ব অবাস্তব হবে।
    \item[$\blacktriangleright$] প্রতিসরাঙ্ক মাধ্যমের প্রকৃতি ও আলোর রঙের উপর নির্ভর করে।
    \item[$\blacktriangleright$] যদি $\text{a}$ মাধ্যমে আলোর বেগ $\text{b}$ মাধ্যমে আলোর বেগের চেয়ে বেশি হয়, তবে $_a\mu_b > 1$ হবে।
    \item[$\blacktriangleright$] আলোকীয় পথ $(\text{L}_0) = \text{মাধ্যমের প্রতিসরাঙ্ক } (\mu) \times \text{জ্যামিতিক পথ } (\text{l})$।
    \item[$\blacktriangleright$] শূন্য মাধ্যমে আলোর বেগ সবচেয়ে বেশি।
    \item[$\blacktriangleright$] $_a\mu_b = 1$ হলে আলোকরশ্মির দিক অপরিবর্তিত থাকে।
    \item[$\blacktriangleright$] আলোক রশ্মি বেগুনী আলোর দিকে বেশি চ্যুতি হয়।
    \item[$\blacktriangleright$] উত্তল লেন্স লক্ষ্যবস্তু $\text{f}$ দূরত্বে থাকলে বিম্বের আকৃতি অত্যন্ত বিবর্ধিত হবে।
\end{itemize}

\bigskip
\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{তড়িৎ চৌম্বকীয় তরঙ্গ :} তড়িৎ চৌম্বকীয় তরঙ্গ হলো শূন্যস্থান দিয়ে আলোর দ্রুতিতে গতিশীল তড়িৎ ও চৌম্বক আলোড়ন, যাতে তড়িৎ ও চৌম্বক ক্ষেত্র পরস্পর লম্ব এবং এরা উভয়ে তরঙ্গ সঞ্চালনের অভিমুখের সাথে লম্ব বরাবর থাকে।

\noindent \textbf{আলোক বর্ষ :} আলোকবর্ষ হচ্ছে দূরত্বের একক। আলো শূন্যস্থানে এক বছরে যে পথ অতিক্রম করে তাই আলোকবর্ষ।

\noindent \textbf{অগ্রগামী তরঙ্গ :} যদি কোনো তরঙ্গ সময়ের সাথে সাথে নির্দিষ্ট দিকে নির্দিষ্ট বেগে চলমান থাকে তাকে অগ্রগামী তরঙ্গ বলে।

\noindent \textbf{পয়েন্টিং ভেক্টর :} কোনো তড়িৎ চৌম্বক তরঙ্গের গতি পথে লম্বভাবে স্থাপিত কোনো একক ক্ষেত্রফলের মধ্য দিয়ে যে পরিমাণ শক্তি অতিক্রম করে তাকে পয়েন্টিং ভেক্টর বলে।

\noindent \textbf{তড়িৎ চৌম্বকীয় বর্ণালি :} তড়িৎ চৌম্বক ক্ষেত্রের পূর্ণাঙ্গ পরিবর্তনের ফলে সৃষ্ট তড়িৎ চৌম্বকীয় বিকিরণ যে বর্ণালি সৃষ্টি করে তাকে তড়িৎ চৌম্বকীয় বর্ণালি বলা হয়।

\noindent \textbf{সৌর বর্ণালি :} সূর্য থেকে আগত আলোকে বিশ্লেষণ করা হলে যে বর্ণালি পাওয়া যায় তাকে সৌর বর্ণালি বলে।

\noindent \textbf{তরঙ্গ মুখ :} কোনো তরঙ্গের উপর অবস্থিত সমদশা সম্পন্ন কণাগুলোর সঞ্চারপথকে তরঙ্গমুখ বলে।

\noindent \textbf{আলোর তরঙ্গ মুখ :} কোনো আলোক তরঙ্গের উপর অবস্থিত সমদশা সম্পন্ন কণাগুলোর সঞ্চারপথকে উক্ত আলোক তরঙ্গের তরঙ্গমুখ বলে।

\noindent \textbf{আলোর ব্যতিচার :} দুটি সুসংগত উৎস হতে নিঃসৃত সমান কম্পাঙ্ক ও বিস্তারের দুটি আলোক তরঙ্গ কোনো মাধ্যমের একটি বিন্দুর মধ্য দিয়ে একই সাথে গমন করলে তরঙ্গ দুটির উপরিপাতনের ফলে বিন্দুটি কখনও কখনও খুব উজ্জ্বল ও কখনও কখনও অন্ধকার দেখায়। আলোকের এ ঘটনাই আলোর ব্যতিচার।

\noindent \textbf{গঠনমূলক ব্যতিচার :} দুটি উৎস হতে সমান কম্পাঙ্ক ও বিস্তারের দুটি আলোক তরঙ্গের উপরিপাতনের ফলে উজ্জ্বল বিন্দু পাওয়া গেলে তাকে গঠনমূলক ব্যতিচার বলে।

\noindent \textbf{ধ্বংসাত্মক ব্যতিচার :} দুটি উৎস হতে সমান কম্পাঙ্ক ও বিস্তারের দুটি আলোক তরঙ্গের উপরিপাতনের ফলে অন্ধকার বিন্দু পাওয়া গেলে তাকে ধ্বংসাত্মক ব্যতিচার বলে।

\noindent \textbf{গৌণ উৎস :} কোনো তরঙ্গমুখের প্রতিটি বিন্দু এক একটি গৌণ তরঙ্গের উৎস হিসেবে গণ্য হয়, এটিই গৌণ উৎস।

\noindent \textbf{গোলকীয় তরঙ্গমুখ :} তরঙ্গস্থিত সমদশাসম্পন্ন কণাগুলোর সঞ্চারপথ গোলকীয় হলে তাকে গোলকীয় তরঙ্গমুখ বলে।

\noindent \textbf{অপবর্তন :} কোনো প্রতিবন্ধকের ধার ঘেঁষে বা সরু ছিদ্রের মধ্য দিয়ে যাওয়ার সময় আলো কিছুটা বেঁকে যাওয়ার ঘটনাই অপবর্তন।

\noindent \textbf{অপবর্তন গ্রেটিং :} পাশাপাশি স্থাপিত অনেকগুলো সমপ্রস্থের ও সম দূরত্বের সমান্তরাল সরু চিরের সমষ্টিকে অপবর্তন গ্রেটিং বলে।

\noindent \textbf{গ্রেটিং ধ্রুবক :} গ্রেটিং এর একটি চিরের শুরু থেকে পরবর্তী চিরের শুরু পর্যন্ত দূরত্বকে গ্রেটিং ধ্রুবক বলে।

\noindent \textbf{ফ্রেনেল শ্রেণির অপবর্তন :} যখন উৎস এবং পর্দা তাদের মধ্যবর্তী বাধা হতে অল্প দূরত্বের মধ্যে অবস্থান করে তখন ঐ বাধার দরুন পর্দায় আলোকের যে অপবর্তন পরিলক্ষিত হয় তাকে ফ্রেনেল শ্রেণির অপবর্তন বলে।

\noindent \textbf{আলোর সমবর্তন :} যে প্রক্রিয়ায় বিভিন্ন তলে কম্পনমান আলোকে একটি নির্দিষ্ট তল বরাবর কম্পনমান করা যায় সেই প্রক্রিয়াই হলো আলোর সমবর্তন।

\noindent \textbf{সমবর্তন কোণ :} কোনো প্রতিফলক মাধ্যমে আপতন কোণ ধীরে ধীরে পরিবর্তন করলে এমন একটি কোণ পাওয়া যাবে যার জন্য সমবর্তন সর্বাধিক হবে, সেই কোণটিকে সমবর্তন কোণ বলে।

\noindent \textbf{সমবর্তিত আলো :} একটি তলে বা এর সমান্তরাল তলে কম্পনমান নির্দিষ্ট তরঙ্গদৈর্ঘ্যবিশিষ্ট আলোককে সমবর্তিত আলো বলে।

\noindent \textbf{সমবর্তন তল :} কম্পন তলের সাথে যে তলটি লম্বভাবে অবস্থান করে তাই সমবর্তন তল।

\noindent \textbf{আলোর দ্বি-প্রতিসরণ :} যেসব কেলাসের মধ্য দিয়ে আলোর রশ্মি গমন করলে আলো দুটি প্রতিসৃত রশ্মিতে বিভক্ত হয় যে ঘটনাকে দ্বি-প্রতিসরণ বলে।

\noindent \textbf{চির :} দৈর্ঘ্যের তুলনায় প্রস্থ অনেক ছোট এমন আয়তাকার সরু ছিদ্র পথকে চির বলে।

\noindent \textbf{ম্যালাসের সূত্র :} বিশ্লেষকের মধ্য দিয়ে সমবর্তিত আলো গমনের ফলে এর তীব্রতা সমবর্তক ও বিশ্লেষকের নিঃসরণ তলের মধ্যবর্তী কোণের $\text{cosine}$-এর বর্গের সমানুপাতিক।

\bigskip
\bigskip



\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] একটি তরঙ্গের দুটি বিন্দুর মধ্যে দশা পার্থক্য $90^\circ$ বা $\frac{\pi}{2}$ হলে পথ পার্থক্য $\frac{\lambda}{4}$ হবে।
    \item[$\blacktriangleright$] ব্যতিচারের ক্ষেত্রে ডোরার প্রস্থ তরঙ্গদৈর্ঘ্যের সমানুপাতিক।
    \item[$\blacktriangleright$] ম্যাগনেট্রন বাল্ব একটি মাইক্রোওয়েভ তরঙ্গ নিঃসরণকারী উৎস।
    \item[$\blacktriangleright$] পথ পার্থক্য $\text{x}$ এবং দশা পার্থক্য $\phi$ এর মধ্যে সম্পর্ক হলো, $\frac{\text{x}}{\lambda} = \frac{\phi}{2\pi}$।
    \item[$\blacktriangleright$] দ্বি-চির থেকে পর্দার দূরত্ব বৃদ্ধি করলে ডোরাপ্রস্থ বৃদ্ধি পায়।
    \item[$\blacktriangleright$] মাইক্রোওয়েভ ওয়্যারলেসে, রান্নাতে রান্নার জন্য ও রাডারে ব্যবহৃত হয়।
    \item[$\blacktriangleright$] আলোর ব্যতিচারের শর্ত (i) আলোক উৎস দুটি সুসংগত হতে হবে, (ii) উৎস দুটি ক্ষুদ্র, সূক্ষ্ম ও কাছাকাছি হতে হবে।
    \item[$\blacktriangleright$] 1801 সালে টমাস ইয়ং দ্বি-চির পরীক্ষার মাধ্যমে আলোর ব্যতিচার প্রদর্শন করেন।
    \item[$\blacktriangleright$] প্রিজমে আলোর বিচ্ছুরণের ক্ষেত্রে বেগুনী বর্ণের রশ্মির বিচ্যুতি বেশি এবং লাল বর্ণের বিচ্যুতি কম কিন্তু গ্রেটিংয়ের ক্ষেত্রে বেগুনী বর্ণের রশ্মির বিচ্যুতি কম এবং লাল বর্ণের বিচ্যুতি বেশি।
    \item[$\blacktriangleright$] সূর্যরশ্মির দৃষ্টিগোচরের সাতটি বর্ণের আলোর সজ্জাকে সৌর বর্ণালি বলে।
    \item[$\blacktriangleright$] আলোর প্রতিফলন, প্রতিসরণ, ব্যতিচার আলোর তরঙ্গ তত্ত্বের সাহায্যে ব্যাখ্যা করা যায়।
    \item[$\blacktriangleright$] আলো এক প্রকার তড়িৎ চুম্বকীয় তরঙ্গ (আড়তরঙ্গ)।
    \item[$\blacktriangleright$] দ্বি-চির পরীক্ষায় চিরগুলোর দূরত্ব অর্ধেক এবং চির ও পর্দার দূরত্ব দ্বিগুণ করা হলে ডোরা প্রস্থ চারগুণ হবে।
    \item[$\blacktriangleright$] ফ্রনহফার শ্রেণির অপবর্তন সৃষ্টি করা যায় গ্রেটিং দ্বারা, একক চির দ্বারা, যুগ্ম চির দ্বারা।
    \item[$\blacktriangleright$] বস্তু তরঙ্গ দ্বারা কণার দ্বৈত আচরণ ব্যাখ্যা করা যায়।
    \item[$\blacktriangleright$] সৌর বর্ণালীর তরঙ্গ দৈর্ঘ্যের সীমা $4000\text{ }\text{Å} - 7000\text{ }\text{Å}$।
    \item[$\blacktriangleright$] মানুষের শরীরে ভিটামিন $\text{D}$ তৈরির কাজে অতিবেগুনি রশ্মি ব্যবহৃত হয়।
\end{itemize}

\bigskip

\noindent \textbf{{\footnotesize [\textit{চিত্র}]} প্রতীক ও এককসহ গুরুত্বপূর্ণ सूत्रাবলি | Important Formulas with Symbols \& Units} \hfill {\footnotesize [\textit{চিত্র}]}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $\text{E}_0, \text{E} = \text{তড়িৎক্ষেত্র}$ & ভোল্ট/মিটার ($\text{V m}^{-1}$) \\ \cline{3-4} 
\textbf{১.} & $\text{c} = \frac{\text{E}_0}{\text{B}_0} = \frac{\text{E}}{\text{B}}$ & $\varepsilon_0 = \text{শূন্য মাধ্যমে তড়িৎ ভেদনযোগ্যতা}$ & \begin{tabular}[c]{@{}l@{}}কুলম্ব$^2$/নিউটন-মিটার$^2$\\ ($\text{C}^2\text{N}^{-1}\text{m}^{-2}$)\end{tabular} \\ \hline
 & & $\text{B}_0, \text{B} = \text{চৌম্বক ক্ষেত্র}$ & টেসলা ($\text{T}$) \\ \cline{3-4} 
\textbf{২.} & $\text{c} = \frac{1}{\sqrt{\mu_0\varepsilon_0}}$ & $\mu_0 = \text{শূন্য মাধ্যমে চৌম্বক প্রবেশ্যতা}$ & নিউটন/অ্যাম্পিয়ার$^2$ ($\text{N A}^{-2}$) \\ \hline
 & प्रतिসরাঙ্ক ও আলোর বেগের মধ্যে সম্পর্ক, & $\mu = \text{মাধ্যমের প্রতিসরাঙ্ক}$ & একক নেই \\ \cline{3-4} 
\textbf{৩.} & \quad $_a\mu_b = \frac{\text{c}_a}{\text{c}_b}$ & $\text{c}_a = \text{a মাধ্যমে আলোর বেগ, } \text{c}_b = \text{b মাধ্যমে আলোর বেগ}$ & মিটার/সে. ($\text{m s}^{-1}$) \\ \hline
\textbf{৪.} & দশা পার্থক্য, $\delta = \frac{2\pi}{\lambda} \times \text{x}$ & $\lambda = \text{তরঙ্গ দৈর্ঘ্য, } \text{x} = \text{পথ পার্থক্য}$ & মিটার ($\text{m}$) \\ \hline
 & & $\text{d} = \text{চির দুটির মধ্যবর্তী দূরত্ব, } \text{D} = \text{চির থেকে পর্দার দূরত্ব}$ & \\ \cline{3-4} 
\textbf{৫.} & কেন্দ্রীয় চরম থেকে দূরত্ব, $\text{x}_\text{n} = \text{n}\lambda \frac{\text{D}}{\text{d}}$ & $\text{x}_\text{n} = \text{কেন্দ্রীয় চরম থেকে দূরত্ব, } \text{n} = \text{ডোরার ক্রম}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৬.} & ডোরা ব্যবধান, $\Delta\text{x} = \lambda \frac{\text{D}}{\text{d}}$ & $\Delta\text{x} = \text{ডোরা ব্যবধান}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৭.} & উজ্জ্বল ডোরার প্রস্থ, $\text{x} = \lambda \frac{\text{D}}{2\text{d}}$ & $\text{x} = \text{ডোরার প্রস্থ, } \lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & meter ($\text{m}$) \\ \hline
 & & $\text{a} = \text{চিরের প্রস্থ, } \lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{৮.} & একক চিরে চরমের শর্ত, $\text{a} \sin \theta = (2\text{n} + 1)\frac{\lambda}{2}$ & $\theta = \text{অপবর্তন কোণ}$ & ডিগ্রি ($^\circ$) \\ \hline
\textbf{৯.} & একক চিরে অবমের শর্ত, $\text{a} \sin \theta = \text{n}\lambda$ & $\text{a} = \text{চিরের প্রস্থ, } \lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
\textbf{১০.} & গ্রেটিং সমীকরণ, $\text{d} \sin \theta = \text{n}\lambda$ & $\text{d} = \text{গ্রেটিং ধ্রুবক, } \lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip



\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $\text{d} = \text{দূরত্ব}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & & $\text{v} = \text{বেগ}$ & মিটার/সে. ($\text{m s}^{-1}$) \\ \cline{3-4} 
\textbf{১.} & ব্যতিচার নকশার অপসারণ, $\text{n} = \frac{2\text{dv}^2}{\lambda\text{c}^2}$ & $\lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & & $\text{c} = \text{আলোর বেগ}$ & মিটার/সে. ($\text{m s}^{-1}$) \\ \hline
\textbf{২.} & কাল দীর্ঘায়ন, $\text{t} = \frac{\text{t}_0}{\sqrt{1 - \frac{\text{v}^2}{\text{c}^2}}}$ & $\text{t}, \text{t}_0 = \text{সময়}$ & বছর ($\text{yr}$) \\ \hline
\textbf{৩.} & দৈর্ঘ্য সংকোচন, $\text{L} = \text{L}_0 \sqrt{1 - \frac{\text{v}^2}{\text{c}^2}}$ & $\text{L}, \text{L}_0 = \text{দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৪.} & গতিশীল ভর, $\text{m} = \frac{\text{m}_0}{\sqrt{1 - \frac{\text{v}^2}{\text{c}^2}}}$ & $\text{m}, \text{m}_0 = \text{ভর}$ & কেজি ($\text{kg}$) \\ \hline
\textbf{৫.} & গতিশক্তি, $\text{K} = (\text{m} - \text{m}_0) \text{c}^2$ & $\text{K} = \text{গতিশক্তি}$ & জুল ($\text{Joule, eV}$) \\ \hline
\textbf{৬.} & ভর-শক্তি সম্পর্ক, $\text{E} = \text{mc}^2$ & $\text{E} = \text{মোট শক্তি}$ & জুল ($\text{Joule, eV, MeV}$) \\ \hline
 & & $\text{h} = \text{প্লাঙ্কের ধ্রুবক}$ & জুল/সে. ($\text{J-s}$) \\ \cline{3-4} 
\textbf{৭.} & ফোটনের শক্তি, $\text{E} = \text{hf} = \frac{\text{hc}}{\lambda}$ & $\text{f} = \text{কম্পাঙ্ক}$ & হার্জ ($\text{Hz}$) \\ \hline
\textbf{৮.} & ফোটনের ভরবেগ, $\text{p} = \frac{\text{h}}{\lambda} = \frac{\text{E}}{\text{c}}$ & & \\ \hline
 & $\text{K}_{\text{max}} = \text{eV}_0$ & $\text{e} = \text{ইলেকট্রনের চার্জ}$ & কুলম্ব ($\text{C}$) \\ \cline{3-4} 
\textbf{৯.} & বা, $\frac{1}{2}\text{mv}_{\text{max}}^2 = \text{eV}_0$ বা, $\text{v}_{\text{max}} = \sqrt{\frac{2\text{eV}_0}{\text{m}}}$ & $\text{V}_0 = \text{নিবৃত্তি বিভব}$ & ভোল্ট ($\text{Volt}$) \\ \hline
 & & $\text{W}_0 = \text{কার্যাপেক্ষক}$ & জুল ($\text{Joule, eV}$) \\ \cline{3-4} 
\textbf{১০.} & কার্যাপেক্ষক, $\text{W}_0 = \text{hf}_0 = \frac{\text{hc}}{\lambda_0}$ & $\lambda_0 = \text{সূচন তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
 & $\text{E} = \text{K}_{\text{max}} + \text{W}_0$ & & \\ 
\textbf{১১.} & $\text{hf} = \frac{1}{2}\text{mv}_{\text{max}}^2 + \text{hf}_0$ & $\text{f}_0 = \text{সূচন কম্পাঙ্ক}$ & হার্জ ($\text{Hz}$) \\ 
 & $\frac{\text{hc}}{\lambda} = \text{K}_{\text{max}} + \frac{\text{hc}}{\lambda_0}$ & & \\ \hline
\textbf{১২.} & দ্য ব্রগলী তরঙ্গ দৈর্ঘ্য, $\lambda = \frac{\text{h}}{\text{mv}}$ & $\lambda = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \hline
 & কম্পটন তরঙ্গ দৈর্ঘ্য, & $\lambda, \lambda_0, \lambda_1 = \text{তরঙ্গ দৈর্ঘ্য}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
\textbf{১৩.} & $\Delta\lambda = \lambda_1 - \lambda_0 = 2\lambda_0 \sin^2 \frac{\phi}{2} = \frac{\text{h}}{\text{m}_0\text{c}} (1 - \cos \phi)$ & $\text{m}_0 = \text{ভর}$ & কেজি ($\text{kg}$) \\ \hline
 & & $\text{p} = \text{ভরবেগ}$ & কেজি-মি./সে. ($\text{kgms}^{-1}$) \\ \cline{3-4} 
\textbf{১৪.} & অনিশ্চয়তা নীতি, $\Delta \text{x} \, \Delta \text{p} \ge \frac{1}{2} \cdot \frac{\text{h}}{2\pi}$ & $\text{h} = \text{প্লাঙ্কের ধ্রুবক}$ & জুল-সে. ($\text{J-s}$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{জড় কাঠামো :} যেসব প্রসঙ্গ কাঠামোতে জড়তার সূত্র এবং নিউটনের গতির প্রথম সূত্র প্রযোজ্য হয় তাকে জড় কাঠামো বা জড়তার কাঠামো বলে।

\noindent \textbf{অজড় কাঠামো :} যেসব প্রসঙ্গ কাঠামোতে নিউটনের গতির সূত্র প্রযোজ্য নয় সেসব কাঠামোই অজড় কাঠামো।

\noindent \textbf{আইনস্টাইনের দ্বিতীয় স্বীকার্য :} আইনস্টাইনের দ্বিতীয় স্বীকার্যটি হলো— সকল জড় প্রসঙ্গ কাঠামোতে শূন্যস্থানে আলোর বেগ সর্বদা ধ্রুব থাকে।

\noindent \textbf{গ্যালিলীয় রূপান্তর :} চিরায়ত পদার্থবিজ্ঞানের যেসব সমীকরণ পরস্পরের সাপেক্ষে ধ্রুববেগে গতিশীল দুটি প্রসঙ্গ কাঠামোর সময় ও স্থানাঙ্কের মধ্যে সম্পর্ক স্থাপন করে তাদের গ্যালিলীয় রূপান্তর বলা হয়।

\noindent \textbf{লরেঞ্জ রূপান্তর :} সময় সার্বভৌম নয় গণ্য করে এবং আপেক্ষিকতার বিশেষ তত্ত্বের মৌলিক স্বীকার্য দুটি মেনে চলে পরস্পরের সাপেক্ষে ধ্রুববেগে গতিশীল দুটি প্রসঙ্গ কাঠামোর স্থানাঙ্ক ও সময়ের মধ্যে সম্পর্ক স্থাপনকারী যেসব সমীকরণ পাওয়া যায় তাদেরেকে লরেঞ্জ রূপান্তর বলে।

\noindent \textbf{আপেক্ষিকতা :} আইনস্টাইনের মতে, স্থান, কাল এবং ভর এদের কোনোটিই নিরপেক্ষ বা পরম নয়, প্রত্যেকটি অন্য কিছুর সাপেক্ষে বিবেচিত হয়। কোনো বিষয় অন্য কিছুর সাপেক্ষে বিবেচিত হওয়াই আপেক্ষিকতা।

\noindent \textbf{ভরের আপেক্ষিকতা :} বস্তুর নিশ্চল ভরের তুলনায় চলমান বা গতিশীল ভর বেশি হওয়ার घटनाকে ভরের আপেক্ষিকতা বলে।

\noindent \textbf{দৈর্ঘ্য সংকোচন :} কোনো বস্তুর গতিশীল অবস্থার দৈর্ঘ্য ঐ বস্তুর স্থির অবস্থার চেয়ে ছোট হওয়াকে দৈর্ঘ্য সংকোচন বলে।

\noindent \textbf{কাল দীর্ঘায়ন :} কোনো পর্যবেক্ষকের সাপেক্ষে গতিশীল অবস্থায় সংঘটিত দুটি ঘটনার মধ্যবর্তী কাল ব্যবধান ঐ পর্যবেক্ষকের সাপেক্ষে নিশ্চল অবস্থায় সংঘটিত ঐ একই ঘটনাদ্বয়ের মধ্যবর্তী কাল ব্যবধানের চেয়ে বেশি হবে, এ ঘটনাকে কাল দীর্ঘায়ন বলে।

\noindent \textbf{মৌলিক বল :} যে সকল বল অন্য কোনো বল থেকে উৎপন্ন হয়নি এবং অন্যকোনো বলের রূপও নয় বা রূপান্তরও নয়, সেসব বলকে মৌলিক বল বলা হয়।

\noindent \textbf{এক্স-রে :} দ্রুত গতিসম্পন্ন ইলেকট্রন কোনো ধাতব পাতে আঘাত করলে তা থেকে উচ্চ ভেদন ক্ষমতাসম্পন্ন অজানা প্রকৃতির এক প্রকার বিকিরণ উৎপন্ন হয়। এ বিকিরণকে বলা হয় এক্স-রে বা রঞ্জন রশ্মি।

\noindent \textbf{ক্ষরণ নল :} নিম্নচাপে বায়ুর মধ্য দিয়ে তড়িৎ ক্ষরণের পরীক্ষা চালানোর জন্য প্রায় $4\text{ cm}$ ব্যাসের $30\text{ cm}$ লম্বা যে কাচনল ব্যবহার করা হয় তাকে ক্ষরণ নল বলে।

\noindent \textbf{ফোটোইলেকট্রন :} যথাযথ উচ্চ কম্পাঙ্কের আলোক রশ্মি কোনো ধাতব পৃষ্ঠে আপতিত হলে তা থেকে ইলেকট্রন নিঃসৃত হয়, এই ইলেকট্রনকে ফোটোইলেকট্রন বলে।

\noindent \textbf{নিবৃত্তি বিভব :} ক্যাথোড প্লেটের সাপেক্ষে অ্যানোড প্লেটে যে ন্যূনতম ঋণ বিভব দিলে আলোক তড়িৎ প্রবাহমাত্রা সদ্য বন্ধ হয়ে যায় সেই বিভবই নিবৃত্তি বিভব।

\noindent \textbf{ফোটোইলেকট্রিক সেল :} যে যন্ত্রের সাহায্যে আলোক তড়িৎ ক্রিয়ার ভিত্তিতে আলোক শক্তিকে বিদ্যুৎ শক্তিতে রূপান্তরিত করা যায়, তাকে আলোক তড়িৎ কোষ বা ফোটোইলেকট্রিক সেল বলে।

\noindent \textbf{তরঙ্গ কণা দ্বৈততা :} তরঙ্গ কণা দ্বৈততা হলো এমন একটি ধারণা যাতে উল্লেখ করা হয় যে, সকল শক্তি তরঙ্গ সদৃশ এবং কণা সদৃশ উভয় ধর্ম প্রদর্শন করে।

\noindent \textbf{কার্যাপেক্ষক :} কোনো ধাতব পৃষ্ঠ হতে শূন্য বেগ সম্পন্ন ইলেকট্রন নির্গত করতে যতটুকু শক্তির প্রয়োজন তাকে ঐ ধাতুর কার্যাপেক্ষক বলে।

\noindent \textbf{আলোক তড়িৎ ক্রিয়া :} উচ্চ কম্পাঙ্কবিশিষ্ট আলোকরশ্মি কোনো ধাতবপৃষ্ঠে আপতিত হলে তা থেকে ইলেকট্রন নিঃসৃত হয়, এ ঘটনাকে আলোক তড়িৎ ক্রিয়া বলে।

\noindent \textbf{দ্য ব্রগলী তরঙ্গদৈর্ঘ্য :} প্রত্যেকটি চলমান পদার্থ কণার সাথে একটি তরঙ্গ যুক্ত থাকে। আবিষ্কারকের নামানুসারে এই তরঙ্গ দ্য ব্রগলী 'বস্তু তরঙ্গ' নামে পরিচিত এবং এই তরঙ্গের তরঙ্গদৈর্ঘ্যকে দ্য ব্রগলী তরঙ্গদৈর্ঘ্য বলে।

\noindent \textbf{দ্য ব্রগলী বস্তু তরঙ্গ :} প্রত্যেকটি চলমান পদার্থ কণার সাথে যে তরঙ্গ যুক্ত থাকে তাকে দ্য ব্রগলী বস্তু তরঙ্গ বলে।

\noindent \textbf{কম্পটন ক্রিয়া বা প্রভাব :} একবর্ণী এক্স রশ্মির দরুন বিক্ষিপ্ত বিকিরণের তরঙ্গদৈর্ঘ্য তথা কম্পাঙ্কের পরিবর্তন ঘটার ক্রিয়াকে কম্পটন প্রভাব বলে।

\bigskip
\bigskip


\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] ১৯০০ সালের আগ পর্যন্ত পদার্থবিজ্ঞানকে চিরায়ত ও সনাতনী পদার্থবিজ্ঞান নামে অভিহিত করা হয়।
    \item[$\blacktriangleright$] মাইকেলসন-মোরলের পরীক্ষায় আলোকরশ্মি কাচ প্লেটে ৪৫° কোণে আপতিত হয়।
    \item[$\blacktriangleright$] পৃথিবীর কক্ষপথের বেগ $30\text{ km s}^{-1}$।
    \item[$\blacktriangleright$] আপেক্ষিক তত্ত্বের জনক আইনস্টাইন।
    \item[$\blacktriangleright$] আপেক্ষিক তত্ত্ব মূলত ২ ভাগে বিভক্ত।
    \item[$\blacktriangleright$] আলবার্ট আইনস্টাইনের আপেক্ষিক তত্ত্ব 1905 সালে প্রকাশিত হয়।
    \item[$\blacktriangleright$] গ্যালিলিও রূপান্তরের অপর নাম নিউটনীয় রূপান্তর।
    \item[$\blacktriangleright$] $30\text{ বছর বয়সী একজন নভোচারী } 2.4 \times 10^8\text{ m s}^{-1}\text{ বেগে গতিশীল রকেটে চড়ে মহাকাশে গেলেন। পৃথিবীর হিসেবে } 50\text{ বছর পর}$ পৃথিবীতে ফিরে আসলে তার বয়স $60\text{ বছর হবে।}$
    \item[$\blacktriangleright$] ভর-শক্তি সম্পর্ক আইনস্টাইন আবিষ্কার করেন।
    \item[$\blacktriangleright$] একটি ইলেকট্রন ও প্রোটনের মধ্যকার মহাকর্ষ বল $3.6 \times 10^{-47}\text{ N}$।
    \item[$\blacktriangleright$] তাড়িতচৌম্বক বলের পাল্লা অসীম।
    \item[$\blacktriangleright$] লোহার ঘনত্ব $7.8 \times 10^3\text{ kg m}^{-3}\text{ হলে } 0.2\text{ c বেগে চলমান নভোযানে এর ঘনত্ব } 8.12 \times 10^3\text{ kg m}^{-3}\text{ হবে।}$
    \item[$\blacktriangleright$] প্ল্যাঙ্ক ধ্রুবকের মান $6.63 \times 10^{-34}\text{ J s}$।
    \item[$\blacktriangleright$] কোয়ান্টাম তত্ত্বানুসারে শক্তি যে গুচ্ছ বা প্যাকেট আকারে নির্গত হয় তার নাম কোয়ান্টাম।
    \item[$\blacktriangleright$] ইলেকট্রনের বেগ এবং প্রযুক্ত বিভব পার্থক্যের মধ্যে সম্পর্ক $\text{v} = \sqrt{\frac{2\text{eV}}{\text{m}}}$।
    \item[$\blacktriangleright$] এক্স-রে এর বেগ $3 \times 10^8\text{ m s}^{-1}$।
    \item[$\blacktriangleright$] সর্বপ্রথম ফোটোতড়িৎ ক্রিয়া আবিষ্কার করেন স্মিথ।
    \item[$\blacktriangleright$] পটাশিয়ামের কার্য আপেক্ষক $2.30\text{ eV}$।
    \item[$\blacktriangleright$] সোডিয়ামের সূচন তরঙ্গদৈর্ঘ্য $6800\text{ }\text{Å}\text{ হলে এর কার্য আপেক্ষক } 2.93 \times 10^{-19}\text{ J}$।
    \item[$\blacktriangleright$] ইলেকট্রনের ভরবেগ $4 \times 10^{-24}\text{ kg m s}^{-1}\text{ হলে ডি. ব্রগলী তরঙ্গ দৈর্ঘ্য } 1.65\text{ }\text{Å}$।
    \item[$\blacktriangleright$] ইলেকট্রনের কম্পটন তরঙ্গদৈর্ঘ্য $0.02468\text{ }\text{Å}$।
    \item[$\blacktriangleright$] হাইজেনবার্গের অনিশ্চয়তার নীতির সাহায্যে পরিমাপকৃত ত্রুটির গুণফলের একক $\text{Js}$।
    \item[$\blacktriangleright$] $1\text{ a.m.u} = 1.66057 \times 10^{-27}\text{ kg} = 931\text{ MeV}$
    \item[$\blacktriangleright$] কোনো বস্তুর দ্রুতি $2.6 \times 10^8\text{ ms}^{-1}\text{ হলে এর মোট শক্তি স্থিতাবস্থার শক্তির দ্বিগুণ।}$
    \item[$\blacktriangleright$] ফোটনের বৈশিষ্ট্য হলো— (i) এর দ্য ব্রগলী তরঙ্গদৈর্ঘ্য আছে। (ii) এর স্থির ভর নেই। (iii) এটি শূন্যস্থানে আলোর বেগে যায়।
    \item[$\blacktriangleright$] আপেক্ষিক তত্ত্ব অনুসারে শূন্য মাধ্যমে আলোর দ্রুতি ধ্রুবক।
    \item[$\blacktriangleright$] কোনো धातবপৃষ্ঠ থেকে ইলেকট্রন মুক্ত করতে যতটুকু শক্তির প্রয়োজন হয় তাকে ধাতুর কার্যাপেক্ষক বলে।
    \item[$\blacktriangleright$] হাইজেনবার্গ এর মতে একটি কণার অবস্থান ও ভরবেগ এবং শক্তি ও সময় একই সাথে জানা সম্ভব নয়।
    \item[$\blacktriangleright$] ফোটনের ভরবেগ হবে, $\text{p} = \frac{\text{h}}{\lambda}$।
    \item[$\blacktriangleright$] আপেক্ষিকতা অনুসারে কোনো বস্তুর স্থির ভর $\text{m}_0$ ও গতিশীল ভর $\text{m}$ হলে গতিশক্তি হবে, $\text{K} = (\text{m} - \text{m}_0)\text{c}^2$।
    \item[$\blacktriangleright$] চিরায়ত বলবিদ্যা মতে স্থান, কাল, ভর, ধ্রুবক।
    \item[$\blacktriangleright$] $\frac{\sqrt{3}}{2}\text{c}$ দ্রুতিতে চলতে থাকলে বস্তুর দৈর্ঘ্য অর্ধেক হয়ে যায়।
    \item[$\blacktriangleright$] ফোটন বিদ্যুৎ ক্ষেত্র দ্বারা প্রভাবিত হয় না।
    \item[$\blacktriangleright$] আপেক্ষিক তত্ত্বানুসারে গতিশীলতার দরুন বস্তুর দৈর্ঘ্য হ্রাস পায় কিন্তু ভর বৃদ্ধি পায়।
    \item[$\blacktriangleright$] কম্পটন ক্রিয়ায় আলোর তরঙ্গ ও কণাধর্ম প্রকাশ পায়।
    \item[$\blacktriangleright$] আলোক তড়িৎ ক্রিয়ায় আপতিত আলোক রশ্মির কম্পাঙ্ক বেশি হলে নির্গত ইলেকট্রনের বেগ বেশি হবে।
    \item[$\blacktriangleright$] সর্বপ্রথম ফোটন তড়িৎ ক্রিয়া আবিষ্কার করেন স্মিথ।
    \item[$\blacktriangleright$] এক্স-রে তড়িৎ চুম্বকীয় তরঙ্গ, সরলরেখায় চলে, চার্জ নিরপেক্ষ।
    \item[$\blacktriangleright$] প্রসঙ্গ কাঠামো ত্রিমাত্রিক স্থানে কল্পনা করা যায়।
    \item[$\blacktriangleright$] পৃথিবীর কক্ষপথের বেগ $30\text{ km s}^{-1}$।
    \item[$\blacktriangleright$] গতিশীল মহাশূন্যযানে ঘড়ি পৃথিবীতে অবস্থিত ঘড়ির তুলনায় ধীরে চলে, একে কাল প্রসারণ বলে।
\end{itemize}


\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] $\gamma$-ray এর কোনো ভর নেই।
    \item[$\blacktriangleright$] হাইড্রোজেন ফিশনের ফলে হিলিয়ামের সৃষ্টি হয়।
    \item[$\blacktriangleright$] $\beta$-ray ঋণাত্মক চার্জ বহন করে।
    \item[$\blacktriangleright$] তেজস্ক্রিয়তা একটি নিউক্লীয় ঘটনা।
    \item[$\blacktriangleright$] এক্স রশ্মির ভেদন ক্ষমতা অত্যধিক কিন্তু গামা রশ্মির ভেদন ক্ষমতা সর্বাধিক।
    \item[$\blacktriangleright$] জড় পদার্থের ভিতরে পরমাণুগুলো গতিশীল থাকে।
    \item[$\blacktriangleright$] 'পরমাণু একটি ধনাত্মক তড়িৎআহিত গোলক' মতবাদটি থমসনের।
    \item[$\blacktriangleright$] রাদারফোর্ড $\alpha$ কণিকা পরীক্ষার জন্য পোলোনিয়াম ব্যবহার করেন।
    \item[$\blacktriangleright$] পরমাণুর ব্যাসার্ধ $10^{-8}\text{ cm}$ পর্যায়ের।
    \item[$\blacktriangleright$] নিউক্লিয়াসের ব্যাসার্ধ $10^{-13}\text{ cm} - 10^{-14}\text{ cm}$ পর্যায়ের।
    \item[$\blacktriangleright$] ইলেকট্রন উচ্চ শক্তিস্তর থেকে নিম্ন শক্তিস্তরে গেলে শক্তির বিকিরণ ঘটে।
    \item[$\blacktriangleright$] বোর কোয়ান্টাম তত্ত্বের প্রসারণ ঘটিয়ে পরমাণুর বর্ণালি ব্যাখ্যা করেন।
    \item[$\blacktriangleright$] রাদারফোর্ডের মডেলকে সৌরজগতের সাথে তুলনা করা হয়।
    \item[$\blacktriangleright$] নিউক্লিয়াসের অভ্যন্তরে মেসন কণিকার সন্ধান পাওয়া যায়।
    \item[$\blacktriangleright$] মেসন কণার অস্তিত্ব মহাজাগতিক রশ্মির সাহায্যে জানা যায়।
    \item[$\blacktriangleright$] পজিট্রন একটি অ্যান্টি ইলেকট্রন।
    \item[$\blacktriangleright$] তেজস্ক্রিয় ভাঙনের সময় $\beta$-রশ্মির সাথে $\gamma$-রশ্মিও নির্গত হয়।
    \item[$\blacktriangleright$] প্রোটন ও নিউট্রনকে একত্রে নিউক্লিয়ন বলা হয়।
    \item[$\blacktriangleright$] $_{92}^{235}\text{U}$ কে নিউট্রন দ্বারা আঘাত করলে ৩টি নিউট্রন এবং বিপুল পরিমাণ শক্তি উৎপন্ন হয়।
    \item[$\blacktriangleright$] ইলেকট্রনের উপর প্রযুক্ত কেন্দ্রমুখী বল $\text{F}_\text{c} = \frac{\text{mv}^2}{\text{r}}$।
    \item[$\blacktriangleright$] তেজস্ক্রিয় পদার্থের গড় আয়ু অর্ধায়ুর সমানুপাতিক $\left(\text{T}_{\frac{1}{2}} = 0.693\text{ }\tau\right)$।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\begin{tabular}{|c|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি ও একক}} \\ \hline
\textbf{১.} & \begin{tabular}[c]{@{}l@{}}হাইড্রোজেন পরমাণুর n-তম বোর কক্ষের ব্যাসার্ধ,\\ $\text{r}_\text{n} = \frac{\text{n}^2\text{h}^2\varepsilon_0}{\pi\text{m}\text{e}^2}$ এবং $\text{r}_\text{n} = \text{n}^2 \times \text{r}_1$\end{tabular} & \begin{tabular}[c]{@{}l@{}}$\text{h} = \text{প্লাঙ্কের ধ্রুবক (J-s)}$\\ $\varepsilon_0 = \text{শূন্য মাধ্যমের ভেদনযোগ্যতা }(\text{N}^{-1}\text{m}^{-2}\text{C}^2)$\end{tabular} \\ \hline
\textbf{২.} & \begin{tabular}[c]{@{}l@{}}হাইড্রোজেন পরমাণুর n-তম বোর কক্ষের শক্তি,\\ $\text{E}_\text{n} = \frac{-\text{m}\text{e}^4}{8\text{n}^2\text{h}^2\varepsilon_0^2}$ এবং $\text{E}_\text{n} = \frac{\text{E}_1}{\text{n}^2}$\end{tabular} & \begin{tabular}[c]{@{}l@{}}$\text{m} = \text{ইলেকট্রনের ভর (kg)}$\\ $\text{e} = \text{ইলেকট্রনের চার্জ (c)}$\\ $\text{r} = \text{ব্যাসার্ধ (m)}$\end{tabular} \\ \hline
\textbf{৩.} & কৌণিক ভরবেগ, $\text{L} = \frac{\text{nh}}{2\pi}$ & \begin{tabular}[c]{@{}l@{}}$\text{E} = \text{শক্তি (J, eV, MeV)}$\\ $\text{L} = \text{কৌণিক ভরবেগ }(\text{kg m}^2\text{ s}^{-1})$\end{tabular} \\ \hline
\textbf{৪.} & কক্ষপথে ইলেকট্রনের বেগ, $\text{v} = \frac{\text{nh}}{2\pi\text{mr}}$ বা, $\text{v} = \frac{\text{e}}{\sqrt{4\pi\text{m}\varepsilon_0\text{r}}}$ & \begin{tabular}[c]{@{}l@{}}$\text{v} = \text{বেগ }(\text{m s}^{-1})$\\ $\text{f} = \text{কম্পাঙ্ক (Hz)}$\end{tabular} \\ \hline
\textbf{৫.} & বিকিরিত বা শোষিত শক্তি, $\text{E} = \text{E}_2 - \text{E}_1 = \text{hf}$ & $\text{c} = \text{আলোর বেগ }(\text{m s}^{-1})$ \\ \hline
\textbf{৬.} & কম্পাঙ্ক, $\text{f} = \frac{\text{m}\text{e}^4}{8\text{h}^3\varepsilon_0^2}\left(\frac{1}{\text{n}_1^2} - \frac{1}{\text{n}_2^2}\right)$ & $\text{R} = \text{রিডবার্গ ধ্রুবক }(\text{m}^{-1})$ \\ \hline
\textbf{৭.} & রিডবার্গ ধ্রুবক, $\text{R} = \frac{\text{m}\text{e}^4}{8\text{h}^3\varepsilon_0^2\text{c}}$ & \begin{tabular}[c]{@{}l@{}}$\lambda = \text{অবক্ষয় ধ্রুবক (সময়}^{-1}\text{, s}^{-1}\text{, min}^{-1}\text{, hr}^{-1}\text{,}$\\ $\text{day}^{-1}\text{, year}^{-1})$\end{tabular} \\ \hline
\textbf{৮.} & অক্ষত পরমাণুর সংখ্যা, $\text{N} = \text{N}_0\text{e}^{-\lambda\text{t}}$ & $\text{t} = \text{সময় (s, min, hr, day, year)}$ \\ \hline
\end{tabular}

\bigskip
\bigskip


\bigskip

\noindent \textbf{■ এক নজরে প্রতিটি গেইটের নাম, প্রতীক, আউটপুট, ফাংশন ও সত্যক সারণি দেখানো হলো :}

\bigskip

\begin{tabular}{|c|c|c|c|}
\hline
\textbf{গেইটের নাম} & \textbf{প্রতীক} & \textbf{আউটপুট ফাংশন} & \textbf{সত্যক সারণি} \\ \hline
 & & & 
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{2}{|c|}{\textbf{ইনপুট}} & \textbf{আউটপুট} \\ \hline
A & B & \textbf{Y = AB} \\ \hline
0 & 0 & 0 \\ \hline
0 & 1 & 0 \\ \hline
1 & 0 & 0 \\ \hline
1 & 1 & 1 \\ \hline
\end{tabular} \\ 
\textbf{AND গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (0,0) -- (0,1) arc[start angle=90, end angle=-90, radius=0.5] -- cycle;
\draw[thick] (-0.6,0.25) -- (0,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (0,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.5,0.5) -- (1.2,0.5) node[right] {\small Y=AB};
\end{tikzpicture}
\end{minipage} & $\text{Y} = \text{AB}$ & \\ \hline

 & & & 
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{2}{|c|}{\textbf{ইনপুট}} & \textbf{আউটপুট} \\ \hline
A & B & \textbf{Y = A + B} \\ \hline
0 & 0 & 0 \\ \hline
0 & 1 & 1 \\ \hline
1 & 0 & 1 \\ \hline
1 & 1 & 1 \\ \hline
\end{tabular} \\ 
\textbf{OR গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (0,0) to[out=25,in=155] (0,1) to[out=-25,in=115] (0.8,0.5) to[out=-115,in=25] (0,0);
\draw[thick] (-0.6,0.25) -- (0.04,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (0.04,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.8,0.5) -- (1.4,0.5) node[right] {\small Y=A+B};
\end{tikzpicture}
\end{minipage} & $\text{Y} = \text{A} + \text{B}$ & \\ \hline

 & & & 
\begin{tabular}{|c|c|}
\hline
\textbf{ইনপুট} & \textbf{আউটপুট} \\ \hline
A & \textbf{Y} = $\mathbf{\bar{A}}$ \\ \hline
0 & 1 \\ \hline
1 & 0 \\ \hline
\end{tabular} \\ 
\textbf{NOT গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (0,0.1) -- (0,0.9) -- (0.6,0.5) -- cycle;
\draw[thick] (0.68,0.5) circle (0.08);
\draw[thick] (-0.6,0.5) -- (0,0.5) node[left,pos=0] {\small A};
\draw[thick] (0.76,0.5) -- (1.4,0.5) node[right] {\small Y=$\overline{\text{A}}$};
\end{tikzpicture}
\end{minipage} & $\text{Y} = \mathbf{\bar{A}}$ & \\ \hline

\textbf{NAND গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (0,0) -- (0,1) arc[start angle=90, end angle=-90, radius=0.5] -- cycle;
\draw[thick] (0.58,0.5) circle (0.08);
\draw[thick] (-0.6,0.25) -- (0,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (0,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.66,0.5) -- (1.3,0.5) node[right] {\small Y=$\overline{\text{AB}}$};
\end{tikzpicture}
\end{minipage} & $\text{Y} = \overline{\text{AB}}$ & 
\begin{tabular}{|c|c|c|c|}
\hline
A & B & AB & \textbf{Y} = $\mathbf{\overline{AB}}$ \\ \hline
0 & 0 & 0 & 1 \\ \hline
0 & 1 & 0 & 1 \\ \hline
1 & 0 & 0 & 1 \\ \hline
1 & 1 & 1 & 0 \\ \hline
\end{tabular} \\ \hline

\textbf{NOR গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (0,0) to[out=25,in=155] (0,1) to[out=-25,in=115] (0.8,0.5) to[out=-115,in=25] (0,0);
\draw[thick] (0.88,0.5) circle (0.08);
\draw[thick] (-0.6,0.25) -- (0.04,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (0.04,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.96,0.5) -- (1.5,0.5) node[right] {\small Y=$\overline{\text{A+B}}$};
\end{tikzpicture}
\end{minipage} & $\text{Y} = \overline{\text{A} + \text{B}}$ & 
\begin{tabular}{|c|c|c|c|}
\hline
A & B & A+B & \textbf{Y} = $\mathbf{\overline{A+B}}$ \\ \hline
0 & 0 & 0 & 1 \\ \hline
0 & 1 & 1 & 0 \\ \hline
1 & 0 & 1 & 0 \\ \hline
1 & 1 & 1 & 0 \\ \hline
\end{tabular} \\ \hline

 & & $\text{Y} = \text{A} \oplus \text{B}$ & 
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{2}{|c|}{\textbf{ইনপুট}} & \textbf{আউটপুট} \\ \hline
A & B & \textbf{Y = A} $\mathbf{\oplus}$ \textbf{B} \\ \hline
0 & 0 & 0 \\ \hline
0 & 1 & 1 \\ \hline
1 & 0 & 1 \\ \hline
1 & 1 & 0 \\ \hline
\end{tabular} \\ 
\textbf{XOR গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (-0.12,0) to[out=25,in=155] (-0.12,1);
\draw[thick] (0,0) to[out=25,in=155] (0,1) to[out=-25,in=115] (0.8,0.5) to[out=-115,in=25] (0,0);
\draw[thick] (-0.6,0.25) -- (-0.06,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (-0.06,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.8,0.5) -- (1.5,0.5) node[right] {\small Y=A$\oplus$B};
\end{tikzpicture}
\end{minipage} & $= \mathbf{\bar{A}}\text{B} + \text{A}\mathbf{\bar{B}}$ & \\ \hline

 & & $\text{Y} = \overline{\text{A} \oplus \text{B}}$ & 
\begin{tabular}{|c|c|c|}
\hline
\multicolumn{2}{|c|}{\textbf{ইনপুট}} & \textbf{আউটপুট} \\ \hline
A & B & \textbf{Y = A} $\mathbf{\oplus}$ \textbf{B} \\ \hline
0 & 0 & 1 \\ \hline
0 & 1 & 0 \\ \hline
1 & 0 & 0 \\ \hline
1 & 1 & 1 \\ \hline
\end{tabular} \\ 
\textbf{XNOR গেইট} & 
\begin{minipage}{3.5cm}
\centering
\begin{tikzpicture}[scale=0.7, baseline={           ([yshift=-0.6ex]current bounding box.center)}]
\draw[thick] (-0.12,0) to[out=25,in=155] (-0.12,1);
\draw[thick] (0,0) to[out=25,in=155] (0,1) to[out=-25,in=115] (0.8,0.5) to[out=-115,in=25] (0,0);
\draw[thick] (0.88,0.5) circle (0.08);
\draw[thick] (-0.6,0.25) -- (-0.06,0.25) node[left,pos=0] {\small B};
\draw[thick] (-0.6,0.75) -- (-0.06,0.75) node[left,pos=0] {\small A};
\draw[thick] (0.96,0.5) -- (1.6,0.5) node[right] {\small Y=$\overline{\text{A}\oplus\text{B}}$};
\end{tikzpicture}
\end{minipage} & $= \text{AB} + \mathbf{\bar{A}}\mathbf{\bar{B}}$ & \\ \hline
\end{tabular}

\bigskip
\bigskip



\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] পরিবাহীর আপেক্ষিক রোধ $10^{-8}\text{ }\Omega\text{m}$।
    \item[$\blacktriangleright$] অ্যান্টিমনি একটি অর্ধপরিবাহী পদার্থ।
    \item[$\blacktriangleright$] $(225)_{10}$ এর অক্টাল মান $(341)_8$।
    \item[$\blacktriangleright$] $\text{NOT}$, $\text{OR}$ ও $\text{AND}$ গেট মৌলিক লজিক গেট।
    \item[$\blacktriangleright$] পরিবাহীতে যোজনী ব্যান্ড এবং পরিবহন ব্যান্ডের মধ্যে শক্তি ফাঁক শূন্য।
    \item[$\blacktriangleright$] ত্রিয়োজী অপদ্রব্য বিশুদ্ধ অর্ধপরিবাহীতে সংযুক্ত করলে হোল সৃষ্টি হয়।
    \item[$\blacktriangleright$] অর্ধপরিবাহীতে যোজনী ব্যান্ড ও পরিবহন ব্যান্ডের মধ্যে শক্তি ব্যবধান $< 2\text{ eV}$।
    \item[$\blacktriangleright$] পরিবহন ব্যান্ড পরিবহন ইলেকট্রন দ্বারা গঠিত।
    \item[$\blacktriangleright$] $\text{NOR}$ ও $\text{NAND}$ গেট দুটিকে সর্বজনীন গেট বলা হয়।
    \item[$\blacktriangleright$] $\text{p-n}$ জাংশনে ব্যাপন প্রক্রিয়ায় হোল ও ইলেকট্রনের স্থানান্তর ঘটে।
    \item[$\blacktriangleright$] রোধ একটি নিয়ন্ত্রণযোগ্য প্রক্রিয়া।
    \item[$\blacktriangleright$] বিপরীতমুখী ঝোঁকের কারণে জাংশন ডায়োডে খালি অঞ্চলের সৃষ্টি হয়।
    \item[$\blacktriangleright$] $1\text{ k byte} = 1024\text{ byte}$।
    \item[$\blacktriangleright$] $\text{p-n}$ জাংশনে বিমুখী বায়াস প্রয়োগ করলে জাংশন রোধ বেড়ে যায়।
    \item[$\blacktriangleright$] জেনার ক্রিয়ায় রোধ কমে যায়।
    \item[$\blacktriangleright$] যোজন ব্যান্ডে সৃষ্ট গর্ত ধনাত্মক হয়।
    \item[$\blacktriangleright$] নিষিদ্ধশক্তি অঞ্চলে ইলেকট্রন থাকতে পারে না।
    \item[$\blacktriangleright$] জার্মেনিয়ামের সর্বশেষ কক্ষপথে চারটি ইলেকট্রন থাকে।
    \item[$\blacktriangleright$] $\text{LED}$ এর পূর্ণরূপ $\text{Light Emitting Diode}$।
    \item[$\blacktriangleright$] $\text{n}$-টাইপ সেমিকন্ডাক্টরে ইলেকট্রনের জন্য তড়িৎ পরিবাহিত হয়।
    \item[$\blacktriangleright$] ইলেকট্রনিক্স সুইচ হিসেবে ট্রানজিস্টর ব্যবহৃত হয়।
    \item[$\blacktriangleright$] কালেক্টর কারেন্ট এমিটার কারেন্ট থেকে সর্বদা কম।
    \item[$\blacktriangleright$] $\text{FET}$ এর পূর্ণরূপ $\text{Field Effect Transister}$।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $\text{R} = \text{জাংশনের রোধ}$ & ওহম ($\Omega$) \\ \cline{3-4} 
\textbf{১.} & জাংশনের রোধ, $\text{R} = \frac{\Delta\text{V}}{\Delta\text{I}}$ & $\Delta\text{V} = \text{বিভব পার্থক্যের পরিবর্তন}$ & ভোল্ট ($\text{V}$) \\ \cline{3-4} 
 & & $\Delta\text{I} = \text{তড়িৎ প্রবাহের পরিবর্তন}$ & অ্যাম্পিয়ার ($\text{A}$) \\ \hline
\textbf{২.} & নিঃসারক প্রবাহ, $\text{I}_\text{E} = \text{I}_\text{B} + \text{I}_\text{C}$ & $\text{I}_\text{B} = \text{পীঠ প্রবাহ, } \text{I}_\text{C} = \text{সংগ্রাহক প্রবাহ}$ & অ্যাম্পিয়ার ($\text{A}$) \\ \hline
\textbf{৩.} & প্রবাহ লাভ, $\beta = \frac{\Delta\text{I}_\text{C}}{\Delta\text{I}_\text{B}}$ & \begin{tabular}[c]{@{}l@{}}$\Delta\text{I}_\text{C} = \text{সংগ্রাহক প্রবাহের পরিবর্তন, } \Delta\text{I}_\text{B} = \text{পীঠ}$\\ \text{প্রবাহের পরিবর্তন}\end{tabular} & মিলি অ্যাম্পিয়ার ($\text{mA}$) \\ \hline
\textbf{৪.} & বিবর্ধন গুণক, $\alpha = \frac{\text{I}_\text{C}}{\text{I}_\text{E}}$ & $\text{I}_\text{C} = \text{সংগ্রাহক প্রবাহ, } \text{I}_\text{E} = \text{নিঃসারক প্রবাহ}$ & অ্যাম্পিয়ার ($\text{A}$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip


\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize সার-সংক্ষেপ | Summary}}}\par\vspace{2pt}

\bigskip

\noindent \textbf{বিগ ব্যাং :} বিগ ব্যাং হচ্ছে মহাবিশ্বের পরিলক্ষিত ক্রমবর্ধমান সম্প্রসারণ। আদিতে ঘনবিন্যস্ত থাকায় পৃথিবী প্রচণ্ড উত্তপ্ত পদার্থের অগ্নিগোলক ছিল যা বিকিরণ বিগ ব্যাং-এর ফলে চতুর্দিকে প্রসারিত হয়, ঠাণ্ডা হয় এবং নির্দিষ্ট তাপমাত্রায় অনুক্রমিত অবস্থানান্তরিত হয়।

\noindent \textbf{সৃষ্টিতত্ত্ব :} মহাবিশ্বের প্রকৃতি, উৎস ও বিবর্তন নিয়ে যে পর্যালোচনা তাকে সৃষ্টিতত্ত্ব বলে।

\noindent \textbf{মহাবিশ্ব :} সূর্য, নক্ষত্র, গ্রহ, উপগ্রহ, উল্কা, নীহারিকা ইত্যাদি নিয়ে মহাবিশ্ব গঠিত। মহাবিশ্ব হলো সকল বস্তু যা আমরা কোনো না কোনোভাবে পর্যবেক্ষণ করতে পারি।

\noindent \textbf{সৌরজগৎ :} সূর্য ও এর গ্রহ ও উপগ্রহ, ধূমকেতু, উল্কা, গ্রহাণু, গ্যাস, ধূলিকণা ইত্যাদি নিয়ে সৌরজগৎ গঠিত।

\noindent \textbf{অ্যান্ড্রোমেডা :} অ্যান্ড্রোমেডা একটি গ্যালাক্সি যাকে খালি চোখে দেখা যায় না।

\noindent \textbf{পালসার :} কোনো নক্ষত্র যখন সুপারনোভা হিসেবে বিস্ফোরিত হয় তখন এর কোর বা মূল বস্তুর চাপ এত বেশি হয় যে প্রোটন ও নিউট্রন একত্রিত হয়ে নিউট্রন গঠন করে। এদেরকে নিউট্রন নক্ষত্র বা পালসার বলে।

\noindent \textbf{মৌলিক কণা :} যে সকল কণা পরম আদি বা প্রাথমিক এবং অবিভাজ্য তাদেরকে মৌলিক কণা বলে।

\noindent \textbf{মিথস্ক্রিয়া :} মিথস্ক্রিয়া বলতে পারস্পরিক ক্রিয়া-প্রতিক্রিয়া অর্থাৎ আকর্ষণ বিকর্ষণকে বুঝায়। অন্যভাবে বলা যায়, দ্বিপাক্ষিক কিছু বিনিময় বা কোনো কিছু ক্ষরণ বা গ্রহণ বিনিময়ে রূপান্তরকে বুঝায়।

\noindent \textbf{আকাশ গঙ্গা :} আমরা যে গ্যালাক্সিতে বা ছায়াপথে বাস করি তার নাম আকাশ গঙ্গা।

\noindent \textbf{চন্দ্র শেখর সীমা :} মৃত্যু পূর্ব শুরুর মুহূর্তে কোনো তারকার ভর $1.4$ সৌর ভরের বেশি হলে তারকাটি কৃষ্ণবিবর বা নিউট্রন তারকায় পরিণত হতে পারে। ভরের এই সীমা চন্দ্রশেখর সীমা নামে পরিচিত।

\noindent \textbf{সুপারনোভা :} নক্ষত্রের ভর যখন দুই থেকে পাঁচ সৌর ভরের মধ্যে থাকে, তখন সংকোচনের সময় এটি এর বহিঃস্থ আস্তরণ ছুঁড়ে দিয়ে অত্যন্ত উজ্জ্বল হয়ে যায়। একে বলা হয় “সুপারনোভা”।

\noindent \textbf{কৃষ্ণবিবর :} সুপারনোভা বিস্ফোরণের পর নক্ষত্রের ভর যদি খুব বেশি হয় তখন এর অন্তর্বস্তু অনির্দিষ্টভাবে সংকুচিত হতে থাকে। এভাবে যে বস্তু তৈরি হয় তাকে কৃষ্ণ বিবর বলে।

\noindent \textbf{কৃষ্ণগহ্বর :} মহাকাশে কোনো বস্তু বা এর আশেপাশে যে অঞ্চল থেকে কোনো তথ্য পাওয়া সম্ভব নয় এবং যেখান থেকে আলো বা কোনো বস্তু বেরিয়ে আসতে পারে না সেই অঞ্চলই হলো কৃষ্ণগহ্বর।

\noindent \textbf{ডার্ক এনার্জি :} মহাবিশ্বের ত্বরান্বিত সম্প্রসারণ কোন এক অদৃশ্য শক্তির কারণেই হচ্ছে। এই অদৃশ্য শক্তিকেই ডার্ক এনার্জি বলে।

\noindent \textbf{সোয়ার্জশাইল্ড ব্যাসার্ধ :} কৃষ্ণবিবরের ঘটনা দিগন্তের ব্যাসার্ধকে সোয়ার্জশাইল্ড ব্যাসার্ধ বলে।

\noindent \textbf{নেবুলা :} মহাকাশে ছড়িয়ে থাকা গ্যাস ও ধুলোর সুবিশাল মেঘের সমারোহই নীহারিকা বা নেবুলা।

\noindent \textbf{কোয়াসার :} কোয়াসার হলো আধানাক্ষত্রিক রেডিও উৎস যাদের গঠন নক্ষত্রের ন্যায় এবং ক্ষমতাশালী বেতার তরঙ্গ নিঃসরণ করে।

\noindent \textbf{হ্যাড্রন কণা :} সে সকল মৌলিক কণা শক্তিশালী নিউক্লীয় বিদ্যুৎ চুম্বকীয় এবং দুর্বল নিউক্লীয় এই তিন প্রক্রিয়াতে অংশগ্রহণ করতে পারে তাদেরকে হ্যাড্রন কণা বলে।

\noindent \textbf{কোয়ার্ক :} কোয়ার্ক হলো অতি পারমাণবিক কণা যা দ্বারা প্রোটন ও নিউট্রনসমূহ গঠিত।

\noindent \textbf{রেডিও টেলিস্কোপ :} রেডিও টেলিস্কোপ এক ধরনের দিক নির্দেশী বেতার এন্টেনা যা বেতার জ্যোতির্বিদ্যায় ব্যবহৃত হয়।

\noindent \textbf{জ্যোতির্বিজ্ঞান :} যে শাস্ত্র আকাশ ও মহাকাশের চন্দ্র, সূর্য, গ্রহ, নক্ষত্র, নীহারিকা ইত্যাদি বিষয়ে তথ্যাদির বিবরণসহ আলোচনা ও অনুসন্ধান করে তাকে জ্যোতির্বিজ্ঞান বলে।

\noindent \textbf{অপটিক্যাল টেলিস্কোপ :} যে টেলিস্কোপের সাহায্যে দৃশ্যমান আলোর সহায়তায় দৃশ্যমান আলো নিঃসরণকারী বা প্রতিফলনকারী বস্তু পর্যবেক্ষণ করা হয় তাকে অপটিক্যাল টেলিস্কোপ বলে।

\noindent \textbf{কৃত্রিম উপগ্রহ :} ভূপৃষ্ঠ হতে একটি নির্দিষ্ট উচ্চতায় নির্দিষ্ট বেগে মনুষ্য নির্মিত কোনো মহাকাশযান উপগ্রহ চাঁদের মতো পৃথিবীকে কেন্দ্র করে বৃত্তাকার পথে ঘুরতে থাকলে তাকে কৃত্রিম উপগ্রহ বলে।

\noindent \textbf{মহাশূন্য প্রোব :} মহাশূন্য প্রোব হলো মহাশূন্যে অনুসন্ধানী যান যা অপটিক্যাল ও রেডিও টেলিস্কোপ ছাড়াও মহাবিশ্ব অনুসন্ধানের জন্য ব্যবহৃত সকল রকম কৌশল অবলম্বন করে।

\bigskip
\bigskip



\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize একনজরে অধ্যায়ের গুরুত্বপূর্ণ বিষয়াবলি | Important Matters of the Chapter at a Glance}}}\par\vspace{2pt}

\bigskip

\begin{itemize}
    \item[$\blacktriangleright$] মহাবিশ্ব সম্প্রসারণের সাথে সাথে বিকিরণের তাপমাত্রা কমে যায়।
    \item[$\blacktriangleright$] মহাবিশ্বে তারকারাজি থেকে নিঃসৃত গ্যাস হাইড্রোজেন।
    \item[$\blacktriangleright$] মহাকাশে তারকার বিস্ফোরণকে সুপারনোভা বলা হয়।
    \item[$\blacktriangleright$] মহাবিশ্বের বর্তমান বয়স ১৫ বিলিয়ন বছর। পৃথিবীর বয়স প্রায় ৫০০ কোটি বছর।
    \item[$\blacktriangleright$] একটি ছায়াপথের লাল বিচ্যুতি আমাদের কাছ থেকে তার দূরত্বের সমানুপাতিক।
    \item[$\blacktriangleright$] প্রোটন ও নিউট্রন কোয়ার্ক দ্বারা গঠিত।
    \item[$\blacktriangleright$] $\rho > \rho_\text{c}$ হলে ভবিষ্যতে একসময় মহাবিশ্ব চুপসে যাবে।
    \item[$\blacktriangleright$] সূর্যের ঘনত্ব পানির তুলনায় 1.4 গুণ।
    \item[$\blacktriangleright$] $\gamma$-রশ্মির ভেদনক্ষমতা সবচেয়ে বেশি।
    \item[$\blacktriangleright$] মহাবিশ্বের বর্তমান তাপমাত্রা $\text{3000 K}$।
    \item[$\blacktriangleright$] সূর্য শ্বেত বামন নক্ষত্র।
    \item[$\blacktriangleright$] সূর্য একটা ২য় জেনারেশন নক্ষত্র।
    \item[$\blacktriangleright$] মহাবিশ্ব একদিন তাপীয় সাম্যাবস্থায় পৌঁছাবে।
    \item[$\blacktriangleright$] মহাবিশ্বের, গড় ঘনত্ব সংকট ঘনত্বের সমান হলে এর আকৃতি সমতল হবে।
    \item[$\blacktriangleright$] সূর্যের পর পৃথিবীর নিকটতম নক্ষত্র আলফা সেন্টুরি। প্রায় ৪.২ আলোকবর্ষ দূরে।
    \item[$\blacktriangleright$] কৃত্রিম উপগ্রহ ব্যবহৃত হয় যোগাযোগের ক্ষেত্রে, ভূ-জরিপের কাজে, আবহাওয়ার পূর্বাভাস জানতে।
    \item[$\blacktriangleright$] মহাবিশ্বে ডার্ক এনার্জি-ম্যাটার সবচেয়ে বেশি।
    \item[$\blacktriangleright$] হাবলের টেলিস্কোপ একটি অপটিক্যাল টেলিস্কোপ।
    \item[$\blacktriangleright$] সুপারনোভা'র পরবর্তী ধাপ হলো নিউট্রন স্টার।
    \item[$\blacktriangleright$] বোল্টজম্যান ধ্রুবকের মান $1.38 \times 10^{-23}\text{ JK}^{-1}$।
    \item[$\blacktriangleright$] মহাবিশ্ব পুনরায় সংকুচিত হয় স্পন্দনশীল তত্ত্ব অনুসারে।
    \item[$\blacktriangleright$] উষ্ণ তারকার অভ্যন্তরীণ তাপমাত্রা দশ হাজার ডিগ্রি সেলসিয়াস।
\end{itemize}

\bigskip

\vspace{6pt}\noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\color{white}\B{\bfseries\footnotesize প্রতীক ও এককসহ গুরুত্বপূর্ণ সূত্রাবলি | Important Formulas with Symbols \& Units}}}\par\vspace{2pt}

\bigskip

\noindent\resizebox{\linewidth}{!}{%
\begin{tabular}{|c|l|l|l|}
\hline
\textbf{নং} & \multicolumn{1}{c|}{\textbf{সূত্রাবলি}} & \multicolumn{1}{c|}{\textbf{প্রতীক পরিচিতি}} & \multicolumn{1}{c|}{\textbf{একক}} \\ \hline
 & & $\text{v} = \text{অপসারণ বেগ}$ & মিটার প্রতি সেকেন্ড ($\text{m s}^{-1}$) \\ \cline{3-4} 
\textbf{১.} & হাবল বিধি অনুসারে অপসারণ বেগ, $\text{v} = \text{HR}$ & $\text{H} = \text{হাবল ধ্রুবক}$ & কিলোমিটার প্রতি সেকেন্ড ($\text{km s}^{-1}$) \\ \cline{3-4} 
 & & $\text{R} = \text{দূরত্ব}$ & মিটার ($\text{m}$) \\ \hline
\textbf{২.} & ক্রান্তিক ঘনত্ব, $\rho_\text{c} = \frac{3\text{H}^2}{8\pi\text{G}}$ & $\text{H} = \text{হাবল ধ্রুবক}$ & কিলোমিটার প্রতি সেকেন্ড ($\text{km s}^{-1}$) \\ \cline{3-4} 
 & & $\text{G} = \text{মহাকর্ষীয় ধ্রুবক}$ & $\text{Nm}^2\text{kg}^{-2}$ \\ \hline
 & ঘনত্ব, $\rho = \frac{\text{M}}{\text{V}} = \frac{\text{M}}{\frac{4}{3}\pi\text{R}^3}$ & $\text{M} = \text{গ্রহ বা নক্ষত্রের ভর}$ & কিলোগ্রাম ($\text{kg}$) \\ \cline{3-4} 
\textbf{৩.} & & $\text{V} = \text{আয়তন}$ & ঘনমিটার ($\text{m}^3$) \\ \hline
\textbf{৪.} & শোয়ার্জশিল্ড ব্যাসার্ধ, $\text{R}_\text{s} = \frac{2\text{GM}}{\text{c}^2}$ & $\text{M} = \text{নক্ষত্রের ভর}$ & কিলোগ্রাম ($\text{kg}$) \\ \cline{3-4} 
 & & $\text{c} = \text{আলোর বেগ}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৫.} & কৃত্রিম উপগ্রহের বেগ, $\text{v} = \sqrt{\frac{\text{GM}}{\text{r}}} = \sqrt{\frac{\text{GM}}{\text{R}+\text{h}}}$ & $\text{M} = \text{পৃথিবীর ভর}$ & কিলোগ্রাম ($\text{kg}$) \\ \cline{3-4} 
 & & $\text{R} = \text{পৃথিবীর ব্যাসার্ধ}$ & মিটার ($\text{m}$) \\ \hline
\textbf{৬.} & কৃত্রিম উপগ্রহের আবর্তনকাল, & $\text{h} = \text{পৃথিবীর পৃষ্ঠ হতে উপগ্রহের উচ্চতা}$ & মিটার ($\text{m}$) \\ \cline{3-4} 
 & \centerline{$\text{T} = 2\pi(\text{R}+\text{h})\sqrt{\frac{\text{R}+\text{h}}{\text{GM}}}$} & $\text{M} = \text{পৃথিবীর ভর}$ & কিলোগ্রাম ($\text{kg}$) \\ \hline
\end{tabular}
}

\bigskip
\bigskip

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

with open("physics_fixed.tex", "w", encoding="utf-8") as fh:
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
               "physics_fixed.tex >logs/xelatex_pass" + str(i) + ".log 2>&1")
    passes.append(code)
    if code != 0:
        raise RuntimeError("xelatex failed; see logs/xelatex_pass" + str(i) + ".log")

print("PDF ready:", os.path.exists("physics_fixed.pdf"), "passes:", passes)
