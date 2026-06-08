import subprocess
import os

tex_content = r"""
\documentclass[7.5pt,a4paper]{article}
\usepackage{fontspec}
\usepackage[left=0.3cm,right=0.3cm,top=0.2cm,bottom=0.2cm]{geometry}
\usepackage{xcolor}
\usepackage{array}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{enumitem}
\usepackage{microtype}
\pagestyle{empty}
\hbadness=10000
\setlength{\emergencystretch}{10pt}
\setmainfont{Latin Modern Roman}
\newfontfamily\bn{Noto Serif Bengali}[Script=Bengali, BoldFont=Noto Serif Bengali Bold]
\newfontfamily\stylish{LiberationSerif-Bold}
\newcommand{\B}[1]{{\bn #1}}

\definecolor{headerblue}{HTML}{C7DFFF}

\definecolor{c1}{HTML}{D0E4FF}
\definecolor{c2}{HTML}{D6E8FF}
\definecolor{c3}{HTML}{DCEBFF}
\definecolor{c4}{HTML}{E2EEFF}
\definecolor{c5}{HTML}{E7F2FF}
\definecolor{c6}{HTML}{ECF5FF}
\definecolor{c7}{HTML}{F0F7FF}
\definecolor{c8}{HTML}{F3F9FF}
\definecolor{c9}{HTML}{F6FBFF}
\definecolor{c10}{HTML}{F9FCFF}
\definecolor{c11}{HTML}{FCFDFF}
\definecolor{c12}{HTML}{FFFFFF}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.3pt}

\begin{document}

\begin{center}
{\large\bfseries\stylish Smart Study Routine}\\[0.5pt]
{\scriptsize\color{black}By Abir Arafat Chawdhury --- HSC 2027}\\
{\scriptsize\color{black}The Complete HSC Academic Success Routine}
\end{center}

\vspace{0.5pt}

\setlength{\tabcolsep}{1.5pt}
\setlength{\arrayrulewidth}{0.4pt}
\renewcommand{\arraystretch}{0.80}

\noindent
\begin{tabularx}{\textwidth}{|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|
>{\centering\arraybackslash}X|}
\hline
\rowcolor{headerblue}\color{black}\bfseries\small Saturday &
\color{black}\bfseries\small Sunday &
\color{black}\bfseries\small Monday &
\color{black}\bfseries\small Tuesday &
\color{black}\bfseries\small Wednesday &
\color{black}\bfseries\small Thursday &
\color{black}\bfseries\small Friday \\
\hline
\rowcolor{c1}\tiny Morning & \tiny Morning & \tiny Morning & \tiny Morning & \tiny Morning & \tiny Morning & \tiny Morning \\
\hline
\rowcolor{c2}\tiny Wake up \textbf{4:30am} & \tiny 4:30am & \tiny 4:30am & \tiny 4:30am & \tiny 4:30am & \tiny 4:30am & \tiny 4:30am \\
\hline
\rowcolor{c3}\tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} & \tiny\textbf{\B{ফজর}} \textbf{4:30--4:50} \\
\hline
\rowcolor{c4}\tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} & \tiny SS1 \textbf{5:00--7:00am} \\
\hline
\rowcolor{c5}\tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} & \tiny Eat,Move,Rest \textbf{7:00--8:00am} \\
\hline
\rowcolor{c6}\tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} & \tiny SS2 \textbf{8:00am--1:00pm} \\
\hline
\rowcolor{c3}\tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} & \tiny\textbf{\B{যোহর}} \textbf{1:20--2:00pm} \\
\hline
\rowcolor{c7}\tiny Afternoon & \tiny Afternoon & \tiny Afternoon & \tiny Afternoon & \tiny Afternoon & \tiny Afternoon & \tiny Afternoon \\
\hline
\rowcolor{c8}\tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Lunch,Shower \textbf{2:00--3:00pm} & \tiny Self Study \textbf{2:00--3:00pm} \\
\hline
\rowcolor{c9}\tiny\textbf{3:00--4:00pm}: \B{শাহিন স্যার} & \tiny\textbf{3:00--4:00pm}: \B{নুর আলম স্যার} & \tiny\textbf{3:00--4:00pm}: \B{শাহিন স্যার} & \tiny\textbf{3:00--4:00pm}: \B{নুর আলম স্যার} & \tiny\textbf{3:00--4:00pm}: \B{শাহিন স্যার} & \tiny\textbf{3:00--4:00pm}: \B{নুর আলম স্যার} & \tiny Self Study \\
\hline
\rowcolor{c10}\tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} & \tiny Rest,Snack \textbf{4:00--5:00pm} \\
\hline
\rowcolor{c3}\tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} & \tiny\textbf{\B{আসর}} \textbf{5:00--5:15pm} \\
\hline
\rowcolor{c11}\tiny\textbf{5:15--6:00pm}: \B{মোরসালিন স্যার} & \tiny Self Study & \tiny\textbf{5:15--6:00pm}: \B{মোরসালিন স্যার} & \tiny Self Study & \tiny\textbf{5:15--6:00pm}: \B{মোরসালিন স্যার} & \tiny Self Study & \tiny Self Study \\
\hline
\rowcolor{c12}\tiny Self Study & \tiny\textbf{5:00--6:00pm}: \B{হেদায়েত স্যার} & \tiny Self Study & \tiny\textbf{5:00--6:00pm}: \B{হেদায়েত স্যার} & \tiny Self Study & \tiny\textbf{5:00--6:00pm}: \B{হেদায়েত স্যার} & \tiny Self Study \\
\hline
\rowcolor{c1}\tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} & \tiny Move,Eat,Reset \textbf{6:00--6:30pm} \\
\hline
\rowcolor{c3}\tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} & \tiny\textbf{\B{মাগরিব}} \textbf{6:50--7:10pm} \\
\hline
\rowcolor{c8}\tiny Evening & \tiny Evening & \tiny Evening & \tiny Evening & \tiny Evening & \tiny Evening & \tiny Evening \\
\hline
\rowcolor{c9}\tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} & \tiny SS4 \textbf{7:10--10:10pm} \\
\hline
\rowcolor{c3}\tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} & \tiny\textbf{\B{এশা}} \textbf{8:45--9:10pm} \\
\hline
\rowcolor{c10}\tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} & \tiny Eat,Move \textbf{10:10--11:20pm} \\
\hline
\rowcolor{c11}\tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} & \tiny SS5 \textbf{10:10--11:20pm} \\
\hline
\rowcolor{c12}\tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} & \tiny Go to Bed \textbf{11:20pm} \\
\hline
\end{tabularx}

\vspace{0.5pt}

\begin{itemize}[leftmargin=1em, itemsep=0.5pt, topsep=0pt, label=\textbullet, font=\tiny]

\item SS1 -- Study Session 1: \textbf{2 hours NO BREAK deep focused study.} Study hardest subjects. Maximum 2 different topics. \B{কঠিনতম বিষয়:} Higher Math 1st Paper (1hr) + Physics 1st Paper (1hr).

\item SS2 -- Study Session 2: \textbf{5 hours study with 5 to 15 minutes break after each cycle.} Cycle time can be 1 hour 30 minutes to 25 minutes. First cycle medium difficulty. Second cycle RESERVED FOR MODEL QUESTION SOLVE.

\item SS4 -- Study Session 4: \textbf{3 hours study with max 3 breaks.} Study new topics. Example: 1hr 30min+15min break+50min+5min break+30min.

\item SS5 -- Study Session 5: \textbf{1 hour 10 minute study. No break.} Revise whole day. \B{ইংরেজী ১ম পত্র} (30 min) + \B{ইংরেজী ২য় পত্র} (30 min) + 10 min scan.

\end{itemize}

\vspace{0pt}

\noindent\textbf{\tiny Day-wise Schedule:}

\vspace{0.3pt}

\begin{itemize}[leftmargin=1em, itemsep=0pt, topsep=0pt, label=$\triangleright$, font=\tiny]

\item \textbf{Saturday:} SS1: \B{পদার্থবিজ্ঞান ১ম পত্র} \quad SS2: \B{রসায়ন ১ম পত্র} \quad SS4: \B{উচ্চতর গণিত ১ম পত্র} (1.5hr) + \B{তথ্য ও যোগাযোগ প্রযুক্তি} (1.5hr)

\item \textbf{Sunday:} SS1: \B{উচ্চতর গণিত ২য় পত্র} \quad SS2: \B{জীববিজ্ঞান ১ম পত্র} \quad SS4: \B{পদার্থবিজ্ঞান ২য় পত্র} (2hr) + \B{বাংলা ১ম পত্র} (1hr)

\item \textbf{Monday:} SS1: \B{রসায়ন ২য় পত্র} \quad SS2: \B{পদার্থবিজ্ঞান ১ম পত্র} \quad SS4: \B{জীববিজ্ঞান ২য় পত্র} (2hr) + \B{ইংরেজী ১ম পত্র} (30min) + \B{ইংরেজী ২য় পত্র} (30min)

\item \textbf{Tuesday:} SS1: \B{উচ্চতর গণিত ১ম পত্র} \quad SS2: \B{রসায়ন ২য় পত্র} \quad SS4: \B{পদার্থবিজ্ঞান ২য় পত্র} (2hr) + \B{বাংলা ২য় পত্র} (1hr)

\item \textbf{Wednesday:} SS1: \B{জীববিজ্ঞান ২য় পত্র} \quad SS2: \B{উচ্চতর গণিত ২য় পত্র} \quad SS4: \B{রসায়ন ১ম পত্র} (1.5hr) + \B{তথ্য ও যোগাযোগ প্রযুক্তি} (1.5hr)

\item \textbf{Thursday:} SS1: \B{পদার্থবিজ্ঞান ২য় পত্র} \quad SS2: \B{জীববিজ্ঞান ১ম পত্র} \quad SS4: \B{উচ্চতর গণিত ২য় পত্র} (2hr) + \B{ইংরেজী ১ম পত্র} (30min) + \B{ইংরেজী ২য় পত্র} (30min)

\item \textbf{Friday:} \textbf{MEGA REVIEW DAY (No Tuitions).} SS1: Weekly Weakest Topic \quad SS2: Full Board Paper Mock Exam \quad SS4: Backlog Clearance + \B{বাংলা} Fast Revision

\end{itemize}

\vspace{0pt}

\begin{itemize}[leftmargin=1em, itemsep=0pt, topsep=0pt, label=$\triangleright$, font=\tiny]

\item Total Study Time: \textasciitilde{}12.5 hours/day. 1 Cycle $\leq$ 1hr 30min. No break $>$ 15 min. No cycle $<$ 25 min.

\item Break must not be used for mobile phone. Just rest with eyes closed if needed.

\item Commit to this routine for at least \textbf{22 days} consecutively. No rest days. Emergency: SS5 of Friday can be skipped.

\item Tuition Schedule: \B{শাহিন স্যার} Physics (Sat, Mon, Wed 3--4pm), \B{মোরসালিন স্যার} H.Math (Sat, Mon, Wed 5:15--6pm), \B{নুর আলম স্যার} English (Sun, Tue, Thu 3--4pm), \B{হেদায়েত স্যার} Chemistry (Sun, Tue, Thu 5--6pm).

\item \textbf{5 Daily Prayers:} \B{ফজর} 4:30--4:50am | \B{যোহর} 1:20--2:00pm | \B{আসর} 5:00--5:15pm | \B{মাগরিব} 6:50--7:10pm | \B{এশা} 8:45--9:10pm

\end{itemize}

\vspace{0.5pt}

\begin{center}
\makebox[5cm]{\hrulefill}\\[1pt]
{\tiny Your Signature (With Date)}
\end{center}

\end{document}
"""

with open("maxdoc.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode

run("apt update -qq --allow-unauthenticated 2>/dev/null; apt install -y texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-lang-other fonts-noto-core fonts-noto-extra fonts-liberation 2>/dev/null")
run("fc-cache -fv 2>/dev/null")
run("xelatex -interaction=nonstopmode maxdoc.tex")
run("xelatex -interaction=nonstopmode maxdoc.tex")

print("PDF ready:", os.path.exists("maxdoc.pdf"))
