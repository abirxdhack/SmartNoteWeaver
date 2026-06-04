import subprocess, os, shutil

tex_content = r'''\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[margin=1.0cm, top=1.2cm, bottom=1.0cm]{geometry}
\usepackage{multicol}
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
\usetikzlibrary{arrows.meta,calc,shadings,decorations.pathmorphing,3d,perspective}
\setlength{\arrayrulewidth}{0.3pt}
\setlength{\tabcolsep}{1.5pt}
\renewcommand{\arraystretch}{1.13}
\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}
\pagestyle{empty}
\setlength{\emergencystretch}{25pt}
\hbadness=10000
\vbadness=10000
\sloppy
\raggedcolumns
\tolerance=9999
\emergencystretch=25pt

\defaultfontfeatures{Ligatures=TeX}
\newfontfamily\lat[Path=/usr/share/fonts/truetype/dejavu/,UprightFont=DejaVuSerif,BoldFont=DejaVuSerif-Bold,Extension=.ttf,Ligatures=TeX]{DejaVuSerif}
\newfontfamily\bn{NotoSerifBengali-Regular.ttf}[Path=./, Script=Bengali, BoldFont=NotoSerifBengali-Bold.ttf, ItalicFont=NotoSerifBengali-Regular.ttf, BoldItalicFont=NotoSerifBengali-Bold.ttf, Renderer=HarfBuzz, AutoFakeSlant=0.18]

\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{85,85,85}
\definecolor{p1bg}{RGB}{20,60,120}
\definecolor{p2bg}{RGB}{0,0,0}

\newcommand{\B}[1]{{\bn #1}}
\newcommand{\LAT}[1]{{\lat #1}}

\newcommand{\chsec}[1]{%
  \vspace{2pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par
}

\newcommand{\chsub}[2]{%
  \vspace{2pt}%
  \noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \bfseries\footnotesize\color{white}\;#1 \B{#2}%
  }}%
  \vspace{1pt}\par
}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.8pt}

\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\setlist[itemize]{nosep, leftmargin=0pt, topsep=0pt, label={}, itemsep=0pt, parsep=0pt}
\newcommand{\itm}[1]{\textbf{{\lat #1.}}\;}
\newcommand{\sub}[1]{\textbf{({\lat #1})}\;}

\begin{document}

\begin{center}
\noindent
{\bn\Large\bfseries ১ম পত্রের সমস্ত সংগা ও সুত্রবলী}\hfill
{\normalfont\small \textbf{By Abir Arafat Chawdhury [Introvert's Area]}}
\vspace{3pt}
\end{center}

\begin{multicols}{2}

\noindent\colorbox{p1bg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{পদার্থবিজ্ঞান প্রথম পত্র}}}
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

\itm{1} \textbf{\B{শতকরা ক্রটি:}} {\lat $= \dfrac{\text{\B{প্রকৃত মান}} - \text{\B{পরীক্ষালব্ধ মান}}}{\text{\B{প্রকৃত মান}}} \times 100\%$}

\itm{2} \textbf{\B{গড় মান:}} {\lat $A = \dfrac{x_1 + x_2 + x_3 + \cdots + x_n}{n}$}

\itm{3} \textbf{\B{গড় বিচ্যুতি বা গড় ভুল:}} {\lat $d = \dfrac{d_1 + d_2 + d_3 + \cdots + d_n}{n}$}

\itm{4} \textbf{\B{প্রমাণ বিচ্যুতি:}} {\lat $D = \dfrac{\sqrt{d_1^2 + d_2^2 + d_3^2 + \cdots + d_n^2}}{n} = \dfrac{\sqrt{\Sigma d^2}}{n}$}

\chsec{অধ্যায়-২: ভেক্টর}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{লব্ধি:}} {\lat $R = \sqrt{P^2 + Q^2 + 2PQ\cos\alpha}$};\; {\lat $\tan\theta = \dfrac{Q\sin\alpha}{P + Q\cos\alpha}$}

\itm{2} \textbf{\B{একক ভেক্টর:}} {\lat $\hat{a} = \dfrac{\vec{A}}{A}$}
\par\noindent{\lat $\vec{A} + \vec{B} = \hat{i}(A_x + B_x) + \hat{j}(A_y + B_y) + \hat{k}(A_z + B_z)$}

\itm{3} \textbf{\B{ডট গুণফল:}} {\lat $\vec{A}\cdot\vec{B} = AB\cos\theta$}
\par\noindent{\lat $\vec{A}\cdot\vec{B} = A_x B_x + A_y B_y + A_z B_z$}

\itm{4} \textbf{\B{ক্রস গুণফল:}} {\lat $\vec{A}\times\vec{B} = AB\sin\theta\,\hat{a}$}
\par\noindent{\lat $\vec{A}\times\vec{B} = \begin{vmatrix}\hat{i} & \hat{j} & \hat{k}\\ A_x & A_y & A_z\\ B_x & B_y & B_z\end{vmatrix}$}

\itm{5} \textbf{\B{অবস্থান ভেক্টর:}} {\lat $\vec{r} = x\hat{i} + y\hat{j} + z\hat{k}$};\; {\lat $|\vec{r}| = \sqrt{x^2+y^2+z^2}$}

\itm{6} \textbf{\B{$\vec{A}$-এর উপর $\vec{B}$-এর লম্ব অভিক্ষেপ:}} {\lat $B\cos\theta = \dfrac{\vec{A}\cdot\vec{B}}{A}$}

\itm{7} \textbf{\B{$\vec{B}$-এর উপর $\vec{A}$-এর লম্ব অভিক্ষেপ:}} {\lat $A\cos\theta = \dfrac{\vec{A}\cdot\vec{B}}{B}$}

\itm{8} {\lat $R_{\max} = P + Q$},\; {\lat $R_{\min} = P - Q$}

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

\chsec{অধ্যায়-৪: নিউটনিয়ান বলবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{ভরবেগ:}} {\lat $\vec{P} = m\vec{v}$}

\itm{2} \textbf{\B{বল:}} {\lat $\vec{F} = m\vec{a}$}

\itm{3} \textbf{\B{ঘাতবল:}} {\lat $\vec{J} = m\vec{v} - m\vec{v_0}$}

\itm{4} {\lat $MV = -mv$}

\itm{5} \textbf{\B{ভরবেগের নিত্যতা:}} {\lat $m_1\vec{v_{1i}} + m_2\vec{v_{2i}} = m_1\vec{v_{1f}} + m_2\vec{v_{2f}}$}

\itm{6} \textbf{\B{রকেটের গতির সমীকরণ:}} {\lat $a = \left(\dfrac{v_r}{m}\times\dfrac{\Delta m}{\Delta t} - g\right)$}

\itm{7} \textbf{\B{টর্ক:}} {\lat $\vec{\tau} = \vec{r}\times\vec{F}$}

\itm{8} \textbf{\B{ঘন্ব:}} {\lat $C = F\times d$}

\itm{9} \textbf{\B{গতিশক্তি:}} {\lat $E_k = \tfrac{1}{2}I\omega^2$}

\itm{10} \textbf{\B{জড়তার ভ্রামক:}} {\lat $I = \Sigma mr^2$}

\itm{11} \textbf{\B{জড়তার ভ্রামক:}} {\lat $I = MK^2$}

\itm{12} \textbf{\B{কৌণিক ভরবেগ:}} {\lat $L = I\omega$}

\itm{13} \textbf{\B{কৌণিক ভরবেগ:}} {\lat $\vec{L} = \vec{r}\times\vec{P}$}

\itm{14} \textbf{\B{টর্ক:}} {\lat $\tau = I\alpha$}

\itm{15} \textbf{\B{কেন্দ্রমুখী বল:}} {\lat $F_c = \dfrac{mv^2}{r} = m\omega^2 r$}

\itm{16} \textbf{\B{রাস্তার বা আবর্তীর নতিকোণ:}} {\lat $\tan\theta = \dfrac{v^2}{rg}$}

\itm{17} \textbf{\B{অভিলাষ উপাদান:}} {\lat $I_z = I_x + I_y$}

\itm{18} \textbf{\B{জড়তার ভ্রামকের সমান্তরাল উপাদান:}} {\lat $I_{AB} = I_{CD} + Mh^2$}

\chsub{}{নিউটনের গতিসূত্র}

\B{১৬৮৭ খ্রিষ্টাব্দে বিখ্যাত বিজ্ঞানী স্যার আইজ্যাক নিউটন ভর, গতি ও বেগের মধ্যে সম্পর্ক সূচক তিনটি সূত্র প্রতিপাদন করেন।}

\textbf{\B{১ম সূত্র:}} \B{বাহ্যিক বল প্রয়োগে বস্তু অবস্থার পরিবর্তন করতে বাধা না পেলে স্থির বস্তু চিরকাল স্থিরই থাকবে এবং গতিশীল বস্তু সমবেগে সরলপথে চলতে থাকবে।}

\textbf{\B{২য় সূত্র:}} \B{বস্তুর ভরবেগের পরিবর্তনের হার তার ওপর প্রযুক্ত বলের সমানুপাতিক এবং বল যেদিকে ক্রিয়া করে বস্তুর ভরবেগের পরিবর্তনও সেদিক ঘটে।}

\textbf{\B{৩য় সূত্র:}} \B{প্রতিটি ক্রিয়ার একটি সমান ও বিপরীত প্রতিক্রিয়া আছে।}

\chsub{}{ভরবেগের নিত্যতা সূত্র}

\B{"একাধিক বস্তুতে ক্রিয়া ও প্রতিক্রিয়া বল ছাড়া ভিন্ন কোনো বল না থাকলে যে কোনো একদিকে এদের মোট ভরবেগের কোনো পরিবর্তন ঘটে না।" এর নাম ভরবেগের নিত্যতা সূত্র। একে ভরবেগের সংরক্ষণ নিয়মও বলা হয়।}

\chsub{}{বলের মিত্রভুজ সূত্র}

\B{"যদি কোনো বস্তুর উপর একই সময়ে ক্রিয়ারত তিনটি বলের মান ও দিক একটি মিত্রভুজের তিনটি বাহু দ্বারা একইক্রমে সূচিত হয়, তবে এদের লব্ধি শূন্য হবে।"}

\chsub{}{নিউটনের মহাকর্ষ সূত্র}

\B{সপ্তদশ শতাব্দীতে বিখ্যাত বিজ্ঞানী স্যার আইজ্যাক নিউটন আপেলের পতন ও গ্রহ-উপগ্রহের গতি পর্যবেক্ষণ করে সূত্র প্রদান করেন।}

\B{"এই মহাবিশ্বের যেকোনো দুটি বস্তুকণা পরস্পরকে এদের সংযোজক সরলরেখা বরাবর একটি বল দ্বারা আকর্ষণ করে। এই আকর্ষণ বলের মান বস্তুকণা দুটির ভরের গুণফলের সমানুপাতিক এবং এদের মধ্যবর্তী দূরত্বের বর্গের ব্যস্তানুপাতিক।"}

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

\chsec{অধ্যায়-৭: পদার্থের গাঠনিক ধর্ম}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{ইয়ং-এর গুণাঙ্ক:}} {\lat $Y = \dfrac{FL}{Al}$}

\itm{2} \textbf{\B{ইয়ং-এর গুণাঙ্ক:}} {\lat $Y = \dfrac{MgL}{\pi r^2 l}$}

\itm{3} \textbf{\B{কাজ:}} {\lat $W = \tfrac{1}{2}\dfrac{YAl^2}{L}$}

\itm{4} \textbf{\B{একক আয়তনে কৃতকাজ:}} {\lat $= \tfrac{1}{2}\times\text{\B{পীড়ন}}\times\text{\B{বিকৃতি}} = \tfrac{1}{2}\times\dfrac{YAl^2}{L}$}

\itm{5} \textbf{\B{পয়সনের অনুপাত:}} {\lat $\sigma = \dfrac{\text{\B{পার্শ্ব বিকৃতি}}}{\text{\B{দৈর্ঘ্য বিকৃতি}}}$}

\itm{6} \textbf{\B{দৃঢ়তার গুণাঙ্ক:}} {\lat $n = \dfrac{F}{A\theta}$}

\itm{7} \textbf{\B{আয়তন গুণাঙ্ক:}} {\lat $K = \dfrac{\text{\B{আয়তন পীড়ন}}}{\text{\B{আয়তন বিকৃতি}}}$}

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
\noindent\B{বা, $\dfrac{\text{পীড়ন}}{\text{বিকৃতি}}$ = ধ্রুবক}

\chsub{}{পয়সনের অনুপাত}

\B{বস্তুর পার্শ্ব বিকৃতি ও দৈর্ঘ্য বিকৃতির অনুপাত একটি ধ্রুব রাশি। অর্থাৎ $\dfrac{\text{পার্শ্ব বিকৃতি}}{\text{দৈর্ঘ্য বিকৃতি}}$ = ধ্রুবক। এই ধ্রুবককে সিগমা ($\sigma$) দ্বারা প্রকাশ করা হয়। এটি পয়সনের অনুপাত।}

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

\itm{1} \textbf{\B{দোলনকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{E}{g}}$}

\itm{2} \textbf{\B{অভিকর্ষজ তুরণ:}} {\lat $g = 4\pi^2\dfrac{l}{T^2}$}

\itm{3} {\lat $F = -kx$}

\itm{4} \textbf{\B{সরণ:}} {\lat $x = A\sin\omega t$}

\itm{5} \textbf{\B{সরণ:}} {\lat $x = A\sin(\omega t + \delta)$}

\itm{6} \textbf{\B{অভিকর্ষজ তুরণ:}} {\lat $g = \dfrac{GM}{R^2}$}

\itm{7} \textbf{\B{তুরণ:}} {\lat $a = -\left(\dfrac{2\pi}{T}\right)^2\times\text{\B{সরণ}}$}

\itm{8} \textbf{\B{দোলকাল:}} {\lat $T = 2\pi\sqrt{\dfrac{m}{k}}$}

\itm{9} \textbf{\B{বেগ:}} {\lat $v = \omega A\cos(\omega t+\delta) = \omega\sqrt{A^2-x^2}$}

\itm{10} {\lat $V_{\max} = \omega A$}

\itm{11} \textbf{\B{গতিশক্তি:}} {\lat $E_k = \tfrac{1}{2}kA^2\cos^2(\omega t+\delta)$}

\itm{12} \textbf{\B{স্থিতিশক্তি:}} {\lat $U = \tfrac{1}{2}kA^2\sin^2(\omega t+\delta) = \tfrac{1}{2}kx^2$}

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
\B{M ভরের ও L দৈর্ঘ্যের সরু ও সুষম দণ্ডের ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=gray!12,rounded corners=1.4pt] (-2.2,-0.13) rectangle (2.2,0.13);\draw (-2.2,0) circle (0.13);\draw (2.2,0) circle (0.13);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-2.2,-0.55)--(2.2,-0.55) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{12}ML^2$} & {\lat $K=\dfrac{L}{\sqrt{12}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের সরু ও সুষম দণ্ডের প্রান্তবিন্দুগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=gray!12,rounded corners=1.4pt] (0,-0.13) rectangle (4.1,0.13);\draw (0,0) circle (0.13);\draw (4.1,0) circle (0.13);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (0,-0.55)--(4.1,-0.55) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\end{tikzpicture} & {\lat $I=\dfrac{1}{3}ML^2$} & {\lat $K=\dfrac{L}{\sqrt{3}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের ও R ব্যাসার্ধের নিরেট সিলিন্ডারের নিজ অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!12] (-1.8,-0.45)--(1.8,-0.45);\draw[fill=gray!12] (-1.8,0.45)--(1.8,0.45);\draw[fill=gray!12] (-1.8,0) ellipse (0.28 and 0.45);\draw[fill=gray!12] (1.8,0) ellipse (0.28 and 0.45);\draw[dashed,->] (-2.35,0)--(2.45,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[->,thin] (1.8,0)--(1.8,0.45) node[midway,right,font=\tiny]{$R$};\draw[<->] (-1.8,-0.75)--(1.8,-0.75) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\end{tikzpicture} & {\lat $I=\dfrac{1}{2}MR^2$} & {\lat $K=\dfrac{R}{\sqrt{2}}$} \\
\hline
\B{M ভরের, $R_1$ অন্তর্ব্যাসার্ধ ও $R_2$ বহির্ব্যাসার্ধবিশিষ্ট ফাঁপা সিলিন্ডারের নিজ অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw (-1.8,-0.55)--(1.8,-0.55) (-1.8,0.55)--(1.8,0.55);\draw (-1.8,0) ellipse (0.33 and 0.55);\draw (1.8,0) ellipse (0.33 and 0.55);\draw (-1.8,0) ellipse (0.18 and 0.31);\draw (1.8,0) ellipse (0.18 and 0.31);\draw[dashed,->] (-2.35,0)--(2.45,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[<-,thin,shorten <=1pt] (-1.8,0.55)--(-1.25,0.7) node[right,font=\tiny]{$R_2$};\draw[<-,thin,shorten <=1pt] (-1.8,0.31)--(-1.25,0.18) node[right,font=\tiny]{$R_1$};\end{tikzpicture} & {\lat $I=\dfrac{1}{2}M(R_1^2+R_2^2)$} & {\lat $K=\sqrt{\dfrac{R_1^2+R_2^2}{2}}$} \\
\hline
\B{M ভরের ও L দৈর্ঘ্যের ও R ব্যাসার্ধের নিরেট সিলিন্ডারের দৈর্ঘ্যের সঙ্গে লম্ব ভরকেন্দ্রগামী অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!12] (-1.8,-0.45)--(1.8,-0.45);\draw[fill=gray!12] (-1.8,0.45)--(1.8,0.45);\draw[fill=gray!12] (-1.8,0) ellipse (0.28 and 0.45);\draw[fill=gray!12] (1.8,0) ellipse (0.28 and 0.45);\draw[dashed,->] (0,-0.95)--(0,0.95) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.8,-0.75)--(1.8,-0.75) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$L$};\draw[->,thin] (2.15,0)--(2.15,0.45) node[midway,right,font=\tiny]{$R$};\end{tikzpicture} & {\lat $I=\dfrac{1}{4}MR^2+\dfrac{1}{12}ML^2$} & {\lat $K=\sqrt{\dfrac{R^2}{4}+\dfrac{L^2}{12}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!16] (0,0) ellipse (1.7 and 0.48);\draw[dashed,->] (0,-1.12)--(0,1.18) node[above,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.7,0) node[right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{2}MR^2$} & {\lat $K=\dfrac{R}{\sqrt{2}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির পৃষ্ঠের অভিলম্বভাবে গমনকারী স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!16,rotate=14] (0,0) ellipse (1.7 and 0.58);\draw[dashed,->] (-1.9,-1.0)--(-1.9,1.1) node[above,font=\tiny]{\B{অক্ষ}};\draw[->,rotate=14] (0,0)--(1.7,0) node[right,font=\tiny]{$R$};\end{tikzpicture} & {\lat $I=\dfrac{3}{2}MR^2$} & {\lat $K=\sqrt{\dfrac{3}{2}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা বৃত্তাকার চাকতির যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!16] (0,0) ellipse (1.65 and 0.48);\draw[dashed,->] (-1.9,0)--(1.95,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[->] (0,0)--(1.65,0) node[above right,font=\tiny]{$R$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{4}MR^2$} & {\lat $K=\dfrac{R}{2}$} \\
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
\B{M ভরের, a দৈর্ঘ্যের ও b প্রস্থের আয়তাকার পাতের ভরকেন্দ্রগামী লম্ব-অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!13] (-1.65,-0.85) rectangle (1.65,0.85);\draw[dashed,->] (0,-1.15)--(0,1.15) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.65,-1.05)--(1.65,-1.05) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$a$};\draw[<->] (1.85,-0.85)--(1.85,0.85) node[midway,right,font=\tiny]{$b$};\fill (0,0) circle (1.2pt);\end{tikzpicture} & {\lat $I=\dfrac{1}{12}M(a^2+b^2)$} & {\lat $K=\sqrt{\dfrac{a^2+b^2}{12}}$} \\
\hline
\B{M ভরের, a দৈর্ঘ্যের ও b প্রস্থের আয়তাকার পাতের প্রস্থের সমান্তরাল ভরকেন্দ্রগামী অক্ষের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[fill=gray!13] (-1.65,-0.85) rectangle (1.65,0.85);\draw[dashed,->] (-1.9,0)--(1.95,0) node[right,font=\tiny]{\B{অক্ষ}};\draw[<->] (-1.65,-1.05)--(1.65,-1.05) node[midway,fill=white,inner sep=0.2pt,font=\tiny]{$a$};\end{tikzpicture} & {\lat $I=\dfrac{1}{12}Ma^2$} & {\lat $K=\dfrac{a}{\sqrt{12}}$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের নিরেট গোলকের যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\shade[ball color=gray!28] (0,0) circle (1.05);\draw[dashed,->] (0,-1.35)--(0,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{2}{5}MR^2$} & {\lat $K=\sqrt{\dfrac{2}{5}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের নিরেট গোলকের স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\shade[ball color=gray!28] (0,0) circle (1.05);\draw[dashed,->] (-1.27,-1.35)--(-1.27,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{7}{5}MR^2$} & {\lat $K=\sqrt{\dfrac{7}{5}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা ফাঁপা গোলকের যেকোনো ব্যাসের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=gray!8] (0,0) circle (1.05);\draw[dashed,->] (0,-1.35)--(0,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{2}{3}MR^2$} & {\lat $K=\sqrt{\dfrac{2}{3}}R$} \\
\hline
\B{M ভরের ও R ব্যাসার্ধের পাতলা ফাঁপা গোলকের স্পর্শকের সাপেক্ষে} & \begin{tikzpicture}[scale=0.34,baseline=-2pt,>=Stealth,line cap=round]\draw[very thick,fill=gray!8] (0,0) circle (1.05);\draw[dashed,->] (-1.27,-1.35)--(-1.27,1.35) node[above,font=\tiny]{\B{অক্ষ}};\draw[<->] (1.32,-1.05)--(1.32,1.05) node[midway,right,font=\tiny]{$2R$};\draw (0,0) ellipse (1.05 and 0.28);\end{tikzpicture} & {\lat $I=\dfrac{5}{3}MR^2$} & {\lat $K=\sqrt{\dfrac{5}{3}}R$} \\
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

\end{multicols}

\vspace{4pt}
\begin{center}
\noindent
{\bn\large\bfseries একনজরে পদার্থবিজ্ঞান দ্বিতীয় পত্র — সূত্র, সংজ্ঞা ও ধ্রুবকসমূহ}\hfill
{\normalfont\small \textbf{By Abir Arafat Chawdhury [Introvert's Area]}}
\vspace{3pt}
\end{center}

\begin{multicols}{2}

\noindent\colorbox{p2bg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{পদার্থবিজ্ঞান দ্বিতীয় পত্র}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: তাপগতিবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তাপমাত্রা স্কেলের রূপান্তর:}} {\lat $\dfrac{C}{5}=\dfrac{F-32}{9}=\dfrac{K-273}{5}=\dfrac{R-492}{9}=\dfrac{\text{Ra}-32}{4}$}
\begin{itemize}
    \item[] {\lat $C,F,K,R,\text{Ra}$} = \B{সেলসিয়াস, ফারেনহাইট, কেলভিন, রোমার, র‍্যাঙ্কিন স্কেলে তাপমাত্রা}
    \item[] {\lat $K=C+273$;\; $R(^\circ\text{Rk})=F+459.67$;\; $1^\circ\text{C}=\tfrac{9}{5}{}^\circ$F}
\end{itemize}

\itm{2} \textbf{\B{থার্মোমেট্রিক ধর্ম থেকে তাপমাত্রা,}} {\lat $\theta=\dfrac{X-X_0}{X_{100}-X_0}\times100$}
\begin{itemize}
    \item[] {\lat $X,X_0,X_{100}$} = \B{যেকোনো / বরফবিন্দু / বাষ্পবিন্দু তাপমাত্রায় থার্মোমেট্রিক ধর্মের মান}
    \item[] \B{রোধ থার্মোমিটার:} {\lat $\theta=\dfrac{R_\theta-R_0}{R_{100}-R_0}\times100$}
    \item[] \B{বরফ–বাষ্পের গলনে:} {\lat $\theta=\dfrac{l_\theta-l_{\rm ice}}{l_{\rm steam}-l_{\rm ice}}\times100$}
\end{itemize}

\itm{3} \textbf{\B{গে-লুসাক / রেনোর সূত্র (স্থির আয়তন গ্যাস থার্মোমিটার),}} {\lat $T=\dfrac{P_T}{P_{\rm tr}}\times273.16$ K}
\begin{itemize}
    \item[] {\lat $P_T$} = \B{পরিমাপ্য তাপমাত্রায় গ্যাসের চাপ;}\; {\lat $P_{\rm tr}$} = \B{পানির ত্রৈধবিন্দুতে চাপ}
\end{itemize}

\itm{4} \textbf{\B{তাপ ও তাপ ধারণক্ষমতা,}} {\lat $Q=mc\Delta T,\; C=mc,\; Q_{\rm latent}=mL,\; W=JQ$}
\begin{itemize}
    \item[] {\lat $Q$} = \B{তাপশক্তি} {\lat [J]};\; {\lat $m$} = \B{ভর} {\lat [kg]}
    \item[] {\lat $c,s$} = \B{আপেক্ষিক তাপ} {\lat [J/(kg$\cdot$K)]};\; {\lat $C$} = \B{তাপ ধারণক্ষমতা}
    \item[] {\lat $\Delta T$} = \B{তাপমাত্রার পরিবর্তন};\; {\lat $L$} = \B{সুপ্ততাপ};\; {\lat $J=4.2$ J/cal} = \B{যান্ত্রিক সমতা}
\end{itemize}

\itm{5} \textbf{\B{গ্যাসের সূত্রসমূহ:}}
\begin{itemize}
    \item[] \B{বয়েল:} {\lat $P_1V_1=P_2V_2$};\; \B{চার্লস:} {\lat $V_1/T_1=V_2/T_2$}
    \item[] \B{চাপের সূত্র:} {\lat $P_1/T_1=P_2/T_2$};\; \B{সম্মিলিত:} {\lat $P_1V_1/T_1=P_2V_2/T_2$}
    \item[] \B{আদর্শ গ্যাস:} {\lat $PV=nRT=NkT$}
    \item[] \B{ডালটনের আংশিক চাপ:} {\lat $P=P_1+P_2+\cdots$}
    \item[] \B{মিশ্রণ:} {\lat $PV=\bigl(\tfrac{m_1}{M_1}+\tfrac{m_2}{M_2}\bigr)RT$}
    \item[] \B{অ্যাভোগাড্রো:} \B{সমান} {\lat $P,T$} \B{তে সমান আয়তনে সমান সংখ্যক অণু}
    \item[] {\lat $P$} = \B{চাপ};\; {\lat $V$} = \B{আয়তন};\; {\lat $T$} = \B{পরম তাপমাত্রা} {\lat [K]}
    \item[] {\lat $n$} = \B{মোল সংখ্যা};\; {\lat $R=8.314$ J/mol$\cdot$K};\; {\lat $N$} = \B{অণু সংখ্যা};\; {\lat $k=1.38\times10^{-23}$ J/K}
\end{itemize}

\itm{6} \textbf{\B{গ্যাসের গতিতত্ত্ব,}} {\lat $P=\tfrac{1}{3}\rho\overline{c^2}=\tfrac{1}{3}\dfrac{Nm}{V}\overline{c^2}$}
\begin{itemize}
    \item[] {\lat $c_{\rm rms}=\sqrt{\dfrac{3RT}{M}}=\sqrt{\dfrac{3kT}{m}}=\sqrt{\dfrac{3P}{\rho}}$}
    \item[] {\lat $\bar c=\sqrt{\dfrac{8RT}{\pi M}}=\sqrt{\dfrac{8kT}{\pi m}}$};\; {\lat $c_p=\sqrt{\dfrac{2RT}{M}}=\sqrt{\dfrac{2kT}{m}}$}
    \item[] {\lat $c_p:\bar c:c_{\rm rms}=\sqrt 2:\sqrt{8/\pi}:\sqrt 3$}
    \item[] \B{গড় গতিশক্তি:} {\lat $E_k=\tfrac{3}{2}kT$};\; \B{$f$ স্বাধীনতা মাত্রায়:} {\lat $E=\tfrac{f}{2}kT$}
    \item[] \B{গড় মুক্তপথ:} {\lat $\lambda=\dfrac{1}{\sqrt 2\,\pi d^2 n}=\dfrac{kT}{\sqrt 2\,\pi d^2 P}$};\; {\lat $N_A=6.022\times10^{23}$ mol$^{-1}$}
    \item[] {\lat $\rho$} = \B{ঘনত্ব};\; {\lat $M$} = \B{মোলার ভর};\; {\lat $d$} = \B{অণু ব্যাস};\; {\lat $f$} = \B{স্বাধীনতার মাত্রা}
\end{itemize}

\itm{7} \textbf{\B{তাপগতিবিদ্যার সূত্র:}}
\begin{itemize}
    \item[] \B{০-তম:} \B{তাপীয় সাম্য সকর্মক (transitive)}
    \item[] \B{১ম:} {\lat $\Delta Q=\Delta U+\Delta W$}
    \item[] \B{২য়:} \B{বদ্ধ চক্রে} {\lat $\oint dQ/T\le0$} \B{(ক্লসিয়াস/কেলভিন বিবৃতি)}
    \item[] \B{৩য়:} {\lat $T\to0$\,K} \B{তে এন্ট্রপি} {\lat $\to0$}
    \item[] {\lat $\Delta U$} = \B{অভ্যন্তরীণ শক্তির পরিবর্তন};\; {\lat $\Delta W$} = \B{কাজ}
\end{itemize}

\itm{8} \textbf{\B{বিভিন্ন প্রক্রিয়ায় কাজ:}}
\begin{itemize}
    \item[] \B{সমতাপীয়:} {\lat $W=nRT\ln\dfrac{V_2}{V_1}=Q$}
    \item[] \B{সমচাপীয়:} {\lat $W=P\Delta V=nR\Delta T$}
    \item[] \B{রুদ্ধতাপীয়:} {\lat $PV^\gamma=\text{const};\; TV^{\gamma-1}=\text{const};\; T^\gamma P^{1-\gamma}=\text{const}$}
    \item[] \B{রুদ্ধতাপীয় কাজ:} {\lat $W=\dfrac{P_1V_1-P_2V_2}{\gamma-1}$}
    \item[] \B{সমআয়তনীয়:} {\lat $W=0,\;\Delta Q=nC_v\Delta T$}
    \item[] \B{প্রত্যাগামী চক্র:} {\lat $\dfrac{Q_1}{T_1}=\dfrac{Q_2}{T_2}$}
    \item[] {\lat $\gamma=C_p/C_v$} = \B{আপেক্ষিক তাপের অনুপাত}
\end{itemize}

\itm{9} \textbf{\B{মোলার আপেক্ষিক তাপ:}}
\begin{itemize}
    \item[] \B{মেয়ার:} {\lat $C_p-C_v=R$}
    \item[] \B{একপরমাণুক:} {\lat $C_v=\tfrac{3}{2}R,\;C_p=\tfrac{5}{2}R,\;\gamma=5/3$}
    \item[] \B{দ্বিপরমাণুক:} {\lat $C_v=\tfrac{5}{2}R,\;C_p=\tfrac{7}{2}R,\;\gamma=7/5$}
    \item[] \B{ত্রিপরমাণুক:} {\lat $C_v=3R,\;C_p=4R,\;\gamma=4/3$}
    \item[] \B{অভ্যন্তরীণ শক্তি:} {\lat $\Delta U=\tfrac{f}{2}nR\Delta T$}
\end{itemize}

\itm{10} \textbf{\B{কার্নো ইঞ্জিন \& হিট পাম্প:}}
\begin{itemize}
    \item[] \B{দক্ষতা:} {\lat $\eta=1-\dfrac{T_2}{T_1}=\dfrac{W}{Q_1}=\dfrac{Q_1-Q_2}{Q_1}$}
    \item[] \B{রেফ্রিজারেটর COP:} {\lat $\beta=\dfrac{Q_2}{W}=\dfrac{T_2}{T_1-T_2}$}
    \item[] \B{হিট পাম্প:} {\lat $\beta'=\dfrac{Q_1}{W}=\dfrac{T_1}{T_1-T_2}=1+\beta$}
\end{itemize}

\itm{11} \textbf{\B{এন্ট্রপি,}} {\lat $\Delta S=\dfrac{\Delta Q}{T}$}
\begin{itemize}
    \item[] \B{প্রত্যাগামী:} {\lat $\oint dQ/T=0$};\; \B{অপ্রত্যাগামী:} {\lat $\Delta S>0$}
\end{itemize}

\itm{12} \textbf{\B{তাপ পরিবহন ও বিকিরণ:}}
\begin{itemize}
    \item[] \B{পরিবহন:} {\lat $\dfrac{Q}{t}=k_{\rm th}A\dfrac{\Delta T}{l}$}
    \item[] \B{স্টেফান-বোলৎজম্যান:} {\lat $E=\sigma T^4$},\; {\lat $\sigma=5.67\times10^{-8}$ W/m$^2$K$^4$}
    \item[] \B{নিউটনের শীতলীকরণ:} {\lat $\dfrac{dT}{dt}=-k(T-T_0)$}
    \item[] \B{ভিয়েনের সূত্র:} {\lat $\lambda_{\max}T=2.898\times10^{-3}$ m$\cdot$K}
    \item[] \B{কার্শফ:} \B{ভালো শোষক $=$ ভালো বিকীর্ণক}
    \item[] {\lat $k_{\rm th}$} = \B{তাপ পরিবাহিতা};\; {\lat $A$} = \B{ক্ষেত্রফল};\; {\lat $l$} = \B{পুরুত্ব}
\end{itemize}

\chsec{অধ্যায়-২: স্থির তড়িৎ}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{কুলম্বের সূত্র,}} {\lat $F=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}=9\times10^9\dfrac{q_1q_2}{r^2}$}
\begin{itemize}
    \item[] \B{মাধ্যমে:} {\lat $F=\dfrac{1}{4\pi\varepsilon_0\varepsilon_r}\dfrac{q_1q_2}{r^2}$};\; {\lat $\varepsilon_r=\varepsilon/\varepsilon_0$}
    \item[] {\lat $F$} = \B{কুলম্ব বল} {\lat [N]};\; {\lat $q_1,q_2$} = \B{চার্জ} {\lat [C]};\; {\lat $r$} = \B{দূরত্ব} {\lat [m]}
    \item[] {\lat $\varepsilon_0=8.85\times10^{-12}$ F/m};\; {\lat $\varepsilon_r,K$} = \B{মাধ্যমের আপেক্ষিক ডাইইলেক্ট্রিক ধ্রুবক}
\end{itemize}

\itm{2} \textbf{\B{তড়িৎ প্রাবল্য,}} {\lat $E=F/q_0=kQ/r^2$}
\begin{itemize}
    \item[] \B{অসীম তার:} {\lat $E=\dfrac{\lambda}{2\pi\varepsilon_0 r}$};\; \B{এক পাত:} {\lat $E=\dfrac{\sigma}{2\varepsilon_0}$}
    \item[] \B{দুই বিপরীত পাত:} {\lat $E=\dfrac{\sigma}{\varepsilon_0}$}
    \item[] \B{পরিবাহী গোলকপৃষ্ঠ:} {\lat $E=\dfrac{Q}{4\pi\varepsilon_0 r^2}$}, \B{ভিতরে} {\lat $E=0$}
    \item[] \B{বিভব-ক্ষেত্র সম্পর্ক:} {\lat $\vec E=-\vec\nabla V$}
    \item[] {\lat $\lambda$} = \B{রৈখিক চার্জ ঘনত্ব};\; {\lat $\sigma$} = \B{পৃষ্ঠ চার্জ ঘনত্ব}
\end{itemize}

\itm{3} \textbf{\B{তড়িৎ বিভব,}} {\lat $V=W/q=kQ/r$}
\begin{itemize}
    \item[] {\lat $V_{AB}=\dfrac{W_{AB}}{q}=\dfrac{V_A-V_B}{d}$};\; {\lat $E=-dV/dx$}
    \item[] {\lat $V$} = \B{বিভব} {\lat [V]};\; {\lat $W$} = \B{কাজ} {\lat [J]}
\end{itemize}

\itm{4} \textbf{\B{তড়িৎ দ্বিমেরু,}} {\lat $p=q\cdot 2l$}
\begin{itemize}
    \item[] \B{অক্ষীয়:} {\lat $E=\dfrac{2kp}{r^3},\;V=\dfrac{kp}{r^2}$}
    \item[] \B{নিরক্ষীয়:} {\lat $E=\dfrac{kp}{r^3},\;V=0$}
    \item[] \B{টর্ক:} {\lat $\tau=pE\sin\theta$};\; \B{স্থিতিশক্তি:} {\lat $U=-\vec p\cdot\vec E$}
    \item[] {\lat $p$} = \B{দ্বিমেরু ভ্রামক} {\lat [C$\cdot$m]};\; {\lat $2l$} = \B{দ্বিমেরু আন্তঃদূরত্ব}
\end{itemize}

\itm{5} \textbf{\B{গাউসের সূত্র,}} {\lat $\Phi_E=\oint\vec E\cdot d\vec A=\dfrac{Q_{\rm enc}}{\varepsilon_0}$}
\begin{itemize}
    \item[] {\lat $\Phi_E$} = \B{তড়িৎ ফ্লাক্স};\; {\lat $Q_{\rm enc}$} = \B{গাউস পৃষ্ঠের ভেতরে আবদ্ধ চার্জ}
\end{itemize}

\itm{6} \textbf{\B{ধারকত্ব,}} {\lat $C=Q/V$}
\begin{itemize}
    \item[] \B{সমান্তরাল পাত:} {\lat $C=\dfrac{\varepsilon_0 A}{d}$};\; \B{ডাইইলেক্ট্রিকসহ:} {\lat $C=\dfrac{K\varepsilon_0 A}{d}=KC_0$}
    \item[] \B{গোলকীয়:} {\lat $C=4\pi\varepsilon_0 r$};\; \B{দ্বিগোলকীয়:} {\lat $C=\dfrac{4\pi\varepsilon_0 ab}{b-a}$}
    \item[] \B{নলাকার:} {\lat $C=\dfrac{2\pi\varepsilon_0 l}{\ln(b/a)}$}
    \item[] \B{সঞ্চিত শক্তি:} {\lat $W=\tfrac{1}{2}QV=\tfrac{1}{2}CV^2=\dfrac{Q^2}{2C}$}
    \item[] \B{শক্তি ঘনত্ব:} {\lat $u=\tfrac{1}{2}\varepsilon_0 E^2$}
    \item[] {\lat $C$} = \B{ধারকত্ব} {\lat [F]};\; {\lat $A$} = \B{পাতের ক্ষেত্রফল};\; {\lat $d$} = \B{ব্যবধান}
\end{itemize}

\itm{7} \textbf{\B{ধারকের সমন্বয়:}}
\begin{itemize}
    \item[] \B{সিরিজ:} {\lat $\dfrac{1}{C_s}=\dfrac{1}{C_1}+\dfrac{1}{C_2}+\cdots+\dfrac{1}{C_n}$}
    \item[] \B{সমান্তরাল:} {\lat $C_p=C_1+C_2+\cdots+C_n$}
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

\itm{1} \textbf{\B{বায়ো-সাভার্টের সূত্র,}} {\lat $dB=\dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2}$}

\itm{2} \textbf{\B{বিভিন্ন চৌম্বক ক্ষেত্র:}}
\begin{itemize}
    \item[] \B{অসীম সরল তার:} {\lat $B=\dfrac{\mu_0 I}{2\pi r}$}
    \item[] \B{সীমিত তার:} {\lat $B=\dfrac{\mu_0 I}{4\pi r}(\sin\theta_1+\sin\theta_2)$}
    \item[] \B{বৃত্তীয় কুণ্ডলীর কেন্দ্রে:} {\lat $B=\dfrac{\mu_0 I}{2R}$};\; \B{$N$ পাকে:} {\lat $B=\dfrac{\mu_0 NI}{2R}$}
    \item[] \B{অক্ষে:} {\lat $B=\dfrac{\mu_0 NIR^2}{2(R^2+x^2)^{3/2}}$}
    \item[] \B{সোলেনয়েড:} {\lat $B=\mu_0 nI$};\; \B{টরয়েড:} {\lat $B=\dfrac{\mu_0 NI}{2\pi r}$}
\end{itemize}

\itm{3} \textbf{\B{অ্যাম্পেয়ারের সূত্র,}} {\lat $\oint\vec B\cdot d\vec l=\mu_0 I_{\rm enc}$}

\itm{4} \textbf{\B{লোরেন্ৎজ বল,}} {\lat $\vec F=q(\vec v\times\vec B)$}
\begin{itemize}
    \item[] \B{বৃত্তীয় গতি:} {\lat $r=\dfrac{mv}{qB},\;f=\dfrac{qB}{2\pi m}$}
    \item[] \B{তারে বল:} {\lat $\vec F=I(\vec l\times\vec B)$}
    \item[] \B{সমান্তরাল তারে:} {\lat $F/l=\dfrac{\mu_0 I_1 I_2}{2\pi d}$}
\end{itemize}

\itm{5} \textbf{\B{হল প্রভাব,}} {\lat $V_H=Bvd$;\; $R_H=1/(nq)$}

\itm{6} \textbf{\B{চৌম্বক ভ্রামক,}} {\lat $\vec m=NI\vec A$;\; $M=\dfrac{\tau}{B\sin\theta}=IAN$}
\begin{itemize}
    \item[] \B{টর্ক:} {\lat $\tau=mB\sin\theta=NIAB\sin\theta$};\; \B{শক্তি:} {\lat $U=-\vec m\cdot\vec B$}
\end{itemize}

\itm{7} \textbf{\B{গ্যালভানোমিটার:}}
\begin{itemize}
    \item[] \B{অ্যামিটার (শান্ট):} {\lat $S=\dfrac{I_g G}{I-I_g}=\dfrac{G}{n-1}$},\; {\lat $n=I/I_g$}
    \item[] \B{ভোল্টমিটার:} {\lat $R_h=\dfrac{V}{I_g}-G$}
    \item[] {\lat $G$} = \B{গ্যালভানো রোধ};\; {\lat $I_g$} = \B{পূর্ণ স্কেল প্রবাহ};\; {\lat $S$} = \B{শান্ট রোধ}
\end{itemize}

\itm{8} \textbf{\B{চৌম্বক পদার্থ:}}
\begin{itemize}
    \item[] {\lat $B=\mu H;\; B=\mu_0(H+M)=\mu_0\mu_r H$}
    \item[] \B{প্রবণতা:} {\lat $\chi_m=I/H=\mu_r-1$}
    \item[] \B{কুরির সূত্র:} {\lat $\chi_m=C/T$}
\end{itemize}

\itm{9} \textbf{\B{পৃথিবীর চৌম্বক ক্ষেত্র:}}
\begin{itemize}
    \item[] \B{অনুভূমিক:} {\lat $H=I\cos\delta$};\; \B{উল্লম্ব:} {\lat $V=I\sin\delta$}
    \item[] {\lat $V/H=\tan\delta$};\; {\lat $I^2=H^2+V^2$}
\end{itemize}

\itm{10} \textbf{\B{ফ্যারাডের তড়িৎচৌম্বক আবেশ:}}
\begin{itemize}
    \item[] \B{২য়:} {\lat $\varepsilon=-N\dfrac{d\Phi}{dt}=-N\dfrac{\Phi_2-\Phi_1}{t}$}
    \item[] \B{ফ্লাক্স:} {\lat $\Phi=BA\cos\theta$}
    \item[] \B{চলমান পরিবাহী:} {\lat $\varepsilon=Blv\sin\theta$}
\end{itemize}

\itm{11} \textbf{\B{আবেশ গুণাঙ্ক:}}
\begin{itemize}
    \item[] \B{স্বকীয়:} {\lat $\varepsilon=L\,dI/dt$;\; $\Phi=LI$}
    \item[] \B{সোলেনয়েড:} {\lat $L=\mu_0 n^2 Al=\mu_0 N^2A/l$}
    \item[] \B{পারস্পরিক:} {\lat $\varepsilon_2=-M\,dI_1/dt$;\; $M=k\sqrt{L_1L_2}$}
    \item[] \B{সঞ্চিত শক্তি:} {\lat $U=\tfrac{1}{2}LI^2$}
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

\itm{1} \textbf{\B{ম্যাক্সওয়েল সম্পর্ক,}} {\lat $c=1/\sqrt{\mu_0\varepsilon_0}=3\times10^8$ m/s}

\itm{2} \textbf{\B{প্রতিফলন ও প্রতিসরণ:}}
\begin{itemize}
    \item[] \B{স্নেলের সূত্র:} {\lat $n_1\sin\theta_1=n_2\sin\theta_2$}
    \item[] {\lat $\mu=\dfrac{c}{v}=\dfrac{\sin i}{\sin r}$}
    \item[] \B{পূর্ণ অভ্যন্তরীণ:} {\lat $\sin\theta_c=1/\mu$}
\end{itemize}

\itm{3} \textbf{\B{দর্পণের সূত্র,}} {\lat $\dfrac{1}{v}+\dfrac{1}{u}=\dfrac{2}{R}=\dfrac{1}{f}$}

\itm{4} \textbf{\B{লেন্স:}}
\begin{itemize}
    \item[] \B{সূত্র:} {\lat $\dfrac{1}{v}-\dfrac{1}{u}=\dfrac{1}{f}$}
    \item[] \B{লেন্স নির্মাতা:} {\lat $\dfrac{1}{f}=(\mu-1)\!\left(\dfrac{1}{R_1}-\dfrac{1}{R_2}\right)$}
    \item[] \B{ক্ষমতা:} {\lat $P=1/f$};\; \B{$n$ লেন্স:} {\lat $\dfrac{1}{F}=\sum\dfrac{1}{f_i}$}
\end{itemize}

\itm{5} \textbf{\B{প্রিজম:}}
\begin{itemize}
    \item[] {\lat $A+\delta=i_1+i_2$;\; $A=r_1+r_2$}
    \item[] \B{ন্যূনতম বিচ্যুতি:} {\lat $\mu=\dfrac{\sin\!\left(\frac{A+\delta_m}{2}\right)}{\sin\!\left(A/2\right)}$}
    \item[] \B{বিক্ষেপণ ক্ষমতা:} {\lat $\omega=\dfrac{\mu_v-\mu_r}{\mu_y-1}$}
\end{itemize}

\itm{6} \textbf{\B{যন্ত্রপাতি:}}
\begin{itemize}
    \item[] \B{সরল অণুবীক্ষণ:} {\lat $m=1+D/f$}
    \item[] \B{জটিল অণুবীক্ষণ:} {\lat $m\approx-\dfrac{L}{f_o}\!\left(1+\dfrac{D}{f_e}\right)$}
    \item[] \B{দূরবীক্ষণ (অসীমে):} {\lat $m=-f_o/f_e$};\; {\lat $L=f_o+f_e$}
    \item[] {\lat $D=25$ cm} = \B{ন্যূনতম স্পষ্ট দূরত্ব}
\end{itemize}

\chsec{অধ্যায়-৭: ভৌত আলোকবিদ্যা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{তরঙ্গ,}} {\lat $c=f\lambda$;\; $k=2\pi/\lambda$;\; $\omega=2\pi f$}

\itm{2} \textbf{\B{ইয়ং দ্বি-চির অপবর্তন:}}
\begin{itemize}
    \item[] \B{ডোরার প্রস্থ:} {\lat $\beta=\lambda D/d$};\; {\lat $y_n=n\lambda D/d$}
\end{itemize}

\itm{3} \textbf{\B{একক-চির অপবর্তন:}}
\begin{itemize}
    \item[] \B{গ্রেটিং:} {\lat $(a+b)\sin\theta_n=n\lambda$}
\end{itemize}

\itm{4} \textbf{\B{পাতলা পর্দা:}}
\begin{itemize}
    \item[] \B{গঠনমূলক:} {\lat $2\mu t\cos r=(2n-1)\lambda/2$}
    \item[] \B{ধ্বংসাত্মক:} {\lat $2\mu t\cos r=n\lambda$}
\end{itemize}

\itm{5} \textbf{\B{নিউটনের বলয়:}}
\begin{itemize}
    \item[] \B{অন্ধকার:} {\lat $r_n=\sqrt{n\lambda R}$};\; {\lat $\lambda=\dfrac{D_n^2-D_m^2}{4R(n-m)}$}
\end{itemize}

\itm{6} \textbf{\B{মেরুকরণ:}}
\begin{itemize}
    \item[] \B{ব্রুস্টার:} {\lat $\tan\theta_B=\mu$};\; \B{ম্যালাস:} {\lat $I=I_0\cos^2\theta$}
\end{itemize}

\itm{7} \textbf{\B{ডপলার ক্রিয়া:}} \B{শব্দ:} {\lat $f'=f\dfrac{c\pm v_o}{c\mp v_s}$};\; \B{আলো:} {\lat $\Delta\lambda/\lambda=v/c$}

\chsec{অধ্যায়-৮: আধুনিক পদার্থবিজ্ঞানের সূচনা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{আপেক্ষিকতা:}}
\begin{itemize}
    \item[] \B{দৈর্ঘ্য সংকোচন:} {\lat $L=L_0\sqrt{1-v^2/c^2}$}
    \item[] \B{কাল প্রসারণ:} {\lat $t=\gamma t_0$};\; \B{ভরবৃদ্ধি:} {\lat $m=\gamma m_0$}
    \item[] \B{ভর-শক্তি:} {\lat $E=mc^2$;\; $E^2=(pc)^2+(m_0c^2)^2$}
    \item[] {\lat $\gamma=1/\sqrt{1-v^2/c^2}$}
\end{itemize}

\itm{2} \textbf{\B{আলোক-তড়িৎ ক্রিয়া:}}
\begin{itemize}
    \item[] {\lat $E=hf=hc/\lambda$};\; \B{কাজ অপেক্ষক:} {\lat $\phi=hf_0$}
    \item[] \B{সর্বোচ্চ গতিশক্তি:} {\lat $E_k^{\max}=hf-\phi=eV_s$}
    \item[] \B{ফোটনের ভরবেগ:} {\lat $p=h/\lambda$}
\end{itemize}

\itm{3} \textbf{\B{কম্পটন প্রভাব,}} {\lat $\Delta\lambda=\dfrac{h}{m_0 c}(1-\cos\theta)$}

\itm{4} \textbf{\B{দ্য ব্রোগলি,}} {\lat $\lambda=\dfrac{h}{p}=\dfrac{h}{mv}=\dfrac{h}{\sqrt{2mE_k}}$}

\itm{5} \textbf{\B{হাইজেনবার্গ অনিশ্চয়তা:}} {\lat $\Delta x\cdot\Delta p\ge\hbar/2$}

\chsec{অধ্যায়-৯: পরমাণুর মডেল ও নিউক্লিয়ার পদার্থবিজ্ঞান}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বোর মডেল:}}
\begin{itemize}
    \item[] \B{কোয়ান্টাইজেশন:} {\lat $mvr_n=n\dfrac{h}{2\pi}$}
    \item[] \B{ব্যাসার্ধ:} {\lat $r_n=\dfrac{n^2}{Z}a_0$};\; \B{H:} {\lat $a_0=0.529$ \AA}
    \item[] \B{মোট শক্তি:} {\lat $E_n=-\dfrac{13.6\,Z^2}{n^2}$ eV}
    \item[] \B{রিডবার্গ:} {\lat $\dfrac{1}{\lambda}=R_HZ^2\!\left(\dfrac{1}{n_1^2}-\dfrac{1}{n_2^2}\right)$};\; {\lat $R_H=1.097\times10^7$ m$^{-1}$}
    \item[] \B{সিরিজ:} \B{লাইমান (1), বামার (2), প্যাশেন (3), ব্র্যাকেট (4), ফান্ড (5)}
\end{itemize}

\itm{2} \textbf{\B{X-রে:}}
\begin{itemize}
    \item[] \B{মোসেলি:} {\lat $\sqrt f=a(Z-b)$};\; \B{ব্র্যাগ:} {\lat $2d\sin\theta=n\lambda$}
    \item[] \B{কাট-অফ:} {\lat $\lambda_{\min}=hc/(eV)$}
\end{itemize}

\itm{3} \textbf{\B{নিউক্লিয়াস:}}
\begin{itemize}
    \item[] \B{ব্যাসার্ধ:} {\lat $R=R_0 A^{1/3}$};\; {\lat $R_0=1.2\times10^{-15}$ m}
    \item[] \B{ভরত্রুটি:} {\lat $\Delta m=[Zm_p+(A-Z)m_n]-M$}
    \item[] \B{বন্ধনশক্তি:} {\lat $E_b=\Delta m\cdot c^2=\Delta m\times 931.5$ MeV}
\end{itemize}

\itm{4} \textbf{\B{তেজস্ক্রিয়তা,}} {\lat $N=N_0 e^{-\lambda t}$}
\begin{itemize}
    \item[] \B{অর্ধায়ু:} {\lat $T_{1/2}=0.693/\lambda$};\; \B{গড় আয়ু:} {\lat $\tau=1/\lambda$}
    \item[] \B{সক্রিয়তা:} {\lat $A=\lambda N$};\; {\lat $1$ Ci $=3.7\times10^{10}$ Bq}
\end{itemize}

\itm{5} \textbf{\B{বিঘটন:}}
\begin{itemize}
    \item[] {\lat $\alpha$}: {\lat ${}^A_ZX\to{}^{A-4}_{Z-2}Y+{}^4_2$He}
    \item[] {\lat $\beta^-$}: {\lat ${}^A_ZX\to{}^A_{Z+1}Y+e^-+\bar\nu_e$}
    \item[] {\lat $\beta^+$}: {\lat ${}^A_ZX\to{}^A_{Z-1}Y+e^++\nu_e$}
\end{itemize}

\itm{6} \textbf{\B{নিউক্লিয়ার বিক্রিয়া:}}
\begin{itemize}
    \item[] \B{ফিশন:} {\lat ${}^{235}$U $+$ n $\to$ Ba $+$ Kr $+$ 3n $+$ \B{শক্তি}}
    \item[] \B{ফিউশন:} {\lat D $+$ T $\to{}^4$He $+$ n $+ 17.6$ MeV}
    \item[] {\lat $1$ u $=931.5$ MeV}
\end{itemize}

\chsec{অধ্যায়-১০: সেমিকন্ডাক্টর ও ইলেকট্রনিক্স}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{সেমিকন্ডাক্টর,}} {\lat $J=e(n\mu_e+p\mu_h)E$;\; $np=n_i^2$}

\itm{2} \textbf{\B{ডায়োড:}}
\begin{itemize}
    \item[] \B{অর্ধতরঙ্গ:} {\lat $V_{\rm dc}=V_m/\pi$};\; \B{পূর্ণতরঙ্গ:} {\lat $V_{\rm dc}=2V_m/\pi$}
\end{itemize}

\itm{3} \textbf{\B{জেনার রেগুলেটর,}} {\lat $R_s=\dfrac{V_s-V_Z}{I_Z+I_L}$}

\itm{4} \textbf{\B{ট্রানজিস্টর:}}
\begin{itemize}
    \item[] {\lat $I_E=I_B+I_C$};\; {\lat $\alpha=I_C/I_E$};\; {\lat $\beta=I_C/I_B$}
    \item[] {\lat $\beta=\dfrac{\alpha}{1-\alpha}$};\; {\lat $\alpha=\dfrac{\beta}{1+\beta}$}
    \item[] \B{ভোল্টেজ গেইন:} {\lat $A_v=-\beta R_C/r_{be}$}
\end{itemize}

\itm{5} \textbf{\B{লজিক গেট:}}
\begin{itemize}
    \item[] \B{AND:} {\lat $Y=A\cdot B$};\; \B{OR:} {\lat $Y=A+B$};\; \B{NOT:} {\lat $Y=\bar A$}
    \item[] \B{NAND:} {\lat $Y=\overline{AB}$};\; \B{NOR:} {\lat $Y=\overline{A+B}$}
    \item[] \B{XOR:} {\lat $Y=A\bar B+\bar AB$}
    \item[] \B{ডি-মর্গান:} {\lat $\overline{AB}=\bar A+\bar B$;\; $\overline{A+B}=\bar A\bar B$}
\end{itemize}

\itm{6} \textbf{\B{অপ-অ্যাম্প:}}
\begin{itemize}
    \item[] \B{ইনভার্টিং:} {\lat $A_v=-R_f/R_1$};\; \B{নন-ইনভার্টিং:} {\lat $A_v=1+R_f/R_1$}
    \item[] \B{সামার:} {\lat $V_o=-R_f(V_1/R_1+V_2/R_2)$}
    \item[] \B{ইন্টিগ্রেটর:} {\lat $V_o=-\dfrac{1}{RC}\int V_{\rm in}\,dt$}
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

\end{document}
'''

with open("physics_both_fixed.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

def run(cmd):
    return subprocess.run(cmd, shell=True).returncode

latex_cmd = "xelatex" if shutil.which("xelatex") else "nix shell nixpkgs#texliveFull -c xelatex"
run("fc-cache -fv 2>/dev/null")
run(f"{latex_cmd} -interaction=nonstopmode physics_both_fixed.tex 2>&1 | tail -20")
run(f"{latex_cmd} -interaction=nonstopmode physics_both_fixed.tex 2>&1 | tail -5")
print("PDF ready:", os.path.exists("physics_both_fixed.pdf"))
