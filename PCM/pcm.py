import subprocess, os, shutil, urllib.request, hashlib

tex_content = r"""\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage{mathtools}
\usepackage{newunicodechar}
\usepackage[margin=1.05cm, top=1.15cm, bottom=1.45cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage{array}
\usepackage{ragged2e}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{colortbl}
\usepackage{adjustbox}
\usepackage{needspace}
\usepackage{graphicx}
\usepackage{balance}
\usepackage[protrusion=false]{microtype}
\usepackage{tikz}
\usepackage{ucharclasses}
\usepackage{fancyhdr}
\usepackage[hidelinks,bookmarks=false]{hyperref}

\usetikzlibrary{arrows.meta,calc,shadings,decorations.pathmorphing,decorations.pathreplacing,patterns,3d,perspective,shapes.geometric,shapes.misc,fadings}

% ---------- global tuning ----------
\setlength{\arrayrulewidth}{0.3pt}
\setlength{\emergencystretch}{30pt}
\hbadness=99999
\vbadness=99999
\hfuzz=2pt
\tolerance=9999
\sloppy
\raggedcolumns
\setlength{\overfullrule}{0pt}
\allowdisplaybreaks[4]
\defaultfontfeatures{Ligatures=TeX}

% ---------- fonts ----------
\setmainfont{Latin Modern Roman}
\newfontfamily\lat[Ligatures=TeX]{Latin Modern Roman}
\newfontfamily\mathfallback{Latin Modern Roman}
\newfontfamily\bn[
  Path=./fonts/,
  Extension=.ttf,
  Script=Bengali,
  Renderer=HarfBuzz,
  Ligatures=TeX,
  BoldFeatures={FakeBold=2.6},
  ItalicFeatures={FakeSlant=0.12},
  BoldItalicFeatures={FakeBold=2.6,FakeSlant=0.12}
]{NotoSerifBengali-Regular}

\newunicodechar{°}{\ensuremath{^\circ}}

\setTransitionTo{Bengali}{\begingroup\bn}
\setTransitionFrom{Bengali}{\endgroup}

% ---------- colours ----------
\definecolor{sectionbg}{RGB}{65,65,65}
\definecolor{subsecbg}{RGB}{85,85,85}
\definecolor{tblhdr}{RGB}{210,224,242}
\definecolor{tblalt}{RGB}{245,247,250}
\definecolor{p1bg}{RGB}{20,60,120}
\definecolor{p2bg}{RGB}{0,0,0}
\definecolor{diagbg}{RGB}{246,246,250}
\definecolor{coverdeep}{RGB}{16,35,72}
\definecolor{coveracc}{RGB}{212,160,52}
\definecolor{inkgrey}{RGB}{60,60,60}
% ---- Smart Formula Encyclopedia cover palette ----
\definecolor{a360purple}{RGB}{122,40,142}
\definecolor{a360purpled}{RGB}{84,26,110}
\definecolor{a360red}{RGB}{206,30,52}
\definecolor{a360navy}{RGB}{30,40,92}
\definecolor{a360gold}{RGB}{214,170,66}
\definecolor{a360goldhi}{RGB}{246,216,134}
\definecolor{a360goldlo}{RGB}{150,108,30}
\definecolor{deeppur}{RGB}{40,18,70}
\definecolor{deeppur2}{RGB}{62,26,98}
\definecolor{hexpur}{RGB}{78,30,96}
\definecolor{hexpurd}{RGB}{44,16,62}
\definecolor{lightbg}{RGB}{245,245,249}

% ---------- robust Bengali wrapper (works in math + text) ----------
\newcommand{\B}[1]{\ifmmode\mbox{\bn #1}\else{\bn #1}\fi}
\newcommand{\LAT}[1]{{\lat #1}}
\newcommand{\srcnote}{\textsuperscript{{\lat\tiny BP}}}
\newcommand{\divider}{\par\vspace{1.5pt}\noindent\textcolor{black!22}{\rule{\linewidth}{0.3pt}}\par\vspace{1.5pt}}

% ---------- footer: book title left, page number right ----------
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyfoot[L]{\footnotesize\itshape Smart Formula Encyclopedia}
\fancyfoot[R]{\footnotesize\bfseries\thepage}
\fancypagestyle{plain}{%
  \fancyhf{}\renewcommand{\headrulewidth}{0pt}\renewcommand{\footrulewidth}{0.4pt}%
  \fancyfoot[L]{\footnotesize\itshape Smart Formula Encyclopedia}%
  \fancyfoot[R]{\footnotesize\bfseries\thepage}}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{9pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{1.2pt}

% ================= per-subject command packs =================
% PHYSICS pack
\newcommand{\setupPHYS}{%
  \setlength{\columnsep}{8pt}\setlength{\columnseprule}{0.3pt}\setlength{\parskip}{0.8pt}%
  \setlist[enumerate]{nosep,leftmargin=*,topsep=0pt}%
  \setlist[itemize]{nosep,leftmargin=0pt,topsep=0pt,label={},itemsep=0pt,parsep=0pt}%
  \renewcommand{\arraystretch}{1.13}\setlength{\tabcolsep}{1.5pt}%
  \renewcommand{\itm}[1]{\par\noindent\textbf{{\lat ##1.}}\;}%
  \renewcommand{\sub}[1]{\textbf{({\lat ##1})}}%
  \renewcommand{\chsec}[1]{\par\Needspace{6\baselineskip}\vspace{2pt}\noindent
    \colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering{\color{white}\B{\small\bfseries ##1}}}}%
    \addcontentsline{toc}{subsection}{##1}\vspace{1pt}\par}%
  \renewcommand{\chsub}[2]{\par\vspace{2pt}\noindent
    \colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{{\color{white}\LAT{\bfseries\footnotesize ##1}\hspace{3pt}\B{\bfseries\footnotesize ##2}}}}\vspace{1pt}\par}%
}
% CHEMISTRY pack
\newcommand{\setupCHEM}{%
  \setlength{\columnsep}{9pt}\setlength{\columnseprule}{0.3pt}\setlength{\parskip}{2pt}%
  \setlist[enumerate]{leftmargin=*,topsep=2pt,itemsep=1pt,parsep=0pt,partopsep=0pt}%
  \setlist[itemize]{leftmargin=14pt,topsep=2pt,itemsep=1pt,parsep=0pt,partopsep=0pt,label={\lat\textbullet}}%
  \renewcommand{\arraystretch}{1.3}%
  \let\oldtabular\tabular\let\endoldtabular\endtabular
  \RenewDocumentEnvironment{tabular}{m}{\par\smallskip\begin{center}\scriptsize\renewcommand{\arraystretch}{1.3}\setlength{\tabcolsep}{3pt}\begin{adjustbox}{max width=\linewidth}\oldtabular{##1}}{\endoldtabular\end{adjustbox}\end{center}\smallskip\par}%
  \renewcommand{\itm}[1]{\textbf{{\lat ##1.}}\;}%
  \renewcommand{\sub}[1]{\textbf{({\lat ##1})}\;}%
  \renewcommand{\chsec}[1]{\par\Needspace{7\baselineskip}\vspace{5pt}\noindent
    \colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\small\color{white}\B{##1}}}%
    \addcontentsline{toc}{subsection}{##1}\vspace{1pt}\par}%
  \renewcommand{\chsub}[2]{\par\Needspace{5\baselineskip}\vspace{4pt}\noindent
    \colorbox{subsecbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\bfseries\footnotesize\color{white}\;{\lat ##1} \B{##2}}}\vspace{1pt}\par}%
}
% HIGHER MATH pack
\newcommand{\setupMATH}{%
  \setlength{\columnsep}{15pt}\setlength{\columnseprule}{0pt}\setlength{\parskip}{2.2pt}%
  \raggedbottom
  \setlist[enumerate]{nosep,leftmargin=*,topsep=0pt}%
  \renewcommand{\arraystretch}{1.3}%
  \renewcommand{\itm}[1]{\par\addvspace{2.7pt}\noindent\textbf{##1.}\;\ignorespaces}%
  \renewcommand{\sub}[1]{\textbf{(##1)}\;\ignorespaces}%
  \renewcommand{\chsec}[1]{\par\addvspace{5pt}\noindent
    \colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\footnotesize\color{white}\B{##1}}}%
    \addcontentsline{toc}{subsection}{##1}\par\addvspace{3pt}\noindent\ignorespaces}%
  \renewcommand{\diag}[1]{\par\addvspace{3pt}\noindent\begin{adjustbox}{max width=.94\linewidth,center}##1\end{adjustbox}\par\addvspace{3pt}\noindent\ignorespaces}%
}
% placeholder definitions so \renewcommand targets exist
\newcommand{\itm}[1]{\textbf{#1.}\;}
\newcommand{\sub}[1]{\textbf{(#1)}\;}
\newcommand{\chsec}[1]{\par\noindent\textbf{#1}\par}
\newcommand{\chsub}[2]{\par\noindent\textbf{#1 #2}\par}
\newcommand{\diag}[1]{\par#1\par}
\newenvironment{safetable}{%
  \par\addvspace{3pt}\noindent\begingroup\tiny\setlength{\tabcolsep}{1.6pt}\renewcommand{\arraystretch}{1.3}%
  \begin{adjustbox}{max width=.94\linewidth,center}%
}{%
  \end{adjustbox}\endgroup\par\addvspace{3pt}\noindent\ignorespaces%
}

% ---------- decorative helpers ----------
\newcommand{\partpage}[4]{%
  % #1 number  #2 english  #3 bengali  #4 tagline
  \clearpage\thispagestyle{plain}%
  \begin{center}\vspace*{0.20\textheight}
  {\color{coveracc}\rule{3.2cm}{1.4pt}}\\[10pt]
  {\fontsize{20}{24}\selectfont\color{inkgrey}\bfseries PART #1}\\[14pt]
  {\fontsize{34}{40}\selectfont\color{coverdeep}\bfseries #2}\\[12pt]
  {\bn\fontsize{26}{32}\selectfont\color{coverdeep}\bfseries #3}\\[14pt]
  {\color{coveracc}\rule{3.2cm}{1.4pt}}\\[18pt]
  {\itshape\large\color{inkgrey} #4}
  \end{center}\vfill
  \clearpage}

\begin{document}
\begin{titlepage}
\thispagestyle{empty}
\begin{tikzpicture}[remember picture,overlay,shift={(current page.south west)},x=1cm,y=1cm,line cap=round,line join=round]
%==================== BACKGROUNDS ====================
\fill[lightbg] (0,0) rectangle (21,29.7);
% faint hexagon texture (top band)
\foreach \j in {0,...,3}{\foreach \i in {0,...,13}{
  \node[regular polygon,regular polygon sides=6,minimum size=0.95cm,draw=a360navy!7,line width=0.4pt,rotate=30] at ({0.6+1.55*\i+0.775*Mod(\j,2)},{29.2-0.86*\j}) {};}}
% bottom deep-purple region with diagonal top edge
\shade[top color=deeppur2,bottom color=deeppur] (0,0) -- (0,9.6) -- (21,6.4) -- (21,0) -- cycle;
\draw[a360gold,line width=1.1pt] (0,9.6) -- (21,6.4);
% faint hex texture inside purple (bottom-right)
\foreach \j in {0,...,5}{\foreach \i in {0,...,7}{
  \node[regular polygon,regular polygon sides=6,minimum size=0.85cm,draw=white!10,line width=0.35pt,rotate=30] at ({13.4+1.4*\i+0.7*Mod(\j,2)},{5.4-0.78*\j}) {};}}

%==================== A360 BADGE (top-left) ====================
\begin{scope}[shift={(1.7,27.0)}]
 \fill[a360purpled] (0,0) -- (3.15,0) -- (3.5,0.66) -- (0.35,0.66) -- cycle;
 \node[white,font=\bfseries] at (1.78,0.34) {\fontsize{22}{22}\selectfont A360};
 \fill[a360red] (0.2,-0.78) -- (3.36,-0.78) -- (3.7,-0.12) -- (0.55,-0.12) -- cycle;
 \node[white,font=\bfseries] at (1.98,-0.45) {\fontsize{12.5}{12.5}\selectfont PROGRAMMING};
 \fill[a360purpled] (3.62,0.0) -- (4.05,0.66) -- (4.34,0.66) -- (3.91,0.0) -- cycle;
 \fill[a360red] (4.0,-0.78) -- (4.36,-0.12) -- (4.62,-0.12) -- (4.26,-0.78) -- cycle;
\end{scope}

%==================== SUBJECT LIST (left) ====================
\begin{scope}[shift={(2.2,24.7)}]
 % physics atom
 \begin{scope}[shift={(0,0)}]
   \foreach \a in {0,60,120}{\draw[a360purple,line width=0.7pt,rotate around={\a:(0,0)}] (0,0) ellipse (0.34 and 0.13);}
   \fill[a360purple] (0,0) circle (0.055);
 \end{scope}
 \node[a360navy,anchor=west,font=\bfseries] at (0.65,0) {\fontsize{15}{16}\selectfont PHYSICS};
 \draw[a360navy!22,line width=0.5pt] (-0.45,-0.5)--(4.4,-0.5);
 % chemistry flask
 \begin{scope}[shift={(0,-1.0)}]
   \draw[a360red,line width=0.8pt] (-0.12,0.34)--(-0.12,0.06)--(-0.32,-0.3)--(0.32,-0.3)--(0.12,0.06)--(0.12,0.34);
   \draw[a360red,line width=0.8pt] (-0.18,0.34)--(0.18,0.34);
   \draw[a360red,line width=0.7pt] (-0.22,-0.12)--(0.22,-0.12);
 \end{scope}
 \node[a360navy,anchor=west,font=\bfseries] at (0.65,-1.0) {\fontsize{15}{16}\selectfont CHEMISTRY};
 \draw[a360navy!22,line width=0.5pt] (-0.45,-1.5)--(4.4,-1.5);
 % math pi
 \node[a360navy] at (0,-2.0) {\fontsize{20}{20}\selectfont $\boldsymbol{\pi}$};
 \node[a360navy,anchor=west,font=\bfseries] at (0.65,-2.0) {\fontsize{15}{16}\selectfont MATH};
\end{scope}

%==================== TITLE BLOCK (right) ====================
\node[anchor=west,a360purple] at (8.4,26.9) {\fontsize{60}{60}\selectfont\bfseries SMART};
\node[anchor=west,a360red]    at (8.4,24.2) {\fontsize{60}{60}\selectfont\bfseries FORMULA};
\node[anchor=west,a360navy]   at (8.45,22.05){\fontsize{27}{27}\selectfont\bfseries E\,N\,C\,Y\,C\,L\,O\,P\,E\,D\,I\,A};
% icon tiles (2x2) top right
\foreach \tx/\ty/\cl/\ic in {17.9/27.5/a360purple/{$\sqrt{x}$}, 19.15/27.5/a360red/{\,$\equiv$\,}, 17.9/26.25/a360navy/{}, 19.15/26.25/a360purpled/{}}{
  \fill[\cl,rounded corners=3pt] (\tx-0.55,\ty-0.55) rectangle (\tx+0.55,\ty+0.55);
  \node[white,font=\bfseries] at (\tx,\ty) {\ic};}
% atom icon tile (bottom-left tile)
\begin{scope}[shift={(17.9,26.25)}]
  \foreach \a in {0,60,120}{\draw[white,line width=0.7pt,rotate around={\a:(0,0)}] (0,0) ellipse (0.34 and 0.13);}
  \fill[white] (0,0) circle (0.05);
\end{scope}
% flask icon tile (bottom-right tile)
\begin{scope}[shift={(19.15,26.25)}]
  \draw[white,line width=0.8pt] (-0.12,0.32)--(-0.12,0.05)--(-0.3,-0.28)--(0.3,-0.28)--(0.12,0.05)--(0.12,0.32);
  \draw[white,line width=0.8pt] (-0.17,0.32)--(0.17,0.32);
\end{scope}
% red divider + tagline
\fill[a360red] (8.45,21.35) circle (0.05);
\draw[a360red,line width=1pt] (8.6,21.35)--(15.9,21.35);
\fill[a360red] (16.05,21.35) circle (0.05);
\node[anchor=west,a360navy,font=\bfseries] at (8.45,20.75) {\fontsize{15}{16}\selectfont ONE BOOK.\ \ ENDLESS SOLUTIONS.};

%==================== CENTRAL GOLD HEXAGON ====================
\def\hx{7.7} \def\hy{14.0}
\node[regular polygon,regular polygon sides=6,minimum size=13.0cm,fill=a360goldlo] at (\hx,\hy) {};
\node[regular polygon,regular polygon sides=6,minimum size=12.6cm,fill=a360goldhi] at (\hx,\hy) {};
\node[regular polygon,regular polygon sides=6,minimum size=12.0cm,fill=a360gold] at (\hx,\hy) {};
\node[regular polygon,regular polygon sides=6,minimum size=11.1cm,fill=a360goldlo] at (\hx,\hy) {};
\node[regular polygon,regular polygon sides=6,minimum size=10.7cm,inner sep=0pt] (hexin) at (\hx,\hy) {};
\begin{scope}
  \clip (hexin.corner 1)--(hexin.corner 2)--(hexin.corner 3)--(hexin.corner 4)--(hexin.corner 5)--(hexin.corner 6)--cycle;
  \shade[top color=hexpur,bottom color=hexpurd] (\hx-6,\hy-6) rectangle (\hx+6,\hy+6);
  % scattered formulas (handwritten-style, white) -- kept inside hex bounds
  \node[white,opacity=0.92] at (\hx-1.7,\hy+3.8) {\footnotesize $V=\tfrac{4}{3}\pi r^{3}$};
  \node[white,opacity=0.92] at (\hx+1.7,\hy+3.8) {\footnotesize $E=mc^{2}$};
  \node[white,opacity=0.92] at (\hx-0.1,\hy+2.9) {\footnotesize $\sin^{2}\theta+\cos^{2}\theta=1$};
  \node[white,opacity=0.92] at (\hx-2.6,\hy+2.0) {\footnotesize $F=ma$};
  \node[white,opacity=0.92] at (\hx+2.0,\hy+2.0) {\footnotesize $a^{2}+b^{2}=c^{2}$};
  \node[white,opacity=0.92] at (\hx-2.6,\hy+0.9) {\footnotesize $x=\dfrac{-b\pm\sqrt{b^{2}-4ac}}{2a}$};
  \node[white,opacity=0.92] at (\hx+2.6,\hy+0.9) {\footnotesize $PV=nRT$};
  \node[white,opacity=0.92] at (\hx+3.4,\hy+0.0) {\footnotesize $V=IR$};
  \node[white,opacity=0.92] at (\hx-2.7,\hy-0.9) {\footnotesize $\displaystyle\sum_{i=1}^{n} i=\tfrac{n(n+1)}{2}$};
  \node[white,opacity=0.92] at (\hx+2.4,\hy-0.9) {\footnotesize $\displaystyle\int x\,dx=\tfrac{x^{2}}{2}+C$};
  \node[white,opacity=0.92] at (\hx-2.4,\hy-2.0) {\footnotesize $\Delta E=h\nu$};
  \node[white,opacity=0.92] at (\hx+2.2,\hy-2.0) {\footnotesize $y=A\sin\omega t$};
  \node[white,opacity=0.92] at (\hx-0.2,\hy-3.1) {\footnotesize $\dfrac{\sin A}{a}=\dfrac{\sin B}{b}=\dfrac{\sin C}{c}$};
  % benzene ring
  \node[regular polygon,regular polygon sides=6,minimum size=1.0cm,draw=white,line width=0.6pt,opacity=0.8] (bz) at (\hx-3.0,\hy+2.9) {};
  \draw[white,opacity=0.8,line width=0.5pt] (bz.center) circle (0.24);
  % atom
  \begin{scope}[shift={(\hx-3.5,\hy-1.2)},opacity=0.8]
    \foreach \a in {0,60,120}{\draw[white,line width=0.5pt,rotate around={\a:(0,0)}] (0,0) ellipse (0.5 and 0.18);}
    \fill[white] (0,0) circle (0.06);
  \end{scope}
  % globe
  \draw[white,opacity=0.8,line width=0.6pt] (\hx-0.1,\hy+0.0) circle (0.5);
  \draw[white,opacity=0.8,line width=0.4pt] (\hx-0.1,\hy+0.0) ellipse (0.2 and 0.5);
  \draw[white,opacity=0.8,line width=0.4pt] (\hx-0.6,\hy+0.0)--(\hx+0.4,\hy+0.0);
  % small triangle
  \draw[white,opacity=0.8,line width=0.5pt] (\hx+2.7,\hy-0.7)--(\hx+3.5,\hy-0.7)--(\hx+3.5,\hy-0.05)--cycle;
\end{scope}

%==================== GOLD SEAL (right) ====================
\begin{scope}[shift={(17.9,12.1)}]
  \foreach \a in {0,12,...,348}{\fill[a360gold] (\a:1.78) circle (0.155);}
  \fill[a360goldhi] (0,0) circle (1.72);
  \fill[a360navy] (0,0) circle (1.46);
  \draw[a360gold,line width=1pt] (0,0) circle (1.46);
  \foreach \a in {-24,0,24}{\node[a360gold] at (\a+90:1.05) {\footnotesize$\star$};}
  \node[a360goldhi,font=\bfseries] at (0,0.42) {\scriptsize ALL ESSENTIAL};
  \node[white,font=\bfseries] at (0,0.02) {\fontsize{15}{15}\selectfont FORMULAS};
  \node[a360goldhi,font=\bfseries] at (0,-0.42) {\scriptsize AT YOUR};
  \node[a360goldhi,font=\bfseries] at (0,-0.78) {\scriptsize FINGERTIPS};
  \node[a360gold] at (0,-1.08) {\tiny$\star$};
\end{scope}

%==================== AUTHOR (bottom purple, left) ====================
% feather in gold ring
\begin{scope}[shift={(2.2,5.0)}]
  \draw[a360gold,line width=1.2pt] (0,0) circle (0.78);
  \draw[a360goldhi,line width=1pt] (-0.35,-0.4) .. controls (0.0,0.1) and (0.25,0.35) .. (0.42,0.5);
  \draw[a360goldhi,line width=2.4pt] (-0.36,-0.42) -- (-0.18,-0.24);
  \foreach \t in {0.15,0.3,0.45,0.6,0.75}{
    \draw[a360goldhi,line width=0.6pt] ($(-0.35,-0.4)!\t!(0.42,0.5)$) -- ++(0.22,-0.05);}
\end{scope}
\node[anchor=west,white,font=\bfseries] at (3.3,5.45) {\fontsize{13}{13}\selectfont WRITTEN BY};
\node[anchor=west,white,font=\bfseries] at (3.25,4.7) {\fontsize{25}{25}\selectfont Abir Arafat Chawdhury};
\draw[a360gold,line width=0.9pt] (3.3,4.05)--(9.6,4.05);

%==================== FEATURE BADGES (bottom row) ====================
\foreach \bx/\lbla/\lblb in {3.0/QUICK/REFERENCE, 7.1/EASY TO/UNDERSTAND, 11.2/BOOST/CONCEPTS, 15.3/EXAM/FOCUSED}{
  \draw[a360gold,line width=1pt] (\bx,1.95) circle (0.5);
  \node[white,anchor=center] at (\bx,1.0) {\scriptsize\bfseries \lbla};
  \node[white,anchor=center] at (\bx,0.62) {\scriptsize\bfseries \lblb};
}
% badge icons
\node[a360goldhi] at (3.0,1.95) {\large$\odot$};                                   % target
\draw[a360goldhi,line width=0.9pt] (6.78,1.78)--(6.78,2.12)--(7.42,2.12)--(7.42,1.78)--cycle;
\draw[a360goldhi,line width=0.7pt] (7.1,1.78)--(7.1,2.12);                          % book
\begin{scope}[shift={(11.2,1.95)}]                                                 % brain
  \draw[a360goldhi,line width=0.8pt] (0,0.28) .. controls (-0.45,0.28) and (-0.45,-0.28) .. (0,-0.28);
  \draw[a360goldhi,line width=0.8pt] (0,0.28) .. controls (0.45,0.28) and (0.45,-0.28) .. (0,-0.28);
  \draw[a360goldhi,line width=0.6pt] (0,0.28)--(0,-0.28);
\end{scope}
\node[a360goldhi] at (15.3,1.95) {\large$\checkmark$};                              % check
% separators
\foreach \sx in {5.05,9.15,13.25}{\draw[white!35,line width=0.5pt] (\sx,0.55)--(\sx,2.45);}

%==================== LIGHTBULB (bottom-right) ====================
\begin{scope}[shift={(18.6,4.5)}]
  % rays
  \foreach \a in {35,55,75,95,115,135,155}{\draw[a360gold,line width=1pt] (\a:1.35)--(\a:1.75);}
  % bulb
  \draw[a360gold,line width=1.3pt] (0,0.2) circle (1.05);
  % brain filament
  \draw[a360gold,line width=0.9pt] (0,0.85) .. controls (-0.7,0.85) and (-0.7,-0.05) .. (0,-0.1);
  \draw[a360gold,line width=0.9pt] (0,0.85) .. controls (0.7,0.85) and (0.7,-0.05) .. (0,-0.1);
  \draw[a360gold,line width=0.7pt] (0,0.85)--(0,-0.1);
  \draw[a360gold,line width=0.7pt] (-0.35,0.55) .. controls (-0.15,0.35) .. (-0.35,0.15);
  \draw[a360gold,line width=0.7pt] (0.35,0.55) .. controls (0.15,0.35) .. (0.35,0.15);
  % base
  \draw[a360gold,line width=1.1pt] (-0.4,-0.78) -- (0.4,-0.78);
  \draw[a360gold,line width=1.1pt] (-0.34,-1.02) -- (0.34,-1.02);
  \draw[a360gold,line width=1.1pt] (-0.28,-1.26) -- (0.28,-1.26);
  \draw[a360gold,line width=1pt] (-0.4,-0.78)--(-0.34,-0.55)--(0.34,-0.55)--(0.4,-0.78);
  \draw[a360gold,line width=1pt] (-0.2,-1.26) .. controls (-0.1,-1.5) and (0.1,-1.5) .. (0.2,-1.26);
\end{scope}
\end{tikzpicture}
\end{titlepage}

\clearpage\thispagestyle{plain}
\begin{center}
{\color{coverdeep}\fontsize{26}{30}\selectfont\bfseries Introduction}\\[4pt]
{\color{coveracc}\rule{4cm}{1.2pt}}
\end{center}
\vspace{10pt}
{\large\setlength{\parskip}{8pt}
\noindent I'm \textbf{Abir Arafat Chawdhury}, a visionary entrepreneur and tech
enthusiast leading the charge as \textbf{CEO and Founder of Abir X Official
Community}. I craft innovative web projects and bring clients' visions to life
through freelancing on \textbf{Upwork} and \textbf{Fiverr}. My passion for
coding fuels my mission to create smarter, cutting-edge solutions that redefine
the digital landscape.

\noindent This book --- the \textbf{Smart Formula Encyclopedia} --- is my effort
to bring together every essential formula, definition, and diagram of
\textbf{Physics}, \textbf{Chemistry}, and \textbf{Higher Mathematics} into one
clean, exam-ready reference. Each subject is organised paper by paper and chapter
by chapter, so revision before the final exam becomes fast, focused and stress-free.

\noindent Bengali and English notation sit side by side exactly the way they
appear in the HSC syllabus, with carefully typeset mathematics and figures. Use
the index on the next page to jump straight to any chapter. Best of luck for your
preparation.
\par}
\vfill
\begin{flushright}{\itshape\color{inkgrey}--- Abir Arafat Chawdhury}\end{flushright}
\clearpage

\clearpage\thispagestyle{plain}
\begingroup
\setcounter{tocdepth}{2}
\begin{center}{\color{coverdeep}\fontsize{24}{28}\selectfont\bfseries Index}\\[3pt]{\color{coveracc}\rule{4cm}{1.2pt}}\end{center}
\vspace{6pt}
\makeatletter
\@starttoc{toc}
\makeatother
\endgroup
\clearpage

\partpage{I}{Physics}{পদার্থবিজ্ঞান}{Complete formulas, definitions \& diagrams --- Paper 1 \& Paper 2}
\phantomsection\addcontentsline{toc}{section}{Physics (পদার্থবিজ্ঞান)}
\begingroup
\setupPHYS




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


\par\endgroup
\clearpage

\partpage{II}{Chemistry}{রসায়ন}{Concept maps \& formulas --- Paper 1 \& Paper 2}
\phantomsection\addcontentsline{toc}{section}{Chemistry (রসায়ন)}
\begingroup
\setupCHEM




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


\par\endgroup
\clearpage

\partpage{III}{Higher Mathematics}{উচ্চতর গণিত}{Essential formulas --- Paper 1 \& Paper 2}
\phantomsection\addcontentsline{toc}{section}{Higher Mathematics (উচ্চতর গণিত)}
\begingroup
\setupMATH





\vspace{2pt}

\begin{multicols}{2}\footnotesize

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}{\bn প্রথম পত্র}}}
\vspace{2pt}\par
\chsec{অধ্যায়-১: ম্যাট্রিক্স ও নির্ণায়ক}

\itm{1} \sub{i} \B{যদি} $A=[a_{ij}]_{n\times n}$ \B{একটি অব্যতিক্রমী ম্যাট্রিক্স হয় তবে,}

$A^{-1}=\dfrac{1}{|A|}\operatorname{adj}A$

\sub{ii} \B{তিন চলকবিশিষ্ট একঘাত সমীকরণ জোট:}

$a_1x+b_1y+c_1z=d_1,\; a_2x+b_2y+c_2z=d_2,\; a_3x+b_3y+c_3z=d_3$

\B{এর সমাধান (ক্রেমারের নিয়ম):}

\vspace{2pt}

$D=\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}\neq0,\quad
D_x=\begin{vmatrix}d_1&b_1&c_1\\d_2&b_2&c_2\\d_3&b_3&c_3\end{vmatrix}$

$D_y=\begin{vmatrix}a_1&d_1&c_1\\a_2&d_2&c_2\\a_3&d_3&c_3\end{vmatrix},\quad
D_z=\begin{vmatrix}a_1&b_1&d_1\\a_2&b_2&d_2\\a_3&b_3&d_3\end{vmatrix}$
\diag{\begin{tikzpicture}[scale=0.55,every node/.style={font=\scriptsize}]
\draw[->] (-0.4,0)--(3.6,0) node[right]{$x$};
\draw[->] (0,-0.4)--(0,3.0) node[above]{$y$};
\draw[thick,blue] (-0.2,2.6)--(3.2,0.2);
\draw[thick,red] (-0.2,0.4)--(3.2,2.4);
\draw[thick,teal] (0.5,-0.2)--(2.4,2.6);
\filldraw (1.45,1.35) circle (1.4pt) node[above right,font=\tiny]{$(x,y,z)$};
\node[blue,font=\tiny] at (3.3,0.4){$L_1$};
\node[red,font=\tiny] at (3.3,2.5){$L_2$};
\node[teal,font=\tiny] at (2.55,2.6){$L_3$};
\end{tikzpicture}}

\B{এবং} $x=\dfrac{D_x}{D},\quad y=\dfrac{D_y}{D},\quad z=\dfrac{D_z}{D}$

\itm{2} \B{ম্যাট্রিক্সের ট্রেস (Trace):} $A$ \B{একটি বর্গ ম্যাট্রিক্স হলে এর প্রধান বা মুখ্য কর্ণের ভুক্তিগুলোর সমষ্টিকে ম্যাট্রিক্সটির ট্রেস বলা হয়{\bn ।}}

$\operatorname{Tr}(A) = a_{11} + a_{22} + \dots + a_{nn} = \sum_{i=1}^{n} a_{ii}$

\itm{3} \B{ম্যাট্রিক্সের গুণনযোগ্যতার শর্ত:} $A_{m \times n}$ \B{এবং} $B_{p \times q}$ \B{ম্যাট্রিক্সদ্বয় গুণনযোগ্য $(AB)$ হবে যদি ও কেবল যদি প্রথম ম্যাট্রিক্সের কলাম সংখ্যা ও দ্বিতীয় ম্যাট্রিক্সের সারী সংখ্যা সমান হয় অর্থাৎ} $n = p$ \B{হয়{\bn ।} উৎপন্ন নতুন ম্যাট্রিক্সের মাত্রা হবে} $m \times q$\B{{\bn ।}}

\itm{4} \B{বিভিন্ন প্রকার বিশেষ বর্গ ম্যাট্রিক্সের শর্তসমূহ:}

\sub{i} \B{প্রতিসম (Symmetric) ম্যাট্রিক্স:} $A^T = A$

\sub{ii} \B{বিপ্রতিসম বা বক্র-প্রতিসম (Skew-symmetric) ম্যাট্রিক্স:} $A^T = -A$\B{; এই ম্যাট্রিক্সের প্রধান কর্ণের ভুক্তিগুলো সর্বদা শূন্য $(0)$ হয়{\bn ।}}

\sub{iii} \B{সমঘাতী (Idempotent) ম্যাট্রিক্স:} $A^2 = A$

\sub{iv} \B{অভেদঘাতী (Involutory) ম্যাট্রিক্স:} $A^2 = I$

\sub{v} \B{শূন্যঘাতী (Nilpotent) ম্যাট্রিক্স:} $A^n = O$\B{; যেখানে $n$ হলো ম্যাট্রিক্সটির শূন্যঘাতী সূচক{\bn ।}}

\sub{vi} \B{লম্ব বা লম্বিক (Orthogonal) ম্যাট্রিক্স:} $A A^T = A^T A = I$

\itm{5} \B{রূপান্তরিত বা ট্রান্সপোজ (Transpose) ম্যাট্রিক্সের ধর্মাবলী:}

\sub{i} $(A^T)^T = A$

\sub{ii} $(A \pm B)^T = A^T \pm B^T$

\sub{iii} $(AB)^T = B^T A^T$ \B{(বিপরীতক্রম নিয়ম)}

\sub{iv} $(kA)^T = kA^T$\B{; যেখানে $k$ একটি স্কেলার বা ধ্রুবক{\bn ।}}

\itm{6} \B{ব্যতিক্রমী ও অব্যতিক্রমী ম্যাট্রিক্সের শর্ত:}

\sub{i} \B{ব্যতিক্রমী (Singular) ম্যাট্রিক্স:} \B{যদি কোনো বর্গ ম্যাট্রিক্সের নির্ণায়কের মান শূন্য হয় অর্থাৎ} $|A| = 0$ \B{হয়{\bn ।}}

\sub{ii} \B{অব্যতিক্রমী (Non-singular) excavation ম্যাট্রিক্স:} \B{যদি কোনো বর্গ ম্যাট্রিক্সের নির্ণায়কের মান শূন্য না হয় অর্থাৎ} $|A| \neq 0$ \B{হয়{\bn ।}}

\itm{7} \B{বিপরীত (Inverse) ম্যাট্রিক্সের ধর্মাবলী:}

\sub{i} $(A^{-1})^{-1} = A$

\sub{ii} $(AB)^{-1} = B^{-1} A^{-1}$

\sub{iii} $(A^T)^{-1} = (A^{-1})^T$

\sub{iv} $A \cdot A^{-1} = A^{-1} \cdot A = I$

\itm{8} \B{অনুবন্ধী বা অ্যাডজয়েন্ট (Adjoint) ম্যাট্রিক্সের ধর্মাবলী:}

\sub{i} $A \cdot \operatorname{adj}(A) = \operatorname{adj}(A) \cdot A = |A| I$

\sub{ii} $|\operatorname{adj}(A)| = |A|^{n-1}$\B{; যেখানে $n$ হলো $A$ ম্যাট্রিক্সের ক্রম $(n \times n)${\bn ।}}

\itm{9} \B{নির্ণায়কের অনুরাশি (Minor) ও সহগুণক (Cofactor):}

\sub{i} \B{অনুরাশি ($M_{ij}$):} \B{কোনো নির্ণায়কের $i$-তম সারী এবং $j$-তম কলামের ভুক্তিটি যে সারী ও কলামে অবস্থিত তা বাদ দিয়ে গঠিত উপ-নির্ণায়ক{\bn ।}}

\sub{ii} \B{সহগুণক ($A_{ij}$):} \B{উপযুক্ত চিহ্নযুক্ত অনুরাশিকে সহগুণক বলে অর্থাৎ,} $A_{ij} = (-1)^{i+j} M_{ij}$


\chsec{অধ্যায়-২: ভেক্টর}

\itm{1} $\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}$ \B{ভেক্টরের মান,} $|\vec{A}|=\sqrt{A_x^2+A_y^2+A_z^2}$
\diag{\begin{tikzpicture}[scale=0.85,every node/.style={font=\scriptsize}]
\coordinate (O) at (0,0);
\coordinate (A) at (2.6,0);
\coordinate (B) at (1.0,1.6);
\coordinate (C) at ($(A)+(B)$);
\draw[->,thick] (O)--(A) node[midway,below]{$\vec{u}$};
\draw[->,thick] (O)--(B) node[midway,above left]{$\vec{v}$};
\draw[dashed] (A)--(C);
\draw[dashed] (B)--(C);
\draw[->,very thick,red] (O)--(C) node[midway,sloped,above]{$\vec{u}+\vec{v}$};
\draw (0.55,0) arc (0:58:0.55);
\node at (30:0.78){$\alpha$};
\end{tikzpicture}}

\itm{2} $\vec{A}$ \B{ভেক্টরের দিকে একক ভেক্টর,} $\hat{\eta}=\dfrac{\vec{A}}{|\vec{A}|}$

\itm{3} \B{দুইটি ভেক্টর} $\vec{A}$ \B{ও} $\vec{B}$ \B{হলে, স্কেলার গুণন,}

$\vec{A}\cdot\vec{B}=|\vec{A}||\vec{B}|\cos\theta$\B{; $\theta$ ভেক্টর দুইটির মধ্যবর্তী কোণ{\bn ।}}

\itm{4} $\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}$ \B{ও} $\vec{B}=B_x\hat{i}+B_y\hat{j}+B_z\hat{k}$ \B{ভেক্টরের ভেক্টর বা ক্রসগুণন,}

\[
\vec{A}\times\vec{B}=\hat{\eta}|\vec{A}||\vec{B}|\sin\theta
=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\A_x&A_y&A_z\\B_x&B_y&B_z\end{vmatrix}
\]

\itm{5} $\vec{A}$ \B{ও} $\vec{B}$ \B{ভেক্টরের লম্বদিকে একক ভেক্টর,}

$\hat{\eta}=\pm\dfrac{\vec{A}\times\vec{B}}{|\vec{A}\times\vec{B}|}$

\itm{6} $\hat{i}\cdot\hat{i}=\hat{j}\cdot\hat{j}=\hat{k}\cdot\hat{k}=1$\B{;}
$\hat{i}\cdot\hat{j}=\hat{j}\cdot\hat{k}=\hat{k}\cdot\hat{i}=0$\B{;}
$\hat{i}\times\hat{i}=\hat{j}\times\hat{j}=\hat{k}\times\hat{k}=0$\B{;}
$\hat{i}\times\hat{j}=\hat{k}$, $\hat{j}\times\hat{k}=\hat{i}$, $\hat{k}\times\hat{i}=\hat{j}$,
$\hat{j}\times\hat{i}=-\hat{k}$, $\hat{k}\times\hat{j}=-\hat{i}$, $\hat{i}\times\hat{k}=-\hat{j}$

\itm{7} \sub{i} $\vec{A}$ \B{ও} $\vec{B}$ \B{ভেক্টরদ্বয় পরস্পর লম্ব হলে,} $\vec{A}\cdot\vec{B}=0$

\sub{ii} $\vec{A}$ \B{ও} $\vec{B}$ \B{ভেক্টরদ্বয় পরস্পর সমান্তরাল হলে,} $\vec{A}\times\vec{B}=0$

\itm{8} \sub{i} $\vec{A}$ \B{ভেক্টরের দিক বরাবর} $\vec{B}$ \B{ভেক্টরের উপাংশ}

$=(\hat{A}\cdot\vec{B})\hat{A}=\dfrac{(\vec{A}\cdot\vec{B})\vec{A}}{|\vec{A}|^2}$

\sub{ii} $\vec{B}$ \B{ভেক্টরের দিক বরাবর} $\vec{A}$ \B{ভেক্টরের উপাংশ}

$=(\hat{B}\cdot\vec{A})\hat{B}=\dfrac{(\vec{A}\cdot\vec{B})\vec{B}}{|\vec{B}|^2}$

\itm{9} \sub{i} $\vec{B}$ \B{ভেক্টরের উপর} $\vec{A}$ \B{ভেক্টরের লম্ব অভিক্ষেপ}

$=\dfrac{\vec{A}\cdot\vec{B}}{|\vec{B}|}$

\sub{ii} $\vec{A}$ \B{ভেক্টরের উপর} $\vec{B}$ \B{ভেক্টরের লম্ব অভিক্ষেপ}

$=\dfrac{\vec{A}\cdot\vec{B}}{|\vec{A}|}$

\itm{10} $\vec{A},\vec{B},\vec{C}$ \B{ভেক্টরত্রয় একই সমতলে অবস্থান করলে,}

$\vec{A}\cdot(\vec{B}\times\vec{C})=0$ \B{অর্থাৎ}

$\begin{vmatrix}A_1&A_2&A_3\\B_1&B_2&B_3\\C_1&C_2&C_3\end{vmatrix}=0$

\itm{11} \B{সামান্তরিকের ক্ষেত্রফল:}
\sub{i} \B{সন্নিহিত বাহুদ্বয়} $\vec{A}$ \B{ও} $\vec{B}$ \B{হলে, ক্ষেত্রফল} $=|\vec{A}\times\vec{B}|$
\sub{ii} \B{কর্ণদ্বয়} $\vec{d}_1$ \B{ও} $\vec{d}_2$ \B{হলে, ক্ষেত্রফল} $=\dfrac{1}{2}|\vec{d}_1\times\vec{d}_2|$
\diag{\begin{tikzpicture}[scale=0.85,every node/.style={font=\scriptsize}]
\coordinate (O) at (0,0);
\coordinate (A) at (2.8,0);
\coordinate (B) at (1.4,1.6);
\draw[->,thick] (O)--(A) node[midway,below]{$\vec{u}$};
\draw[->,thick] (O)--(B) node[midway,above left]{$\vec{v}$};
\draw[->,very thick,red] (B)--(A) node[midway,above right]{$\vec{u}-\vec{v}$};
\node at (O) [below left]{$O$};
\node at (A) [right]{$A$};
\node at (B) [above]{$B$};
\end{tikzpicture}}

\itm{12} \B{ত্রিভুজের ক্ষেত্রফল:}
\sub{i} \B{সন্নিহিত বাহুদ্বয়} $\vec{A}$ \B{ও} $\vec{B}$ \B{হলে, ক্ষেত্রফল} $=\dfrac{1}{2}|\vec{A}\times\vec{B}|$
\sub{ii} \B{শীর্ষবিন্দুত্রয়ের অবস্থান ভেক্টর} $\vec{a}, \vec{b}, \vec{c}$ \B{হলে, ক্ষেত্রফল} $=\dfrac{1}{2}|\vec{a}\times\vec{b}+\vec{b}\times\vec{c}+\vec{c}\times\vec{a}|$

\itm{13} \B{সামান্তরিকের সূত্র (বলবিদ্যা সংক্রান্ত):}
\B{যদি দুটি বল} $P$ \B{ও} $Q$ \B{পরস্পর} $\alpha$ \B{কোণে ক্রিয়া করে, তবে তাদের লব্ধি} $R$ \B{এবং লব্ধির দিক} $\theta$ \B{($P$ বলের সাথে):}
\[ R = \sqrt{P^2+Q^2+2PQ\cos\alpha} \]
\[ \tan\theta = \dfrac{Q\sin\alpha}{P+Q\cos\alpha} \]

\itm{14} \sub{i} \B{সর্বোচ্চ লব্ধি,} $R_{\max} = P+Q$ \B{; যখন} $\alpha = 0^\circ$
\diag{\begin{tikzpicture}[scale=0.9,every node/.style={font=\scriptsize}]
\coordinate (O) at (0,0);
\draw[->,thick] (O)--(0:1.7) node[right]{$\vec{P}$};
\draw[->,thick] (O)--(135:1.7) node[above left]{$\vec{Q}$};
\draw[->,thick] (O)--(245:1.7) node[below]{$\vec{R}$};
\draw (0.55,0) arc (0:135:0.55); \node at (70:0.78){$\gamma$};
\draw (135:0.4) arc (135:245:0.4); \node at (190:0.62){$\alpha$};
\draw (245:0.6) arc (245:360:0.6); \node at (300:0.82){$\beta$};
\end{tikzpicture}}
\sub{ii} \B{সর্বনিম্ন লব্ধি,} $R_{\min} = |P-Q|$ \B{; যখন} $\alpha = 180^\circ$

\itm{15} \B{লব্ধির বিশেষ ক্ষেত্রসমূহ:}
\sub{ii} $\alpha = 90^\circ$ \B{হলে,} $R = \sqrt{P^2+Q^2}$ \B{এবং} $\tan\theta = \dfrac{Q}{P}$
\sub{iii} $R=P=Q$ \B{হলে ভেক্টরদ্বয়ের মধ্যবর্তী কোণ,} $\alpha = 120^\circ$

\itm{16} \B{ভেক্টর ক্যালকুলাস (Vector Calculus):}
\sub{i} \B{স্কেলার অপেক্ষক} $\phi(x,y,z)$ \B{-এর গ্রেডিয়েন্ট (Gradient):}
\[ \vec{\nabla}\phi = \left(\hat{i}\dfrac{\partial}{\partial x}+\hat{j}\dfrac{\partial}{\partial y}+\hat{k}\dfrac{\partial}{\partial z}\right)\phi = \hat{i}\dfrac{\partial\phi}{\partial x}+\hat{j}\dfrac{\partial\phi}{\partial y}+\hat{k}\dfrac{\partial\phi}{\partial z} \]

\sub{ii} \B{ভেক্টর ক্ষেত্র} $\vec{A}$ \B{-এর ডাইভারজেন্স (Divergence):}
\[ \vec{\nabla}\cdot\vec{A} = \dfrac{\partial A_x}{\partial x}+\dfrac{\partial A_y}{\partial y}+\dfrac{\partial A_z}{\partial z} \]
\B{ডাইভারজেন্স শূন্য হলে} $(\vec{\nabla}\cdot\vec{A}=0)$ \B{ভেক্টরটি সোলেনয়ডাল (Solenoidal) বা চোঙাকৃতির হয়{\bn ।}}

\sub{iii} \B{ভেক্টর ক্ষেত্র} $\vec{A}$ \B{-এর কার্ল (Curl):}
\[ \vec{\nabla}\times\vec{A} = \begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\\dfrac{\partial}{\partial x}&\dfrac{\partial}{\partial y}&\dfrac{\partial}{\partial z}\\A_x&A_y&A_z\end{vmatrix} \]
\B{কার্ল শূন্য হলে} $(\vec{\nabla}\times\vec{A}=0)$ \B{ভেক্টরটি অঘূর্ণনশীল (Irrotational) বা সংরক্ষণশীল হয়{\bn ।}}

\chsec{অধ্যায়-৩: সরলরেখা}

\itm{1} \sub{i} \B{কার্তেসীয় স্থানাঙ্ক} $(x,y)$ \B{এবং পোলার স্থানাঙ্ক} $(r,\theta)$ \B{হলে,}

$x=r\cos\theta,\; y=r\sin\theta$\B{; মডুলাস,} $r=\sqrt{x^2+y^2}$\B{; আর্গুমেন্ট,} $\theta=\tan^{-1}\!\left(\dfrac{y}{x}\right)$

\itm{2} $(x_1,y_1)$ \B{এবং} $(x_2,y_2)$ \B{বিন্দুদ্বয়ের দূরত্ব}

$=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}$

\itm{3} \sub{i} \B{বর্গ হওয়ার শর্ত: বাহুগুলি এবং কর্ণদ্বয় সমান}

\sub{ii} \B{আয়ত হওয়ার শর্ত: বিপরীত বাহু এবং কর্ণদ্বয় সমান}

\sub{iii} \B{রম্বস হওয়ার শর্ত: বাহুগুলি সমান কিন্তু কর্ণদ্বয় অসমান}

\sub{iv} \B{সামান্তরিক হওয়ার শর্ত: বিপরীত বাহু সমান কিন্তু কর্ণদ্বয় অসমান}

\itm{4} $(x_1,y_1)$ \B{এবং} $(x_2,y_2)$ \B{বিন্দুদ্বয়ের সংযোগ রেখাংশকে} $(x,y)$ \B{বিন্দুটি} $m_1:m_2$ \B{অনুপাতে অন্তর্বিভক্ত অথবা বহির্বিভক্ত করলে,}

\[
(x,y)=\left(\frac{m_1x_2\pm m_2x_1}{m_1\pm m_2},\;\frac{m_1y_2\pm m_2y_1}{m_1\pm m_2}\right)
\]

\itm{5} \sub{i} $(x_1,y_1),(x_2,y_2)$ \B{এবং} $(x_3,y_3)$ \B{বিন্দুদ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল,}

$\Delta=\dfrac{1}{2}|x_1(y_2-y_3)+x_2(y_3-y_1)+x_3(y_1-y_2)|$

$=\dfrac{1}{2}\left|(x_1y_2+x_2y_3+x_3y_1)-(y_1x_2+y_2x_3+y_3x_1)\right|$

\sub{ii} \B{উপরোক্ত ত্রিভুজের ভরকেন্দ্রের স্থানাঙ্ক,}

$G=\!\left(\dfrac{x_1+x_2+x_3}{3},\dfrac{y_1+y_2+y_3}{3}\right)$

\sub{iii} \B{বিন্দুত্রয় সমরেখ হলে, ত্রিভুজের ক্ষেত্রফল শূন্য হবে এবং বিপরীতক্রমে সত্য{\bn ।}}

\sub{iv} \B{চতুর্ভুজ} $ABCD$ \B{এর চারটি শীর্ষবিন্দু হলে, চতুর্ভুজের ক্ষেত্রফল}

\[
=\frac{1}{2}\left\{
\begin{vmatrix}x_1&y_1\\x_2&y_2\end{vmatrix}+
\begin{vmatrix}x_2&y_2\\x_3&y_3\end{vmatrix}+
\begin{vmatrix}x_3&y_3\\x_4&y_4\end{vmatrix}+
\begin{vmatrix}x_4&y_4\\x_1&y_1\end{vmatrix}
\right\}
\]

$=\dfrac{1}{2}\left|(x_1y_2+x_2y_3+x_3y_4+x_4y_1)-(y_1x_2+y_2x_3+y_3x_4+y_4x_1)\right|$

\itm{6} \sub{i} $x$\B{-অক্ষের সমীকরণ,} $y=0$ \quad

\sub{ii} $y$\B{-অক্ষের সমীকরণ,} $x=0$

\itm{7} \sub{i} $x$\B{-অক্ষের সমান্তরাল সরলরেখার সমীকরণ,} $y=b$

\sub{ii} $y$\B{-অক্ষের সমান্তরাল সরলরেখার সমীকরণ,} $x=a$

\itm{8} \sub{i} \B{মূলবিন্দুগামী সরলরেখার সমীকরণ,} $y=mx$\B{; সরলরেখাটির ঢাল} $=m$

\sub{ii} $ax+by+c=0$ \B{রেখার ঢাল} $=-\dfrac{x\text{\B{ এর সহগ}}}{y\text{\B{ এর সহগ}}}$

\itm{9} $y$\B{-অক্ষকে ছেদ করে এরূপ সরলরেখার সমীকরণ,} $y=mx+c$\B{; একে ঢাল আকার সমীকরণও বলা হয়{\bn ।}}
\diag{\begin{tikzpicture}[scale=0.55,every node/.style={font=\scriptsize}]
\draw[->] (-0.4,0)--(4.6,0) node[right]{$x$};
\draw[->] (0,-0.4)--(0,3.4) node[above]{$y$};
\draw[thick,blue] (-0.4,0.5)--(4.4,3.5);
\filldraw (0,0.75) circle (1.2pt) node[left]{$c$};
\node[blue,right] at (4.4,3.5){$y=mx+c$};
\draw (1.4,0) arc (0:32:1.4); \node at (16:1.6){$\theta$};
\end{tikzpicture}}

\itm{10} \B{মূলবিন্দু ও} $(x_1,y_1)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$y=\dfrac{y_1}{x_1}x$

\itm{11} \B{ঢাল} $m$ \B{এবং} $(x_1,y_1)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$y-y_1=m(x-x_1)$

\itm{12} $x$\B{-অক্ষ ও} $y$\B{-অক্ষের ছেদক রেখার সমীকরণ,} $\dfrac{x}{a}+\dfrac{y}{b}=1$\B{; যেখানে,} $x$ \B{ও} $y$ \B{অক্ষের ছেদিতাংশ যথাক্রমে} $a$ \B{ও} $b$\B{; রেখাটি} $x$\B{-অক্ষকে} $(a,0)$ \B{এবং} $y$\B{-অক্ষকে} $(0,b)$ \B{বিন্দুতে ছেদ করে{\bn ।}}

\itm{13} $(x_1,y_1)$ \B{ও} $(x_2,y_2)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$\dfrac{y-y_1}{y_1-y_2}=\dfrac{x-x_1}{x_1-x_2}$

\B{বা} $y-y_1=\dfrac{y_2-y_1}{x_2-x_1}(x-x_1)$

\B{এবং ঢাল} $=\dfrac{\text{\B{কোটিদ্বয়ের অন্তর}}}{\text{\B{ভুজদ্বয়ের অন্তর}}}=\dfrac{y_2-y_1}{x_2-x_1}$

\itm{14} \B{মূলবিন্দু হতে একটি সরলরেখার উপর অঙ্কিত লম্বের দৈর্ঘ্য} $p$ \B{এবং} $x$\B{-অক্ষের সাথে উক্ত লম্বের অন্তর্ভুক্ত কোণ} $\alpha$ \B{হলে, সরলরেখার সমীকরণ,}

$x\cos\alpha+y\sin\alpha=p$

\itm{15} $ax+by+c=0$ \B{রেখার সমান্তরাল ও লম্ব যেকোনো রেখার সমীকরণ যথাক্রমে,}

$ax+by+k=0$ \B{ও} $bx-ay+k=0$\B{; যেখানে,} $k$ \B{ইচ্ছাধীন ধ্রুবক{\bn ।}}

\itm{16} \B{দুইটি রেখার ছেদবিন্দুগামী সরলরেখার সমীকরণ, (একটি সরলরেখা)} $+k$ \B{(অপর সরলরেখা)} $=0$\B{; যেখানে} $k$ \B{ইচ্ছাধীন ধ্রুবক{\bn ।}}

\itm{17} $a_1x+b_1y+c_1=0$, $a_2x+b_2y+c_2=0$ \B{ও} $a_3x+b_3y+c_3=0$ \B{সরলরেখা তিনটি সমবিন্দু হওয়ার শর্ত:}

$\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}=0$ \B{এবং বিপরীতক্রমে সত্য{\bn ।}}

\itm{18} $y=m_1x+c_1$ \B{ও} $y=m_2x+c_2$ \B{বা দুইটি সরলরেখার অন্তর্ভুক্ত কোণ} $\varphi$ \B{হলে,}
\diag{\begin{tikzpicture}[scale=0.7,every node/.style={font=\scriptsize}]
\draw[->] (-0.4,0)--(3.8,0); \draw[->] (0,-0.4)--(0,2.8);
\draw[thick,blue] (-0.3,-0.1)--(3.6,2.4) node[right]{$L_1$};
\draw[thick,red] (-0.2,0.3)--(3.4,2.8) node[right]{$L_2$};
\draw[->] (1.2,0.95) arc (32:46:0.7);
\node at (1.55,1.18){$\theta$};
\end{tikzpicture}}

$\tan\varphi=\pm\dfrac{m_1-m_2}{1+m_1m_2}$

\B{[}$\because\; m_1=\tan\theta_1,\; m_2=\tan\theta_2$\B{]}

\itm{19} $m_1$ \B{ও} $m_2$ \B{ঢালবিশিষ্ট দুইটি সরলরেখা পরস্পর সমান্তরাল ও লম্ব হলে যথাক্রমে,}
\diag{\begin{tikzpicture}[scale=0.6,every node/.style={font=\scriptsize}]
\draw[thick,blue] (0,2)--(3.4,2) node[right]{$L_1$};
\draw[thick,blue] (0,0.6)--(3.4,0.6) node[right]{$L_2$};
\node at (1.7,-0.1){\B{সমান্তরাল}};
\begin{scope}[xshift=4.6cm]
\draw[thick,red] (0,0)--(3.0,2.6) node[right]{$L_1$};
\draw[thick,red] (2.6,-0.1)--(0.0,2.4) node[left]{$L_2$};
\node at (1.5,-0.4){\B{লম্ব}};
\end{scope}
\end{tikzpicture}}

$m_1=m_2$ \B{ও} $m_1m_2=-1$

\itm{20} $P(x_1,y_1)$ \B{বিন্দু হতে} $ax+by+c=0$ \B{সরলরেখার উপর অঙ্কিত লম্বের দৈর্ঘ্য বা লম্বদূরত্ব}
\diag{\begin{tikzpicture}[scale=0.55,every node/.style={font=\scriptsize}]
\draw[->] (-0.4,0)--(4.6,0) node[right]{$x$};
\draw[->] (0,-0.4)--(0,3.4) node[above]{$y$};
\draw[thick,blue] (0.2,3.0)--(4.4,0.4);
\filldraw (3.4,2.4) circle (1.4pt) node[above right]{$P(x_1,y_1)$};
\draw[dashed,thick,red] (3.4,2.4)--(2.31,0.97);
\node[red,right] at (2.85,1.7){$d$};
\node[blue,right] at (4.4,0.5){\tiny$ax+by+c=0$};
\end{tikzpicture}}

$=\dfrac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$

\itm{21} $ax+by+c_1=0$ \B{এবং} $ax+by+c_2=0$ \B{সমান্তরাল সরলরেখা দুইটির মধ্যবর্তী দূরত্ব}

$=\dfrac{|c_1-c_2|}{\sqrt{a^2+b^2}}$

\itm{22} $a_1x+b_1y+c_1=0$ \B{এবং} $a_2x+b_2y+c_2=0$ \B{রেখাদ্বয়ের অন্তর্ভুক্ত কোণের সমদ্বিখণ্ডকের সমীকরণ}

\[
\frac{a_1x+b_1y+c_1}{\sqrt{a_1^2+b_1^2}}=\pm\frac{a_2x+b_2y+c_2}{\sqrt{a_2^2+b_2^2}}
\]

\sub{i} $c_1$ \B{ও} $c_2$ \B{উভয়কে ধনাত্মক করে,} $a_1a_2+b_1b_2>0$ \B{হলে, $+$ চিহ্ন নিয়ে স্থূলকোণের এবং $-$ চিহ্ন নিয়ে সূক্ষ্মকোণের সমদ্বিখণ্ডক পাওয়া যাবে{\bn ।}}

\sub{ii} $a_1a_2+b_1b_2<0$ \B{হলে, $+$ চিহ্ন নিয়ে সূক্ষ্মকোণের এবং $-$ চিহ্ন নিয়ে স্থূলকোণের সমদ্বিখণ্ডক পাওয়া যাবে{\bn ।}}

\sub{iii} $c_1$ \B{ও} $c_2$ \B{ধনাত্মক হলে, $+$ চিহ্নধারী সমদ্বিখণ্ডকটি মূলবিন্দু ধারণকারী কোণের সমদ্বিখণ্ডক এবং $-$ চিহ্নধারী সমদ্বিখণ্ডকটি মূলবিন্দু না-ধারণকারী কোণের সমদ্বিখণ্ডক{\bn ।}}

\itm{23} \B{কোনো বিন্দুর সাপেক্ষে বা সরলরেখার সাপেক্ষে প্রতিবিম্ব এবং লম্বপাদবিন্দু:}

\sub{i} $P(x_1,y_1)$ \B{বিন্দু হতে} $ax+by+c=0$ \B{সরলরেখার উপর অঙ্কিত লম্বের পাদবিন্দুর স্থানাঙ্ক $(x,y)$ হলে:}

\[
\frac{x-x_1}{a}=\frac{y-y_1}{b}=-\frac{ax_1+by_1+c}{a^2+b^2}
\]

\sub{ii} $P(x_1,y_1)$ \B{বিন্দুর সাপেক্ষে} $ax+by+c=0$ \B{সরলরেখার সাপেক্ষে প্রতিবিম্ব বিন্দুর স্থানাঙ্ক $(x,y)$ হলে:}

\[
\frac{x-x_1}{a}=\frac{y-y_1}{b}=-\frac{2(ax_1+by_1+c)}{a^2+b^2}
\]

\itm{24} \B{অক্ষের রূপান্তর:}

\sub{i} \B{অক্ষের দিক অপরিবর্তিত রেখে মূলবিন্দুকে} $(\alpha,\beta)$ \B{বিন্দুতে স্থানান্তর করলে নতুন স্থানাঙ্ক} $(X,Y)$ \B{হলে আদি স্থানাঙ্ক:}

$x=X+\alpha,\; y=Y+\beta$

\sub{ii} \B{মূলবিন্দু অপরিবর্তিত রেখে অক্ষদ্বয়কে} $\theta$ \B{কোণে আবর্তন করলে নতুন স্থানাঙ্ক} $(X,Y)$ \B{হলে আদি স্থানাঙ্ক:}

$x=X\cos\theta-Y\sin\theta,\; y=X\sin\theta+Y\cos\theta$



\chsec{অধ্যায়-৪: বৃত্ত}

\itm{1} \sub{i} $(0,0)$ \B{কেন্দ্র এবং} $a$ \B{ব্যাসার্ধবিশিষ্ট বৃত্তের সমীকরণ,} $x^2+y^2=a^2$

\sub{ii} $(h,k)$ \B{কেন্দ্র এবং} $r$ \B{ব্যাসার্ধবিশিষ্ট বৃত্তের সমীকরণ,} $(x-h)^2+(y-k)^2=r^2$
\diag{\begin{tikzpicture}[scale=0.6,every node/.style={font=\scriptsize}]
\draw[->] (-0.4,0)--(4.4,0) node[right]{$x$};
\draw[->] (0,-0.4)--(0,3.6) node[above]{$y$};
\draw[thick,red] (2.2,1.8) circle (1.3);
\filldraw (2.2,1.8) circle (1.4pt) node[above right]{$(h,k)$};
\draw[->] (2.2,1.8)--++(28:1.3) node[midway,above,sloped]{$a$};
\end{tikzpicture}}

\itm{2} \B{বৃত্তের সাধারণ সমীকরণ,} $x^2+y^2+2gx+2fy+c=0$ \B{যার--}

\sub{i} \B{কেন্দ্র} $(-g,-f)$ \B{এবং ব্যাসার্ধ} $=\sqrt{g^2+f^2-c}$

\sub{ii} $x$\B{-অক্ষের খণ্ডিতাংশ} $=2\sqrt{g^2-c}$ \B{এবং} $y$\B{-অক্ষের খণ্ডিতাংশ} $=2\sqrt{f^2-c}$

\sub{iii} $x$\B{-অক্ষকে স্পর্শ করলে} $g^2=c$\B{;} $y$\B{-অক্ষকে স্পর্শ করলে} $f^2=c$ \B{এবং উভয় অক্ষকে স্পর্শ করলে} $g^2=f^2=c$.

\sub{iv} $-g=0$ \B{বা,} $g=0$ \B{হলে বৃত্তের কেন্দ্র} $y$\B{-অক্ষের উপর অবস্থিত এবং} $-f=0$ \B{বা} $f=0$ \B{হলে বৃত্তের কেন্দ্র} $x$\B{-অক্ষের উপর অবস্থিত{\bn ।}}

\sub{v} $x$\B{-অক্ষকে স্পর্শ করলে বৃত্তের ব্যাসার্ধ} $=|$\B{কেন্দ্রের কোটি}$|$ \B{এবং} $y$\B{-অক্ষকে স্পর্শ করলে বৃত্তের ব্যাসার্ধ} $=|$\B{কেন্দ্রের ভুজ}$|$

\itm{3} $(x_1,y_1)$ \B{এবং} $(x_2,y_2)$ \B{বিন্দুদ্বয়ের সংযোগকারী রেখাংশকে ব্যাস ধরে অঙ্কিত বৃত্তের সমীকরণ,}

$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)=0$

\itm{4} $y=mx+c$ \B{সরলরেখাটি} $x^2+y^2=a^2$ \B{বৃত্তকে স্পর্শ করার শর্ত:}

$c=\pm a\sqrt{1+m^2}$ \B{বা} $c^2=a^2(1+m^2)$\B{; স্পর্শকের সমীকরণ,} $y=mx\pm a\sqrt{1+m^2}$

\B{এবং স্পর্শবিন্দু} $\left(\dfrac{\mp am}{\sqrt{1+m^2}},\;\dfrac{\pm a}{\sqrt{1+m^2}}\right)$

\itm{5} \sub{i} $x^2+y^2=a^2$ \B{বৃত্তের উপরিস্থিত} $(x_1,y_1)$ \B{বিন্দুতে অঙ্কিত স্পর্শকের সমীকরণ,}

$xx_1+yy_1=a^2$ \B{এবং স্পর্শকের দৈর্ঘ্য} $=\sqrt{x_1^2+y_1^2-a^2}$

\sub{ii} $x^2+y^2+2gx+2fy+c=0$ \B{বৃত্তের উপরিস্থিত} $(x_1,y_1)$ \B{বিন্দুতে অঙ্কিত স্পর্শকের সমীকরণ,}

$xx_1+yy_1+g(x+x_1)+f(y+y_1)+c=0$\B{, অভিলম্বের সমীকরণ}

$(x_1+g)y-(y_1+f)x+fx_1-gy_1=0$

\B{এবং স্পর্শকের দৈর্ঘ্য} $=\sqrt{x_1^2+y_1^2+2gx_1+2fy_1+c}$

\itm{6} \sub{i} \B{দুইটি বৃত্ত পরস্পর বহিঃস্থভাবে স্পর্শ করলে, কেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব} $=$ \B{ব্যাসার্ধদ্বয়ের যোগফল{\bn ।}}

\sub{ii} \B{দুইটি বৃত্ত পরস্পরকে অন্তঃস্থভাবে স্পর্শ করলে, কেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব} $=$ \B{ব্যাসার্ধদ্বয়ের অন্তর{\bn ।}}

\itm{7} $S_1=0$ \B{এবং} $S_2=0$ \B{দুইটি বৃত্তের ছেদবিন্দুগামী যেকোনো বৃত্তের সমীকরণ,}

$S_1+kS_2=0$\B{; যেখানে} $k$ \B{একটি অশূন্য ধ্রুবক{\bn ।}}

\itm{8} $S_1=0$ \B{বৃত্ত এবং} $L=0$ \B{সরলরেখা হলে, এদের ছেদবিন্দুগামী যেকোনো বৃত্তের সমীকরণ,}

$S_1+kL=0$\B{; যেখানে} $k$ \B{একটি অশূন্য ধ্রুবক{\bn ।}}

\itm{9} $(x_1,y_1)$ \B{ও} $(x_2,y_2)$ \B{বিন্দুগামী বৃত্তের সমীকরণ}

$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)+k\{(x-x_1)(y_1-y_2)-(y-y_1)(x_1-x_2)\}=0$\B{; যেখানে,} $k$ \B{একটি ইচ্ছামূলক ধ্রুবক{\bn ।}}

\itm{10} $(x_1,y_1),(x_2,y_2)$ \B{ও} $(x_3,y_3)$ \B{বিন্দুগামী বৃত্তের সমীকরণ,}

\begingroup
\small
\[
\begin{aligned}
&\frac{(x-x_1)(x-x_2)+(y-y_1)(y-y_2)}
{(x_3-x_1)(x_3-x_2)+(y_3-y_1)(y_3-y_2)}\\
&=\frac{(x-x_1)(y_1-y_2)-(y-y_1)(x_1-x_2)}
{(x_3-x_1)(y_1-y_2)-(y_3-y_1)(x_1-x_2)}
\end{aligned}
\]
\endgroup

\itm{11} $S_1=0$ \B{এবং} $S_2=0$ \B{দুইটি বৃত্তের সাধারণ জ্যা এর সমীকরণ,} $S_1-S_2=0$

\itm{12} $R$ \B{ব্যাসার্ধ ও} $(r_0,\theta_0)$ \B{কেন্দ্রবিশিষ্ট বৃত্তের পোলার সমীকরণ,}

$r^2-2rr_0\cos(\theta-\theta_0)+r_0^2=R^2$

\itm{13} $R$ \B{ব্যাসার্ধ ও পোল মূলবিন্দু দিয়ে যায় এমন বৃত্তের ব্যাস—}

\sub{i} \B{পোলার অক্ষ বরাবর হলে সমীকরণ,} $r=\pm2R\cos\theta$

\sub{ii} \B{পোলার অক্ষের উপর লম্ব বরাবর হলে সমীকরণ,} $r=\pm2R\sin\theta$

\itm{14} \B{পোলার স্থানাংকে বৃত্তের সাধারণ সমীকরণ:}

$r^2-2r(g\cos\theta+f\sin\theta)+c=0$

\B{যেখানে, কেন্দ্র} $=\!\left(\sqrt{g^2+f^2},\;\tan^{-1}\!\dfrac{f}{g}\right)$ \B{এবং ব্যাসার্ধ} $=\sqrt{g^2+f^2-c}$

\itm{15} $x^2+y^2=r^2$ \B{বৃত্তের উপরিস্থিত} $(x_1,y_1)$ \B{বিন্দুতে স্পর্শকের সমীকরণ,} $xx_1+yy_1=r^2$

\B{এবং অভিলম্বের সমীকরণ,} $xy_1-yx_1=0$

\itm{16} $x^2+y^2+2gx+2fy+c=0$ \B{বৃত্তের উপরিস্থিত} $(x_1,y_1)$ \B{বিন্দুতে অভিলম্বের সমীকরণ,}

$xy_1-yx_1+f(x-x_1)-g(y-y_1)=0$

\itm{17} \B{বহিঃস্থ কোনো বিন্দু} $(x_1,y_1)$ \B{হতে} $x^2+y^2=r^2$ \B{বৃত্তে অঙ্কিত স্পর্শদ্বয়ের সমীকরণ,}

$(xx_1+yy_1-r^2)^2=(x^2+y^2-r^2)(x_1^2+y_1^2-r^2)$ \B{অর্থাৎ} $T^2=SS_1$

\itm{18} \B{বহিঃস্থ} $(x_1,y_1)$ \B{বিন্দু হতে} $x^2+y^2+2gx+2fy+c=0$ \B{বৃত্তে অঙ্কিত স্পর্শকের সমীকরণ,}

\begingroup\small
$\{xx_1+yy_1+g(x+x_1)+f(y+y_1)+c\}^2=(x^2+y^2+2gx+2fy+c)(x_1^2+y_1^2+2gx_1+2fy_1+c)$
\endgroup

\itm{19} $y=mx+c$ \B{রেখাটি} $x^2+y^2=r^2$ \B{বৃত্তের স্পর্শক হওয়ার শর্ত:} $c^2=r^2(1+m^2)$\B{; স্পর্শবিন্দু} $\left(\dfrac{-mr}{\sqrt{1+m^2}},\;\dfrac{r}{\sqrt{1+m^2}}\right)$

\itm{20} \B{বৃত্তের বহিঃস্থ} $(x_1,y_1)$ \B{বিন্দু হতে} $x^2+y^2=r^2$ \B{বৃত্তে অঙ্কিত স্পর্শজ্যার (chord of contact) সমীকরণ,} $xx_1+yy_1=r^2$

\B{এবং} $x^2+y^2+2gx+2fy+c=0$ \B{বৃত্তে অঙ্কিত স্পর্শজ্যার সমীকরণ,} $xx_1+yy_1+g(x+x_1)+f(y+y_1)+c=0$

\itm{21} $x^2+y^2=r^2$ \B{বৃত্তের কোনো জ্যার মধ্যবিন্দু} $(x_1,y_1)$ \B{হলে, ঐ জ্যার সমীকরণ,} $xx_1+yy_1=x_1^2+y_1^2$

$x^2+y^2+2gx+2fy+c=0$ \B{বৃত্তের ক্ষেত্রে জ্যার সমীকরণ,} $xx_1+yy_1+g(x+x_1)+f(y+y_1)=x_1^2+y_1^2+2gx_1+2fy_1$

\itm{22} \B{দুটি বৃত্ত পরস্পর লম্বালম্বিভাবে ছেদ করার শর্ত (Orthogonal intersection):} $2g_1g_2+2f_1f_2=c_1+c_2$
\diag{\begin{tikzpicture}[scale=0.55,every node/.style={font=\scriptsize}]
\draw[thick] (0,0) circle (1.2);
\draw[thick] (1.6,0) circle (1.0);
\filldraw (0,0) circle (1pt) node[below left]{$C_1$};
\filldraw (1.6,0) circle (1pt) node[below right]{$C_2$};
\node at (0.85,1.05){\tiny$90^\circ$};
\end{tikzpicture}}

\chsec{অধ্যায়-৫: বিন্যাস ও সমাবেশ}

\itm{1} \sub{i} $n$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিস থেকে} $r$ \B{সংখ্যক জিনিসের বিন্যাস}

${}^nP_r=\dfrac{n!}{(n-r)!}$\B{;} $n\geq r$

\sub{ii} $n!=n(n-1)!=n(n-1)(n-2)!=n(n-1)(n-2)\cdots3\cdot2\cdot1$\B{;} ${}^nP_n=n!$, $0!=1$

\sub{iii} $p$ \B{সংখ্যক এক প্রকার,} $q$ \B{সংখ্যক অন্য এক প্রকার, $r$ সংখ্যক অন্য আর এক প্রকার বাকিগুলি ভিন্ন ভিন্ন এরূপ} $n$ \B{সংখ্যক বস্তুর বিন্যাস সংখ্যা} $=\dfrac{n!}{p!\,q!\,r!}$

\sub{iv} $n$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিস থেকে প্রতিবার} $r$ \B{সংখ্যক জিনিস নিয়ে বিন্যাস সংখ্যা (যেখানে, যেকোনো জিনিসের} $r$ \B{সংখ্যক বার পুনরাবৃত্তি ঘটতে পারে)} $=n^r$

\sub{v} $n$ \B{সংখ্যক ভিন্ন জিনিস একত্রে নিয়ে চক্র বিন্যাস} $=(n-1)!$

\sub{vi} \B{টেবিল বা মালার ক্ষেত্রে (যাকে উল্টিয়ে দেখা যায়) চক্র বিন্যাস} $=\dfrac{(n-1)!}{2}$

\itm{2} \sub{i} ${}^nC_r=\dfrac{n!}{r!\,(n-r)!}={}^nC_{n-r}$ \B{(সম্পূরক সমাবেশ)}

\sub{ii} ${}^nC_r+{}^nC_{r-1}={}^{n+1}C_r$

\sub{iii} ${}^nC_x={}^nC_y$ \B{হলে,} $x+y=n$

\sub{iv} \B{বিন্যাস ও সমাবেশ এর মধ্যে সম্পর্ক:} ${}^nP_r = {}^nC_r \times r!$

\itm{3} \sub{i} \B{১ম প্রকারের} $p$ \B{সংখ্যক ২য় প্রকারের} $q$ \B{সংখ্যক ও ৩য় প্রকারের} $r$ \B{সংখ্যক থেকে যেকোনো সংখ্যক জিনিস নিয়ে মোট সমাবেশ} $(p+1)(q+1)(r+1)-1$

\sub{ii} \B{১ম প্রকারের} $p$ \B{সংখ্যক ২য় প্রকারের} $q$ \B{সংখ্যক ও} $r$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিসের সমাবেশ} $(p+1)(q+1)2^r-1$

\sub{iii} $n$ \B{সংখ্যক জিনিস থেকে প্রত্যেক বার অন্তত একটি জিনিস নিয়ে গঠিত সমাবেশ} $2^n-1$

\itm{4} \B{শর্তাধীন সমাবেশ:}
\sub{i} $p$ \B{সংখ্যক নির্দিষ্ট বস্তু সর্বদা অন্তর্ভুক্ত করে} $n$ \B{সংখ্যক ভিন্ন ভিন্ন বস্তু থেকে প্রতিবার} $r$ \B{সংখ্যক বস্তু নিয়ে গঠিত সমাবেশ} $={}^{n-p}C_{r-p}$

\sub{ii} $p$ \B{সংখ্যক নির্দিষ্ট বস্তু সর্বদা অন্তর্ভুক্ত না করে} $n$ \B{সংখ্যক ভিন্ন ভিন্ন বস্তু থেকে প্রতিবার} $r$ \B{সংখ্যক বস্তু নিয়ে গঠিত সমাবেশ} $={}^{n-p}C_r$

\itm{5} \B{দল গঠন ও বিভক্তিকরণ:}
\sub{i} $p_1+p_2+\cdots+p_n$ \B{সংখ্যক জিনিসকে} $n$ \B{সংখ্যক ভাগে বিভক্ত করার সমাবেশ যেন ভাগগুলিতে যথাক্রমে} $p_1,p_2,\ldots,p_n$ \B{জিনিস থাকে,}

$\dfrac{(p_1+p_2+\cdots+p_n)!}{p_1!\,p_2!\cdots p_n!}$

\sub{ii} $(p+q)$ \B{সংখ্যক জিনিসকে} $A$ \B{ও} $B$ \B{দুটি নির্দিষ্ট দলে বিভক্ত করা যায়} $\dfrac{(p+q)!}{p!\,q!}$ \B{উপায়ে}

\sub{iii} $2q$ \B{সংখ্যক জিনিসকে} $A$ \B{ও} $B$ \B{দুটি নির্দিষ্ট দলে সমান ভাগে ভাগ করা যায়} $\dfrac{(2q)!}{(q!)^2}$ \B{উপায়ে}

\sub{iv} $2q$ \B{সংখ্যক জিনিসকে দুটি সমান ভাগে (দলে) ভাগ করা যায়} $\dfrac{(2q)!}{2!\,(q!)^2}$ \B{উপায়ে}

\chsec{অধ্যায়-৬: ত্রিকোণমিতিক অনুপাত}

\itm{1} $1^\circ=\dfrac{\pi}{180}$ \B{রেডিয়ান; 1 রেডিয়ান} $=\dfrac{180^\circ}{\pi}$
\diag{\begin{tikzpicture}[scale=1.0,every node/.style={font=\scriptsize}]
\draw[->] (-1.25,0)--(1.25,0) node[right]{$x$};
\draw[->] (0,-1.25)--(0,1.25) node[above]{$y$};
\draw[thick] (0,0) circle (1);
\draw[->,thick,blue] (0,0)--(38:1);
\draw[dashed] (38:1)--(0.788,0);
\draw[dashed] (38:1)--(0,0.616);
\node[below,font=\tiny] at (0.788,0){$\cos\theta$};
\node[left,font=\tiny] at (0,0.616){$\sin\theta$};
\draw (0.25,0) arc (0:38:0.25); \node at (19:0.4){$\theta$};
\end{tikzpicture}}

\itm{2} \sub{i} \B{বৃত্তচাপের দৈর্ঘ্য,} $s=r\theta$ \B{একক; যেখানে,} $r$ \B{ব্যাসার্ধ ও} $\theta$ \B{রেডিয়ান কোণ}

\sub{ii} \B{বৃত্তকলার ক্ষেত্রফল} $A=\dfrac{1}{2}r^2\theta$ \B{বর্গ একক}

\itm{3} \sub{i} \B{ঘড়ির ঘণ্টার কাঁটা ও মিনিটের কাঁটার মধ্যবর্তী কোণ,} $\theta = \left|\dfrac{60H-11M}{2}\right|^\circ$

\sub{ii} \B{যদি,} $\theta > 180^\circ$ \B{হয়, তাহলে মধ্যবর্তী কোণ} $= 360^\circ - \left|\dfrac{60H-11M}{2}\right|^\circ$

\B{যেখানে,} $H =$ \B{ঘণ্টার কাঁটা যে সংখ্যায় আছে এবং} $M =$ \B{মিনিটের কাঁটা যে সংখ্যায় আছে{\bn ।}}

\itm{4} \B{চতুর্ভাগ অনুযায়ী ত্রিকোণমিতিক অনুপাতের চিহ্ন:}
\sub{i} \B{১ম চতুর্ভাগে সকল ত্রিকোণমিতিক অনুপাত} (+)ve
\sub{ii} \B{২য় চতুর্ভাগে শুধু} $\sin$ \B{ও} $\csc$ (+)ve
\sub{iii} \B{৩য় চতুর্ভাগে শুধু} $\tan$ \B{ও} $\cot$ (+)ve
\sub{iv} \B{৪র্থ চতুর্ভাগে শুধু} $\cos$ \B{ও} $\sec$ (+)ve

\itm{5} \B{ত্রিকোণমিতিক অনুপাতের সূত্রসমূহ:}
\sub{i} $\sin\theta = \dfrac{1}{\csc\theta}$
\sub{ii} $\cos\theta = \dfrac{1}{\sec\theta}$
\sub{iii} $\csc^2\theta - \cot^2\theta = 1$
\sub{iv} $\tan\theta = \dfrac{1}{\cot\theta}$
\sub{v} $\tan\theta = \dfrac{\sin\theta}{\cos\theta}$
\sub{vi} $\cot\theta = \dfrac{\cos\theta}{\sin\theta}$
\sub{vii} $\sin^2\theta + \cos^2\theta = 1$
\sub{viii} $\sec^2\theta - \tan^2\theta = 1$

\itm{6} \B{ত্রিকোণমিতিক অনুপাতে মানের সীমা:}
\sub{i} $-1 \le \sin\theta \le 1$
\sub{ii} $-1 \le \cos\theta \le 1$
\sub{iii} $\csc\theta \ge 1$ \B{অথবা} $\csc\theta \le -1$
\sub{iv} $\sec\theta \ge 1$ \B{অথবা} $\sec\theta \le -1$
\sub{v} $\tan\theta = \mathbb{R}$ \B{[ যেখানে} $\mathbb{R} =$ \B{যেকোনো বাস্তব সংখ্যা ]}
\sub{vi} $\cot\theta = \mathbb{R}$

\itm{7} \B{ত্রিকোণমিতিক ফাংশনের ডোমেন ও রেঞ্জ:}

\B{ফাংশন} | \B{ডোমেন} | \B{রেঞ্জ}
:---: | :---: | :---:
$\sin\theta$ | $\mathbb{R}$ | $[-1,1]$
$\cos\theta$ | $\mathbb{R}$ | $[-1,1]$
$\tan\theta$ | $\mathbb{R} - \left\{(2n+1)\dfrac{\pi}{2} ; n \in \mathbb{Z}\right\}$ | $\mathbb{R}$
$\sec\theta$ | $\mathbb{R} - \left\{(2n+1)\dfrac{\pi}{2} ; n \in \mathbb{Z}\right\}$ | $\mathbb{R} - (-1,1)$
$\cot\theta$ | $\mathbb{R} - \{n\pi ; n \in \mathbb{Z}\}$ | $\mathbb{R}$
$\csc\theta$ | $\mathbb{R} - \{n\pi ; n \in \mathbb{Z}\}$ | $\mathbb{R} - (-1,1)$

\chsec{অধ্যায়-৭: সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত}

\itm{1} \B{ঋণাত্মক কোণের ত্রিকোণমিতিক অনুপাত:}
\sub{i} $\sin(-\theta) = -\sin\theta, \quad \cos(-\theta) = \cos\theta$
\sub{ii} $\tan(-\theta) = -\tan\theta, \quad \csc(-\theta) = -\csc\theta$
\sub{iii} $\sec(-\theta) = \sec\theta, \quad \cot(-\theta) = -\cot\theta$

\itm{2} \B{সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত নির্ণয়ের নিয়ম:}
\sub{i} $\sin\left(n\dfrac{\pi}{2} \pm \theta\right) = \pm\sin\theta$ \B{ [যখন } n \B{ জোড়] } $= \pm\cos\theta$ \B{ [যখন } n \B{ বিজোড়]}
\sub{ii} $\tan\left(n\dfrac{\pi}{2} \pm \theta\right) = \pm\tan\theta$ \B{ [যখন } n \B{ জোড়] } $= \pm\cot\theta$ \B{ [যখন } n \B{ বিজোড়]}
\sub{iii} $\csc\left(n\dfrac{\pi}{2} \pm \theta\right) = \pm\csc\theta$ \B{ [যখন } n \B{ জোড়] } $= \pm\sec\theta$ \B{ [যখন } n \B{ বিজোড়]}
\B{[(+) বা (-) চিহ্ন চতুর্ভাগের অবস্থান দেখে বসাতে হবে]}

\itm{3} \B{যৌগিক কোণের সূত্রাবলী (Compound Angles):}
\sub{i} $\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$
\sub{ii} $\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$
\sub{iii} $\tan(A\pm B)=\dfrac{\tan A\pm\tan B}{1\mp\tan A\tan B}$
\sub{iv} $\cot(A\pm B)=\dfrac{\cot A\cot B\mp1}{\cot B\pm\cot A}$

\itm{4} \B{ত্রিকোণমিতিক অনুপাতের যোগফল ও গুণফলের রূপান্তর:}
\sub{i} $2\sin A\cos B=\sin(A+B)+\sin(A-B)$
\sub{ii} $2\cos A\sin B=\sin(A+B)-\sin(A-B)$
\sub{iii} $2\cos A\cos B=\cos(A+B)+\cos(A-B)$
\sub{iv} $2\sin A\sin B=\cos(A-B)-\cos(A+B)$

\itm{5} \B{যোগফল ও বিয়োগফলকে গুণফলে রূপান্তর:}
\sub{i} $\sin C+\sin D=2\sin\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{ii} $\sin C-\sin D=2\cos\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$
\sub{iii} $\cos C+\cos D=2\cos\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{iv} $\cos C-\cos D=2\sin\dfrac{C+D}{2}\sin\dfrac{D-C}{2}$

\itm{6} \B{বর্গীয় কোণের গুণফলের সূত্রাবলী:}
\sub{i} $\sin(A+B)\sin(A-B)=\sin^2\!A-\sin^2\!B=\cos^2\!B-\cos^2\!A$
\sub{ii} $\cos(A+B)\cos(A-B)=\cos^2\!A-\sin^2\!B=\cos^2\!B-\sin^2\!A$

\itm{7} \B{গুণিতক কোণের সূত্রাবলী (Multiple Angles):}
\sub{i} $\sin2A=2\sin A\cos A=\dfrac{2\tan A}{1+\tan^2\!A}$
\sub{ii} $\cos2A=\cos^2\!A-\sin^2\!A=1-2\sin^2\!A=2\cos^2\!A-1=\dfrac{1-\tan^2\!A}{1+\tan^2\!A}$
\sub{iii} $\tan2A=\dfrac{2\tan A}{1-\tan^2\!A}$
\sub{iv} $1-\cos2A=2\sin^2\!A$
\sub{v} $1+\cos2A=2\cos^2\!A$

\itm{8} \B{ত্রিগুণিতক কোণের সূত্রাবলী (Triple Angles):}
\sub{i} $\sin3A=3\sin A-4\sin^3\!A$
\sub{ii} $\cos3A=4\cos^3\!A-3\cos A$
\sub{iii} $\tan3A=\dfrac{3\tan A-\tan^3\!A}{1-3\tan^2\!A}$

\itm{9} \B{উপ-গুণিতক কোণের সূত্রাবলী (Sub-multiple Angles):}
\sub{i} $\tan\dfrac{A}{2} = \dfrac{1-\cos A}{\sin A} = \dfrac{\sin A}{1+\cos A} = \sqrt{\dfrac{1-\cos A}{1+\cos A}}$
\sub{ii} $\cot\dfrac{A}{2} = \dfrac{\sin A}{1-\cos A} = \dfrac{1+\cos A}{\sin A} = \sqrt{\dfrac{1+\cos A}{1-\cos A}}$
\sub{iii} $\tan\left(\dfrac{\pi}{4} - \dfrac{A}{2}\right) = \dfrac{1-\sin A}{\cos A} = \dfrac{\cos A}{1+\sin A} = \sqrt{\dfrac{1-\sin A}{1+\sin A}}$
\sub{iv} $\tan\left(\dfrac{\pi}{4} + \dfrac{A}{2}\right) = \dfrac{1+\sin A}{\cos A} = \dfrac{\cos A}{1-\sin A} = \sqrt{\dfrac{1+\sin A}{1-\sin A}}$

\itm{10} \B{কিছু গুরত্বপূর্ণ General Form:}
\sub{i} $A + B = 45^\circ$ \B{ হলে,}
\quad 1. $\tan A + \tan B + \tan A\tan B = 1$
\quad 2. $(1 + \tan A)(1 + \tan B) = 2$
\sub{ii} $A = B + C$ \B{ হলে, } $\tan A - \tan B - \tan C = \tan A\tan B\tan C$
\sub{iii} $A + B = 90^\circ$ \B{ হলে, } $\tan A = \tan B + 2\tan(A-B)$
\sub{iv} $\tan(45^\circ + A) = \dfrac{1+\tan A}{1-\tan A} = \dfrac{\cos A + \sin A}{\cos A - \sin A}$
\sub{v} $\tan(45^\circ - A) = \dfrac{1-\tan A}{1+\tan A} = \dfrac{\cos A - \sin A}{\cos A + \sin A}$
\sub{vi} $\sin A + \cos A = \sqrt{2}\cos(45^\circ - A) = \sqrt{2}\sin(45^\circ + A)$
\sub{vii} $A + B = 90^\circ$ \B{ হলে, } $\sin A + \cos A = \sin B + \cos B$

\itm{11} \B{বৃত্তীয় কোণ বিভাজনের বিশেষ ধর্ম (সাম্যাবস্থা):}
\sub{i} $\sin A + \sin(A + 120^\circ) + \sin(A - 120^\circ) = 0$
\sub{ii} $\cos A + \cos(A + 120^\circ) + \cos(A - 120^\circ) = 0$
\sub{iii} $\sin A + \sin(A + 120^\circ) + \sin(A + 240^\circ) = 0$
\sub{iv} $\cos A + \cos(A + 120^\circ) + \cos(A + 240^\circ) = 0$

\itm{12} \B{ধারাবাহিক বর্গমূলের Shortcut সূত্রাবলী:}
\sub{i} $\sqrt{2+\sqrt{2+\sqrt{2+\dots}}} \quad \text{[} n-1 \B{ বার]} = 2\cos\dfrac{\pi}{2^n}$
\sub{ii} $\sqrt{2-\sqrt{2+\sqrt{2+\dots}}} \quad \text{[} n-1 \B{ বার]} = 2\sin\dfrac{\pi}{2^n}$
\sub{iii} $\sqrt{2+\sqrt{2+\dots+(n-1)\text{বার}+\sqrt{3}}} = 2\cos\dfrac{\pi}{3 \cdot 2^n}$
\sub{iv} $\sqrt{2-\sqrt{2+\dots+(n-1)\text{বার}+\sqrt{3}}} = 2\sin\dfrac{\pi}{3 \cdot 2^n}$

\itm{13} \B{ত্রিভুজের ধর্ম ও মৌলিক সূত্রাবলী (Properties of Triangle):}
\diag{\begin{tikzpicture}[scale=0.85,every node/.style={font=\scriptsize}]
\coordinate (A) at (1.6,2.0);
\coordinate (B) at (0,0);
\coordinate (C) at (3.0,0);
\draw[thick] (A)--(B)--(C)--cycle;
\node[above] at (A) {$A$}; \node[below left] at (B) {$B$}; \node[below right] at (C) {$C$};
\node[below] at ($(B)!0.5!(C)$) {$a$};
\node[above right] at ($(A)!0.5!(C)$) {$b$};
\node[above left] at ($(A)!0.5!(B)$) {$c$};
\end{tikzpicture}}
\sub{i} \B{কোণ সমষ্টি: } $A + B + C = 180^\circ$ \B{ এবং বাহুর দৈর্ঘ্য } $BC = a, \; AC = b, \; AB = c$
\sub{ii} \B{সাইন সূত্র (Sine Rule): } $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$ \B{ [যেখানে } $R$ = \B{ পরিবৃত্তের ব্যাসার্ধ]}
\sub{iii} \B{কোসাইন সূত্র (Cosine Rule):}
$$\cos A=\dfrac{b^2+c^2-a^2}{2bc}, \quad \cos B=\dfrac{c^2+a^2-b^2}{2ca}, \quad \cos C=\dfrac{a^2+b^2-c^2}{2ab}$$
\sub{iv} \B{অভিক্ষেপ সূত্র (Projection Rule):}
$$a=b\cos C+c\cos B, \quad b=c\cos A+a\cos C, \quad c=a\cos B+b\cos A$$

\itm{14} \B{ত্রিভুজের ক্ষেত্রফল ($\Delta$):}
$$\Delta=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B=\dfrac{1}{2}ab\sin C=\sqrt{s(s-a)(s-b)(s-c)}$$
\B{যেখানে, } $s=\dfrac{a+b+c}{2} = \B{ অর্ধপরিসীমা{\bn ।}}$

\itm{15} \B{ত্রিভুজের অর্ধকোণের ত্রিকোণমিতিক অনুপাত:}
\sub{i} $\sin\dfrac{A}{2}=\sqrt{\dfrac{(s-b)(s-c)}{bc}}, \quad \sin\dfrac{B}{2}=\sqrt{\dfrac{(s-a)(s-c)}{ca}}, \quad \sin\dfrac{C}{2}=\sqrt{\dfrac{(s-a)(s-b)}{ab}}$
\sub{ii} $\cos\dfrac{A}{2}=\sqrt{\dfrac{s(s-a)}{bc}}, \quad \cos\dfrac{B}{2}=\sqrt{\dfrac{s(s-b)}{ca}}, \quad \cos\dfrac{C}{2}=\sqrt{\dfrac{s(s-c)}{ab}}$
\sub{iii} $\tan\dfrac{A}{2}=\sqrt{\dfrac{(s-b)(s-c)}{s(s-a)}}=\dfrac{\Delta}{s(s-a)}$
\sub{iv} $\tan\dfrac{B}{2}=\sqrt{\dfrac{(s-a)(s-c)}{s(s-b)}}=\dfrac{\Delta}{s(s-b)}$
\sub{v} $\tan\dfrac{C}{2}=\sqrt{\dfrac{(s-a)(s-b)}{s(s-c)}}=\dfrac{\Delta}{s(s-c)}$

\itm{16} \B{অন্তর্ব্যাসার্ধ ($r$), পরিব্যাসার্ধ ($R$) ও ক্ষেত্রফলের ($\Delta$) সম্পর্ক:}
\sub{i} $\Delta = \dfrac{abc}{4R}$
\sub{ii} $\Delta = rs$
\sub{iii} $r = (s-a)\tan\dfrac{A}{2} = (s-b)\tan\dfrac{B}{2} = (s-c)\tan\dfrac{C}{2}$
\sub{iv} $rs = \dfrac{abc}{4R}$
\sub{v} $\dfrac{r}{R} = \dfrac{4(s-a)(s-b)(s-c)}{abc}$
\sub{vi} $r = 4R\sin\dfrac{A}{2}\sin\dfrac{B}{2}\sin\dfrac{C}{2}$

\itm{17} \B{বহির্বৃত্তের ব্যাসার্ধ ($r_a, r_b, r_c$):}
\sub{i} $r_a = \dfrac{\Delta}{s-a}, \quad r_b = \dfrac{\Delta}{s-b}, \quad r_c = \dfrac{\Delta}{s-c}$
\sub{ii} $\dfrac{1}{r_a} + \dfrac{1}{r_b} + \dfrac{1}{r_c} = \dfrac{1}{r}$

\itm{18} \B{কিছু গুরুত্বপূর্ণ ত্রিকোণমিতিক কোণের মান:}
\sub{i} $\tan15^\circ = 2 - \sqrt{3}$
\sub{ii} $\cos15^\circ = \sin75^\circ = \dfrac{\sqrt{3}+1}{2\sqrt{2}}$
\sub{iii} $\tan75^\circ = 2 + \sqrt{3}$
\sub{iv} $\sin18^\circ = \dfrac{\sqrt{5}-1}{4}$
\sub{v} $\sin15^\circ = \cos75^\circ = \dfrac{\sqrt{3}-1}{2\sqrt{2}}$
\sub{vi} $\cos36^\circ = \dfrac{\sqrt{5}+1}{4}$
\sub{vii} $\cos18^\circ = \dfrac{\sqrt{10+2\sqrt{5}}}{4}$
\sub{viii} $\tan7\dfrac{1}{2}^\circ = \sqrt{6} - \sqrt{3} + \sqrt{2} - 2$

\itm{19} \B{যদি } $A+B = 180^\circ$ \B{ হয় তবে বিশেষ ধর্ম:}
\sub{i} $\sin A - \sin B = 0$
\sub{ii} $\cos A + \cos B = 0$
\sub{iii} $\tan A + \tan B = 0$

\chsec{অধ্যায়-৮: ফাংশন ও ফাংশনের লেখচিত্র}

\itm{1} \B{ফাংশন ও এক-এক ফাংশন পরীক্ষা:}

\sub{i} Y\B{-অক্ষের সমান্তরাল রেখা পরীক্ষা (Vertical Line Test): কোনো সমীকরণ বা লেখচিত্র ফাংশন কি না তা যাচাই করার জন্য{\bn ।} যদি কোনো সমান্তরাল রেখা লেখচিত্রটিকে একাধিক বিন্দুতে ছেদ করে, তবে সেটি ফাংশন নয়{\bn ।}}

\sub{ii} X\B{-অক্ষের সমান্তরাল রেখা পরীক্ষা (Horizontal Line Test): কোনো ফাংশন এক-এক (One-to-One) কি না তা যাচাই করার জন্য{\bn ।} যদি কোনো সমান্তরাল রেখা লেখচিত্রটিকে একাধিক বিন্দুতে ছেদ করে, তবে সেটি এক-এক ফাংশন নয়{\bn ।}}

\itm{2} \B{সার্বিক ফাংশন (Onto Function):}
\B{কোনো ফাংশন } $f: A \to B$ \B{ সার্বিক হবে যদি এবং কেবল যদি ফাংশনটির রেঞ্জ ও কোডোমেন সমান হয়, অর্থাৎ } $R_f = B$\B{{\bn ।}}

\itm{3} \B{টাইপ-ভিত্তিক ডোমেন ও রেঞ্জ:}

\sub{i} $f(x) = ax + b \implies D_f = \mathbb{R};\quad R_f = \mathbb{R}$

\sub{ii} $f(x) = \dfrac{ax+b}{cx+d} \implies D_f = \mathbb{R} - \left\{-\dfrac{d}{c}\right\};\quad R_f = \mathbb{R} - \left\{\dfrac{a}{c}\right\}$

\sub{iii} $f(x) = \dfrac{x^2-a^2}{x-a} \implies D_f = \mathbb{R} - \{a\};\quad R_f = \mathbb{R} - \{2a\}$

\sub{iv} $f(x) = \sqrt{a^2-x^2} \implies D_f = [-a, a];\quad R_f = [0, a]$

\sub{v} $f(x) = \sqrt{x^2-a^2} \implies D_f = (-\infty, -a] \cup [a, \infty);\quad R_f = [0, \infty)$

\sub{vi} $f(x) = \log_k(a+bx) \implies D_f = \left(-\dfrac{a}{b}, \infty\right)\ [b > 0];\quad R_f = \mathbb{R}$

\sub{vii} $f(x) = e^{ax}\ \text{or}\ k^{ax} \implies D_f = \mathbb{R};\quad R_f = (0, \infty)$

\itm{4} \B{দ্বিঘাত ফাংশনের ডোমেন ও রেঞ্জ:}
$f(x) = ax^2 + bx + c$ \B{ এর ডোমেন } $D_f = \mathbb{R}$ \B{ এবং নিশ্চায়ক } $D = b^2 - 4ac$ \B{ হলে,}

\sub{i} $a > 0$ \B{ হলে রেঞ্জ, } $R_f = \left[-\dfrac{D}{4a}, \infty\right)$

\sub{ii} $a < 0$ \B{ হলে রেঞ্জ, } $R_f = \left(-\infty, -\dfrac{D}{4a}\right]$

\itm{5} \B{বিপরীত ফাংশন (Inverse Function):}

\sub{i} $f(x) = ax + b \implies f^{-1}(x) = \dfrac{x-b}{a}$

\sub{ii} $f(x) = \dfrac{ax+b}{cx+d} \implies f^{-1}(x) = \dfrac{-dx+b}{cx-a}$

\sub{iii} $f(x) = \dfrac{ax+b}{cx-a}$ \B{ হলে ফাংশনটি নিজেই নিজের বিপরীত{\bn ।} অর্থাৎ, } $f^{-1}(x) = f(x) \implies f(f(x)) = x$

\itm{6} \B{ত্রিকোণমিতিক বিশেষ ফাংশনের রেঞ্জ ও চরমমান:}
$f(x) = a\sin x + b\cos x + c$ \B{ হলে,}

\sub{i} \B{সর্বোচ্চ মান } $= c + \sqrt{a^2+b^2}$

\sub{ii} \B{সর্বনিম্ন মান } $= c - \sqrt{a^2+b^2}$

\sub{iii} \B{রেঞ্জ } $= \left[c - \sqrt{a^2+b^2},\ c + \sqrt{a^2+b^2}\right]$

\itm{7} \B{ত্রিকোণমিতিক ফাংশনের পর্যায় (Period) নির্ণয়:}

\sub{i} $\sin^n(ax+b)$, $\cos^n(ax+b)$, $\sec^n(ax+b)$, $\csc^n(ax+b)$ \B{ এর ক্ষেত্রে:}

\B{যদি } $n$ \B{ বিজোড় হয়, তবে পর্যায় } $= \dfrac{2\pi}{|a|}$

\B{যদি } $n$ \B{ জোড় হয়, তবে পর্যায় } $= \dfrac{\pi}{|a|}$

\sub{ii} $\tan^n(ax+b)$ \B{ এবং } $\cot^n(ax+b)$ \B{ এর ক্ষেত্রে } $n$ \B{ জোড় বা বিজোড় যাই হোক না কেন, পর্যায় } $= \dfrac{\pi}{|a|}$

\itm{8} \B{সংযোজিত ফাংশন (Composite Function) ও গুরুত্বপূর্ণ ধর্ম:}

\sub{i} $(g \circ f)(x) = g(f(x))$ \B{ এবং } $(f \circ g)(x) = f(g(x))$

\sub{ii} $e^{\ln x} = x$ \B{ এবং } $a^{\log_a x} = x$


\chsec{অধ্যায়-৯: লিমিট ও অন্তরীকরণ}

\itm{1} \B{লিমিটের অস্তিত্ব ও অবিচ্ছিন্নতা:}
\sub{i} $x = a$ \B{বিন্দুতে $f(x)$ ফাংশনের সীমা বিদ্যমান থাকবে যদি,} $\displaystyle\lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x)$ \B{হয়{\bn ।}}
\sub{ii} $x = a$ \B{বিন্দুতে $f(x)$ অবিচ্ছিন্ন হওয়ার শর্ত:} $f(a) = \displaystyle\lim_{x\to a^-} f(x) = \lim_{x\to a^+} f(x)$
\sub{iii} \B{কোনো ফাংশনের বিপরীত ফাংশন পাওয়া যাবে যদি এবং কেবল যদি ফাংশনটি এক-এক ও সার্বিক হয়{\bn ।}}

\itm{2} \B{লিমিটের ধর্মসমূহ:}
\sub{i} $\displaystyle\lim_{x\to a}[f(x) \pm g(x)] = \lim_{x\to a}f(x) \pm \lim_{x\to a}g(x)$
\sub{ii} $\displaystyle\lim_{x\to a}[f(x) \cdot g(x)] = \lim_{x\to a}f(x) \times \lim_{x\to a}g(x)$
\sub{iii} $\displaystyle\lim_{x\to a} \frac{1}{f(x)} = \frac{1}{\displaystyle\lim_{x\to a} f(x)}$
\sub{iv} $\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)} = \frac{\displaystyle\lim_{x\to a}f(x)}{\displaystyle\lim_{x\to a}g(x)}$
\sub{v} $\displaystyle\lim_{x\to a} \sqrt[n]{f(x)} = \sqrt[n]{\displaystyle\lim_{x\to a} f(x)}$
\sub{vi} $\displaystyle\lim_{x\to a} c \cdot f(x) = c \cdot \lim_{x\to a} f(x)$
\sub{vii} $\displaystyle\lim_{x\to a} c = c$ \B{ [এখানে, $c =$ ধ্রুবক]}

\itm{3} \B{লিমিটের প্রমিত সূত্রাবলী:}
$\displaystyle\lim_{x\to0}\frac{\sin x}{x} = \lim_{x\to0}\frac{x}{\sin x} = \lim_{x\to0}\frac{\sin^{-1}x}{x} = 1$
$\displaystyle\lim_{x\to0}\frac{\tan x}{x} = \lim_{x\to0}\frac{x}{\tan x} = \lim_{x\to0}\frac{\tan^{-1}x}{x} = 1$
$\displaystyle\lim_{x\to0}\frac{\ln(1+x)}{x} = 1$
$\displaystyle\lim_{x\to0}\frac{e^x-1}{x} = 1$
$\displaystyle\lim_{x\to0}\frac{(1+x)^n-1}{x} = n$
$\displaystyle\lim_{x\to a}\frac{x^n-a^n}{x-a} = na^{n-1}$
$\displaystyle\lim_{x\to a}\frac{x^m-a^m}{x^n-a^n} = \frac{m}{n}a^{m-n}$
$\displaystyle\lim_{x\to\infty}\left(1+\frac{1}{x}\right)^x = e$
$\displaystyle\lim_{x\to0}(1+x)^{\frac{1}{x}} = e$
$\displaystyle\lim_{x\to\infty}\left(1+\frac{m}{x}\right)^{nx} = e^{mn}$
$\displaystyle\lim_{x\to0}(1+mx)^{\frac{n}{x}} = e^{mn}$
$\displaystyle\lim_{h\to0}\frac{f(x+h)-f(x)}{h} = \frac{d}{dx}f(x)$

\itm{4} \B{কিছু গুরুত্বপূর্ণ General Form (Limits):}
\sub{i} $\displaystyle\lim_{x\to\infty} a^x \sin\frac{b}{a^x} = b$ \B{ [যখন, $a > 0$]}
\sub{ii} $\displaystyle\lim_{x\to0} (1+ax)^{\frac{bx+c}{dx}} = e^{\frac{ac}{dx}}$
\sub{iii} $\displaystyle\lim_{x\to\infty} \left(\frac{x+a}{x+b}\right)^x = e^{a-b}$
\sub{iv} $\displaystyle\lim_{x\to0} \frac{\sqrt{1+ax} - \sqrt{1-bx}}{x} = \frac{a+b}{2}$
\sub{v} $\displaystyle\lim_{x\to0} \frac{\sqrt[n]{1+ax} - \sqrt[n]{1-bx}}{x} = \frac{a-b}{2}$
\sub{vi} $\displaystyle\lim_{x\to0} \frac{1-\cos ax}{bx^2} = \frac{a^2}{2b}$
\sub{vii} $\displaystyle\lim_{x\to0} \frac{1-\cos ax}{1-\cos bx} = \frac{a^2}{b^2}$
\sub{viii} $\displaystyle\lim_{x\to0} \frac{\cos ax - \cos bx}{\cos cx - \cos dx} = \frac{a^2-b^2}{c^2-d^2}$
\sub{ix} $\displaystyle\lim_{x\to0} \frac{\tan ax - \sin ax}{x^3} = \frac{a^3}{2}$
\sub{x} $\displaystyle\lim_{x\to\infty} \{\ln(ax+b) - \ln(cx+d)\} = \ln\frac{a}{c}$
\sub{xi} $\displaystyle\lim_{x\to0} \frac{\sin ax}{\sin bx} = \frac{a}{b}$

\itm{5} \B{মূলনিয়মে অন্তরীকরণের সূত্র:}
$\dfrac{d}{dx}\{f(x)\} = \displaystyle\lim_{h\to0}\dfrac{f(x+h)-f(x)}{h}$

\itm{6} \B{অন্তরীকরণের সাধারণ নিয়মাবলী:}
\sub{i} $\dfrac{d}{dx}(c) = 0$ \B{ [যখন, $c$ ধ্রুবক]}
\sub{ii} $\dfrac{d}{dx}\{cf(x)\} = c\dfrac{d}{dx}\{f(x)\}$
\sub{iii} $\dfrac{d}{dx}(u \pm v \pm w) = \dfrac{du}{dx} \pm \dfrac{dv}{dx} \pm \dfrac{dw}{dx}$
\sub{iv} $\dfrac{d}{dx}(uv) = u\dfrac{dv}{dx} + v\dfrac{du}{dx}$ \B{ [$u,v$ উভয়ই $x$-এর ফাংশন]}
\sub{v} $\dfrac{d}{dx}(uvw) = uv\dfrac{dw}{dx} + uw\dfrac{dv}{dx} + vw\dfrac{du}{dx}$
\sub{vi} $\dfrac{d}{dx}\left(\dfrac{u}{v}\right) = \dfrac{v\dfrac{du}{dx} - u\dfrac{dv}{dx}}{v^2}$
\sub{vii} $\dfrac{d}{dx}\left(\dfrac{u}{v}\cdot\dfrac{w}{x}\right) = \dots$ \B{ [পর্যায়ক্রমিক নিয়মে গুণ ও ভাগফল]}
\sub{viii} $\dfrac{d}{dx}(u^v) = u^v\left[v\cdot\dfrac{d}{dx}(\ln u) + \ln u\cdot\dfrac{dv}{dx}\right]$
\sub{ix} \B{চেইন রুল:} $y = f(z)$ \B{এবং} $z = f(x)$ \B{হলে,} $\dfrac{dy}{dx} = \dfrac{dy}{z} \times \dfrac{dz}{dx}$

\itm{7} \B{অন্তরীকরণের প্রমিত সূত্রাবলী:}
\sub{i} $\dfrac{d}{dx}(x^n) = nx^{n-1}$
\sub{ii} $\dfrac{d}{dx}(\sqrt{x}) = \dfrac{1}{2\sqrt{x}}$
\sub{iii} $\dfrac{d}{dx}(e^x) = e^x$
\sub{iv} $\dfrac{d}{dx}(e^{mx}) = me^{mx}$
\sub{v} $\dfrac{d}{dx}(a^x) = a^x\ln a$
\sub{vi} $\dfrac{d}{dx}(\ln x) = \dfrac{1}{x}$
\sub{vii} $\dfrac{d}{dx}(\log_a x) = \dfrac{1}{x}\log_a e = \dfrac{1}{x\ln a}$
\sub{viii} $\dfrac{d}{dx}(\sin x) = \cos x$
\sub{ix} $\dfrac{d}{dx}(\cos x) = -\sin x$
\sub{x} $\dfrac{d}{dx}(\tan x) = \sec^2 x$
\sub{xi} $\dfrac{d}{dx}(\cot x) = -\csc^2 x$
\sub{xii} $\dfrac{d}{dx}(\sec x) = \sec x\tan x$
\sub{xiii} $\dfrac{d}{dx}(\csc x) = -\csc x\cot x$
\sub{xiv} $\dfrac{d}{dx}(\sin^{-1}x) = \dfrac{1}{\sqrt{1-x^2}}$
\sub{xv} $\dfrac{d}{dx}(\cos^{-1}x) = \dfrac{-1}{\sqrt{1-x^2}}$
\sub{xvi} $\dfrac{d}{dx}(\tan^{-1}x) = \dfrac{1}{1+x^2}$
\sub{xvii} $\dfrac{d}{dx}(\cot^{-1}x) = \dfrac{-1}{1+x^2}$
\sub{xviii} $\dfrac{d}{dx}(\sec^{-1}x) = \dfrac{1}{x\sqrt{x^2-1}}$
\sub{xviii} $\dfrac{d}{dx}(\csc^{-1}x) = \dfrac{-1}{x\sqrt{x^2-1}}$

\itm{8} \B{প্রতিস্থাপন পদ্ধতিতে অন্তরক সহগ নির্ণয়ের কৌশল:}
\begin{safetable}\begin{tabular}{|>{\centering\arraybackslash}p{0.45\linewidth}|>{\centering\arraybackslash}p{0.45\linewidth}|}
\hline
\B{Term এর আকৃতি} & \B{যা ধরতে হবে} \\ \hline
$1-x^2$ & $x = \sin\theta$ \B{বা} $\cos\theta$ \\
$1+x^2$ & $x = \tan\theta$ \B{বা} $\cot\theta$ \\
$x^2-1$ & $x = \sec\theta$ \B{বা} $\csc\theta$ \\
$\sqrt{\dfrac{1-x}{1+x}}$ \B{এবং} $\sqrt{\dfrac{1+x}{1-x}}$ & $x = \cos\theta$ \B{বা} $\cos2\theta$ \\
$\dfrac{2x}{1\pm x^2}$ \B{এবং} $\dfrac{1-x^2}{1+x^2}$ & $x = \tan\theta$ \\
$\dfrac{1-x}{a+x}$ \B{এবং} $\dfrac{1-x}{1-ax}$ \B{বা} $\dfrac{a-x}{a+x}$ & $x = a\tan\theta$ \B{বা} $x = a\cos\theta$ \\
\hline
\end{tabular}\end{safetable}

\itm{9} \B{অব্যক্ত ফাংশন (Implicit Function) সংক্রান্ত শর্টকাট:}
\sub{i} \B{যদি} $f(x,y)=0$ \B{হয় তবে,} $\dfrac{dy}{dx} = -\dfrac{f_x}{f_y} = -\dfrac{y \text{ কে ধ্রুবক রেখে } x \text{ এর সাপেক্ষে অন্তরীকরণ}}{x \text{ কে ধ্রুবক রেখে } y \text{ এর সাপেক্ষে অন্তরীকরণ}}$
\sub{ii} $y = \sqrt{f(x) + \sqrt{f(x) + \sqrt{f(x) + \dots}}}$ \B{হলে,} $\dfrac{dy}{dx} = \dfrac{f'(x)}{2y-1}$
\sub{iii} $x^a \cdot y^b = (x \pm y)^{a+b}$ \B{হলে,} $\dfrac{dy}{dx} = \dfrac{y}{x}$

\itm{10} \B{ফাংশনের সাপেক্ষে ফাংশনের Differentiation:}
$g(x)$ \B{এর সাপেক্ষে} $f(x)$ \B{এর অন্তরীকরণ} $= \dfrac{\dfrac{d}{dx}f(x)}{\dfrac{d}{dx}g(x)} = \dfrac{f'(x)}{g'(x)}$

\itm{11} \B{পর্যায়ক্রমিক অন্তরীকরণ ($n$-তম অন্তরজ):}
\sub{i} $y = x^n$ \B{হলে,} $y_r = {^n}P_r \cdot x^{n-r}$ \B{ [যখন $n \ge r$];} $y_n = n!$ \B{ [যখন $n=r$] এবং} $y_r = 0$ \B{ [যখন $n<r$]}
\sub{ii} $y = e^{ax}$ \B{হলে,} $y_n = a^n \cdot e^{ax}$
\sub{iii} $y = e^{ax}\sin bx$ \B{হলে,} $y_n = r^n \cdot e^{ax} \cdot \sin(bx+n\theta)$ \B{ [যেখানে, $r = \sqrt{a^2+b^2}$ এবং $\theta = \tan^{-1}\frac{b}{a}$]}
\sub{iv} $y = e^{ax}\cos bx$ \B{হলে,} $y_n = r^n \cdot e^{ax} \cdot \cos(bx+n\theta)$ \B{ [যেখানে, $r = \sqrt{a^2+b^2}$ এবং $\theta = \tan^{-1}\frac{b}{a}$]}
\sub{v} $y = \dfrac{1}{ax+b}$ \B{হলে,} $y_n = \dfrac{(-1)^n \cdot n! \cdot a^n}{(ax+b)^{n+1}}$
\sub{vi} $y = \ln(ax+b)$ \B{হলে,} $y_n = \dfrac{(-1)^{n-1} \cdot (n-1)! \cdot a^n}{(ax+b)^n}$
\sub{vii} $y = \sin(ax+b)$ \B{হলে,} $y_n = a^n \cdot \sin\left(\frac{n\pi}{2} + (ax+b)\right)$
\sub{viii} $y = \sin x$ \B{হলে,} $y_n = \sin\left(\frac{n\pi}{2} + x\right)$
\sub{ix} $y = \cos(ax+b)$ \B{হলে,} $y_n = a^n \cdot \cos\left(\frac{n\pi}{2} + (ax+b)\right)$
\sub{x} $y = a^x$ \B{হলে,} $y_n = (\ln a)^n \cdot a^x$

\itm{12} \B{ম্যাকলরিনের উপপাদ্য (Maclaurin's Theorem):}
$f(x) = f(0) + \frac{x}{1!}f'(0) + \frac{x^2}{2!}f''(0) + \frac{x^3}{3!}f'''(0) + \dots + \frac{x^n}{n!}f^{(n)}(0) + \dots$

\itm{13} \B{অন্তরীকরণের জ্যামিতিক প্রয়োগ ও স্পর্শক-অভিলম্ব:}
\sub{i} $\dfrac{dy}{dx}$ \B{দ্বারা বোঝায়:} $x$ \B{এর সাপেক্ষে $y$ এর পরিবর্তনের হার, তাৎক্ষণিক পরিবর্তন, অথবা $y=f(x)$ বক্ররেখার যেকোনো বিন্দুতে অঙ্কিত স্পর্শকের ঢাল{\bn ।}}
\sub{ii} $(x_1, y_1)$ \B{বিন্দুতে অঙ্কিত স্পর্শকের সমীকরণ:} $y - y_1 = \left(\dfrac{dy}{dx}\right)_{(x_1,y_1)}(x - x_1)$
\sub{iii} $(x_1, y_1)$ \B{বিন্দুতে অঙ্কিত অভিলম্বের সমীকরণ:} $y - y_1 = \dfrac{-1}{\left(\dfrac{dy}{dx}\right)_{(x_1,y_1)}}(x - x_1)$ \B{বা,} $(x-x_1) + \dfrac{dy}{dx}(y-y_1) = 0$
\sub{iv} \B{স্পর্ষক $x$-অক্ষের ধনাত্মক দিকের সাথে $\theta$ কোণ উৎপন্ন করলে ঢাল,} $m = \tan\theta$
\sub{v} \B{স্পর্শক $x$-অক্ষের সমান্তরাল বা $y$-অক্ষের উপর লম্ব হলে,} $\dfrac{dy}{dx} = \tan0^\circ = 0$
\sub{vi} \B{স্পর্শক $y$-অক্ষের সমান্তরাল বা $x$-অক্ষের উপর লম্ব হলে,} $\dfrac{dx}{dy} = 0$ \B{বা} $\dfrac{dy}{dx} = \infty$
\sub{vii} \B{স্পর্শক উভয় অক্ষের সাথে সমান কোণ উৎপন্ন করলে,} $\dfrac{dy}{dx} = \pm1$

\itm{14} \B{পরিবর্তনের হার সংক্রান্ত সূত্রাবলী:}
\sub{i} \B{বৃত্তের ক্ষেত্রে:} $\dfrac{dA}{dt} = 2\pi r \cdot \dfrac{dr}{dt}$, $\dfrac{dp}{dt} = 2\pi \cdot \dfrac{dr}{dt}$, $\dfrac{dA}{dt} = r \cdot \dfrac{dp}{dt}$ \B{ [যেখানে, $r=$ ব্যাসার্ধ, $A=$ ক্ষেত্রফল, $p=$ পরিধি]}
\sub{ii} \B{গোলকের ক্ষেত্রে:} $\dfrac{dA}{dt} = 8\pi r \cdot \dfrac{dr}{dt}$, $\dfrac{dV}{dt} = 4\pi r^2 \cdot \dfrac{dr}{dt}$, $\dfrac{dA}{dt} = \dfrac{2}{r}\cdot\dfrac{dV}{dt}$ \B{ [যেখানে, $V=$ আয়তন, $A=$ পৃষ্ঠের ক্ষেত্রফল]}

\itm{15} \B{ফাংশনের লঘু ও গুরুমান (Maxima and Minima):}
\sub{i} \B{চরম বিন্দুতে (Maximum বা Minimum বিন্দুতে) স্পর্শকের ঢাল,} $\dfrac{dy}{dx} = 0$
\sub{ii} \B{প্রয়োজনীয় ধাপসমূহ:} $y = f(x)$ ফাংশনের জন্য প্রথমে $\dfrac{dy}{dx}$ ও $\dfrac{d^2y}{dx^2}$ নির্ণয় করতে হবে{\bn ।}
\sub{iii} $\dfrac{dy}{dx} = 0$ \B{ধরে $x$ এর মানসমূহ নির্ণয় করতে হবে{\bn ।}}
\sub{iv} $x$ \B{এর যে মানের জন্য} $\dfrac{d^2y}{dx^2} = (-)\text{ve}$ \B{হবে, সেই মানের জন্য $f(x)$ ফাংশনটির গুরুমান (Maximum value) পাওয়া যাবে{\bn ।}}
\sub{v} $x$ \B{এর যে মানের জন্য} $\dfrac{d^2y}{dx^2} = (+)\text{ve}$ \B{হবে, সেই মানের জন্য $f(x)$ ফাংশনটির লঘূমান (Minimum value) পাওয়া যাবে{\bn ।}}
\sub{vi} $x$ \B{এর মান অবাস্তব হলে বা $f''(x)=0$ হলে ফাংশনটির চরমমান নেই{\bn ।}}

\itm{16} \B{বৃদ্ধিপ্রাপ্ত (ক্রমবর্ধমান) ও হ্রাসপ্রাপ্ত (ক্রমহ্রাসমান) ফাংশন:}
\sub{i} \B{for increasing function,} $\dfrac{dy}{dx} > 0$
\sub{ii} \B{for decreasing function,} $\dfrac{dy}{dx} < 0$

\itm{17} \B{ফাংশনের সর্বোচ্চ ও সর্বনিম্ন মানের শর্টকাট:}
\sub{i} $ax^2 + bx + c$ \B{এর সর্বোচ্চ/সর্বনিম্ন মান} $= c - \dfrac{b^2}{4a}$
\sub{ii} $a\sin x \pm b\cos x + c$ \B{এর সর্বোচ্চ মান} $= c + \sqrt{a^2+b^2}$ \B{এবং সর্বনিম্ন মান} $= c - \sqrt{a^2+b^2}$
\sub{iii} $\dfrac{x}{\ln x}$ \B{এর লঘুমান} $= e$
\sub{iv} $\dfrac{ln x}{x}$ \B{এর গুরুমান} $= \dfrac{1}{e}$

---

\chsec{অধ্যায়-১০: যোগজীকরণ}

\itm{1} \B{অনির্দিষ্ট যোগজের সাধারণ সূত্রসমূহ (প্রত্যেকটির শেষে $+c$ দিতে হবে):}
\sub{i} $\int x^n dx = \dfrac{x^{n+1}}{n+1} + c \quad [n \neq -1]$
\sub{ii} $\dfrac{d}{dx}\left[\int f(x)dx\right] = f(x)$
\sub{iii} $\int \left[\dfrac{d}{dx}(f(x))\right] dx = f(x) + c$
\sub{iv} $\int dx = x + c$
\sub{v} $\int \dfrac{dx}{\sqrt{x}} = 2\sqrt{x} + c$
\sub{vi} $\int m \cdot f(x)dx = m \cdot \int f(x)dx \quad [m = \text{ধ্রুবক}]$
\sub{vii} $\int \sin x \, dx = -\cos x + c$
\sub{viii} $\int \cos x \, dx = \sin x + c$
\sub{ix} $\int \sec^2 x \, dx = \tan x + c$
\sub{x} $\int \csc^2 x \, dx = -\cot x + c$
\sub{xi} $\int \sec x \cdot \tan x \, dx = \sec x + c$
\sub{xii} $\int \csc x \cdot \cot x \, dx = -\csc x + c$
\sub{xiii} $\int (ax + b)^n dx = \dfrac{(ax+b)^{n+1}}{a(n+1)} + c$
\sub{xiv} $\int (u \pm v \pm w)dx = \int u\,dx \pm \int v\,dx \pm \int w\,dx$
\sub{xv} $\int e^x dx = e^x + c$
\sub{xvi} $\int e^{mx} dx = \dfrac{e^{mx}}{m} + c$
\sub{xvii} $\int \dfrac{1}{x} dx = \ln |x| + c$
\sub{xviii} $\int a^x dx = \dfrac{a^x}{\ln a} + c$
\sub{xix} $\int \dfrac{1}{ax+b} dx = \dfrac{1}{a}\ln|ax+b| + c$
\sub{xx} $\int \cos ax \, dx = \dfrac{\sin ax}{a} + c$
\sub{xxi} $\int \sin ax \, dx = -\dfrac{\cos ax}{a} + c$
\sub{xxii} $\int \sec^2 ax \, dx = \dfrac{\tan ax}{a} + c$
\sub{xxiii} $\int \csc^2 ax \, dx = -\dfrac{\cot ax}{a} + c$
\sub{xxiv} $\int \sec ax \cdot \tan ax \, dx = \dfrac{\sec ax}{a} + c$
\sub{xxv} $\int \csc ax \cdot \cot ax \, dx = -\dfrac{\csc ax}{a} + c$
\sub{xxvi} $\int \tan x \, dx = \ln|\sec x| + c = -\ln|\cos x| + c$
\sub{xxvii} $\int \cot x \, dx = \ln|\sin x| + c$
\sub{xxviii} $\int \sec x \, dx = \ln|\sec x + \tan x| + c = \ln\left|\tan\left(\frac{x}{2}+\frac{\pi}{4}\right)\right| + c$
\sub{xxix} $\int \csc x \, dx = \ln|\csc x - \cot x| + c = \ln\left|\tan\dfrac{x}{2}\right| + c$

\itm{2} \B{বিপরীত ত্রিকোণমিতিক ফাংশন সংক্রান্ত যোগজ সূত্রাবলী:}
\sub{i} $\int \dfrac{1}{1+x^2} dx = \tan^{-1}x + c$
\sub{ii} $\int \dfrac{-1}{1+x^2} dx = \cot^{-1}x + c$
\sub{iii} $\int \dfrac{1}{\sqrt{1-x^2}} dx = \sin^{-1}x + c$
\sub{iv} $\int \dfrac{-1}{\sqrt{1-x^2}} dx = \cos^{-1}x + c$
\sub{v} $\int \dfrac{1}{x\sqrt{x^2-1}} dx = \sec^{-1}x + c$
\sub{vi} $\int \dfrac{-1}{x\sqrt{x^2-1}} dx = \csc^{-1}x + c$
\sub{vii} $\int \dfrac{dx}{a^2+x^2} = \dfrac{1}{a}\tan^{-1}\dfrac{x}{a} + c$
\sub{viii} $\int \dfrac{dx}{\sqrt{a^2-x^2}} = \sin^{-1}\dfrac{x}{a} + c$
\sub{ix} $\int \dfrac{dx}{x\sqrt{x^2-a^2}} = \dfrac{1}{a}\sec^{-1}\dfrac{x}{a} + c$
\sub{x} $\int \dfrac{dx}{x^2-a^2} = \dfrac{1}{2a}\ln\left|\dfrac{x-a}{x+a}\right| + c$
\sub{xi} $\int \dfrac{dx}{a^2-x^2} = \dfrac{1}{2a}\ln\left|\dfrac{a+x}{a-x}\right| + c$
\sub{xii} $\int \dfrac{dx}{\sqrt{x^2+a^2}} = \ln|x+\sqrt{x^2+a^2}| + c$
\sub{xiii} $\int \dfrac{dx}{\sqrt{x^2-a^2}} = \ln|x+\sqrt{x^2-a^2}| + c$
\sub{xiv} $\int \sqrt{a^2-x^2} dx = \dfrac{x}{2}\sqrt{a^2-x^2} + \dfrac{a^2}{2}\sin^{-1}\dfrac{x}{a} + c$
\sub{xv} $\int \sqrt{a^2+x^2} dx = \dfrac{x}{2}\sqrt{a^2+x^2} + \dfrac{a^2}{2}\ln|x+\sqrt{a^2+x^2}| + c$
\sub{xvi} $\int \sqrt{x^2-a^2} dx = \dfrac{x}{2}\sqrt{x^2-a^2} - \dfrac{a^2}{2}\ln|x+\sqrt{x^2-a^2}| + c$

\itm{3} \B{ইউ-ভি পদ্ধতি (Integration by Parts):}
$\int u \cdot v \, dx = u \int v \, dx - \int \left\{ \dfrac{d}{dx}(u) \cdot \int v \, dx \right\} dx$
\B{ইউ ($u$) নির্ধারণের জন্য ক্রম (LIATE নিয়ম):}
$$\text{L (Logarithmic) } \rightarrow \text{I (Inverse) } \rightarrow \text{A (Algebraic) } \rightarrow \text{T (Trigonometric) } \rightarrow \text{E (Exponential)}$$
\B{আগে যেটি আসবে তা $u$, পরে যেটি আসবে তা $v${\bn ।}}

\itm{4} \B{কিছু সাধারণ আকৃতির রূপ (General Forms):}
\sub{i} $\int [f(x)]^n \cdot f'(x) \, dx = \dfrac{[f(x)]^{n+1}}{n+1} + c$
\sub{ii} $\int e^{f(x)} \cdot f'(x) \, dx = e^{f(x)} + c$
\sub{iii} $\int \dfrac{f'(x)}{f(x)} \, dx = \ln|f(x)| + c$
\sub{iv} $\int \dfrac{f'(x)}{\sqrt{f(x)}} \, dx = 2\sqrt{f(x)} + c$
\sub{v} $\int e^{ax} \cdot [a \cdot f(x) + f'(x)] \, dx = e^{ax} \cdot f(x) + c$
\sub{vi} $\int e^x \cdot [f(x) + f'(x)] \, dx = e^x \cdot f(x) + c$

\itm{5} \B{কিছু বিশেষ পদ্ধতির প্রতিস্থাপন কৌশল:}
\sub{i} $\int \dfrac{dx}{\sqrt{ax+b} + \sqrt{ax+c}}$ \B{আকৃতির ক্ষেত্রে লব ও হরকে হরের অনুবন্ধী রাশি দ্বারা গুণ করতে হবে{\bn ।}}
\sub{ii} $\int \sqrt{ax+b}\cdot(cx+d)dx$ \B{আকৃতির ক্ষেত্রে, $(ax+b) = t^2$ ধরতে হবে{\bn ।}}
\sub{iii} $\int \dfrac{(a+bx)^m}{(c+dx)^n} dx$ \B{ [যেখানে $m \rightarrow$ ধনাত্মক পূর্ণসংখ্যা, $n \rightarrow$ মূলদ], এক্ষেত্রে, $c+dx = t$ ধরতে হবে{\bn ।}}
\sub{iv} $\int \dfrac{dx}{a+be^{mx}}$ \B{থাকলে, লব ও হরকে $e^{-mx}$ দ্বারা এবং $\int \dfrac{dx}{a+be^{-mx}}$ থাকলে, লব ও হরকে $e^{mx}$ দ্বারা গুণ করতে হবে{\bn ।}}
\sub{v} $\int \dfrac{dx}{a+b\sin^2x}$, $\int \dfrac{dx}{a+b\cos^2x}$, $\int \dfrac{dx}{a^2\sin^2x + b^2\cos^2x}$ \B{থাকলে লব ও হরকে $\cos^2x$ দ্বারা ভাগ করে $\tan x = t$ ধরতে হবে{\bn ।}}
\sub{vi} $\int \dfrac{x^2 \pm 1}{x^4 + kx^2 + 1} dx$ \B{থাকলে, $x^2$ দ্বারা লব ও হরকে ভাগ করে $\left(x+\frac{1}{x}\right)=t$ অথবা $\left(x-\frac{1}{x}\right)=t$ ধরতে হবে{\bn ।}}
\sub{vii} $\int \dfrac{dx}{(a\sin x + b\cos x)^n}$ \B{থাকলে, $a = r\cos\theta$ এবং $b = r\sin\theta$ ধরতে হবে{\bn ।}}

\itm{6} \B{MCQ Special যোগজ সূত্রাবলী:}
\sub{i} $\int \dfrac{dx}{ax^2+bx+c} = \dfrac{2}{\sqrt{|D|}} \cdot \tan^{-1}\dfrac{f'(x)}{\sqrt{|D|}} + c$ \B{ [যখন নিশ্চায়ক, $D < 0$]}
\sub{ii} $\int \dfrac{a\sin x + b\cos x}{c\sin x + d\cos x} \, dx = \dfrac{ac+bd}{c^2+d^2}x + \dfrac{bc-ad}{c^2+d^2}\ln|c\sin x + d\cos x| + c$
\sub{iii} $\int \dfrac{dx}{\sqrt{(x-\alpha)(\beta-x)}} = \sin^{-1}\left(\dfrac{2x-(\alpha+\beta)}{\beta-\alpha}\right) + c$
\sub{iv} $\int e^{ax} \cdot x^n \, dx = e^{ax}\left[ \dfrac{x^n}{a} - \dfrac{n\cdot x^{n-1}}{a^2} + \dfrac{n(n-1)x^{n-2}}{a^3} - \dots \right]$ \B{ [ধ্রুবক পদ না আসা পর্যন্ত পর্যায়ক্রমে অন্তরীকরণ চালাতে হবে]}
\sub{v} $\begin{matrix} \int e^{ax}\sin(bx+c)dx \\ \int e^{ax}\cos(bx+c)dx \end{matrix} \Bigg\} = \dfrac{T \cdot E_D - E \cdot T_D}{a^2+b^2}$ \B{ [যেখানে $T=$ Trigonometric, $E=$ Exponential; $T_D$ ও $E_D$ যথাক্রমে এদের Differentiation]}
\sub{vi} $\int \dfrac{dx}{f(x)\sqrt{\{f(x)\}^2-1}} = \dfrac{\sec^{-1}f(x)}{f'(x)} + c \quad [f(x) = \text{Linear function}]$

\itm{7} \B{নির্দিষ্ট যোগজের সূত্রাবলী (Properties of Definite Integrals):}
\sub{i} $\int_a^b f(x)dx = \int_a^b f(a+b-x)dx$
\sub{ii} $\int_a^b f(x)dx = -\int_b^a f(x)dx$
\sub{iii} $\int_a^b f(x)dx = \int_a^c f(x)dx + \int_c^b f(x)dx \quad [a < c < b]$
\sub{iv} $\int_a^b f(x)dx = p \cdot \int_{a/p}^{b/p} f(px)dx$
\sub{v} \B{যদি} $f(x) = f(2a-x)$ \B{হয়, তবে} $\int_0^{2a} f(x)dx = 2 \cdot \int_0^a f(x)dx$
\sub{vi} \B{যদি} $f(x) = -f(-x)$ \B{ [বিজড় ফাংশন] হয়, তবে} $\int_{-a}^a f(x)dx = 0$
\sub{vii} \B{যদি} $f(x) = f(-x)$ \B{ [জোড় ফাংশন] হয়, তবে} $\int_{-a}^a f(x)dx = 2 \cdot \int_0^a f(x)dx$
\sub{viii} $\int_a^b f(x)dx = \int_a^b f(t)dt$

\itm{8} \B{নির্দিষ্ট যোগজের শর্টকাট (Definite Integral Shortcuts):}
\sub{i} $\int_a^b \dfrac{\sin^n x}{\sin^n x + \cos^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, $a+b = \frac{\pi}{2}$]}
\sub{ii} $\int_a^b \dfrac{\tan^n x}{\tan^n x + \cot^n x} dx = \int_a^b \dfrac{\cot^n x}{\tan^n x + \cot^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, $a+b = \frac{\pi}{2}$]}
\sub{iii} $\int_a^b \dfrac{\sec^n x}{\sec^n x + \csc^n x} dx = \int_a^b \dfrac{\csc^n x}{\sec^n x + \csc^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, $a+b = \frac{\pi}{2}$]}
\sub{iv} $\int_0^\pi \dfrac{dx}{a+b\cos x} = \int_0^\pi \dfrac{dx}{a+b\sin x} = \dfrac{\pi}{\sqrt{a^2-b^2}}$
\sub{v} $\int_0^\infty e^{-ax} \cdot \cos bx \, dx = \dfrac{a}{a^2+b^2}$
\sub{vi} $\int_0^\infty e^{-ax} \cdot \sin bx \, dx = \dfrac{b}{a^2+b^2}$
\sub{vii} $\int_0^a \sqrt{\dfrac{a+x}{a-x}} dx = \dfrac{\pi a}{2} + a$
\sub{viii} $\int_0^a \sqrt{\dfrac{a-x}{a+x}} dx = \dfrac{\pi a}{2} - a$
\sub{ix} $\int_0^a \dfrac{dx}{\sqrt{2ax-x^2}} = \dfrac{\pi}{2}$
\sub{x} $\int_0^a \sqrt{a^2-x^2} dx = \dfrac{\pi a^2}{4}$
\sub{xi} $\int_0^a \dfrac{1}{\sqrt{a^2-x^2}} dx = \dfrac{\pi}{2}$

\itm{9} \B{ওয়ালিস উপপাদ্য (Walli's Theorem):}
$\int_0^{\frac{\pi}{2}} \sin^n x \, dx = \int_0^{\frac{\pi}{2}} \cos^n x \, dx$
$$= \dfrac{n-1}{n} \times \dfrac{n-3}{n-2} \times \dfrac{n-5}{n-4} \times \dots \times \dfrac{3}{4} \times \dfrac{1}{2} \times \dfrac{\pi}{2} \quad \text{[\B{যখন, } $n =$ জোড়]}$$
$$= \dfrac{n-1}{n} \times \dfrac{n-3}{n-2} \times \dfrac{n-5}{n-4} \times \dots \times \dfrac{4}{5} \times \dfrac{2}{3} \times 1 \quad \text{[\B{যখন, } $n =$ বিজোড়]}$$

\itm{10} \B{ক্ষেত্রফল নির্ণয় সংক্রান্ত সাধারণ তত্ত্ব:}
\sub{i} \B{নির্দিষ্ট যোগজ} $A = \int_a^b y \, dx = \int_a^b f(x)dx$ \B{যা, $y=f(x)$ বক্ররেখা, $x$-অক্ষ এবং $x=a$ ও $x=b$ দুটি নির্দিষ্ট ভুজ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল নির্দেশ করে{\bn ।}}
\sub{ii} \B{নির্দিষ্ট যোগজ} $A = \int_c^d x \, dy = \int_c^d f(y)dy$ \B{যা, $x=f(y)$ বক্ররেখা, $y$-অক্ষ এবং $y=c$ ও $y=d$ দুটি নির্দিষ্ট কোটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল নির্দেশ করে{\bn ।}}
\sub{iii} $y_1 = f(x_1)$ \B{ও} $y_2 = f(x_2)$ \B{বক্ররেখা এবং $x=a$ ও $x=b$ ভুজ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল,} $A = \int_a^b (y_2 - y_1)dx = \int_a^b [f_2(x) - f_1(x)]dx$
\sub{iv} $x_1 = f(y_1)$ \B{এবং} $x_2 = f(y_2)$ \B{বক্ররেখা এবং $y=c$ ও $y=d$ কোটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল,} $A = \int_c^d (x_1 - x_2)dy = \int_c^d [f_1(y) - f_2(y)]dy$

\itm{11} \B{ক্ষেত্রফল সংক্রান্ত শর্টকাট সূত্রাবলী (MCQ Special):}
\sub{1} $\dfrac{x}{a} + \dfrac{y}{b} = 1$ \B{রেখা এবং স্থানাঙ্কের অক্ষদ্বয় দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{1}{2}ab$
\sub{2} $x + y = a$ \B{রেখা এবং স্থানাঙ্কের অক্ষদ্বয় দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{1}{2}a^2$
\sub{3} $x = a, x = b, y = c$ \B{এবং} $y = d$ \B{রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= (b-a)(d-c)$ \B{ [এখানে $a < b$ এবং $c < d$]}
\sub{4} $y = |x|$ \B{এবং} $y = b$ \B{রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= b^2$
\sub{5} $y = -|x|$ \B{এবং} $y = -b$ \B{রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= b^2$
\sub{6} $y = mx$ \B{সরলরেখা, $x$-অক্ষ এবং $x = a$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{1}{2}ma^2$
\sub{7} $y = mx$ \B{সরলরেখা, $y$-অক্ষ এবং $y = b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{b^2}{2m}$
\sub{8} $y^2 = 4ax$ \B{পরাবৃত্ত এবং $x = b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}\sqrt{a}(\sqrt{b})^3$
\sub{9} $x^2 = 4ay$ \B{পরাবৃত্ত এবং $y = b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}\sqrt{a}(\sqrt{b})^3$
\sub{10} $y^2 = 4ax$ \B{পরাবৃত্ত এবং এর উপকেন্দ্রিক লম্ব দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}a^2$
\sub{11} $x^2 = 4ay$ \B{পরাবৃত্ত এবং এর উপকেন্দ্রিক লম্ব দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}a^2$
\sub{12} $y^2 = 4ax$ \B{পরাবৃত্ত এবং $y = mx$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8a^2}{3m^3}$
\sub{13} $x^2 = 4ay$ \B{পরাবৃত্ত এবং $y = mx$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}a^2m^3$
\sub{14} $y^2 = 4ax$ \B{পরাবৃত্ত এবং $y = mx + c$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}\dfrac{a^2}{m^3}\left(\sqrt{1-\dfrac{cm}{a}}\right)^3$
\sub{15} $x^2 = 4ay$ \B{পরাবৃত্ত এবং $y = mx + c$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{8}{3}a^2m^3\left(\sqrt{1+\dfrac{c}{am^2}}\right)^3$
\sub{16} $y^2 = 4ax$ \B{পরাবৃত্ত এবং $x^2 = 4by$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{16}{3}ab$
\sub{17} $y^2 = 4ax$ \B{পরাবৃত্ত এবং $x^2 = 4ay$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{16}{3}a^2$
\sub{18} $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ \B{উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \pi ab$
\sub{19} $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ \B{উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের এক চতুর্থাংশের ক্ষেত্রফল} $= \dfrac{\pi ab}{4}$
\sub{20} $x^2 + y^2 = a^2$ \B{বৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \pi a^2$
\sub{21} $x^2 + y^2 = a^2$ \B{বৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের এক চতুর্থাংশের ক্ষেত্রফল} $= \dfrac{\pi a^2}{4}$
\sub{22} $y = \sqrt{a^2-x^2}$ \B{অর্ধবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi a^2}{2}$
\sub{23} $y = -\sqrt{a^2-x^2}$ \B{অর্ধবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi a^2}{2}$
\sub{24} $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ \B{উপবৃত্ত এবং} $\dfrac{x}{a} + \dfrac{y}{b} = 1$ \B{রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi ab}{4} - \dfrac{1}{2}ab$
\sub{25} $x^2 + y^2 = a^2$ \B{বৃত্ত এবং $x + y = a$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi a^2}{4} - \dfrac{1}{2}a^2$
\sub{26} $x^2 + y^2 = 2ax$ \B{বৃত্ত এবং $y^2 = ax$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi a^2}{2} - \dfrac{4}{3}a^2$
\sub{27} $x^2 + y^2 = a^2$ \B{বৃত্ত এবং $y^2 = a^2 - x$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{\pi a^2}{2} - \dfrac{4}{3}a^2$
\sub{28} $xy = c^2$ \B{অধিবৃত্ত, $x$-অক্ষ এবং $x = a$ ও $x = b$ রেখাদ্বয় দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= c^2\ln\left(\dfrac{b}{a}\right)$ \B{ [এখানে $a < b$]}
\sub{29} $\sqrt{x} + \sqrt{y} = \sqrt{a}$ \B{অধিবৃত্ত এবং স্থানাঙ্কের অক্ষ দুটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $= \dfrac{a^2}{6}$

\chsec{অধ্যায়-১০: যোগজীকরণ}

\itm{1} \B{সাধারণ সূত্রসমূহ: [প্রত্যেকটির শেষে +c দিতে হবে]}

\sub{i} $\int\!\{f(x)\pm\varphi(x)\}\,dx=\int\!f(x)\,dx\pm\int!\varphi(x)\,dx$

\sub{ii} $\int\!cf(x)\,dx=c\int\!f(x)\,dx$

\sub{iii} $\displaystyle\int\!x^n\,dx=\frac{x^{n+1}}{n+1}+c$\B{; যখন} $n\neq-1$

\sub{iv} $\displaystyle\int\!\frac{1}{x}\,dx=\ln|x|+c$

\sub{v} $\displaystyle\int\!\frac{f'(x)}{f(x)}\,dx=\ln|f(x)|+c$

\sub{vi} $\int\!\sin x\,dx=-\cos x+c$\B{ এবং} $\displaystyle\int\!\sin mx\,dx=-\frac{\cos mx}{m}+c$

\sub{vii} $\int\!\cos x\,dx=\sin x+c$\B{ এবং} $\displaystyle\int\!\cos mx\,dx=\frac{\sin mx}{m}+c$

\sub{viii} $\int\!\sec^2 x\,dx=\tan x+c$\B{ এবং} $\displaystyle\int\!\sec^2 mx\,dx=\frac{\tan mx}{m}+c$

\sub{ix} $\int\!\csc^2 x\,dx=-\cot x+c$\B{ এবং} $\displaystyle\int\!\csc^2 mx\,dx=-\frac{\cot mx}{m}+c$

\sub{x} $\displaystyle\int\!e^{mx}\,dx=\frac{1}{m}e^{mx}+c$

\sub{xi} $\displaystyle\int\!a^x\,dx=\frac{a^x}{\ln a}+c$\B{ এবং} $\displaystyle\int\!a^{mx}\,dx=\frac{a^{mx}}{m\ln a}+c$

\sub{xii} $\int\!\csc x\cot x\,dx=-\csc x+c$\B{ এবং} $\displaystyle\int\!\csc mx\cot mx\,dx=-\frac{\csc mx}{m}+c$

\sub{xiii} $\int\!\sec x\tan x\,dx=\sec x+c$\B{ এবং} $\displaystyle\int\!\sec mx\tan mx\,dx=\frac{\sec mx}{m}+c$

\sub{xiv} $\displaystyle\int\!\frac{dx}{\sqrt{1-x^2}}=\sin^{-1}x+c$

\sub{xv} $\displaystyle\int\!\frac{-dx}{\sqrt{1-x^2}}=\cos^{-1}x+c$

\sub{xvi} $\displaystyle\int\!\frac{dx}{1+x^2}=\tan^{-1}x+c$

\sub{xvii} $\displaystyle\int\!\frac{-dx}{1+x^2}=\cot^{-1}x+c$

\sub{xviii} $\displaystyle\int\!\frac{dx}{x\sqrt{x^2-1}}=\sec^{-1}x+c$

\sub{xix} $\displaystyle\int\!\frac{-dx}{x\sqrt{x^2-1}}=\csc^{-1}x+c$

\sub{xx} $\displaystyle\int\!\frac{1}{2\sqrt{x}}\,dx=\sqrt{x}+c$

\sub{xxi} $\displaystyle\int\!\sqrt{x}\,dx=\frac{2}{3}x^{3/2}+c$

\sub{xxii} $\displaystyle\int\!\frac{1}{\sqrt{x}}\,dx=2\sqrt{x}+c$

\sub{xxiii} $\displaystyle\frac{d}{dx}\left[\int\!f(x)\,dx\right]=f(x)$

\sub{xxiv} $\displaystyle\int\!\left[\frac{d}{dx}\{f(x)\}\right]dx=f(x)+c$

\sub{xxv} $\displaystyle\int\!dx=x+c$

\sub{xxvi} $\displaystyle\int\!m\cdot f(x)\,dx=m\cdot\int\!f(x)\,dx$\B{ [এখানে } $m=\text{\B{ধ্রুবক}}$\B{]}

\sub{xxvii} $\displaystyle\int\!(ax+b)^n\,dx=\frac{(ax+b)^{n+1}}{a(n+1)}+c$

\sub{xxviii} $\displaystyle\int\!(u\pm v\pm w)\,dx=\int\!u\,dx\pm\int\!v\,dx\pm\int\!w\,dx$

\sub{xxix} $\displaystyle\int\!e^x\,dx=e^x+c$

\sub{xxx} $\displaystyle\int\!\frac{1}{ax+b}\,dx=\frac{1}{a}\ln|ax+b|+c$

\sub{xxxi} $\displaystyle\int\!\cos ax\,dx=\frac{\sin ax}{a}+c$

\sub{xxxii} $\displaystyle\int\!\sin ax\,dx=-\frac{\cos ax}{a}+c$

\sub{xxxiii} $\displaystyle\int\!\sec^2 ax\,dx=\frac{\tan ax}{a}+c$

\sub{xxxiv} $\displaystyle\int\!\csc^2 ax\,dx=-\frac{\cot ax}{a}+c$

\sub{xxxv} $\displaystyle\int\!\sec ax\cdot\tan ax\,dx=\frac{\sec ax}{a}+c$

\sub{xxxvi} $\displaystyle\int\!\csc ax\cdot\cot ax\,dx=-\frac{\csc ax}{a}+c$

\sub{xxxvii} $\displaystyle\int\!\tan x\,dx=\ln|\sec x|+c$

\sub{xxxviii} $\displaystyle\int\!\cot x\,dx=\ln|\sin x|+c$

\sub{xxxix} $\displaystyle\int\!\sec x\,dx=\ln|\sec x+\tan x|+c$

\sub{xl} $\displaystyle\int\!\csc x\,dx=\ln\left|\tan\frac{x}{2}\right|+c$

\itm{2} \B{প্রমিত যোগজসমূহ:}

\sub{i} $\displaystyle\int\!\frac{dx}{x^2+a^2}=\frac{1}{a}\tan^{-1}\!\frac{x}{a}+c$

\sub{ii} $\displaystyle\int\!\frac{dx}{\sqrt{a^2-x^2}}=\sin^{-1}\!\frac{x}{a}+c$

\sub{iii} $\displaystyle\int\!\frac{dx}{x\sqrt{x^2-a^2}}=\frac{1}{a}\sec^{-1}\frac{x}{a}+c$

\sub{iv} $\displaystyle\int\!\frac{dx}{x^2-a^2}=\frac{1}{2a}\ln\!\left|\frac{x-a}{x+a}\right|+c$

\sub{v} $\displaystyle\int\!\frac{dx}{a^2-x^2}=\frac{1}{2a}\ln\!\left|\frac{a+x}{a-x}\right|+c$

\sub{vi} $\displaystyle\int\!\frac{dx}{\sqrt{x^2+a^2}}=\ln\!\left|x+\sqrt{x^2+a^2}\right|+c$

\sub{vii} $\displaystyle\int\!\frac{dx}{\sqrt{x^2-a^2}}=\ln\!\left|x+\sqrt{x^2-a^2}\right|+c$

\sub{viii} $\displaystyle\int\!\sqrt{a^2-x^2}\,dx=\frac{x\sqrt{a^2-x^2}}{2}+\frac{a^2}{2}\sin^{-1}\!\frac{x}{a}+c$

\sub{ix} $\displaystyle\int\!\sqrt{a^2+x^2}\,dx=\frac{x}{2}\sqrt{a^2+x^2}+\frac{a^2}{2}\ln\left|x+\sqrt{a^2+x^2}\right|+c$

\sub{x} $\displaystyle\int\!\sqrt{x^2-a^2}\,dx=\frac{x}{2}\sqrt{x^2-a^2}-\frac{a^2}{2}\ln\left|x+\sqrt{x^2-a^2}\right|+c$

\itm{3} \B{অংশ্যায়ন ও সাধারণ আকারসমূহ:}

\sub{i} $\displaystyle\int\!uv\,dx=u\int\!v\,dx-\int\!\left\{\frac{du}{dx}\int\!v\,dx\right\}dx$

\sub{ii} $\int\!e^x\{f(x)+f'(x)\}\,dx=e^x f(x)+c$\B{ এবং} $\int\!e^{ax}\{af(x)+f'(x)\}\,dx=e^{ax}f(x)+c$

\sub{iii} $\displaystyle\int\!\tan x\,dx=-\ln|\cos x|+c=\ln|\sec x|+c$

\sub{iv} $\displaystyle\int\!\ln x\,dx=x\ln x-x+c$

\sub{v} \B{U, V নির্ণয় (LIATE নিয়ম):}
$\text{L} \rightarrow \text{\B{Logarithmic}}, \ \text{I} \rightarrow \text{\B{Inverse}}, \ \text{A} \rightarrow \text{\B{Algebraic}}, \ \text{T} \rightarrow \text{\B{Trigonometric}}, \ \text{E} \rightarrow \text{\B{Exponential}}$ \\
\B{আগে যেটি আসবে তা $u$, পরে যেটি আসবে তা $v${\bn ।}}

\sub{vi} $\displaystyle\int\!\{f(x)\}^n\cdot f'(x)\,dx=\frac{\{f(x)\}^{n+1}}{n+1}+c$

\sub{vii} $\displaystyle\int\!e^{f(x)}\cdot f'(x)\,dx=e^{f(x)}+c$

\sub{viii} $\displaystyle\int\!\frac{f'(x)}{\sqrt{f(x)}}\,dx=2\sqrt{f(x)}+c$

\itm{4} \B{প্রতিস্থাপন কৌশল ও বিশেষ সাধারণ পদ্ধতি:}

\sub{i} \B{যদি কোনো যোগজ} $\displaystyle\int\!\frac{a+bx^l}{p+qx^n}\,dx$ \B{আকারে থাকে, যেখানে} $l$ \B{ও} $m$ \B{উভয়ে ভগ্নাংশ এবং তাদের হরের ল.সা.গু} $n$ \B{হয়, তবে} $x=z^n$ \B{ধরতে হয়{\bn ।}}

\sub{ii} $\displaystyle\int\!\frac{dx}{x(a+bx^n)}$ \B{আকারের যোগজের জন্য,} $x^n=\dfrac{1}{z}$ \B{ধরতে হয়{\bn ।}}

\sub{iii} $\displaystyle\int\!\frac{dx}{x\sqrt{a+bx^n}}$ \B{আকারের যোগজের জন্য,} $x^n=\dfrac{1}{z}$ \B{ধরতে হয়{\bn ।}}

\sub{iv} $\displaystyle\int\!\frac{dx}{x^m(a+bx)^n}$ \B{আকারের যোগজের জন্য,} $a+bx=zx$ \B{ধরতে হয়{\bn ।}}

\sub{v} $\displaystyle\int\!\frac{dx}{(x-a)^m(x-b)^n}$ \B{আকারের যোগজের জন্য,} $z=\dfrac{x-b}{x-a}$ \B{ধরতে হয়{\bn ।}}

\sub{vi} $\displaystyle\int\!\frac{dx}{\sqrt{ax+b}+\sqrt{ax+c}}$ \B{আকৃতির ক্ষেত্রে লব ও হরকে হরের অনুবন্ধী রাশি দ্বারা গুণ করতে হবে{\bn ।}}

\sub{vii} $\displaystyle\int\!\sqrt{ax+b}\cdot(cx+d)\,dx$ \B{আকৃতির ক্ষেত্রে, } $(ax+b)=t^2$ \B{ ধরতে হবে{\bn ।}}

\sub{viii} $\displaystyle\int\!\frac{(a+bx)^m}{(c+dx)^n}\,dx$ \B{ যেখানে } $m \rightarrow \text{\B{ধনাত্মক পূর্ণসংখ্যা}}$\B{, } $n \rightarrow \text{\B{মূলদ}}$\B{{\bn ।} এক্ষেত্রে, } $c+dx=t$ \B{ ধরতে হবে{\bn ।}}

\sub{ix} $\displaystyle\int\!\frac{dx}{a+be^{mx}}$ \B{ থাকলে, লব ও হরকে } $e^{-mx}$ \B{ দ্বারা এবং } $\displaystyle\int\!\frac{dx}{a+be^{-mx}}$ \B{ থাকলে, লব ও হরকে } $e^{mx}$ \B{ দ্বারা গুণ করতে হবে{\bn ।}}

\sub{x} $\displaystyle\int\!\frac{dx}{a+b\sin^2x}$\B{, } $\displaystyle\int\!\frac{dx}{a+b\cos^2x}$\B{, } $\displaystyle\int\!\frac{dx}{a^2\sin^2x+b^2\cos^2x}$ \B{ থাকলে লব ও হরকে } $\cos^2x$ \B{ দ্বারা ভাগ করে } $\tan x=t$ \B{ ধরতে হবে{\bn ।}}

\sub{xi} $\displaystyle\int\!\frac{x^2\pm1}{x^4+kx^2+1}\,dx$ \B{ থাকলে, } $x^2$ \B{ দ্বারা লব ও হরকে ভাগ করে } $(x+\frac{1}{x})=t$ \B{ অথবা } $(x-\frac{1}{x})=t$ \B{ ধরতে হবে{\bn ।}}

\sub{xii} $\displaystyle\int\!\frac{dx}{(a\sin x+b\cos x)^n}$ \B{ থাকলে, } $a=r\cos\theta$ \B{ এবং } $b=r\sin\theta$ \B{ ধরতে হবে{\bn ।}}

\itm{5} \B{নির্দিষ্ট যোগজের সূত্রাবলী:}

\sub{i} $\displaystyle\int_a^b\!f'(x)\,dx=\bigl[f(x)\bigr]_a^b=f(b)-f(a)$

\sub{ii} $\displaystyle\int_a^b\!f(x)\,dx=-\int_b^a\!f(x)\,dx$

\sub{iii} $\displaystyle\int_0^a\!f(x)\,dx=\int_0^a\!f(a-x)\,dx$

\sub{iv} $\displaystyle\int_a^b\!f(x)\,dx=\int_a^b\!f(a+b-x)\,dx$

\sub{v} $\displaystyle\int_a^b\!f(x)\,dx=\int_{a\pm c}^{b\pm c}\!f(x\mp c)\,dx$

\sub{vi} $\displaystyle\int_a^b\!f(x)\,dx=p\cdot\int_{a/p}^{b/p}\!f(px)\,dx$

\sub{vii} $f(x)=f(2a-x)$ \B{ হলে, } $\displaystyle\int_0^{2a}\!f(x)\,dx=2\cdot\int_0^a\!f(x)\,dx$

\sub{viii} $f(x)=f(-x)$ \B{ হলে, } $\displaystyle\int_{-a}^a\!f(x)\,dx=2\cdot\int_0^a\!f(x)\,dx$

\sub{ix} $\displaystyle\int_a^b\!f(x)\,dx=\int_a^b\!f(t)\,dt$

\itm{6} \B{MCQ Special \& Shortcuts:}

\sub{i} $\displaystyle\int\!\frac{dx}{ax^2+bx+c}=\frac{2}{\sqrt{-D}}\cdot\tan^{-1}\frac{f'(x)}{\sqrt{-D}}+c$\B{ [যখন, নিশ্চায়ক, } $D < 0$\B{]}

\sub{ii} $\displaystyle\int\!\frac{a\sin x+b\cos x}{c\sin x+d\cos x}\,dx=\frac{ac+bd}{c^2+d^2}x+\frac{bc-ad}{c^2+d^2}\ln|c\sin x+d\cos x|+c$

\sub{iii} $\displaystyle\int\!\frac{dx}{\sqrt{(x-\alpha)(x-\beta)}}=2\ln\left|\sqrt{x-\alpha}+\sqrt{x-\beta}\right|+c$

\sub{iv} $\displaystyle\int\!e^{ax}\cdot x^n\,dx=e^{ax}\left[\frac{x^n}{a}-\frac{n\cdot x^{n-1}}{a^2}+\frac{n(n-1)x^{n-2}}{a^3}-\dots\right]$\B{ [ধ্রুবক না আসা পর্যন্ত differentiation করতে হবে]}

\sub{v} $\displaystyle\int\!e^{ax}\sin(bx+c)\,dx \rightarrow \frac{T\cdot E_D - E\cdot T_D}{a^2+b^2}$ \B{ [যেখানে } $T=\text{\B{trigonometric}}$\B{, } $E=\text{\B{exponential}}$\B{, } $T_D$ \B{ ও } $E_D$ \B{ তাদের যথাক্রমে differentiation]}

\sub{vi} $\displaystyle\int\!e^{ax}\cos(bx+c)\,dx \rightarrow \frac{T\cdot E_D - E\cdot T_D}{a^2+b^2}$

\sub{vii} $\displaystyle\int\!\frac{dx}{f(x)\sqrt{\{f(x)\}^2-1}}=\frac{\sec^{-1}f(x)}{f'(x)}+c$\B{ [এখানে $f(x) = \text{\B{linear function}}$]}

\sub{viii} $\displaystyle\int_a^b\!\frac{\sin^nx}{\sin^nx+\cos^nx}\,dx=\frac{b-a}{2}$\B{ [যখন, } $a+b=\frac{\pi}{2}$\B{]}

\sub{ix} $\displaystyle\int_a^b\!\frac{\tan^nx}{\tan^nx+\cot^nx}\,dx=\frac{b-a}{2}$ \B{ এবং } $\displaystyle\int_a^b\!\frac{\cot^nx}{\tan^nx+\cot^nx}\,dx=\frac{b-a}{2}$\B{ [যখন, } $a+b=\frac{\pi}{2}$\B{]}

\sub{x} $\displaystyle\int_a^b\!\frac{\sec^nx}{\sec^nx+\csc^nx}\,dx=\int_a^b\!\frac{\csc^nx}{\sec^nx+\csc^nx}\,dx=\frac{b-a}{2}$\B{ [যখন, } $a+b=\frac{\pi}{2}$\B{]}

\sub{xi} $\displaystyle\int_0^\pi\!\frac{dx}{a+b\cos x}=\int_0^\pi\!\frac{dx}{a+b\sin x}=\frac{\pi}{\sqrt{a^2-b^2}}$

\sub{xii} $\displaystyle\int_0^\infty\!e^{-ax}\cdot\cos bx\,dx=\frac{a}{a^2+b^2}$

\sub{xiii} $\displaystyle\int_0^\infty\!e^{-ax}\cdot\sin bx\,dx=\frac{b}{a^2+b^2}$

\sub{xiv} $\displaystyle\int_0^a!\sqrt{\frac{a+x}{a-x}}\,dx=\frac{\pi}{2}a+a$

\sub{xv} $\displaystyle\int_0^a!\sqrt{\frac{a-x}{a+x}}\,dx=\frac{\pi}{2}a-a$

\sub{xvi} $\displaystyle\int_0^a!\frac{dx}{\sqrt{2ax-x^2}}=\frac{\pi}{2}$

\sub{xvii} $\displaystyle\int_0^a!\sqrt{a^2-x^2}\,dx=\frac{\pi a^2}{4}$

\sub{xviii} $\displaystyle\int_0^a!\frac{1}{\sqrt{a^2-x^2}}\,dx=\frac{\pi}{2}$

\sub{xix} \B{Walli's theorem:} \\
$\displaystyle\int_0^{\pi/2}\!\sin^nx\,dx=\int_0^{\pi/2}\!\cos^nx\,dx = \frac{n-1}{n}\times\frac{n-3}{n-2}\times\frac{n-5}{n-4}\times\dots\times\frac{3\times1}{4\times2}\times\frac{\pi}{2}$ \B{ [যখন, $n = \text{\B{জোড়}}$]} \\
$= \frac{n-1}{n}\times\frac{n-3}{n-2}\times\frac{n-5}{n-4}\times\dots\times\frac{2}{3}$ \B{ [যখন,} $n = $ \B{বিজোড়]}

\itm{7} \B{ক্ষেত্রফল নির্ণয় সংক্রান্ত জ্যামিতিক ধারণা ও লেখচিত্র:}

\sub{i} \B{নির্দিষ্ট যোগজ } $A=\displaystyle\int_a^b\!y\,dx=\int_a^b\!f(x)\,dx$ \B{ যা } $y=f(x)$ \B{ বক্ররেখা, $x$-অক্ষ এবং $x=a$ ও $x=b$ দুটি নির্দিষ্ট ভুজ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল নির্দেশ করে{\bn ।}}

\sub{ii} \B{নির্দিষ্ট যোগজ } $A=\displaystyle\int_c^d\!x\,dy=\int_c^d\!f(y)\,dy$ \B{ যা } $x=f(y)$ \B{ বক্ররেখা, $y$-অক্ষ এবং $y=c$ ও $y=d$ দুইটি নির্দিষ্ট কোটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল নির্দেশ করে{\bn ।}}

\sub{iii} $y_1=f(x_1)$ \B{ ও } $y_2=f(x_2)$ \B{ বক্ররেখা এবং $x=a$ ও $x=b$ ভুজ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল, } $A=\displaystyle\int_a^b\!(y_2-y_1)\,dx=\int_a^b\!\{f_2(x)-f_1(x)\}\,dx$

\sub{iv} $x_1=f(y_1)$ \B{ এবং } $x_2=f(y_2)$ \B{ বক্ররেখা এবং $y=c$ ও $y=d$ দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল, } $A=\displaystyle\int_c^d\!(x_1-x_2)\,dy=\int_c^d\!\{f_1(y)-f_2(y)\}\,dy$

\itm{8} \B{ক্ষেত্রফল সংক্ষেপঃ অঙ্কের জন্য এই সূত্রগুলো মুখস্থ রাখতে হবে}

\sub{1} $\dfrac{x}{a}+\dfrac{y}{b}=1$ \B{ রেখা এবং স্থানাঙ্কের অক্ষদ্বয় দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{1}{2}ab$

\sub{2} $x+y=a$ \B{ রেখা এবং স্থানাঙ্কের অক্ষদ্বয় দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{1}{2}a^2$

\sub{3} $x=a, x=b, y=c$ \B{ এবং } $y=d$ \B{ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $(b-a)(d-c)$ \B{ [এখানে } $a<b$ \B{ এবং } $c<d$\B{]}

\sub{4} $y=|x|$ \B{ এবং } $y=b$ \B{ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $b^2$

\sub{5} $y=-|x|$ \B{ এবং } $y=-b$ \B{ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $b^2$

\sub{6} $y=mx$ \B{ সরলরেখা, $x$-অক্ষ এবং $x=a$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{1}{2}ma^2$

\sub{7} $y=mx$ \B{ সরলরেখা, $y$-অক্ষ এবং $y=b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{1}{2}\cdot\dfrac{b^2}{m}$

\sub{8} $y^2=4ax$ \B{ পরাবৃত্ত এবং $x=b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}\sqrt{a}(\sqrt{b})^3$

\sub{9} $x^2=4ay$ \B{ পরাবৃত্ত এবং $y=b$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}\sqrt{a}(\sqrt{b})^3$

\sub{10} $y^2=4ax$ \B{ পরাবৃত্ত এবং এর উপকেন্দ্রিক লম্ব দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}a^2$

\sub{11} $x^2=4ay$ \B{ পরাবৃত্ত এবং এর উপকেন্দ্রিক লম্ব দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}a^2$

\sub{12} $y^2=4ax$ \B{ পরাবৃত্ত এবং $y=mx$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}\cdot\dfrac{a^2}{m^3}$

\sub{13} $x^2=4ay$ \B{ পরাবৃত্ত এবং $y=mx$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}a^2m^3$

\sub{14} $y^2=4ax$ \B{ পরাবৃত্ত এবং $y=mx+c$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}\cdot\dfrac{a^2}{m^3}\left(\sqrt{1-\dfrac{cm}{a}}\right)^3$

\sub{15} $x^2=4ay$ \B{ পরাবৃত্ত এবং $y=mx+c$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{8}{3}a^2m^3\left(\sqrt{1+\dfrac{c}{am^2}}\right)^3$

\sub{16} $y^2=4ax$ \B{ পরাবৃত্ত এবং $x^2=4by$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{16}{3}ab$

\sub{17} $y^2=4ax$ \B{ পরাবৃত্ত এবং $x^2=4ay$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{16}{3}a^2$

\sub{18} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{ উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\pi ab$

\sub{19} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{ উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের এক চতুর্থাংশের ক্ষেত্রফল = } $\dfrac{\pi ab}{4}$

\sub{20} $x^2+y^2=a^2$ \B{ বৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\pi a^2$

\sub{21} $x^2+y^2=a^2$ \B{ বৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের এক চতুর্থাংশের ক্ষেত্রফল = } $\dfrac{\pi a^2}{4}$

\sub{22} $y=\sqrt{a^2-x^2}$ \B{ অর্ধবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi a^2}{2}$

\sub{23} $y=-\sqrt{a^2-x^2}$ \B{ অর্ধবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi a^2}{2}$

\sub{24} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{ উপবৃত্ত এবং } $\dfrac{x}{a}+\dfrac{y}{b}=1$ \B{ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi ab}{4}-\dfrac{1}{2}ab$

\sub{25} $x^2+y^2=a^2$ \B{ বৃত্ত এবং $x+y=a$ রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi a^2}{4}-\dfrac{1}{2}a^2$

\sub{26} $x^2+y^2=2ax$ \B{ বৃত্ত এবং $y^2=ax$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi a^2}{2}-\dfrac{4}{3}a^2$

\sub{27} $x^2+y^2=a^2$ \B{ বৃত্ত এবং $y^2=a^2-x$ পরাবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{\pi a^2}{2}-\dfrac{4}{3}a^2$

\sub{28} $xy=c^2$ \B{ অধিবৃত্ত, $x$-অক্ষ এবং $x=a$ ও $x=b$ রেখাদুটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $c^2\ln\left(\dfrac{b}{a}\right)$ \B{ [এখানে } $a<b$\B{]}

\sub{29} $\sqrt{x}+\sqrt{y}=\sqrt{a}$ \B{ অধিবৃত্ত এবং স্থানাঙ্কের অক্ষ দুইটি দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল = } $\dfrac{a^2}{6}$

\vspace{4pt}
\noindent\colorbox{black}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{\centering\bfseries\large\color{white}{\bn দ্বিতীয় পত্র}}}
\vspace{2pt}\par


\chsec{অধ্যায়-১: বাস্তব সংখ্যা ও অসমতা}

\itm{1} \B{সকল} $a, b \in \mathbb{R}$ \B{এর জন্য,}

\sub{i} $|a|\geq a$ \quad
\sub{ii} $|a|^2=|-a|^2=a^2$

\sub{iii} $|ab|=|a||b|$ \quad
\sub{iv} $|a+b|\leq|a|+|b|$ \B{ (ত্রিভুজ অসমতা)}

\sub{v} $|a-b|\leq|a|+|b|$ \quad
\sub{vi} $|a-b|\geq\bigl||a|-|b|\bigr|$

\sub{vii} $|ab|\geq ab$ \quad
\sub{viii} $\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$ \B{; যেখানে } $b \neq 0$

\itm{2} $|x|=\begin{cases}x, & x>0\\0, & x=0\\-x, & x<0\end{cases}$

\itm{3} \B{পরমমান চিহ্নের সাহায্যে অসমতার প্রকাশ ($a > 0$ হলে):}
\diag{\begin{tikzpicture}[scale=0.9,every node/.style={font=\scriptsize}]
\draw[->] (-3.2,0)--(3.2,0);
\foreach \x in {-2,-1,0,1,2} \draw (\x,0.06)--(\x,-0.06) node[below]{$\x$};
\draw[very thick,red] (-1.5,0)--(1.5,0);
\filldraw[red] (-1.5,0) circle (1.6pt);
\filldraw[red] (1.5,0) circle (1.6pt);
\node[above] at (0,0.18){$|x|\leq a$};
\end{tikzpicture}}
\sub{i} $|x| < a \iff -a < x < a$
\sub{ii} $|x| \leq a \iff -a \leq x \leq a$
\sub{iii} $|x| > a \iff x > a$ \B{ অথবা } $x < -a$
\sub{iv} $|x| \geq a \iff x \geq a$ \B{ অথবা } $x \leq -a$

\itm{4} \B{অসমতার মৌলিক বৈশিষ্ট্যসমূহ:}
\sub{i} $a > b$ \B{ এবং } $c \in \mathbb{R}$ \B{ হলে, } $a + c > b + c$ \B{ এবং } $a - c > b - c$
\sub{ii} $a > b$ \B{ এবং } $c > 0$ \B{ হলে, } $ac > bc$ \B{ এবং } $\dfrac{a}{c} > \dfrac{b}{c}$
\sub{iii} $a > b$ \B{ এবং } $c < 0$ \B{ হলে, } $ac < bc$ \B{ এবং } $\dfrac{a}{c} < \dfrac{b}{c}$ \B{ (ঋণাত্মক সংখ্যা দ্বারা গুণ বা ভাগ করলে অসমতার চিহ্ন উল্টে যায়)}
\sub{iv} $a > b$ \B{ এবং } $b > c$ \B{ হলে, } $a > c$ \B{ (সংক্রামক ধর্ম)}
\sub{v} $a > b > 0$ \B{ হলে, } $\dfrac{1}{a} < \dfrac{1}{b}$

\itm{5} \B{বাস্তব সংখ্যার বিভিন্ন প্রকার ব্যবধি (Intervals):}
\sub{i} \B{খোলা ব্যবধি (Open Interval):} $(a, b) = \{x \in \mathbb{R} : a < x < b\}$
\sub{ii} \B{বদ্ধ ব্যবধি (Closed Interval):} $[a, b] = \{x \in \mathbb{R} : a \leq x \leq b\}$
\sub{iii} \B{খোলা-বদ্ধ ব্যবধি (Open-Closed Interval):} $(a, b] = \{x \in \mathbb{R} : a < x \leq b\}$
\sub{iv} \B{বদ্ধ-খোলা ব্যবধি (Closed-Open Interval):} $[a, b) = \{x \in \mathbb{R} : a \leq x < b\}$
\sub{v} \B{অসীম ব্যবধি (Infinite Interval):} $(a, \infty) = \{x \in \mathbb{R} : x > a\}$ \B{ এবং } $(-\infty, b] = \{x \in \mathbb{R} : x \leq b\}$

\itm{6} \B{ঊর্ধ্বসীমা, নিম্নসীমা, সুপ্রিমাম ও ইনফিমাম:}
\sub{i} \B{ঊর্ধ্বসীমা (Upper Bound):} \B{কোনো সেট $S$ এর সকল উপাদান যদি একটি নির্দিষ্ট সংখ্যা $M$ অপেক্ষা ছোট বা সমান হয়, তবে $M$-কে সেটের ঊর্ধ্বসীমা বলে{\bn ।}}
\sub{ii} \B{নিম্নসীমা (Lower Bound):} \B{কোনো সেট $S$ এর সকল উপাদান যদি একটি নির্দিষ্ট সংখ্যা $m$ অপেক্ষা বড় বা সমান হয়, তবে $m$-কে সেটের নিম্নসীমা বলে{\bn ।}}
\sub{iii} \B{লঘিষ্ঠ ঊর্ধ্বসীমা বা সুপ্রিমাম (Supremum / L.U.B):} \B{কোনো সেটের ঊর্ধ্বসীমাবদ্ধ সেটটির ক্ষুদ্রতম ঊর্ধ্বসীমাকে সুপ্রিমাম বলে{\bn ।}}
\sub{iv} \B{গরিষ্ঠ নিম্নসীমা বা ইনফিমাম (Infimum / G.L.B):} \B{কোনো সেটের নিম্নসীমাবদ্ধ সেটটির বৃহত্তম নিম্নসীমাকে ইনফিমাম বলে{\bn ।}}

\chsec{অধ্যায়-৩: জটিল সংখ্যা}

\itm{1} \B{জটিল সংখ্যা,} $z=x+iy$ \B{এর ক্ষেত্রে, মডুলাস,} $r=\sqrt{x^2+y^2}$\B{, আর্গুমেন্ট,} $\theta=\tan^{-1}\!\left(\dfrac{y}{x}\right)$
\diag{\begin{tikzpicture}[scale=0.7,every node/.style={font=\scriptsize}]
\draw[->] (-0.6,0)--(2.8,0) node[right]{Re};
\draw[->] (0,-0.6)--(0,2.4) node[above]{Im};
\draw[->,thick,blue] (0,0)--(2.0,1.6);
\filldraw (2.0,1.6) circle (1.3pt) node[above right]{$z=x+iy$};
\draw[dashed] (2.0,0)--(2.0,1.6); \draw[dashed] (0,1.6)--(2.0,1.6);
\node[below] at (2.0,0){$x$}; \node[left] at (0,1.6){$y$};
\node at (0.6,0.22){$\theta$};
\draw (0.4,0) arc (0:38:0.4);
\end{tikzpicture}}

\itm{2} \B{যদি} $a+ib=x+iy$ \B{হয়, তবে} $a=x,\,b=y$\B{; যেখানে} $i=\sqrt{-1}$\B{, সুতরাং} $i^2=-1,\,i^3=-i$ \B{এবং} $i^4=1$

\itm{3} \B{একেকের জটিল ঘনমূল দুইটির একটি} $\omega$ \B{হলে, অপরটি} $\omega^2$

\B{এবং} $\omega^3=1,\;1+\omega+\omega^2=0$\B{;} $\omega=\dfrac{1}{2}(-1+\sqrt{3}i),\;\omega^2=\dfrac{1}{2}(-1-\sqrt{3}i)$

\itm{4} \B{মুখ্য আর্গুমেন্ট নির্ণয়ের নিয়ম ($z = x + iy$ এর জন্য):}
\sub{i} \B{১ম চতুর্ভাগ $(x > 0, y > 0)$:} $\theta = \tan^{-1}\left|\dfrac{y}{x}\right|$
\sub{ii} \B{২য় চতুর্ভাগ $(x < 0, y > 0)$:} $\theta = \pi - \tan^{-1}\left|\dfrac{y}{x}\right|$
\sub{iii} \B{৩য় চতুর্ভাগ $(x < 0, y < 0)$:} $\theta = -\pi + \tan^{-1}\left|\dfrac{y}{x}\right|$
\sub{iv} \B{৪র্থ চতুর্ভাগ $(x > 0, y < 0)$:} $\theta = -\tan^{-1}\left|\dfrac{y}{x}\right|$

\itm{5} \B{অনুবন্ধী জটিল সংখ্যা ও তার ধর্মাবলী:}
\sub{i} $z = x+iy$ \B{ হলে এর অনুবন্ধী ম্যাট্রিক্স বা সংখ্যা } $\bar{z} = x-iy$
\sub{ii} $z\bar{z} = |z|^2 = x^2+y^2$
\sub{iii} $\overline{z_1 \pm z_2} = \bar{z}_1 \pm \bar{z}_2$
\sub{iv} $\overline{z_1 z_2} = \bar{z}_1 \cdot \bar{z}_2$

\itm{6} \B{মডুলাস ও আর্গুমেন্টের ধর্মাবলী:}
\sub{i} $|z_1 z_2| = |z_1||z_2|$ \B{ এবং } $\left|\dfrac{z_1}{z_2}\right| = \dfrac{|z_1|}{|z_2|}$
\sub{ii} $\arg(z_1 z_2) = \arg(z_1) + \arg(z_2)$
\sub{iii} $\arg\left(\dfrac{z_1}{z_2}\right) = \arg(z_1) - \arg(z_2)$

\chsec{অধ্যায়-৪: বহুপদী ও বহুপদী সমীকরণ}

\itm{1} \B{দ্বিঘাত সমীকরণ,} $ax^2+bx+c=0$ \B{(যেখানে,} $a\neq0$\B{) এর ক্ষেত্রে,}

\sub{i} \B{মূলদ্বয়} $\alpha,\beta$ \B{হলে,} $\alpha+\beta=-\dfrac{b}{a}$ \B{এবং} $\alpha\beta=\dfrac{c}{a}$

\sub{ii} \B{উপরি-উক্ত সমীকরণের সমাধান,} $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$

\sub{iii} \B{দ্বিঘাত সমীকরণের নিশ্চায়ক} $=b^2-4ac$ \B{যেখানে,}
\diag{\begin{tikzpicture}[scale=0.5,domain=-1.7:1.7,samples=40,every node/.style={font=\tiny}]
\begin{scope}
\draw[->] (-1.9,0)--(1.9,0); \draw[->] (0,-0.6)--(0,2.4);
\draw[thick,blue,smooth] plot (\x,{\x*\x+0.4});
\node[below] at (0,-0.55){$D<0$};
\end{scope}
\begin{scope}[xshift=4.4cm]
\draw[->] (-1.9,0)--(1.9,0); \draw[->] (0,-0.6)--(0,2.4);
\draw[thick,blue,smooth] plot (\x,{\x*\x});
\node[below] at (0,-0.55){$D=0$};
\end{scope}
\begin{scope}[xshift=8.8cm]
\draw[->] (-1.9,0)--(1.9,0); \draw[->] (0,-0.6)--(0,2.4);
\draw[thick,blue,smooth] plot (\x,{\x*\x-0.7});
\node[below] at (0,-0.55){$D>0$};
\end{scope}
\end{tikzpicture}}

$b^2-4ac=0$ \B{হলে, মূলদ্বয় বাস্তব ও সমান;}\quad $b^2-4ac>0$ \B{হলে, মূলদ্বয় বাস্তব ও অসমান{\bn ।}}

$b^2-4ac<0$ \B{হলে, মূলদ্বয় জটিল ও অসমান;}\quad $b^2-4ac>0$ \B{এবং পূর্ণবর্গ সংখ্যা হলে, মূলদ্বয় মূলদ ও অসমান{\bn ।}}

$b^2-4ac>0$ \B{এবং পূর্ণবর্গ সংখ্যা না হলে, মূলদ্বয় অমূলদ ও অসমান{\bn ।}}

\itm{2} \B{ত্রিঘাত সমীকরণ,} $ax^3+bx^2+cx+d=0$ \B{(যেখানে,} $a\neq0$\B{) এর ক্ষেত্রে}

\sub{i} \B{মূলত্রয়,} $\alpha,\beta,\gamma$ \B{হলে,} $\Sigma\alpha=\alpha+\beta+\gamma=-\dfrac{b}{a}$\B{,} $\Sigma\alpha\beta=\alpha\beta+\alpha\gamma+\beta\gamma=\dfrac{c}{a}$ \B{এবং} $\alpha\beta\gamma=-\dfrac{d}{a}$

\sub{ii} \B{মূলত্রয় সমান্তর প্রগমনে থাকলে তাদের সাধারণ আকার,} $\alpha-\beta,\;\alpha,\;\alpha+\beta$

\sub{iii} \B{মূলত্রয় গুণোত্তর প্রগমনে থাকলে তাদের সাধারণ আকার,} $\dfrac{\alpha}{r},\;\alpha,\;\alpha r$

\sub{iv} \B{মূলত্রয় ভাজিত }\textnormal{(Harmonic)}\B{ প্রগমনে থাকলে তাদের সাধারণ আকার,} $\dfrac{1}{\alpha-\beta},\;\dfrac{1}{\alpha},\;\dfrac{1}{\alpha+\beta}$

\itm{3} \sub{i} $\alpha,\beta$ \B{মূলদ্বয় বিশিষ্ট দ্বিঘাত সমীকরণ} $x^2-(\alpha+\beta)x+\alpha\beta=0$

\sub{ii} \B{ত্রিঘাত সমীকরণের মূলত্রয়} $\alpha,\beta$ \B{ও} $\gamma$ \B{হলে, সমীকরণ}

$x^3-(\alpha+\beta+\gamma)x^2+(\alpha\beta+\beta\gamma+\gamma\alpha)x-\alpha\beta\gamma=0$

\itm{4} \B{চতুর্ঘাত সমীকরণ,} $ax^4+bx^3+cx^2+dx+e=0$ \B{(যেখানে,} $a\neq0$\B{) এর মূলগুলি} $\alpha,\beta,\gamma,\delta$ \B{হলে:}
\sub{i} $\sum\alpha = \alpha+\beta+\gamma+\delta = -\dfrac{b}{a}$
\sub{ii} $\sum\alpha\beta = \alpha\beta+\alpha\gamma+\alpha\delta+\beta\gamma+\beta\delta+\gamma\delta = \dfrac{c}{a}$
\sub{iii} $\sum\alpha\beta\gamma = \alpha\beta\gamma+\alpha\beta\delta+\alpha\gamma\delta+\beta\gamma\delta = -\dfrac{d}{a}$
\sub{iv} $\alpha\beta\gamma\delta = \dfrac{e}{a}$

\itm{5} \B{সাধারণ মূল (Common Root) থাকার শর্তসমূহ:}
\sub{i} $a_1x^2+b_1x+c_1=0$ \B{ এবং } $a_2x^2+b_2x+c_2=0$ \B{ সমীকরণদ্বয়ের একটি সাধারণ মূল } $\alpha$ \B{ থাকলে:}
\[ (c_1a_2-c_2a_1)^2 = (a_1b_2-a_2b_1)(b_1c_2-b_2c_1) \]
\sub{ii} \B{উভয় মূল সাধারণ হওয়ার শর্ত:} $\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} = \dfrac{c_1}{c_2}$

\itm{6} \B{দ্বিঘাত রাশির সর্বোচ্চ ও সর্বনিম্ন মান:}
$ax^2+bx+c$ \B{ রাশিটির সর্বোচ্চ বা সর্বনিম্ন মান } $=\dfrac{4ac-b^2}{4a}$
\sub{i} $a>0$ \B{ হলে রাশিটির সর্বনিম্ন মান পাওয়া যায়{\bn ।}}
\sub{ii} $a<0$ \B{ হলে রাশিটির সর্বোচ্চ মান পাওয়া যায়{\bn ।}}

\itm{7} \B{ভাগশেষ উপপাদ্য ও উৎপাদক উপপাদ্য:}
\sub{i} \B{ভাগশেষ উপপাদ্য (Remainder Theorem):} \B{কোনো বহুপদী $f(x)$-কে $(x-a)$ দ্বারা ভাগ করলে ভাগশেষ হবে $f(a)${\bn ।}}
\sub{ii} \B{উৎপাদক উপপাদ্য (Factor Theorem):} \B{যদি $f(a)=0$ হয়, তবে $(x-a)$ রাশিটি $f(x)$ এর একটি উৎপাদক হবে{\bn ।}}

\chsec{অধ্যায়-৫: দ্বিপদী বিস্তৃতি}

\itm{1} \B{ধনাত্মক পূর্ণসাংখ্যিক ঘাতের ক্ষেত্রে দ্বিপদী উপপাদ্য ($n \in \mathbb{N}$):}

\sub{i} $(a+x)^n=a^n+{}^nC_1 a^{n-1}x+{}^nC_2 a^{n-2}x^2+\cdots+{}^nC_r a^{n-r}x^r+\cdots+x^n$

\sub{ii} $(a+x)^n$ \B{এর বিস্তৃতির মোট পদসংখ্যা} $= n+1$ \B{টি{\bn ।}}

\sub{iii} $(a+x)^n$ \B{এর বিস্তৃতির সাধারণ পদ অর্থাৎ} $(r+1)$ \B{তম পদ,} $T_{r+1}={}^nC_r a^{n-r}x^r$

\sub{iv} $(a+x)^n$ \B{এর বিস্তৃতিতে মধ্যপদ (Middle Term) নির্ণয়:}
\sub{a} $n$ \B{জোড় সংখ্যা হলে, মধ্যপদ একটি এবং তা} $\left(\dfrac{n}{2}+1\right)$ \B{তম পদ{\bn ।}}
\sub{b} $n$ \B{বিজোড় সংখ্যা হলে, মধ্যপদ দুইটি এবং তা} $\left(\dfrac{n-1}{2}+1\right)$ \B{এবং} $\left(\dfrac{n+1}{2}+1\right)$ \B{তম পদদ্বয়{\bn ।}}

\sub{v} $(ax^p+bx^q)^n$ \B{এর বিস্তৃতিতে} $(r+1)$ \B{তম পদে} $x^m$ \B{সম্বলিত হলে,} $r=\dfrac{np-m}{p-q}$ \B{এবং} $x^m$ \B{এর সহগ} $={}^nC_r a^{n-r}b^r$\B{; যেখানে,} $m,n\in\mathbb{N}$

\itm{2} \B{যেকোনো মূলদীয় ঘাতের জন্য দ্বিপদী উপপাদ্য ($n$ ঋণাত্মক পূর্ণসংখ্যা অথবা ভগ্নাংশ এবং $|x|<1$ হলে):}

\sub{i} $(1+x)^n=1+nx+\dfrac{n(n-1)}{2!}x^2+\dfrac{n(n-1)(n-2)}{3!}x^3+\cdots+\dfrac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r+\cdots$

\sub{ii} $(1+x)^n$ \B{এর বিস্তৃতির সাধারণ পদ অর্থাৎ} $(r+1)$ \B{তম পদ,} $T_{r+1}=\dfrac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r$

\sub{iii} $(1-x)^n=1-nx+\dfrac{n(n-1)}{2!}x^2-\dfrac{n(n-1)(n-2)}{3!}x^3+\cdots+(-1)^r\dfrac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r+\cdots$

\itm{3} \B{কিছু গুরুত্বপূর্ণ নির্দিষ্ট অনুমিত বিস্তৃতি ($|x|<1$ হলে):}

\sub{i} $(1-x)^{-1}=1+x+x^2+x^3+\cdots+x^r+\cdots$

\sub{ii} $(1+x)^{-1}=1-x+x^2-x^3+\cdots+(-1)^rx^r+\cdots$

\sub{iii} $(1-x)^{-2}=1+2x+3x^2+4x^3+\cdots+(r+1)x^r+\cdots$

\sub{iv} $(1+x)^{-2}=1-2x+3x^2-4x^3+\cdots+(-1)^r(r+1)x^r+\cdots$

\sub{v} $(1-x)^{-3}=1+3x+6x^2+10x^3+\cdots+\dfrac{1}{2}(r+1)(r+2)x^r+\cdots$

\sub{vi} $(1+x)^{-3}=1-3x+6x^2-10x^3+\cdots+(-1)^r\dfrac{1}{2}(r+1)(r+2)x^r+\cdots$

\sub{vii} $(1-x)^{-n}=1+nx+\dfrac{n(n+1)}{2!}x^2+\cdots+\dfrac{n(n+1)\cdots(n+r-1)}{r!}x^r+\cdots$

\sub{viii} $(1+x)^{-n}=1-nx+\dfrac{n(n+1)}{2!}x^2-\cdots+(-1)^r\dfrac{n(n+1)\cdots(n+r-1)}{r!}x^r+\cdots$

\itm{4} \B{অনন্ত দ্বিপদী ধারার অভিসারিতা (Convergence of Binomial Series):}

\sub{i} \B{যদি} $\displaystyle\lim_{n\to\infty}\left|\dfrac{U_{n+1}}{U_n}\right|<1$ \B{হয়, তাহলে ধারাটি অভিসৃত }\textnormal{(Convergent)}\B{ হবে{\bn ।}}

\sub{ii} \B{যদি} $\displaystyle\lim_{n\to\infty}\left|\dfrac{U_{n+1}}{U_n}\right|>1$ \B{হয়, তাহলে ধারাটি অপসৃত }\textnormal{(Divergent)}\B{ হবে{\bn ।}}

\chsec{অধ্যায়-৬: কণিক (Conics)}

\itm{1} \B{দ্বিঘাত সমীকরণ ও কণিকের শ্রেণীবিভাগ:}
\sub{i} \B{সাধারণ দ্বিঘাত সমীকরণ:} $ax^2 + 2hxy + by^2 + 2gx + 2fy + c = 0$
\sub{ii} \B{নিশ্চায়ক (Discriminant):} $\Delta = abc + 2fgh - af^2 - bg^2 - ch^2$
\sub{iii} $\Delta = 0$ \B{ হলে সমীকরণটি একজোড়া সরলরেখা প্রকাশ করে{\bn ।}}
\sub{iv} $\Delta \neq 0$ \B{ হলে বিভিন্ন শর্তে নিচের কণিকসমূহ নির্দেশ করে:}
\sub{a} $h = 0$ \B{ এবং } $a = b$ \B{ হলে এটি একটি \B{বৃত্ত (Circle)}{\bn ।}}
\sub{b} $h^2 - ab = 0$ \B{ হলে এটি একটি \B{পরাবৃত্ত (Parabola)}; উৎকেন্দ্রিকতা, } $e = 1$
\sub{c} $h^2 - ab < 0$ \B{ হলে এটি একটি \B{উপবৃত্ত (Ellipse)}; উৎকেন্দ্রিকতা, } $0 < e < 1$
\sub{d} $h^2 - ab > 0$ \B{ হলে এটি একটি \B{অধিবৃত্ত (Hyperbola)}; উৎকেন্দ্রিকতা, } $e > 1$
\sub{e} $h^2 - ab > 0$ \B{ এবং } $a + b = 0$ \B{ হলে এটি একটি \B{আয়তাকার অধিবৃত্ত (Rectangular Hyperbola)}{\bn ।}}
\par\medskip
\itm{2} \B{পরাবৃত্তের পূর্ণাঙ্গ তুলনামূলক চিত্র ও সূত্রাবলী (Table of Parabola):}
\diag{\begin{tikzpicture}[scale=0.6,domain=-1.7:1.7,samples=60,every node/.style={font=\scriptsize}]
\draw[->] (-1.2,0)--(3.6,0) node[right]{$x$};
\draw[->] (0,-1.9)--(0,1.9) node[above]{$y$};
\draw[thick,blue,smooth] plot (\x*\x*0.55,\x);
\filldraw (0.55,0) circle (1.2pt) node[above right]{$S(a,0)$};
\draw[dashed] (-0.55,-1.7)--(-0.55,1.7) node[right]{\tiny$x=-a$};
\end{tikzpicture}}

\sub{A} \B{প্রমিত রূপসমূহ (Standard Forms):}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.22\linewidth}|>{\centering\arraybackslash}p{0.17\linewidth}|>{\centering\arraybackslash}p{0.17\linewidth}|>{\centering\arraybackslash}p{0.17\linewidth}|>{\centering\arraybackslash}p{0.17\linewidth}|}
\hline
\B{বৈশিষ্ট্য / সমীকরণ} & $y^2 = 4ax \; (a>0)$ & $y^2 = -4ax \; (a>0)$ & $x^2 = 4ay \; (a>0)$ & $x^2 = -4ay \; (a>0)$ \\
\hline
১. \B{শীর্ষবিন্দু (Vertex)} & $(0,0)$ & $(0,0)$ & $(0,0)$ & $(0,0)$ \\
\hline
২. \B{উপকেন্দ্র (Focus)} & $(a,0)$ & $(-a,0)$ & $(0,a)$ & $(0,-a)$ \\
\hline
৩. \B{অক্ষরেখার সমীকরণ} & $y = 0$ & $y = 0$ & $x = 0$ & $x = 0$ \\
\hline
৪. \B{নিয়ামকের সমীকরণ} & $x + a = 0$ & $x - a = 0$ & $y + a = 0$ & $y - a = 0$ \\
\hline
৫. \B{উপকেন্দ্রিক লম্বের দৈর্ঘ্য} & $4a$ & $4a$ & $4a$ & $4a$ \\
\hline
৬. \B{উপকেন্দ্রিক লম্বের সমীকরণ} & $x = a$ & $x = -a$ & $y = a$ & $y = -a$ \\
\hline
৭. \B{শীর্ষে স্পর্শকের সমীকরণ} & $x = 0$ & $x = 0$ & $y = 0$ & $y = 0$ \\
\hline
৮. \B{নিয়ামক ও অক্ষের ছেদবিন্দু} & $(-a,0)$ & $(a,0)$ & $(0,-a)$ & $(0,a)$ \\
\hline
৯. \B{উপকেন্দ্রিক দূরত্ব ($P(x_1,y_1)$)} & $x_1 + a$ & $a - x_1$ & $y_1 + a$ & $a - y_1$ \\
\hline
\end{tabular}\end{safetable}

\sub{B} \B{শীর্ষবিন্দু $(\alpha, \beta)$ বিন্দুতে স্থানান্তরিত হলে:}
\sub{i} $(y-\beta)^2 = 4a(x-\alpha)$ \B{ এর ক্ষেত্রে: শীর্ষ } $(\alpha, \beta)$\B{, উপকেন্দ্র } $(\alpha+a, \beta)$\B{, অক্ষ } $y = \beta$\B{, নিয়ামক } $x = \alpha - a$
\sub{ii} $(x-\alpha)^2 = 4a(y-\beta)$ \B{ এর ক্ষেত্রে: শীর্ষ } $(\alpha, \beta)$\B{, উপকেন্দ্র } $(\alpha, \beta+a)$\B{, অক্ষ } $x = \alpha$\B{, নিয়ামক } $y = \beta - a$
\par\medskip
\itm{3} \B{উপবৃত্তের পূর্ণাঙ্গ তুলনামূলক চিত্র ও সূত্রাবলী (Table of Ellipse):}
\diag{\begin{tikzpicture}[scale=0.55,every node/.style={font=\scriptsize}]
\draw[->] (-3.2,0)--(3.2,0) node[right]{$x$};
\draw[->] (0,-2.0)--(0,2.0) node[above]{$y$};
\draw[thick,blue] (0,0) ellipse (2.6 and 1.5);
\filldraw (2.1,0) circle (1.2pt) node[below]{$S$};
\filldraw (-2.1,0) circle (1.2pt) node[below]{$S'$};
\filldraw (-2.6,0) circle (1pt) node[above left]{$A$};
\filldraw (2.6,0) circle (1pt) node[above right]{$B$};
\node[above right] at (1.6,1.0){$P$};
\filldraw (1.6,1.18) circle (1pt);
\draw[dotted] (1.6,1.18)--(2.1,0); \draw[dotted] (1.6,1.18)--(-2.1,0);
\end{tikzpicture}}

\sub{A} \B{প্রমিত সমীকরণ:} $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|}
\hline
\B{বৈশিষ্ট্য} & \B{শর্ত:} $a > b$ & \B{শর্ত:} $a < b$ \\
\hline
১. \B{কেন্দ্রের স্থানাঙ্ক (Center)} & $(0,0)$ & $(0,0)$ \\
\hline
২. \B{উৎকেন্দ্রিকতা (Eccentricity)} & $e = \sqrt{\dfrac{a^2 - b^2}{a^2}}$ & $e = \sqrt{\dfrac{b^2 - a^2}{b^2}}$ \\
\hline
৩. \B{উপকেন্দ্রদ্বয়ের স্থানাঙ্ক} & $(\pm ae, 0)$ & $(0, \pm be)$ \\
\hline
৪. \B{শীর্ষবিন্দুদ্বয়ের স্থানাঙ্ক} & $(\pm a, 0)$ & $(0, \pm b)$ \\
\hline
৫. \B{বৃহৎ অক্ষের দৈর্ঘ্য ও সমীকরণ} & দৈর্ঘ্য $= 2a$, সমীকরণ: $y = 0$ & দৈর্ঘ্য $= 2b$, সমীকরণ: $x = 0$ \\
\hline
৬. \B{ক্ষুদ্র অক্ষের দৈর্ঘ্য ও সমীকরণ} & দৈর্ঘ্য $= 2b$, সমীকরণ: $x = 0$ & দৈর্ঘ্য $= 2a$, সমীকরণ: $y = 0$ \\
\hline
৭. \B{নিয়ামক রেখাদ্বয়ের সমীকরণ} & $x = \pm \dfrac{a}{e}$ & $y = \pm \dfrac{b}{e}$ \\
\hline
৮. \B{উপকেন্দ্রিক লম্বের দৈর্ঘ্য} & $\dfrac{2b^2}{a}$ & $\dfrac{2a^2}{b}$ \\
\hline
৯. \B{উপকেন্দ্রিক লম্বের সমীকরণ} & $x = \pm ae$ & $y = \pm be$ \\
\hline
১০. \B{উপকেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব} & $2ae$ & $2be$ \\
\hline
১১. \B{নিয়ামকদ্বয়ের মধ্যবর্তী দূরত্ব} & $\dfrac{2a}{e}$ & $\dfrac{2b}{e}$ \\
\hline
১২. \B{উপকেন্দ্রিক দূরত্বের সমষ্টি} & $SP + S'P = 2a$ & $SP + S'P = 2b$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{4} \B{অধিবৃত্তের পূর্ণাঙ্গ তুলনামূলক চিত্র ও সূত্রাবলী (Table of Hyperbola):}
\diag{\begin{tikzpicture}[scale=0.55,domain=-1.4:1.4,samples=60,every node/.style={font=\scriptsize}]
\draw[->] (-3.4,0)--(3.4,0) node[right]{$x$};
\draw[->] (0,-2.2)--(0,2.2) node[above]{$y$};
\draw[thick,blue,smooth] plot ({1.4*cosh(\x)},{1.0*sinh(\x)});
\draw[thick,blue,smooth] plot ({-1.4*cosh(\x)},{1.0*sinh(\x)});
\draw[dashed,gray] (-3.0,-2.14)--(3.0,2.14);
\draw[dashed,gray] (-3.0,2.14)--(3.0,-2.14);
\filldraw (1.4,0) circle (1pt) node[below]{$A$};
\filldraw (-1.4,0) circle (1pt) node[below]{$A'$};
\end{tikzpicture}}

\sub{A} \B{প্রমিত সমীকরণদ্বয়:}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.29\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.31\linewidth}|}
\hline
\B{বৈশিষ্ট্য} & $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ & $\dfrac{y^2}{b^2} - \dfrac{x^2}{a^2} = 1$ (বা $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = -1$) \\
\hline
১. \B{কেন্দ্রের স্থানাঙ্ক} & $(0,0)$ & $(0,0)$ \\
\hline
২. \B{উৎকেন্দ্রিকতা ($e$)} & $e = \sqrt{\dfrac{a^2 + b^2}{a^2}}$ & $e = \sqrt{\dfrac{a^2 + b^2}{b^2}}$ \\
\hline
৩. \B{উপকেন্দ্রদ্বয়ের স্থানাঙ্ক} & $(\pm ae, 0)$ & $(0, \pm be)$ \\
\hline
৪. \B{শীর্ষবিন্দুদ্বয়ের স্থানাঙ্ক} & $(\pm a, 0)$ & $(0, \pm b)$ \\
\hline
৫. \B{আড় অক্ষের (Transverse Axis) দৈর্ঘ্য} & $2a$ (সমীকরণ: $y = 0$) & $2b$ (সমীকরণ: $x = 0$) \\
\hline
৬. \B{অনুবন্ধী অক্ষের (Conjugate Axis) দৈর্ঘ্য} & $2b$ (সমীকরণ: $x = 0$) & $2a$ (সমীকরণ: $y = 0$) \\
\hline
৭. \B{নিয়ামক রেখাদ্বয়ের সমীকরণ} & $x = \pm \dfrac{a}{e}$ & $y = \pm \dfrac{b}{e}$ \\
\hline
৮. \B{উপকেন্দ্রিক লম্বের দৈর্ঘ্য} & $\dfrac{2b^2}{a}$ & $\dfrac{2a^2}{b}$ \\
\hline
৯. \B{উপকেন্দ্রিক লম্বের সমীকরণ} & $x = \pm ae$ & $y = \pm be$ \\
\hline
১০. \B{অসীমতটের সমীকরণ (Asymptotes)} & $y = \pm \dfrac{b}{a}x \implies \dfrac{x}{a} \pm \dfrac{y}{b} = 0$ & $y = \pm \dfrac{b}{a}x \implies \dfrac{y}{b} \pm \dfrac{x}{a} = 0$ \\
\hline
১১. \B{উপকেন্দ্রিক দূরত্বের অন্তর} & $|SP - S'P| = 2a$ & $|SP - S'P| = 2b$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{5} \B{স্পর্শক ও অভিলম্ব সংক্রান্ত সমীকরণ এবং শর্তাবলী (Tangents and Normals):}

\sub{A} \B{পরাবৃত্তের ক্ষেত্রে ($y^2 = 4ax$):}
\sub{i} \B{স্পর্শক হওয়ার শর্ত:} $y = mx + c$ রেখাটি স্পর্শ করবে যদি $c = \dfrac{a}{m}$ হয়{\bn ।}
\sub{ii} \B{স্পর্শবিন্দু:} $\left(\dfrac{a}{m^2}, \dfrac{2a}{m}\right)$
\sub{iii} $(x_1, y_1)$ \B{ বিন্দুতে স্পর্শকের সমীকরণ:} $yy_1 = 2a(x + x_1)$
\sub{iv} $(x_1, y_1)$ \B{ বিন্দুতে অভিলম্বের (Normal) সমীকরণ:} $y - y_1 = -\dfrac{y_1}{2a}(x - x_1)$

\sub{B} \B{উপবৃত্তের ক্ষেত্রে ($\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$):}
\sub{i} \B{স্পর্শক হওয়ার শর্ত:} $y = mx + c$ রেখাটি স্পর্শ করবে যদি $c = \pm\sqrt{a^2m^2 + b^2}$ হয়{\bn ।}
\sub{ii} \B{স্পর্শবিন্দু:} $\left(\mp \dfrac{a^2m}{c}, \pm \dfrac{b^2}{c}\right)$ যেখানে $c = \sqrt{a^2m^2+b^2}$
\sub{iii} $(x_1, y_1)$ \B{ বিন্দুতে স্পর্শকের সমীকরণ:} $\dfrac{xx_1}{a^2} + \dfrac{yy_1}{b^2} = 1$
\sub{iv} $(x_1, y_1)$ \B{ বিন্দুতে অভিলম্বের সমীকরণ:} $\dfrac{a^2x}{x_1} - \dfrac{b^2y}{y_1} = a^2 - b^2$

\sub{C} \B{অধিবৃত্তের ক্ষেত্রে ($\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$):}
\sub{i} \B{স্পর্শক হওয়ার শর্ত:} $y = mx + c$ রেখাটি স্পর্শ করবে যদি $c = \pm\sqrt{a^2m^2 - b^2}$ হয়{\bn ।}
\sub{ii} \B{স্পর্শবিন্দু:} $\left(\mp \dfrac{a^2m}{c}, \mp \dfrac{b^2}{c}\right)$ যেখানে $c = \sqrt{a^2m^2-b^2}$
\sub{iii} $(x_1, y_1)$ \B{ বিন্দুতে স্পর্শকের সমীকরণ:} $\dfrac{xx_1}{a^2} - \dfrac{yy_1}{b^2} = 1$
\sub{iv} $(x_1, y_1)$ \B{ বিন্দুতে অভিলম্বের সমীকরণ:} $\dfrac{a^2x}{x_1} + \dfrac{b^2y}{y_1} = a^2 + b^2$
\par\medskip
\itm{6} \B{প্যারামেট্রিক স্থানাঙ্ক (Parametric Coordinates):}
\sub{i} \B{পরাবৃত্ত } $y^2 = 4ax$ \B{ এর জন্য:} $(at^2, 2at)$
\sub{ii} \B{উপবৃত্ত } $\dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} = 1$ \B{ এর জন্য:} $(a\cos\theta, b\sin\theta)$
\sub{iii} \B{অধিবৃত্ত } $\dfrac{x^2}{a^2} - \dfrac{y^2}{b^2} = 1$ \B{ এর জন্য:} $(a\sec\theta, b\tan\theta)$
\par\medskip
\itm{7} \B{অন্যান্য গুরুত্বপূর্ণ তথ্য:}
\sub{i} \B{উপবৃত্তের ক্ষেত্রফল:} $\pi ab$ বর্গ একক{\bn ।}
\sub{ii} \B{নিয়ামক বৃত্ত (Director Circle):} উপবৃত্তের পরস্পর লম্ব স্পর্শকদ্বয়ের ছেদবিন্দুর সঞ্চারপথ একটি বৃত্ত, যার সমীকরণ: $x^2 + y^2 = a^2 + b^2$
\sub{iii} \B{অধিবৃত্তের নিয়ামক বৃত্ত:} $x^2 + y^2 = a^2 - b^2$ ($a > b$ হলে)
\sub{iv} \B{আয়তাকার অধিবৃত্তের (Rectangular Hyperbola) অসীমতটদ্বয় পরস্পর লম্ব হয়,} অর্থাৎ তাদের মধ্যবর্তী কোণ $90^\circ$ এবং $e = \sqrt{2}${\bn ।}

\chsec{অধ্যায়-৭: বিপরীত ত্রিকোণমিতিক ফাংশন ও ত্রিকোণমিতিক সমীকরণ}

\itm{1} \B{বিপরীত ত্রিকোণমিতিক ফাংশনের প্রধান মান, ডোমেন ও রেঞ্জ (Table of Domain and Range):}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.26\linewidth}|c|c|c|}
\hline
\B{ফাংশন} & \B{ডোমেন (Domain)} & \B{রেঞ্জ / প্রধান মান (Principal Value Range)} \\
\hline
১. $y = \sin^{-1}x$ & $-1 \leq x \leq 1 \implies [-1, 1]$ & $-\dfrac{\pi}{2} \leq y \leq \dfrac{\pi}{2} \implies \left[-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right]$ \\
\hline
২. $y = \cos^{-1}x$ & $-1 \leq x \leq 1 \implies [-1, 1]$ & $0 \leq y \leq \pi \implies [0, \pi]$ \\
\hline
৩. $y = \tan^{-1}x$ & $-\infty < x < \infty \implies \mathbb{R}$ & $-\dfrac{\pi}{2} < y < \dfrac{\pi}{2} \implies \left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$ \\
\hline
৪. $y = \cot^{-1}x$ & $-\infty < x < \infty \implies \mathbb{R}$ & $0 < y < \pi \implies (0, \pi)$ \\
\hline
৫. $y = \sec^{-1}x$ & $x \geq 1$ \B{অথবা} $x \leq -1 \implies \mathbb{R} \setminus (-1, 1)$ & $0 \leq y \leq \pi, \; y \neq \dfrac{\pi}{2}$ \\
\hline
৬. $y = \csc^{-1}x$ & $x \geq 1$ \B{অথবা} $x \leq -1 \implies \mathbb{R} \setminus (-1, 1)$ & $-\dfrac{\pi}{2} \leq y \leq \dfrac{\pi}{2}, \; y \neq 0$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{2} \B{সংযুক্ত ও যৌগিক কোণের ত্রিকোণমিতিক সূত্রাবলী:}
\sub{i} $\sin(A+B)=\sin A\cos B+\cos A\sin B$
\sub{ii} $\sin(A-B)=\sin A\cos B-\cos A\sin B$
\sub{iii} $\cos(A+B)=\cos A\cos B-\sin A\sin B$
\sub{iv} $\cos(A-B)=\cos A\cos B+\sin A\sin B$
\sub{v} $\tan(A+B)=\dfrac{\tan A+\tan B}{1-\tan A\tan B}$
\sub{vi} $\tan(A-B)=\dfrac{\tan A-\tan B}{1+\tan A\tan B}$
\sub{vii} $\cot(A+B)=\dfrac{\cot A\cot B-1}{\cot B+\cot A}$
\sub{viii} $\cot(A-B)=\dfrac{\cot A\cot B+1}{\cot B-\cot A}$
\par\medskip
\itm{3} \B{ত্রিকোণমিতিক গুণফলকে যোগফল বা বিয়োগফলে রূপান্তর:}
\sub{i} $2\sin A\cos B=\sin(A+B)+\sin(A-B)$
\sub{ii} $2\cos A\sin B=\sin(A+B)-\sin(A-B)$
\sub{iii} $2\cos A\cos B=\cos(A+B)+\cos(A-B)$
\sub{iv} $2\sin A\sin B=\cos(A-B)-\cos(A+B)$
\par\medskip
\itm{4} \B{ত্রিকোণমিতিক যোগফল বা বিয়োগফলকে গুণফলে রূপান্তর:}
\sub{i} $\sin C+\sin D=2\sin\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{ii} $\sin C-\sin D=2\cos\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$
\sub{iii} $\cos C+\cos D=2\cos\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{iv} $\cos C-\cos D=2\sin\dfrac{C+D}{2}\sin\dfrac{D-C}{2}$
\par\medskip
\itm{5} \B{গুণিতক কোণের ত্রিকোণমিতিক অনুপাতসমূহ:}
\sub{i} $\sin 2A=2\sin A\cos A=\dfrac{2\tan A}{1+\tan^2\!A}$
\sub{ii} $\cos 2A=\cos^2\!A-\sin^2\!A=1-2\sin^2\!A=2\cos^2\!A-1=\dfrac{1-\tan^2\!A}{1+\tan^2\!A}$
\sub{iii} $1+\cos 2A=2\cos^2\!A$ \B{ এবং } $1-\cos 2A=2\sin^2\!A$
\sub{iv} $\tan 2A=\dfrac{2\tan A}{1-\tan^2\!A}$
\sub{v} $\sin 3A=3\sin A-4\sin^3\!A$
\sub{vi} $\cos 3A=4\cos^3\!A-3\cos A$
\sub{vii} $\tan 3A=\dfrac{3\tan A-\tan^3\!A}{1-3\tan^2\!A}$
\par\medskip
\itm{6} \B{বিপরীত ত্রিকোণমিতিক ফাংশনের পারস্পরিক রূপান্তর:}
$\sin^{-1}x=\csc^{-1}\!\dfrac{1}{x}=\cos^{-1}\!\sqrt{1-x^2}=\sec^{-1}\!\dfrac{1}{\sqrt{1-x^2}}=\cot^{-1}\!\dfrac{\sqrt{1-x^2}}{x}=\tan^{-1}\!\dfrac{x}{\sqrt{1-x^2}}$
\par\medskip
\itm{7} \B{বিপরীত বৃত্তীয় ফাংশনের সমাহার ও যোগসূত্র:}
\sub{i} $\sin^{-1}x+\cos^{-1}x=\dfrac{\pi}{2}$
\sub{ii} $\tan^{-1}x+\cot^{-1}x=\dfrac{\pi}{2}$
\sub{iii} $\csc^{-1}x+\sec^{-1}x=\dfrac{\pi}{2}$
\par\medskip
\itm{8} \B{বিপরীত বৃত্তীয় ফাংশনের যোগ ও বিয়োগ সংক্রান্ত সূত্রাবলী:}
\sub{i} $\tan^{-1}x+\tan^{-1}y=\tan^{-1}\!\dfrac{x+y}{1-xy}$ \B{ [যখন } $xy < 1$\B{]}
\sub{ii} \B{বিশেষ শর্ত:} $\tan^{-1}x+\tan^{-1}y=\pi + \tan^{-1}\!\dfrac{x+y}{1-xy}$ \B{ [যখন } $x>0, y>0$ \B{ এবং } $xy > 1$\B{]}
\sub{iii} $\tan^{-1}x-\tan^{-1}y=\tan^{-1}\!\dfrac{x-y}{1+xy}$ \B{ [যখন } $xy > -1$\B{]}
\sub{iv} $\tan^{-1}x+\tan^{-1}y+\tan^{-1}z=\tan^{-1}\!\dfrac{x+y+z-xyz}{1-yz-zx-xy}$
\sub{v} $\sin^{-1}x+\sin^{-1}y=\sin^{-1}\!\left\{x\sqrt{1-y^2}+y\sqrt{1-x^2}\right\}$ \B{ [যখন } $x^2+y^2\leq1$ \B{ বা } $x^2+y^2>1$ \B{ এবং } $xy \leq 0$\B{]}
\sub{vi} $\sin^{-1}x-\sin^{-1}y=\sin^{-1}\!\left\{x\sqrt{1-y^2}-y\sqrt{1-x^2}\right\}$
\sub{vii} $\cos^{-1}x+\cos^{-1}y=\cos^{-1}\!\left\{xy-\sqrt{(1-x^2)(1-y^2)}\right\}$ \B{ [যখন } $x+y\geq0$\B{]}
\sub{viii} $\cos^{-1}x-\cos^{-1}y=\cos^{-1}\!\left\{xy+\sqrt{(1-x^2)(1-y^2)}\right\}$ \B{ [যখন } $x \leq y$\B{]}
\sub{ix} $2\tan^{-1}x=\tan^{-1}\!\dfrac{2x}{1-x^2}=\sin^{-1}\!\dfrac{2x}{1+x^2}=\cos^{-1}\!\dfrac{1-x^2}{1+x^2}$
\par\medskip
\itm{9} \B{ত্রিকোণমিতিক সমীকরণের সাধারণ সমাধান (General Solutions Table):}
\B{এখানে প্রত্যেক ক্ষেত্রে সাধারণ সমাধানের জন্য ধ্রুবক সংখ্যা $n \in \mathbb{Z}$ (পূর্ণসংখ্যা):}

\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.27\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|}
\hline
\B{ত্রিকোণমিতিক সমীকরণ} & \B{সাধারণ সমাধান ($\theta$)} & \B{বিশেষ শর্ত / শর্তাবলী} \\
\hline
১. $\sin\theta = 0$ \B{বা} $\tan\theta = 0$ & $\theta = n\pi$ & $n \in \mathbb{Z}$ \\
\hline
২. $\cos\theta = 0$ \B{বা} $\cot\theta = 0$ & $\theta = (2n+1)\dfrac{\pi}{2}$ & $n \in \mathbb{Z}$ \\
\hline
৩. $\sin\theta = 1$ & $\theta = (4n+1)\dfrac{\pi}{2}$ & $n \in \mathbb{Z}$ \\
\hline
৪. $\sin\theta = -1$ & $\theta = (4n-1)\dfrac{\pi}{2}$ & $n \in \mathbb{Z}$ \\
\hline
৫. $\cos\theta = 1$ & $\theta = 2n\pi$ & $n \in \mathbb{Z}$ \\
\hline
৬. $\cos\theta = -1$ & $\theta = (2n+1)\pi$ & $n \in \mathbb{Z}$ \\
\hline
৭. $\sin\theta = \sin\alpha$ & $\theta = n\pi + (-1)^n\alpha$ & $-\dfrac{\pi}{2} \leq \alpha \leq \dfrac{\pi}{2}$ \\
\hline
৮. $\cos\theta = \cos\alpha$ & $\theta = 2n\pi \pm \alpha$ & $0 \leq \alpha \leq \pi$ \\
\hline
৯. $\tan\theta = \tan\alpha$ & $\theta = n\pi + \alpha$ & $-\dfrac{\pi}{2} < \alpha < \dfrac{\pi}{2}$ \\
\hline
১০. $\sin^2\theta = \sin^2\alpha$ & & \\
১১. $\cos^2\theta = \cos^2\alpha$ & $\theta = n\pi \pm \alpha$ & \B{তিনটি বর্গের সমীকরণের জন্যই একই সমাধান} \\
১২. $\tan^2\theta = \tan^2\alpha$ & & \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{10} \B{বিশেষ আকারের সমীকরণ সমাধান পদ্ধতি:}
\sub{i} $a\cos\theta + b\sin\theta = c$ \B{আকারের সমীকরণটি সমাধানের জন্য উভয় পক্ষকে } $\sqrt{a^2+b^2}$ \B{ দ্বারা ভাগ করতে হয়{\bn ।}}
\sub{ii} \B{সমীকরণটির বাস্তব সমাধান থাকার শর্ত:} $c^2 \leq a^2 + b^2$ \B{ অর্থাৎ } $-\sqrt{a^2+b^2} \leq c \leq \sqrt{a^2+b^2}$

\chsec{অধ্যায়-৮: স্থিতিবিদ্যা (Statics)}

\itm{1} \B{সমবিন্দু বলের লব্ধি (Resultant of Coplanar Concurrent Forces):}
\sub{i} $P$ \B{ও} $Q$ \B{বলদ্বয়ের মধ্যবর্তী কোণ} $\alpha$ \B{এবং লব্ধি} $R$ \B{হলে:} 
$R=\sqrt{P^2+Q^2+2PQ\cos\alpha}$
\sub{ii} $P$ \B{বল এবং লব্ধিবল} $R$ \B{এর মধ্যবর্তী কোণ} $\theta$ \B{হলে:} 
$\tan\theta=\dfrac{Q\sin\alpha}{P+Q\cos\alpha}$
\sub{iii} \B{লব্ধির সর্বোচ্চ মান ($R_{\max}$):} $\alpha = 0^\circ$ \B{হলে,} $R_{\max} = P + Q$ \B{ (বলদ্বয় একই দিকে ক্রিয়াশীল)}
\sub{iv} \B{লব্ধির সর্বনিম্ন মান ($R_{\min}$):} $\alpha = 180^\circ$ \B{হলে,} $R_{\min} = |P - Q|$ \B{ (বলদ্বয় বিপরীত দিকে ক্রিয়াশীল)}
\sub{v} \B{লব্ধি $R$, $P$ বলের সাথে লম্ব হলে ($\theta = 90^\circ$):} 
$P + Q\cos\alpha = 0 \implies \cos\alpha = -\dfrac{P}{Q}$ \B{ এবং } $R = \sqrt{Q^2 - P^2}$ \B{ [এখানে } $Q > P$\B{]}
\sub{vi} \B{বলদ্বয়ের মান সমান হলে ($P = Q$):} 
$R = 2P\cos\dfrac{\alpha}{2}$ \B{ এবং লব্ধির দিক, } $\theta = \dfrac{\alpha}{2}$ \B{ (অর্থাৎ লব্ধি কোণটিকে সমদ্বিখণ্ডিত করে)}
\par\medskip
\itm{2} \B{লব্ধির সর্বোচ্চ ও সর্বনিম্ন মানের শর্তাবলী (Summary Table):}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.26\linewidth}|c|c|c|}
\hline
\B{অবস্থা / বৈশিষ্ট্য} & \B{মধ্যবর্তী কোণ ($\alpha$)} & \B{লব্ধির মান ($R$)} & \B{লব্ধির দিক ($\theta$)} \\
\hline
১. সর্বোচ্চ লব্ধি & $\alpha = 0^\circ$ & $R = P + Q$ & $\theta = 0^\circ$ \\
\hline
২. সর্বনিম্ন লব্ধি & $\alpha = 180^\circ$ & $R = |P - Q|$ & $\theta = 0^\circ$ \B{বা} $180^\circ$ \\
\hline
৩. পরস্পর লম্ব বল & $\alpha = 90^\circ$ & $R = \sqrt{P^2 + Q^2}$ & $\tan\theta = \dfrac{Q}{P}$ \\
\hline
৪. সমান মানের বল & $\alpha$ & $R = 2P\cos\dfrac{\alpha}{2}$ & $\theta = \dfrac{\alpha}{2}$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{3} \B{বল বিভাজন ও লম্বাংশ উপপাদ্য (Resolution of Forces):}
\sub{i} \B{যেকোনো দুটি নির্দিষ্ট দিকে বলের উপাংশ (Resolution into two components):}
$F$ \B{বলকে দুটি উপাংশে বিভক্ত করলে যারা} $F$ \B{এর সাথে যথাক্রমে} $\alpha$ \B{ও} $\beta$ \B{কোণ উৎপন্ন করে:}
$\dfrac{P}{\sin\beta}=\dfrac{Q}{\sin\alpha}=\dfrac{F}{\sin(\alpha+\beta)}$
\sub{ii} \B{লম্ব উপাংশ (Rectangular Components):} $\beta = 90^\circ - \alpha$ \B{ হলে পরস্পর লম্ব দিকে উপাংশদ্বয়:}
$P = F\cos\alpha$ \B{ এবং } $Q = F\sin\alpha$
\sub{iii} \B{লম্বাংশ উপপাদ্য (Theorem of Resolving Parts):} 
\B{কোনো সমতলে ক্রিয়ারত $P, Q, \dots$ বলসমূহের যেকোনো নির্দিষ্ট দিকে লম্বাংশের বীজগাণিতিক সমষ্টি, ওই একই দিকে তাদের লব্ধি $R$ এর লম্বাংশের সমান{\bn ।}}
$R\cos\theta = P\cos\alpha + Q\cos\beta + \dots$
$R\sin\theta = P\sin\alpha + Q\sin\beta + \dots$
\B{লব্ধির মান ও দিক:} $R = \sqrt{(\Sigma X)^2 + (\Sigma Y)^2}$ \B{ এবং } $\tan\theta = \dfrac{\Sigma Y}{\Sigma X}$
\par\medskip
\itm{4} \B{তিনটি বলের সাম্যাবস্থা ও লামীর উপপাদ্য (Equilibrium and Lami's Theorem):}
\sub{i} \B{লামীর উপপাদ্য (Lami's Theorem):} \B{কোনো বিন্দুতে ক্রিয়ারত তিনটি সমতলীয় বল সাম্যাবস্থায় থাকলে, প্রতিটি বলের মান অপর দুটি বলের মধ্যবর্তী কোণের sine এর সমানুপাতিক{\bn ।}}
$\dfrac{P}{\sin\alpha}=\dfrac{Q}{\sin\beta}=\dfrac{R}{\sin\gamma}$
\B{[যেখানে $\alpha$ হলো $Q$ ও $R$ এর মধ্যবর্তী কোণ, $\beta$ হলো $R$ ও $P$ এর মধ্যবর্তী কোণ, $\gamma$ হলো $P$ ও $Q$ এর মধ্যবর্তী কোণ]}
\sub{ii} \B{বলের ত্রিভুজ সূত্র (Triangle Law of Forces):} \B{কোনো বিন্দুতে ক্রিয়ারত তিনটি বলের মান ও দিক যদি কোনো ত্রিভুজের একই ক্রমে গৃহীত তিনটি বাহু দ্বারা নির্দেশ করা যায়, তবে বলগুলো সাম্যাবস্থায় থাকবে{\bn ।}}
\sub{iii} \B{বলের বিপরীত ত্রিভুজ সূত্র (Converse of Triangle Law of Forces):} \B{কোনো বিন্দুতে ক্রিয়ারত তিনটি বল সাম্যাবস্থায় থাকলে এবং তাদের ক্রিয়ারেখা কোনো ত্রিভুজের বাহুগুলোর সমান্তরাল হলে, বলগুলোর মান ওই বাহুগুলোর দৈর্ঘ্যের সমানুপাতিক হবে{\bn ।}}
$\dfrac{P}{BC} = \dfrac{Q}{CA} = \dfrac{R}{AB}$
\par\medskip
\itm{5} \B{ত্রিভুজের $m-n$ উপপাদ্য ($m-n$ Theorem):}
\B{কোনো ত্রিভুজ $ABC$ এর $BC$ বাহুর উপর $D$ একটি বিন্দু যেন $BD : DC = m : n$ এবং $\angle ADC = \theta$ হয়, তবে:}
\sub{i} $(m+n)\cot\theta = m\cot\alpha - n\cot\beta$ \B{ [যেখানে } $\angle BAD = \alpha$ \B{ এবং } $\angle CAD = \beta$\B{]}
\sub{ii} $(m+n)\cot\theta = n\cot B - m\cot C$
\par\medskip
\itm{6} \B{সমান্তরাল বলসমূহ (Parallel Forces Table):}
\diag{\begin{tikzpicture}[scale=0.85,every node/.style={font=\scriptsize}]
\draw[thick] (0,0)--(3.6,0);
\filldraw (0,0) circle (1pt) node[above]{$A$};
\filldraw (3.6,0) circle (1pt) node[above]{$B$};
\filldraw (1.4,0) circle (1pt) node[above]{$C$};
\draw[->,thick] (0,0)--(0,-0.9) node[below]{$P$};
\draw[->,thick] (3.6,0)--(3.6,-0.7) node[below]{$Q$};
\draw[->,very thick,red] (1.4,0)--(1.4,-1.3) node[below]{$R$};
\end{tikzpicture}}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.31\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|}
\hline
\B{বৈশিষ্ট্য} & \B{সদৃশ সমান্তরাল বল (Like Parallel)} & \B{অসদৃশ সমান্তরাল বল (Unlike Parallel)} \\
\hline
১. বলের প্রকৃতি ও দিক & \B{দিক একই মুখী} ($P$ ও $Q$) & \B{দিক বিপরীত মুখী} ($P$ ও $Q$, যেখানে $P>Q$) \\
\hline
২. লব্ধির মান ($R$) & $R = P + Q$ & $R = P - Q$ \\
\hline
৩. লব্ধির অবস্থান ($C$) & $AB$ \B{রেখার অভ্যন্তরে অবস্থিত} & $AB$ \B{রেখার বাইরে, বৃহত্তর বলের পাশে অবস্থিত} \\
\hline
৪. বলের সমাবস্থা সূত্র & $P \cdot AC = Q \cdot BC$ & $P \cdot AC = Q \cdot BC$ \\
\hline
৫. অনুপাত সূত্র & $\dfrac{P}{BC} = \dfrac{Q}{AC} = \dfrac{R}{AB}$ & $\dfrac{P}{BC} = \dfrac{Q}{AC} = \dfrac{R}{AB}$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{7} \B{বলযুগল বা দ্বন্দ্ব এবং ভ্রামক (Moment of Force and Couple):}
\sub{i} \B{বলের ভ্রামক (Moment of a Force):} কোনো বিন্দু $O$ এর সাপেক্ষে $P$ বলের ভ্রামক = বল $\times$ বিন্দু থেকে বলের ক্রিয়ারেখার লম্ব দূরত্ব = $P \cdot d$
\sub{ii} \B{বলযুগল (Couple):} দুটি সমান ও বিপরীতমুখী অসদৃশ সমান্তরাল বল ভিন্ন ক্রিয়ারেখায় ক্রিয়া করলে তাকে বলযুগল বলে{\bn ।}
\sub{iii} \B{বলযুগলের ভ্রামক (Moment of a Couple):} যেকোনো একটি বলের মান $\times$ বলদ্বয়ের মধ্যবর্তী লম্ব দূরত্ব; $G = P \cdot d$
\sub{iv} \B{চিহ্নের প্রথা:} ঘড়ির কাটার বিপরীত দিকে (Counter-clockwise) ঘূর্ণন প্রবণতা থাকলে ভ্রামক \B{ধনাত্মক (+)} এবং ঘড়ির কাটার দিকে (Clockwise) হলে ভ্রামক \B{ঋণাত্মক (-)} ধরা হয়{\bn ।}

\chsec{অধ্যায়-৯: সমতলে বস্তুকণার গতি (Motion of Particles in a Plane)}

\itm{1} \B{বেগের সামান্তরিক সূত্র ও লব্ধি বেগ (Parallelogram Law of Velocities):}
\sub{i} \B{লব্ধি বেগ ($w$):} কোনো বিন্দুতে একই সময়ে ক্রিয়ারত দুটি বেগ $u$ ও $v$ এর মধ্যবর্তী কোণ $\alpha$ হলে, তাদের লব্ধি বেগের মান:
$w=\sqrt{u^2+v^2+2uv\cos\alpha}$
\sub{ii} \B{লব্ধি বেগের দিক ($\theta$):} লব্ধি বেগ $w$ যদি $u$ বেগের ক্রিয়ারেখার সাথে $\theta$ কোণ উৎপন্ন করে, তবে:
$\tan\theta=\dfrac{v\sin\alpha}{u+v\cos\alpha} \implies \theta=\tan^{-1}\!\left(\dfrac{v\sin\alpha}{u+v\cos\alpha}\right)$
\sub{iii} \B{সর্বোচ্চ লব্ধি বেগ ($w_{\max}$):} $\alpha = 0^\circ$ হলে (বেগদ্বয় একই দিকে ক্রিয়া করলে), $w_{\max} = u + v$
\sub{iv} \B{সর্বনিম্ন লব্ধি বেগ ($w_{\min}$):} $\alpha = 180^\circ$ হলে (বেগদ্বয় বিপরীত দিকে ক্রিয়া করলে), $w_{\min} = |u - v|$
\sub{v} \B{পরস্পর লম্বভাবে ক্রিয়ারত বেগ:} $\alpha = 90^\circ$ হলে, $w = \sqrt{u^2 + v^2}$ এবং $\tan\theta = \dfrac{v}{u}$
\par\medskip
\itm{2} \B{আপেক্ষিক বেগ ও নদী-নৌকা সংক্রান্ত সূত্রাবলী (Relative Velocity \& River-Boat Problems):}
\sub{i} \B{আপেক্ষিক বেগ (Relative Velocity):} $A$ বস্তুর বেগ $\vec{v}_A$ এবং $B$ বস্তুর বেগ $\vec{v}_B$ হলে, $A$ এর সাপেক্ষে $B$ এর আপেক্ষিক বেগ:
$\vec{v}_{BA} = \vec{v}_B - \vec{v}_A = \vec{v}_B + (-\vec{v}_A)$
\sub{ii} \B{নদী-নৌকা পারাপারের পূর্ণাঙ্গ চিত্র (Table of River-Boat Scenarios):}
\B{এখানে স্রোতের বেগ = $u$, নৌকার/সাঁতারুর আদি বেগ = $v$ (যেখানে $v > u$), নদীর প্রস্থ = $d$, এবং স্রোত ও নৌকার মধ্যবর্তী কোণ = $\alpha$}

\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.31\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|}
\hline
\B{বিষয় / শর্ত} & \B{১. ন্যূনতম দূরত্বে বা সোজাসুজি পারাপার} & \B{২. ন্যূনতম সময়ে নদী পারাপার} \\
\hline
১. \B{লব্ধি বেগের দিক ($\theta$)} & $\theta = 90^\circ$ (স্রোতের সাথে লম্বভাবে) & $\tan\theta = \dfrac{v}{u}$ (যেহেতু $\alpha = 90^\circ$) \\
\hline
২. \B{প্রক্ষেপণ কোণ ($\alpha$)} & $\alpha = \cos^{-1}\left(-\dfrac{u}{v}\right) \implies \alpha > 90^\circ$ & $\alpha = 90^\circ$ (স্রোতের সাথে লম্বভাবে রওনা) \\
\hline
৩. \B{লব্ধি বেগ ($w$)} & $w = \sqrt{v^2 - u^2}$ & $w = \sqrt{u^2 + v^2}$ \\
\hline
৪. \B{পারাপারের সময় ($t$)} & $t = \dfrac{d}{v\sin\alpha} = \dfrac{d}{\sqrt{v^2 - u^2}}$ & $t_{\min} = \dfrac{d}{v}$ \\
\hline
৫. \B{আনুভূমিক সরণ/নদীর পাড় বরাবর দূরত্ব} & $x = 0$ (ঠিক বিপরীত বিন্দুতে পৌঁছাবে) & $x = u \cdot t_{\min} = \dfrac{ud}{v}$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{3} \B{সরলরেখায় সুষম ত্বরণে গতিশীল কণার সমীকরণসমূহ (Motion under Uniform Acceleration):}
\sub{i} \B{নির্দিষ্ট সময়ে শেষ বেগ:} $v = u + ft$
\sub{ii} \B{গড় বেগের সাহায্যে দূরত্ব:} $s = \left(\dfrac{u+v}{2}\right)t$
\sub{iii} \B{ত্বরণ ও সময়ের সাহায্যে দূরত্ব:} $s = ut + \dfrac{1}{2}ft^2$
\sub{iv} \B{বেগ ও দূরত্বের সম্পর্ক:} $v^2 = u^2 + 2fs$
\sub{v} \B{$t$-তম সেকেন্ডে অতিক্রান্ত দূরত্ব ($s_t$):} কণাটি তার গতির ঠিক $t$ সেকেন্ড সময়টিতে যে দূরত্ব অতিক্রম করে:
$s_t = u + \dfrac{1}{2}f(2t - 1)$
\B{[দ্রষ্টব্য: মন্দন বা গতি হ্রাস পাওয়ার ক্ষেত্রে ত্বরণ $ft$ এর স্থলে $-f$ বসাতে হবে{\bn ।}]}
\par\medskip
\itm{4} \B{মহাকর্ষের অধীনে উলম্ব গতি (Vertical Motion Under Gravity):}

\sub{A} \B{খাড়া নিচের দিকে পতনশীল বস্তুর ক্ষেত্রে (স্থির অবস্থান বা আদিবেগ $u$ সহ):}
\sub{i} $v = u + gt$
\sub{ii} $h = ut + \dfrac{1}{2}gt^2$
\sub{iii} $v^2 = u^2 + 2gh$
\sub{iv} \B{স্থির অবস্থান ($u=0$) হতে $h$ উচ্চতা থেকে মাটিতে পড়তে প্রয়োজনীয় সময় ও শেষ বেগ:}
$t = \sqrt{\dfrac{2h}{g}}$ \quad \B{এবং} \quad $v = \sqrt{2gh}$

\sub{B} \B{খাড়া উপরের দিকে নিক্ষিপ্ত বস্তুর ক্ষেত্রে:}
\sub{i} $v = u - gt$
\sub{ii} $h = ut - \dfrac{1}{2}gt^2$
\sub{iii} $v^2 = u^2 - 2gh$
\sub{iv} \B{সর্বোচ্চ উচ্চতা ($H$):} $v=0$ হলে, $H = \dfrac{u^2}{2g}$
\sub{v} \B{সর্বোচ্চ উচ্চতায় পৌঁছানোর সময় (উত্থানকাল, $t_h$):} $t_h = \dfrac{u}{g}$
\sub{vi} \B{মোট বিচরণকাল বা শূন্যে থাকার সময় ($T$):} $T = 2t_h = \dfrac{2u}{g}$ (উত্থানকাল = পতনকাল)

\sub{C} \B{কোনো নির্দিষ্ট উচ্চতা ($h$) থেকে খাড়া উপরের দিকে নিক্ষিপ্ত বস্তুর গতি:}
\B{ভূমি থেকে $h$ উচ্চতায় অবস্থিত কোনো টাওয়ার বা ছাদ হতে $u$ আদিবেগে খাড়া উপরের দিকে নিক্ষিপ্ত বস্তু $t$ সময় পর ভূমিতে পতিত হলে:}
\sub{i} \B{উচ্চতা বা সরণের সমীকরণ:} $h = -ut + \dfrac{1}{2}gt^2$
\sub{ii} \B{যেকোনো সময়ে বেগের সমীকরণ:} $v = -u + gt$
\sub{iii} \B{বেগ ও দূরত্বের সমীকরণ:} $v^2 = u^2 + 2gh$
\par\medskip
\itm{5} \B{প্রাসের গতি বা দ্বিমাত্রিক প্রক্ষিপ্ত বস্তুর গতি (Motion of a Projectile):}
\diag{\begin{tikzpicture}[scale=0.55,domain=0:4,samples=40,every node/.style={font=\scriptsize}]
\draw[->] (0,0)--(4.6,0) node[right]{$x$};
\draw[->] (0,0)--(0,2.6) node[above]{$y$};
\draw[thick,blue,smooth] plot (\x, {\x*(4-\x)*0.45});
\draw[->,thick] (0,0)--(0.95,0.95) node[above]{$u$};
\draw (0.45,0) arc (0:45:0.45); \node at (24:0.62){$\alpha$};
\node[below] at (2,0){$R$};
\draw[dashed] (2,1.8)--(2,0); \node[right] at (2,1.4){$H$};
\end{tikzpicture}}
\B{ভূমি থেকে কোনো বস্তুকে আনুভূমিকের সাথে $\alpha$ কোণে $u$ আদিবেগে নিক্ষেপ করা হলে:}



\sub{A} \B{প্রাসের গতির সাধারণ সমীকরণসমূহ (Table of Projectile Formulas):}
\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.28\linewidth}|>{\centering\arraybackslash}p{0.29\linewidth}|>{\raggedright\arraybackslash}p{0.34\linewidth}|}
\hline
\B{বৈশিষ্ট্য / রাশি} & \B{গাণিতিক সূত্র (Formula)} & \B{ব্যাখ্যা ও বিশেষ দ্রষ্টব্য} \\
\hline
১. $t$ সময় পর আনুভূমিক সরণ & $x = u\cos\alpha \cdot t$ & \B{আনুভূমিক দিকে কোনো ত্বরণ নেই ($f_x = 0$)} \\
\hline
২. $t$ সময় পর উলম্ব সরণ & $y = u\sin\alpha \cdot t - \dfrac{1}{2}gt^2$ & \B{উলম্ব দিকে অভিকর্ষজ মন্দন কাজ করে} \\
\hline
৩. গতির গতিপথের সমীকরণ & $y = x\tan\alpha - \dfrac{gx^2}{2u^2\cos^2\alpha}$ & \B{সমীকরণটি একটি পরাবৃত্ত (Parabola) নির্দেশ করে} \\
\hline
৪. আনুভূমিক পাল্লার সাথে সম্পর্ক & $y = x\tan\alpha \left(1 - \dfrac{x}{R}\right)$ & \B{গাণিতিক সমস্যা সমাধানে অত্যন্ত গুরুত্বপূর্ণ} \\
\hline
৫. সর্বোচ্চ উচ্চতা ($H$) & $H = \dfrac{u^2\sin^2\alpha}{2g}$ & \B{এই বিন্দুতে উলম্ব বেগ শূন্য হয় ($v_y = 0$)} \\
\hline
৬. সর্বোচ্চ উচ্চতায় ওঠার সময় & $t = \dfrac{u\sin\alpha}{g}$ & \B{মোট বিচরণকালের অর্ধেক} \\
\hline
৭. মোট বিচরণকাল ($T$) & $T = \dfrac{2u\sin\alpha}{g}$ & \B{আবার ভূমিতে ফিরে আসার মোট সময়} \\
\hline
৮. আনুভূমিক পাল্লা ($R$) & $R = \dfrac{u^2\sin 2\alpha}{g}$ & \B{ভূমিতে অতিক্রান্ত মোট আনুভূমিক দূরত্ব} \\
\hline
৯. সর্বোচ্চ আনুভূমিক পাল্লা & $R_{\max} = \dfrac{u^2}{g}$ & \B{যখন প্রক্ষেপণ কোণ, $\alpha = 45^\circ$ হয়} \\
\hline
\end{tabular}\end{safetable}

\sub{B} \B{প্রাসের গতি সংক্রান্ত গুরুত্বপূর্ণ অনুসিদ্ধান্তসমূহ:}
\sub{i} \B{একই আনুভূমিক পাল্লার জন্য দুটি প্রক্ষেপণ কোণ:} কোনো বস্তুকে $u$ আদিবেগে নিক্ষেপ করলে প্রক্ষেপণ কোণ $\alpha$ অথবা $(90^\circ - \alpha)$ উভয় ক্ষেত্রের জন্যই আনুভূমিক পাল্লা ($R$) একই থাকে{\bn ।}
\sub{ii} \B{$t$ সময় পরে প্রাসের লব্ধি বেগ ($v_t$):} 
$v_t = \sqrt{v_x^2 + v_y^2}$ \quad \B{যেখানে,} \;\; $v_x = u\cos\alpha$ \;\; \B{এবং} \;\; $v_y = u\sin\alpha - gt$
\sub{iii} \B{$t$ সময় পরে লব্ধি বেগের দিক ($\theta_t$):} $\tan\theta_t = \dfrac{v_y}{v_x} = \dfrac{u\sin\alpha - gt}{u\cos\alpha}$

\chsec{অধ্যায়-১০: বিস্তার পরিমাপ ও সম্ভাবনা (Measures of Dispersion and Probability)}

\itm{1} \B{বিস্তার পরিমাপের প্রকারভেদ (Classification of Measures of Dispersion):}
\sub{i} \B{অনপেক্ষ বিস্তার পরিমাপ (Absolute Measures):} ১. পরিসর (Range) ২. চতুর্থক ব্যবধান (Quartile Deviation) ৩. গড় ব্যবধান (Mean Deviation) ৪. পরিমিত ব্যবধান (Standard Deviation){\bn ।}
\sub{ii} \B{আপেক্ষিক বিস্তার পরিমাপ (Relative Measures):} ১. পরিসরাঙ্ক ২. চতুর্থক ব্যবধান অঙ্ক ৩. গড় ব্যবধান অঙ্ক ৪. বিভেদঙ্ক বা ব্যবধান অঙ্ক (Coefficient of Variation){\bn ।}
\par\medskip
\itm{2} \B{অনপেক্ষ বিস্তার পরিমাপের পূর্ণাঙ্গ গাণিতিক সূত্রাবলী (Absolute Measures of Dispersion):}

\sub{A} \B{অশ্রেণীকৃত উপাত্তের ক্ষেত্রে (For Ungrouped Data):}
\B{তথ্যমানসমূহ $x_1, x_2, \ldots, x_n$ এবং গাণিতিক গড় $\bar{x}$ হলে:}
\sub{i} \B{পরিসর (Range):} $R = X_H - X_L$ \B{ [এখানে $X_H = $ সর্বোচ্চ মান, $X_L = $ সর্বনিম্ন মান]}
\sub{ii} \B{চতুর্থক ব্যবধান (Quartile Deviation):} $QD = \dfrac{Q_3 - Q_1}{2}$ \B{ [এখানে $Q_1 = $ প্রথম চতুর্থক, $Q_3 = $ তৃতীয় চতুর্থক]}
\sub{iii} \B{গড় ব্যবধান (Mean Deviation):} $MD(\bar{x}) = \dfrac{\sum |x_i - \bar{x}|}{n}$ \B{ [মধ্যমার সাপেক্ষে হলে: } $MD(Me) = \dfrac{\sum |x_i - Me|}{n}$\B{]}
\sub{iv} \B{ভেদাঙ্ক (Variance):} $\sigma^2 = \dfrac{\sum (x_i - \bar{x})^2}{n} = \dfrac{\sum x_i^2}{n} - \left(\dfrac{\sum x_i}{n}\right)^2$
\sub{v} \B{পরিমিত ব্যবধান (Standard Deviation):} $\sigma = \sqrt{\dfrac{\sum (x_i - \bar{x})^2}{n}} = \sqrt{\dfrac{\sum x_i^2}{n} - \left(\dfrac{\sum x_i}{n}\right)^2}$

\sub{B} \B{শ্রেণীকৃত উপাত্তের ক্ষেত্রে (For Grouped Data):}
\B{শ্রেণি মধ্যমানসমূহ $x_1, x_2, \ldots, x_n$, গণসংখ্যা $f_1, f_2, \ldots, f_n$, মোট গণসংখ্যা $N = \sum f_i$ এবং গাণিতিক গড় $\bar{x}$ হলে:}
\sub{i} \B{গড় ব্যবধান (Mean Deviation):} $MD(\bar{x}) = \dfrac{\sum f_i|x_i - \bar{x}|}{N}$
\sub{ii} \B{ভেদাঙ্ক (Variance):} $\sigma^2 = \dfrac{\sum f_i(x_i - \bar{x})^2}{N} = \dfrac{\sum f_ix_i^2}{N} - \left(\dfrac{\sum f_ix_i}{N}\right)^2$
\sub{iii} \B{পরিমিত ব্যবধান (Standard Deviation):} $\sigma = \sqrt{\dfrac{\sum f_i(x_i - \bar{x})^2}{N}} = \sqrt{\dfrac{\sum f_ix_i^2}{N} - \left(\dfrac{\sum f_ix_i}{N}\right)^2}$
\sub{iv} \B{সংক্ষিপ্ত পদ্ধতি (Short-cut Method):} অনুমিত গড় $a$, শ্রেণির ব্যবধান $h$ এবং ধাপ বিচ্যুতি $d_i = \dfrac{x_i - a}{h}$ হলে:
$\sigma = h \times \sqrt{\dfrac{\sum f_id_i^2}{N} - \left(\dfrac{\sum f_id_i}{N}\right)^2}$ \B{ এবং ভেদাঙ্ক } $\sigma^2 = h^2 \left[ \dfrac{\sum f_id_i^2}{N} - \left(\dfrac{\sum f_id_i}{N}\right)^2 \right]$
\par\medskip
\itm{3} \B{আপেক্ষিক বিস্তার পরিমাপের তুলনামূলক ছক (Table of Relative Measures of Dispersion):}

\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.31\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|>{\centering\arraybackslash}p{0.30\linewidth}|}
\hline
\B{ক্রমিং} & \B{আপেক্ষিক বিস্তার পরিমাপের নাম} & \B{গাণিতিক সূত্র (Formula)} \\
\hline
১. & \B{পরিসরাঙ্ক (Coefficient of Range)} & $\text{CR} = \dfrac{X_H - X_L}{X_H + X_L} \times 100\%$ \\
\hline
২. & \B{চতুর্থক ব্যবধান অঙ্ক (Coefficient of QD)} & $\text{CQD} = \dfrac{Q_3 - Q_1}{Q_3 + Q_1} \times 100\%$ \\
\hline
৩. & \B{গড় ব্যবধান অঙ্ক (Coefficient of MD)} & $\text{CMD} = \dfrac{MD(\bar{x})}{\bar{x}} \times 100\%$ \\
\hline
৪. & \B{বিভেদঙ্ক বা ব্যবধান অঙ্ক (Coefficient of Variation)} & $\text{CV} = \dfrac{\sigma}{\bar{x}} \times 100\%$ \\
\hline
\end{tabular}\end{safetable}
\par\medskip
\itm{4} \B{পরিমিত ব্যবধান ও ভেদাঙ্কের গুরুত্বপূর্ণ বৈশিষ্ট্য ও অনুসিদ্ধান্ত:}
\sub{i} \B{মূল ও মাপনী পরিবর্তন:} পরিমিত ব্যবধান মূল (Origin) পরিবর্তনের উপর নির্ভরশীল নয়, কিন্তু মাপনীর (Scale) পরিবর্তনের উপর নির্ভরশীল{\bn ।} মূল $a$ ও মাপনী $c$ দ্বারা চলক পরিবর্তন $u_i = \dfrac{x_i - a}{c}$ হলে, $\sigma_x = |c| \cdot \sigma_u$ হয়{\bn ।} ভেদাঙ্কের ক্ষেত্রে, $\sigma_x^2 = c^2 \cdot \sigma_u^2$
\sub{ii} \B{ধ্রুবকের বিস্তার:} যেকোনো ধ্রুবক সংখ্যার পরিমিত ব্যবধান ও ভেদাঙ্ক সর্বদা শূন্য হয়{\bn ।} $\sigma(c) = 0, \; \sigma^2(c) = 0$
\sub{iii} \B{প্রথম $n$ সংখ্যক স্বাভাবিক সংখ্যার ক্ষেত্রে ($1, 2, 3, \ldots, n$):}
\sub{a} \B{গাণিতিক গড়:} $\bar{x} = \dfrac{n + 1}{2}$
\sub{b} \B{ভেদাঙ্ক:} $\sigma^2 = \dfrac{n^2 - 1}{12}$
\sub{c} \B{পরিমিত ব্যবধান:} $\sigma = \sqrt{\dfrac{n^2 - 1}{12}}$
\sub{iv} \B{সম্মিলিত পরিমিত ব্যবধান (Combined Standard Deviation):} দুটি তথ্যসেটের আকার $n_1, n_2$, গড় $\bar{x}_1, \bar{x}_2$ এবং পরিমিত ব্যবধান $\sigma_1, \sigma_2$ হলে তাদের সম্মিলিত পরিমিত ব্যবধান $\sigma_c$:
$\sigma_c = \sqrt{\dfrac{n_1(\sigma_1^2 + d_1^2) + n_2(\sigma_2^2 + d_2^2)}{n_1 + n_2}}$ \B{ [যেখানে, } $d_1 = \bar{x}_1 - \bar{x}_c$\B{, } $d_2 = \bar{x}_2 - \bar{x}_c$ \B{ এবং সম্মিলিত গড় } $\bar{x}_c = \dfrac{n_1\bar{x}_1 + n_2\bar{x}_2}{n_1 + n_2}$\B{]}
\par\medskip
\itm{5} \B{সম্ভাবনার মৌলিক সূত্রাবলী ও সীমারেখা (Basic Principles of Probability):}
\sub{i} \B{গাণিতিক সংজ্ঞা:} কোনো ঘটনার অনুকূল ফলাফল সংখ্যা $n(A)$ এবং নমুনা ক্ষেত্রের মোট ফলাফল সংখ্যা $n(S)$ হলে, $A$ ঘটনার সম্ভাবনা:
$P(A) = \dfrac{n(A)}{n(S)}$
\sub{ii} \B{সম্ভাবনার সীমা (Range of Probability):} যেকোনো ঘটনা $A$ এর জন্য সম্ভাবনার মান $0$ থেকে $1$ এর মধ্যে থাকে{\bn ।} $0 \leq P(A) \leq 1$
\sub{iii} \B{নিশ্চিত ঘটনা (Certain Event):} নমুনা ক্ষেত্র $S$ এর জন্য, $P(S) = 1$
\sub{iv} \B{অসম্ভব ঘটনা (Impossible Event):} ফাঁকা সেট $\Phi$ এর জন্য, $P(\Phi) = 0$
\sub{v} \B{পূরক ঘটনা (Complementary Event):} $A$ ঘটনাটি না ঘটার সম্ভাবনা $P(A^c)$ বা $P(A')$ হলে, $P(A) + P(A^c) = 1 \implies P(A^c) = 1 - P(A)$
\sub{vi} \B{অনুকূল ও প্রতিকূল সংযোগ (Odds in Favor and Against):} কোনো ঘটনার অনুকূল অনুপাত $a:b$ হলে, অনুকূলের সম্ভাবনা $= \dfrac{a}{a+b}$ এবং প্রতিকূলের সম্ভাবনা $= \dfrac{b}{a+b}$
\par\medskip
\itm{6} \B{সম্ভাবনার যোগ ও গুণন উপপাদ্য (Addition \& Multiplication Theorems):}
\sub{i} \B{$A$ ও $B$ বর্জনশীল (Mutually Exclusive) ঘটনা হলে:} $A \cap B = \Phi \implies P(A \cap B) = 0$
$P(A \cup B) = P(A) + P(B)$
\sub{ii} \B{$A$ ও $B$ অবর্জনশীল (Non-mutually Exclusive) ঘটনা হলে:}
$P(A \cup B) = P(A) + P(B) - P(A \cap B)$
\sub{iii} \B{তিনটি অবর্জনশীল ঘটনা $A, B$ ও $C$ এর ক্ষেত্রে যোগ সূত্র:}
$P(A \cup B \cup C) = P(A) + P(B) + P(C) - P(A \cap B) - P(B \cap C) - P(C \cap A) + P(A \cap B \cap C)$
\sub{iv} \B{$A$ ও $B$ স্বাধীন (Independent) ঘটনা হলে:} $A$ এর সংঘটন $B$ এর উপর প্রভাব ফেলে না{\bn ।}
$P(A \cap B) = P(A) \times P(B)$
\sub{v} \B{$A$ ও $B$ অধীন (Dependent) বা শর্তাধীন (Conditional) ঘটনা হলে:}
$P(A \cap B) = P(A) \times P(B|A) = P(B) \times P(A|B)$
\sub{vi} \B{শর্তাধীন সম্ভাবনার সূত্র (Conditional Probability):} $A$ ঘটনা ঘটার সাপেক্ষে $B$ ঘটার সম্ভাবনা:
$P(B|A) = \dfrac{P(A \cap B)}{P(A)}$ \;\; $[P(A) \neq 0]$ \quad \B{এবং} \quad $P(A|B) = \dfrac{P(A \cap B)}{P(B)}$ \;\; $[P(B) \neq 0]$
\sub{vii} \B{সম্পূর্ণ ঘটনা (Exhaustive Events):} $A$ ও $B$ সম্পূর্ণ ঘটনা হলে, $P(A \cup B) = P(S) = 1$
\par\medskip
\itm{7} \B{ঘটনার বিভিন্ন সমাবেশের সম্ভাবনার রূপান্তর ছক (Set Operations and Probability Chart):}

\begin{safetable}\begin{tabular}{|>{\raggedright\arraybackslash}p{0.27\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|>{\raggedright\arraybackslash}p{0.32\linewidth}|}
\hline
\B{ক্রমিং} & \B{ঘটনার বিবরণ ও সেট প্রতীক} & \B{গাণিতিক বিস্তৃতি ও সূত্র (Formula)} \\
\hline
১. & $A$ বা $B$ এর কমপক্ষে একটি ঘটার সম্ভাবনা ($A \cup B$) & $P(A \cup B) = P(A) + P(B) - P(A \cap B)$ \\
\hline
২. & $A$ ও $B$ উভয়ই একসাথে ঘটার সম্ভাবনা ($A \cap B$) & $P(A \cap B) = P(A) + P(B) - P(A \cup B)$ \\
\hline
৩. & কেবল $A$ ঘটবে কিন্তু $B$ ঘটবে না ($A \cap B^c$) & $P(A \cap B^c) = P(A) - P(A \cap B)$ \\
\hline
৪. & কেবল $B$ ঘটবে কিন্তু $A$ ঘটবে না ($A^c \cap B$) & $P(A^c \cap B) = P(B) - P(A \cap B)$ \\
\hline
৫. & $A$ ও $B$ এর কোনোটিই না ঘটার সম্ভাবনা ($A^c \cap B^c$) & $P(A^c \cap B^c) = P((A \cup B)^c) = 1 - P(A \cup B)$ \\
\hline
৬. & $A$ অথবা $B$ এর কোনোটিই না ঘটার সম্ভাবনা ($A^c \cup B^c$) & $P(A^c \cup B^c) = P((A \cap B)^c) = 1 - P(A \cap B)$ \\
\hline
৭. & কেবল একটি ঘটনা ঘটার সম্ভাবনা & $P(A \cap B^c) + P(A^c \cap B) = P(A \cup B) - P(A \cap B)$ \\
\hline
\end{tabular}\end{safetable}

\end{multicols}

\par\endgroup
\clearpage

\clearpage\thispagestyle{empty}
\null
\begin{tikzpicture}[remember picture,overlay,shift={(current page.south west)},x=1cm,y=1cm,line cap=round,line join=round]
% background
\shade[top color=deeppur,bottom color=deeppur2] (0,0) rectangle (21,29.7);
\foreach \j in {0,...,33}{\foreach \i in {0,...,13}{
  \node[regular polygon,regular polygon sides=6,minimum size=0.95cm,draw=white!6,line width=0.3pt,rotate=30] at ({0.6+1.55*\i+0.775*Mod(\j,2)},{29.2-0.86*\j}) {};}}
% top gold rule + heading
\draw[a360gold,line width=1.3pt] (5.5,26.4)--(15.5,26.4);
\node[white,font=\bfseries] at (10.5,25.3) {\fontsize{15}{16}\selectfont YOUR ULTIMATE COMPANION FOR};
\node[white,font=\bfseries] at (10.5,24.0) {\fontsize{30}{32}\selectfont EVERY FORMULA,};
\node[white,font=\bfseries] at (10.5,23.0) {\fontsize{30}{32}\selectfont EVERY CONCEPT,};
\node[a360gold,font=\bfseries] at (10.5,22.0) {\fontsize{30}{32}\selectfont EVERY SUCCESS.};

% central lightbulb emblem
\begin{scope}[shift={(10.5,17.2)},scale=1.7]
  \foreach \a in {15,40,65,90,115,140,165}{\draw[a360gold,line width=1.1pt] (\a:1.35)--(\a:1.75);}
  \draw[a360gold,line width=1.5pt] (0,0.2) circle (1.05);
  \draw[a360gold,line width=1pt] (0,0.85) .. controls (-0.7,0.85) and (-0.7,-0.05) .. (0,-0.1);
  \draw[a360gold,line width=1pt] (0,0.85) .. controls (0.7,0.85) and (0.7,-0.05) .. (0,-0.1);
  \draw[a360gold,line width=0.8pt] (0,0.85)--(0,-0.1);
  \draw[a360gold,line width=0.7pt] (-0.35,0.55) .. controls (-0.15,0.35) .. (-0.35,0.15);
  \draw[a360gold,line width=0.7pt] (0.35,0.55) .. controls (0.15,0.35) .. (0.35,0.15);
  \draw[a360gold,line width=1.2pt] (-0.4,-0.78)--(0.4,-0.78);
  \draw[a360gold,line width=1.2pt] (-0.34,-1.02)--(0.34,-1.02);
  \draw[a360gold,line width=1pt] (-0.4,-0.78)--(-0.34,-0.55)--(0.34,-0.55)--(0.4,-0.78);
  \draw[a360gold,line width=1pt] (-0.18,-1.02) .. controls (-0.09,-1.24) and (0.09,-1.24) .. (0.18,-1.02);
\end{scope}

% WHAT'S INSIDE checklist
\node[rounded corners=4pt,draw=a360gold,line width=1pt,inner sep=5pt] at (10.5,12.6) {\color{a360gold}\fontsize{14}{14}\selectfont\bfseries WHAT'S INSIDE?};
\foreach \k/\txt in {0/{All important formulas at your fingertips},1/{Organized by topic for quick access},2/{Clear, concise \& exam-focused},3/{Covers school to competitive level},4/{A must-have for every student}}{
  \fill[a360gold] (5.6,11.4-0.78*\k) circle (0.2);
  \node[deeppur,font=\bfseries] at (5.6,11.4-0.78*\k) {\tiny$\checkmark$};
  \node[white,anchor=west] at (6.05,11.4-0.78*\k) {\fontsize{13}{15}\selectfont \txt};
}

% gold divider
\draw[a360gold,line width=0.8pt] (4.5,6.6)--(16.5,6.6);

% closing lines
\node[white,font=\bfseries] at (10.5,5.6) {\fontsize{30}{34}\selectfont The End};
\node[white!88] at (10.5,4.7) {\bn\fontsize{15}{20}\selectfont তোমার পরিশ্রমই তোমার সাফল্যের চাবিকাঠি};
\node[white!85,font=\itshape] at (10.5,4.05) {\fontsize{13}{15}\selectfont Keep learning, keep building.};
\node[a360gold,font=\bfseries] at (10.5,3.1) {\fontsize{16}{18}\selectfont Abir Arafat Chawdhury};
\node[white!70] at (10.5,2.55) {\footnotesize CEO \& Founder --- Abir X Official Community};

% A360 badge (bottom)
\begin{scope}[shift={(8.55,1.1)}]
 \fill[a360purpled] (0,0) -- (2.6,0) -- (2.9,0.55) -- (0.3,0.55) -- cycle;
 \node[white,font=\bfseries] at (1.5,0.28) {\fontsize{17}{17}\selectfont A360};
 \fill[a360red] (0.18,-0.64) -- (2.78,-0.64) -- (3.08,-0.09) -- (0.48,-0.09) -- cycle;
 \node[white,font=\bfseries] at (1.66,-0.37) {\fontsize{10}{10}\selectfont PROGRAMMING};
 \fill[a360purpled] (3.0,0.0) -- (3.36,0.55) -- (3.62,0.55) -- (3.26,0.0) -- cycle;
\end{scope}
\end{tikzpicture}
\vfill


\end{document}"""

