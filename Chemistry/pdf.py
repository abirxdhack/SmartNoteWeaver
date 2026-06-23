import subprocess, os, shutil, urllib.request, hashlib

tex_content = r"""\documentclass[10pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{mathtools}
\usepackage{newunicodechar}
\usepackage[margin=1.15cm, top=1.25cm, bottom=1.15cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{graphicx}
\usepackage{array}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{adjustbox}
\usepackage{needspace}
\usepackage{ucharclasses}
\pagestyle{empty}
\setlength{\emergencystretch}{35pt}
\hbadness=10000
\vbadness=10000
\sloppy
\raggedcolumns
\tolerance=9999
\emergencystretch=35pt

\defaultfontfeatures{Ligatures=TeX}

\setmainfont{Latin Modern Roman}

\newfontfamily\lat[Ligatures=TeX]{Latin Modern Roman}

\newfontfamily\bn[
  Path=./fonts/,
  Extension=.ttf,
  Script=Bengali,
  Ligatures=TeX,
  BoldFeatures={FakeBold=2.6},
  ItalicFeatures={FakeSlant=0.12},
  BoldItalicFeatures={FakeBold=2.6,FakeSlant=0.12}
]{NotoSerifBengali-Regular}

\newunicodechar{°}{\ensuremath{^\circ}}

\setTransitionTo{Bengali}{\begingroup\bn}
\setTransitionFrom{Bengali}{\endgroup}

\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{85,85,85}
\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}

\newcommand{\B}[1]{{\bn #1}}
\newcommand{\LAT}[1]{{\lat #1}}

\newcommand{\divider}{\par\vspace{1.5pt}\noindent\textcolor{black!22}{\rule{\linewidth}{0.3pt}}\par\vspace{1.5pt}}

\let\oldtabular\tabular
\let\endoldtabular\endtabular
\RenewDocumentEnvironment{tabular}{m}{\par\smallskip\begin{center}\scriptsize\renewcommand{\arraystretch}{1.3}\setlength{\tabcolsep}{3pt}\begin{adjustbox}{max width=\linewidth}\oldtabular{#1}}{\endoldtabular\end{adjustbox}\end{center}\smallskip\par}

\newcommand{\chsec}[1]{%
  \par\Needspace{7\baselineskip}\vspace{5pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par
}

\newcommand{\chsub}[2]{%
  \par\Needspace{5\baselineskip}\vspace{4pt}%
  \noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \bfseries\footnotesize\color{white}\;{\lat #1} \B{#2}%
  }}%
  \vspace{1pt}\par
}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{2pt}

\setlist[enumerate]{leftmargin=*, topsep=2pt, itemsep=1pt, parsep=0pt, partopsep=0pt}
\setlist[itemize]{leftmargin=14pt, topsep=2pt, itemsep=1pt, parsep=0pt, partopsep=0pt, label={\lat\textbullet}}
\newcommand{\itm}[1]{\textbf{{\lat #1.}}\;}
\newcommand{\sub}[1]{\textbf{({\lat #1})}\;}


\begin{document}

\begin{center}
\noindent
{\bn\Large\bfseries একনজরে রসায়ন প্রথম পত্র — কনসেপ্ট ম্যাপ ও সূত্রাবলি}\hfill
{\normalfont\small \textbf{By Abir Arafat Chawdhury [Introvert's Area]}}
\vspace{3pt}
\end{center}

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{রসায়ন প্রথম পত্র}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: ল্যাবরেটরির নিরাপদ ব্যবহার (Safe Use of Laboratory)}

\chsub{Concept Map: The Chapter at a Glance}{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: ল্যাবরেটরি}}

\divider

\textbf{{\lat 1.} \B{ব্যবহার বিধি} $\rightarrow$ \B{নিরাপদ পরিবেশ সৃষ্টির সোনালী বিধি:}}
\begin{itemize}
    \item \B{নিয়মানুবর্তিতা, যত্নশীলতা, অধ্যবসায়, পরিশ্রম, সুবিবেচনা, পরিচ্ছন্নতা}
    \item \B{অ্যাপ্রন, চোখে নিরাপদ চশমা (Safety Goggles), হ্যান্ড গ্লাভস, মাস্ক, পায়ে জুতা, ক্যাপ পরা, পর্যাপ্ত আলো ও বায়ু চলাচলের (Fume Hood) ব্যবস্থা}
    \item \B{বিভিন্ন প্রকার হ্যান্ড গ্লাভস ও তাদের ব্যবহার:}
    \begin{itemize}
        \item \B{নাইট্রাইল গ্লাভস (Nitrile Gloves):} সর্বাপেক্ষা নিরাপদ, ক্ষয়কারী ও ত্বক সংবেদনশীল রাসায়নিক পদার্থ ব্যবহারে ব্যবহৃত হয়.
        \item \B{ল্যাটেক্স গ্লাভস (Lateex Gloves):} চামড়ার সুরক্ষায় এবং সাধারণ ল্যাব কার্যক্রমে বহুল ব্যবহৃত.
        \item \B{নিওপ্রিন গ্লাভস (Neoprene Gloves):} এসিড, ক্ষার ও জৈব দ্রাবকের বিরুদ্ধে চমৎকার প্রতিরোধ গড়ে তোলে.
        \item \B{অ্যাসবেস্টস গ্লাভস (Asbestos Gloves):} উচ্চ তাপে উত্তপ্ত বস্তু বা পাত্র ধরার জন্য ব্যবহৃত হয়.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 2.} \B{ব্যবহৃত যন্ত্রপাতি ও পরিষ্কারকরণ প্রক্রিয়া:}}
\begin{itemize}
    \item \textbf{\B{গ্লাস সামগ্রী:}} \B{টেস্টটিউব, কনিক্যাল ফ্লাস্ক, বিকার, আয়তনিক ফ্লাস্ক (Volumetric Flask), মাপন সিলিন্ডার, ফানেল, ব্যুরেট, পিপেট, ওজন বোতল (Weighing Bottle), ওয়াশ বোতল, গ্লাস রড, ওয়াচ গ্লাস, রি-এজেন্ট বোতল.}
    \item \textbf{\B{গ্লাস সামগ্রী পরিষ্কার করার কৌশল (Cleaning Mixtures):}}
    \begin{itemize}
        \item \B{ডিটারজেন্ট বা ল্যাবোগ্লিজ:} সাধারণ ময়লা ও তৈলাক্ত পদার্থ দূর করতে ১০\% ল্যাবোগ্লিজ দ্রবণ ব্যবহার করা হয়.
        \item \B{ক্রোমিক এসিড মিশ্রণ (Chromic Acid Mixture):} গ্লাস সামগ্রীতে লেগে থাকা সব ধরণের জটিল গ্রীজ, চর্বি বা অজৈব ময়লা দূর করতে সর্বাপেক্ষা কার্যকরী ক্ষালন মিশ্রণ. এটি মূলত পটাসিয়াম ডাইক্রোমেট ও গাঢ় সালফিউরিক এসিডের মিশ্রণ [{\lat $\text{K}_2\text{Cr}_2\text{O}_7 + \text{conc. H}_2\text{SO}_4$}].
    \end{itemize}
    \item \textbf{\B{তাপ প্রদানকারী যন্ত্র:}} \B{স্পিরিট ল্যাম্প, বুনসেন বার্নার (অনুজ্জ্বল শিখা, উজ্জ্বল শিখা), হিটিং ম্যান্টল, পানি গাহ (Water Bath).}
    
    \begin{itemize}
        \item \B{অনুজ্জ্বল শিখা (Non-luminous Flame):} বায়ু ছিদ্র সম্পূর্ণ খোলা থাকলে উৎপন্ন হয়. এটি ধোঁয়াহীন, নীল বর্ণের এবং অত্যন্ত উত্তপ্ত (সর্বোচ্চ তাপমাত্রার জোন থাকে). ল্যাবরেটরিতে রসায়নের বিভিন্ন পরীক্ষা ও উত্তপ্তকরণের জন্য এই শিখা ব্যবহার করা হয়.
        \item \B{উজ্জ্বল শিখা (Luminous Flame):} বায়ু ছিদ্র বন্ধ থাকলে উৎপন্ন হয়. এটি হলুদ বর্ণের এবং অপূর্ণ দহনের কারণে কার্বন কণা বা ধোঁয়া সৃষ্টি করে.
    \end{itemize}
    \item \textbf{\B{ব্যালেন্স:}} \B{ম্যানুয়াল (} $\rightarrow$ \B{টপলোড), ডিজিটাল (} $\rightarrow$ \B{অ্যানালাইটিক্যাল).}
    \item \textbf{\B{অন্যান্য যন্ত্রপাতি:}} \B{বলয় ধারক (Ring Stand), তারজালি (Wire Gauze), ক্ল্যাম্প, ক্রুসিবল চিমটা (Crucible Tongs), শিখা বিস্তারক (Wing Top), স্প্যাচুলা, ফরসেপ, স্কুপলা.}
\end{itemize}

\divider

\textbf{{\lat 3.} \B{কার্যক্রমসমূহ:}}
\begin{itemize}
    \item \B{যন্ত্রপাতি ব্যবহারের কৌশল, তাপ প্রয়োগের কৌশল, যন্ত্রপাতি পরিষ্কারের কৌশল, এবং ল্যাবরেটরি বর্জ্য সঠিক স্থানে অপসারণের নিয়মাবলী.}
\end{itemize}

\divider

\textbf{{\lat 4.} \B{দুর্ঘটনা, প্রতিরোধ ও সতর্কতা:}}
\begin{itemize}
    \item \textbf{\B{প্রতিকার:}} \B{ল্যাবরেটরির নির্দেশ মেনে চলা; রাসায়নিক বস্তুর ক্ষতিকারণ দিক সম্পর্কে জানা; পূর্ব প্রস্তুতি নেয়া.}
    \item \textbf{\B{সতর্কতা:}} \B{রাসায়নিক দ্রব্য খালি হাতে স্পর্শ করা, সরাসরি নাক দিয়ে গন্ধ নেয়া বা মুখ দিয়ে স্বাদ নেয়া যাবে না; পাত্রের নির্দিষ্ট স্প্যাচুলা ব্যবহার করা; ওয়াশ বোতলকে কেবল মাত্র পাতিত পানি (Distilled Water) দ্বারা পূর্ণ করা; মুখ দিয়ে পিপেটের মাধ্যমে ক্ষয়কারী তরল দ্রব্য স্থানান্তর না করে পিপেট ফিলার ব্যবহার করা.}
    \item \textbf{\B{কারণ:}} \B{অসতর্কতা, ঝুঁকিপূর্ণ রাসায়নিক দ্রব্য, আগুন, কাঁচের ভাঙা অংশ, অপরিকল্পিত ল্যাবরেটরি বা ভুল পরীক্ষণ পদ্ধতি.}
\end{itemize}

\divider

\textbf{{\lat 5.} \B{দ্রব্যাদি} $\rightarrow$ \B{বিকারক ও নির্দেশক:}}
\begin{itemize}
    \item \textbf{\B{ক্ষার:}} \B{লঘু} {\lat $\text{NaOH}$}, \B{লঘু} {\lat $\text{KOH}$}, \B{লঘু} {\lat $\text{NH}_4\text{OH}$}
    \item \textbf{\B{এসিড:}} \B{লঘু} {\lat $\text{HCl}$}, \B{লঘু} {\lat $\text{HNO}_3$}, \B{লঘু} {\lat $\text{H}_2\text{SO}_4$}, \B{লঘু} {\lat $\text{CH}_3\text{COOH}$}
    \item \textbf{\B{নির্দেশক (Indicators):}} \B{লিটমাস ব্লু, লিটমাস রেড, মিথাইল অরেঞ্জ, ফেনলফথ্যালিন, মিথাইল রেড.}
    \item \textbf{\B{প্রাথমিক ও মাধ্যমিক প্রমাণ পদার্থ (Primary \& Secondary Standard Substances):}}
    \begin{itemize}
        \item \B{প্রাথমিক প্রমাণ পদার্থ:} যা বিশুদ্ধ অবস্থায় পাওয়া যায়, বায়ুর উপাদান দ্বারা আক্রান্ত হয় না এবং এর দ্বারা প্রস্তুত দ্রবণের ঘনমাত্রা দীর্ঘদিন অপরিবর্তিত থাকে. যেমন: অনার্দ্র সোডিয়াম কার্বনেট [{\lat $\text{Na}_2\text{CO}_3$}], অক্সালিক এসিড [{\lat $\text{H}_2\text{C}_2\text{O}_4 \cdot 2\text{H}_2\text{O}$}], পটাসিয়াম ডাইক্রোমেট [{\lat $\text{K}_2\text{Cr}_2\text{O}_7$}].
        \item \B{মাধ্যমিক প্রমাণ পদার্থ:} যা বিশুদ্ধ অবস্থায় পাওয়া যায় না, বায়ুর আর্দ্রতা বা গ্যাস দ্বারা দ্রুত আক্রান্ত হয় এবং এর ঘনমাত্রা পরিবর্তিত হয়ে যায়. যেমন: সালফিউরিক এসিড [{\lat $\text{H}_2\text{SO}_4$}], হাইড্রোক্লোরিক এসিড [{\lat $\text{HCl}$}], সোডিয়াম হাইড্রোক্সাইড [{\lat $\text{NaOH}$}], পটাসিয়াম পারম্যাঙ্গানেট [{\lat $\text{KMnO}_4$}].
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 6.} \B{আয়ন শনাক্তকরণে ব্যবহৃত বিকারক ও উৎপন্ন অধঃক্ষেপের কালার চার্ট:}}
\begin{itemize}
    \item \B{পটাসিয়াম ফেরোসায়ানাইড,} {\lat $\text{K}_4[\text{Fe}(\text{CN})_6]$} $\rightarrow$ {\lat $\text{Fe}^{2+}$} \B{এর সাথে হালকা নীল এবং } {\lat $\text{Fe}^{3+}$} \B{এর সাথে গাঢ় নীল (প্রুসিয়ান ব্লু) অধঃক্ষেপ দেয়.}
    \item \B{পটাসিয়াম ফেরিসায়ানাইড,} {\lat $\text{K}_3[\text{Fe}(\text{CN})_6]$} $\rightarrow$ {\lat $\text{Fe}^{2+}$} \B{এর সাথে গাঢ় নীল এবং } {\lat $\text{Fe}^{3+}$} \B{এর সাথে বাদামী দ্রবণ তৈরি করে.}
    \item \B{পটাসিয়াম পাইরোঅ্যান্টিমোনেট,} {\lat $\text{K}_2\text{H}_2\text{Sb}_2\text{O}_7$} $\rightarrow$ {\lat $\text{Na}^+$} \B{আয়ন শনাক্তকরণের একমাত্র বিকারক (সাদা অধঃক্ষেপ).}
    \item \B{নেসলার দ্রবণ} {\lat $\text{K}_2[\text{HgI}_4] + \text{KOH}$} $\rightarrow$ {\lat $\text{NH}_4^+$} \B{আয়ন শনাক্তকরণে ব্যবহৃত হয় (বাদামী অধঃক্ষেপ বা অ্যামিনো মারকিউরিক আয়োডাইডের তামাটে বাদামী রং).}
    \item \B{সিলভার নাইট্রেট দ্রবণ,} {\lat $\text{AgNO}_3$} $\rightarrow$ {\lat $\text{Cl}^-$} \B{আয়ন শনাক্তকরণে দইয়ের মতো সাদা অধঃক্ষেপ দেয় যা } {\lat $\text{NH}_4\text{OH}$} \B{এ দ্রবণীয়.}
    \item \B{অ্যামোনিয়াম থায়োসায়ানেট,} {\lat $\text{NH}_4\text{CNS}$} $\rightarrow$ {\lat $\text{Fe}^{3+}$} \B{এর সাথে রক্তলাল বর্ণ তৈরি করে.}
    \item \B{অ্যামোনিয়াম অক্সালেট,} {\lat $(\text{NH}_4)_2\text{C}_2\text{O}_4$} $\rightarrow$ {\lat $\text{Ca}^{2+}$} \B{আয়ন শনাক্তকরণে সাদা অধঃক্ষেপ সৃষ্টি করে.}
    \item \B{বেরিয়াম নাইট্রেট বা বেরিয়াম ক্লোরাইড দ্রবণ} {\lat $\text{Ba}(\text{NO}_3)_2 / \text{BaCl}_2$} $\rightarrow$ {\lat $\text{SO}_4^{2-}$} \B{ও } {\lat $\text{CO}_3^{2-}$} \B{শনাক্তকরণে সাদা অধঃক্ষেপ দেয়.}
\end{itemize}

\divider

\textbf{{\lat 7.} \B{পরিবেশ ও মানবদেহের উপর রাসায়নিকের প্রভাব:}}
\begin{itemize}
    \item \textbf{\B{ভারী ধাতু (লেড, মার্কারি, ক্রোমিয়াম, ক্যাডমিয়াম প্রভৃতি):}} \B{মানব শরীরের এনজাইমেটিক ক্রিয়া ও মেটাবলিক সিস্টেমে মারাত্মক ক্ষতিসাধন করে, স্নায়ুতন্ত্র বিকল করে.}
    \item \textbf{\B{হ্যালোজেন যুক্ত জৈব যৌগ (যেমন- ক্লোরোফর্ম):}} \B{লিভারের স্থায়ী ক্ষতি (জন্ডিস, লিভার সিরোসিস), সেন্ট্রাল নার্ভাস সিস্টেম ও কিডনির কার্যকারিতা নষ্ট করে.}
    \item \textbf{\B{উদ্বায়ী পদার্থ (লিকার অ্যামোনিয়া, গাঢ় }} {\lat HCl}, \B{ইথার প্রভৃতি):} \B{শ্বাসের তীব্র সঙ্কট, চোখের কর্নিয়ার ক্ষতি, খাদ্যনালী ও ফুসফুসের প্রদাহ সৃষ্টি করে.}
    \item \textbf{\B{বিক্রিয়ার উপজাত হিসেবে নির্গত গ্যাস (}} {\lat $\text{NO}_2, \text{SO}_2, \text{SO}_3, \text{CO}_2, \text{H}_2\text{S}$} \textbf{\B{ প্রভৃতি):}} \B{তীব্র বায়ু দূষণ, গ্রীনহাউজ প্রভাব এবং বায়ুমণ্ডলে পানির সাথে মিশে এসিড বৃষ্টি সৃষ্টি করে.}
\end{itemize}

\divider

\textbf{{\lat 8.} \B{অ্যানালিটিক্যাল ল্যাবরেটরি পদ্ধতিসমূহ (Analytical Methods):}}
\begin{itemize}
    \item \textbf{\B{বিশ্লেষণাত্মক পদ্ধতির তুলনামূলক ছক (Comparison Table):}}
    \begin{tabular}{|l|c|c|c|}
    \hline
    \B{বৈশিষ্ট্য / পদ্ধতি} & \B{ম্যাক্রো পদ্ধতি (Macro)} & \B{সেমি-মাইক্রো পদ্ধতি (Semi-micro)} & \B{মাইক্রো পদ্ধতি (Micro)} \\
    \hline
    ১. দ্রবের ভর (Weight) & $0.5 \text{ g} \rightarrow 1.0 \text{ g}$ & $0.05 \text{ g} \rightarrow 0.1 \text{ g}$ (বা $50\text{-}100\text{ mg}$) & $0.005 \text{ g} \rightarrow 0.01 \text{ g}$ (বা $5\text{-}10\text{ mg}$) \\
    \hline
    ২. দ্রবণের আয়তন (Volume) & $20 \text{ mL} \rightarrow 50 \text{ mL}$ & $2 \text{ mL} \rightarrow 4 \text{ mL}$ & $< 1 \text{ mL}$ (বা $0.1\text{-}0.5\text{ mL}$) \\
    \hline
    ৩. বর্জ্যের পরিমাণ & সবচেয়ে বেশি উৎপন্ন হয় & পরিবেশ বান্ধব ও নিয়ন্ত্রিত & অত্যন্ত কম বা নগণ্য \\
    \hline
    ৪. প্রধান সুবিধা & সাধারণ যন্ত্রেই সহজে করা যায় & রাসায়নিক ও সময়ের সাশ্রয় হয় & অত্যন্ত সূক্ষ্ম ও নিখুঁত বিশ্লেষণ \\
    \hline
    \end{tabular}
    \item \textbf{\B{উচ্চ ক্ষমতাসম্পন্ন আধুনিক যন্ত্রপাতি:}} 
    \begin{itemize}
        \item \B{ক্রোমাটোগ্রাফি (Chromatography):} {\lat HPLC} (High Performance Liquid Chromatography), {\lat GC} (Gas Chromatography) $\rightarrow$ যৌগের পৃথকীকরণ ও বিশুদ্ধতা যাচাই.
        \item \B{স্পেক্ট্রোমেট্রি ও বর্ণালীমিতি:} {\lat IR} (ইনফ্রারেড- কার্যকরী মূলক শনাক্তকরণ), {\lat UV-Vis} (আল্ট্রাভায়োলেট- যৌগের সংযুক্তি ও দ্রবণ পরিমাপ), {\lat NMR} (নিউক্লিয়ার ম্যাগনেটিক রেজোন্যান্স- গাঠনিক কার্বন-হাইড্রোজেন কাঠামো নির্ধারণ).
        \item \B{থার্মো অ্যানালাইসিস:} {\lat DSC} (Differential Scanning Calorimetry) $\rightarrow$ তাপীয় স্থায়িত্ব পরিমাপ.
        \item \B{পারমাণবিক শোষণ বর্ণালি:} {\lat AAS} (Atomic Absorption Spectroscopy) $\rightarrow$ অতি সূক্ষ্ম ভারী ধাতুর পরিমাণ নির্ধারণ.
        \item {\lat X}-\B{রশ্মি কেলাসবিদ্যা (X-ray Crystallography):} কেলাসের ত্রিমাত্রিক অভ্যন্তরীণ গঠন বিশ্লেষণ.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 9.} \B{রাসায়নিক নিক্তি বা ব্যালেন্স (Chemical Balances):}}
\begin{itemize}
    \item \textbf{\B{পল বুঙ্গি নিক্তি (Paul Bunge Balance):}} \B{শুষ্ক পদার্থ অত্যন্ত সূক্ষ্মভাবে ওজন করার জন্য ব্যবহৃত ম্যানুয়াল চার-ডিজিট অ্যানালিটিক্যাল ব্যালেন্স. এর বিমের উপর রাইডার (Rider) ব্যবহার করে সূক্ষ্মতম ভর মাপা হয়.}
    \item \textbf{\B{ডিজিটাল নিক্তি (Digital Balance):}} {\lat 2}-\B{ডিজিট (রূঢ় পরিমাপ),} {\lat 4}-\B{ডিজিট (অত্যন্ত সূক্ষ্ম অ্যানালাইটিক্যাল পরিমাপ).}
    \item \textbf{\B{সেমিমাইক্রো ও মাইক্রো ল্যাব সামগ্রী:}} \B{সেমিমাইক্রো টেস্ট টিউব, সেন্ট্রিফিউজ টিউব, সেন্ট্রিফিউজ যন্ত্র (অধঃক্ষেপ পৃথকীকরণের জন্য), ড্রপিং টিউব, বিকারক ড্রপার, বিকারক বোতল, স্প্যাচুলা, কৈশিক নল, পানিগাহ, বাষ্পীভবন বাটি.}
\end{itemize}

\divider

\textbf{{\lat 10.} \B{রাসায়নিকের বিপদ সংকেত বা GHS হেজার্ড পিক্টোগ্রাম (Hazard Symbols):}}

\begin{tabular}{|l|l|l|}
\hline
\B{পিক্টোগ্রাম চিহ্ন} & \B{ঝুঁকির প্রকৃতি (Nature of Risk)} & \B{সতর্কতামূলক ব্যবস্থা (Precautions)} \\
\hline
১. জ্বলন্ত শিখা (Flammable) & \B{দাহ্য পদার্থ} (যেমন: অ্যালকোহল, ইথার, অ্যাসিটোন) & আগুন ও তাপের উৎস থেকে দূরে শুষ্ক স্থানে রাখা. \\
\hline
২. বিস্ফোরণোন্মুখ বোমা & \B{বিস্ফোরক পদার্থ} (যেমন: অর্গানিক পারক্সাইড, TNT) & আঘাত, ঘর্ষণ বা ঝাঁকুনি থেকে দূরে সাবধানে নাড়াচাড়া করা. \\
\hline
৩. বৃত্তের উপর শিখা (Oxidizing) & \B{জারক পদার্থ (যেমন: হাইড্রোজেন পারক্সাইড,} {\lat $\text{KMnO}_4$}\B{)} & দাহ্য বস্তুর সংস্পর্শ থেকে দূরে আলাদা স্থানে রাখা. \\
\hline
৪. করোটি ও ক্রস বোন (Toxic) & \B{তীব্র বিষাক্ত} (যেমন: নিকোটিন, সায়ানাইড, ক্লোরোফর্ম) & গ্লাভস ও মাস্ক ব্যবহার করা, শ্বাস বা ত্বকের সংস্পর্শ এড়ানো. \\
\hline
৫. অ্যাসিডের ফোঁটা (Corrosive) & \B{ক্ষয়কারী পদার্থ (যেমন: গাঢ়} {\lat $\text{H}_2\text{SO}_4, \text{NaOH}$}\B{)} & চশমা ও নাইট্রাইল গ্লাভস পরা, ত্বকে লাগলে দ্রুত ধোয়া. \\
\hline
৬. মরা গাছ ও মাছ & \B{পরিবেশের জন্য ঝুঁকিপূর্ণ} (যেমন: ক্লোরিন, ভারী ধাতু) & ড্রেন বা সাধারণ বর্জ্যে না ফেলে নির্দিষ্ট শোধন পাত্রে রাখা. \\
\hline
\end{tabular}

\divider

\textbf{{\lat 11.} \B{চিকিৎসা} $\rightarrow$ \B{ফার্স্ট এইড বক্স (First Aid Box):}}
\begin{itemize}
    \item \B{অ্যাসিটামিনোফেন (প্যারাসিটামল), অ্যাডহেসিভ ব্যান্ডেজ, অ্যাডহেসিভ টেপ ১/২'' চওড়া ২-৩ গজ, অ্যান্টিসেপটিক তোয়ালে (২/৩টি)}
    \item \B{অ্যাসপিরিন ট্যাবলেট (২ প্যাকেট), পুড়ে যাওয়া ক্ষত স্থানের জন্য} {\lat First Aid Cream / Burnol}, \B{তুলা (৫০০ গ্রাম)}
    \item \B{ইলাস্টিক ব্যান্ডেজ (২'' চওড়া ৫ গজ), আই প্যাড (Eye Pad), আই ওয়াশ (চোখ ধোয়ার বোরিক এসিডের লঘু দ্রবণ), ফরসেপ, গজ ব্যান্ডেজ}
    \item \B{গজ প্যাড, রাবারের গ্লাভস, ননস্টিক প্যাড, ছোট/বড় (২/৩টি) কাঁচি, স্প্লিন্টার রিমুভার, স্যাভলন বা ডেটল (২৫০ মিলি) ইত্যাদি.}
    \item \B{ল্যাবে ক্ষতের তাৎক্ষণিক প্রাথমিক চিকিৎসা:} 
    \begin{itemize}
        \item \B{এসিড পুড়লে:} আক্রান্ত স্থান প্রচুর পানি দিয়ে ধুয়ে ৫\% সোডিয়াম বাইকার্বনেট [{\lat $\text{NaHCO}_3$}] দ্রবণ যোগ করতে হবে.
        \item \B{ক্ষার পুড়লে:} প্রচুর পানি দিয়ে ধুয়ে ৫\% বোরিক এসিড [{\lat $\text{H}_3\text{BO}_3$}] বা লঘু অ্যাসিটিক এসিড দ্রবণ প্রয়োগ করতে হবে.
    \end{itemize}
\end{itemize}

\divider
\divider

\chsub{}{প্রয়োজনীয় সূত্রাবলি (Key Formulas)}

\itm{1} \textbf{\B{মোলার ঘনমাত্রা (Molarity),}} {\lat $S = \dfrac{w \times 1000}{M \times V_{mL}}$} \B{ অথবা } {\lat $w = \dfrac{S \times M \times V_{mL}}{1000}$}
\begin{itemize}
    \item[] {\lat $S$} = \B{মোলার ঘনমাত্রা বা শক্তিমাত্রা} {\lat $[M, \text{ mol L}^{-1}]$}
    \item[] {\lat $w$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{দ্রবের আণবিক ভর (যেমন- $\text{Na}_2\text{CO}_3$ এর জন্য $106\text{ g mol}^{-1}$)}
    \item[] {\lat $V_{mL}$} = \B{মিলিলিটারে দ্রবণের আয়তন} {\lat [mL]}
\end{itemize}

\divider

\itm{2} \textbf{\B{এসিড-ক্ষার অনুমাপণের মূলতত্ত্ব (Titration Formula),}} {\lat $\dfrac{V_A \times S_A}{x} = \dfrac{V_B \times S_B}{y}$}
\B{সাধারণ রাসায়নিক বিক্রিয়া: } {\lat $x\text{Acid} + y\text{Base} \rightarrow \text{Salt} + \text{Water}$}
\begin{itemize}
    \item[] {\lat $V_A$} = \B{এসিডের আয়তন}, {\lat $V_B$} = \B{ক্ষারের আয়তন} {\lat [L, mL]}
    \item[] {\lat $S_A$} = \B{এসিডের মোলার ঘনমাত্রা}, {\lat $S_B$} = \B{ক্ষারের মোলার ঘনমাত্রা} {\lat [M]}
    \item[] {\lat $x$} = \B{সমতাকৃত বিক্রিয়ায় এসিডের মোল সংখ্যা}, {\lat $y$} = \B{ক্ষারের মোল সংখ্যা}
\end{itemize}

\divider

\itm{3} \textbf{\B{দ্রবণ লঘুকরণ সূত্র (Dilution Law),}} {\lat $V_1 S_1 = V_2 S_2$}
\begin{itemize}
    \item[] {\lat $V_1$} = \B{লঘুকরণের পূর্বে আদি বা উচ্চতর ঘনমাত্রার আয়তন} {\lat [L, mL]}
    \item[] {\lat $S_1$} = \B{আদি বা উচ্চতর ঘনমাত্রার মোলারিটি} {\lat [M]}
    \item[] {\lat $V_2$} = \B{লঘুকরণের পর মোট কাঙ্ক্ষিত আয়তন} {\lat [L, mL]}
    \item[] {\lat $S_2$} = \B{লঘুকরণের পর প্রাপ্ত নিম্নতর বা কাঙ্ক্ষিত মোলারিটি} {\lat [M]}
    \item[] \textbf{\B{যোগকৃত পানির আয়তন:}} {\lat $V_{\text{water}} = V_2 - V_1$}
\end{itemize}

\divider

\itm{4} \textbf{\B{রাইডার ধ্রুবক (Rider Constant - RC) গণনা পদ্ধতি:}}

\sub{i} \B{যখন রাসায়নিক নিক্তির বিমের সর্ববামে} {\lat 0} \B{দাগ এবং সর্বডানে} {\lat 100} \B{দাগ থাকে (মাঝখানে ৫০ দাগ):}
${\text{\B{রাইডার ধ্রুবক (RC)}} = \dfrac{2 \times \text{\B{রাইডারের ভর (g)}}}{\text{\B{বিমের মোট দাগ সংখ্যা}}} = \dfrac{2 \times w_R}{100} \;\; \text{[g]}}$

\sub{ii} \B{যখন রাসায়নিক নিক্তির বিমের ঠিক মাঝখানে} {\lat 0} \B{দাগ এবং ডানে ও বামে সর্বোচ্চ} {\lat 50} \B{করে দাগ থাকে:}
${\text{\B{রাইডার ধ্রুবক (RC)}} = \dfrac{\text{\B{রাইডারের ভর (g)}}}{\text{\B{বিমের এক পাশের দাগ সংখ্যা}}} = \dfrac{w_R}{50} \;\; \text{[g]}}$

\sub{iii} \B{নিক্তিতে মোট ওজন পরিমাপের সমীকরণ:}
${\text{\B{মোট ভর}} = \text{\B{বাম পাল্লার ওজন}} + (\text{\B{রাইডারের অবস্থান}} \times \text{\B{রাইডার ধ্রুবক}})}$
\B{[দ্রষ্টব্য: মাঝখানে শূন্য দাগবিশিষ্ট নিক্তির ক্ষেত্রে রাইডার ডানদিকের বাহুতে থাকলে মান যোগ হয় এবং বামদিকের বাহুতে থাকলে বিয়োগ হয়.]}

\chsec{অধ্যায়-২: গুণগত রসায়ন (Qualitative Chemistry)}

\chsub{Concept Map: The Chapter at a Glance}{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: পরমাণুর গঠন, বর্ণালিমিতি এবং দ্রাব্যতা সাম্যাবস্থা}}

\divider

\textbf{{\lat 1.} \B{মূল কণিকা (Fundamental Particles):}}
\begin{itemize}
    \item \textbf{\B{স্থায়ী মূল কণিকা:}} \B{ইলেকট্রন (} \lat $e^-$ \B{), প্রোটন (} \lat $p^+$ \B{), নিউট্রন (} \lat $n$ \B{).}
    \begin{itemize}
        \item \B{ইলেকট্রন:} আধান $= -1.6 \times 10^{-19}\text{ C}$, ভর $= 9.11 \times 10^{-31}\text{ kg}$ বা $0.000548\text{ amu}$. আবিষ্কারক স্যার জে. জে. থমসন.
        \item \B{প্রোটন:} আধান $= +1.6 \times 10^{-19}\text{ C}$, ভর $= 1.673 \times 10^{-27}\text{ kg}$ বা $1.007276\text{ amu}$. আবিষ্কারক আর্নেস্ট রাদারফোর্ড.
        \item \B{নিউট্রন:} আধান $= 0$ (নিরপেক্ষ), ভর $= 1.675 \times 10^{-27}\text{ kg}$ বা $1.008665\text{ amu}$. আবিষ্কারক জেমস চ্যাডউইক.
    \end{itemize}
    \item \textbf{\B{অস্থায়ী মূল কণিকা:}} \B{নিউট্রিনো, অ্যান্টিনিউট্রিনো, পজিট্রন (} \lat $e^+$ \B{), মেসন, পাইওন, মিউওন.}
    \item \textbf{\B{কম্পোজিট কণা (Composite Particles):}} \B{ভারী বা বহু-কণাবিশিষ্ট গুচ্ছ. যেমন: আলফা কণা (} \lat $\alpha\text{-particle / He}^{2+}$ \B{), ডিউটেরন কণা (} \lat $^2_1\text{H}^+$ \B{).}
\end{itemize}

\divider

\textbf{{\lat 2.} \B{আণবিক মডেল সমূহ} $\rightarrow$ \B{রাদারফোর্ডের পরমাণু মডেল (Solar System Model):}}
\begin{itemize}
    \item \textbf{\B{আলফা কণা বিচ্ছুরণ পরীক্ষার উপকরণসমূহ (Alpha Scattering Experiment):}} 
    \begin{itemize}
        \item তেজস্ক্রিয় মৌল (যেমন: রেডিয়াম \lat Ra \B{ বা ইউরেনিয়াম } \lat U) থেকে নির্গত তীব্র গতিসম্পন্ন হিলিয়াম নিউক্লিয়াস বা \lat $\alpha$-কণা ($^4_2\text{He}^{2+}$).
        \item অতি পাতলা সোনার পাত (পুরুত্ব প্রায় \lat $0.0004\text{ cm}$ বা $4 \times 10^{-5}\text{ cm}$).
        \item জিংক সালফাইড (\lat ZnS) এর প্রলেপযুক্ত প্রতিপ্রভ পর্দা (Scintillation Screen).
    \end{itemize}
    \item \textbf{\B{পর্যবেক্ষণ ও সিদ্ধান্ত:}}
    \begin{itemize}
        \item প্রায় ৯৯% $\alpha$-কণাই সোনার পাত ভেদ করে সোজা চলে যায় $\rightarrow$ পরমাণুর অভ্যন্তরভাগ মূলত ফাঁকা.
        \item মাত্র অল্প কিছু কণা সামান্য বেঁকে যায় এবং ২০,০০০ এর মধ্যে ১টি কণা যে পথে গিয়েছিল ঠিক সেই পথেই ১৮০° কোণে সোজা ফিরে আসে $\rightarrow$ পরমাণুর কেন্দ্রে পরমাণুর সমস্ত ধনাত্মক চার্জ এবং প্রায় সমস্ত ভর (প্রায় ৯৯.৯৭\%) অতি ক্ষুদ্র স্থান দখল করে কেন্দ্রীভূত আছে. রাদারফোর্ড এই কেন্দ্রের নাম দেন \textbf{নিউক্রিয়াস}.
        \item পরমাণুর ব্যাস ($10^{-8}\text{ cm}$) নিউক্লিয়াসের ব্যাসের ($10^{-13}\text{ cm}$) চেয়ে প্রায় ১০,০০০ থেকে ১,০০,০০০ গুণ বড়.
    \end{itemize}
    \item \textbf{\B{সীমাবদ্ধতা:}} 
    \begin{itemize}
        \item সৌরজগতের সূর্য ও গ্রহসমূহ সামগ্রিকভাবে আধানহীন, কিন্তু নিউক্লিয়াস ও ইলেকট্রনসমূহ আধানযুক্ত. আধানহীন বস্তুর সাথে আধানযুক্ত কণার এই তুলনা ত্রুটিপূর্ণ.
        \item ম্যাক্সওয়েলের তড়িৎ-চৌম্বকীয় তত্ত্বানুসারে, কোনো আধানযুক্ত কণা বৃত্তাকার পথে ঘুরলে তা অনবরত শক্তি বিকিরণ করবে এবং তার আবর্তন চক্রের ব্যাসার্ধ কমতে কমতে একসময় ইলেকট্রনটি নিউক্লিয়াসে পতিত হবে. ফলে রাদারফোর্ড মডেলের স্থায়িত্ব থাকে না.
        \item হাইড্রোজেন পরমাণুর রেখা বর্ণালী (\lat Line Spectrum) সৃষ্টির কোনো ব্যাখ্যা এ মডেলে পাওয়া যায় না.
        \item আবর্তনশীল ইলেকট্রনের কক্ষপথের আকার (Size) ও আকৃতি (Shape) সম্বন্ধে কোনো ধারণা দেওয়া হয় নি.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 3.} \B{আণবিক মডেল সমূহ} $\rightarrow$ \B{বোর মডেল (Bohr Atomic Model):}}
\begin{itemize}
    \item \textbf{\B{ভিত্তি মতবাদ:}} \B{ম্যাক্স প্ল্যাঙ্কের কোয়ান্টাম তত্ত্ব (Quantum Theory).}
    \item \textbf{\B{প্রধান স্বীকার্যসমূহ (Postulates):}}
    \sub{i} \B{স্থির কক্ষপথ বা শক্তিস্তরের ধারণা (Orbit):} নিউক্লিয়াসকে কেন্দ্র করে ইলেকট্রনসমূহ নির্দিষ্ট কতগুলো বৃত্তাকার অনুমোদিত কক্ষপথে আবর্তন করে. এদের প্রধান শক্তিস্তর বা শেল (\lat $n = 1, 2, 3, \ldots$) বলে. স্থির কক্ষপথে আবর্তনের সময় ইলেকট্রন কোনো শক্তি শোষণ বা বিকিরণ করে না.
    \sub{ii} \B{কৌণিক ভরবেগের ধারণা (Angular Momentum):} একটি নির্দিষ্ট শক্তিস্তরে আবর্তনশীল ইলেকট্রনের কৌণিক ভরবেগ ($\displaystyle mvr$) সর্বদা $\displaystyle \frac{h}{2\pi}$ এর অখণ্ড পূর্ণাঙ্গ গুণিতক. অর্থাৎ, \lat $mvr = \frac{nh}{2\pi}$.
    \sub{iii} \B{শক্তির শোষণ-বিকিরণ ও বর্ণালি সৃষ্টি (Energy Transition):} ইলেকট্রন নিম্ন শক্তিস্তর ($E_1$) থেকে উচ্চ শক্তিস্তরে ($E_2$) লাফিয়ে চলার সময় নির্দিষ্ট পরিমাণ শক্তি শোষণ করে এবং উচ্চ স্তর থেকে নিম্ন স্তরে নেমে আসার সময় শক্তি বিকিরণ করে. এই বিকিরিত শক্তি প্রিজমের মধ্য দিয়ে প্রবেশ করলে বর্ণালির সৃষ্টি হয়. শক্তির সমীকরণ: \lat $\Delta E = E_2 - E_1 = h\nu = \frac{hc}{\lambda}$.
    \item \textbf{\B{সাফল্য:}} 
    \begin{itemize}
        \item পরমাণুর স্থায়িত্ব সুচারুভাবে ব্যাখ্যা করতে পারে.
        \item এক ইলেকট্রনবিশিষ্ট পরমাণু বা আয়নের (যেমন: \lat $\text{H}, \text{He}^+, \text{Li}^{2+}, \text{Be}^{3+}$) রেখা বর্ণালী নিখুঁতভাবে ব্যাখ্যা করতে পারে.
        \item বোর ব্যাসার্ধ ($r_1 = 0.5292 \times 10^{-8}\text{ cm}$) এবং হাইড্রোজেন পরমাণুর প্রথম কক্ষপথে ইলেকট্রনের শক্তি গণনা সম্ভব হয়.
        \item রিডবার্গ ধ্রুবকের তাত্ত্বিক মান নির্ণয় করা যায়.
    \end{itemize}
    \item \textbf{\B{সীমাবদ্ধতা:}}
    \begin{itemize}
        \item বহু ইলেকট্রনবিশিষ্ট পরমাণুসমূহের জটিল বর্ণালি ব্যাখ্যা করতে সম্পূর্ণ ব্যর্থ.
        \item উচ্চ ক্ষমতাসম্পন্ন বর্ণালিবীক্ষণ যন্ত্রের সাহায্যে পরীক্ষা করলে দেখা যায় যে প্রতিটি প্রধান বর্ণালী রেখা আবার একাধিক সূক্ষ্ম রেখায় বিভক্ত. বোর মডেল এই সূক্ষ্ম রেখা সৃষ্টির কারণ ব্যাখ্যা করতে পারে না.
        \item জিম্যান প্রভাব (\lat Zeeman Effect: চৌম্বক ক্ষেত্রের প্রভাবে বর্ণালী রেখার বিভাজন) এবং স্টার্ক প্রভাব (\lat Stark Effect: তড়িৎ ক্ষেত্রের প্রভাবে বর্ণালী রেখার বিভাজন) ব্যাখ্যা করতে পারে না.
        \item এটি হাইজেনবার্গের অনিশ্চয়তা নীতি লঙ্ঘন করে, কারণ বোর মডেলে ইলেকট্রনের অবস্থান ও বেগ একই সাথে সুনির্দিষ্টভাবে নির্ণয় করা হয়েছে.
    \end{itemize}
\end{itemize}



\divider

\textbf{{\lat 4.} \B{কোয়ান্টাম বলবিদ্যা ও আধুনিক পরমাণু তত্ত্বের বিকাশ:}}
\begin{itemize}
    \item \textbf{\B{নীলস বোর (১৯১৩ খ্রি.):}} প্রথম কোয়ান্টায়িত বৃত্তাকার কক্ষপথ বা প্রধান শক্তিস্তরের ধারণা প্রবর্তন করেন.
    \item \textbf{\B{লুই ডি-ব্রগলি (১৯২৪ খ্রি.):}} ইলেকট্রনের কণা ও তরঙ্গ উভয় ধর্মের সমন্বয় ঘটিয়ে পদার্থের দ্বৈত নীতি (\lat Dual Nature of Matter) প্রদান করেন. সমীকরণ: $\displaystyle \lambda = \frac{h}{mv}$.
    \item \textbf{\B{আরউইন শ্রোডিঞ্জার (১৯২৬ খ্রি.):}} ইলেকট্রনের তরঙ্গ ধর্মকে ভিত্তি করে ত্রিমাত্রিক ক্ষেত্রে অরবিটালে ইলেকট্রন পাওয়ার সম্ভাবনা বলয় নির্দেশক বিখ্যাত ত্রিমাত্রিক তরঙ্গ সমীকরণ প্রদান করেন.
    \item \textbf{\B{ওয়ার্নার হাইজেনবার্গ (১৯২৭ খ্রি.):}} অনিশ্চয়তা নীতি (\lat Uncertainty Principle) প্রদান করেন. এই নীতি অনুযায়ী, কোনো অতি ক্ষুদ্র গতিশীল কণার (যেমন ইলেকট্রন) অবস্থান ($\Delta x$) এবং ভরবেগ ($\Delta p$) একই সাথে নিখুঁতভাবে নিশ্চিত করা অসম্ভব. সমীকরণ: $\displaystyle \Delta x \cdot \Delta p \geq \frac{h}{4\pi}$.
\end{itemize}

\divider

\textbf{{\lat 5.} \B{কোয়ান্টাম সংখ্যা (Quantum Numbers):}}
\B{পরমাণুতে অবস্থিত কোনো ইলেকট্রনের কক্ষপথের আকার, আকৃতি, ত্রিমাত্রিক দিক-বিন্যাস এবং ইলেকট্রনের ঘূর্ণনের দিক সম্পূর্ণ প্রকাশ করার জন্য যে চারটি সূচক সংখ্যা ব্যবহৃত হয়, তাদের কোয়ান্টাম সংখ্যা বলে.}

\begin{tabular}{|l|c|c|l|}
\hline
\B{কোয়ান্টাম সংখ্যার নাম} & \B{প্রতীক} & \B{অনুমোদিত মানসমূহ} & \B{তাৎপর্য / ভৌত রূপ} \\
\hline
১. প্রধান কোয়ান্টাম সংখ্যা & $n$ & $n = 1, 2, 3, 4, \ldots$ & কক্ষপথের প্রধান আকার ও শক্তিস্তর (Shell: K, L, M, N) নির্দেশ করে. \\
\hline
২. সহকারী / অ্যাজিমুথাল & $l$ & $l = 0$ থেকে $(n-1)$ & উপশক্তিস্তরের আকৃতি (Subshell: s, p, d, f) ও কৌণিক ভরবেগ জানায়. \\
\hline
৩. চৌম্বকীয় (Magnetic) & $m$ & $m = -l$ থেকে $+l$ (শূন্যসহ) & উপশক্তিস্তরের ত্রিমাত্রিক দিক-বিন্যাস ও মোট অরবিটাল সংখ্যা নির্দেশ করে. \\
\hline
৪. ঘূর্ণন (Spin) & $s$ & $s = +\dfrac{1}{2}, -\dfrac{1}{2}$ & ইলেকট্রনটির নিজস্ব অক্ষের চারদিকে ঘূর্ণনের দিক (ক্লকওয়াইজ/অ্যান্টিক্লকওয়াইজ). \\
\hline
\end{tabular}

\divider

\textbf{{\lat 6.} \B{উপশক্তিস্তর ও অরবিটাল ধারণার বিস্তারিত রূপ (Orbital Configurations):}}
\begin{itemize}
    \item \B{অরবিটাল শক্তির উপস্তরসমূহ ও তাদের আকৃতি:}
    \begin{itemize}
        \item \lat $l = 0 \rightarrow s$\B{-অরবিটাল:} আকৃতি গোলাকার (Spherical). সর্বোচ্চ ইলেকট্রন ধারণ ক্ষমতা ২টি.
        \item \lat $l = 1 \rightarrow p$\B{-অরবিটাল:} আকৃতি ডাম্বেলকার (Dumbbell). তিনটি ত্রিমাত্রিক বিন্যাস: $p_x, p_y, p_z$. সর্বোচ্চ ইলেকট্রন ধারণ ক্ষমতা ৬টি.
        \item \lat $l = 2 \rightarrow d$\B{-অরবিটাল:} আকৃতি ডাবল-ডাম্বেলকার (Double Dumbbell). পাঁচটি বিন্যাস: $d_{xy}, d_{yz}, d_{zx}, d_{x^2-y^2}, d_{z^2}$. সর্বোচ্চ ইলেকট্রন ধারণ ক্ষমতা ১০টি.
        \item \lat $l = 3 \rightarrow f$\B{-অরবিটাল:} অত্যন্ত জটিল গাঠনিক আকৃতি. সাতটি বিন্যাসযুক্ত. সর্বোচ্চ ইলেকট্রন ধারণ ক্ষমতা ১৪টি.
    \end{itemize}
    \item \B{ধারণক্ষমতার সূত্রসমূহ:}
    \begin{itemize}
        \item যেকোনো উপশক্তিস্তরে মোট অরবিটাল সংখ্যা $= (2l + 1)$ এবং মোট ইলেকট্রন ধারণ ক্ষমতা $= 2(2l + 1)$.
        \item যেকোনো প্রধান শক্তিস্তরে মোট অরবিটাল সংখ্যা $= n^2$ এবং মোট ইলেকট্রন ধারণ ক্ষমতা $= 2n^2$.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 7.} \B{ইলেকট্রন বিন্যাসের নিয়মাবলী ও ব্যতিক্রম (Principles of Electron Configuration):}}
\sub{i} \B{আউফবাউ নীতি (Building-up Principle / $(n+l)$ Rule):} ইলেকট্রন প্রথমে সর্বনিম্ন শক্তির অরবিটালে প্রবেশ করবে এবং ক্রমান্বয়ে উচ্চ শক্তির অরবিটাল পূর্ণ করবে. অরবিটালের শক্তি নির্ধারিত হয় $(n+l)$ এর মান দ্বারা.
\begin{itemize}
    \item যার $(n+l)$ এর মান কম, তার শক্তি কম (যেমন: $4s \rightarrow 4+0=4$; $3d \rightarrow 3+2=5$; তাই ইলেকট্রন আগে $4s$-এ যায়).
    \item যদি দুটি অরবিটালের $(n+l)$ এর মান সমান হয়, তবে যার প্রধান কোয়ান্টাম সংখ্যা ($n$) এর মান কম, তার শক্তি কম এবং ইলেকট্রন আগে সেখানে প্রবেশ করবে (যেমন: $3d \rightarrow 3+2=5$ এবং $4p \rightarrow 4+1=5$; এখানে $3d$ এর $n$ ছোট হওয়ায় এটি নিম্ন শক্তির).
    \item \B{শক্তির সাধারণ ক্রম:} $1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < 6s < 4f \dots$
\end{itemize}
\sub{ii} \B{হুন্ডের নীতি (Hund's Rule of Maximum Multiplicity):} সমশক্তির অরবিটালসমূহে (যেমন: $p_x, p_y, p_z$) ইলেকট্রনগুলো এমনভাবে প্রবেশ করবে যেন তারা সর্বাধিক সংখ্যায় অয়ুগ্ম বা বিজোড় অবস্থায় থাকতে পারে. এই বিজোড় ইলেকট্রনগুলোর স্পিন সর্বদা একই মুখী (সমমুখী) হবে.
\sub{iii} \B{পলির বর্জন নীতি (Pauli's Exclusion Principle):} একটি একই পরমাণুতে যেকোনো দুটি ইলেকট্রনের চারটি কোয়ান্টাম সংখ্যার মান কখনো এক বা অভিন্ন হতে পারে না. অন্ততপক্ষে ঘূর্ণন কোয়ান্টাম সংখ্যা ($s$) অবশ্যই ভিন্ন হবে.
\sub{iv} \B{ইলেকট্রন বিন্যাসের বিশেষ ব্যতিক্রম (Stability of Half-filled \& Full-filled Orbits):} সমশক্তির অরবিটালসমূহ অর্ধপূর্ণ ($s^1, p^3, d^5, f^7$) বা সম্পূর্ণ পূর্ণ ($s^2, p^6, d^{10}, f^{14}$) থাকলে সেই ইলেকট্রন বিন্যাস অধিক সুস্থিতি অর্জন করে.
\begin{itemize}
    \item \B{ক্রোমিয়াম (Cr, Z = 24):} সাধারণ নিয়মে $[Ar]\,3d^4\,4s^2$ হওয়ার কথা থাকলেও সুস্থিতির জন্য হয় $\mathbf{[Ar]\,3d^5\,4s^1}$.
    \item \B{কপার (Cu, Z = 29):} সাধারণ নিয়মে $[Ar]\,3d^9\,4s^2$ হওয়ার কথা থাকলেও সুস্থিতির জন্য হয় $\mathbf{[Ar]\,3d^{10}\,4s^1}$.
\end{itemize}

\divider

\textbf{{\lat 8.} \B{তড়িৎ-চৌম্বকীয় বর্ণালি ও হাইড্রোজেন পরমাণুর রেখা সিরিজ (Electromagnetic Spectrum):}}
\B{উচ্চ শক্তিস্তর থেকে ইলেকট্রন যখন নিম্ন শক্তিস্তরে স্থানান্তরিত হয়, তখন নির্গত রশ্মির তরঙ্গদৈর্ঘ্যের ওপর ভিত্তি করে বিভিন্ন অঞ্চলের সৃষ্টি হয়.}



\begin{tabular}{|l|c|c|c|l|}
\hline
\B{সিরিজের নাম} & \B{নিম্ন স্তর ($n_1$)} & \B{উচ্চ স্তর ($n_2$)} & \B{বর্ণালি অঞ্চল (Region)} & \B{ব্যবহারিক প্রয়োগ ও ভৌত বৈশিষ্ট্য} \\
\hline
১. লাইম্যান (Lyman) & $n_1 = 1$ & $n_2 = 2, 3, 4, \dots$ & অতিবেগুনি (UV) & জাল নোট ও পাসপোর্ট শনাক্তকরণ \\
\hline
২. বামার (Balmer) & $n_1 = 2$ & $n_2 = 3, 4, 5, \dots$ & দৃশ্যমান (Visible) & একমাত্র দৃশ্যমান রেখা (বেগুনি-লাল) \\
\hline
৩. প্যাশ্চেন (Paschen) & $n_1 = 3$ & $n_2 = 4, 5, 6, \dots$ & নিকট অবলোহিত (Near IR) & চিকিৎসাবিজ্ঞানে থেরাপিতে \\
\hline
৪. ব্র্যাকেট (Brackett) & $n_1 = 4$ & $n_2 = 5, 6, 7, \dots$ & মধ্য অবলোহিত (Middle IR) & অণু ও বন্ধন বিশ্লেষণ \\
\hline
৫. ফুন্ড (Pfund) & $n_1 = 5$ & $n_2 = 6, 7, 8, \dots$ & দূর অবলোহিত (Far IR) & টিস্যু ও ফিজিওথেরাপি \\
\hline
৬. হামফ্রেজ (Humphreys) & $n_1 = 6$ & $n_2 = 7, 8, 9, \dots$ & সুদূর অবলোহিত (Far IR) & জ্যোতির্বিদ্যা ও কসমোলজি \\
\hline
\end{tabular}

\divider

\textbf{{\lat 9.} \B{তড়িৎ-চৌম্বকীয় বিকিরণের ব্যবহারিক প্রয়োগসমূহ:}}
\begin{itemize}
    \item \textbf{\B{UV (Ultra-Violet) রশ্মি:}} জাল পাসপোর্ট, জাল টাকা ও ব্যাংক নোট শনাক্তকরণে ফসফর নামক রাসায়নিকের প্রতিপ্রভ আলোক ছটা তৈরিতে ব্যবহৃত হয় (তরঙ্গদৈর্ঘ্য পরিসর প্রায় $230\text{-}375\text{ nm}$).
    \item \textbf{\B{IR (Infra-Red) রশ্মি:}} চিকিৎসাক্ষেত্রে রক্ত সঞ্চালন বৃদ্ধি, পেশীর ব্যথা উপশম ও লেজার সার্জারিতে. সুদূর অবলোহিত রশ্মি (Far-IR) মানবদেহের জৈবিক কোষকে উদ্দীপিত করতে ব্যবহৃত হয়.
    \item \textbf{\B{MRI (Magnetic Resonance Imaging):}} মানবদেহের নরম টিস্যু ও ভেতরের অঙ্গের স্পষ্ট ত্রিমাত্রিক প্রতিচ্ছবি তৈরির অত্যন্ত নিরাপদ রোগ নির্ণয় পদ্ধতি. এতে শক্তিশালী চৌম্বক ক্ষেত্র ও রেডিও তরঙ্গ (Radio Waves) ব্যবহার করে হাইড্রোজেন প্রোটনের স্পিন পরিবর্তন পরিমাপ করা হয়.
\end{itemize}

\divider

\textbf{{\lat 10.} \B{দ্রাব্যতা ও দ্রাব্যতা গুণফল সাম্যাবস্থা (Solubility and Precipitation):}}
\begin{itemize}
    \item \B{দ্রাব্যতা (Solubility, S):} নির্দিষ্ট তাপমাত্রায় $100\text{ g}$ দ্রাবককে সম্পৃক্ত দ্রবণে পরিণত করতে যত গ্রাম দ্রবের প্রয়োজন হয় তাকে ওই তাপমাত্রায় ওই দ্রবের দ্রাব্যতা বলে. এর কোনো একক নেই. তবে আধুনিক রসায়নে মোলার দ্রাব্যতাকে একক ধরা হয় যার একক $\text{mol L}^{-1}$ বা $\text{M}$.
    \item \B{আয়নিক গুণফল ($K_{ip}$) ও দ্রাব্যতা গুণফল ($K_{sp}$):}
    \begin{itemize}
        \item \B{আয়নিক গুণফল ($K_{ip}$):} যেকোনো অবস্থায় (অসম্পৃক্ত, সম্পৃক্ত বা অতিপৃক্ত) দ্রবণে উপস্থিত আয়নসমূহের উপযুক্ত ঘাতসহ ঘনমাত্রার গুণফল.
        \item \B{দ্রাব্যতা গুণফল ($K_{sp}$):} নির্দিষ্ট তাপমাত্রায় কোনো স্বল্পদ্রাব্য লবণের সম্পৃক্ত দ্রবণে তার উপাদান আয়নসমূহের উপযুক্ত ঘাতসহ মোলার ঘনমাত্রার সর্বোচ্চ ধ্রুবক গুণফল.
    \end{itemize}
    \item \B{অধঃক্ষেপণের শর্তাবলী (Conditions for Precipitation):}
    \begin{itemize}
        \item যদি $K_{ip} < K_{sp}$ হয় $\rightarrow$ দ্রবণটি \textbf{অসম্পৃক্ত (Unsaturated)}. কোনো অধঃক্ষেপ পড়বে না এবং আরও দ্রব দ্রবীভূত করা যাবে.
        \item যদি $K_{ip} = K_{sp}$ হয় $\rightarrow$ দ্রবণটি \textbf{সম্পৃক্ত (Saturated)}. দ্রবণটি সাম্যাবস্থায় থাকবে এবং কোনো অধঃক্ষেপ পড়বে না.
        \item যদি $K_{ip} > K_{sp}$ হয় $\rightarrow$ দ্রবণটি \textbf{অতিপৃক্ত (Supersaturated)}. অতিরিক্ত দ্রব পাত্রের নিচে \textbf{অধঃক্ষিপ্ত (Precipitated)} হবে.
    \end{itemize}
    \item \B{সম-আয়ন প্রভাব (Common Ion Effect):} কোনো স্বল্পদ্রাব্য লবণের দ্রবণে একটি তীব্র তড়িৎ-বিশ্লেষ্য একই আয়নযুক্ত যৌগ যোগ করলে স্বল্পদ্রাব্য লবণটির বিয়োজন মাত্রা এবং দ্রাব্যতা উভয়ই মারাত্মকভাবে হ্রাস পায়. এই ঘটনাকে সম-আয়ন প্রভাব বলে. যেমন: $\text{AgCl}$ এর সম্পৃক্ত দ্রবণে $\text{NaCl}$ যোগ করলে সম-আয়ন $\text{Cl}^-$ এর প্রভাবে $\text{AgCl}$ এর দ্রাব্যতা হ্রাস পেয়ে পুনরায় অধঃক্ষেপ পড়ে.
\end{itemize}

\divider
\divider

\chsub{}{প্রয়োজনীয় সূত্রাবলি (Mathematical Formulas)}

\itm{1} \textbf{\B{ভরত্রুটি (Mass Defect),}} {\lat $\Delta m = \{Z \cdot m_p + (A - Z) \cdot m_n\} - M$}
\begin{itemize}
    \item[] {\lat $\Delta m$} = \B{নিউক্লিয়াসের ভরত্রুটি} {\lat $[\text{amu}$} \B{বা} {\lat $\text{ kg}]$}
    \item[] {\lat $Z$} = \B{পারমাণবিক সংখ্যা / প্রোটন সংখ্যা}
    \item[] {\lat $m_p$} = \B{একটি মুক্ত প্রোটনের ভর} {\lat $[1.007276\text{ amu}$} \B{বা} {\lat $1.673 \times 10^{-27}\text{ kg}]$}
    \item[] {\lat $A$} = \B{ভরসংখ্যা (প্রোটন + নিউট্রন সংখ্যা)}
    \item[] {\lat $m_n$} = \B{একটি মুক্ত নিউট্রনের ভর} {\lat $[1.008665\text{ amu}$} \B{বা} {\lat $1.675 \times 10^{-27}\text{ kg}]$}
    \item[] {\lat $M$} = \B{নিউক্লিয়াসের প্রকৃত পরীক্ষামূলক ভর} {\lat $[\text{amu}$} \B{বা} {\lat $\text{ kg}]$}
    \item[] \textbf{\B{নিউক্লিয়ার বন্ধন শক্তি (Binding Energy):}} $E = \Delta m \cdot c^2$ \B{ [যদি $\Delta m$ amu এককে থাকে, তবে $E = \Delta m \times 931.5\text{ MeV}$]}
\end{itemize}

\divider

\itm{2} \textbf{\B{নিউক্লিয়াসে নিউট্রন সংখ্যা,}} {\lat $Q = (A - Z)$}
\begin{itemize}
    \item[] {\lat $Q$} = \B{নিউট্রন সংখ্যা}, {\lat $A$} = \B{ভরসংখ্যা}, {\lat $Z$} = \B{পারমাণবিক সংখ্যা}
\end{itemize}

\divider

\itm{3} \textbf{\B{মৌলের আপেক্ষিক পারমাণবিক ভর (Relative Atomic Mass),}}
$$\text{আপেক্ষিক পারমাণবিক ভর} = \dfrac{\text{\B{মৌলের ১টি পরমাণুর ভর (g)}}}{\dfrac{1}{12} \times \text{\B{কার্বন-12 এর একটি পরমাণুর ভর}}} = \dfrac{\text{\B{মৌলের ১টি পরমাণুর ভর (g)}}}{1.66 \times 10^{-24}\text{ g}}$$

\divider

\itm{4} \textbf{\B{আইসোটোপের প্রাচুর্য থেকে গড় পারমাণবিক ভর নির্ণয়,}} {\lat $M = \dfrac{(p_1 \times m_1) + (p_2 \times m_2) + \dots + (p_n \times m_n)}{100}$}
\begin{itemize}
    \item[] {\lat $p_1, p_2, \dots$} = \B{যথাক্রমে ১ম, ২য় ও $n$-তম আইসোটোপের প্রকৃত ভর সংখ্যা}
    \item[] {\lat $m_1, m_2, \dots$} = \B{যথাক্রমে প্রকৃতিতে ১ম, ২য় ও $n$-তম আইসোটোপের শতকরা প্রাচুর্যের পরিমাণ (\%)}
\end{itemize}

\divider

\itm{5} \textbf{\B{প্ল্যাঙ্কের কোয়ান্টাম সমীকরণ,}} {\lat $\Delta E = h\nu = \dfrac{hc}{\lambda} = hc\bar{\nu}$}
\begin{itemize}
    \item[] {\lat $\Delta E$} = \B{বিকিরিত বা শোষিত কোয়ান্টাম শক্তির পরিমাণ} {\lat $[\text{J}$} \B{বা} {\lat $\text{ erg}]$}
    \item[] {\lat $h$} = \B{প্ল্যাঙ্কের ধ্রুবক} {\lat $= 6.626 \times 10^{-34}\text{ J}\cdot\text{s} = 6.626 \times 10^{-27}\text{ erg}\cdot\text{s}$}
    \item[] {\lat $\nu$} = \B{বিকিরণের কম্পাঙ্ক (Frequency)} {\lat $[\text{s}^{-1}$} \B{বা} {\lat $\text{ Hz}]$}
    \item[] {\lat $c$} = \B{আলোর বেগ} {\lat $= 3 \times 10^8\text{ m s}^{-1} = 3 \times 10^{10}\text{ cm s}^{-1}$}
    \item[] {\lat $\lambda$} = \B{আলোক তরঙ্গের তরঙ্গদৈর্ঘ্য (Wavelength)} {\lat $[\text{m, cm, nm, }\text{\AA}]$}
    \item[] {\lat $\bar{\nu}$} = \B{তরঙ্গসংখ্যা (Wavenumber)} {\lat $[\text{m}^{-1}$} \B{বা} {\lat $\text{ cm}^{-1}]$}
\end{itemize}

\divider

\itm{6} \textbf{\B{রিডবার্গ সমীকরণ (হাইড্রোজেন বর্ণালির জন্য),}} {\lat $\bar{\nu} = \dfrac{1}{\lambda} = R_H \cdot Z^2 \left[\dfrac{1}{n_1^2} - \dfrac{1}{n_2^2}\right]$}
\begin{itemize}
    \item[] {\lat $R_H$} = \B{রিডবার্গ ধ্রুবক} {\lat $= 1,09,678\text{ cm}^{-1} = 1.097 \times 10^7\text{ m}^{-1}$}
    \item[] {\lat $n_1$} = \B{নিম্নতম প্রধান শক্তিস্তর যেখানে ইলেকট্রন ফিরে আসে}
    \item[] {\lat $n_2$} = \B{উচ্চতর প্রধান শক্তিস্তর যেখান থেকে ইলেকট্রন লাফিয়ে পড়ে ($n_2 > n_1$)}
    \item[] {\lat $Z$} = \B{পরমাণুর পারমাণবিক সংখ্যা (হাইড্রোজেনের জন্য $Z=1$, অন্য একক ইলেকট্রন আয়নের জন্য মান বসবে)}
    \item[] \textbf{\B{সর্বোচ্চ রেখার জন্য তরঙ্গদৈর্ঘ্য (সর্বনিম্ন শক্তি):}} $n_2 = n_1 + 1$
    \item[] \textbf{\B{সীমান্ত রেখা বা ক্ষুদ্রতম তরঙ্গদৈর্ঘ্যের জন্য (সর্বোচ্চ শক্তি):}} $n_2 = \infty$
\end{itemize}

\divider

\itm{7} \textbf{\B{বোর মডেল অনুযায়ী কৌণিক ভরবেগ,}} {\lat $mvr = \dfrac{nh}{2\pi}$}
\begin{itemize}
    \item[] {\lat $n$} = \B{প্রধান শক্তিস্তর বা কক্ষপথ নম্বর ($1, 2, 3, \dots$)}
    \item[] {\lat $m$} = \B{ইলেকট্রনের স্থির ভর} {\lat $[9.11 \times 10^{-31}\text{ kg}$} \B{বা} {\lat $9.11 \times 10^{-28}\text{ g}]$}
    \item[] {\lat $v$} = \B{কক্ষপথে আবর্তনশীল ইলেকট্রনের রৈখিক গতিবেগ} {\lat $[\text{m s}^{-1}$} \B{বা} {\lat $\text{ cm s}^{-1}]$}
    \item[] {\lat $r$} = \B{কক্ষপথের সুনির্দিষ্ট ব্যাসার্ধ} {\lat $[\text{m}$} \B{বা} {\lat $\text{ cm}]$}
\end{itemize}

\divider

\itm{8} \textbf{\B{লুই ডি-ব্রগলির পদার্থের দ্বৈত সমীকরণ,}} {\lat $\lambda = \dfrac{h}{mv} = \dfrac{h}{p}$}
\begin{itemize}
    \item[] {\lat $\lambda$} = \B{গতিশীল কণার সাথে সংশ্লিষ্ট তরঙ্গের তরঙ্গদৈর্ঘ্য}
    \item[] {\lat p} = \B{কণার রৈখিক ভরবেগ ($p = m \cdot v$)}
\end{itemize}

\divider

\itm{9} \textbf{\B{বোর কক্ষপথের ব্যাসার্ধ রাশিমালা (CGS এককে):}} {\lat $r_n = \dfrac{n^2 h^2}{4\pi^2 Z e^2 m}$}
\begin{itemize}
    \item[] {\lat $r_n$} = {\lat n}\B{-তম কক্ষপথের ব্যাসার্ধ [cm]}
    \item[] {\lat $e$} = \B{ইলেকট্রনের আধান (CGS এককে)} {\lat $= 4.8 \times 10^{-10}\text{ esu}$}
    \item[] {\lat m} = \B{ইলেকট্রনের ভর [g]}, {\lat h} = \B{প্ল্যাঙ্কের ধ্রুবক [erg$\cdot$s]}
\end{itemize}

\divider

\itm{10} \textbf{\B{হাইড্রোজেন পরমাণুর জন্য বোর ব্যাসার্ধের রূপান্তর সমীকরণ:}}
{\lat $r_n = \dfrac{n^2}{Z} \times r_1$}
\begin{itemize}
    \item[] {\lat $r_1$} = \B{হাইড্রোজেনের ১ম কক্ষপথের ব্যাসার্ধ (বোর ব্যাসার্ধ, } {\lat $a_0 = 0.5292 \times 10^{-8}\text{ cm} = 0.529\text{ \AA} = 0.0529\text{ nm}$)}
\end{itemize}

\divider

\itm{11} \textbf{\B{কক্ষপথে ইলেকট্রনের গতিবেগ (CGS এককে):}}
{\lat $v_n = \dfrac{2\pi Z e^2}{nh} = \dfrac{v_1 \times Z}{n}$}
\begin{itemize}
    \item[] {\lat $v_n$} = {\lat n}\B{-তম কক্ষপথে ইলেকট্রনের রৈখিক বেগ}
    \item[] {\lat $v_1$} = \B{হাইড্রোজেনের প্রথম কক্ষপথে ইলেকট্রনের বেগ} {\lat $= 2.1837 \times 10^8\text{ cm s}^{-1}$}
\end{itemize}

\divider

\itm{12} \textbf{\B{কক্ষপথের পরিধি ও তরঙ্গের সম্পর্ক,}} {\lat $2\pi r = n\lambda$}
\begin{itemize}
    \item[] \B{তাৎপর্য:} একটি ইলেকট্রন নিউক্লিয়াসকে কেন্দ্র করে আবর্তনের সময় $n$-তম কক্ষপথে ঠিক $n$ সংখ্যক পূর্ণ তরঙ্গ বা স্পন্দন সৃষ্টি করে.
\end{itemize}

\divider

\itm{13} \textbf{\B{ইলেকট্রনের প্রতি সেকেন্ডে আবর্তন সংখ্যা (Frequency of Revolution),}}
$$\text{আবর্তন সংখ্যা} = \dfrac{\text{\B{ইলেকট্রনের রৈখিক গতিবেগ }}(v)}{\text{\B{কক্ষপথের পরিধি }}(2\pi r)}$$

\divider

\itm{14} \textbf{\B{বোর কক্ষপথে ইলেকট্রনের মোট শক্তি (CGS এককে):}}
{\lat $E_n = -\dfrac{2\pi^2 m Z^2 e^4}{n^2 h^2} = -\dfrac{Z^2}{n^2} \times E_1$}
\begin{itemize}
    \item[] {\lat $E_n$} = {\lat n}\B{-তম কক্ষপথে ইলেকট্রনের মোট শক্তি (ঋণাত্মক চিহ্ন নিউক্লিয়াস দ্বারা ইলেকট্রনের আবদ্ধ অবস্থা নির্দেশ করে)}
    \item[] {\lat $E_1$} = \B{হাইড্রোজেনের প্রথম কক্ষপথের মোট শক্তি} {\lat $= -2.18 \times 10^{-11}\text{ erg} = -2.18 \times 10^{-18}\text{ J} = -13.6\text{ eV}$}
\end{itemize}

\divider

\itm{15} \textbf{\B{শ্রোডিঞ্জারের ত্রিমাত্রিক তরঙ্গ সমীকরণ,}}
$$\dfrac{\partial^2 \psi}{\partial x^2} + \dfrac{\partial^2 \psi}{\partial y^2} + \dfrac{\partial^2 \psi}{\partial z^2} + \dfrac{8\pi^2 m}{h^2}(E - V)\psi = 0$$
\begin{itemize}
    \item[] {\lat $x, y, z$} = \B{ত্রিমাত্রিক কার্তেসীয় স্থানাঙ্ক অক্ষত্রয়}
    \item[] {\lat $E$} = \B{ইলেকট্রনের মোট শক্তি}, {\lat $V$} = \B{ইলেকট্রনের স্থিতিশক্তি (Potential Energy)}
    \item[] {\lat $\psi$} = \B{তরঙ্গ ফাংশন (Wave Function)}, এবং $|\psi|^2$ দ্বারা অরবিটালে ইলেকট্রন পাওয়ার সর্বোচ্চ সম্ভাবনা ঘনত্ব প্রকাশ পায়.
\end{itemize}

\divider

\itm{16} \textbf{\B{হাইজেনবার্গের অনিশ্চয়তা নীতি সমীকরণ,}}
{\lat $\Delta x \cdot \Delta p \geq \dfrac{h}{4\pi} \implies \Delta x \cdot (m \cdot \Delta v) \geq \dfrac{h}{4\pi}$}
\begin{itemize}
    \item[] {\lat $\Delta x$} = \B{অবস্থানের অনিশ্চয়তা}, {\lat $\Delta p$} = \B{ভরবেগের অনিশ্চয়তা}, {\lat $\Delta v$} = \B{বেগের অনিশ্চয়তা}
\end{itemize}

\divider

\itm{17} \textbf{\B{তরঙ্গবেগ ও কম্পাঙ্কের মৌলিক সম্পর্ক,}} {\lat $c = \lambda \cdot \nu$}

\itm{18} \textbf{\B{তরঙ্গসংখ্যা,}} {\lat $\bar{\nu} = \dfrac{1}{\lambda}$}

\divider

\itm{19} \textbf{\B{দ্রাব্যতা (Solubility) গাণিতিক সমীকরণ,}} {\lat $S = \dfrac{100 \cdot m}{M - m} = \dfrac{100 \cdot w}{W_{\text{solvent}}}$}
\begin{itemize}
    \item[] {\lat $m$ \B{ বা } w} = \B{দ্রবীভূত দ্রবের ভর [g]}
    \item[] {\lat M} = \B{সম্পৃক্ত দ্রবণের মোট ভর [g]}
    \item[] {\lat $M - m = W_{\text{solvent}}$} = \B{শুধু বিশুদ্ধ দ্রাবকের ভর [g]}
\end{itemize}

\divider

\itm{20} \textbf{\B{স্বল্পদ্রাব্য সাধারণ লবণের দ্রাব্যতা গুণফল ($K_{sp}$) গণনা:}}
\B{ধরি একটি স্বল্পদ্রাব্য লবণ } {\lat $A_m B_n$} \B{জলীয় দ্রবণে আংশিক বিয়োজিত হয়ে নিম্নোক্ত সাম্যাবস্থা তৈরি করে:}
$$A_m B_n (s) \rightleftharpoons m A^{n+} (aq) + n B^{m-} (aq)$$
\B{লবণটির মোলার দ্রাব্যতা } {\lat $S \text{ mol L}^{-1}$} \B{হলে, সাম্যাবস্থায় আয়নসমূহের ঘনমাত্রা হবে:}
$$[A^{n+}] = mS \quad \text{এবং} \quad [B^{m-}] = nS$$
$$\mathbf{K_{sp} = [A^{n+}]^m \cdot [B^{m-}]^n = (mS)^m \cdot (nS)^n = m^m \cdot n^n \cdot S^{m+n}}$$

\B{বিশেষ গুরুত্বপূর্ণ উদাহরণসমূহ:}
\begin{itemize}
    \item \textbf{\B{1:1 টাইপ লবণ (যেমন: } $\text{AgCl, BaSO}_4$):} $m=1, n=1 \implies \mathbf{K_{sp} = S^2 \implies S = \sqrt{K_{sp}}}$
    \item \textbf{\B{1:2 বা 2:1 টাইপ লবণ (যেমন: } $\text{MgCl}_2, \text{Ag}_2\text{CrO}_4, \text{CaF}_2$):} $m=1, n=2 \implies \mathbf{K_{sp} = 1^1 \cdot 2^2 \cdot S^{1+2} = 4S^3 \implies S = \sqrt[3]{\dfrac{K_{sp}}{4}}}$
    \item \textbf{\B{1:3 টাইপ লবণ (যেমন: } $\text{Fe(OH)}_3, \text{AlCl}_3$):} $m=1, n=3 \implies \mathbf{K_{sp} = 1^1 \cdot 3^3 \cdot S^{1+3} = 27S^4 \implies S = \sqrt[4]{\dfrac{K_{sp}}{27}}}$
    \item \textbf{\B{2:3 টাইপ লবণ (যেমন: } $\text{As}_2\text{S}_3, \text{Ca}_3(\text{PO}_4)_2$):} $m=3, n=2 \implies \mathbf{K_{sp} = 3^3 \cdot 2^2 \cdot S^{3+2} = 108S^5 \implies S = \sqrt[5]{\dfrac{K_{sp}}{108}}}$
\end{itemize}

\divider

\itm{21} \textbf{\B{ইলেকট্রন ভোল্ট (eV) এককে শক্তি রূপান্তর সমীকরণ,}}
{\lat $E_n = -13.6 \times \dfrac{Z^2}{n^2}\text{ eV}$}
\begin{itemize}
    \item[] \B{শক্তির একক রূপান্তর ধ্রুবক:} {\lat $1\text{ eV} = 1.602 \times 10^{-19}\text{ J} = 1.602 \times 10^{-12}\text{ erg}$}
\end{itemize}

\divider

\itm{22} \textbf{\B{দুটি কক্ষপথের শক্তির পার্থক্য (eV এককে),}}
{\lat $\Delta E = E_{n_2} - E_{n_1} = 13.6 \cdot Z^2 \left(\dfrac{1}{n_1^2} - \dfrac{1}{n_2^2}\right)\text{ eV}$}

\divider

\itm{23} \textbf{\B{অরবিটাল ও উপশক্তিস্তরের সর্বোচ্চ ইলেকট্রন ধারণ ক্ষমতা ছক:}}
\begin{tabular}{|c|c|c|c|}
\hline
\B{প্রধান শক্তিস্তর ($n$)} & \B{সহকারী কোয়ান্টাম সংখ্যা ($l$)} & \B{অরবিটালের নাম} & \B{সর্বোচ্চ ইলেকট্রন সংখ্যা} \\
\hline
$n = 1$ & $l = 0$ & $1s$ & $2 \times 1 = 2$ \\
\hline
$n = 2$ & $l = 0, 1$ & $2s, 2p$ & $2 + 6 = 8$ \\
\hline
$n = 3$ & $l = 0, 1, 2$ & $3s, 3p, 3d$ & $2 + 6 + 10 = 18$ \\
\hline
$n = 4$ & $l = 0, 1, 2, 3$ & $4s, 4p, 4d, 4f$ & $2 + 6 + 10 + 14 = 32$ \\
\hline
\end{tabular}

\divider

\itm{24} \textbf{\B{কোয়ান্টাম সংখ্যার পারস্পরিক সেটের সীমা নির্ধারণ নিয়মাবলী:}}
\begin{itemize}
    \item $n \rightarrow$ যেকোনো ধনাত্মক পূর্ণসংখ্যা ($1, 2, 3, 4, \dots$).
    \item $l \rightarrow$ সর্বদা $0$ থেকে $(n-1)$ পর্যন্ত. ($l$ এর মান কখনো $n$ এর সমান বা বড় হতে পারে না. যেমন: $2d$ বা $1p$ অরবিটাল অসম্ভব).
    \item $m \rightarrow$ সর্বদা $-l$ থেকে $+l$ পর্যন্ত শূন্যসহ মোট $(2l+1)$ টি মান.
    \item $s \rightarrow$ প্রতিটি অরবিটালের একক চৌম্বক মানের বিপরীতে দুটি ঘূর্ণন মান থাকে: $+\dfrac{1}{2}$ এবং $-\dfrac{1}{2}$.
\end{itemize}

\divider

\itm{25} \textbf{\B{তেজস্ক্রিয় ক্ষয় এবং অর্ধায়ু সমীকরণ (Radioactivity - অধ্যায়ের অন্তর্ভুক্ত বিশেষ সংযুক্তি):}}
{\lat $N = N_0 \cdot e^{-\lambda t}$}
\begin{itemize}
    \item[] {\lat $N_0$} = \B{শুরুর প্রারম্ভিক মুহূর্তে তেজস্ক্রিয় পরমাণুর সংখ্যা ($t = 0$)}
    \item[] {\lat N} = {\lat t} \B{সময় অতিবাহিত হওয়ার পর অবশিষ্ট অক্ষত পরমাণুর সংখ্যা}
    \item[] {\lat $\lambda$} = \B{তেজস্ক্রিয় ক্ষয় ধ্রুবক (Decay Constant)}
    \item[] \textbf{\B{অর্ধায়ু (Half-life) সমীকরণ:}} $\mathbf{t_{1/2} = \dfrac{\ln(2)}{\lambda} = \dfrac{0.693}{\lambda}}$
\end{itemize}


\chsec{অধ্যায়-৩: মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন (Periodic Properties of Elements \& Chemical Bonding)}

\chsub{Concept Map: The Chapter at a Glance}{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: ইলেকট্রন বিন্যাসভিত্তিক মৌলের আণবিক পর্যায়বৃত্ত ধর্ম ও বন্ধন রাসায়নিকতা}}

\divider

\textbf{{\lat 1.} \B{ইলেকট্রন বিন্যাস ও মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat s}\B{-ব্লক মৌল (মৌল সংখ্যা: ১৪টি):}}
\begin{itemize}
    \item \textbf{\B{মৌলসমূহ:}} গ্রুপ-১ (ক্ষার ধাতু): \lat H, Li, Na, K, Rb, Cs, Fr\B{; গ্রুপ-২ (মৃৎক্ষার ধাতু): } \lat Be, Mg, Ca, Sr, Ba, Ra\B{ এবং গ্রুপ-১৮ এর } \lat He\B{.}
    \item \textbf{\B{সাধারণ ইলেকট্রন বিন্যাস:}} {\lat $ns^{1\text{-}2}$}
    \item \textbf{\B{ভৌত ও রাসায়নিক ধর্মাবলী:}} 
    \begin{itemize}
        \item ক্ষার ধাতুগুলোর সর্ববহিঃস্থ স্তরে ১টি ইলেকট্রন থাকায় এদের জারণ সংখ্যা সর্বদা +১ (যেমন: \lat Na$^+$, K$^+$) এবং মৃৎক্ষার ধাতুগুলোর জারণ সংখ্যা +২ হয়.
        \item এদের পারমাণবিক আকার সংশ্লিষ্ট পর্যায়ের অন্যান্য মৌলের চেয়ে অনেক বড় এবং এদের আয়নিকরণ বিভব (\lat Ionization Potential) এর মান খুবই কম.
        \item এরা অত্যন্ত তীব্র তড়িৎ-ধনাত্মক এবং সক্রিয় ধাতু. রাসায়নিক বিক্রিয়ায় এরা তীব্র বিজারকরূপে ক্রিয়া করে.
        \item \lat Na, K \B{অত্যন্ত সক্রিয় ধাতু হওয়ায় এরা পানির সংস্পর্শে এলেই সজোরে বিক্রিয়া করে আগুন ধরে যায়. এই কারণে এদের নিষ্ক্রিয় কেরোসিনের নিচে ডুবিয়ে রাখা হয়.}
        \item এরা অত্যন্ত নরম, নমনীয় এবং কম গলনাঙ্ক ও স্ফুটনাঙ্কবিশিষ্ট ধাতু (ছুরি দিয়ে কাটা যায়). 
        \item এরা প্রধানত স্থির-তড়িৎ আকর্ষণ বলের মাধ্যমে আয়নিক যৌগ গঠন করে.
        \item \B{শিখা পরীক্ষা (Flame Test):} \lat s-ব্লকের মৌলসমূহ (ব্যতিক্রম: \lat Be \B{ ও } \lat Mg) বুন্সেন বার্নারের অনুজ্জ্বল শিখায় চরিত্রগত উজ্জ্বল বর্ণ প্রদর্শন করে. যেমন: \lat Li $\rightarrow$ টকটকে লাল, \lat Na $\rightarrow$ সোনালী হলুদ, \lat K $\rightarrow$ বেগুনী, \lat Ca $\rightarrow$ ইটের মতো লাল, \lat Ba $\rightarrow$ কাঁচা আপেলের মতো সবুজ.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 2.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat p}\B{-ব্লক মৌল (মৌল সংখ্যা: ৩৬টি):}}
\begin{itemize}
    \item \textbf{\B{মৌলসমূহ:}} পর্যায় সারণির গ্রুপ-১৩ থেকে গ্রুপ-১৮ পর্যন্ত মৌলসমূহ (ব্যতিক্রম \lat He) এই ব্লকের অন্তর্ভুক্ত. এর মধ্যে ধাতু, অধাতু ও উপধাতু (যেমন: \lat B, Si, Ge, As, Sb, Te) তিন প্রকার মৌলই বিদ্যমান.
    \item \textbf{\B{সাধারণ ইলেকট্রন বিন্যাস:}} {\lat $ns^2 np^{1\text{-}6}$}
    \item \textbf{\B{ভৌত ও রাসায়নিক ধর্মাবলী:}}
    \begin{itemize}
        \item এরা মূলত উচ্চ তড়িৎ-ঋণাত্মক অধাতব মৌল. একই পর্যায়ে বাম থেকে ডানদিকে গেলে \lat p\B{-ব্লকের মৌলসমূহের পারমাণবিক আকার ক্রমশ হ্রাস পায়.}
        \item একই পর্যায়ে বাম থেকে ডানদিকে গেলে \lat p\B{-ব্লক মৌলসমূহের বিজারণ ক্ষমতা ক্রমশ হ্রাস পায় এবং জারণ ক্ষমতা (Oxidizing Power) ক্রমশ বৃদ্ধি পায়.}
        \item একই গ্রুপের উপর থেকে নিচের দিকে নামলে মৌলসমূহের জারণ ক্ষমতা হ্রাস পায় এবং বিজারণ ক্ষমতা বৃদ্ধি পায়.
        \item এরা অধাতু বা ধাতুর সাথে যুক্ত হয়ে প্রধানত সমযোজী যৌগ গঠন করে, তবে তীব্র তড়িৎ-ধনাত্মক ধাতুর সাথে এরা আয়নিক যৌগও সৃষ্টি করতে পারে.
        \item এরা পরিবর্তনশীল জারণ অবস্থা (\lat Variable Oxidation States) প্রদর্শন করে.
        \item \B{নিষ্ক্রিয় জোড় প্রভাব (Inert Pair Effect):} এই ব্লকের নিচের দিকের ভারী মৌলসমূহের (যেমন: \lat Pb, Bi, Tl) ক্ষেত্রে সর্ববহিঃস্থ \lat $ns^2$ ইলেকট্রন জোড় রাসায়নিক বন্ধনে অংশ নিতে চায় না, ফলে এদের নিম্ন জারণ অবস্থা বেশি সুস্থিত হয় (যেমন: \lat $\text{Pb}^{2+}$ এর সুস্থিতি \lat $\text{Pb}^{4+}$ এর চেয়ে বেশি).
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 3.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat d}\B{-ব্লক ও অবস্থান্তর মৌল (মৌল সংখ্যা: ৪১টি):}}
\begin{itemize}
    \item \textbf{\B{সাধারণ ইলেকট্রন বিন্যাস:}} {\lat $(n-1)d^{1\text{-}10} ns^{1\text{-}2}$} \B{(গ্রুপ-৩ থেকে গ্রুপ-১২).}
    \item \textbf{\B{সাধারণ ধর্মাবলী:}} এরা সবাই ভারী ধাতু (\lat Heavy Metals), উচ্চ ঘনত্বের অধিকারী এবং এদের গলনাঙ্ক ও স্ফুটনাঙ্ক অত্যন্ত উচ্চ. এরা অত্যন্ত কঠিন ও শক্ত প্রকৃতির ধাতু.
    \item \textbf{\B{ভৌত অবস্থা ও পরিবাহিতা:}} কক্ষ তাপমাত্রায় এরা সবাই কঠিন হলেও মারকারী (\lat Hg) একটি ব্যতিক্রমী তরল ধাতু. এরা প্রত্যেকেই উত্তম তাপ ও বিদ্যুৎ সুপরিবাহী.
    \item \textbf{\B{চৌম্বক ধর্ম:}} \B{এদের অধিকাংশ মৌলই প্যারাম্যাগনেটিক (}\lat Paramagnetic\B{), অর্থাৎ অপূর্ণ }\lat d\B{-অরবিটালে অয়ুগ্ম ইলেকট্রন থাকার কারণে এরা চুম্বকক্ষেত্র দ্বারা তীব্রভাবে আকৃষ্ট হয়. এরা পরস্পরের সাথে যুক্ত হয়ে সহজে সংকর ধাতু (}\lat Alloys\B{) তৈরি করে.}
    \item \textbf{\B{অবস্থান্তর মৌল (Transition Elements):}} যেসকল \lat d-ব্লক মৌলের অন্তত একটি সুস্থিত আয়নে \lat d-অরবিটালটি আংশিকভাবে পূর্ণ থাকে (অর্থাৎ \lat $d^{1\text{-}9}$ বিন্যাস থাকে), তাদের অবস্থান্তর মৌল বলে.
    \item \textbf{\B{ব্যতিক্রম (অবস্থান্তর নয় এমন d-ব্লক মৌল):}} 
    \begin{itemize}
        \item \lat $\text{Sc}$ ($3d^1 4s^2$) এর সুস্থিত আয়ন $\text{Sc}^{3+}$ এর ইলেকট্রন বিন্যাস $3d^0$ (অরবিটাল শূন্য).
        \item \lat $\text{Zn}$ ($3d^{10} 4s^2$) এর সুস্থিত আয়ন $\text{Zn}^{2+}$ এর ইলেকট্রন বিন্যাস $3d^{10}$ (অরবিটাল সম্পূর্ণ পূর্ণ).
        \item তাই \lat $\text{Sc, Ti}^{4+}, \text{Cu}^+$ (সুস্থিত আয়নে $3d^{10}$) বা \lat $\text{Zn, Cd, Hg}$ এরা \lat d-ব্লক মৌল হলেও অবস্থান্তর মৌল নয়.
    \end{itemize}
    \item \textbf{\B{অবস্থান্তর মৌলের বিশিষ্ট রাসায়নিক ধর্মসমূহ:}}
    \sub{i} \B{পরিবর্তনশীল জারণ অবস্থা:} \lat $(n-1)d$ ও \lat $ns$ অরবিটালের শক্তির পার্থক্য খুব কম হওয়ায় এরা একাধিক জারণ অবস্থা দেখায় (যেমন: \lat $\text{Fe}^{2+}, \text{Fe}^{3+}$).
    \sub{ii} \B{রঙিন আয়ন বা রঙিন যৌগ গঠন:} অপূর্ণ \lat d-অরবিটালের ইলেকট্রনসমূহ যখন দৃশ্যমান আলোর শক্তি শোষণ করে এক \lat d-অরবিটাল থেকে অন্য \lat d-অরবিটালে স্থানান্তরিত হয় (\lat d-d transition), তখন এরা রঙিন যৌগ গঠন করে.
    \sub{iii} \B{জটিল আয়ন বা যৌগ গঠন (Complex Ion Formation):} এদের উচ্চ চার্জ ঘনত্ব ও খালি \lat d-অরবিটাল থাকার কারণে এরা লিগ্যান্ডের (\lat Ligands) কাছ থেকে মুক্তজোড় ইলেকট্রন গ্রহণ করে সন্নিবেশ বন্ধনের মাধ্যমে জটিল যৌগ তৈরি করে [যেমন: \lat $\text{[Fe(CN)}_6]^{4-}$].
    \sub{iv} \B{প্রভাবকীয় ক্ষমতা:} এরা রাসায়নিক বিক্রিয়ায় শক্তিশালী প্রভাবক বা ক্যাটালিস্ট হিসেবে কাজ করে (যেমন: হেবার পদ্ধতিতে \lat Fe চূর্ণ).
\end{itemize}

\divider

\textbf{{\lat 4.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat f}\B{-ব্লক ও অভ্যন্তরীণ অবস্থান্তর মৌল (মৌল সংখ্যা: ২৭টি):}}
\begin{itemize}
    \item \textbf{\B{সাধারণ ইলেকট্রন বিন্যাস:}} {\lat $(n-2)f^{1\text{-}14} (n-1)d^{0\text{-}1} ns^2$} \B{(গ্রুপ-৩, পর্যায়-৬ ও ৭).}
    \item \textbf{\B{ল্যান্থানাইড সিরিজ (Lanthanide Series):}} পর্যায়-৬ এর \lat $\text{Ce (58)}$ থেকে \lat $\text{Lu (71)}$ পর্যন্ত ১৪টি মৌল.
    \begin{itemize}
        \item এরা চকচকে রূপালী ও ভারী ধাতু. এরা বিদ্যুৎ ও তাপের উত্তম সুপরিবাহী. এদের ঘনত্ব, গলনাঙ্ক ও স্ফুটনাঙ্ক অনেক বেশি.
        \item এদের উৎপন্ন আয়নসমূহ বর্ণযুক্ত হয়. এদের সবচেয়ে স্থায়ী ও সাধারণ জারণ অবস্থা হলো +৩.
        \item \B{ল্যান্থানাইড সংকোচন (Lanthanide Contraction):} ল্যান্থানাইড সিরিজে পারমাণবিক সংখ্যা বৃদ্ধির সাথে সাথে ভেতরের \lat $4f$ অরবিটালে ইলেকট্রন প্রবেশ করে. \lat $f$-অরবিটালের আবরণী ক্ষমতা (\lat Screening Effect) অত্যন্ত দুর্বল হওয়ায় নিউক্লিয়াসের প্রতি বহিঃস্থ ইলেকট্রনের আকর্ষণ তীব্রভাবে বৃদ্ধি পায়, ফলে বাম থেকে ডানে পারমাণবিক ও আয়নিক ব্যাসার্ধ প্রত্যাশার চেয়ে অনেক বেশি হ্রাস পায়. একে ল্যান্থানাইড সংকোচন বলে.
    \end{itemize}
    \item \textbf{\B{অ্যাকটিনাইড সিরিজ (Actinide Series):}} পর্যায়-৭ এর \lat $\text{Th (90)}$ থেকে \lat $\text{Lr (103)}$ পর্যন্ত ১৪টি মৌল.
    \begin{itemize}
        \item এরা সবাই অত্যন্ত ভারী এবং তেজস্ক্রিয় মৌল (\lat Radioactive Elements). ইউরেনিয়ামের (\lat U-92) পরের মৌলগুলোকে কৃত্রিমভাবে তৈরি করা হয় বিধায় এদের ট্রান্সইউরেনিয়াম মৌল বলে.
        \item এদের ঘনত্ব খুব বেশি এবং এরা উচ্চ গলনাঙ্ক ও স্ফুটনাঙ্কবিশিষ্ট অত্যন্ত তড়িৎ-ধনাত্মক ধাতু.
    \end{itemize}
\end{itemize}

\divider

\textbf{{\lat 5.} \B{মৌলের পর্যায়বৃত্ত ধর্মসমূহের পরিবর্তনশীলতার রূপরেখা (Periodic Trends):}}
\B{পর্যায় সারণির একই পর্যায়ে বাম থেকে ডানে গেলে এবং একই গ্রুপের উপর থেকে নিচে নামলে ভৌত ধর্মসমূহের সাধারণ পরিবর্তন নিচে ছক আকারে দেওয়া হলো:}

\begin{tabular}{|l|l|l|}
\hline
\B{পর্যায়বৃত্ত ধর্ম} & \B{একই পর্যায়ে (বাম থেকে ডানে)} & \B{একই গ্রুপে (উপর থেকে নিচে)} \\
\hline
১. পারমাণবিক ব্যাসার্ধ / আকার & হ্রাস পায় (নিউক্লিয়ার চার্জ বাড়ে) & বৃদ্ধি পায় (নতুন শক্তিস্তর যুক্ত হয়) \\
\hline
২. ধাতব ধর্ম & হ্রাস পায় & বৃদ্ধি পায় \\
\hline
৩. অধাতব ধর্ম & বৃদ্ধি পায় & হ্রাস পায় \\
\hline
৪. জারণ ক্ষমতা & বৃদ্ধি পায় & হ্রাস পায় \\
\hline
৫. বিজারণ ক্ষমতা & হ্রাস পায় & বৃদ্ধি পায় \\
\hline
৬. আয়নিকরণ শক্তি (\lat IE) & বৃদ্ধি পায় & হ্রাস পায় \\
\hline
৭. ইলেকট্রন আসক্তি (\lat EA) & বৃদ্ধি পায় & হ্রাস পায় \\
\hline
৮. তড়িৎ ঋণাত্মকতা (\lat EN) & বৃদ্ধি পায় & হ্রাস পায় \\
\hline
\end{tabular}

\begin{itemize}
    \item \textbf{\B{আয়নিকরণ শক্তির ব্যতিক্রম (Crucial Exceptions of Ionization Energy):}}
    \begin{itemize}
        \item \B{বেরিলিয়াম ও বোরন:} সাধারণ নিয়মে \lat $\text{B}$ এর \lat IE, \lat $\text{Be}$ এর চেয়ে বেশি হওয়ার কথা থাকলেও প্রকৃতপক্ষে $\mathbf{\text{Be } (1s^2 2s^2) > \text{B } (1s^2 2s^2 2p^1)}$ হয়. কারণ \lat $\text{Be}$ এর সুস্থিত পূর্ণ \lat $2s$ অরবিটাল থেকে ইলেকট্রন অপসারণ করা কঠিন.
        \item \B{নাইট্রোজেন ও অক্সিজেন:} একইভাবে নাইট্রোজেনের \lat IE অক্সিজেনের চেয়ে বেশি হয়, অর্থাৎ $\mathbf{\text{N } (1s^2 2s^2 2p^3) > \text{O } (1s^2 2s^2 2p^4)}$. কারণ \lat $\text{N}$ এর \lat $2p$ উপশক্তিস্তরটি সুস্থিত অর্ধপূর্ণ ($2p_x^1 2p_y^1 2p_z^1$) অবস্থায় থাকে.
    \end{itemize}
    \item \textbf{\B{ইলেকট্রন আসক্তির ব্যতিক্রম (Exception of Electron Affinity):}}
    \begin{itemize}
        \item \B{ফ্লোরিন ও ক্লোরিন:} সাধারণ নিয়মে ফ্লোরিনের ইলেকট্রন আসক্তি বেশি হওয়ার কথা থাকলেও প্রকৃতপক্ষে $\mathbf{\text{Cl} > \text{F}}$ হয়. কারণ ফ্লোরিনের পরমাণুর আকার অতি ক্ষুদ্র হওয়ায় এর ২য় শক্তিস্তরে ইলেকট্রন ঘনত্ব অনেক বেশি থাকে, ফলে আগত নতুন ইলেকট্রনের প্রতি তীব্র আন্তঃইলেকট্রন বিকর্ষণ কাজ করে. ক্লোরিনের আকার বড় হওয়ায় এমন বিকর্ষণ হয় না. (একই কারণে $\text{S} > \text{O}$ হয়).
    \end{itemize}
    \item \textbf{\B{তড়িৎ ঋণাত্মকতার পলিং স্কেল মান (Pauling Scale Values):}} 
    \lat $\text{F (4.0) } > \text{ O (3.5) } > \text{ N (3.0) } \approx \text{ Cl (3.0) } > \text{ Br (2.8) } > \text{ C (2.5) } \approx \text{ S (2.5) } > \text{ H (2.1)}$
\end{itemize}

\divider

\textbf{{\lat 6.} \B{রাসায়নিক বন্ধন ও অরবিটাল ওভারল্যাপ (Chemical Bonding Theories):}}
\begin{itemize}
    \item \textbf{\B{প্রধান প্রকারভেদ:}} \B{আয়নিক বন্ধন (স্থির তড়িৎ আকর্ষণ), সমযোজী বন্ধন (ইলেকট্রন শেয়ারিং), সন্নিবেশ সমযোজী বন্ধন (একতরফা ইলেকট্রন দান ও যৌথ শেয়ার), হাইড্রোজেন বন্ধন (তীব্র আকর্ষণ).}
    \item \textbf{\B{আয়নিক যৌগের বৈশিষ্ট্য:}} \B{এরা পোলার বা মেরুপ্রবণ ক্যারেক্টার দেখায়; সুনির্দিষ্ট জ্যামিতিক কেলাসিত বা দানাদার গঠনযুক্ত হয়; এদের গলনাঙ্ক ও স্ফুটনাঙ্ক অত্যন্ত উচ্চ থাকে; এরা পানি বা পোলার দ্রাবকে দ্রবণীয় কিন্তু অপোলার জৈব দ্রাবকে অদ্রবণীয়; কঠিন অবস্থায় অপরিবাহী হলেও গলিত বা জলীয় দ্রবণে এরা চমৎকার তড়িৎ পরিবাহী.}
    \item \textbf{\B{সমযোজী বন্ধনের অরবিটাল অধিক্রমণ শ্রেণিবিভাগ (Orbital Overlap):}}
    \begin{itemize}
        \item \textbf{\B{সিগমা বন্ধন (} \lat $\sigma$ \B{ বন্ধন):}} দুটি পরমাণুর অরবিটালদ্বয়ের অক্ষ বরাবর মুখোমুখি বা সামনাসামনি আংশিক অধিক্রমণের ফলে যে শক্তিশালী সমযোজী বন্ধন গঠিত হয়, তাকে সিগমা বন্ধন বলে. সব একক বন্ধনই সিগমা বন্ধন.
        \item \textbf{\B{পাই বন্ধন (} \lat $\pi$ \B{-বন্ধন):}} দুটি পরমাণুর সমান্তরাল অক্ষবিশিষ্ট দুটি বিশুদ্ধ পি-অরবিটালের পাশাপাশি বা পার্শ্বমুখী আংশিক অধিক্রমণের ফলে যে অপেক্ষাকৃত দুর্বল বন্ধন গঠিত হয়, তাকে পাই বন্ধন বলে. দ্বিবন্ধনে ১টি $\sigma$ ও ১টি $\pi$ এবং ত্রিবন্ধনে ১টি $\sigma$ ও ২টি $\pi$ বন্ধন থাকে.
    \end{itemize}
    \item \textbf{\B{বন্ধন মতবাদসমূহ:}} \B{যোজনী বন্ধন মতবাদ (}\lat Valence Bond Theory - VBT\B{) এবং আণবিক অরবিটাল মতবাদ (}\lat Molecular Orbital Theory - MOT\B{).}
\end{itemize}

\divider

\textbf{{\lat 7.} \B{পোলারায়ন ও ফাজানের নিয়ম (Polarization \& Fajan's Rules):}}
\B{আয়নিক যৌগের মধ্যে সমযোজী বৈশিষ্ট্যের আংশিক বিকাশকে পোলারায়ন বলে. ক্যাটায়ন কর্তৃক অ্যানায়নের ইলেকট্রন মেঘ নিজের দিকে টেনে এনে বিকৃত করার ক্ষমতাই হলো পোলারায়ন. ফাজানের নিয়ম অনুযায়ী পোলারায়ন তথা সমযোজী ধর্ম বৃদ্ধির শর্তসমূহ হলো:}
\begin{itemize}
    \item \textbf{\B{ক্যাটায়ন ও অ্যানায়নের চার্জ:}} \B{ক্যাটায়ন ও অ্যানায়নের আধান বা চার্জের পরিমাণ যত বেশি হবে, পোলারায়ন তত বেশি হবে এবং সমযোজী ধর্ম তত বৃদ্ধি পাবে (গলনাঙ্ক হ্রাস পাবে). যেমন:} \lat $\text{NaCl} < \text{MgCl}_2 < \text{AlCl}_3$ \B{(সমযোজী ধর্ম বৃদ্ধির ক্রম).}
    \item \textbf{\B{ক্যাটায়নের আকার:}} \B{ক্যাটায়নের আকার যত ছোট হবে, তার চার্জ ঘনত্ব তত বেশি হবে এবং অ্যানায়নকে বিকৃত করার ক্ষমতা তত বৃদ্ধি পাবে. যেমন:} \lat $\text{BeCl}_2 > \text{MgCl}_2 > \text{CaCl}_2$ \B{(সমযোজী ধর্মের ক্রম).}
    \item \textbf{\B{অ্যানায়নের আকার:}} \B{অ্যানায়নের আকার যত বড় হবে, তার বহিঃস্থ ইলেকট্রন মেঘের ওপর নিজস্ব নিউক্লিয়াসের নিয়ন্ত্রণ তত শিথিল হবে, ফলে ক্যাটায়ন দ্বারা সেটি সহজে বিকৃত হবে. যেমন:} \lat $\text{AgF} < \text{AgCl} < \text{AgBr} < \text{AgI}$ \B{(সমযোজী ধর্ম বৃদ্ধির ক্রম).}
    \item \textbf{\B{ক্যাটায়নের ইলেকট্রন বিন্যাস:}} \B{সমআকার ও সমচার্জযুক্ত দুটি ক্যাটায়নের মধ্যে যার সর্ববহিঃস্থ স্তরে ছদ্ম-নিষ্ক্রিয় গ্যাস বিন্যাস বা} \lat $ns^2 np^6 nd^{10}$ \B{বিন্যাস থাকে, তার পোলারায়ন ক্ষমতা সাধারণ নিষ্ক্রিয় গ্যাস বিন্যাসযুক্ত (}\lat $ns^2 np^6$\B{) ক্যাটায়নের চেয়ে অনেক বেশি ঘটে. যেমন:} \lat $\text{CuCl}$ \B{এর গলনাঙ্ক} \lat $\text{NaCl}$ \B{এর চেয়ে অনেক কম, কারণ $\text{Cu}^+$ এর বহিঃস্থ স্তরে ১৮টি ইলেকট্রন ($3d^{10}$) বিদ্যমান.}
\end{itemize}

\divider

\textbf{{\lat 8.} \B{ভ্যানডার ওয়ালস বল (Van der Waals Forces):}}
\B{অপোলার সমযোজী অণুসমূহের মধ্যে ক্রিয়াশীল অত্যন্ত দুর্বল আন্তঃআণবিক আকর্ষণ বলকে ভ্যানডার ওয়ালস বল বলে. এর মূল শ্রেণিবিভাগ:}
\begin{itemize}
    \item \textbf{\B{স্থায়ী ডাইপোল - স্থায়ী ডাইপোল আকর্ষণ:}} \B{পোলার অণুসমূহের মধ্যে ধনাত্মক ও ঋণাত্মক প্রান্তের আকর্ষণ (যেমন:} \lat $\text{HCl}$ \B{অণুসমূহের মাঝে).}
    \item \textbf{\B{ডাইপোল - আবিষ্ট ডাইপোল আকর্ষণ:}} \B{একটি পোলার অণু যখন একটি অপোলার অণুকে আবেশের মাধ্যমে ক্ষণস্থায়ী পোলারিটি দান করে আকর্ষিত করে.}
    \item \textbf{\B{লন্ডন বল বা বিস্তারণ বল (London Dispersion Force):}} সম্পূর্ণ অপোলার অণু বা নিষ্ক্রিয় গ্যাসসমূহের মধ্যে ইলেকট্রন মেঘের তাৎক্ষণিক অসম বণ্টনের ফলে ক্ষণস্থায়ী ডাইপোল সৃষ্টির মাধ্যমে যে অতি দুর্বল আকর্ষণ বল তৈরি হয়. অণুর আণবিক ভর ও আকার বাড়লে লন্ডন বলের মান বৃদ্ধি পায় (যেমন: গলনাঙ্কের ক্রম $\text{F}_2 < \text{Cl}_2 < \text{Br}_2 < \text{I}_2$).
\end{itemize}

\divider

\textbf{{\lat 9.} \B{নন-বন্ডিং আন্তঃআণবিক বলসমূহের সংক্ষেপ ছক (Non-bonding Interactions):}}
\begin{itemize}
    \item \B{আয়ন-ডাইপোল আকর্ষণ:} সোডিয়াম ক্লোরাইড পানিতে দ্রবীভূত হওয়ার মূল কারণ (\lat $\text{Na}^+$ ও পানির ঋণাত্মক \lat $\text{O}$ প্রান্তের আকর্ষণ).
    \item \B{হাইড্রোজেন বন্ধন (Hydrogen Bonding):} তীব্র তড়িৎ-ঋণাত্মক মৌলের (\lat F, O, N) সাথে যুক্ত হাইড্রোজেন পরমাণু যখন অন্য কোনো তীব্র তড়িৎ-ঋণাত্মক পরমাণুর সাথে দুর্বল স্থির-তড়িৎ বল দ্বারা যুক্ত হয়. 
    \begin{itemize}
        \item \B{অন্তঃআণবিক H-বন্ধন (Intramolecular):} একই অণুর ভেতরে গঠিত হয় (যেমন: অর্থো-নাইট্রোফেনল).
        \item \B{আন্তঃআণবিক H-বন্ধন (Intermolecular):} পৃথক দুটি অণুর মধ্যে গঠিত হয় (যেমন: পানি, অ্যালকোহল). পানির আন্তঃআণবিক H-বন্ধনের কারণেই \lat $\text{H}_2\text{O}$ তরল কিন্তু \lat $\text{H}_2\text{S}$ একটি গ্যাস.
    \end{itemize}
\end{itemize}

\divider
\divider

\chsub{}{সংকরায়ন সূত্র ও জ্যামিতিক আকৃতি (Hybridization Details)}

\itm{1} \textbf{\B{কেন্দ্রীয় পরমাণুর সংকরায়ন সংখ্যা (H) নির্ণয়ের সার্বজনীন সূত্র:}}
$$\mathbf{H = \dfrac{1}{2}[V + M - C + A]}$$
\begin{itemize}
    \item[] {\lat $H$} = \B{মোট সংকর অরবিটাল সংখ্যা (যদি $H=2 \rightarrow sp$, $H=3 \rightarrow sp^2$, $H=4 \rightarrow sp^3$, $H=5 \rightarrow sp^3d$, $H=6 \dots$)}
    \item[] {\lat $V$} = \B{কেন্দ্রীয় পরমাণুর সর্ববহিঃস্থ যোজনী স্তরের মোট ইলেকট্রন সংখ্যা}
    \item[] {\lat $M$} = \B{কেন্দ্রীয় পরমাণুর সাথে একক বন্ধনে যুক্ত একযোজী পরমাণুর সংখ্যা (যেমন: \lat H, F, Cl, Br, I). দ্বিজোজী পরমাণু যেমন \lat O, S হলে $M=0$ বসবে.}
    \item[] {\lat $C$} = \B{ক্যাটায়নের ধনাত্মক আধানের সংখ্যা (আধানের মানটি বিয়োগ করতে হবে)}
    \item[] {\lat $A$} = \B{অ্যানায়নের ঋণাত্মক আধানের সংখ্যা (আধানের মানটি যোগ করতে হবে)}
    \item[] \textbf{\B{মুক্তজোড় ইলেকট্রন সংখ্যা (Lone Pair, LP) গণনা:}} $\mathbf{\text{LP} = H - \text{নিলম্বিত পরমাণুর সংখ্যা (Surrounding Atoms)}}$
\end{itemize}

\begin{quote}
\textbf{\B{VSEPR তত্ত্বের বিশেষ দ্রষ্টব্য:}} ভ্যালেন্স শেল ইলেকট্রন পেয়ার রিপালশন (\lat VSEPR) তত্ত্বানুসারে, লোন পেয়ার-লোন পেয়ার (\lat LP-LP) বিকর্ষণ সবচেয়ে তীব্র হয় ($\text{LP-LP} > \text{LP-BP} > \text{BP-BP}$). পরমাণুতে প্রতিটি মুক্তজোড় ইলেকট্রন যুগলের (\lat Lone Pair) উপস্থিতির কারণে যৌগের সুষম জ্যামিতিক আকৃতি বিকৃত হয় এবং আদর্শ বন্ধন কোণ প্রায় $\mathbf{2^{\circ}\text{--}2.5^{\circ}}$ করে হ্রাস পায়.
\end{quote}

\divider

\itm{2} \textbf{\B{সংকরািয়নের প্রকারভেদ, জ্যামিতিক আকৃতি ও বন্ধন কোণের পূর্ণাঙ্গ ছক:}}

\begin{tabular}{|c|c|c|c|c|l|}
\hline
\B{সংকর সংখ্যা ($H$)} & \B{প্রকারভেদ} & \B{মুক্তজোড় (LP)} & \B{প্রকৃত জ্যামিতিক আকৃতি} & \B{আদর্শ বন্ধন কোণ} & \B{বাস্তব উদাহরণ} \\
\hline
\lat 2 & \lat sp & 0 & রৈখিক (\lat Linear) & \lat 180$^{\circ}$ & \lat BeCl$_2$, C$_2$H$_2$, CO$_2$ \\
\hline
\lat 3 & \lat sp$^2$ & 0 & সমতলীয় ত্রিভুজাকার (\lat Trigonal Planar) & \lat 120$^{\circ}$ & \lat BF$_3$, C$_2$H$_4$, SO$_3$ \\
\hline
\lat 3 & \lat sp$^2$ & 1 & কৌণিক / V-আকৃতি (\lat Bent / V-shape) & \lat < 120$^{\circ}$ (প্রকৃত $119.5^\circ$) & \lat SO$_2$, O$_3$ \\
\hline
\lat 4 & \lat sp$^3$ & 0 & সুষম চতুস্তলকীয় (\lat Tetrahedron) & \lat 109.5$^{\circ}$ / $109^\circ28'$ & \lat CH$_4$, CCl$_4$, NH$_4^+$ \\
\hline
\lat 4 & \lat sp$^3$ & 1 & ত্রিকোণীয় পিরামিডাল (\lat Trigonal Pyramidal) & \lat 107$^{\circ}$ (LP-BP বিকর্ষণ) & \lat NH$_3$, PH$_3$, H$_3$O$^+$ \\
\hline
\lat 4 & \lat sp$^3$ & 2 & কৌণিক / V-আকৃতি (\lat Bent / V-shape) & \lat 104.5$^{\circ}$ (২টি LP এর তীব্র বিকর্ষণ) & \lat H$_2$O, H$_2$S, NH$_2^-$ \\
\hline
\lat 4 & \lat dsp$^2$ & 0 & বর্গাকার সমতলীয় (\lat Square Planar) & \lat 90$^{\circ}$ & \lat [Ni(CN)$_4$]$^{2-}$, [PtCl$_4$]$^{2-}$ \\
\hline
\lat 5 & \lat sp$^3$ & 0 & ত্রিকোণীয় দ্বিপিরামিডাল (\lat Trigonal Bipyramidal) & \lat 90$^{\circ}$ \B{ এবং } 120$^{\circ}$ & \lat PCl$_5$, PF$_5$ \\
\hline
\lat 5 & \lat sp$^3$d & 1 & সী-স / ঢেকী আকৃতি (\lat See-saw) & \lat <90$^{\circ}$ / <120$^{\circ}$ & \lat SF$_4$ \\
\hline
\lat 5 & \lat sp$^3$d & 2 & T-আকৃতি (\lat T-shaped) & \lat 90$^{\circ}$ & \lat ClF$_3$, ICl$_3$ \\
\hline
\lat 5 & \lat sp$^3$d & 3 & রৈখিক (\lat Linear) & \lat 180$^{\circ}$ & \lat XeF$_2$, I$_3^-$ \\
\hline
\lat 6 & \lat sp$^3$d$^2$ & 0 & সুষম অষ্টতলকীয় (\lat Octahedral) & \lat 90$^{\circ}$ & \lat SF$_6$, [Co(NH$_3$)$_6$]$^{3+}$ \\
\hline
\lat 6 & \lat sp$^3$d$^2$ & 2 & বর্গাকার সমতলীয় (\lat Square Planar) & \lat 90$^{\circ}$ & \lat XeF$_4$ \\
\hline
\lat 7 & \lat sp$^3$d$^3$ & 0 & পঞ্চকোণীয় দ্বিপিরামিডাল (\lat Pentagonal Bipyramid) & \lat 72$^{\circ}$ \B{ এবং } 90$^{\circ}$ & \lat IF$_7$ \\
\hline
\lat 7 & \lat sp$^3$d$^3$ & 1 & বিকৃত অষ্টতলকীয় (\lat Distorted Octahedral) & \lat <90$^{\circ}$ & \lat XeF$_6$ \\
\hline
\end{tabular}

\chsec{অধ্যায়-৪: রাসায়নিক পরিবর্তন}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{শতকরা এটম ইকনমি (}} {\lat \%AE} \textbf{\B{)}} {\lat $= \dfrac{\text{\B{কাঙ্ক্ষিত উৎপাদের মোট ভর}}}{\text{\B{সমস্ত বিক্রিয়ক বা উৎপাদের মোট ভর}}} \times 100$}

\itm{2} \textbf{\B{বিক্রিয়ার হার}} {\lat $= \dfrac{\Delta C}{\Delta t}$}
\begin{itemize}
    \item[] {\lat $\Delta C$} = \B{ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta t$} = \B{সময়ের পরিবর্তন} {\lat [s]}
\end{itemize}

\itm{3} \textbf{\B{বিক্রিয়ার হার}} {\lat $= -\dfrac{\Delta c}{\Delta t} = \dfrac{\Delta x}{\Delta t}$}
\begin{itemize}
    \item[] {\lat $\Delta c$} = \B{বিক্রিয়কের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta x$} = \B{উৎপাদের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta t$} = \B{ব্যয়িত সময়} {\lat [s, min]}
\end{itemize}

\itm{4} {\lat $aA + bB \rightarrow mM + nN$} \textbf{\B{সাম্যাবস্থায় বিক্রিয়ার হার,}}
{\lat $-\dfrac{1}{a}\dfrac{\Delta[A]}{\Delta t} = -\dfrac{1}{b}\dfrac{\Delta[B]}{\Delta t} = \dfrac{1}{m}\dfrac{\Delta[M]}{\Delta t} = \dfrac{1}{n}\dfrac{\Delta[N]}{\Delta t}$}
\begin{itemize}
    \item[] {\lat $\Delta[A]$} = {\lat $A$} \B{বিক্রিয়কের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta[B]$} = {\lat $B$} \B{বিক্রিয়কের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta[M]$} = {\lat $M$} \B{উৎপাদের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $\Delta[N]$} = {\lat $N$} \B{উৎপাদের ঘনমাত্রার পরিবর্তন} {\lat [mol/L, M]}
    \item[] {\lat $t$} = \B{সময়ের ব্যবধান} {\lat [s]}
\end{itemize}

\itm{5} \textbf{\B{১ম ক্রম বিক্রিয়ার হার ধ্রুবক,}} {\lat $k_1 = \dfrac{1}{t} \ln \dfrac{a}{a - x}$} \quad \textbf{\B{বা,}} \quad {\lat $k_1 = \dfrac{2.303}{t} \log \dfrac{a}{a - x}$}
\begin{itemize}
    \item[] {\lat $a$} = \B{বিক্রিয়কের আদি ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $x$} = \B{উৎপাদের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{6} \textbf{\B{১ম ক্রম বিক্রিয়ার অর্ধায়ু,}} {\lat $t_{1/2} = \dfrac{0.693}{k_1}$} \quad [{\lat $k_1$} = \B{বিক্রিয়ার হার ধ্রুবক,} {\lat s$^{-1}$}]

\itm{7} \textbf{\B{২য় ক্রম বিক্রিয়ার হার ধ্রুবক,}} {\lat $k_2 = \dfrac{x}{t a (a - x)}$}
\begin{itemize}
    \item[] {\lat $t$} = \B{সময়ের ব্যবধান} {\lat [s]}
    \item[] {\lat $a$} = \B{বিক্রিয়কের আদি ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $x$} = \B{উৎপাদের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{8} \textbf{\B{২য় ক্রম বিক্রিয়ার অর্ধায়ু,}} {\lat $t_{1/2} = \dfrac{1}{k_2 a}$} \quad [{\lat $k_2$} = \B{বিক্রিয়ার হার ধ্রুবক,} {\lat L mol$^{-1}$s$^{-1}$}]

\itm{9} \textbf{\B{অ্যারহেনিয়াস সমীকরণ,}} {\lat $k = A e^{-E_a / RT}$}
\begin{itemize}
    \item[] {\lat $k$} = \B{বিক্রিয়ার হার ধ্রুবক} {\lat [s$^{-1}$]}
    \item[] {\lat $A$} = \B{অ্যারহেনিয়াস ফ্যাক্টর বা কম্পন গুণাঙ্ক}
    \item[] {\lat $E_a$} = \B{বিক্রিয়কের সক্রিয়ণ শক্তি} {\lat [kJ mol$^{-1}$]}
    \item[] {\lat $R$} = \B{সার্বজনীন গ্যাস ধ্রুবক} {\lat [JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{কেলভিন তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{10} {\lat $\log k = \log A - \dfrac{E_a}{2.303 R T}$}\\[2pt]
\textbf{\B{সমীকরণের ঢাল}} {\lat $= -\dfrac{E_a}{2.303 R}$}

\itm{11} {\lat $\log \dfrac{K_2}{K_1} = \dfrac{E_a}{2.303 R} \left(\dfrac{T_2 - T_1}{T_1 T_2}\right)$}

\itm{12} {\lat $\ln \dfrac{K_2}{K_1} = \dfrac{E_a}{R} \left(\dfrac{1}{T_1} - \dfrac{1}{T_2}\right)$}
\begin{itemize}
    \item[] {\lat $E_a$} = \B{বিক্রিয়ার সক্রিয়ণ শক্তি} {\lat [J mol$^{-1}$]}
    \item[] {\lat $K$} = \B{বিক্রিয়ার হার ধ্রুবক} {\lat [Lmol$^{-1}$s$^{-1}$, M$^{-1}$s$^{-1}$]}
    \item[] {\lat $T$} = \B{কেলভিন স্কেলে তাপমাত্রা} {\lat [K]}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T_1$} = \B{প্রাথমিক তাপমাত্রা} {\lat [K]}, {\lat $T_2$} = \B{শেষ তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{13} {\lat $\ln \dfrac{K_2}{K_1} = -\dfrac{\Delta H}{R} \cdot \dfrac{1}{T} + \text{\B{ধ্রুবক}}$}
\begin{itemize}
    \item[] {\lat $\Delta H$} = \B{তাপ শক্তির পরিবর্তন} {\lat [kJmol$^{-1}$]}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{কেলভিন তাপমাত্রা} {\lat [K]}
\end{itemize}
\textbf{\B{সমীকরণের ঢাল}} {\lat $= \dfrac{-\Delta H}{R}$}

\itm{14} {\lat $\log K_p = -\dfrac{\Delta H}{2.303 R} \cdot \dfrac{1}{T} + \text{\B{ধ্রুবক}}$}
\begin{itemize}
    \item[] {\lat $K_p$} = \B{আংশিক চাপে সাম্যধ্রুবক} {\lat [(atm)$^{\Delta n}$]}
\end{itemize}
\textbf{\B{সমীকরণের ঢাল}} {\lat $= \dfrac{-\Delta H}{2.303 R}$}

\itm{15} \textbf{\B{সাম্যধ্রুবকের সংজ্ঞা — সাধারণ উভমুখী বিক্রিয়া:}}\\[2pt]
{\lat $aA + bB \rightleftharpoons cC + dD$}\\[3pt]
\textbf{\B{ঘনমাত্রা প্রকাশক সাম্যধ্রুবক ($K_c$):}}\\[1pt]
{\lat $K_c = \dfrac{\text{\B{উৎপাদসমূহের সাম্যাবস্থার মোলার ঘনমাত্রার গুণফল}}}{\text{\B{বিক্রিয়কসমূহের সাম্যাবস্থার মোলার ঘনমাত্রার গুণফল}}}$}\\[4pt]
{\lat $K_c = \dfrac{[C]^c\,[D]^d}{[A]^a\,[B]^b}$}
\begin{itemize}
    \item[] \B{নোট: তৃতীয় বন্ধনী {\lat [ ]} দ্বারা সাম্যাবস্থায় বিক্রিয়ক ও উৎপাদের মোলার ঘনমাত্রা বোঝায়.}
    \item[] {\lat $[A], [B]$} = \B{বিক্রিয়কের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $[C], [D]$} = \B{উৎপাদের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $a, b$} = \B{বিক্রিয়কের মোল সংখ্যা (সূচক)}; {\lat $c, d$} = \B{উৎপাদের মোল সংখ্যা (সূচক)}
\end{itemize}

\vspace{2pt}
\textbf{\B{আংশিক চাপ প্রকাশক সাম্যধ্রুবক ($K_p$):}}\\[1pt]
{\lat $K_p = \dfrac{\text{\B{উৎপাদসমূহের সাম্যাবস্থার আংশিক চাপের গুণফল}}}{\text{\B{বিক্রিয়কসমূহের সাম্যাবস্থার আংশিক চাপের গুণফল}}}$}\\[4pt]
{\lat $K_p = \dfrac{(P_C)^c\,(P_D)^d}{(P_A)^a\,(P_B)^b}$}
\begin{itemize}
    \item[] \B{নোট: {\lat $P$} দ্বারা সাম্যাবস্থায় প্রতিটি গ্যাসের নিজস্ব আংশিক চাপ বোঝায়.}
    \item[] {\lat $P_A, P_B$} = \B{বিক্রিয়কের আংশিক চাপ} {\lat [atm]}
    \item[] {\lat $P_C, P_D$} = \B{উৎপাদের আংশিক চাপ} {\lat [atm]}
\end{itemize}

\vspace{2pt}
\textbf{\B{বিস্তারিত আকার:}}\\[1pt]
{\lat $K_p = \dfrac{(P_{\text{\B{১ম উৎপাদ}}})^{\text{\B{মোল সংখ্যা}}} \times (P_{\text{\B{২য় উৎপাদ}}})^{\text{\B{মোল সংখ্যা}}}}{(P_{\text{\B{১ম বিক্রিয়ক}}})^{\text{\B{মোল সংখ্যা}}} \times (P_{\text{\B{২য় বিক্রিয়ক}}})^{\text{\B{মোল সংখ্যা}}}}$}\\[4pt]
{\lat $K_c = \dfrac{[\text{\B{১ম উৎপাদ}}]^{\text{\B{মোল সংখ্যা}}} \times [\text{\B{২য় উৎপাদ}}]^{\text{\B{মোল সংখ্যা}}}}{[\text{\B{১ম বিক্রিয়ক}}]^{\text{\B{মোল সংখ্যা}}} \times [\text{\B{২য় বিক্রিয়ক}}]^{\text{\B{মোল সংখ্যা}}}}$}

\vspace{2pt}\textbf{\B{সাধারণ রূপ (একাধিক উৎপাদ ও বিক্রিয়ক):}}\\[1pt]
{\lat $aA + bB + \dots \rightleftharpoons lL + mM + \dots$}\\[2pt]
{\lat $K_c = \dfrac{[L]^l\,[M]^m\,\dots}{[A]^a\,[B]^b\,\dots}$}
\begin{itemize}
    \item[] {\lat $[L], [M]$} = \B{উৎপাদকের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $[A], [B]$} = \B{বিক্রিয়কের ঘনমাত্রা}
\end{itemize}

\itm{16} \textbf{\B{নির্দিষ্ট কিছু গুরুত্বপূর্ণ উভমুখী বিক্রিয়ার ক্ষেত্রে }} {\lat $K_c$} \textbf{\B{ ও }} {\lat $K_p$} \textbf{\B{ এর রাশিমালা:}}\\[4pt]
\textbf{\B{১. }} {\lat $\text{PCl}_5(g) \rightleftharpoons \text{PCl}_3(g) + \text{Cl}_2(g)$} \B{ (আদি মোল = }{\lat $a$}\B{, বিয়োজন মাত্রা = }{\lat $x$}\B{):}\\[2pt]
{\lat $K_c = \dfrac{x^2}{(a-x)V}$} \quad \textbf{\B{এবং}} \quad {\lat $K_p = \dfrac{x^2 \cdot P}{a^2 - x^2}$} \quad \B{[যদি আদি মোল }{\lat $a = 1$} \B{হয়, তবে }{\lat $K_p = \dfrac{\alpha^2 P}{1-\alpha^2}$}\B{]}\\[4pt]
\textbf{\B{২. }} {\lat $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g)$} \B{ (আদি মোল = }{\lat $a, b$}\B{, বিয়োজন মাত্রা = }{\lat $x$}\B{):}\\[2pt]
{\lat $K_c = \dfrac{4x^2 V^2}{(a-x)(b-3x)^3}$} \quad \textbf{\B{এবং}} \quad {\lat $K_p = \dfrac{4x^2 (a+b-2x)^2 \cdot P^{-2}}{(a-x)(b-3x)^3}$}\\[4pt]
\textbf{\B{৩. }} {\lat $\text{H}_2(g) + \text{I}_2(g) \rightleftharpoons 2\text{HI}(g)$}\\[2pt]
{\lat $K_c = K_p = \dfrac{4x^2}{(a-x)(b-x)}$} \quad \B{[এখানে }{\lat $\Delta n = 0$}\B{, তাই আয়তন ও মোট চাপ নিরপেক্ষ]}

\itm{17} {\lat $\alpha = \dfrac{x}{n}$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}
    \item[] {\lat $x$} = \B{বিয়োজিত মোল সংখ্যা} {\lat [mol]}
    \item[] {\lat $n$} = \B{প্রাথমিক মোল সংখ্যা} {\lat [mol]}
\end{itemize}

\itm{18} {\lat $P_A = X_A \cdot P$}
\begin{itemize}
    \item[] {\lat $P_A$} = \B{আংশিক চাপ} {\lat [atm]}
    \item[] {\lat $X_A$} = \B{মোল ভগ্নাংশ}
    \item[] {\lat $P$} = \B{মোট চাপ} {\lat [atm]}
\end{itemize}

\itm{19} {\lat $X_A = \dfrac{n_A}{n}$}
\begin{itemize}
    \item[] {\lat $n_A$} = {\lat $A$} \B{বিক্রিয়কের মোল সংখ্যা} {\lat [mol]}
    \item[] {\lat $n$} = \B{বিক্রিয়া পাত্রে উপস্থিত বিক্রিয়কসমূহের মোল সংখ্যা} {\lat [mol]}
\end{itemize}

\itm{20} \textbf{\B{কোনো উভমুখী বিক্রিয়ার,}} {\lat $K_p = K_c(RT)^{\Delta n}$}
\begin{itemize}
    \item[] \B{যেখানে} {\lat $\Delta n = (l + m + n + \dots) - (a + b + c + \dots)$}
    \item[] {\lat $=$} \B{(উৎপাদের গ্যাসীয় মোল সংখ্যা)} $-$ \B{(বিক্রিয়কের গ্যাসীয় মোল সংখ্যা)}
\end{itemize}

\itm{21} {\lat $K_p = K_c$} \quad \B{[যখন {\lat $\Delta n = 0$}]}

\itm{22} \textbf{\B{মৃদু এসিডের বিয়োজন ধ্রুবক (অসওয়াল্ডের লঘুকরণ সূত্র):}} {\lat $K_a = \alpha^2 c$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{এসিডের বিয়োজন মাত্রা}
    \item[] {\lat $c$} = \B{মৃদু এসিডের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] \B{হাইড্রোজেন আয়নের ঘনমাত্রা,} {\lat $[\text{H}^+] = \sqrt{K_a \cdot c} = \alpha c$}
    \item[] \B{মৃদু অম্লের ক্ষেত্রে,} {\lat $pH = \dfrac{1}{2}pK_a - \dfrac{1}{2}\log c$}
\end{itemize}

\itm{23} \textbf{\B{মৃদু ক্ষারের বিয়োজন ধ্রুবক:}} {\lat $K_b = \alpha^2 c$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{ক্ষারের বিয়োজন মাত্রা}
    \item[] {\lat $c$} = \B{মৃদু ক্ষারের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] \B{হাইড্রোক্সিল আয়নের ঘনমাত্রা,} {\lat $[\text{OH}^-] = \sqrt{K_b \cdot c} = \alpha c$}
    \item[] \B{মৃদু ক্ষারকের ক্ষেত্রে,} {\lat $pOH = \dfrac{1}{2}pK_b - \dfrac{1}{2}\log c$}
\end{itemize}

\itm{24} {\lat $K_w = [\text{H}_3\text{O}^+] \times [\text{OH}^-] = 1 \times 10^{-14}$} \quad \B{[}{\lat 25°C}\B{ তাপমাত্রায়]}
\begin{itemize}
    \item[] {\lat $K_w$} = \B{পানির আয়নিক গুণফল} {\lat [mol$^2$ L$^{-2}$]}
    \item[] {\lat $[\text{H}_3\text{O}^+] = [\text{H}^+]$} = \B{হাইড্রোজেন আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $[\text{OH}^-]$} = \B{হাইড্রোক্সিল আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{25} {\lat $K_w = K_a \times K_b$}
\begin{itemize}
    \item[] {\lat $K_a$} = \B{এসিড বিয়োজন ধ্রুবক}
    \item[] {\lat $K_b$} = \B{ক্ষার বিয়োজন ধ্রুবক}
\end{itemize}

\itm{26} {\lat $pK_a + pK_b = 14$}

\itm{27} {\lat $pH = -\log [\text{H}^+]$} \quad [{\lat $[\text{H}^+]$} = {\lat $\text{H}^+$} \B{এর ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{28} {\lat $pOH = -\log [\text{OH}^-]$} \quad [{\lat $[\text{OH}^-]$} = {\lat $\text{OH}^-$} \B{এর ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{29} \textbf{\B{এসিডের বিয়োজন মাত্রা,}} {\lat $\alpha = \sqrt{\dfrac{K_a}{C}}$} \quad [{\lat $C$} = \B{এসিডের ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{30} \textbf{\B{ক্ষারের বিয়োজন মাত্রা,}} {\lat $\alpha = \sqrt{\dfrac{K_b}{C}}$} \quad [{\lat $C$} = \B{ক্ষারের ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{31} {\lat $pH + pOH = 14$}

\itm{32} {\lat $[\text{H}^+] = \alpha C$}
\begin{itemize}
    \item[] {\lat $[\text{H}^+]$} = \B{হাইড্রোজেন আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}
    \item[] {\lat $C$} = \B{ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{33} \textbf{\B{অম্লীয় বাফার দ্রবণের (হেন্ডারসন-হাসেলবাখ সমীকরণ):}} {\lat $pH = pK_a + \log \dfrac{[\text{\B{লবণ}}]}{[\text{\B{অম্ল}}]}$} \quad [{\lat $K_a$} = \B{অম্লের বিয়োজন ধ্রুবক}]

\itm{34} \textbf{\B{ক্ষারীয় বাফার দ্রবণের (হেন্ডারসন-হাসেলবাখ সমীকরণ):}} {\lat $pOH = pK_b + \log \dfrac{[\text{\B{লবণ}}]}{[\text{\B{ক্ষারক}}]}$}\\[2pt]
\textbf{\B{অথবা,}} {\lat $pH = 14 - pK_b - \log \dfrac{[\text{\B{লবণ}}]}{[\text{\B{ক্ষারক}}]}$} \quad [{\lat $K_b$} = \B{ক্ষারকের বিয়োজন ধ্রুবক}]

\itm{35} \textbf{\B{স্বল্পদ্রাব্য লবণের দ্রাব্যতা গুণফল:}} {\lat $A_m B_n \rightleftharpoons mA^{n+} + nB^{m-}$}\\[2pt]
{\lat $K_{SP} = [A^{n+}]^m \times [B^{m-}]^n = m^m \cdot n^n \cdot S^{m+n}$}
\begin{itemize}
    \item[] \B{যেখানে} {\lat $S$} = \B{দ্রাব্যতা} {\lat [mol\,L$^{-1}$]}; \B{এই সূত্রটিই} {\lat $x^x y^y S^{(x+y)}$} \B{রূপে লেখা হয়}
    \item[] \textbf{\B{উদাহরণ:}} {\lat $Ca_3(PO_4)_2$}: {\lat $K_{SP} = 108\,S^5$}; {\lat $BaSO_4$}: {\lat $K_{SP} = S^2$}
\end{itemize}

\itm{36} \textbf{\B{অধঃক্ষেপণের শর্ত (দ্রাব্যতা গুণফল ও আয়নিক গুণফলের সম্পর্ক):}}
\begin{itemize}
    \item[] {\lat $K_{ip} > K_{SP} \rightarrow$} \B{দ্রবণটি অতিপৃক্ত এবং অধঃক্ষেপ পড়বে.}
    \item[] {\lat $K_{ip} = K_{SP} \rightarrow$} \B{দ্রবণটি সম্পৃক্ত এবং সাম্যাবস্থায় থাকবে (অধঃক্ষেপ পড়বে না).}
    \item[] {\lat $K_{ip} < K_{SP} \rightarrow$} \B{দ্রবণটি অসম্পৃক্ত এবং কোনো অধঃক্ষেপ পড়বে না.}
\end{itemize}

\itm{37} \textbf{\B{দ্রাব্যতা ও দ্রাব্যতা গুণফলের সম্পর্ক:}}
\begin{itemize}
    \item[] {\lat $AB \rightarrow K_{SP} = S^2$} \quad {\lat $A_2B \rightarrow K_{SP} = 4S^3$}
    \item[] {\lat $AB_2 \rightarrow K_{SP} = 4S^3$} \quad {\lat $A_2B_3 \rightarrow K_{SP} = 108\,S^5$}
    \item[] {\lat $A_3B \rightarrow K_{SP} = 27\,S^4$} \quad {\lat $AB_3 \rightarrow K_{SP} = 27\,S^4$}
\end{itemize}

\itm{38} \textbf{\B{তাপগতিবিদ্যার সূত্রসমূহ:}}\\[2pt]
{\lat $\Delta G = \Delta H - T\Delta S$} \quad \B{(গিবস মুক্ত শক্তি)}
\begin{itemize}
    \item[] {\lat $\Delta G = -nFE_{cell}$} \quad {\lat $\Delta G^\circ = -RT\ln K$}
    \item[] {\lat $\Delta G^\circ = -2.303\,RT\log K$}
    \item[] {\lat $\Delta H = \Delta U + \Delta n_g RT$}
    \item[] {\lat $\Delta G < 0$} = \B{স্বতঃস্ফূর্ত}; {\lat $\Delta G > 0$} = \B{অস্বতঃস্ফূর্ত}; {\lat $\Delta G = 0$} = \B{সাম্যাবস্থা}
\end{itemize}

\itm{39} \textbf{\B{হেস সূত্র:}} \B{একটি বিক্রিয়ার তাপের পরিমাণ বিক্রিয়াটি সরাসরি বা ধাপে ধাপে সম্পন্ন হোক সমান.}\\[2pt]
{\lat $\Delta H_{rxn} = \sum \Delta H_f^\circ(\text{\B{উৎপাদ}}) - \sum \Delta H_f^\circ(\text{\B{বিক্রিয়ক}})$}

\itm{40} \textbf{\B{বন্ড শক্তি থেকে এনথালপি:}}\\[2pt]
{\lat $\Delta H = \sum$} \B{(ভাঙা বন্ধনের শক্তি)} $-$ {\lat $\sum$} \B{(তৈরি বন্ধনের শক্তি)}

\itm{41} \textbf{\B{এনট্রপি পরিবর্তন:}}\\[2pt]
{\lat $\Delta S = \dfrac{q_{rev}}{T}$} \quad [\B{প্রত্যাবর্তী প্রক্রিয়ায়}]; \quad {\lat $\Delta S_{univ} = \Delta S_{sys} + \Delta S_{surr} \geq 0$}

\itm{42} \textbf{\B{সমতাপীয় প্রসারণে কাজ:}} {\lat $w = -nRT\ln\dfrac{V_2}{V_1} = -2.303\,nRT\log\dfrac{V_2}{V_1}$}

\itm{43} \textbf{\B{তড়িৎ রাসায়নিক কোষের বিভব — নার্নস্ট সমীকরণ:}}\\[2pt]
{\lat $E_{cell} = E^\circ_{cell} - \dfrac{RT}{nF}\ln Q = E^\circ_{cell} - \dfrac{0.0592}{n}\log Q$} \B{(২৫}{\lat °C} \B{তাপমাত্রায়)}

\itm{44} \textbf{\B{বাষ্পচাপ হ্রাস (রাউল্টের সূত্র):}}\\[2pt]
{\lat $\dfrac{\Delta P}{P^\circ} = X_B = \dfrac{n_B}{n_A + n_B}$}
\begin{itemize}
    \item[] {\lat $\Delta P = P^\circ - P_s$} = \B{বাষ্পচাপ হ্রাস}; {\lat $P^\circ$} = \B{বিশুদ্ধ দ্রাবকের বাষ্পচাপ}
    \item[] {\lat $P_s$} = \B{দ্রবণের বাষ্পচাপ}; {\lat $X_B$} = \B{দ্রবের মোল ভগ্নাংশ}
\end{itemize}

\itm{45} \textbf{\B{স্ফুটনাঙ্ক উন্নয়ন:}} {\lat $\Delta T_b = K_b \times m$}\\[2pt]
\textbf{\B{হিমাঙ্ক অবনমন:}} {\lat $\Delta T_f = K_f \times m$}
\begin{itemize}
    \item[] {\lat $m$} = \B{মোলালিটি} {\lat [mol\,kg$^{-1}$]}; {\lat $K_b$} = \B{স্ফুটনাঙ্ক উন্নয়ন ধ্রুবক}; {\lat $K_f$} = \B{হিমাঙ্ক অবনমন ধ্রুবক}
\end{itemize}

\itm{46} \textbf{\B{অভিস্রবণ চাপ:}} {\lat $\pi = CRT = \dfrac{n}{V}RT$}
\begin{itemize}
    \item[] {\lat $\pi$} = \B{অভিস্রবণ চাপ} {\lat [atm]}; {\lat $C$} = \B{মোলার ঘনমাত্রা} {\lat [mol\,L$^{-1}$]}
    \item[] {\lat $R$} = \B{গ্যাস ধ্রুবক}; {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{47} \textbf{\B{আণবিক ভর নির্ণয় (হিমাঙ্ক অবনমন থেকে):}}\\[2pt]
{\lat $M_B = \dfrac{K_f \times W_B \times 1000}{\Delta T_f \times W_A}$}
\begin{itemize}
    \item[] {\lat $W_B$} = \B{দ্রবের ভর} {\lat [g]}; {\lat $W_A$} = \B{দ্রাবকের ভর} {\lat [g]}
\end{itemize}

\itm{48} \textbf{\B{ভ্যান্ট হফ গুণক:}} {\lat $i = \dfrac{\text{\B{পরিমাপকৃত সংখ্যা}}}{\text{\B{প্রত্যাশিত সংখ্যা}}} = 1 + \alpha(n-1)$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}; {\lat $n$} = \B{আয়নের সংখ্যা}
    \item[] \B{সংশোধিত সূত্র:} {\lat $\Delta T_b = i\,K_b\,m$}; {\lat $\Delta T_f = i\,K_f\,m$}; {\lat $\pi = i\,CRT$}
\end{itemize}

\itm{49} \textbf{\B{রেডক্স বিক্রিয়ায় ইলেকট্রন সংখ্যা:}}\\[2pt]
{\lat $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$}\\[2pt]
{\lat $\Delta G^\circ = -nFE^\circ_{cell}$} \quad \B{এবং} \quad {\lat $\log K = \dfrac{nE^\circ}{0.0592}$} \B{(২৫}{\lat °C} \B{তে)}

\chsec{অধ্যায়-৫: কর্মমুখী রসায়ন}

\chsub{Concept Map: The Chapter at a Glance}{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: কর্মমুখী রসায়ন}}

\textbf{{\lat 1.} \B{খাদ্য নিরাপত্তার নীতিমালা:}}
\begin{itemize}
    \item \B{পর্যাপ্ত খাদ্য প্রাপ্তি, খাদ্য গ্রহণের সামর্থ্য, খাদ্য ব্যবহার}
\end{itemize}

\textbf{{\lat 2.} \B{খাদ্য সংরক্ষণ কৌশল} $\rightarrow$ \B{প্রকারভেদ:}}
\begin{itemize}
    \item \textbf{\B{প্রাকৃতিক:}} \B{খাদ্য লবণ দ্বারা খাদ্য সংরক্ষণ, সরিষার তেল দ্বারা খাদ্য সংরক্ষণ, চিনি দ্বারা খাদ্যবস্তু সংরক্ষণ.}
    \item \textbf{\B{কৃত্রিম:}} \B{অ্যান্টি মাইক্রোবিয়াল এজেন্ট, অ্যান্টি অক্সিডেন্ট এজেন্ট, কিলেটিং এজেন্ট.}
\end{itemize}

\textbf{{\lat 3.} \B{ক্যানিং প্রসেস (মাংসে, দেশি ফল, সবজি):}}
\begin{itemize}
    \item \textbf{\B{১ম স্তর:}} \B{কাঁচামাল সংগ্রহ} $\rightarrow$ \B{গ্রেডিং বা বাছাই} $\rightarrow$ \B{ধৌতকরণ} $\rightarrow$ \B{খোসা ছাড়ানো ও ছোট টুকরা করা}
    \item \textbf{\B{২য় স্তর:}} \B{ব্লাঞ্চিং বা সিদ্ধ করা} $\rightarrow$ \B{কৌটায় ভর্তি করা} $\rightarrow$ \B{চিনির সিরাপ বা লবণ দ্রবণ যোগ করা}
    \item \textbf{\B{৩য় স্তর:}} \B{এগজস্টিং ও সিলিং} $\rightarrow$ \B{রিটর্টিং বা নির্বীজকরণ} $\rightarrow$ \B{কৌটা শীতলকরণ} $\rightarrow$ \B{লেবেলিং ও গুদামজাতকরণ}
\end{itemize}

\textbf{{\lat 4.} \B{দুধের শতকরা সংযুক্তি:}}
\begin{itemize}
    \item \B{পানি, চর্বি, প্রোটিন, দুগ্ধচিনি বা ল্যাকটোজ, দুধের খনিজ উপাদান, ভিটামিন ও অন্যান্য উপাদান}
\end{itemize}

\textbf{{\lat 5.} \B{মাখন পৃথকীকরণ:}}
\begin{itemize}
    \item \B{রেফ্রিজারেশন, কোয়াগুলেশন, ক্রীমের প্রসেসিং, মাখন মন্থন, মাখনে লবণ প্রয়োগ, রেফ্রিজারেশন}
\end{itemize}

\textbf{{\lat 6.} \B{ঘি উৎপাদন} $\rightarrow$ \B{উপাদান ও সরঞ্জাম:}}
\begin{itemize}
    \item \textbf{\B{উপাদান:}} \B{লবণমুক্ত সাদা বাটার, তেজপাতা, রান্নার লবণ, পরিষ্কার কাপড়, স্টিলের পুরুতলযুক্ত কড়াই, বড় চামচ, থার্মোমিটার (} {\lat 150$^\circ$C} \B{ বা } {\lat 200$^\circ$C} \B{), বার্নার বা চুলা}
    \item \textbf{\B{সরঞ্জাম:}} \B{স্টিলের পাত্র, ঢাকনিসহ বয়েম, সূক্ষ্ম সুতার পরিষ্কার কাপড়, তেজপাতা, বড় চামচ, চুলা, থার্মোমিটার}
\end{itemize}

\textbf{{\lat 7.} \B{টয়লেট্রিজ সামগ্রী যোগ করায় রসায়ন:}}
\begin{itemize}
    \item \textbf{\B{হেয়ার অয়েল উপাদান:}} \B{চুলের কোমলতাবর্ধক, ইমালসিফায়ার, অ্যান্টিঅক্সিডেন্ট, মেনথল, মিন্ট অয়েল, রোজমেরি, রং}
    \item \textbf{\B{নমুনা:}} \B{নারিকেল তেল,} {\lat t}-\B{বিউটাইল অ্যালকোহল, ক্যানোলা অয়েল, মিন্ট অয়েল, রং বা ডাই}
    \item \textbf{\B{বেবি পাউডার নমুনা:}} \B{ট্যালক, ম্যাগনেসিয়াম স্টিয়ারেট, বোরিক এসিড পাউডার, ম্যাগনেসিয়াম কার্বনেট, জিংক অক্সাইড, স্টিরাইল অ্যালকোহল}
    \item \textbf{\B{স্নো নমুনা:}} \B{সয়াবিন অয়েল, স্টিরাইল অ্যালকোহল, পলি ইথাইলিন গ্লাইকল, গ্লিসারিন মনোস্টিয়ারেট, সোডিয়াম লরাইল সালফেট, গ্লিসারিন, পাতিত পানি, সুগন্ধি}
    \item \textbf{\B{কোল্ড ক্রিম নমুনা:}} \B{মিনারেল অয়েল, হোয়াইট বি-ওয়াক্স, গ্লিসারিন, বোরাক্স, পাতিত পানি, সুগন্ধি রোজমেরি}
    \item \textbf{\B{ট্যালকম নমুনা:}} \B{ট্যালক (হাইড্রেটেড ম্যাগনেসিয়াম সিলিকেট), জিংক স্টিয়ারেট, ম্যাগনেসিয়াম কার্বনেট, মেনথল}
    \item \textbf{\B{লিপস্টিক উপাদান:}} \B{ওয়াক্স চর্বি, অয়েল, অ্যালকোহল, পিগমেন্ট, সুগন্ধ বস্তু}
    \item \textbf{\B{আফটার শেভ উপাদান:}} \B{অ্যান্টিসেপটিক, ময়েশ্চারাইজার, সুগন্ধ বস্তু}
    \item \textbf{\B{আফটার শেভ নমুনা:}} \B{ডি ন্যাচার্ড অ্যালকোহল-৪০, অলিভ অয়েল, কমলা লেবুর খোসা, দারুচিনি, লবঙ্গ}
\end{itemize}

\textbf{{\lat 8.} \B{ক্লিনিং এজেন্টের রসায়ন ও উপাদান:}}
\begin{itemize}
    \item \textbf{\B{গ্লাস ক্লিনার উপাদান:}} \B{অ্যামোনিয়া দ্রবণ (প্রধান উপাদান), আইসোপ্রোপাইল অ্যালকোহল, সোডিয়াম লরাইল সালফেট, টেট্রাসোডিয়াম } {\lat EDTA}\B{, পাতিত পানি, রং বা ডাই}
    \item \textbf{\B{টয়লেট ক্লিনার উপাদান:}} \B{সোডিয়াম হাইড্রোক্সাইড (প্রধান উপাদান), সোডিয়াম হাইপোক্লোরাইট (ব্লিচিং এজেন্ট), সোডিয়াম লরাইল ইথার সালফেট, সুগন্ধি, পানি}
\end{itemize}

\textbf{{\lat 9.} \B{মেহেদির রঞ্জন কৌশল ও রসায়ন:}}
\begin{itemize}
    \item \textbf{\B{প্রধান উপাদান:}} \B{লসোনে (} {\lat 2-hydroxy-1,4-naphthoquinone} \B{)}
    \item \textbf{\B{রঞ্জন কৌশল:}} \B{ত্বক ও চুলের কেরাটিন প্রোটিনের সাথে লসোনের স্থায়ী রাসায়নিক বন্ধন (মাইকেল সংযোজন) গঠনের মাধ্যমে লাল-বাদামী রঙ সৃষ্টি করা}
\end{itemize}

\textbf{{\lat 10.} \B{ভিনেগার প্রস্তুতি ও খাদ্য সংরক্ষণ কৌশল:}}
\begin{itemize}
    \item \textbf{\B{পরিচয়:}} \B{অ্যাসিটিক এসিডের } {\lat 4\%-6\%} \B{ জলীয় দ্রবণ}
    \item \textbf{\B{প্রস্তুতি:}} \B{ইথানল থেকে অ্যাসিটোভ্যাক্টর (} {\lat Acetobacter} \B{) ব্যাকটেরিয়ার উপস্থিতিতে জারণ প্রক্রিয়ার মাধ্যমে ভিনেগার উৎপাদন}
    \item \textbf{\B{সংরক্ষণ কৌশল:}} \B{খাদ্যের } {\lat pH} \B{ মান কমিয়ে অম্লীয় পরিবেশ তৈরি করা, যা ব্যাকটেরিয়া ও ছত্রাকের বংশবৃদ্ধি রোধ এবং এনজাইমের কার্যকারিতা নষ্ট করে}
\end{itemize}

---

\chsub{}{প্রয়োজনীয় সূত্রাবলি ও গুরুত্বপূর্ণ তথ্য (সূত্র যখন হাতের মুঠোয় - 1000305916.jpg)}

\itm{1} \textbf{\B{পানি সক্রিয়তা,}} {\lat $a_w = \dfrac{\text{\B{খাদ্যবস্তুতে থাকা জলীয় বাষ্পের পরিমাণ}}}{\text{\B{খাদ্যবস্তুর চারপাশের পরিবেশে থাকা জলীয় বাষ্পের পরিমাণ}}}$}

\itm{2} \textbf{\B{পানি সক্রিয়তা }} {\lat $a_w$} \textbf{\B{ এর মান সর্বদা }} {\lat (0 - 1)} \textbf{\B{ এর মধ্যে থাকে.}}

\itm{3} \textbf{\B{পানি-বাষ্পহীন খালি খাদ্যে }} {\lat $a_w = 0$}

\itm{4} \textbf{\B{খাদ্যবস্তুতে অণুজীবের বংশবৃদ্ধি ও }} {\lat $a_w$} \textbf{\B{ এর সম্পর্ক:}}
\begin{itemize}
    \item[i.] \B{ব্যাকটেরিয়া বৃদ্ধির জন্য,} {\lat $a_w > 0.90$}
    \item[ii.] \B{ইস্ট জন্মানোর জন্য,} {\lat $a_w > 0.88$}
    \item[iii.] \B{ছত্রাক জন্মানোর জন্য,} {\lat $a_w > 0.80$}
\end{itemize}

\itm{5} \textbf{\B{ফ্রিজিং এর তাপমাত্রা }} {\lat $0^\circ\text{C} - 4^\circ\text{C}$}

\itm{6} \textbf{\B{ডিপফ্রিজিং বা হিমায়নের তাপমাত্রা, }} {\lat $(-5^\circ\text{C}) - (-18^\circ\text{C})$}

\itm{7} \textbf{\B{চিনির সিরাপ: }} {\lat 65-70\%}\textbf{\B{, চিনির দ্রবণ}}

\itm{8} \textbf{\B{গুরুত্বপূর্ণ গাঠনিক সংকেত (Antioxidants):}}
\begin{itemize}
    \item \textbf{\B{BHA (Butylated Hydroxyanisole):}} \B{বেনজিন বলয়ের }{\lat 1}\B{-নং অবস্থানে }{\lat $-\text{OH}$}\B{, }{\lat 2}\B{-নং অবস্থানে }{\lat $-\text{C(CH}_3)_3$}\B{ এবং }{\lat 4}\B{-নং অবস্থানে }{\lat $-\text{O-CH}_3$}\B{ মূলক যুক্ত থাকে.}
    \item \textbf{\B{BHT (Butylated Hydroxytoluene):}} \B{বেনজিন বলয়ের }{\lat 1}\B{-নং অবস্থানে }{\lat $-\text{OH}$}\B{, }{\lat 2, 6}\B{-নং অবস্থানে দুটি }{\lat $-\text{C(CH}_3)_3$}\B{ এবং }{\lat 4}\B{-নং অবস্থানে }{\lat $-\text{CH}_3$}\B{ মূলক যুক্ত থাকে.}
    \item \textbf{\B{TBHQ (tert-Butylhydroquinone):}} \B{বেনজিন বলয়ের }{\lat 1}\B{ ও }{\lat 4}\B{-নং অবস্থানে দুটি }{\lat $-\text{OH}$}\B{ এবং }{\lat 2}\B{-নং অবস্থানে }{\lat $-\text{C(CH}_3)_3$}\B{ মূলক যুক্ত থাকে.}
    \item \textbf{\B{Propyl-gallate:}} \B{বেনজিন বলয়ের }{\lat 3, 4, 5}\B{-নং অবস্থানে তিনটি }{\lat $-\text{OH}$}\B{ এবং }{\lat 1}\B{-নং অবস্থানে এস্টার মূলক }{\lat $\text{O = C - O - C}_3\text{H}_7$}\B{ যুক্ত থাকে.}
\end{itemize}


\chsub{}{গুরুত্বপূর্ণ প্রভাবকসমূহ}

\chsub{}{গুরুত্বপূর্ণ বিক্রিয়া ও প্রভাবক}

\textbf{\B{জৈব বিক্রিয়া ও প্রভাবক:}}
\begin{itemize}
    \item \B{ডিকার্বক্সিলেশন বিক্রিয়া} $\rightarrow$ {\lat NaOH + CaO} \B{বা ইথার}
    \item \B{ডাইজো বিক্রিয়া} $\rightarrow$ \B{তুষার}
    \item \B{উইটিক-ফিটিক বিক্রিয়া} $\rightarrow$ \B{অনার্দ্র} {\lat AlCl$_3$}
    \item \B{ফ্রিডেল-ক্রাফটস অ্যালকাইলেশন} $\rightarrow$ \B{অ্যালকোহলীয় কস্টিক সোডা বা পটাশ}
    \item \B{কার্বাইল অ্যামিন বিক্রিয়া} $\rightarrow$ \B{অ্যালকোহলীয় কস্টিক সোডা বা পটাশ}
    \item \B{ক্যানিজারো বিক্রিয়া} $\rightarrow$ \B{অ্যালকোহল ঘুঁটি}
    \item \B{জট গঠন} $\rightarrow$ \B{হিম শীতল কার}
    \item \B{মুলডালেন বা অ্যাসিডিক অর্ধ বিশ্লেষণ} $\rightarrow$ \B{প্রথমে ও পরে এসিডীয় অর্ধ বিশ্লেষণ}
    \item \B{নিরুদয়ন পরীক্ষা} $\rightarrow$ \B{গাঢ় সালফিউরিক এসিড}
    \item \B{হ্যালজান সংযোজন বিক্রিয়া} $\rightarrow$ \B{জারীয় মাধ্যম}
    \item \B{মূলধাম বিক্রিয়া} $\rightarrow$ \B{হিম শীতল কার}
    \item \B{ক্যানিজারো বিক্রিয়া} $\rightarrow$ \B{গাঢ়} {\lat NaOH, K$_2$CO$_3$} \B{বা গাঢ়} {\lat KOH} \B{দ্রবণ}
    \item \B{আলড়ল ঘনীভবন বিক্রিয়া} $\rightarrow$ \B{লঘু} {\lat K$_2$CO$_3$} \B{বা} {\lat NaOH}
    \item \B{হ্যালোফর্ম বিক্রিয়া} $\rightarrow$ {\lat NaOH/KOH} \B{(তাপ)}
    \item \B{উইলিয়ামসন বিক্রিয়া} $\rightarrow$ \B{নিরুদক পদার্থ (গাঢ় সালফিউরিক এসিড)}
    \item \B{গ্রিগনার্ড বিক্রিয়া} $\rightarrow$ {\lat Mg/BsSO$_4$}
\end{itemize}

\chsub{}{কার্যকরী মূলক, এর সক্রিয়তা ও শনাক্তকরণ}

\chsub{}{কার্যকরী মূলকের তালিকা}

\begin{itemize}
    \item \textbf{\B{আলকিন}} $\rightarrow$ \B{আলকিন বা অলিফিন মূলক;} {\lat $>\text{C}{=}\text{C}<$}
    \item \textbf{\B{আলকাইন}} $\rightarrow$ \B{অ্যাসিটিলিন মূলক;} {\lat $-\text{C}{\equiv}\text{C}-$}
    \item \textbf{\B{আলকোহল (১{\lat $^\circ$}):}} {\lat $-\text{CH}_2\text{OH}$}; \textbf{\B{(২{\lat $^\circ$}):}} {\lat $=\text{CHOH}$}; \textbf{\B{(৩{\lat $^\circ$}):}} {\lat $\equiv\text{COH}$}
    \item \textbf{\B{কিটোন}} $\rightarrow$ \B{কার্বোনিল মূলক;} {\lat $>\text{C}{=}\text{O}$}
    \item \textbf{\B{আলডিহাইড}} $\rightarrow$ {\lat $-\text{CHO}$}
    \item \textbf{\B{কার্বক্সিলিক এসিড}} $\rightarrow$ {\lat $-\text{COOH}$}
    \item \textbf{\B{এস্টার}} $\rightarrow$ {\lat $-\text{COOR}$}
    \item \textbf{\B{আনহাইড্রাইড}} $\rightarrow$ {\lat $-\text{CO{-}O{-}CO}-$}
    \item \textbf{\B{ইথার}} $\rightarrow$ {\lat $\text{R{-}O{-}R}$}
    \item \textbf{\B{আমিন (আমিনো মূলক)}} $\rightarrow$ {\lat $-\text{NH}_2$}
    \item \textbf{\B{এসিড আমাইড (আমাইডো মূলক)}} $\rightarrow$ {\lat $-\text{CONH}_2$}
    \item \textbf{\B{এসিড হ্যালাইড}} $\rightarrow$ {\lat $-\text{COX}$}
    \item \textbf{\B{সালফোনিক এসিড}} $\rightarrow$ {\lat $-\text{SO}_3\text{H}$}
    \item \textbf{\B{নাইট্রো যৌগ (নাইট্রো মূলক)}} $\rightarrow$ {\lat $-\text{NO}_2$}
    \item \textbf{\B{সায়ানাইড}} $\rightarrow$ {\lat $-\text{CN}$}
    \item \textbf{\B{আইসোসায়ানাইড}} $\rightarrow$ {\lat $-\text{NC}$}
    \item \textbf{\B{আইসো-থায়োসায়ানেট}} $\rightarrow$ {\lat $-\text{NCS}$} \B{বা} {\lat $-\text{N}{=}\text{C}{=}\text{S}$}
    \item \textbf{\B{নাইট্রোসো মূলক}} $\rightarrow$ {\lat $-\text{NO}$} \B{বা} {\lat $-\text{N}{=}\text{O}$}
    \item \textbf{\B{ফেনল (ফেনলিক মূলক)}} $\rightarrow$ {\lat Ar{-}OH} \B{বা} {\lat $=\text{C{-}OH}$}
    \item \textbf{\B{থায়ো যৌগ (থায়ল মূলক)}} $\rightarrow$ {\lat R{-}SH} \B{বা} {\lat $-\text{S{-}H}$}
\end{itemize}

\clearpage

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{রসায়ন দ্বিতীয় পত্র — প্রয়োজনীয় সূত্রাবলী ও তথ্যসমূহ}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: পরিবেশ রসায়ন}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{বয়েলের সূত্র,}} {\lat $P_1 V_1 = P_2 V_2$}
\begin{itemize}
    \item[] {\lat $P_1$} = \B{প্রাথমিক অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $P_2$} = \B{পরিবর্তিত অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V_1$} = \B{প্রাথমিক অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$]}
    \item[] {\lat $V_2$} = \B{পরিবর্তিত অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$]}
\end{itemize}

\itm{2} \textbf{\B{চার্লসের সূত্র,}} {\lat $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$}
\begin{itemize}
    \item[] {\lat $V_1$} = \B{প্রাথমিক অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $V_2$} = \B{পরিবর্তিত অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $T_1$} = \B{প্রাথমিক অবস্থায় তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
    \item[] {\lat $T_2$} = \B{পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
\end{itemize}

\itm{3} \textbf{\B{গে-লুস্যাকের চাপের সূত্র,}} {\lat $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$}
\begin{itemize}
    \item[] {\lat $P_1$} = \B{প্রাথমিক অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $P_2$} = \B{পরিবর্তিত অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $T_1$} = \B{প্রাথমিক অবস্থায় তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
    \item[] {\lat $T_2$} = \B{পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
\end{itemize}

\itm{4} \textbf{\B{বয়েল ও চার্লসের সমন্বয় সূত্র,}} {\lat $\dfrac{P_1 V_1}{T_1} = \dfrac{P_2 V_2}{T_2}$}
\begin{itemize}
    \item[] {\lat $P_1, P_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V_1, V_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $T_1, T_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
\end{itemize}

\itm{5} \textbf{\B{গ্যাসের ঘনত্ব, তাপ ও চাপের মধ্যে সম্পর্ক,}} {\lat $\dfrac{d_1 T_1}{P_1} = \dfrac{d_2 T_2}{P_2}$}
\begin{itemize}
    \item[] {\lat $d_1$} = \B{প্রাথমিক অবস্থায় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
    \item[] {\lat $d_2$} = \B{পরিবর্তিত অবস্থায় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
    \item[] {\lat $P_1, P_2$} = \B{চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $T_1, T_2$} = \B{তাপমাত্রা} {\lat [K} \B{(কেলভিন)}{\lat ]}
\end{itemize}

\itm{6} \textbf{\B{অ্যাভোগেড্রো সূত্র,}} {\lat $\dfrac{V_1}{V_2} = \dfrac{n_1}{n_2}$}
\begin{itemize}
    \item[] {\lat $V_1$} = \B{প্রাথমিক অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $V_2$} = \B{পরিবর্তিত অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $n_1$} = \B{প্রাথমিক অবস্থায় মোলসংখ্যা} {\lat [mol]}
    \item[] {\lat $n_2$} = \B{পরিবর্তিত অবস্থায় মোলসংখ্যা} {\lat [mol]}
\end{itemize}

\itm{7} \textbf{\B{আদর্শ গ্যাসের সমীকরণ:}}
\begin{itemize}
    \item[] \textbf{(i)} {\lat $PV = nRT$}
    \item[] \textbf{(ii)} {\lat $PV = \dfrac{W}{M}\,RT$}
    \item[] \textbf{(iii)} {\lat $PV = \dfrac{N}{N_A}\,RT$}
    \item[] \textbf{(iv)} {\lat $d = \dfrac{PM}{RT}$}
    \item[] {\lat $P$} = \B{গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V$} = \B{গ্যাসের আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $n$} = \B{গ্যাসের মোলসংখ্যা} {\lat [mol]}
    \item[] {\lat $W$} = \B{গ্যাসের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{গ্যাসের আণবিক ভর} {\lat [gmol$^{-1}$]}
    \item[] {\lat $N$} = \B{মোট অণুর সংখ্যা}
    \item[] {\lat $N_A$} = \B{আভোগেড্রো সংখ্যা}
    \item[] {\lat $d$} = \B{গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [L-atmK$^{-1}$mol$^{-1}$, JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{8} \textbf{\B{সংকোচনশীল গুণাঙ্ক,}} {\lat $Z = \dfrac{PV}{nRT}$}
\begin{itemize}
    \item[] {\lat $P$} = \B{গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V$} = \B{গ্যাসের আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $n$} = \B{গ্যাসের মোলসংখ্যা} {\lat [mol]}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [L-atmK$^{-1}$mol$^{-1}$, JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{9} \textbf{\B{ভ্যানডারওয়ালস সমীকরণ,}} {\lat $\left(P + \dfrac{n^2 a}{V^2}\right)(V - nb) = nRT$}
\begin{itemize}
    \item[] {\lat $P$} = \B{গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V$} = \B{গ্যাসের আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $a, b$} = \B{ভ্যানডারওয়ালস ধ্রুবক}
    \item[] {\lat $n$} = \B{গ্যাসের মোলসংখ্যা} {\lat [mol]}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [L-atmK$^{-1}$mol$^{-1}$, JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{10} \textbf{\B{গ্রাহামের ব্যাপন সূত্র,}}\\[2pt]
{\lat $\dfrac{r_1}{r_2} = \dfrac{t_2}{t_1} = \sqrt{\dfrac{M_2}{M_1}} = \dfrac{V_1}{V_2} = \sqrt{\dfrac{d_2}{d_1}}$}
\begin{itemize}
    \item[] {\lat $r_1, r_2$} = \B{১ম/২য় গ্যাসের ব্যাপন হার} {\lat [Ls$^{-1}$]}
    \item[] {\lat $t_1, t_2$} = \B{১ম/২য় গ্যাসের ব্যাপন সময়} {\lat [s]} \B{(সেকেন্ড)}
    \item[] {\lat $M_1, M_2$} = \B{১ম/২য় গ্যাসের আণবিক ভর} {\lat [gmol$^{-1}$]}
    \item[] {\lat $V_1, V_2$} = \B{১ম/২য় গ্যাসের বেগ} {\lat [ms$^{-1}$, cms$^{-1}$]}
    \item[] {\lat $d_1, d_2$} = \B{১ম/২য় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
\end{itemize}

\itm{11} \textbf{\B{ডালটনের আংশিক চাপ সূত্র,}} {\lat $P = P_A + P_B + \dots + P_n$}\\[2pt]
\textbf{\B{আংশিক চাপ,}} {\lat $P_A = n_A \times P$}
\begin{itemize}
    \item[] {\lat $P$} = \B{গ্যাস মিশ্রণের মোট চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $P_A, P_B, \dots P_n$} = \B{গ্যাসের আংশিক চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $n_A$} = \B{গ্যাসের মোল ভগ্নাংশ}
    \item[] {\lat $P_1, P_2$} = \B{১ম/২য় গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
\end{itemize}

\itm{12} \textbf{\B{আদর্শ গ্যাসের গতীয় সমীকরণ,}} {\lat $PV = \dfrac{1}{3} mNC^2$}
\begin{itemize}
    \item[] {\lat $P$} = \B{গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V$} = \B{গ্যাসের আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $m$} = \B{একটি অণুর ভর} {\lat [g]}
    \item[] {\lat $N$} = \B{মোট অণুসংখ্যা}
    \item[] {\lat $C$} = \B{বর্গমূল গড় বর্গ গতিবেগ} {\lat [m/s]}
    \item[] {\lat $C_{rms}$} = \B{বর্গমূল গড় বর্গ গতিবেগ} {\lat [m/s]}
    \item[] {\lat $C_{mp}$} = \B{সম্ভাব্যতা বেগ} {\lat [m/s]}
\end{itemize}

\itm{13} \textbf{\B{বর্গমূল গড় বর্গ গতিবেগ,}}\\[2pt]
{\lat $C_{rms} = \sqrt{\dfrac{3RT}{M}} = \sqrt{\dfrac{3PV}{M}} = \sqrt{\dfrac{3P}{d}}$}
\begin{itemize}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [L-atmK$^{-1}$mol$^{-1}$, JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
    \item[] {\lat $M$} = \B{গ্যাসের আণবিক ভর} {\lat [kg/m$^3$]}
    \item[] {\lat $P$} = \B{গ্যাসের চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $d$} = \B{গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
\end{itemize}

\itm{14} \textbf{\B{সম্ভাব্যতা বেগ,}} {\lat $C_{mp} = \sqrt{\dfrac{2RT}{M}}$}

\itm{15} \textbf{\B{গড় গতিবেগ,}} {\lat $\bar{C} = \sqrt{\dfrac{8RT}{\pi M}}$}
\begin{itemize}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [L-atmK$^{-1}$mol$^{-1}$, JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
    \item[] {\lat $M$} = \B{গ্যাসের আণবিক ভর} {\lat [kg/m$^3$]}
\end{itemize}

\itm{16} \textbf{\B{আদর্শ গ্যাসের গতিশক্তির সমীকরণ:}}
\begin{itemize}
    \item[] \textbf{(i)} \B{প্রতিটি অণুর গড় গতিশক্তি} {\lat $= \dfrac{3RT}{2N}$}
    \item[] \textbf{(ii)} \B{মোলার গতিশক্তি} {\lat $= \dfrac{3}{2}\,nRT$}
    \item[] {\lat $R$} = \B{মোলার গ্যাস ধ্রুবক} {\lat [JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
    \item[] {\lat $N$} = \B{মোট অণু সংখ্যা}
    \item[] {\lat $n$} = \B{মোল সংখ্যা} {\lat [mol]}
\end{itemize}

---

\chsub{}{গুরুত্বপূর্ণ লেখচিত্র ও অনুসিদ্ধান্ত (সূত্র যখন হাতের মুঠোয়)}

\itm{17} \textbf{\B{বয়েলের সূত্রের লেখচিত্রসমূহ (ধ্রুবক তাপমাত্রায় বা সমোষ্ণ রেখা / Isotherm):}}
\begin{itemize}
    \item[i.] \textbf{{\lat $P$} \B{বনাম} {\lat $V$} \B{লেখচিত্র:}} \B{এটি একটি অধিবৃত্তাকার রেখা (Hyperbola).}
    \item[ii.] \textbf{{\lat $PV$} \B{বনাম} {\lat $P$} \B{বা} {\lat $PV$} \B{বনাম} {\lat $V$} \B{লেখচিত্র:}} \B{এটি } {\lat $P$} \B{ বা } {\lat $V$} \B{ অক্ষের সমান্তরাল সরলরেখা.}
    \item[iii.] \textbf{{\lat $P$} \B{বনাম} {\lat $\dfrac{1}{V}$} \B{লেখচিত্র:}} \B{এটি মূলবিন্দুগামী একটি সরলরেখা.}
\end{itemize}

\itm{18} \textbf{\B{চার্লসের সূত্রের লেখচিত্রসমূহ (ধ্রুবক চাপে বা সমচাপ রেখা / Isobar):}}
\begin{itemize}
    \item[i.] \textbf{{\lat $V$} \B{বনাম} {\lat $T$} \B{ (কেলভিন) লেখচিত্র:}} \B{এটি একটি মূলবিন্দুগামী সরলরেখা.}
    \item[ii.] \textbf{{\lat $V$} \B{বনাম} {\lat $t$} \B{ ($^\circ$C) লেখচিত্র:}} \B{এটি তাপমাত্রা অক্ষের ঋণাত্মক দিকে } {\lat $-273.15^\circ$C} \B{ বিন্দুতে ছেদ করে, যা পরম শূন্য তাপমাত্রা.}
\end{itemize}

\itm{19} \textbf{\B{গে-লুস্যাকের চাপের সূত্রের লেখচিত্র (ধ্রুবক আয়তনে বা সমআয়তন রেখা / Isochore):}}
\begin{itemize}
    \item[] \textbf{{\lat $P$} \B{বনাম} {\lat $T$} \B{ (কেলভিন) লেখচিত্র:}} \B{এটি একটি মূলবিন্দুগামী সরলরেখা.}
\end{itemize}

\chsub{}{মোলার গ্যাস ধ্রুবক ও গ্যাস পরিমাপের এককসমূহ}

\itm{20} \textbf{\B{মোলার গ্যাস ধ্রুবক } {\lat ($R$)} \B{ এর বিভিন্ন এককে মান:}}
\begin{itemize}
    \item[i.] \textbf{\B{লিটার-বায়ুমণ্ডল একক (L-atm unit):}} {\lat $R = 0.0821 \text{ L}\cdot\text{atm}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$}
    \item[ii.] \textbf{\B{এসআই একক (SI Unit):}} {\lat $R = 8.314 \text{ J}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$}
    \item[iii.] \textbf{\B{সিজিএস একক (CGS Unit):}} {\lat $R = 8.314 \times 10^7 \text{ erg}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$}
    \item[iv.] \textbf{\B{ক্যালরি একক (Calorie unit):}} {\lat $R = 1.987 \text{ cal}\cdot\text{K}^{-1}\cdot\text{mol}^{-1}$}
\end{itemize}

\itm{21} \textbf{\B{বোল্টজম্যান ধ্রুবক, }} {\lat $k = \dfrac{R}{N_A} = 1.38 \times 10^{-23} \text{ J}\cdot\text{K}^{-1}$}

\itm{22} \textbf{\B{গ্যাস পরিমাপের প্রমাণ অবস্থা (STP ও SATP):}}
\begin{itemize}
    \item[i.] \textbf{{\lat STP (Standard Temperature and Pressure):}}
    \begin{itemize}
        \item[] \B{তাপমাত্রা, } {\lat $T = 0^\circ\text{C} = 273.15\text{ K}$}
        \item[] \B{চাপ, } {\lat $P = 1\text{ atm} = 760\text{ mmHg} = 101.325\text{ kPa} = 1.01325 \times 10^5\text{ N}\cdot\text{m}^{-2}$}
        \item[] \B{মোলার আয়তন, } {\lat $V = 22.414\text{ L} = 22.4\text{ dm}^3$}
    \end{itemize}
    \item[ii.] \textbf{{\lat SATP (Standard Ambient Temperature and Pressure):}}
    \begin{itemize}
        \item[] \B{তাপমাত্রা, } {\lat $T = 25^\circ\text{C} = 298.15\text{ K}$}
        \item[] \B{চাপ, } {\lat $P = 1\text{ bar} = 100\text{ kPa}$}
        \item[] \B{মোলার আয়তন, } {\lat $V = 24.789\text{ L} = 24.79\text{ dm}^3$}
    \end{itemize}
\end{itemize}

\chsub{}{আংশিক চাপ, মোল ভগ্নাংশ ও জলীয় টান}

\itm{23} \textbf{\B{জলীয় বাষ্পের উপস্থিতিতে শুষ্ক গ্যাসের চাপ হিসাব:}}
\begin{itemize}
    \item[] {\lat $P_{\text{dry}} = P_{\text{moist}} - f$}
    \item[] \B{এখানে, } {\lat $f = $} \B{জলীয় বাষ্পের সম্পৃক্ত চাপ বা জলীয় টান (Aqueous tension)}
\end{itemize}

\itm{24} \textbf{\B{মোল ভগ্নাংশ } {\lat ($X$)} \B{ সংক্রান্ত গাণিতিক তথ্য:}}
\begin{itemize}
    \item[i.] \B{মিশ্রণের কোনো উপাদানের মোল সংখ্যা এবং মিশ্রণের উপাদানগুলোর মোট মোল সংখ্যার অনুপাতকে মোল ভগ্নাংশ বলে.}
    \item[ii.] {\lat $X_A = \dfrac{n_A}{n_A + n_B + \dots}$}
    \item[iii.] \B{মিশ্রণের সব উপাদানগুলোর মোল ভগ্নাংশের সমষ্টি সর্বদা ১ হয় } {\lat ($X_A + X_B + \dots = 1$).}
    \item[iv.] \B{আংশিক চাপ = মোল ভগ্নাংশ } $\times$ \B{ মোট চাপ } {\lat ($P_A = X_A \times P_{\text{total}}$)}
\end{itemize}

\chsub{}{আদর্শ ও বাস্তব গ্যাস এবং বিচ্যুতির কারণ}

\itm{25} \textbf{\B{আদর্শ ও বাস্তব গ্যাসের বৈশিষ্ট্য:}}
\begin{itemize}
    \item[i.] \textbf{\B{আদর্শ গ্যাস:}} \B{যারা সব তাপমাত্রা ও চাপে আদর্শ গ্যাসের সমীকরণ } {\lat ($PV=nRT$)} \B{ মেনে চলে. বাস্তবে কোনো আদর্শ গ্যাস নেই.}
    \item[ii.] \textbf{\B{বাস্তব গ্যাস:}} \B{যারা উচ্চ চাপ ও নিম্ন তাপমাত্রায় আদর্শ আচরণ থেকে বিচ্যুত হয় (যেমন: } {\lat H$_2$, He, N$_2$, O$_2$, CO$_2$} \B{ ইত্যাদি).}
\end{itemize}

\itm{26} \textbf{\B{বাস্তব গ্যাসের আদর্শ আচরণ থেকে বিচ্যুতির কারণ (ভ্যানডারওয়ালস সংশোধন):}}
\begin{itemize}
    \item[i.] \textbf{\B{আয়তন সংশোধন:}} \B{বাস্তব গ্যাসের অণুগুলোর নিজস্ব নির্দিষ্ট আয়তন আছে. কার্যকরী আয়তন, } {\lat $V_{\text{ideal}} = V - nb$} \B{ (এখানে } {\lat $b =$} \B{ বর্জনীয় আয়তন বা কো-ভলিউম).}
    \item[ii.] \textbf{\B{চাপ সংশোধন:}} \B{বাস্তব গ্যাসের অণুগুলোর মধ্যে আন্তঃআণবিক আকর্ষণ বল বিদ্যমান. সংশোধিত চাপ, } {\lat $P_{\text{ideal}} = P + \dfrac{n^2 a}{V^2}$} \B{ (এখানে } {\lat $a =$} \B{ আন্তঃআণবিক আকর্ষণ গুণাঙ্ক).}
\end{itemize}

\itm{27} \textbf{\B{সংকোচনশীলতা গুণাঙ্ক } {\lat ($Z$)} \B{ দ্বারা আদর্শ আচরণ পরিমাপ:}}
\begin{itemize}
    \item[i.] \B{আদর্শ গ্যাসের জন্য } {\lat $Z = 1$}
    \item[ii.] \B{বাস্তব গ্যাসের জন্য } {\lat $Z \neq 1$}
    \item[iii.] {\lat $Z < 1$} \B{ হলে গ্যাসটি আদর্শ গ্যাস অপেক্ষা অধিক সংকোচনশীল (যেমন: নিম্ন চাপে } {\lat CH$_4$, CO$_2$, N$_2$}\B{).}
    \item[iv.] {\lat $Z > 1$} \B{ হলে গ্যাসটি আদর্শ গ্যাস অপেক্ষা কম সংকোচনশীল (যেমন: সব চাপে } {\lat H$_2$, He}\B{).}
\end{itemize}

\itm{28} \textbf{\B{গুরুত্বপূর্ণ অনুসিদ্ধান্তসমূহ:}}
\begin{itemize}
    \item[i.] \textbf{\B{বয়েল তাপমাত্রা } {\lat ($T_b$):}} \B{যে তাপমাত্রায় বাস্তব গ্যাসসমূহ বয়েলের সূত্র মেনে চলে অর্থাৎ আদর্শ গ্যাসের ন্যায় আচরণ করে.}
    \item[ii.] \textbf{\B{বাস্তব গ্যাসের আদর্শ আচরণের শর্ত:}} \B{উচ্চ তাপমাত্রা ও নিম্ন চাপ.}
    \item[iii.] \textbf{\B{তরলীকরণ সহজ হওয়ার শর্ত:}} \B{ভ্যানডারওয়ালস ধ্রুবক } {\lat $a$} \B{ এর মান যত বেশি হবে, গ্যাসটি তত সহজে তরলীকৃত হবে.}
\end{itemize}

\chsec{অধ্যায়-২: জৈব রসায়ন}

\chsub{}{গুরুত্বপূর্ণ বিক্রিয়া ও বিকারক}

\itm{1} \textbf{\B{উর্টজ বিক্রিয়া (Wurtz Reaction):}} \B{Alkane প্রস্তুতি}
\begin{itemize}
    \item[] {\lat $2\text{R-X} + 2\text{Na} \xrightarrow{\text{শুষ্ক ইথার}} \text{R-R} + 2\text{NaX}$}
    \item[] \B{ব্যবহার:} উচ্চতর সমগোত্রীয় অ্যালকেন প্রস্তুতিতে ব্যবহৃত হয়.
\end{itemize}

\itm{2} \textbf{\B{মার্কনিকভ নীতি (Markovnikov's Rule):}}
\begin{itemize}
    \item[] \B{নীতি:} অপ্রতিসম অসম্পৃক্ত হাইড্রোকার্বনের সাথে অপ্রতিসম বিকারকের বিক্রিয়ায় বিকারকের ঋণাত্মক অংশটি কম হাইড্রোজেনযুক্ত দ্বিবন্ধনযুক্ত কার্বনে যুক্ত হয়.
    \item[] {\lat $\text{CH}_3\text{-CH=CH}_2 + \text{HBr} \rightarrow \text{CH}_3\text{-CH(Br)-CH}_3$ (90\%)}
\end{itemize}

\itm{3} \textbf{\B{বিপরীত মার্কনিকভ নীতি (খারাশের পারঅক্সাইড নীতি):}}
\begin{itemize}
    \item[] \B{নীতি:} জৈব পারঅক্সাইডের ({\lat $\text{R}_2\text{O}_2$}) উপস্থিতিতে অপ্রতিসম অ্যালকিনের সাথে {\lat $\text{HBr}$} এর বিক্রিয়ায় বিপরীত উৎপাদ তৈরি হয়.
    \item[] {\lat $\text{CH}_3\text{-CH=CH}_2 + \text{HBr} \xrightarrow{\text{Peroxide}} \text{CH}_3\text{-CH}_2\text{-CH}_2\text{Br}$ (99\%)}
\end{itemize}

\itm{4} \textbf{\B{ওজোনোলিসিস বিক্রিয়া (Ozonolysis):}}
\begin{itemize}
    \item[] \B{বিক্রিয়া:} অ্যালকিন বা অ্যালকাইনের সাথে ওজোনের ({\lat $\text{O}_3$}) বিক্রিয়ায় ওজোনাইড গঠন এবং পরবর্তীতে {\lat $\text{Zn/H}_2\text{O}$} দ্বারা আর্দ্রবিশ্লেষণ.
    \item[] \B{কাজ:} মূল যৌগে কার্বন-কার্বন দ্বিবন্ধন বা ত্রিবন্ধনের অবস্থান নির্ণয়.
\end{itemize}

\itm{5} \textbf{\B{নিউক্লিওফিলিক প্রতিস্থাপন বিক্রিয়া ($S_N1$ ও $S_N2$):}}
\begin{itemize}
    \item[] {\lat $S_N1$} \B{সক্রিয়তার ক্রম:} $3^\circ > 2^\circ > 1^\circ > \text{CH}_3\text{X}$ \B{(দুই ধাপে ঘটে, কার্বোকেটায়ন তৈরি হয়)}
    \item[] {\lat $S_N2$} \B{সক্রিয়তার ক্রম:} $\text{CH}_3\text{X} > 1^\circ > 2^\circ > 3^\circ$ \B{(এক ধাপে ঘটে, অবস্থান্তর অবস্থা তৈরি হয়)}
\end{itemize}

\itm{6} \textbf{\B{অ্যারোমেটিক প্রতিস্থাপন বিক্রিয়া (Electrophilic Substitution):}}
\begin{itemize}
    \item[] \B{অর্থো-প্যারা নির্দেশক (বলয় সক্রিয়কারী):} {\lat $-\text{OH}, -\text{NH}_2, -\text{CH}_3, -\text{Cl}$} (ব্যতিক্রম)
    \item[] \B{মেটা নির্দেশক (বলয় নিষ্ক্রিয়কারী):} {\lat $-\text{NO}_2, -\text{COOH}, -\text{CHO}, -\text{SO}_3\text{H}$}
\end{itemize}

---

\chsub{}{শনাক্তকরণ পরীক্ষাসমূহ}

\itm{7} \textbf{\B{অসম্পৃক্ততার পরীক্ষা (Unsaturation Test):}}
\begin{itemize}
    \item[] \B{ব্রোমিন দ্রবণ পরীক্ষা:} লাল বর্ণের ব্রোমিন দ্রবণ ({\lat $\text{Br}_2/\text{CCl}_4$}) বর্ণহীন হয়.
    \item[] \B{বেয়ার পরীক্ষা (Baeyer's Test):} ক্ষারীয় {\lat $\text{KMnO}_4$} এর গোলাপী বর্ণ বর্ণহীন হয়.
\end{itemize}

\itm{8} \textbf{\B{কার্বনিল মূলকের পরীক্ষা (Carbonyl Test):}}
\begin{itemize}
    \item[] \B{সাধারণ পরীক্ষা:} {\lat $2,4\text{-DNP}$} এর সাথে বিক্রিয়ায় হলুদ বা কমলা বর্ণের অধঃক্ষেপ দেয়.
    \item[] \B{টলেন বিকারক পরীক্ষা:} শুধু অ্যালডিহাইড সিলভার দর্পণ ({\lat $\text{Ag}$} mirror) তৈরি করে.
    \item[] \B{ফেলিং দ্রবণ পরীক্ষা:} শুধু অ্যালডিহাইড লাল অধঃক্ষেপ ({\lat $\text{Cu}_2\text{O}$}) তৈরি করে.
\end{itemize}

\itm{9} \textbf{\B{হ্যালোফর্ম / আয়োডোফর্ম পরীক্ষা:}}
\begin{itemize}
    \item[] \B{শর্ত:} মিথাইল কার্বনিল মূলক ({\lat $\text{CH}_3\text{-CO-}$} বা {\lat $\text{CH}_3\text{-CH(OH)-}$}) থাকতে হবে.
    \item[] \B{ফলাফল:} {\lat $\text{NaOH} + \text{I}_2$} এর সাথে বিক্রিয়ায় হলুদ বর্ণের আয়োডোফর্ম ({\lat $\text{CHI}_3$}) অধঃক্ষেপ পড়ে.
\end{itemize}


\chsec{অধ্যায়-৩: পরিমাণগত রসায়ন}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{মোলসংখ্যা,}} {\lat $n = \dfrac{W}{M} = \dfrac{V'}{V} = \dfrac{N}{N_A} = SV_{L} = \dfrac{PV'}{RT}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{প্রদত্ত ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{পারমাণবিক বা আণবিক ভর} {\lat [g/mol]}
    \item[] {\lat $V'$} = \B{প্রদত্ত আয়তন (}{\lat STP}\B{ তে)} {\lat [L]}
    \item[] {\lat $V = 22.4$} {\lat L} \B{(}{\lat STP}\B{ তে এক মোল গ্যাসের আয়তন)}
    \item[] {\lat $N$} = \B{প্রদত্ত অণু/পরমাণু/আয়নের সংখ্যা}
    \item[] {\lat $N_A$} = \B{আভোগেড্রো সংখ্যা} {\lat ($6.022 \times 10^{23}$)}
    \item[] {\lat $S$} = \B{ঘনমাত্রা বা মোলারিটি} {\lat [mol/L]}
\end{itemize}

\itm{2} \textbf{\B{মোলারিটি (Molarity),}} {\lat $S = \dfrac{W \times 1000}{M \times V_{\text{mL}}}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{দ্রবের আণবিক ভর}
    \item[] {\lat $V_{\text{mL}}$} = \B{দ্রবণের আয়তন} {\lat [mL]}
\end{itemize}

\itm{3} \textbf{\B{মোলালিটি (Molality),}} {\lat $m = \dfrac{W \times 1000}{M \times W'}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{দ্রবের আণবিক ভর}
    \item[] {\lat $W'$} = \B{দ্রাবকের ভর} {\lat [g]}
\end{itemize}

\itm{4} \textbf{\B{নরমালিটি (Normality),}} {\lat $N = \dfrac{W \times 1000}{E \times V_{\text{mL}}} = S \times e$}
\begin{itemize}
    \item[] {\lat $E$} = \B{তুল্য ভর} {\lat $\left(E = \dfrac{M}{e}\right)$}
    \item[] {\lat $e$} = \B{তুল্য সংখ্যা (অম্লতা/ক্ষারকতা/ইলেকট্রন সংখ্যা)}
    \item[] {\lat $S$} = \B{মোলারিটি} {\lat [mol/L]}
\end{itemize}

\itm{5} \textbf{\B{ঘনমাত্রার পারস্পরিক রূপান্তরসমূহ:}}
\begin{itemize}
    \item[] \B{মোলারিটি থেকে মোলালিটি:} {\lat $m = \dfrac{S \times 1000}{1000\rho - S \times M}$}
    \item[] \B{মোলালিটি থেকে মোলারিটি:} {\lat $S = \dfrac{m \times 1000\rho}{1000 + m \times M}$}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব} {\lat [g/mL]}
\end{itemize}

\itm{6} \textbf{\B{শতকরা মাত্রা থেকে মোলারিটিতে রূপান্তর:}}
\begin{itemize}
    \item[] {\lat $x\%\!\left(\tfrac{w}{v}\right)$}\B{ দ্রবণ হলে:} {\lat $S = \dfrac{10 \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{w}{w}\right)$}\B{ দ্রবণ হলে:} {\lat $S = \dfrac{10 \times \rho \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{V}{V}\right)$}\B{ দ্রবণ হলে:} {\lat $S = \dfrac{10 \times \rho' \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{V}{w}\right)$}\B{ দ্রবণ হলে:} {\lat $S = \dfrac{10 \times \rho \times \rho' \times x}{M}$}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব} {\lat [g/mL]}, {\lat $\rho'$} = \B{দ্রবের ঘনত্ব} {\lat [g/mL]}
\end{itemize}

\itm{7} \textbf{{\lat ppm (Parts Per Million)} \B{ও অন্যান্য ঘনমাত্রা:}}
\begin{itemize}
    \item[] {\lat $\text{ppm} = \text{mg/L} = S \times M \times 10^3$}
    \item[] {\lat $x\%\!\left(\tfrac{w}{v}\right)$} \B{দ্রবণ} {\lat $= x \times 10^4\text{ ppm}$}
    \item[] {\lat $x\%\!\left(\tfrac{w}{w}\right)$} \B{দ্রবণ} {\lat $= x \times \rho \times 10^4\text{ ppm}$}
    \item[] {\lat \text{ppb (Parts Per Billion)} $= \text{ppm} \times 10^3 = \mu\text{g/L}$}
\end{itemize}

\itm{8} \textbf{\B{দ্রবণের ঘনমাত্রা লঘুকরণ সূত্র (Dilution Formula):}} {\lat $V_1 S_1 = V_2 S_2$}

\itm{9} \textbf{\B{এসিড-ক্ষারক প্রশমন বিক্রিয়া:}} {\lat $b \times V_A \times S_A = a \times V_B \times S_B \implies \dfrac{V_A S_A}{a} = \dfrac{V_B S_B}{b}$}
\begin{itemize}
    \item[] {\lat $V_A, S_A$} = \B{এসিডের আয়তন ও মোলারিটি}
    \item[] {\lat $V_B, S_B$} = \B{ক্ষারকের আয়তন ও মোলারিটি}
    \item[] {\lat $a, b$} = \B{সমতাকৃত বিক্রিয়ায় এসিড ও ক্ষারকের মোলসংখ্যা}
\end{itemize}

\itm{10} \textbf{\B{জারন-বিজারন টাইট্রেশন সূত্র:}} {\lat $V_{ox} \times S_{ox} \times e_{ox} = V_{red} \times S_{red} \times e_{red}$}
\begin{itemize}
    \item[] {\lat $V_{ox}, S_{ox}, e_{ox}$} = \B{জারকের আয়তন, ঘনমাত্রা ও তুল্য সংখ্যা}
    \item[] {\lat $V_{red}, S_{red}, e_{red}$} = \B{বিজারকের আয়তন, ঘনমাত্রা ও তুল্য সংখ্যা}
\end{itemize}

\itm{11} \textbf{\B{মোল ভগ্নাংশ (Mole Fraction):}} {\lat $X_A = \dfrac{n_A}{n_A + n_B}$}; \quad {\lat $X_A + X_B = 1$}

\itm{12} \textbf{\B{ভরের ভাগ (Mass Fraction):}} {\lat $w_A = \dfrac{m_A}{m_{\text{solution}}}$}

---

\chsub{}{গুরুত্বপূর্ণ ছক ও তথ্যসমূহ}

\itm{13} \textbf{\B{প্রাথমিক ও সেকেন্ডারি স্ট্যান্ডার্ড পদার্থ:}}
\begin{tabular}{|l|l|}
\hline
\textbf{\B{প্রাথমিক স্ট্যান্ডার্ড পদার্থ (বায়ুতে অপরিবর্তিত থাকে)}} & \textbf{\B{সেকেন্ডারি স্ট্যান্ডার্ড পদার্থ (বায়ুর সাথে বিক্রিয়া করে)}} \\ \hline
{\lat Anhydrous $\text{Na}_2\text{CO}_3$} & {\lat NaOH, KOH} \\ \hline
{\lat Oxalic Acid ($\text{H}_2\text{C}_2\text{O}_4 \cdot 2\text{H}_2\text{O}$)} & {\lat HCl, $\text{H}_2\text{SO}_4$} \\ \hline
{\lat Potassium Dichromate ($\text{K}_2\text{Cr}_2\text{O}_7$)} & {\lat Potassium Permanganate ($\text{KMnO}_4$)} \\ \hline
{\lat Sodium Oxalate ($\text{Na}_2\text{C}_2\text{O}_4$)} & {\lat Sodium Thiosulfate ($\text{Na}_2\text{S}_2\text{O}_3 \cdot 5\text{H}_2\text{O}$)} \\ \hline
\end{tabular}

\itm{14} \textbf{\B{গুরুত্বপূর্ণ জারক-বিজারকের তুল্য সংখ্যা ($e$):}}
\begin{tabular}{|l|c|l|c|}
\hline
\textbf{\B{জারক পদার্থ}} & \textbf{\B{তুল্য সংখ্যা ($e_{ox}$)}} & \textbf{\B{বিজারক পদার্থ}} & \textbf{\B{তুল্য সংখ্যা ($e_{red}$)}} \\ \hline
{\lat $\text{KMnO}_4$ (অম্লীয়)} & {\lat 5} & {\lat $\text{FeSO}_4$ / $\text{Fe}^{2+}$} & {\lat 1} \\ \hline
{\lat $\text{K}_2\text{Cr}_2\text{O}_7$} & {\lat 6} & {\lat $\text{H}_2\text{C}_2\text{O}_4$ / Oxalate} & {\lat 2} \\ \hline
{\lat $\text{MnO}_2$} & {\lat 2} & {\lat $\text{Na}_2\text{S}_2\text{O}_3$} & {\lat 1} \\ \hline
{\lat Halogen ($\text{Cl}_2, \text{Br}_2, \text{I}_2$)} & {\lat 2} & {\lat $\text{H}_2\text{S}$} & {\lat 2} \\ \hline
\end{tabular}

\itm{15} \textbf{\B{অম্ল-ক্ষারক নির্দেশকের পিএইচ ($pH$) পরিসর ও বর্ণ:}}
\begin{tabular}{|l|c|c|c|}
\hline
\textbf{\B{নির্দেশকের নাম}} & \textbf{\B{কার্যকর $pH$ পরিসর}} & \textbf{\B{অম্লীয় মাধ্যমে বর্ণ}} & \textbf{\B{ক্ষারীয় মাধ্যমে বর্ণ}} \\ \hline
\B{মিথাইল অরেঞ্জ} & {\lat 3.1 -- 4.4} & \B{গোলাপী-লাল} & \B{হলুদ} \\ \hline
\B{মিথাইল রেড} & {\lat 4.2 -- 6.3} & \B{লাল} & \B{হলুদ} \\ \hline
\B{লিটমাস} & {\lat 5.0 -- 8.0} & \B{লাল} & \B{নীল} \\ \hline
\B{ফেনলফথালিন} & {\lat 8.2 -- 10.0} & \B{বর্ণহীন} & \B{গোলাপী} \\ \hline
\B{থাইমল ব্লু} & {\lat 8.0 -- 9.6} & \B{হলুদ} & \B{নীল} \\ \hline
\end{tabular}

\chsec{অধ্যায়-৪: তড়িৎ রসায়ন}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{আপেক্ষিক পরিবাহিতা,}} {\lat $\kappa = \dfrac{1}{\rho} = \dfrac{1}{R} \times \dfrac{l}{A} = L \times \dfrac{l}{A}$}
\begin{itemize}
    \item[] {\lat $\kappa$ (Kappa)} = \B{আপেক্ষিক পরিবাহিতা} {\lat [$\Omega^{-1}\text{cm}^{-1}$, $\text{Sm}^{-1}$]}
    \item[] {\lat $L$} = \B{পরিবাহিতা} {\lat [$\Omega^{-1}$, $\text{S}$]}
    \item[] {\lat $\Lambda$ (Lambda)} = \B{তুল্য পরিবাহিতা} {\lat [$\Omega^{-1}\text{cm}^2(\text{g.eqv})^{-1}$]}
    \item[] {\lat $\Lambda_m$} = \B{মোলার পরিবাহিতা} {\lat [$\Omega^{-1}\text{cm}^2\text{mol}^{-1}$]}
    \item[] {\lat $C$} = \B{দ্রবণের ঘনমাত্রা} {\lat [$\text{g.eqv/L}$]}
    \item[] {\lat $M$} = \B{মোলার ঘনমাত্রা} {\lat [$\text{mol/L}$, $\text{M}$]}
    \item[] {\lat $V$} = \B{দ্রবণের আয়তন} {\lat [$\text{cm}^3$]}
    \item[] {\lat $A$} = \B{তড়িৎদ্বারের প্রস্থচ্ছেদ} {\lat [$\text{cm}^2$]}
    \item[] {\lat $l$} = \B{তড়িৎদ্বারদ্বয়ের মধ্যবর্তী দূরত্ব} {\lat [$\text{cm}$]}
    \item[] {\lat $N$} = \B{নরমালিটি মাত্রা} {\lat [$\text{N}$]}
\end{itemize}

\itm{2} \textbf{\B{কোষ ধ্রুবক (Cell Constant),}} {\lat $G^* = \dfrac{l}{A}$}

\itm{3} \textbf{\B{তুল্য পরিবাহিতা ও আয়তনের সম্পর্ক,}} {\lat $\Lambda = \kappa V$}

\itm{4} \textbf{\B{ঘনমাত্রা সহ তুল্য পরিবাহিতা,}} {\lat $\Lambda = \kappa \times \dfrac{1000}{C}$}

\itm{5} \textbf{\B{মোলার পরিবাহিতা,}} {\lat $\Lambda_m = \kappa \times \dfrac{1000}{M}$}

\itm{6} \textbf{\B{নরমালিটি সহ তুল্য পরিবাহিতা,}} {\lat $\Lambda = \kappa \times \dfrac{1000}{N}$}

\itm{7} \textbf{\B{কোলরাউশের সূত্র (Kohlrausch's Law):}} {\lat $\Lambda_m^\infty = \nu_+ \lambda_+^\infty + \nu_- \lambda_-^\infty$}
\begin{itemize}
    \item[] {\lat $\lambda_+^\infty, \lambda_-^\infty$} = \B{অসীম লঘুতায় ক্যাটায়ন ও অ্যানায়নের আয়নিক পরিবাহিতা}
    \item[] {\lat $\nu_+, \nu_-$} = \B{যৌগের প্রতি অণুতে উৎপন্ন ক্যাটায়ন ও অ্যানায়নের সংখ্যা}
\end{itemize}

\itm{8} \textbf{\B{মৌলের তড়িৎ রাসায়নিক তুল্যাঙ্ক,}} {\lat $Z = \dfrac{\text{\B{মৌলের পারমাণবিক ভর}}}{F \times \text{\B{মৌলের যোজ্যতা}}} = \dfrac{M}{nF}$}
\begin{itemize}
    \item[] {\lat $Z$} = \B{তড়িৎ রাসায়নিক তুল্যাঙ্ক} {\lat [$\text{g/C}$]}
\end{itemize}

\itm{9} \textbf{\B{যৌগের তড়িৎ রাসায়নিক তুল্যাঙ্ক,}} {\lat $Z = \dfrac{\text{\B{যৌগের আণবিক ভর}}}{F \times \text{\B{ধনাত্মক অংশের মোট যোজ্যতা}}}$}

\itm{10} \textbf{\B{ফ্যারাডের ১ম সূত্র (Faraday's 1st Law):}}
\begin{itemize}
    \item \textbf{(i)} {\lat $W = ZQ$}
    \item \textbf{(ii)} {\lat $Q = It$}
    \item \textbf{(iii)} {\lat $W = ZIt$}
    \item \textbf{(iv)} {\lat $W = \dfrac{MIt}{nF} = \dfrac{EIt}{F}$}
\end{itemize}
\begin{itemize}
    \item[] {\lat $W$} = \B{সঞ্চিত বা দ্রবীভূত পদার্থের ভর} {\lat [$\text{g}$]}
    \item[] {\lat $E$} = \B{রাসায়নিক তুল্যাঙ্ক বা তুল্য ভর} {\lat $\left(E = \dfrac{M}{n}\right)$}
    \item[] {\lat $I$} = \B{তড়িৎ প্রবাহ মাত্রা} {\lat [$\text{A}$]}
    \item[] {\lat $t$} = \B{সময়} {\lat [$\text{s}$]}
    \item[] {\lat $n$} = \B{সংযোজিত বা বর্জিত ইলেকট্রন সংখ্যা বা যোজ্যতা}
    \item[] {\lat $Q$} = \B{বিদ্যুৎ আধান বা চার্জ} {\lat [$\text{C}$]}
    \item[] {\lat $F$} = \B{ফ্যারাডে ধ্রুবক} {\lat $\approx 96500\text{ C}$}
\end{itemize}

\itm{11} \textbf{\B{ফ্যারাডের ২য় সূত্র (Faraday's 2nd Law):}} {\lat $\dfrac{W_A}{W_B} = \dfrac{E_A}{E_B}$}

\itm{12} \textbf{\B{কোষ বিভব (Cell Potential),}} {\lat $E^\circ_{\text{cell}} = E^\circ_{\text{ox(anode)}} + E^\circ_{\text{red(cathode)}}$}
\begin{itemize}
    \item[] {\lat $E^\circ_{\text{cell}} = E^\circ_{\text{ox(anode)}} - E^\circ_{\text{ox(cathode)}}$}
    \item[] {\lat $E^\circ_{\text{cell}} = E^\circ_{\text{red(cathode)}} - E^\circ_{\text{red(anode)}}$}
\end{itemize}

\itm{13} \textbf{\B{নার্নস্ট সমীকরণ (Nernst Equation):}} {\lat $xA + yB^{z+} \rightleftharpoons xA^{z+} + yB$} \B{বিক্রিয়ার জন্য:}
\begin{itemize}
    \item \textbf{(i)} {\lat $E_{\text{cell}} = E^\circ_{\text{cell}} - \dfrac{RT}{nF} \ln \dfrac{[A^{z+}]^x}{[B^{z+}]^y}$}
    \item \textbf{(ii)} {\lat $25^\circ\text{C}$ বা $298\text{K}$ তাপমাত্রায়:} {\lat $E_{\text{cell}} = E^\circ_{\text{cell}} - \dfrac{0.0592}{n} \log \dfrac{[A^{z+}]^x}{[B^{z+}]^y}$}
\end{itemize}

\itm{14} \textbf{\B{মুক্ত শক্তির পরিবর্তন ও কোষ বিভবের সম্পর্ক ($\Delta G$):}}
\begin{itemize}
    \item \textbf{(i)} {\lat $\Delta G = -nFE_{\text{cell}}$}
    \item \textbf{(ii)} {\lat $\Delta G^\circ = -nFE^\circ_{\text{cell}}$}
    \item \textbf{(iii)} {\lat $\Delta G^\circ = -RT \ln K_c = -2.303 RT \log K_c$}
\end{itemize}

\itm{15} \textbf{\B{প্রমাণ হাইড্রোজেন ইলেকট্রোড (SHE) ও স্বতঃস্ফূর্ততা:}}
\begin{itemize}
    \item[] \B{প্রমাণ হাইড্রোজেন তড়িৎদ্বারের প্রমাণ বিভব:} {\lat $E^\circ = 0.00\text{ V}$}
    \item[] \B{বিক্রিয়া স্বতঃস্ফূর্ত হওয়ার শর্ত:} {\lat $E_{\text{cell}} > 0$} \B{(ধনাত্মক) এবং} {\lat $\Delta G < 0$} \B{(ঋণাত্মক)}
\end{itemize}

---

\chsub{}{পরিবেশ রসায়ন: গ্যাস সূত্রসমূহ — At a Glance}

\chsub{}{গ্যাস সূত্রের তালিকা}

\itm{1} \textbf{\B{বয়েলের সূত্র (Boyle's Law — ১৬৬২ সাল, ইংল্যান্ড):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির তাপমাত্রায় নির্দিষ্ট ভরের কোনো গ্যাসের আয়তন তার চাপের ব্যস্তানুপাতিক.
    \item[] {\lat $P_1V_1 = P_2V_2$} \quad [\B{ধ্রুবক তাপমাত্রা} {\lat $T$} \B{ও ভর} {\lat $m$}]
\end{itemize}

\itm{2} \textbf{\B{চার্লসের সূত্র (Charles's Law — ১৭৮৭ সাল, ফ্রান্স):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির চাপে নির্দিষ্ট ভরের কোনো গ্যাসের আয়তন তার পরম তাপমাত্রার সমানুপাতিক.
    \item[] {\lat $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$} \quad [\B{ধ্রুবক চাপ} {\lat $P$} \B{ও ভর} {\lat $m$}]
\end{itemize}

\itm{3} \textbf{\B{গে-লুস্যাকের চাপের সূত্র (Gay-Lussac's Pressure Law — ১৮০২ সাল):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির আয়তনে নির্দিষ্ট ভরের কোনো গ্যাসের চাপ তার পরম তাপমাত্রার সমানুপাতিক.
    \item[] {\lat $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$} \quad [\B{ধ্রুবক আয়তন} {\lat $V$} \B{ও ভর} {\lat $m$}]
\end{itemize}

\itm{4} \textbf{\B{অ্যাভোগেড্রোর সূত্র (Avogadro's Law — ১৮১১ সাল, ইতালি):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির তাপমাত্রা ও চাপে সম-আয়তনের সকল গ্যাসে সমান সংখ্যক অণু থাকে.
    \item[] {\lat $V \propto n \implies \dfrac{V_1}{n_1} = \dfrac{V_2}{n_2}$}
\end{itemize}

\itm{5} \textbf{\B{ডালটনের আংশিক চাপ সূত্র (Dalton's Partial Pressure Law — ১৮০২ সাল):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির তাপমাত্রায় পরস্পর বিক্রিয়াহীন কোনো গ্যাস মিশ্রণের মোট চাপ উপাদান গ্যাসসমূহের আংশিক চাপের সমষ্টির সমান.
    \item[] {\lat $P = P_1 + P_2 + P_3 + \dots + P_n$}
    \item[] \B{আংশিক চাপ = মোল ভগ্নাংশ $\times$ মোট চাপ} $\implies$ {\lat $P_1 = X_1 \times P$}
\end{itemize}

\itm{6} \textbf{\B{গ্রাহামের ব্যাপন সূত্র (Graham's Diffusion Law — ১৮২৯ সাল):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} স্থির তাপমাত্রা ও চাপে যেকোনো গ্যাসের ব্যাপন বা নিঃসরণ হার তার ঘনত্বের (বা আণবিক ভরের) বর্গমূলের ব্যস্তানুপাতিক.
    \item[] {\lat $\dfrac{r_1}{r_2} = \sqrt{\dfrac{d_2}{d_1}} = \sqrt{\dfrac{M_2}{M_1}} = \dfrac{t_2}{t_1}$}
\end{itemize}

\itm{7} \textbf{\B{গে-লুস্যাকের গ্যাস আয়তন সূত্র (১৮০৮ সাল):}}
\begin{itemize}
    \item[] \B{বিবৃতি:} গ্যাসীয় বিক্রিয়কসমূহ পরস্পর সরল আয়তন অনুপাতে বিক্রিয়া করে এবং উৎপাদ গ্যাসীয় হলে তার আয়তনও বিক্রিয়কসমূহের আয়তনের সাথে সরল অনুপাতে থাকে.
\end{itemize}

---

\chsec{অধ্যায়-৫: অর্থনৈতিক রসায়ন (শিল্প কারখানায় সাম্যাবস্থার প্রয়োগ)}

\chsub{}{শিল্প উৎপাদন ও অনুকূল শর্তাবলি}

\itm{1} \textbf{\B{অ্যামোনিয়া ($\text{NH}_3$) উৎপাদন:}}
\begin{itemize}
    \item[] \B{পদ্ধতির নাম:} হেবার-বশ পদ্ধতি (Habber-Bosch Process)
    \item[] \B{মূল বিক্রিয়া:} {\lat $\text{N}_2(g) + 3\text{H}_2(g) \rightleftharpoons 2\text{NH}_3(g) + \Delta H$}
    \item[] \B{অনুকূল তাপমাত্রা:} {\lat $450^\circ\text{C} - 550^\circ\text{C}$}
    \item[] \B{অনুকূল চাপ:} {\lat $200\text{ atm}$}
    \item[] \B{প্রভাবক (Catalyst):} লৌহ চূর্ণ ({\lat $\text{Fe}$}) এবং প্রভাবক সহায়ক হিসেবে মলিবডেনাম ({\lat $\text{Mo}$}) বা {\lat $\text{Al}_2\text{O}_3$}.
\end{itemize}

\itm{2} \textbf{\B{সালফিউরিক এসিড ($\text{H}_2\text{SO}_4$) উৎপাদন:}}
\begin{itemize}
    \item[] \B{পদ্ধতির নাম:} স্পর্শ প্রণালী (Contact Process)
    \item[] \B{মূল বিক্রিয়া:} {\lat $2\text{SO}_2(g) + \text{O}_2(g) \rightleftharpoons 2\text{SO}_3(g) + \Delta H$}
    \item[] \B{অনুকূল তাপমাত্রা:} {\lat $400^\circ\text{C} - 500^\circ\text{C}$}
    \item[] \B{অনুকূল চাপ:} {\lat $1.5\text{ atm} - 1.7\text{ atm}$}
    \item[] \B{প্রভাবক (Catalyst):} ভ্যানাডিয়াম পেন্টাক্সাইড ({\lat $\text{V}_2\text{O}_5$}) বা প্লাটিনাম ({\lat $\text{Pt}$}).
\end{itemize}

\itm{3} \textbf{\B{মিথানল ($\text{CH}_3\text{OH}$) উৎপাদন:}}
\begin{itemize}
    \item[] \B{পদ্ধতির নাম:} বাণিজ্যিক সংশ্লেষণ পদ্ধতি
    \item[] \B{মূল বিক্রিয়া:} {\lat $\text{CO}(g) + 2\text{H}_2(g) \rightleftharpoons \text{CH}_3\text{OH}(g)$}
    \item[] \B{অনুকূল তাপমাত্রা:} {\lat $300^\circ\text{C} - 400^\circ\text{C}$}
    \item[] \B{অনুকূল চাপ:} {\lat $200\text{ atm} - 300\text{ atm}$}
    \item[] \B{প্রভাবক (Catalyst):} জিংক অক্সাইড ({\lat $\text{ZnO}$}) ও ক্রোমিয়াম অক্সাইড ({\lat $\text{Cr}_2\text{O}_3$}) মিশ্রণ.
\end{itemize}

\itm{4} \textbf{\B{ইউরিয়া [$\text{CO(NH}_2)_2$] উৎপাদন:}}
\begin{itemize}
    \item[] \B{পদ্ধতির নাম:} বাণিজ্যিক অ্যামোনিয়াম কার্বামেট পদ্ধতি
    \item[] \B{মূল বিক্রিয়া:} {\lat $2\text{NH}_3 + \text{CO}_2 \rightleftharpoons \text{NH}_2\text{COONH}_4 \rightarrow \text{CO(NH}_2)_2 + \text{H}_2\text{O}$}
    \item[] \B{অনুকূল তাপমাত্রা:} {\lat $170^\circ\text{C} - 200^\circ\text{C}$}
    \item[] \B{অনুকূল চাপ:} {\lat $100\text{ atm} - 300\text{ atm}$}
\end{itemize}


\chsub{}{শিল্পক্ষেত্রে অনুঘটকের ব্যবহার}

\chsub{}{শিল্পক্ষেত্রে বিক্রিয়া ও অনুঘটক}

\begin{itemize}
    \item \textbf{\B{১. অ্যামোনিয়া উৎপাদন:}} {\lat $N_2 + 3H_2 \rightleftharpoons 2NH_3$}\\
    \B{অনুঘটক:} {\lat Fe} \B{(অনুঘটক সহায়ক} {\lat Mo, Al$_2$O$_3$} \B{বা} {\lat K$_2$O)}
    \item \textbf{{\lat H$_2$SO$_4$} \B{উৎপাদন:}} {\lat $2SO_2 + O_2 \rightleftharpoons 2SO_3$}; \B{অনুঘটক:} {\lat Pt} \B{বা} {\lat V$_2$O$_5$}
    \item \textbf{{\lat HNO$_3$} \B{উৎপাদন:}} {\lat $4NH_3 + 5O_2 \rightleftharpoons 4NO + 6H_2O$}; \B{অনুঘটক:} {\lat Pt}
    \item \textbf{\B{৪. তেলের হাইড্রোজিনেশন:}} {\lat $\text{R}_2\text{C}{=}\text{CR}_2 + \text{H}_2 \rightarrow \text{R}_2\text{CH{-}CHR}_2$}; \B{অনুঘটক:} {\lat Ni}
    \item \textbf{\B{৫. মিথানল উৎপাদন:}} {\lat $CO + 2H_2O \rightarrow CH_3OH$}; \B{অনুঘটক:} {\lat ZnO + Cr$_2$O$_3$}
    \item \textbf{\B{৬. তরল জ্বালানি উৎপাদন:}} {\lat $CO + H_2O \rightarrow C_nH_{2n+2} + H_2O$}; \B{অনুঘটক:} {\lat Co{-}Fe{-}Ni}
    \item \textbf{\B{৭. পেট্রোলিয়াম (ক্র্যাকিং):}} {\lat \scalebox{0.82}{$C_nH_{2n+2} \rightarrow CH_3{-}C(CH_3){-}CH_2{-}CH_3$}}; \B{অনুঘটক:} {\lat Pt+Cr+}\B{বক্সাইট}
    \item \textbf{\B{৮. ভিনেগার উৎপাদন:}} {\lat $CH_3{-}CH_2{-}OH + O_2 \rightarrow CH_3{-}COOH + H_2O$}; \B{অনুঘটক:} \B{মাইকোডার্মা অ্যাসিটি}
    \item \textbf{\B{৯. ইথানল উৎপাদন:}} {\lat $C_6H_{12}O_6 \rightarrow 2CH_3{-}CH_2{-}OH + 2CO_2$}; \B{অনুঘটক:} \B{জাইমেজ এনজাইম}
    \item \textbf{\B{১০. অ্যালকিনের পলিমারকরণ:}} \B{প্রভাবক:} {\lat Al $(C_2H_5)_3$TiCl$_3$} (\B{জিপলার-নেটা প্রভাবক})
\end{itemize}


\chsub{}{বিভিন্ন পলিমারের বৈশিষ্ট্য ও ব্যবহার}

\chsub{}{পলিমারের তালিকা}

\itm{1} \textbf{\B{পলিইথিলিন (পলিথিন):}} {\lat CH$_2${=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: নমনীয় কিন্তু শক্ত প্রকৃতির; এটা এসিড, ক্ষার ও বিভিন্ন দ্রাবক দ্বারা আক্রান্ত হয় না; উত্তম তড়িৎ অন্তরক.}
    \item \B{ব্যবহার: ওষুধ প্যাকেট; মগ, বালতি, টেবিল, রুথ; বৈদ্যুতিক তারের অন্তরক; বোতল তৈরিতে.}
\end{itemize}

\itm{2} \textbf{\B{পলিপ্রোপিলিন:}} {\lat CH$_3$CH{=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: সবচেয়ে হালকা পলিমার.}
    \item \B{ব্যবহার: দড়ি তৈরিতে, মালপত্র প্যাকেজিং; মোটরজু, কার্পেট তৈরিতে.}
\end{itemize}

\itm{3} \textbf{\B{পলিভিনাইল ক্লোরাইড (}} {\lat PVC} \textbf{\B{):}} {\lat CH$_2${=}CHCl} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}-)_n$}
\begin{itemize}
    \item \B{ব্যবহার: কৃত্রিম চামড়া; ঘরের ছাদ তৈরি; রেইন কোট, গ্রামোফোন রেকর্ড.}
\end{itemize}

\itm{4} \textbf{\B{পলিটেট্রাফ্লোরো ইথিন (}} {\lat PTFE} \B{— টেফলন):} {\lat CF$_2${=}CF$_2$} $\rightarrow$ {\lat $(-\text{CF}_2{-}\text{CF}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: ফুয়েরো কার্বন হিসেবে খুবই নিষ্ক্রিয়; বিদ্যুৎ ও তাপ অপরিবাহী.}
    \item \B{ব্যবহার: নন-স্টিক রান্নার প্যান; জাহাজের রঙে.}
\end{itemize}

\itm{5} \textbf{\B{পলিস্টাইরিন (পলিফিনাইল ইথিন):}}
\begin{itemize}
    \item \B{ব্যবহার: খাবার পাত্র, কসমেটিকের বোতল; টেলিভিশন ক্যাবিনেট; শিশুর খেলনা.}
\end{itemize}

\itm{6} \textbf{\B{নিওপ্রিন (পলি-২-ক্লোরোবিউটা-ডাই-ইন):}}
\begin{itemize}
    \item \B{ব্যবহার: সিনথেটিক রাবার তৈরিতে.}
\end{itemize}

\itm{7} \textbf{\B{পলিভিনাইল অ্যাসিটেট (}} {\lat PVA} \textbf{):} {\lat CH$_3$COO{-}CH{=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH{-}CH}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য:} {\lat PVC} \B{থেকে নমনীয়.}
    \item \B{ব্যবহার: ইমালসন পেইন্ট; গ্রামোফোন রেকর্ড.}
\end{itemize}

\itm{8} \textbf{\B{নাইলন ৬:৬:}} {\lat HOOC(CH$_2$)$_4$CONH(CH$_2$)$_6$NH$_2$} $\rightarrow$ {\lat $[-\text{OC(CH}_2)_4\text{CONH(CH}_2)_6\text{NH}-]_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: তন্তুময়.}
    \item \B{ব্যবহার: সুতা তৈরিতে.}
\end{itemize}

\itm{9} \textbf{\B{নাইলন ৬:}}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: নাইলন ৬:৬ অপেক্ষা নমনীয় ও নিম্ন গলনাঙ্ক বিশিষ্ট.}
    \item \B{ব্যবহার: তন্তু হিসাবে, কাপড়ের সুতা, চাকার টায়ারের রজ্জু, দড়ি তৈরিতে.}
\end{itemize}

\chsub{}{বিভিন্ন ভৌত পরিমাপের প্রচলিত ও আন্তর্জাতিক {\lat (SI)} একক}

\chsub{}{{\lat SI} \B{একক সমূহ}}

\begin{itemize}
    \item \textbf{\B{আয়তন:}} \B{ঘন মিটার} {\lat (SI): m$^3$}; \B{ঘন সেন্টিমিটার লিটার} {\lat cm$^3$, L}\\
    {\lat $1\,m^3 = 10^6\,cm^3$; $1\,m^3 = 10^3\,dm^3 = 10^3\,L$; $1\,L = 10^3\,cm^3$}
    \item \textbf{\B{ঘনত্ব:}} \B{কিলোগ্রাম/ঘনমিটার} {\lat (SI): kgm$^{-3}$}; \B{গ্রাম/ঘনসেন্টিমিটার} {\lat g/cm$^3$}; \B{গ্রাম/মিলি লিটার} {\lat g/ml}\\
    {\lat $1\,g/cm^3 = 1\,g/ml = 10^3\,kg/m^3$}
    \item \textbf{\B{শক্তি} {\lat (Force):}} \B{নিউটন} {\lat (SI): N}; {\lat $1\,N = 1\,kg\,ms^{-2}$}
    \item \textbf{\B{চাপ:}} \B{প্যাসকাল} {\lat (SI): Pa}; \B{বার:} {\lat bar}; \B{বায়ুচাপ:} {\lat atm}; \B{মিমি পারদ:} {\lat mm}\\
    {\lat $1\,Pa = 1\,N/m^2$; $1\,bar = 10^5\,Pa$; $1\,atm = 101.325\,kPa = 760\,\text{mm}$}
    \item \textbf{\B{তড়িৎ বিভব:}} \B{ভোল্ট:} {\lat V}; {\lat $1\,V = 1\,W/A$}
    \item \textbf{\B{শক্তি} {\lat (Energy):}} \B{জুল:} {\lat J}; \B{তাপ-ক্যালরি:} {\lat cal}; \B{বিদ্যুৎ-ইলেকট্রন ভোল্ট:} {\lat eV}\\
    {\lat $1\,J = 1\,N.m = 1\,kg\,m^2s^{-2}$; $1\,cal = 4.184\,J$; $1\,eV = 1.6022 \times 10^{-19}\,J$}
    \item \textbf{\B{গতিবেগ:}} \B{মিটার/সেকেন্ড} {\lat (SI): ms$^{-1}$}; \B{সেন্টিমিটার/সেকেন্ড:} {\lat cms$^{-1}$}\\
    {\lat $1\,ms^{-1} = 100\,cm\,s^{-1}$}
    \item \textbf{\B{সময়:}} \B{সেকেন্ড} {\lat (SI): s}; \B{মিনিট:} {\lat min}; {\lat $1\,min = 60\,s$}
    \item \textbf{\B{তাপমাত্রা:}} \B{ডিগ্রি কেলভিন} {\lat (SI): K}; \B{ডিগ্রি সেলসিয়াস:} {\lat °C}; {\lat $K = {^\circ}C + 273$}
    \item \textbf{\B{ভর:}} \B{কিলোগ্রাম} {\lat (SI): kg}; \B{গ্রাম:} {\lat g}; {\lat $1\,kg = 10^3\,g$}
\end{itemize}

\chsub{}{মৌলিক ধ্রুবকসমূহ}

\chsub{}{প্রয়োজনীয় মৌলিক ধ্রুবক}

\begin{itemize}
    \item \textbf{\B{পারমাণবিক ভর একক} (amu):} {\lat $1.66 \times 10^{-27}$} {\lat kg}
    \item \textbf{\B{আভোগেড্রো সংখ্যা} (N):} {\lat $6.023 \times 10^{23}$} {\lat mol}$^{-1}$
    \item \textbf{\B{ফ্যারাডে ধ্রুবক} (F):} {\lat $96485 \approx 96500$} {\lat C}
    \item \textbf{\B{মৌলিক চার্জ} (e):} {\lat $1.602 \times 10^{-19}$\,C}
    \item \textbf{\B{বোল্টজম্যান ধ্রুবক} (K$_b$):} {\lat $1.38 \times 10^{-22}$\,Jk$^{-1}$}
    \item \textbf{\B{মোলার গ্যাস ধ্রুবক} (R):} {\lat \scalebox{0.85}{$8.316\,Jk^{-1}\,mol^{-1} = 1.987\,cal\,deg^{-1}\,mol^{-1}$}}
    \item \textbf{\B{ইলেকট্রনের ভর} (m$_e$):} {\lat $9.1095 \times 10^{-31}$\,kg}
    \item \textbf{\B{প্রোটনের ভর} (m$_p$):} {\lat $1.673 \times 10^{-27}$} {\lat kg}
    \item \textbf{\B{নিউট্রনের ভর} (m$_n$):} {\lat $1.675 \times 10^{-27}$} {\lat kg}
    \item \textbf{\B{প্ল্যাংকের ধ্রুবক} (h):} {\lat $6.626 \times 10^{-34}$} {\lat Js}
    \item \textbf{\B{রিডবার্গ ধ্রুবক} (Rz):} {\lat $1.097 \times 10^5$} {\lat cm}$^{-1}$
\end{itemize}



\chsub{}{গুরুত্বপূর্ণ রাসায়নিক বিক্রিয়া ও শর্ত}

\chsub{}{শিল্পোৎপাদনে ব্যবহৃত প্রভাবক}

\begin{itemize}
    \item \textbf{\B{হেবার বস পদ্ধতি (অ্যামোনিয়া):}} {\lat N$_2$ + 3H$_2$ $\rightleftharpoons$ 2NH$_3$}; \B{তাপমাত্রা:} {\lat 450--550\,°C}; \B{চাপ:} {\lat 200\,atm}; \B{প্রভাবক:} {\lat Fe + K$_2$O + Al$_2$O$_3$}
    \item \textbf{\B{স্পর্শ পদ্ধতি (সালফিউরিক এসিড):}} {\lat 2SO$_2$ + O$_2$ $\rightleftharpoons$ 2SO$_3$}; \B{তাপমাত্রা:} {\lat 400--500\,°C}; \B{চাপ:} {\lat 1.7\,atm}; \B{প্রভাবক:} {\lat V$_2$O$_5$}
    \item \textbf{\B{অস্টওয়াল্ড পদ্ধতি (নাইট্রিক এসিড):}} {\lat 4NH$_3$ + 5O$_2$ $\rightarrow$ 4NO + 6H$_2$O}; \B{তাপমাত্রা:} {\lat 850\,°C}; \B{প্রভাবক:} {\lat Pt/Rh}
    \item \textbf{\B{সোলভে পদ্ধতি (সোডিয়াম কার্বনেট):}} {\lat NaCl + NH$_3$ + CO$_2$ + H$_2$O $\rightarrow$ NaHCO$_3$ + NH$_4$Cl}
    \item \textbf{\B{ডাউন পদ্ধতি (সোডিয়াম):}} \B{গলিত} {\lat NaCl} \B{এর তড়িৎ বিশ্লেষণ}
\end{itemize}

\chsub{}{গুরুত্বপূর্ণ জৈব বিক্রিয়া}

\begin{itemize}
    \item \textbf{\B{মার্কভনিকভের নিয়ম:}} \B{হাইড্রোজেন পরমাণু সেই কার্বনে যুক্ত হয় যে কার্বনে বেশি হাইড্রোজেন আছে.}
    \item \textbf{\B{জাইতসেভের নিয়ম:}} \B{বেশি প্রতিস্থাপিত অ্যালকিন মুখ্য উৎপাদ.}
    \item \textbf{\B{উলফ-কিশনার বিজারণ:}} {\lat $>$C=O $\rightarrow$ $>$CH$_2$}; \B{প্রভাবক:} {\lat KOH, N$_2$H$_4$}
    \item \textbf{\B{ক্লেমেনসেন বিজারণ:}} {\lat $>$C=O $\rightarrow$ $>$CH$_2$}; \B{প্রভাবক: জিংক-অ্যামালগাম + গাঢ়} {\lat HCl}
    \item \textbf{\B{স্যান্ডমায়ার বিক্রিয়া:}} {\lat ArN$_2$Cl + CuCl $\rightarrow$ ArCl + N$_2$}
    \item \textbf{\B{কোলবে বিক্রিয়া:}} {\lat 2HCOONa $\xrightarrow{\Delta}$ Na$_2$CO$_3$ + H$_2$ + CO$_2$}
    \item \textbf{\B{রাইমার-টিম্যান বিক্রিয়া:}} \B{ফেনল থেকে স্যালিসিলালডিহাইড তৈরি;} {\lat CHCl$_3$/NaOH} \B{প্রভাবক}
\end{itemize}

\chsub{}{গুরুত্বপূর্ণ তথ্য}

\begin{itemize}
    \item \textbf{\B{তেজস্ক্রিয় মৌল:}} {\lat U, Th, Ra, Rn, Po, At, Fr, Ac, Pa} \B{ইত্যাদি}
    \item \textbf{\B{নোবেল গ্যাস:}} {\lat He, Ne, Ar, Kr, Xe, Rn}
    \item \textbf{\B{হ্যালোজেন:}} {\lat F, Cl, Br, I, At}
    \item \textbf{\B{অ্যালকালি ধাতু:}} {\lat Li, Na, K, Rb, Cs, Fr}
    \item \textbf{\B{অ্যালকালাইন আর্থ ধাতু:}} {\lat Be, Mg, Ca, Sr, Ba, Ra}
    \item \textbf{\B{অর্ধপরিবাহী:}} {\lat Si, Ge, As, Sb, Te}
    \item \textbf{\B{অ্যাম্ফোটেরিক অক্সাইড:}} {\lat Al$_2$O$_3$, ZnO, SnO, PbO, Cr$_2$O$_3$}
    \item \textbf{\B{সবল এসিড:}} {\lat HCl, HBr, HI, HNO$_3$, H$_2$SO$_4$, HClO$_4$}
    \item \textbf{\B{সবল ক্ষার:}} {\lat NaOH, KOH, Ca(OH)$_2$, Ba(OH)$_2$}
    \item \textbf{\B{বাফার দ্রবণ:}} \B{দুর্বল এসিড + সংযুগ ক্ষার; উদা:} {\lat CH$_3$COOH + CH$_3$COONa}
\end{itemize}

\end{document}"""


def run(cmd):
    return subprocess.run(cmd, shell=True, executable="/bin/bash").returncode


os.makedirs("fonts", exist_ok=True)
os.makedirs("logs", exist_ok=True)

font_sources = {
    "NotoSerifBengali-Regular.ttf": [
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

tex_content = tex_content.replace("\u200d", "")

with open("chemistry_fixed.tex", "w", encoding="utf-8") as fh:
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
               "chemistry_fixed.tex >logs/xelatex_pass" + str(i) + ".log 2>&1")
    passes.append(code)
    if code != 0:
        raise RuntimeError("xelatex failed; see logs/xelatex_pass" + str(i) + ".log")

print("PDF ready:", os.path.exists("chemistry_fixed.pdf"), "passes:", passes)
