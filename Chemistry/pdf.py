import subprocess
import os

tex_content = r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[margin=1.0cm, top=1.2cm, bottom=1.0cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage[protrusion=false]{microtype}
\usepackage{balance}
\usepackage{graphicx}
\pagestyle{empty}
\setlength{\emergencystretch}{25pt}
\hbadness=10000
\vbadness=10000
\sloppy
\raggedcolumns
\tolerance=9999
\emergencystretch=25pt

\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Latin Modern Roman}
\newfontfamily\lat{Latin Modern Roman}[Ligatures=TeX]
\newfontfamily\bn{Noto Serif Bengali}[Script=Bengali, BoldFont=Noto Serif Bengali Bold, ItalicFont=Noto Serif Bengali, BoldItalicFont=Noto Serif Bengali Bold, Renderer=HarfBuzz]

\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{85,85,85}

\newcommand{\B}[1]{{\bn #1}}
\newcommand{\LAT}[1]{{\lat #1}}

\newcommand{\chsec}[1]{%
  \vspace{3pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par
}

\newcommand{\chsub}[2]{%
  \vspace{3pt}%
  \noindent\colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \bfseries\footnotesize\color{white}\;#1 \B{#2}%
  }}%
  \vspace{1pt}\par
}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}

\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\setlist[itemize]{nosep, leftmargin=12pt, topsep=0pt, label={\lat\textbullet}}
\newcommand{\itm}[1]{\textbf{{\lat #1.}}\;}
\newcommand{\sub}[1]{\textbf{({\lat #1})}\;}

\begin{document}

\begin{center}
\noindent
{\bn\Large\bfseries একনজরে রসায়ন প্রথম পত্র — কনসেপ্ট ম্যাপ ও সূত্রাবলি}\hfill
{\normalfont\small \textbf{By Abir Arafat Chawdhury [Introvert's Area]}}
\vspace{3pt}
\end{center}

\begin{multicols}{2}

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{রসায়ন প্রথম পত্র}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: ল্যাবরেটরির নিরাপদ ব্যবহার}

\chsub{Concept Map: The Chapter at a Glance }{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: ল্যাবরেটরি}}

\textbf{{\lat 1.} \B{ব্যবহার বিধি} $\rightarrow$ \B{নিরাপদ পরিবেশ সৃষ্টির সোনালী বিধি:}}
\begin{itemize}
    \item \B{নিয়মানুবর্তিতা, যত্নশীলতা, অধ্যবসায়, পরিশ্রম, সুবিবেচনা, পরিচ্ছন্নতা}
    \item \B{অ্যাপ্রন, চোখে নিরাপদ চশমা, হ্যান্ড গ্লাভস, মাস্ক, পায়ে জুতা, ক্যাপ পরা, পর্যাপ্ত বায়ু চলাচলের ব্যবস্থা}
\end{itemize}

\textbf{{\lat 2.} \B{ব্যবহৃত যন্ত্রপাতি:}}
\begin{itemize}
    \item \textbf{\B{গ্লাস সামগ্রী:}} \B{টেস্টটিউব, কনিক্যাল ফ্লাস্ক, বিকার, আয়তনিক ফ্লাস্ক, মাপন সিলিন্ডার, ফানেল, ব্যুরেট, পিপেট, ওজন বোতল, ওয়াশ বোতল, গ্লাস রড, ওয়াচ গ্লাস, রি-এজেন্ট বোতল।}
    \item \textbf{\B{তাপ প্রদানকারী যন্ত্র:}} \B{স্পিরিট ল্যাম্প, বুনসেন বার্নার (অনুজ্জ্বল শিখা, উজ্জ্বল শিখা), হিটিং ম্যান্টল, পানি গাহ।}
    \item \textbf{\B{ব্যালেন্স:}} \B{ম্যানুয়াল (} $\rightarrow$ \B{টপলোড), ডিজিটাল (} $\rightarrow$ \B{অ্যানালাইটিক্যাল)।}
    \item \textbf{\B{অন্যান্য যন্ত্রপাতি:}} \B{বলয় ধারক, তারজালি, ক্ল্যাম্প, ক্রুসিবল চিমটা, শিখা বিস্তারক, স্প্যাচুলা, ফরসেপ, স্কুপলা।}
\end{itemize}

\textbf{{\lat 3.} \B{কার্যক্রমসমূহ:}}
\begin{itemize}
    \item \B{যন্ত্রপাতি ব্যবহারের কৌশল, তাপ প্রয়োগের কৌশল, যন্ত্রপাতি পরিষ্কারের কৌশল।}
\end{itemize}

\textbf{{\lat 4.} \B{দুর্ঘটনা:}}
\begin{itemize}
    \item \textbf{\B{প্রতিকার:}} \B{ল্যাবরেটরির নির্দেশ মেনে চলা; রাসায়নিক বস্তুর ক্ষতিকারণ দিক সম্পর্কে জানা; পূর্ব প্রস্তুতি নেয়া।}
    \item \textbf{\B{সতর্কতা:}} \B{রাসায়নিক দ্রব্য স্পর্শ করা, গন্ধ নেয়া, স্বাদ নেয়া যাবে না; পাত্রের নির্দিষ্ট স্প্যাচুলা ব্যবহার করা; ওয়াশ বোতলকে কেবল মাত্র পাতিত পানি দ্বারা পূর্ণ করা; মুখ দিয়ে পিপেটের মাধ্যমে তরল দ্রব্য স্থানান্তর না করা।}
    \item \textbf{\B{কারণ:}} \B{অসতর্কতা, ঝুঁকিপূর্ণ রাসায়নিক দ্রব্য, আগুন, কাঁচ, অপরিকল্পিত ল্যাবরেটরি।}
\end{itemize}

\textbf{{\lat 5.} \B{দ্রব্যাদি} $\rightarrow$ \B{বিকারক ও নির্দেশক:}}
\begin{itemize}
    \item \textbf{\B{ক্ষার:}} \B{লঘু} {\lat $\text{NaOH}$}, \B{লঘু} {\lat $\text{KOH}$}, \B{লঘু} {\lat $\text{NH}_4\text{OH}$}
    \item \textbf{\B{এসিড:}} \B{লঘু} {\lat $\text{HCl}$}, \B{লঘু} {\lat $\text{HNO}_3$}, \B{লঘু} {\lat $\text{H}_2\text{SO}_4$}, \B{লঘু} {\lat $\text{CH}_3\text{COOH}$}
    \item \textbf{\B{নির্দেশক:}} \B{লিটমাস ব্লু, লিটমাস রেড, মিথাইল অরেঞ্জ, ফেনলফথ্যালিন}
\end{itemize}

\textbf{{\lat 6.} \B{আয়ন শনাক্তকরণে ব্যবহৃত বিকারক:}}
\begin{itemize}
    \item \B{পটাসিয়াম ফেরোসায়ানাইড,} {\lat $\text{K}_4[\text{Fe}(\text{CN})_6]$}
    \item \B{পটাসিয়াম ফেরিসায়ানাইড,} {\lat $\text{K}_3[\text{Fe}(\text{CN})_6]$}
    \item \B{পটাসিয়াম পাইরোঅ্যান্টিমোনেট,} {\lat $\text{K}_2\text{H}_2\text{Sb}_2\text{O}_7$}
    \item \B{নেসলার দ্রবণ} {\lat $\text{K}_2[\text{HgI}_4] + \text{KOH}$} \B{(পটাসিয়াম টেট্রাআয়োডো মার্কিউরেট (} {\lat II} \B{))}
    \item \B{সিলভার নাইট্রেট দ্রবণ} {\lat $\text{AgNO}_3$}
    \item \B{অ্যামোনিয়াম থায়োসায়ানেট,} {\lat $\text{NH}_4\text{CNS}$}
    \item \B{অ্যামোনিয়াম অক্সালেট,} {\lat $(\text{NH}_4)_2\text{C}_2\text{O}_4$}
    \item \B{বেরিয়াম নাইট্রেট দ্রবণ} {\lat $\text{Ba}(\text{NO}_3)_2$}
\end{itemize}

\textbf{{\lat 7.} \B{পরিবেশের উপর প্রভাব:}}
\begin{itemize}
    \item \textbf{\B{ভারী ধাতু (লেড, মার্কারি, ক্রোমিয়াম প্রভৃতি):}} \B{মানব শরীরের মেটাবলিক সিস্টেমে ক্ষতিসাধন করে।}
    \item \textbf{\B{হ্যালোজেন যুক্ত জৈব যৌগ:}} \B{লিভারের ক্ষতি (জন্ডিস, সিরোসিস), কিডনির ক্ষতি করে।}
    \item \textbf{\B{উদ্বায়ী পদার্থ (লিকার অ্যামোনিয়া, গাঢ় }} {\lat HCl} \textbf{\B{ প্রভৃতি):}} \B{শ্বাসের সঙ্কট, খাদ্যনালী ও ফুসফুসের ক্ষতি করে।}
    \item \textbf{\B{বিক্রিয়ার উপজাত হিসেবে নির্গত গ্যাস (}} {\lat $\text{NO}_2, \text{SO}_2, \text{SO}_3, \text{CO}_2$} \textbf{\B{ প্রভৃতি):}} \B{বায়ু দূষণ, এসিড বৃষ্টি সৃষ্টি করে।}
\end{itemize}

\textbf{{\lat 8.} \B{অ্যানালিটিক্যাল পদ্ধতিসমূহ:}}
\begin{itemize}
    \item \textbf{\B{বিশ্লেষণ} $\rightarrow$ \B{আয়তনিক যন্ত্রপাতি:}} \B{মেজারিং সিলিন্ডার, মেজারিং ফ্লাস্ক, ব্যুরেট, পিপেট।}
    \item \textbf{\B{পদ্ধতি:}} \B{ম্যাক্রো, সেমি মাইক্রো, মাইক্রো} $\rightarrow$ \B{যৌগের পৃথকীকরণ, পরমাণুগত বিশ্লেষণ, গাঠনিক কাঠামো।}
    \item \textbf{\B{উচ্চ ক্ষমতাসম্পন্ন যন্ত্রপাতি:}} \B{ক্রোমাটোগ্রাফি:} {\lat HPLC, GPLC}; \B{স্পেক্ট্রোমেট্রিতে:} {\lat IR, UV-NMR}; \B{থার্মো অ্যানালাইসিসে:} {\lat DSC}; \B{পারমাণবিক শোষণ বর্ণালিতে:} {\lat AAS}; {\lat X}-\B{রশ্মি ব্যতিচার যন্ত্র।}
\end{itemize}

\textbf{{\lat 9.} \B{রাসায়নিক নিক্তি:}}
\begin{itemize}
    \item \textbf{\B{ডিজিটাল নিক্তি:}} {\lat 2}-\B{ডিজিট,} {\lat 4}-\B{ডিজিট।} \textbf{\B{পল বুঙ্গি:}} \B{শুষ্ক পদার্থ ওজন করা।}
    \item \textbf{\B{যন্ত্রপাতি:}} \B{সেমিমাইক্রো টেস্ট টিউব, সেন্ট্রিফিউজ টিউব, সেন্ট্রিফিউজ যন্ত্র, ড্রপিং টিউব, বিকারক ড্রপার, বিকারক বোতল, স্প্যাচুলা, দ্রবণ স্থানান্তর, পানিগাহ, বাষ্পীভবন।}
\end{itemize}

\textbf{{\lat 10.} \B{চিকিৎসা} $\rightarrow$ \B{ফার্স্ট এইড বক্স:}}
\begin{itemize}
    \item \B{অ্যাসিটামিন, অ্যাডহেসিভ ব্যান্ডেজ, অ্যাডহেসিভ টেপ ১/২'' চওড়া ২-৩ গজ, অ্যান্টিসেপটিক তোয়ালে (২/৩টি)}
    \item \B{অ্যাসপিরিন ট্যাবলেট (২ প্যাকেট), পুড়ে যাওয়া ক্ষত স্থানের জন্য} {\lat First Aid Cream}, \B{তুলা (৫০০ গ্রাম)}
    \item \B{ইলাস্টিক ব্যান্ডেজ (২'' চওড়া ৫ গজ), আই প্যাড, আই ওয়াশ, ফরসেপ, গজ ব্যান্ডেজ}
    \item \B{গজ প্যাড, রাবারের গ্লাভস, ননস্টিক প্যাড, ছোট/বড় (২/৩টি) কাঁচি, স্প্লিন্টার রিমুভার, স্যাভলন (২৫০ মিলি) ইত্যাদি}
\end{itemize}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{মোলার ঘনমাত্রা,}} {\lat $S = \dfrac{w \times 1000}{M \times V}$}
\begin{itemize}
    \item[] {\lat $S$} = \B{মোলার ঘনমাত্রা} {\lat [M]}
    \item[] {\lat $w$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{দ্রবের আণবিক বা পারমাণবিক ভর}
    \item[] {\lat $V$} = \B{দ্রবণের আয়তন} {\lat [L, mL]}
\end{itemize}

\itm{2} \textbf{\B{এসিড-ক্ষার অনুমাপণের মূলতত্ত্ব,}} {\lat $\dfrac{V_A \times S_A}{x} = \dfrac{V_B \times S_B}{y}$}
\begin{itemize}
    \item[] {\lat $V_A$} = \B{এসিডের আয়তন}, {\lat $V_B$} = \B{ক্ষারের আয়তন} {\lat [L, mL]}
    \item[] {\lat $S_A$} = \B{এসিডের শক্তিমাত্রা}, {\lat $S_B$} = \B{ক্ষারের শক্তিমাত্রা} {\lat [mol L$^{-1}$, M]}
    \item[] {\lat $x$} = \B{ক্ষারকের অম্লত্ব}, {\lat $y$} = \B{অম্লের ক্ষারকত্ব}
\end{itemize}

\itm{3} \textbf{\B{দ্রবণ লঘুকরণ,}} {\lat $V_1 S_1 = V_2 S_2$}
\begin{itemize}
    \item[] {\lat $V_1$} = \B{উচ্চতর ঘনমাত্রায় আয়তন} {\lat [L, mL]}
    \item[] {\lat $V_2$} = \B{নিম্নতর ঘনমাত্রায় কাঙ্ক্ষিত আয়তন} {\lat [L, mL]}
    \item[] {\lat $S_1$} = \B{উচ্চতর ঘনমাত্রায় মোলারিটি} {\lat [mol L$^{-1}$, M]}
    \item[] {\lat $S_2$} = \B{নিম্নতর ঘনমাত্রায় কাঙ্ক্ষিত মোলারিটি} {\lat [mol L$^{-1}$, M]}
\end{itemize}

\itm{4} \textbf{\B{রাইডার ধ্রুবক}} {\lat $= \dfrac{2 \times \text{\B{রাইডারের ভর}}}{\text{\B{বিমের দাগ সংখ্যা}}}$} {\lat [g]}
\begin{itemize}
    \item[] \textbf{{\lat Note:}} \B{বিমের সর্ববামে }{\lat 0} \B{দাগ।}
\end{itemize}

\itm{5} \textbf{\B{রাইডার ধ্রুবক}} {\lat $= \dfrac{\text{\B{রাইডারের ভর}}}{\text{\B{বিমের দাগ সংখ্যা}}}$} {\lat [g]}
\begin{itemize}
    \item[] \textbf{{\lat Note:}} \B{রাইডারের বিমের ডানে বা বামে দাগ সংখ্যা ৫০ (মাঝখানে }{\lat 0} \B{দাগ)।}
\end{itemize}


\chsec{অধ্যায়-২: গুণগত রসায়ন}

\chsub{Concept Map: The Chapter at a Glance }{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: পরমাণু}}

\textbf{{\lat 1.} \B{মূল কণিকা:}}
\begin{itemize}
    \item \textbf{\B{স্থায়ী মূল কণিকা:}} \B{ইলেকট্রন, প্রোটন, নিউট্রন।}
    \item \textbf{\B{অস্থায়ী মূল কণিকা:}} \B{নিউট্রিনো, অ্যান্টিনিউট্রিনো, পজিট্রন, মেসন।}
    \item \textbf{\B{কম্পোজিট কণা:}} \B{আলফা কণা, ডিউটেরন কণা।}
\end{itemize}

\textbf{{\lat 2.} \B{মডেল সমূহ} $\rightarrow$ \B{রাদারফোর্ডের:}}
\begin{itemize}
    \item \textbf{\B{উপকরণসমূহ:}} {\lat $\alpha$}-\B{কণার উৎস (তেজস্ক্রিয় মৌল } {\lat Ra} \B{ অথবা } {\lat U} \B{); পাতলা (} {\lat 0.0004 cm} \B{) সোনার পাত;} {\lat ZnS} \B{আবরণযুক্ত স্ক্রিন বা পর্দা।}
    \item \textbf{\B{সিদ্ধান্ত:}} \B{পরমাণুর অভ্যন্তরভাগ ফাঁকা; পরমাণুর কেন্দ্রে পরমাণুর সমস্ত ভর কেন্দ্রীভূত (পরমাণু ভরের প্রায় ৯৯.৯৭\% ভর) অতি ক্ষুদ্র স্থান দখল করে আছে; পরমাণুর কেন্দ্রকে নিউক্লিয়াস নামকরণ করেন; নিউক্লিয়াসে ধনাত্মক চার্জের পরিমাণ মৌলের পারমাণবিক সংখ্যার সমান; পরমাণুটির ব্যাস নিউক্লিয়াসের থেকে ১০ হাজার থেকে ১ লক্ষ গুণ বড়।}
    \item \textbf{\B{সীমাবদ্ধতা:}} \B{গ্রহগুলোর সাথে ইলেকট্রনগুলোর তুলনা সঠিক হয় নি; ইলেকট্রনের নিউক্লিয়াসে পতন কোনোভাবেই ঘটে না; } {\lat H}\B{-পরমাণুর বর্ণালী সম্বন্ধে কোনো সুষ্ঠু ব্যাখ্যা এ মডেলে দিতে পারে নি; কক্ষপথের আকার ও আকৃতি সম্বন্ধে কোনো ধারণা দেয়া হয় নি।}
\end{itemize}

\textbf{{\lat 3.} \B{মডেল সমূহ} $\rightarrow$ \B{বোর মডেল:}}
\begin{itemize}
    \item \textbf{\B{ভিত্তি মতবাদ:}} \B{প্ল্যাঙ্কের কোয়ান্টাম তত্ত্ব।}
    \item \textbf{\B{স্বীকার্যসমূহ:}} \B{ইলেকট্রনের স্থির কক্ষপথ বা শক্তিস্তর ধারণা; ইলেকট্রনের কৌণিক ভরবেগের ধারণা,} {\lat $mvr = \frac{nh}{2\pi}$}; \B{শক্তির শোষণ বা বিকিরণ ও বর্ণালি সৃষ্টি,} {\lat $\Delta E = (E_2 - E_1) = h\nu$}\B{।}
    \item \textbf{\B{সাফল্য:}} \B{পরমাণু মডেলের স্থায়িত্ব; বর্ণালির ব্যাখ্যা।}
    \item \textbf{\B{সীমাবদ্ধতা:}} \B{একাধিক ইলেকট্রনবিশিষ্ট পরমাণুসমূহের বর্ণালি ব্যাখ্যা করতে পারে না; সূক্ষ্ম রেখার উপস্থিতির কারণ ব্যাখ্যা করতে পারে না; প্রকৃত ত্রিমাত্রিক কাঠামোর কোনো ধারণা পাওয়া যায় না; হাইজেনবার্গের অনিশ্চয়তা নীতিকে মানা করে না।}
\end{itemize}

\textbf{{\lat 4.} \B{কোয়ান্টাম বলবিদ্যা} $\rightarrow$ \B{ভিত্তি মতবাদ:}}
\begin{itemize}
    \item \textbf{\B{নীলস বোর (১৯১৩ খ্রি.):}} \B{শক্তিস্তর।}
    \item \textbf{\B{ডি-ব্রগলি (১৯২৪ খ্রি.):}} \B{তরঙ্গ ধর্ম, দ্বৈত ধর্ম।}
    \item \textbf{\B{শ্রোডিঞ্জার (১৯২৬ খ্রি.):}} \B{তরঙ্গ সমীকরণ।}
    \item \textbf{\B{হাইজেনবার্গ (১৯২৭ খ্রি.):}} \B{অনিশ্চয়তা নীতি।}
\end{itemize}

\textbf{{\lat 5.} \B{কোয়ান্টাম সংখ্যা:}}
\begin{itemize}
    \item \B{প্রধান কোয়ান্টাম সংখ্যা (} {\lat $n$} \B{)}
    \item \B{সহকারী/অ্যাজিমুথাল কোয়ান্টাম সংখ্যা (} {\lat $l$} \B{)}
    \item \B{চৌম্বকীয় কোয়ান্টাম সংখ্যা (} {\lat $m$} \B{)}
    \item \B{ঘূর্ণন কোয়ান্টাম সংখ্যা (} {\lat $s$} \B{)}
\end{itemize}

\textbf{{\lat 6.} \B{উপশক্তিস্তর:}}
\begin{itemize}
    \item {\lat s}-\B{অরবিটাল,} {\lat p}-\B{অরবিটাল,} {\lat d}-\B{অরবিটাল,} {\lat f}-\B{অরবিটাল,} {\lat g}-\B{অরবিটাল।}
\end{itemize}

\textbf{{\lat 7.} \B{ইলেকট্রন বিন্যাস:}}
\begin{itemize}
    \item \textbf{\B{নিয়ম:}} \B{আউফবাউ নীতি, হুন্ডের নীতি, পলির বর্জন নীতি।}
    \item \textbf{\B{প্রয়োগ:}} \B{মৌলের যোজ্যতা নির্ণয় করা যায়; পর্যায় সারণিতে মৌলের অবস্থান নির্ণয় করা যায়; মৌলের সক্রিয়তা নির্ণয় করা যায়।}
\end{itemize}

\textbf{{\lat 8.} \B{তড়িৎ চুম্বকীয় বর্ণালি} $\rightarrow$ \B{অঞ্চলসমূহ:}}
\begin{itemize}
    \item \B{গামা (} {\lat $\gamma$} \B{) রশ্মি অঞ্চল, রঞ্জন রশ্মি (} {\lat X-ray} \B{) অঞ্চল}
    \item \B{অতিবেগুনি রশ্মি (} {\lat UV} \B{) অঞ্চল: লাইম্যান সিরিজ}
    \item \B{দৃশ্যমান (} {\lat Visible} \B{) অঞ্চল: বামার সিরিজ}
    \item \B{অবলোহিত (} {\lat IR} \B{) অঞ্চল: প্যাশ্চেন সিরিজ, ব্র্যাকেট সিরিজ, ফুন্ড সিরিজ}
    \item \B{মাইক্রোওয়েভস (} {\lat Micro waves} \B{) অঞ্চল}
    \item \B{রেডিও ওয়েভস (} {\lat Radio waves} \B{) অঞ্চল}
\end{itemize}

\textbf{{\lat 9.} \B{তড়িৎ চুম্বকীয় বর্ণালি} $\rightarrow$ \B{ব্যবহার:}}
\begin{itemize}
    \item \B{আলো বিচ্ছুরণ বর্ণালি, আলো শোষণ বর্ণালি}
    \item \textbf{{\lat UV} \B{রশ্মি}} \B{— জাল নোট শনাক্তকরণ}
    \item \textbf{{\lat IR} \B{রশ্মি}} \B{— চিকিৎসাক্ষেত্রে রোগ শনাক্তকরণ}
    \item \B{দেহের অভ্যন্তরীণ কাঠামোর চিত্রায়নের জন্য} {\lat MRI} \B{পরীক্ষা}
\end{itemize}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{ভরত্রুটি,}} {\lat $\Delta m = \{Z m_p + Q m_n\} - M$}
\begin{itemize}
    \item[] {\lat $\Delta m$} = \B{ভরত্রুটি} {\lat [amu, kg]}
    \item[] {\lat $Z$} = \B{প্রোটন সংখ্যা}
    \item[] {\lat $m_p$} = \B{প্রোটনের ভর} {\lat [amu, kg]}
    \item[] {\lat $A$} = \B{ভরসংখ্যা}
    \item[] {\lat $m_n$} = \B{নিউট্রনের ভর} {\lat [amu, kg]}
    \item[] {\lat $M$} = \B{আপেক্ষিক পারমাণবিক ভর} {\lat [g]}
\end{itemize}

\itm{2} \textbf{\B{নিউট্রন সংখ্যা,}} {\lat $Q = (A - Z)$}
\begin{itemize}
    \item[] {\lat $Z$} = \B{প্রোটন সংখ্যা}, {\lat $A$} = \B{ভরসংখ্যা}, {\lat $Q$} = \B{নিউট্রন সংখ্যা}
\end{itemize}

\itm{3} \textbf{\B{মৌলের আপেক্ষিক পারমাণবিক ভর}}\\[1pt]
\scalebox{0.78}{$\displaystyle = \dfrac{\text{\B{মৌলের ১টি পরমাণুর ভর}}}{\dfrac{1}{12} \times \text{\B{কার্বন-12 এর একটি পরমাণুর ভর}}}$}

\itm{4} \textbf{\B{মৌলের পারমাণবিক ভর}} {\lat $= \dfrac{\sum_{n=1}^{n} p_n \times m_n}{100}$}
\begin{itemize}
    \item[] {\lat $p$} = \B{তম আইসোটোপের ভর সংখ্যা}
    \item[] {\lat $m$} = \B{তম আইসোটোপের শতকরা পরিমাণ}
\end{itemize}

\itm{5} \textbf{\B{প্ল্যাঙ্কের কোয়ান্টাম সূত্র,}} {\lat $\Delta E = h\nu = \dfrac{hc}{\lambda}$}
\begin{itemize}
    \item[] {\lat $h$} = \B{প্ল্যাঙ্কের ধ্রুবক} {\lat $= 6.626 \times 10^{-34}$ Js [J.s]}
    \item[] {\lat $\Delta E$} = \B{বিকিরিত বা শোষিত শক্তি} {\lat [J]}
    \item[] {\lat $\nu$} = \B{কম্পাঙ্ক} {\lat [cycles/sec, Hz]}
    \item[] {\lat $\lambda$} = \B{তরঙ্গ দৈর্ঘ্য} {\lat [$\mu$m, nm, \AA]}
    \item[] {\lat $c$} = \B{আলোর বেগ} {\lat [cm sec$^{-1}$, ms$^{-1}$]}
\end{itemize}

\itm{6} \textbf{\B{রিডবার্গ সমীকরণ,}} {\lat $\bar{\nu} = R_H \left[\dfrac{1}{n_1^2} - \dfrac{1}{n_2^2}\right]$}
\begin{itemize}
    \item[] {\lat $R_H$} = \B{রিডবার্গ ধ্রুবক} {\lat $= 109678$ cm$^{-1}$ [cm$^{-1}$]}
    \item[] {\lat $n_1 = 1, 2, 3, 4, 5, 6;$} {\lat $n_2 = 2, 3, 4, 5, 6,\ldots$} \B{ইত্যাদি}
    \item[] {\lat $\bar{\nu}$} = \B{ফ্রিকুয়েন্সি} {\lat [Hz]}
\end{itemize}

\itm{7} \textbf{\B{কৌণিক ভরবেগ,}} {\lat $mvr = \dfrac{nh}{2\pi}$}
\begin{itemize}
    \item[] {\lat $n$} = \B{কক্ষপথ নাম্বার}
    \item[] {\lat $m$} = \B{বস্তুর ভর} {\lat [g, kg]}
    \item[] {\lat $v$} = \B{ইলেকট্রনের গতিবেগ} {\lat [cm sec$^{-1}$, ms$^{-1}$]}
    \item[] {\lat $r$} = \B{কক্ষপথের ব্যাসার্ধ} {\lat [cm, m]}
\end{itemize}

\itm{8} \textbf{\B{ডি-ব্রগলির সমীকরণ,}} {\lat $\lambda = \dfrac{h}{mv} = \dfrac{h}{p}$}
\begin{itemize}
    \item[] {\lat $h$} = \B{প্ল্যাঙ্কের ধ্রুবক} {\lat $= 6.626 \times 10^{-34}$ Js [ergs, Js]}
    \item[] {\lat $m$} = \B{ইলেকট্রনের ভর} {\lat $= 9.11 \times 10^{-31}$ kg [g, kg]}
    \item[] {\lat $v$} = \B{ইলেকট্রনের বেগ} {\lat [cm sec$^{-1}$, ms$^{-1}$]}
\end{itemize}

\itm{9} \textbf{\B{কক্ষপথের ব্যাসার্ধ,}} {\lat $r_n = \dfrac{n^2 h^2}{4\pi^2 Z e^2 m}$}
\begin{itemize}
    \item[] {\lat $r_n$} = {\lat $n$} \B{তম কক্ষপথের ব্যাসার্ধ} {\lat [cm]}
    \item[] {\lat $Z$} = \B{পারমাণবিক সংখ্যা}
    \item[] {\lat $n$} = \B{কক্ষপথ নাম্বার}
    \item[] {\lat $e$} = \B{ইলেকট্রনের আধান} {\lat [esu]}
    \item[] {\lat $m$} = \B{ইলেকট্রন ভর} {\lat [g]}
\end{itemize}

\itm{10} \textbf{{\lat CGS} \B{এককে} {\lat H} \B{পরমাণুর কক্ষপথের ব্যাসার্ধ,}}
{\lat $r_n = \dfrac{n^2 h^2}{4\pi^2 m e^2}$; $r_n = \dfrac{n^2}{Z} \times r_1$}\\
\B{[} {\lat $r_1$} \B{ কে বোর ব্যাসার্ধ (} {\lat $a_0$} \B{) হিসেবেও প্রকাশ করা হয়]}
\begin{itemize}
    \item[] {\lat $e$} = \B{ইলেকট্রনের আধান} {\lat [esu]}
    \item[] {\lat $n$} = \B{কক্ষপথের নাম্বার}
    \item[] {\lat $m$} = \B{ইলেকট্রনের ভর} {\lat [g]}
    \item[] {\lat $h$} = \B{প্ল্যাঙ্কের ধ্রুবক} {\lat [ergs]}
    \item[] {\lat $r_1 = 0.5292 \times 10^{-8}$ cm}
\end{itemize}

\itm{11} \textbf{{\lat CGS} \B{এককে} {\lat n}\B{-তম কক্ষপথের ইলেকট্রনের গতিবেগ,}}
{\lat $V_n = \dfrac{2\pi Z e^2}{nh}$; $v_n = \dfrac{v_1 \times Z}{n}$}
\begin{itemize}
    \item[] {\lat $Z$} = \B{মৌলের পারমাণবিক সংখ্যা}
    \item[] {\lat $e$} = \B{ইলেকট্রন চার্জ} {\lat [e.s.u]}
    \item[] {\lat $n$} = \B{কক্ষপথের নাম্বার}
    \item[] {\lat $h = 6.626 \times 10^{-27}$ erg.s}
    \item[] {\lat $v_1 = 2.1837 \times 10^{8}$ cm s$^{-1}$}
\end{itemize}

\itm{12} {\lat $2\pi r = n\lambda$} \B{[একটি ইলেকট্রন যততম কক্ষপথে অবস্থান করে সেখানে ততগুলো পূর্ণস্পন্দন বা তরঙ্গ সৃষ্টি হবে]}
\begin{itemize}
    \item[] {\lat $n$} = \B{প্রধান শক্তিস্তর} \B{[অখণ্ড পূর্ণসংখ্যা]}
    \item[] {\lat $r$} = \B{কক্ষপথের ব্যাসার্ধ} {\lat [m, cm, nm]}
    \item[] {\lat $\lambda$} = \B{তরঙ্গ দৈর্ঘ্য} {\lat [m, cm, nm]}
\end{itemize}

\itm{13} \textbf{\B{আবর্তন সংখ্যা}} {\lat $= \dfrac{\text{\B{ইলেকট্রনের গতিবেগ}}}{\text{\B{কক্ষপথের পরিধি}}}$}

\itm{14} \textbf{{\lat CGS} \B{এককে} {\lat n}\B{-তম কক্ষপথের ইলেকট্রনের মোট শক্তি,}}
{\lat $E_n = -\dfrac{2\pi^2 m Z^2 e^4}{n^2 h^2}$; $E_n = -\dfrac{Z^2}{n^2} \times E_1$}
\begin{itemize}
    \item[] {\lat $m$} = \B{ইলেকট্রন ভর} {\lat [g]}
    \item[] {\lat $Z$} = \B{মৌলের পারমাণবিক সংখ্যা}
    \item[] {\lat $e$} = \B{ইলেকট্রন চার্জ} {\lat [e.s.u]}
    \item[] {\lat $n$} = \B{কক্ষপথের নাম্বার}
    \item[] {\lat $h = 6.626 \times 10^{-27}$ erg.s}
    \item[] {\lat $E_1 = 2.18 \times 10^{-18}$ J}
\end{itemize}

\itm{15} \textbf{\B{শ্রোডিঞ্জারের তরঙ্গ সমীকরণ,}}
{\lat $\dfrac{\delta^2 \psi}{\delta x^2} + \dfrac{\delta^2 \psi}{\delta y^2} + \dfrac{\delta^2 \psi}{\delta z^2} + \dfrac{8\pi^2 m}{h^2}(E - V)\psi = 0$}
\begin{itemize}
    \item[] {\lat $m$} = \B{ইলেকট্রন ভর} {\lat [kg]}
    \item[] {\lat $h = 6.626 \times 10^{-34}$ J.s}
    \item[] {\lat $E$} = \B{মোট শক্তির মান} {\lat [J]}
    \item[] {\lat $V$} = \B{স্থিতিশক্তির মান} {\lat [J]}
    \item[] {\lat $\psi$} = \B{ইলেকট্রনের তরঙ্গ ফাংশন}
\end{itemize}

\itm{16} \textbf{\B{হাইজেনবার্গের অনিশ্চয়তা নীতি,}}
{\lat $\Delta x \cdot \Delta p \geq \dfrac{h}{4\pi}$; $\Delta p = m\Delta v$}
\begin{itemize}
    \item[] {\lat $\Delta x$} = \B{অবস্থানের অনিশ্চয়তা} {\lat [m, cm, pm]}
    \item[] {\lat $\Delta p$} = \B{ভরবেগের অনিশ্চয়তা} {\lat [kgms$^{-1}$, gcms$^{-1}$]}
    \item[] {\lat $h$} = \B{প্ল্যাঙ্কের ধ্রুবক} {\lat [Js, ergs]}
    \item[] {\lat $\Delta v$} = \B{বেগের অনিশ্চয়তা} {\lat [ms$^{-1}$, cms$^{-1}$]}
\end{itemize}

\itm{17} \textbf{\B{তরঙ্গবেগ,}} {\lat $c = \lambda \nu$}
\begin{itemize}
    \item[] {\lat $\nu$} = \B{কম্পাঙ্ক} {\lat [Hz]}
    \item[] {\lat $\lambda$} = \B{তরঙ্গদৈর্ঘ্য} {\lat [m]}
\end{itemize}

\itm{18} \textbf{\B{তরঙ্গসংখ্যা,}} {\lat $\bar{\nu} = \dfrac{1}{\lambda}$} [{\lat $\lambda$} = \B{তরঙ্গদৈর্ঘ্য,} {\lat m}]

\itm{19} \textbf{\B{দ্রাব্যতা,}} {\lat $S = \dfrac{100 m}{M - m}$}
\begin{itemize}
    \item[] {\lat $m$} = \B{দ্রবের ভর} {\lat [g, kg]}
    \item[] {\lat $M$} = \B{দ্রবণের ভর} {\lat [g, kg]}
    \item[] {\lat $M - m$} = \B{দ্রাবকের ভর} {\lat [g, kg]}
\end{itemize}

\itm{20} \textbf{\B{স্বল্পদ্রাব্য লবণের দ্রাব্যতা গুণফল:}}\\
{\lat $A_m B_n (s) \rightleftharpoons mA^{n+}(aq) + nB^{m-}(aq)$}\\
\B{ধরি,} {\lat $A_m B_n$} \B{স্বল্পদ্রাব্য লবণের দ্রাব্যতা} {\lat $S$}\B{।} {\lat $S$} \B{এর একক} {\lat $gL^{-1}$}, {\lat $mol L^{-1}$}\B{।}\\
\textbf{\B{দ্রাব্যতা গুণফল,}} {\lat $K_{SP} = [A^{n+}]^m \times [B^{m-}]^n = m^m n^n (S)^{m+n}$}



\itm{21} \textbf{\B{বোহর মডেলে ইলেকট্রনের শক্তি:}}\\[2pt]
{\lat $E_n = -\dfrac{2\pi^2 m e^4 Z^2}{n^2 h^2} = -13.6\dfrac{Z^2}{n^2}$} {\lat (eV} \B{তে)}
\begin{itemize}
    \item[] {\lat $Z$} = \B{পারমাণবিক সংখ্যা}; {\lat $n$} = \B{কক্ষপথ নম্বর}
    \item[] \B{একক: {\lat eV} (ইলেকট্রন ভোল্ট)}; {\lat $1\,eV = 1.6 \times 10^{-19}\,J$}
\end{itemize}

\itm{22} \textbf{\B{কক্ষপথের শক্তি পার্থক্য:}}\\[2pt]
{\lat $\Delta E = E_{n_2} - E_{n_1} = 13.6\,Z^2\left(\dfrac{1}{n_1^2} - \dfrac{1}{n_2^2}\right)$} {\lat eV}

\itm{23} \textbf{\B{সর্বাধিক ইলেকট্রন ধারণ ক্ষমতা:}} {\lat $= 2n^2$}\\[2pt]
\textbf{\B{উপশক্তিস্তরে:}} {\lat s=2, p=6, d=10, f=14}

\itm{24} \textbf{\B{কোয়ান্টাম সংখ্যা:}}
\begin{itemize}
    \item \textbf{\B{প্রধান কোয়ান্টাম সংখ্যা} (n):} {\lat $n = 1, 2, 3, \dots$}
    \item \textbf{\B{দিগংশীয়} (l):} {\lat $l = 0, 1, 2, \dots, (n-1)$}
    \item \textbf{\B{চৌম্বক} ($m_l$):} {\lat $m_l = -l, \dots, 0, \dots, +l$}
    \item \textbf{\B{স্পিন} ($m_s$):} {\lat $m_s = +\dfrac{1}{2}$} \B{বা} {\lat $-\dfrac{1}{2}$}
\end{itemize}

\itm{25} \textbf{\B{পলির বর্জন নীতি:}} \B{একই পরমাণুতে দুটি ইলেকট্রনের চারটি কোয়ান্টাম সংখ্যা অভিন্ন হতে পারে না।}

\itm{26} \textbf{\B{হুন্ডের নিয়ম:}} \B{সমশক্তির অরবিটালে ইলেকট্রন একে একে সর্বোচ্চ স্পিন বজায় রেখে প্রবেশ করে।}

\itm{27} \textbf{\B{আউফবাউ নীতি:}} \B{ইলেকট্রন সর্বনিম্ন শক্তির অরবিটালে আগে প্রবেশ করে।}\\[2pt]
\B{ক্রম:} {\lat $1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d \dots$}

\itm{28} \textbf{\B{তেজস্ক্রিয় ক্ষয়ের সূত্র:}} {\lat $N = N_0 e^{-\lambda t}$}
\begin{itemize}
    \item[] {\lat $N_0$} = \B{আদি পরমাণু সংখ্যা}; {\lat $N$} = {\lat $t$} \B{সময়ে পরমাণু সংখ্যা}
    \item[] {\lat $\lambda$} = \B{ক্ষয় ধ্রুবক}; {\lat $t_{1/2} = \dfrac{0.693}{\lambda}$}
\end{itemize}

\chsec{অধ্যায়-৩: মৌলের পর্যায়বৃত্ত ধর্ম ও রাসায়নিক বন্ধন}

\chsub{Concept Map: The Chapter at a Glance }{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: ইলেকট্রন বিন্যাস}}

\textbf{{\lat 1.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat s}\B{-ব্লক (মৌল সমূহ: ১৪টি):}}
\begin{itemize}
    \item {\lat H, Li, Na, K, Rb, Cs, Fr, He, Be, Mg, Ca, Sr, Ba, Ra}
    \item \textbf{\B{ধর্মাবলী:}} \B{ক্ষার ধাতুগুলোর জারণ সংখ্যা +১ (} {\lat Na$^+$, K$^+$} \B{); এদের আকার ও আয়নিক বিভবের মান খুবই কম; ক্ষার ধাতুগুলো তীব্র তড়িৎ ধনাত্মক মৌল;} {\lat Na, K} \B{পানির সংস্পর্শে এলেই আগুন ধরে; এরা অত্যন্ত সক্রিয়; এরা নরম ও নমনীয় ধাতু; এরা আয়নিক যৌগ গঠন করে; এরা তীব্র বিজারকরূপে ক্রিয়া করে।}
\end{itemize}

\textbf{{\lat 2.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat p}\B{-ব্লক (মৌল সমূহ: ৩৬টি):}}
\begin{itemize}
    \item \textbf{\B{ধর্মাবলী:}} \B{তড়িৎ ঋণাত্মক ধাতু; মৌলসমূহের পারমাণবিক আকার হ্রাস; পর্যায়ে বাম থেকে ডানদিকে } {\lat p}\B{-ব্লকের মৌলসমূহের বিজারণ ক্ষমতা ক্রমশ হ্রাস পায়; পর্যায়ে বাম থেকে ডানদিকে } {\lat p}\B{-ব্লকের মৌলসমূহের জারণ ক্ষমতা ক্রমশ বৃদ্ধি পায়; একই গ্রুপের উপর থেকে নিচের দিকে মৌলসমূহের জারণ ক্ষমতা হ্রাস পায়; বিজারণ ক্ষমতা বৃদ্ধি পায়; আয়নিক যৌগ সৃষ্টি করে; পরিবর্তনশীল জারণ অবস্থা।}
\end{itemize}

\textbf{{\lat 3.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat d}\B{-ব্লক (মৌল সমূহ: ৪১টি):}}
\begin{itemize}
    \item \textbf{\B{ধর্মাবলী:}} \B{ভারী ধাতু; উচ্চ গলনাঙ্ক ও উচ্চ স্ফুটনাঙ্কবিশিষ্ট; কঠিন ও শক্ত; } {\lat Hg} \B{ তরল; তাপ ও বিদ্যুৎ সুপরিবাহী; প্যারাম্যাগনেটিক অর্থাৎ চুম্বকক্ষেত্র দ্বারা আকৃষ্ট হয়; সংকর ধাতু তৈরি করে।}
    \item \textbf{\B{ব্যতিক্রম:}} {\lat $\text{Sc}^{3+}, \text{Ti}^{4+}, \text{Cu}^+$}\B{।}
    \item \textbf{\B{শ্রেণিবিন্যাস:}} {\lat 3d}-\B{ব্লক মৌল,} {\lat 4d}-\B{ব্লক মৌল,} {\lat 5d}-\B{ব্লক মৌল,} {\lat 6d}-\B{ব্লক মৌল।}
    \item \textbf{\B{রাসায়নিক ধর্ম:}} \B{পরিবর্তনশীল জারণ অবস্থা; রঙিন আয়ন বা রঙিন যৌগ গঠন; জটিল আয়ন বা যৌগ গঠন।}
\end{itemize}

\textbf{{\lat 4.} \B{মৌলের শ্রেণিবিভাগ} $\rightarrow$ {\lat f}\B{-ব্লক:}}
\begin{itemize}
    \item \textbf{\B{ল্যান্থানাইড সিরিজ ধর্মাবলী:}} \B{ভারী ধাতু; তাপ ও বিদ্যুৎ সুপরিবাহী; ঘনত্ব, গলনাঙ্ক ও স্ফুটনাঙ্ক বেশি; আয়ন বর্ণযুক্ত; অধিকতর স্থায়ী জারণ অবস্থা হলো +৩; ল্যান্থানাইড সংকোচন।}
    \item \textbf{\B{অ্যাকটিনাইড সিরিজ ধর্মাবলী:}} \B{তেজস্ক্রিয় মৌল; ঘনত্ব খুব বেশি; উচ্চ গলনাঙ্ক ও স্ফুটনাঙ্ক; অধিক তড়িৎ ধনাত্মক ধাতু।}
\end{itemize}

\textbf{{\lat 5.} \B{মৌলের পর্যায়বৃত্ত ধর্ম:}}
\begin{itemize}
    \item \B{পারমাণবিক ব্যাসার্ধ — বাম থেকে ডান দিকে হ্রাস; ওপর থেকে নিচের দিকে বৃদ্ধি।}
    \item \B{ধাতব ধর্ম — বাম থেকে ডান দিকে হ্রাস; ওপর থেকে নিচের দিকে বৃদ্ধি।}
    \item \B{অধাতব ধর্ম — বাম থেকে ডান দিকে বৃদ্ধি; ওপর থেকে নিচের দিকে হ্রাস।}
    \item \B{জারণ ক্ষমতা — বাম থেকে ডান দিকে বৃদ্ধি; ওপর থেকে নিচের দিকে হ্রাস।}
    \item \B{বিজারণ ক্ষমতা — বাম থেকে ডান দিকে হ্রাস; ওপর থেকে নিচের দিকে বৃদ্ধি।}
    \item \B{আয়নিকরণ শক্তি — বাম থেকে ডান দিকে বৃদ্ধি; ওপর থেকে নিচের দিকে হ্রাস।}
    \item \B{ইলেকট্রন আসক্তি — বাম থেকে ডান দিকে বৃদ্ধি; ওপর থেকে নিচের দিকে হ্রাস।}
    \item \B{তড়িৎ ঋণাত্মকতা — বাম থেকে ডান দিকে বৃদ্ধি; ওপর থেকে নিচের দিকে হ্রাস।}
\end{itemize}

\textbf{{\lat 6.} \B{রাসায়নিক বন্ধন:}}
\begin{itemize}
    \item \textbf{\B{প্রকার:}} \B{আয়নিক বন্ধন, সমযোজী বন্ধন, সন্নিবেশ সমযোজী বন্ধন, } {\lat H} \B{ বন্ধন।}
    \item \textbf{\B{বৈশিষ্ট্য (আয়নিক):}} \B{পোলার; কেলাসিত বা দানাদার; গলনাঙ্ক বা স্ফুটনাঙ্ক উচ্চ; পোলার দ্রাবকে দ্রবণীয়; তড়িৎ পরিবাহী।}
    \item \textbf{\B{সমযোজী প্রকার:}} \B{একক বন্ধন, দ্বি-বন্ধন, ত্রি-বন্ধন; সিগমা বন্ধন (} {\lat $\sigma$} \B{ বন্ধন); পাই বন্ধন (} {\lat $\pi$} \B{-বন্ধন)।}
    \item \textbf{\B{মতবাদ:}} \B{যোজনী বন্ধন মতবাদ; আণবিক অরবিটাল মতবাদ।}
    \item \textbf{\B{সংকর অরবিটাল:}} {\lat $SP^3$, $SP^2$, $SP$}
\end{itemize}

\textbf{{\lat 7.} \B{পোলারায়ন} $\rightarrow$ \B{ফাজানের নিয়ম:}}
\begin{itemize}
    \item \B{ক্যাটায়নের ও অ্যানায়নের চার্জের পরিমাণ যত বেশি হয়}
    \item \B{ক্যাটায়নের আকার যত ছোট হয় এবং অ্যানায়নের আকার যত বড় হয়}
    \item {\lat $ns^2 np^6$} \B{এর তুলনায় অ্যানায়নের বিকৃতি বা পোলারায়ন বেশি মাত্রায় ঘটে}
\end{itemize}

\textbf{{\lat 8.} \B{ভ্যানডার ওয়ালস বল} $\rightarrow$ \B{শ্রেণিবিভাগ:}}
\begin{itemize}
    \item \B{স্থায়ী ডাইপোল ও আবিষ্ট ডাইপোল আকর্ষণ}
    \item \B{বিস্তারণ বল বা লন্ডন বল}
\end{itemize}

\textbf{{\lat 9.} \B{নন-বন্ডিং বল:}}
\begin{itemize}
    \item \B{আয়ন ডাইপোল আকর্ষণ; হাইড্রোজেন বন্ধন; ডাইপোল আকর্ষণ}
    \item \B{আয়ন-আবিষ্ট ডাইপোল আকর্ষণ; ডাইপোল-আবিষ্ট ডাইপোল আকর্ষণ; লন্ডন বল বা বিস্তারণ}
\end{itemize}


\chsub{}{সংকরায়ন সূত্র ও আকৃতি}

\itm{1} \textbf{\B{সংকরায়ন সংখ্যা নির্ণয়ের সূত্র,}} {\lat $H = \dfrac{1}{2}[V + M - C + A]$}
\begin{itemize}
    \item[] {\lat $H$} = \B{সংকরায়ন সংখ্যা}
    \item[] {\lat $V$} = \B{কেন্দ্রীয় পরমাণুর যোজ্যতা ইলেকট্রন সংখ্যা}
    \item[] {\lat $M$} = \B{কেন্দ্রীয় পরমাণুর সাথে যুক্ত একযোজী পরমাণুর সংখ্যা}
    \item[] {\lat $C$} = \B{কেন্দ্রীয় পরমাণুর ধনাত্মক আধান (ক্যাটায়নের ক্ষেত্রে বিয়োগ করতে হয়)}
    \item[] {\lat $A$} = \B{কেন্দ্রীয় পরমাণুর ঋণাত্মক আধান (অ্যানায়নের ক্ষেত্রে যোগ করতে হয়)}
\end{itemize}

\B{প্রত্যেক মুক্তজোড় ইলেকট্রন যুগলের জন্য বন্ধন কোণ {\lat 2--2.5}$^{\circ}$ হ্রাস পায়।}

\itm{2} \textbf{\B{সংকরায়নের প্রকারভেদ, আকৃতি ও বন্ধন কোণ:}}
\begin{itemize}
    \item \textbf{{\lat sp}} \B{সংকরায়ন — রৈখিক ({\lat Linear}); বন্ধন কোণ {\lat 180}$^{\circ}$; উদাহরণ:} {\lat BeCl$_2$, C$_2$H$_2$, CO$_2$}
    \item \textbf{{\lat sp$^2$}} \B{সংকরায়ন — সমতলীয় ত্রিভুজাকার ({\lat Trigonal Planar}); বন্ধন কোণ {\lat 120}$^{\circ}$; উদাহরণ:} {\lat BF$_3$, C$_2$H$_4$, SO$_3$}
    \item \textbf{{\lat sp$^3$}} \B{সংকরায়ন — চতুস্তলকীয় ({\lat Tetrahedral}); বন্ধন কোণ {\lat 109.5}$^{\circ}$; উদাহরণ:} {\lat CH$_4$, CCl$_4$, NH$_3$, H$_2$O}
    \item \textbf{{\lat sp$^2$d / dsp$^2$}} \B{সংকরায়ন — বর্গাকার সমতলীয় ({\lat Square Planar}); বন্ধন কোণ {\lat 90}$^{\circ}$; উদাহরণ:} {\lat [Ni(CN)$_4$]$^{2-}$, [PtCl$_4$]$^{2-}$}
    \item \textbf{{\lat sp$^3$d}} \B{সংকরায়ন — ত্রিকোণীয় দ্বিপিরামিডাল ({\lat Trigonal Bipyramidal}); বন্ধন কোণ {\lat 90}$^{\circ}$/{\lat 120}$^{\circ}$; উদাহরণ:} {\lat PCl$_5$, PF$_5$}
    \item \textbf{{\lat sp$^3$d$^2$}} \B{সংকরায়ন — অষ্টতলকীয় ({\lat Octahedral}); বন্ধন কোণ {\lat 90}$^{\circ}$; উদাহরণ:} {\lat SF$_6$, PCl$_6^-$, [Co(NH$_3$)$_6$]$^{3+}$}
    \item \textbf{{\lat sp$^3$d$^3$}} \B{সংকরায়ন — পঞ্চকোণীয় দ্বিপিরামিডাল ({\lat Pentagonal Bipyramidal}); বন্ধন কোণ {\lat 72}$^{\circ}$/{\lat 90}$^{\circ}$; উদাহরণ:} {\lat IF$_7$, XeF$_6$}
    \item \textbf{{\lat d$^2$sp$^3$}} \B{সংকরায়ন — অষ্টতলকীয় ({\lat Octahedral}); বন্ধন কোণ {\lat 90}$^{\circ}$ (অন্তর্বর্তী {\lat d}-অরবিটাল ব্যবহার); উদাহরণ:} {\lat [Fe(CN)$_6$]$^{3-}$, [Co(NH$_3$)$_6$]$^{3+}$}
\end{itemize}

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

\itm{5} \textbf{\B{১ম ক্রম বিক্রিয়ার হার ধ্রুবক,}} {\lat $k_1 = \dfrac{1}{t} \ln \dfrac{a}{a - x}$}
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
    \item[] {\lat $A$} = \B{অ্যারহেনিয়াস ফ্যাক্টর}
    \item[] {\lat $E_a$} = \B{বিক্রিয়কের সক্রিয়ণ শক্তি} {\lat [kJ mol$^{-1}$]}
    \item[] {\lat $R$} = \B{সার্বজনীন গ্যাস ধ্রুবক} {\lat [JK$^{-1}$mol$^{-1}$]}
    \item[] {\lat $T$} = \B{কেলভিন তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{10} {\lat $\log k = \log A - \dfrac{E_a}{2.303 R T}$}

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
    \item[] \B{নোট: তৃতীয় বন্ধনী {\lat [ ]} দ্বারা সাম্যাবস্থায় বিক্রিয়ক ও উৎপাদের মোলার ঘনমাত্রা বোঝায়।}
    \item[] {\lat $[A], [B]$} = \B{বিক্রিয়কের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $[C], [D]$} = \B{উৎপাদের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $a, b$} = \B{বিক্রিয়কের মোল সংখ্যা (সূচক)}; {\lat $c, d$} = \B{উৎপাদের মোল সংখ্যা (সূচক)}
\end{itemize}

\vspace{2pt}
\textbf{\B{আংশিক চাপ প্রকাশক সাম্যধ্রুবক ($K_p$):}}\\[1pt]
{\lat $K_p = \dfrac{\text{\B{উৎপাদসমূহের সাম্যাবস্থার আংশিক চাপের গুণফল}}}{\text{\B{বিক্রিয়কসমূহের সাম্যাবস্থার আংশিক চাপের গুণফল}}}$}\\[4pt]
{\lat $K_p = \dfrac{(P_C)^c\,(P_D)^d}{(P_A)^a\,(P_B)^b}$}
\begin{itemize}
    \item[] \B{নোট: {\lat $P$} দ্বারা সাম্যাবস্থায় প্রতিটি গ্যাসের নিজস্ব আংশিক চাপ বোঝায়।}
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

\itm{16} {\lat $\alpha = \dfrac{x}{n}$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}
    \item[] {\lat $x$} = \B{বিয়োজিত মোল সংখ্যা} {\lat [mol]}
    \item[] {\lat $n$} = \B{প্রাথমিক মোল সংখ্যা} {\lat [mol]}
\end{itemize}

\itm{17} {\lat $P_A = X_A \cdot P$}
\begin{itemize}
    \item[] {\lat $P_A$} = \B{আংশিক চাপ} {\lat [atm]}
    \item[] {\lat $X_A$} = \B{মোল ভগ্নাংশ}
    \item[] {\lat $P$} = \B{মোট চাপ} {\lat [atm]}
\end{itemize}

\itm{18} {\lat $X_A = \dfrac{n_A}{n}$}
\begin{itemize}
    \item[] {\lat $n_A$} = {\lat $A$} \B{বিক্রিয়কের মোল সংখ্যা} {\lat [mol]}
    \item[] {\lat $n$} = \B{বিক্রিয়া পাত্রে উপস্থিত বিক্রিয়কসমূহের মোল সংখ্যা} {\lat [mol]}
\end{itemize}

\itm{19} \textbf{\B{কোনো উপমুখী বিক্রিয়ার,}} {\lat $K_p = K_c(RT)^{\Delta n}$}
\begin{itemize}
    \item[] \B{যেখানে} {\lat $\Delta n = (l + m + n + \dots) - (a + b + c + \dots)$}
    \item[] {\lat $=$} \B{(উৎপাদের মোল সংখ্যা)} $-$ \B{(বিক্রিয়কের মোল সংখ্যা)}
\end{itemize}

\itm{20} {\lat $K_p = K_c$} \quad \B{[যখন {\lat $\Delta n = 0$}]}

\itm{21} \textbf{\B{মৃদু এসিডের বিয়োজন ধ্রুবক,}} {\lat $k_a = \alpha^2 c$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{এসিডের বিয়োজন মাত্রা}
    \item[] {\lat $c$} = \B{মৃদু এসিডের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{22} \textbf{\B{মৃদু ক্ষারের বিয়োজন ধ্রুবক,}} {\lat $k_b = \alpha^2 c$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{ক্ষারের বিয়োজন মাত্রা}
    \item[] {\lat $c$} = \B{মৃদু ক্ষারের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{23} {\lat $K_w = [\text{H}_3\text{O}^+] \times [\text{OH}^-] = 1 \times 10^{-14}$}
\begin{itemize}
    \item[] {\lat $K_w$} = \B{পানির আয়নিক গুণফল} {\lat [mol$^2$ L$^{-2}$]}
    \item[] {\lat $[\text{H}_3\text{O}^+] = [\text{H}^+]$} = \B{হাইড্রোজেন আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $[\text{OH}^-]$} = \B{হাইড্রোক্সিল আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{24} {\lat $K_w = K_a \times K_b$}
\begin{itemize}
    \item[] {\lat $K_a$} = \B{এসিড বিয়োজন ধ্রুবক}
    \item[] {\lat $K_b$} = \B{ক্ষার বিয়োজন ধ্রুবক}
\end{itemize}

\itm{25} {\lat $pK_a + pK_b = 14$}

\itm{26} {\lat $pH = -\log [\text{H}^+]$} \quad [{\lat $[\text{H}^+]$} = {\lat $\text{H}^+$} \B{এর ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{27} {\lat $pOH = -\log [\text{OH}^-]$} \quad [{\lat $[\text{OH}^-]$} = {\lat $\text{OH}^-$} \B{এর ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{28} \textbf{\B{এসিডের বিয়োজন মাত্রা,}} {\lat $\alpha = \sqrt{\dfrac{K_a}{C}}$} \quad [{\lat $C$} = \B{এসিডের ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{29} \textbf{\B{ক্ষারের বিয়োজন মাত্রা,}} {\lat $\alpha = \sqrt{\dfrac{K_b}{C}}$} \quad [{\lat $C$} = \B{ক্ষারের ঘনমাত্রা,} {\lat mol L$^{-1}$}]

\itm{30} {\lat $pH + pOH = 14$}

\itm{31} {\lat $[\text{H}^+] = \alpha C$}
\begin{itemize}
    \item[] {\lat $[\text{H}^+]$} = \B{হাইড্রোজেন আয়নের ঘনমাত্রা} {\lat [mol L$^{-1}$]}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}
    \item[] {\lat $C$} = \B{ঘনমাত্রা} {\lat [mol L$^{-1}$]}
\end{itemize}

\itm{32} \textbf{\B{অম্লীয় বাফার দ্রবণের}} {\lat $pH = pK_a + \log \dfrac{[\text{\B{লবণ}}]}{[\text{\B{অম্ল}}]}$} \quad [{\lat $K_a$} = \B{অম্লের বিয়োজন ধ্রুবক}]

\itm{33} \textbf{\B{ক্ষারীয় বাফার দ্রবণের}} {\lat $pH = 14 - pK_b - \log \dfrac{[\text{\B{লবণ}}]}{[\text{\B{ক্ষারক}}]}$} \quad [{\lat $K_b$} = \B{ক্ষারকের বিয়োজন ধ্রুবক}]



\itm{34} \textbf{\B{স্বল্পদ্রাব্য লবণের দ্রাব্যতা গুণফল:}} {\lat $A_m B_n \rightleftharpoons mA^{n+} + nB^{m-}$}\\[2pt]
{\lat $K_{SP} = [A^{n+}]^m \times [B^{m-}]^n = m^m \cdot n^n \cdot S^{m+n}$}
\begin{itemize}
    \item[] \B{যেখানে} {\lat $S$} = \B{দ্রাব্যতা} {\lat [mol\,L$^{-1}$]}; \B{এই সূত্রটিই} {\lat $x^x y^y S^{(x+y)}$} \B{রূপে লেখা হয়}
    \item[] \textbf{\B{উদাহরণ:}} {\lat $Ca_3(PO_4)_2$}: {\lat $K_{SP} = 108\,S^5$}; {\lat $BaSO_4$}: {\lat $K_{SP} = S^2$}
\end{itemize}

\itm{35} \textbf{\B{দ্রাব্যতা ও দ্রাব্যতা গুণফলের সম্পর্ক:}}
\begin{itemize}
    \item[] {\lat $AB \rightarrow K_{SP} = S^2$} \quad {\lat $A_2B \rightarrow K_{SP} = 4S^3$}
    \item[] {\lat $AB_2 \rightarrow K_{SP} = 4S^3$} \quad {\lat $A_2B_3 \rightarrow K_{SP} = 108\,S^5$}
    \item[] {\lat $A_3B \rightarrow K_{SP} = 27\,S^4$} \quad {\lat $AB_3 \rightarrow K_{SP} = 27\,S^4$}
\end{itemize}

\itm{36} \textbf{\B{তাপগতিবিদ্যার সূত্রসমূহ:}}\\[2pt]
{\lat $\Delta G = \Delta H - T\Delta S$} \quad \B{(গিবস মুক্ত শক্তি)}
\begin{itemize}
    \item[] {\lat $\Delta G = -nFE_{cell}$} \quad {\lat $\Delta G^\circ = -RT\ln K$}
    \item[] {\lat $\Delta G^\circ = -2.303\,RT\log K$}
    \item[] {\lat $\Delta H = \Delta U + \Delta n_g RT$} \quad \B{(কির্শহফের সূত্র)}
    \item[] {\lat $\Delta G < 0$} = \B{স্বতঃস্ফূর্ত}; {\lat $\Delta G > 0$} = \B{অস্বতঃস্ফূর্ত}; {\lat $\Delta G = 0$} = \B{সাম্যাবস্থা}
\end{itemize}

\itm{37} \textbf{\B{হেস সূত্র:}} \B{একটি বিক্রিয়ার তাপের পরিমাণ বিক্রিয়াটি সরাসরি বা ধাপে ধাপে সম্পন্ন হোক সমান।}\\[2pt]
{\lat $\Delta H_{rxn} = \sum \Delta H_f^\circ(\text{\B{উৎপাদ}}) - \sum \Delta H_f^\circ(\text{\B{বিক্রিয়ক}})$}

\itm{38} \textbf{\B{বন্ড শক্তি থেকে এনথালপি:}}\\[2pt]
{\lat $\Delta H = \sum$} \B{(ভাঙা বন্ধনের শক্তি)} $-$ {\lat $\sum$} \B{(তৈরি বন্ধনের শক্তি)}

\itm{39} \textbf{\B{এনট্রপি পরিবর্তন:}}\\[2pt]
{\lat $\Delta S = \dfrac{q_{rev}}{T}$} \quad [\B{প্রত্যাবর্তী প্রক্রিয়ায়}]; \quad {\lat $\Delta S_{univ} = \Delta S_{sys} + \Delta S_{surr} \geq 0$}

\itm{40} \textbf{\B{সমতাপীয় প্রসারণে কাজ:}} {\lat $w = -nRT\ln\dfrac{V_2}{V_1} = -2.303\,nRT\log\dfrac{V_2}{V_1}$}

\itm{41} \textbf{\B{তড়িৎ রাসায়নিক কোষের বিভব — নার্নস্ট সমীকরণ:}}\\[2pt]
{\lat $E_{cell} = E^\circ_{cell} - \dfrac{RT}{nF}\ln Q = E^\circ_{cell} - \dfrac{0.0592}{n}\log Q$} \B{(২৫}{\lat °C} \B{তাপমাত্রায়)}

\itm{42} \textbf{\B{বাষ্পচাপ হ্রাস (রাউল্টের সূত্র):}}\\[2pt]
{\lat $\dfrac{\Delta P}{P^\circ} = X_B = \dfrac{n_B}{n_A + n_B}$}
\begin{itemize}
    \item[] {\lat $\Delta P = P^\circ - P_s$} = \B{বাষ্পচাপ হ্রাস}; {\lat $P^\circ$} = \B{বিশুদ্ধ দ্রাবকের বাষ্পচাপ}
    \item[] {\lat $P_s$} = \B{দ্রবণের বাষ্পচাপ}; {\lat $X_B$} = \B{দ্রবের মোল ভগ্নাংশ}
\end{itemize}

\itm{43} \textbf{\B{স্ফুটনাঙ্ক উন্নয়ন:}} {\lat $\Delta T_b = K_b \times m$}\\[2pt]
\textbf{\B{হিমাঙ্ক অবনমন:}} {\lat $\Delta T_f = K_f \times m$}
\begin{itemize}
    \item[] {\lat $m$} = \B{মোলালিটি} {\lat [mol\,kg$^{-1}$]}; {\lat $K_b$} = \B{স্ফুটনাঙ্ক উন্নয়ন ধ্রুবক}; {\lat $K_f$} = \B{হিমাঙ্ক অবনমন ধ্রুবক}
\end{itemize}

\itm{44} \textbf{\B{অভিস্রবণ চাপ:}} {\lat $\pi = CRT = \dfrac{n}{V}RT$}
\begin{itemize}
    \item[] {\lat $\pi$} = \B{অভিস্রবণ চাপ} {\lat [atm]}; {\lat $C$} = \B{মোলার ঘনমাত্রা} {\lat [mol\,L$^{-1}$]}
    \item[] {\lat $R$} = \B{গ্যাস ধ্রুবক}; {\lat $T$} = \B{তাপমাত্রা} {\lat [K]}
\end{itemize}

\itm{45} \textbf{\B{আণবিক ভর নির্ণয় (হিমাঙ্ক অবনমন থেকে):}}\\[2pt]
{\lat $M_B = \dfrac{K_f \times W_B \times 1000}{\Delta T_f \times W_A}$}
\begin{itemize}
    \item[] {\lat $W_B$} = \B{দ্রবের ভর} {\lat [g]}; {\lat $W_A$} = \B{দ্রাবকের ভর} {\lat [g]}
\end{itemize}

\itm{46} \textbf{\B{ভ্যান্ট হফ গুণক:}} {\lat $i = \dfrac{\text{\B{পরিমাপকৃত সংখ্যা}}}{\text{\B{প্রত্যাশিত সংখ্যা}}} = 1 + \alpha(n-1)$}
\begin{itemize}
    \item[] {\lat $\alpha$} = \B{বিয়োজন মাত্রা}; {\lat $n$} = \B{আয়নের সংখ্যা}
    \item[] \B{সংশোধিত সূত্র:} {\lat $\Delta T_b = i\,K_b\,m$}; {\lat $\Delta T_f = i\,K_f\,m$}; {\lat $\pi = i\,CRT$}
\end{itemize}

\itm{47} \textbf{\B{রেডক্স বিক্রিয়ায় ইলেকট্রন সংখ্যা:}}\\[2pt]
{\lat $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$}\\[2pt]
{\lat $\Delta G^\circ = -nFE^\circ_{cell}$} \quad \B{এবং} \quad {\lat $\log K = \dfrac{nE^\circ}{0.0592}$} \B{(২৫}{\lat °C} \B{তে)}

\chsec{অধ্যায়-৫: কর্মমুখী রসায়ন}

\chsub{Concept Map: The Chapter at a Glance }{(এক নজরে অধ্যায়টি)}

\textbf{\B{কেন্দ্রীয় ধারণা: কর্মমুখী রসায়ন}}

\textbf{{\lat 1.} \B{খাদ্য নিরাপত্তার নীতিমালা:}}
\begin{itemize}
    \item \B{পর্যাপ্ত খাদ্য প্রাপ্তি, খাদ্য গ্রহণের সামর্থ্য, খাদ্য ব্যবহার}
\end{itemize}

\textbf{{\lat 2.} \B{খাদ্য সংরক্ষণ কৌশল} $\rightarrow$ \B{প্রকারভেদ:}}
\begin{itemize}
    \item \textbf{\B{প্রাকৃতিক:}} \B{খাদ্য লবণ দ্বারা খাদ্য সংরক্ষণ, সরিষার তেল দ্বারা খাদ্য সংরক্ষণ, চিনি দ্বারা খাদ্যবস্তু সংরক্ষণ।}
    \item \textbf{\B{কৃত্রিম:}} \B{অ্যান্টি মাইক্রোবিয়াল এজেন্ট, অ্যান্টি অক্সিডেন্ট এজেন্ট, কিলেটিং এজেন্ট।}
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



\chsec{অধ্যায়-১৩: গুরুত্বপূর্ণ প্রভাবকসমূহ}

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

\chsec{অধ্যায়-১৪: কার্যকরী মূলক, এর সক্রিয়তা ও শনাক্তকরণ}

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

\balance
\end{multicols}

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{রসায়ন দ্বিতীয় পত্র — প্রয়োজনীয় সূত্রাবলী ও তথ্যসমূহ}}}
\vspace{2pt}\par

\begin{multicols*}{2}

\chsec{অধ্যায়-১: গ্যাসের ধর্ম}

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
    \item[] {\lat $C_{mp}$} = \B{সম্ভাব্যতম বেগ} {\lat [m/s]}
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

\itm{14} \textbf{\B{সম্ভাব্যতম বেগ,}} {\lat $C_{mp} = \sqrt{\dfrac{2RT}{M}}$}

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


\chsec{অধ্যায়-৩: দ্রবণের ঘনমাত্রা}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{মোলসংখ্যা,}} {\lat $n = \dfrac{W}{M} = \dfrac{V'}{V} = \dfrac{N}{N_A} = SV' = \dfrac{PV'}{RT}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{প্রদত্ত ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর}
    \item[] {\lat $V'$} = \B{প্রদত্ত আয়তন (}{\lat STP}\B{ তে প্রকাশিত)} {\lat [L]}
    \item[] {\lat $V = 22.4$} {\lat L} \B{(}{\lat STP}\B{ তে)}
    \item[] {\lat $N$} = \B{প্রদত্ত অণু/পরমাণুর সংখ্যা}
    \item[] {\lat $N_A$} = \B{আভোগেড্রো সংখ্যা}
    \item[] {\lat $S$} = \B{ঘনমাত্রা} {\lat [mol/L]}
\end{itemize}

\itm{2} \textbf{\B{মোলারিটি,}} {\lat $S = \dfrac{W \times 1000}{M \times V}$}\\[3pt]
{\lat $S = \dfrac{S_{mo}}{1 + S_m \cdot M \times 10^{-3}}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর}
    \item[] {\lat $V$} = \B{আয়তন} {\lat [mL]}
    \item[] {\lat $S_{mo}$} = \B{মোলালিটি}; {\lat $S_m$} = \B{মোলারিটি}
\end{itemize}

\itm{3} \textbf{\B{মোলালিটি,}} {\lat $m = \dfrac{W \times 1000}{M \times W'}$}\\[3pt]
{\lat $S_m = \dfrac{S}{\rho \times SM \times 10^{-3}}$}
\begin{itemize}
    \item[] {\lat $W$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর}
    \item[] {\lat $W'$} = \B{দ্রাবকের ভর} {\lat [g]}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব}; {\lat $S$} = \B{মোলারিটি} {\lat [mol/L]}
\end{itemize}

\itm{4} \textbf{\B{নরমালিটি,}}\\[2pt]
{\lat $N = \dfrac{W \times 1000}{E \times V} = \dfrac{W \times 1000}{\frac{M}{e} \times V} = \left(\dfrac{W \times 1000}{M \times V}\right) \times e = S \times e$}
\begin{itemize}
    \item[] {\lat $W$} = \B{দ্রবের ভর} {\lat [g]}
    \item[] {\lat $E$} = \B{তুল্য ভর}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর}
    \item[] {\lat $e$} = \B{তুল্য সংখ্যা}
    \item[] {\lat $V$} = \B{দ্রবণের আয়তন} {\lat [mL]}
    \item[] {\lat $S$} = \B{মোলারিটি} {\lat [mol/L]}
\end{itemize}

\itm{5} \textbf{\B{শতকরা মাত্রা থেকে মোলারিটি:}}
\begin{itemize}
    \item[] {\lat $x\%\!\left(\tfrac{w}{v}\right)$}\B{:} {\lat $S = \dfrac{10 \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{w}{w}\right)$}\B{:} {\lat $S = \dfrac{10 \times \rho \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{V}{V}\right)$}\B{:} {\lat $S = \dfrac{10 \times \rho' \times x}{M}$}
    \item[] {\lat $x\%\!\left(\tfrac{V}{w}\right)$}\B{:} {\lat $S = \dfrac{10 \times \rho \times \rho' \times x}{M}$}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব} {\lat [g/L]}; {\lat $\rho'$} = \B{দ্রবের ঘনত্ব} {\lat [g/L]}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর} {\lat [g]}; {\lat $S$} = \B{মোলারিটি} {\lat [mol/L]}
\end{itemize}

\itm{6} \textbf{{\lat ppm} \B{ও অন্যান্য ঘনমাত্রা:}}
\begin{itemize}
    \item[] {\lat $x$} \B{মোলার দ্রবণ} {\lat $= \dfrac{x \times M \times 10^6}{1000 \times \rho}$ ppm}
    \item[] {\lat $x\%\!\left(\tfrac{w}{v}\right)$} \B{দ্রবণ} {\lat $= \dfrac{x \times 10^6}{100 \times \rho}$ ppm}
    \item[] {\lat $x\%\!\left(\tfrac{w}{w}\right)$} \B{দ্রবণ} {\lat $= \dfrac{x}{100} \times 10^6$ ppm}
    \item[] {\lat $x\%\!\left(\tfrac{V}{V}\right)$} \B{দ্রবণ} {\lat $= \dfrac{x \times \rho}{100} \times 10^6$ ppm}
    \item[] {\lat $x$} \B{মোলাল দ্রবণ} {\lat $= \dfrac{x \times M \times 10^6}{1000 + (x \times \rho)}$ ppm}
    \item[] {\lat $M$} = \B{পারমাণবিক/আণবিক ভর} {\lat [g]}; {\lat $\rho$} = \B{আপেক্ষিক গুরুত্ব} {\lat [g/L]}
\end{itemize}

\itm{7} \textbf{\B{দ্রবণের ঘনমাত্রা লঘুকরণ,}} {\lat $V_1 S_1 = V_2 S_2$}
\begin{itemize}
    \item[] {\lat $V_1$} = \B{দ্রবণের প্রাথমিক আয়তন} {\lat [mL, L]}
    \item[] {\lat $V_2$} = \B{দ্রবণের পরিবর্তিত আয়তন} {\lat [mL, L]}
    \item[] {\lat $S_1$} = \B{দ্রবণের প্রাথমিক ঘনমাত্রা} {\lat [mol/L]}
    \item[] {\lat $S_2$} = \B{দ্রবণের পরিবর্তিত ঘনমাত্রা} {\lat [mol/L]}
\end{itemize}

\itm{8} \textbf{\B{এসিড-ক্ষারক প্রশমন,}} {\lat $b \times V_A \times S_A = a \times V_B \times S_B$}
\begin{itemize}
    \item[] {\lat $V_A$} = \B{এসিডের আয়তন} {\lat [mL, L]}
    \item[] {\lat $V_B$} = \B{ক্ষারকের আয়তন} {\lat [mL, L]}
    \item[] {\lat $S_A$} = \B{এসিডের ঘনমাত্রা} {\lat [mol/L]}
    \item[] {\lat $S_B$} = \B{ক্ষারকের ঘনমাত্রা} {\lat [mol/L]}
    \item[] {\lat $a$} = \B{এসিডের মোলসংখ্যা} {\lat [mol]}
    \item[] {\lat $b$} = \B{ক্ষারকের মোলসংখ্যা} {\lat [mol]}
\end{itemize}



\itm{8} \textbf{\B{নর্মালিটি থেকে মোলারিটি:}} {\lat $M = \dfrac{N}{n}$}\\[2pt]
\textbf{\B{মোলারিটি থেকে মোলালিটি:}} {\lat $m = \dfrac{M \times 1000}{\rho \times 1000 - M \times M_B}$}
\begin{itemize}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব} {\lat [g\,mL$^{-1}$]}; {\lat $M_B$} = \B{দ্রবের আণবিক ভর}
\end{itemize}

\itm{9} \textbf{\B{মোল ভগ্নাংশ:}} {\lat $X_A = \dfrac{n_A}{n_A + n_B}$}; \quad {\lat $X_A + X_B = 1$}

\itm{10} \textbf{\B{ভরের ভাগ} {\lat (mass fraction)}\B{:}} {\lat $w_A = \dfrac{m_A}{m_{solution}}$}

\itm{11} \textbf{\B{দ্রবণের ঘনত্ব থেকে মোলারিটি:}}\\[2pt]
{\lat $M = \dfrac{10 \times \rho \times \%}{M_B}$}
\begin{itemize}
    \item[] {\lat $\rho$} = \B{দ্রবণের ঘনত্ব} {\lat [g/mL]}; {\lat \%} = \B{ভর শতাংশ}; {\lat $M_B$} = \B{আণবিক ভর}
\end{itemize}

\chsec{অধ্যায়-৪: তড়িৎ রসায়ন}

\chsub{}{প্রয়োজনীয় সূত্রাবলি}

\itm{1} \textbf{\B{আপেক্ষিক পরিবাহিতা,}} {\lat $\kappa = \dfrac{1}{\rho} = \dfrac{1}{R} \times \dfrac{l}{A} = L \times \dfrac{l}{A}$}
\begin{itemize}
    \item[] {\lat $\kappa$ (Kappa)} = \B{আপেক্ষিক পরিবাহিতা} {\lat [ohm$^{-1}$cm$^{-1}$, Sm$^{-1}$]}
    \item[] {\lat $L$} = \B{পরিবাহিতা} {\lat [ohm$^{-1}$]}
    \item[] {\lat $\Lambda$ (Lambda)} = \B{তুল্য পরিবাহিতা} {\lat [ohm$^{-1}$cm$^2$(g.eqv)$^{-1}$; Sm$^2$(g.eqv)$^{-1}$]}
    \item[] {\lat $\Lambda_m$} = \B{মোলার পরিবাহিতা} {\lat [ohm$^{-1}$cm$^2$mol$^{-1}$; Sm$^2$mol$^{-1}$]}
    \item[] {\lat $C$} = \B{দ্রবণের ঘনমাত্রা} {\lat [g.eqv]}
    \item[] {\lat $M$} = \B{দ্রবণের ঘনমাত্রা} {\lat [molL$^{-1}$, M]}
    \item[] {\lat $V$} = \B{দ্রবণের আয়তন} {\lat [cm$^3$]}
    \item[] {\lat $A$} = \B{দুইটি তড়িৎদ্বারের প্রস্থচ্ছেদ} {\lat [cm$^2$]}
    \item[] {\lat $l$} = \B{দৈর্ঘ্য} {\lat [cm]}
    \item[] {\lat $N$} = \B{দ্রবণের ঘনমাত্রা} {\lat [g.eqv, N]}
\end{itemize}

\itm{2} \textbf{\B{কোষ ধ্রুবক} {\lat $= \dfrac{l}{A}$}}

\itm{3} \textbf{\B{তুল্য পরিবাহিতা,}} {\lat $\Lambda = \kappa V$}

\itm{4} \textbf{\B{তুল্য পরিবাহিতা,}} {\lat $\Lambda = \kappa \times \dfrac{1000}{C}$}

\itm{5} \textbf{\B{মোলার পরিবাহিতা,}} {\lat $\Lambda_m = \kappa \times \dfrac{1000}{M}$}

\itm{6} \textbf{\B{তুল্য পরিবাহিতা,}} {\lat $\Lambda = \kappa \times \dfrac{1000}{N}$}

\itm{7} \textbf{\B{মৌলের তড়িৎ রাসায়নিক তুলনাঙ্ক,}}\\[2pt]
{\lat $Z = \dfrac{\text{\B{মৌলের পারমাণবিক ভর}}}{F \times \text{\B{মৌলের যোজ্যতা}}}$}
\begin{itemize}
    \item[] {\lat $Z$} = \B{তড়িৎ রাসায়নিক তুল্যাঙ্ক} {\lat [gC$^{-1}$]}
\end{itemize}

\itm{8} \textbf{\B{যৌগের তড়িৎ রাসায়নিক তুলনাঙ্ক,}}\\[2pt]
{\lat $Z = \dfrac{\text{\B{যৌগের পারমাণবিক ভর}}}{F \times \text{\B{যৌগের ধনাত্মক অংশের যোজ্যতা}}}$}

\itm{9} \textbf{\B{ফ্যারাডের ১ম সূত্র:}}
\begin{itemize}
    \item \textbf{(i)} {\lat $W = ZQ$}
    \item \textbf{(ii)} {\lat $Q = It$}
    \item \textbf{(iii)} {\lat $W = ZIt$}
    \item \textbf{(iv)} {\lat $W = \dfrac{MIt}{nF}$}
\end{itemize}
\begin{itemize}
    \item[] {\lat $Z$} = \B{তড়িৎ রাসায়নিক তুল্যাঙ্ক} {\lat [g/C]}
    \item[] {\lat $w$} = \B{সঞ্চিত বা দ্রবীভূত পদার্থের ভর} {\lat [g]}
    \item[] {\lat $E$} = \B{রাসায়নিক তুল্যাঙ্ক বা তুল্য ভর} {\lat [g]}
    \item[] {\lat $I$} = \B{তড়িৎ প্রবাহ} {\lat [A]} \B{(অ্যাম্পিয়ার)}
    \item[] {\lat $t$} = \B{সময়} {\lat [s]} \B{(সেকেন্ড)}
    \item[] {\lat $n$} = \B{যোজ্যতা}
    \item[] {\lat $Q$} = \B{চার্জ} {\lat [C]} \B{(কুলম্ব)}
    \item[] {\lat $F$} = \B{ফ্যারাডে ধ্রুবক} {\lat = 96500 C}
\end{itemize}

\itm{10} \textbf{\B{ফ্যারাডের ১ম সূত্র,}} {\lat $\dfrac{W_A}{W_B} = \dfrac{E_1}{E_2}$}

\itm{11} \textbf{\B{কোষ বিভব,}} {\lat $E^\circ_{\text{cell}} = E^\circ_{\text{ox(anode)}} + E^\circ_{\text{red(cathode)}}$}\\[2pt]
{\lat $= E^\circ_{\text{ox(anode)}} - E^\circ_{\text{ox(cathode)}}$}\\[2pt]
{\lat $= E^\circ_{\text{red(cathode)}} - E^\circ_{\text{red(anode)}}$}
\begin{itemize}
    \item[] {\lat $E^\circ_{\text{ox(cathode)}}$} = \B{ক্যাথোডের প্রমাণ জারণ বিভব}
    \item[] {\lat $E^\circ_{\text{ox(anode)}}$} = \B{অ্যানোডের প্রমাণ জারণ বিভব}
    \item[] {\lat $E^\circ_{\text{red(cathode)}}$} = \B{ক্যাথোডের প্রমাণ বিজারণ বিভব}
    \item[] {\lat $E^\circ_{\text{red(anode)}}$} = \B{অ্যানোডের প্রমাণ বিজারণ বিভব}
\end{itemize}

\itm{12} \textbf{\B{নার্নস্ট সমীকরণ} — {\lat xA + yB$^+$ $\rightleftharpoons$ xA$^+$ + yB} \B{বিক্রিয়ার ক্ষেত্রে:}}
\begin{itemize}
    \item \textbf{(i)} {\lat $E_{A/A^+} = E^\circ_{A/A^+} - \dfrac{RT}{nF} \ln [A^+]^x$}
    \item \textbf{(ii)} {\lat $E_{B^+/B} = E^\circ_{B^+/B} + \dfrac{RT}{nF} \ln [B^+]^y$}
    \item \textbf{(iii)} {\lat $E_{\text{cell}} = E^\circ_{\text{cell}} - \dfrac{RT}{nF} \ln \dfrac{[A^+]^x}{[B^+]^y}$}
    \item \textbf{(iv)} {\lat $E_{\text{cell}} = [E^\circ_{\text{ox(Anode)}} + E^\circ_{\text{red(cathode)}}] - \dfrac{RT}{nF} \ln \dfrac{[A^+]^x}{[B^+]^y}$}
\end{itemize}
\begin{itemize}
    \item[] {\lat $[A^+]$} = {\lat $A^+$} \B{এর ঘনমাত্রা} {\lat [molL$^{-1}$]}
    \item[] {\lat $[B^+]$} = {\lat $B^+$} \B{এর ঘনমাত্রা} {\lat [molL$^{-1}$]}
    \item[] {\lat $F = 96500$} \B{কুলম্ব} {\lat [C} \B{(কুলম্ব)}{\lat ]}
    \item[] {\lat $E_{\text{cell}}$} = \B{নির্দিষ্ট তাপমাত্রায় কোষটির তড়িৎচালক বল} {\lat [V]}
    \item[] {\lat $E^\circ_{\text{cell}}$} = \B{প্রমাণ তাপমাত্রায় কোষটির তড়িৎচালক বল} {\lat [V]}
\end{itemize}

\itm{13} \textbf{\B{{\lat EMF} ও মুক্ত শক্তির পরিবর্তন সম্পর্কিত:}}
\begin{itemize}
    \item \textbf{(i)} {\lat $\Delta G = -nFE_{\text{cell}}$}
    \item \textbf{(ii)} {\lat $\Delta G^\circ = -nFE^\circ_{\text{cell}}$}
    \item \textbf{(iii)} {\lat $\Delta G = -RT\ln K$}
    \item \textbf{(iv)} {\lat $RT\ln K = nFE_{\text{cell}}$}
\end{itemize}
\begin{itemize}
    \item[] {\lat $E_{\text{cell}}$} = \B{তাপমাত্রায় কোষটির তড়িৎচালক বল} {\lat [V]}
    \item[] {\lat $E^\circ_{\text{cell}}$} = \B{প্রমাণ তাপমাত্রায় কোষটির তড়িৎচালক বল} {\lat [V]}
    \item[] {\lat $\Delta G$} = \B{মুক্ত শক্তির পরিবর্তন} {\lat [J]}
\end{itemize}


\itm{12} \textbf{\B{পরিবাহিতার সম্পর্ক:}} {\lat $\kappa = \dfrac{1}{\rho}$} \quad [\B{আপেক্ষিক পরিবাহিতা = আপেক্ষিক রোধের বিপরীত}]\\[2pt]
{\lat $\Lambda_m = \dfrac{\kappa \times 1000}{C}$} \quad [\B{মোলার পরিবাহিতা}; {\lat $C$} = \B{মোলার ঘনমাত্রা}]

\itm{13} \textbf{\B{কোলরাউশের সূত্র:}} {\lat $\Lambda_m^\infty = \nu_+ \lambda_+^\infty + \nu_- \lambda_-^\infty$}
\begin{itemize}
    \item[] {\lat $\lambda_+^\infty, \lambda_-^\infty$} = \B{অসীম লঘুতায় আয়নিক পরিবাহিতা}
    \item[] {\lat $\nu_+, \nu_-$} = \B{ক্যাটায়ন ও অ্যানায়নের সংখ্যা}
\end{itemize}

\itm{14} \textbf{\B{তড়িৎ বিশ্লেষণে সঞ্চিত/দ্রবীভূত ভর:}}\\[2pt]
{\lat $W = \dfrac{M \times I \times t}{n \times F} = Z \times I \times t$}
\begin{itemize}
    \item[] {\lat $M$} = \B{আণবিক ভর}; {\lat $n$} = \B{যোজনী}; {\lat $F = 96500\,C$}
    \item[] {\lat $Z$} = \B{তড়িৎ রাসায়নিক তুল্যাঙ্ক} {\lat $= \dfrac{E}{96500}$}
\end{itemize}

\itm{15} \textbf{\B{প্রমাণ হাইড্রোজেন ইলেকট্রোড} {\lat (SHE)}\B{:}} {\lat $E^\circ = 0.00\,V$}\\[2pt]
\textbf{\B{কোষের প্রমাণ বিভব:}} {\lat $E^\circ_{cell} = E^\circ_{cathode} - E^\circ_{anode}$}\\[2pt]
\textbf{\B{কোষের বিভব ধনাত্মক হলে বিক্রিয়া স্বতঃস্ফূর্ত।}}

\chsec{অধ্যায়-১: গ্যাস সূত্রসমূহ — {\lat At a Glance}}

\chsub{}{গ্যাস সূত্রের তালিকা}

\itm{1} \textbf{\B{বয়েলের সূত্র} ({\lat 1662} \B{সাল, ইংল্যান্ড}):} \B{স্থির তাপমাত্রায় কোন নির্দিষ্ট ভরের যেকোন গ্যাসের আয়তন তার চাপের বিপরীত অনুপাতে পরিবর্তিত হয়।}\\[1pt]
{\lat $P_1V_1 = P_2V_2$}

\itm{2} \textbf{\B{চার্লসের সূত্র} ({\lat 1787} \B{সাল, ফ্রান্স; গে-লুস্যাক, ১৮০২ সাল):}} \B{স্থির চাপে কোন নির্দিষ্ট ভরের যেকোন গ্যাসের আয়তন তার তাপমাত্রার সমানুপাতিক।}\\[1pt]
{\lat $V \propto T$} \quad \B{বা,} {\lat $\dfrac{V_1}{T_1} = \dfrac{V_2}{T_2}$}

\itm{3} \textbf{\B{চাপের সূত্র বা গে-লুস্যাকের চাপের সূত্র} ({\lat 1802} \B{সাল):}} \B{স্থির আয়তনে গ্যাসের চাপ তার পরম তাপমাত্রার সমানুপাতিক।}\\[1pt]
{\lat $P \propto T$}

\itm{4} \textbf{\B{অ্যাভোগেড্রোর সূত্র} ({\lat 1811} \B{সাল, ইতালী):}} \B{নির্দিষ্ট আয়তনের গ্যাসে সমান সংখ্যক অণু থাকে।}\\[1pt]
{\lat $V \propto n$}

\itm{5} \textbf{\B{ডালটনের আংশিক চাপ সূত্র} (\B{জন ডালটন, ১৮০২ সাল, ইংল্যান্ড}):} \B{স্থির তাপমাত্রা ও চাপে বিভিন্ন গ্যাস মিশ্রণের মোট চাপ ও তাদের আংশিক চাপের সমষ্টির সমান।}\\[1pt]
{\lat $P = P_1 + P_2 + P_3 + \dots + P_n$}

\itm{6} \textbf{\B{গ্রাহামের ব্যাপন সূত্র} ({\lat 1829} \B{বা ১৮৩৩ সাল):}} \B{স্থির তাপমাত্রা ও চাপে যেকোন গ্যাসের ব্যাপনের হার তার ঘনত্বের বর্গমূলের বিপরীত অনুপাতে পরিবর্তিত হয়।}\\[1pt]
{\lat $r \propto \sqrt{\dfrac{1}{d}}$}

\itm{7} \textbf{\B{গে-লুস্যাকের আয়তন সূত্র} ({\lat 1808} \B{সাল, ইংল্যান্ড):}} \B{রাসায়নিক বিক্রিয়ার সময় ও গ্যাসের আয়তনের সম্পর্ক। যখন বিভিন্ন গ্যাস পরস্পর রাসায়নিক বিক্রিয়ার অংশগ্রহণ করে তখন বিক্রিয়ক গ্যাসগুলোর আয়তন সরল অনুপাতিক থাকে।}

\chsec{অধ্যায়-৫: শিল্প কারখানায় সাম্যাবস্থার প্রয়োগ}

\chsub{}{শিল্প কারখানায় সাম্যাবস্থার প্রয়োগ এবং ব্যবহৃত অনুঘটক}

\begin{itemize}
    \item \textbf{\B{১. অ্যামোনিয়া}} — \B{পদ্ধতি: হেবার বস; তাপমাত্রা: ৪৫০–৫৫০}{\lat °C}\B{; চাপ: ২০০ }{\lat atm}\B{; প্রভাবক:} {\lat Fe/MO}
    \item \textbf{{\lat H$_2$SO$_4$}} \B{(২.)} — \B{পদ্ধতি: স্পর্শ প্রণালী; তাপমাত্রা: ৪০০–৫০০}{\lat °C}\B{; চাপ: ১.৭ }{\lat atm}\B{; প্রভাবক:} {\lat V$_2$O$_5$} \B{বা} {\lat Pt}
    \item \textbf{\B{৩. মিথানল}} — \B{পদ্ধতি: বাণিজ্যিক; তাপমাত্রা: ৩০০–৪০০}{\lat °C}\B{; চাপ: ২০০–৩০০ }{\lat atm}\B{; প্রভাবক:} {\lat ZnO + Cr$_2$O$_3$}
    \item \textbf{\B{৪. ইউরিয়া}} — \B{পদ্ধতি: রাসায়নিক; তাপমাত্রা: ১৭০–২০০}{\lat °C}\B{; চাপ: ১০০–৩০০ }{\lat atm}
\end{itemize}

\chsec{অধ্যায়-৫: শিল্পক্ষেত্রে অনুঘটকের ব্যবহার}

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


\chsec{অধ্যায়-১২: বিভিন্ন পলিমারের বৈশিষ্ট্য ও ব্যবহার}

\chsub{}{পলিমারের তালিকা}

\itm{1} \textbf{\B{পলিইথিলিন (পলিথিন):}} {\lat CH$_2${=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: নমনীয় কিন্তু শক্ত প্রকৃতির; এটা এসিড, ক্ষার ও বিভিন্ন দ্রাবক দ্বারা আক্রান্ত হয় না; উত্তম তড়িৎ অন্তরক।}
    \item \B{ব্যবহার: ওষুধ প্যাকেট; মগ, বালতি, টেবিল, রুথ; বৈদ্যুতিক তারের অন্তরক; বোতল তৈরিতে।}
\end{itemize}

\itm{2} \textbf{\B{পলিপ্রোপিলিন:}} {\lat CH$_3$CH{=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: সবচেয়ে হালকা পলিমার।}
    \item \B{ব্যবহার: দড়ি তৈরিতে, মালপত্র প্যাকেজিং; মোটরজু, কার্পেট তৈরিতে।}
\end{itemize}

\itm{3} \textbf{\B{পলিভিনাইল ক্লোরাইড (}} {\lat PVC} \textbf{\B{):}} {\lat CH$_2${=}CHCl} $\rightarrow$ {\lat $(-\text{CH}_2{-}\text{CH}-)_n$}
\begin{itemize}
    \item \B{ব্যবহার: কৃত্রিম চামড়া; ঘরের ছাদ তৈরি; রেইন কোট, গ্রামোফোন রেকর্ড।}
\end{itemize}

\itm{4} \textbf{\B{পলিটেট্রাফ্লোরো ইথিন (}} {\lat PTFE} \B{— টেফলন):} {\lat CF$_2${=}CF$_2$} $\rightarrow$ {\lat $(-\text{CF}_2{-}\text{CF}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: ফুয়েরো কার্বন হিসেবে খুবই নিষ্ক্রিয়; বিদ্যুৎ ও তাপ অপরিবাহী।}
    \item \B{ব্যবহার: নন-স্টিক রান্নার প্যান; জাহাজের রঙে।}
\end{itemize}

\itm{5} \textbf{\B{পলিস্টাইরিন (পলিফিনাইল ইথিন):}}
\begin{itemize}
    \item \B{ব্যবহার: খাবার পাত্র, কসমেটিকের বোতল; টেলিভিশন ক্যাবিনেট; শিশুর খেলনা।}
\end{itemize}

\itm{6} \textbf{\B{নিওপ্রিন (পলি-২-ক্লোরোবিউটা-ডাই-ইন):}}
\begin{itemize}
    \item \B{ব্যবহার: সিনথেটিক রাবার তৈরিতে।}
\end{itemize}

\itm{7} \textbf{\B{পলিভিনাইল অ্যাসিটেট (}} {\lat PVA} \textbf{):} {\lat CH$_3$COO{-}CH{=}CH$_2$} $\rightarrow$ {\lat $(-\text{CH{-}CH}_2-)_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য:} {\lat PVC} \B{থেকে নমনীয়।}
    \item \B{ব্যবহার: ইমালসন পেইন্ট; গ্রামোফোন রেকর্ড।}
\end{itemize}

\itm{8} \textbf{\B{নাইলন ৬:৬:}} {\lat HOOC(CH$_2$)$_4$CONH(CH$_2$)$_6$NH$_2$} $\rightarrow$ {\lat $[-\text{OC(CH}_2)_4\text{CONH(CH}_2)_6\text{NH}-]_n$}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: তন্তুময়।}
    \item \B{ব্যবহার: সুতা তৈরিতে।}
\end{itemize}

\itm{9} \textbf{\B{নাইলন ৬:}}
\begin{itemize}
    \item \B{বৈশিষ্ট্য: নাইলন ৬:৬ অপেক্ষা নমনীয় ও নিম্ন গলনাঙ্ক বিশিষ্ট।}
    \item \B{ব্যবহার: তন্তু হিসাবে, কাপড়ের সুতা, চাকার টায়ারের রজ্জু, দড়ি তৈরিতে।}
\end{itemize}

\chsec{অধ্যায়-৭: বিভিন্ন ভৌত পরিমাপের প্রচলিত ও আন্তর্জাতিক {\lat (SI)} একক}

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

\chsec{অধ্যায়-৮: মৌলিক ধ্রুবকসমূহ}

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



\chsec{অধ্যায়-৯: গুরুত্বপূর্ণ রাসায়নিক বিক্রিয়া ও শর্ত}

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
    \item \textbf{\B{মার্কভনিকভের নিয়ম:}} \B{হাইড্রোজেন পরমাণু সেই কার্বনে যুক্ত হয় যে কার্বনে বেশি হাইড্রোজেন আছে।}
    \item \textbf{\B{জাইতসেভের নিয়ম:}} \B{বেশি প্রতিস্থাপিত অ্যালকিন মুখ্য উৎপাদ।}
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

\end{multicols*}
\end{document}"""

with open("chemistry.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

def run(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True)
    return result.returncode

run("apt-get update -qq 2>/dev/null")
run("apt-get install -y -q texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-lang-other fonts-noto-core fonts-noto-extra 2>/dev/null")
run("fc-cache -fv 2>/dev/null")
run("xelatex -interaction=nonstopmode chemistry.tex 2>/dev/null")
run("xelatex -interaction=nonstopmode chemistry.tex 2>/dev/null")
print("PDF ready:", os.path.exists("chemistry.pdf"))
if os.path.exists("chemistry.pdf"):
    print("PDF size:", os.path.getsize("chemistry.pdf"), "bytes")
else:
    print("PDF generation failed")