import subprocess, os, shutil, urllib.request, hashlib

# === Smart Formula Encyclopedia ===
# By Abir Arafat Chawdhury  (Physics + Chemistry + Higher Mathematics)
# Self-contained builder: downloads the Bengali font, installs xelatex if
# needed, and compiles a single, fully-typeset book PDF.

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
    return head in (b"\x00\x01\x00\x00", b"OTTO", b"ttcf")

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
        except Exception as e:
            last_error = e
    if not good_font(path):
        raise RuntimeError("font download failed: " + name + " " + str(last_error))

with open("logs/font_hashes.log", "w", encoding="utf-8") as fh:
    for name in sorted(font_sources):
        path = os.path.join("fonts", name)
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
        fh.write(f"{name}\t{os.path.getsize(path)}\t{digest}\n")

tex_content = tex_content.replace("\u200d", "")

with open("book.tex", "w", encoding="utf-8") as fh:
    fh.write(tex_content)

# Install a TeX engine if missing. Tries apt (VPS), else nix (Lovable sandbox).
if not shutil.which("xelatex"):
    if shutil.which("apt-get"):
        run("apt-get update -qq --allow-unauthenticated >>logs/apt.log 2>&1; "
            "apt-get install -y --no-install-recommends texlive-xetex "
            "texlive-fonts-recommended texlive-latex-extra texlive-pictures "
            "texlive-lang-other lmodern fonts-freefont-otf fonts-dejavu "
            ">>logs/apt.log 2>&1")
    elif shutil.which("nix"):
        out = subprocess.run(
            "nix build --no-link --print-out-paths 'nixpkgs#texliveFull'",
            shell=True, executable="/bin/bash", capture_output=True, text=True
        ).stdout.strip().splitlines()
        if out:
            os.environ["PATH"] = out[-1] + "/bin:" + os.environ["PATH"]

run("fc-cache -f ./fonts >>logs/fontcache.log 2>&1")

if not shutil.which("xelatex"):
    raise RuntimeError("xelatex not found after setup")

passes = []
for i in range(1, 4):  # 3 passes: body + table of contents + page refs
    code = run("xelatex -halt-on-error -file-line-error -interaction=nonstopmode "
               "book.tex >logs/xelatex_pass" + str(i) + ".log 2>&1")
    passes.append(code)
    if code != 0:
        raise RuntimeError("xelatex failed; see logs/xelatex_pass" + str(i) + ".log")

print("PDF ready:", os.path.exists("book.pdf"), "passes:", passes)
