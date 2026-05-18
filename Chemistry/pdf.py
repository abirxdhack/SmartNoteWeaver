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
\usepackage{graphicx}
\pagestyle{empty}
\setlength{\emergencystretch}{25pt}
\hbadness=10000
\vbadness=10000
\sloppy
\raggedcolumns
\tolerance=9999
\emergencystretch=25pt

\setmainfont{Latin Modern Roman}
\newfontfamily\lat{Latin Modern Roman}
\newfontfamily\bn{Noto Serif Bengali}[Script=Bengali, BoldFont=Noto Serif Bengali Bold, ItalicFont=Noto Serif Bengali]

\defaultfontfeatures{}

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
    \item \textbf{\B{উচ্চ ক্ষমতাসম্পন্ন যন্ত্রপাতি:}} \B{ক্রোমাটোগ্রাফি:} {\lat HPLC, GPLC}; \B{স্পেক্ট্রোমেট্রিতে:} {\lat IR, UV-NMR}; \B{থার্মো অ্যানালাইসিসে:} {\lat DSC}; \B{পারমাণবিক শোষণ বর্ণালিতে:} {\lat AAS}; {\lat X-ray} \B{ব্যতিচার যন্ত্র।}
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
    \item \textbf{{\lat d$^2$sp$^3$}} \B{সংকরায়ন — অষ্টতলকীয় ({\lat Octahedral}); বন্ধন কোণ {\lat 90}$^{\circ}$ (অন্তর্বর্তী d-অরবিটাল ব্যবহার); উদাহরণ:} {\lat [Fe(CN)$_6$]$^{3-}$, [Co(NH$_3$)$_6$]$^{3+}$}
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


\end{multicols}

\newpage

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}\B{রসায়ন দ্বিতীয় পত্র — প্রয়োজনীয় সূত্রাবলী ও তথ্যসমূহ}}}
\vspace{2pt}\par

\begin{multicols}{2}

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
    \item[] {\lat $T_1$} = \B{প্রাথমিক অবস্থায় তাপমাত্রা} {\lat [K (কেলভিন)]}
    \item[] {\lat $T_2$} = \B{পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K (কেলভিন)]}
\end{itemize}

\itm{3} \textbf{\B{গে-লুস্যাকের চাপের সূত্র,}} {\lat $\dfrac{P_1}{T_1} = \dfrac{P_2}{T_2}$}
\begin{itemize}
    \item[] {\lat $P_1$} = \B{প্রাথমিক অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $P_2$} = \B{পরিবর্তিত অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $T_1$} = \B{প্রাথমিক অবস্থায় তাপমাত্রা} {\lat [K (কেলভিন)]}
    \item[] {\lat $T_2$} = \B{পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K (কেলভিন)]}
\end{itemize}

\itm{4} \textbf{\B{বয়েল ও চার্লসের সমন্বয় সূত্র,}} {\lat $\dfrac{P_1 V_1}{T_1} = \dfrac{P_2 V_2}{T_2}$}
\begin{itemize}
    \item[] {\lat $P_1, P_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $V_1, V_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় আয়তন} {\lat [mL, L, dm$^3$, cm$^3$, m$^3$]}
    \item[] {\lat $T_1, T_2$} = \B{প্রাথমিক/পরিবর্তিত অবস্থায় তাপমাত্রা} {\lat [K (কেলভিন)]}
\end{itemize}

\itm{5} \textbf{\B{গ্যাসের ঘনত্ব, তাপ ও চাপের মধ্যে সম্পর্ক,}} {\lat $\dfrac{d_1 T_1}{P_1} = \dfrac{d_2 T_2}{P_2}$}
\begin{itemize}
    \item[] {\lat $d_1$} = \B{প্রাথমিক অবস্থায় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
    \item[] {\lat $d_2$} = \B{পরিবর্তিত অবস্থায় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
    \item[] {\lat $P_1, P_2$} = \B{চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $T_1, T_2$} = \B{তাপমাত্রা} {\lat [K (কেলভিন)]}
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
    \item[] {\lat $t_1, t_2$} = \B{১ম/২য় গ্যাসের ব্যাপন সময়} {\lat [s (সেকেন্ড)]}
    \item[] {\lat $M_1, M_2$} = \B{১ম/২য় গ্যাসের আণবিক ভর} {\lat [gmol$^{-1}$]}
    \item[] {\lat $V_1, V_2$} = \B{১ম/২য় গ্যাসের বেগ} {\lat [ms$^{-1}$, cms$^{-1}$]}
    \item[] {\lat $d_1, d_2$} = \B{১ম/২য় গ্যাসের ঘনত্ব} {\lat [gL$^{-1}$, kgm$^{-3}$, gcm$^{-3}$, gdm$^{-3}$]}
\end{itemize}

\itm{11} \textbf{\B{ডালটনের আংশিক চাপ সূত্র,}} {\lat $P = P_A + P_B + \dots + P_n$}\\[2pt]
\textbf{\B{আংশিক চাপ,}} {\lat $P_A = n_A \times P$}
\begin{itemize}
    \item[] {\lat $P$} = \B{গ্যাস মিশ্রণের মোট চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $P_A, P_B, \dots P_n$} = \B{A, B,.. গ্যাসের আংশিক চাপ} {\lat [atm, Pa, kPa, Nm$^{-2}$, mm(Hg), cm(Hg)]}
    \item[] {\lat $n_A$} = \B{A গ্যাসের মোল ভগ্নাংশ}
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
    \item[] {\lat $V'$} = \B{প্রদত্ত আয়তন (STP তে প্রকাশিত)} {\lat [L]}
    \item[] {\lat $V = 22.4$} \B{L (STP তে)}
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

\itm{6} \textbf{\B{ppm ও অন্যান্য ঘনমাত্রা:}}
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


\end{multicols}
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
