import os
import pathlib
import shutil
import subprocess
import sys
import urllib.request

tex_content = (
    '\documentclass[8pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath}
\usepackage{unicode-math}
\usepackage{graphicx}
\usepackage{adjustbox}
\usepackage{tabularx}
\usepackage{array}
\usepackage{ragged2e}
\usepackage[margin=1.15cm,top=1.2cm,bottom=1.05cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\usepackage{tikz}
\usetikzlibrary{calc,arrows.meta,decorations.pathreplacing,patterns}
\pagestyle{empty}

\tolerance=9999
\emergencystretch=36pt
\hbadness=99999
\vbadness=99999
\hfuzz=0pt
\vfuzz=0pt
\widowpenalty=10000
\clubpenalty=10000
\binoppenalty=9999
\relpenalty=9999
\allowdisplaybreaks[4]
\sloppy
\setlength{\overfullrule}{0pt}
\lineskiplimit=1pt
\lineskip=2pt

\setmainfont{Noto Serif}[Ligatures=TeX]
\setmathfont{latinmodern-math.otf}[Path=./fonts/]
\newfontfamily\mathfallback{Noto Serif}
\newfontfamily\bn{NotoSerifBengali.ttf}[Path=./fonts/, Renderer=HarfBuzz, Script=Bengali]
\usepackage{ucharclasses}
\setTransitionTo{Bengali}{\begingroup\bn}
\setTransitionFrom{Bengali}{\endgroup}

\definecolor{sectionbg}{RGB}{55,55,55}
\definecolor{diagbg}{RGB}{246,246,250}
\definecolor{parablue}{RGB}{25,95,185}
\definecolor{focusred}{RGB}{202,54,54}
\definecolor{directgreen}{RGB}{24,138,96}
\definecolor{axisgray}{RGB}{72,77,84}
\definecolor{guideorange}{RGB}{225,130,35}
\definecolor{softblue}{RGB}{232,242,252}
\definecolor{softgreen}{RGB}{232,247,240}
\definecolor{softorange}{RGB}{252,242,226}

\newcommand{\B}[1]{\ifmmode\text{{\bn #1}}\else{\bn #1}\fi}

\newcommand{\chsec}[1]{%
  \par\addvspace{5pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth-2\fboxsep\relax}{%
    \centering\bfseries\footnotesize\color{white}\B{#1}}}%
  \par\addvspace{3pt}\noindent\ignorespaces}

\newcommand{\diag}[1]{%
  \par\addvspace{3pt}%
  \noindent\begin{adjustbox}{max width=.94\linewidth,center}#1\end{adjustbox}%
  \par\addvspace{3pt}\noindent\ignorespaces}

\newenvironment{safetable}{%
  \par\addvspace{3pt}\noindent\begingroup\tiny\setlength{\tabcolsep}{1.6pt}\renewcommand{\arraystretch}{1.3}%
  \begin{adjustbox}{max width=.94\linewidth,center}%
}{%
  \end{adjustbox}\endgroup\par\addvspace{3pt}\noindent\ignorespaces%
}

\setlength{\columnseprule}{0pt}
\setlength{\columnsep}{15pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{2.2pt}
\raggedcolumns
\raggedbottom

\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\newcommand{\itm}[1]{\par\addvspace{2.7pt}\noindent\textbf{#1.}\;\ignorespaces}
\newcommand{\sub}[1]{\textbf{(#1)}\;\ignorespaces}
\newcolumntype{L}{>{\raggedright\arraybackslash}X}
\newcolumntype{Y}{>{\centering\arraybackslash}X}
\newcommand{\fulltablebegin}{\par\addvspace{3pt}\begingroup\normalsize\setlength{\tabcolsep}{6pt}\renewcommand{\arraystretch}{1.55}\begin{adjustbox}{max width=\textwidth,center}}
\newcommand{\fulltableend}{\end{adjustbox}\endgroup\par\addvspace{3pt}}

\begin{document}


\begin{center}
\noindent
{\bn\Large\bfseries একনজরে প্রয়োজনীয় সূত্রাবলি — প্রথম ও দ্বিতীয় পত্র}\hfill
\textnormal{\small By \textbf{Abir Arafat Chawdhury} [Introvert's Area]}
\vspace{3pt}
\end{center}

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

\sub{ii} \B{অব্যতিক্রমী (Non-singular) ম্যাট্রিক্স:} \B{যদি কোনো বর্গ ম্যাট্রিক্সের নির্ণায়কের মান শূন্য না হয় অর্থাৎ} $|A| \neq 0$ \B{হয়{\bn ।}}

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
\sub{i} $\displaystyle\lim_{x\to\infty} a^x \sin\frac{b}{a^x} = b$ \B{ [যখন, } $a > 0$ \B{]}
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
\sub{i} $\dfrac{d}{dx}(c) = 0$ \B{ [যখন, } $c$ \B{ ধ্রুবক]}
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
\sub{i} $\int_a^b \dfrac{\sin^n x}{\sin^n x + \cos^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, } $a+b = \frac{\pi}{2}$ \B{]}
\sub{ii} $\int_a^b \dfrac{\tan^n x}{\tan^n x + \cot^n x} dx = \int_a^b \dfrac{\cot^n x}{\tan^n x + \cot^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, } $a+b = \frac{\pi}{2}$ \B{]}
\sub{iii} $\int_a^b \dfrac{\sec^n x}{\sec^n x + \csc^n x} dx = \int_a^b \dfrac{\csc^n x}{\sec^n x + \csc^n x} dx = \dfrac{b-a}{2}$ \B{ [যখন, } $a+b = \frac{\pi}{2}$ \B{]}
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

\sub{xvi} $\displaystyle\int_0^a\!\frac{dx}{\sqrt{2ax-x^2}}=\frac{\pi}{2}$

\sub{xvii} $\displaystyle\int_0^a!\sqrt{a^2-x^2}\,dx=\frac{\pi a^2}{4}$

\sub{xviii} $\displaystyle\int_0^a\!\frac{1}{\sqrt{a^2-x^2}}\,dx=\frac{\pi}{2}$

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

\itm{2} $|x|=\begin{cases}x, & \mbox{\bn\scriptsize যখন } x>0\\0, & \mbox{\bn\scriptsize যখন } x=0\\-x, & \mbox{\bn\scriptsize যখন } x<0\end{cases}$

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

\end{multicols}
\clearpage
\chsec{অধ্যায়-৬: কণিক (Conics)}
\footnotesize
\itm{1} \B{দ্বিঘাত সমীকরণ ও কণিকের শ্রেণীবিভাগ:}
\sub{i} \B{সাধারণ দ্বিঘাত সমীকরণ:} $ax^2+2hxy+by^2+2gx+2fy+c=0$
\sub{ii} \B{নিশ্চায়ক:} $\Delta=abc+2fgh-af^2-bg^2-ch^2$
\sub{iii} $\Delta=0$ \B{ হলে সমীকরণটি একজোড়া সরলরেখা প্রকাশ করে{\bn ।}}
\sub{iv} $\Delta\neq0$ \B{ হলে: } $h=0,\ a=b$ \B{ হলে বৃত্ত; } $h^2-ab=0$ \B{ হলে পরাবৃত্ত } $(e=1)$\B{; } $h^2-ab<0$ \B{ হলে উপবৃত্ত } $(0<e<1)$\B{; } $h^2-ab>0$ \B{ হলে অধিবৃত্ত } $(e>1)$\B{; এবং } $h^2-ab>0,\ a+b=0$ \B{ হলে আয়তাকার অধিবৃত্ত{\bn ।}}

\itm{2} \B{পরাবৃত্তের পূর্ণাঙ্গ চিত্র ও তুলনামূলক সূত্রাবলী}
\begin{center}
\begin{tikzpicture}[x=1.35cm,y=1.12cm,every node/.style={font=\scriptsize}]
\fill[softblue] plot[domain=-2.25:2.25,samples=100] ({0.52*\x*\x},{\x}) -- (5.0,2.25) -- (5.0,-2.25) -- cycle;
\draw[->,axisgray,thick] (-1.35,0)--(5.35,0) node[right]{$x$};
\draw[->,axisgray,thick] (0,-2.75)--(0,2.75) node[above]{$y$};
\draw[very thick,parablue,smooth,domain=-2.35:2.35,samples=120] plot ({0.52*\x*\x},{\x});
\draw[directgreen,very thick,dashed] (-0.52,-2.55)--(-0.52,2.55) node[above]{$x=-a$};
\draw[guideorange,very thick] (0.52,-1.42)--(0.52,1.42) node[pos=.30,rotate=90,text=guideorange,fill=white,inner sep=1.5pt]{\B{উপকেন্দ্রিক লম্ব}};
\fill[focusred] (0.52,0) circle (2.1pt) node[below right]{$S(a,0)$};
\fill[axisgray] (0,0) circle (1.8pt) node[below left,xshift=-9pt,yshift=-3pt]{$A(0,0)$};
\fill[guideorange] (0.52,1.42) circle (1.5pt) node[right]{$L$};
\fill[guideorange] (0.52,-1.42) circle (1.5pt) node[left,xshift=-1pt]{$L'$};
\coordinate (P) at (2.15,2.03);
\fill[focusred] (P) circle (1.7pt) node[above right]{$P(x_1,y_1)$};
\draw[focusred,thick] (0.52,0)--(P) node[pos=.62,above,sloped]{$SP=x_1+a$};
\draw[directgreen,thick,densely dotted] (P)--(-0.52,2.03) node[midway,above]{$PM$};
\fill[directgreen] (-0.52,2.03) circle (1.4pt) node[left]{$M$};
\draw[guideorange,<->] (0,-2.55)--(0.52,-2.55) node[midway,below]{$a$};
\node[parablue] at (4.0,1.3) {$y^2=4ax$};
\node[directgreen] at (-1.0,-2.25){\B{নিয়ামক}};
\end{tikzpicture}
\end{center}
\fulltablebegin
\begin{tabularx}{\textwidth}{|L|Y|Y|Y|Y|}
\hline
\B{বৈশিষ্ট্য} & $y^2=4ax$ & $y^2=-4ax$ & $x^2=4ay$ & $x^2=-4ay$ \\
\hline
\B{খোলার দিক} & $+x$ & $-x$ & $+y$ & $-y$ \\
\hline
\B{শীর্ষবিন্দু} & $(0,0)$ & $(0,0)$ & $(0,0)$ & $(0,0)$ \\
\hline
\B{উপকেন্দ্র} & $(a,0)$ & $(-a,0)$ & $(0,a)$ & $(0,-a)$ \\
\hline
\B{অক্ষরেখা} & $y=0$ & $y=0$ & $x=0$ & $x=0$ \\
\hline
\B{নিয়ামক} & $x=-a$ & $x=a$ & $y=-a$ & $y=a$ \\
\hline
\B{উপকেন্দ্রিক লম্ব} & $x=a$ & $x=-a$ & $y=a$ & $y=-a$ \\
\hline
\B{লম্বের প্রান্তবিন্দু} & $(a,\pm2a)$ & $(-a,\pm2a)$ & $(\pm2a,a)$ & $(\pm2a,-a)$ \\
\hline
\B{লম্বের দৈর্ঘ্য} & $4a$ & $4a$ & $4a$ & $4a$ \\
\hline
\B{শীর্ষে স্পর্শক} & $x=0$ & $x=0$ & $y=0$ & $y=0$ \\
\hline
\B{নিয়ামক ও অক্ষের ছেদবিন্দু} & $(-a,0)$ & $(a,0)$ & $(0,-a)$ & $(0,a)$ \\
\hline
\B{$P(x_1,y_1)$-এর উপকেন্দ্রিক দূরত্ব} & $x_1+a$ & $a-x_1$ & $y_1+a$ & $a-y_1$ \\
\hline
\B{প্যারামেট্রিক বিন্দু} & $(at^2,2at)$ & $(-at^2,2at)$ & $(2at,at^2)$ & $(2at,-at^2)$ \\
\hline
\end{tabularx}
\fulltableend
\sub{B} \B{শীর্ষবিন্দু $(\alpha,\beta)$ হলে:}
\sub{i} $(y-\beta)^2=4a(x-\alpha)$\B{: শীর্ষ } $(\alpha,\beta)$\B{, উপকেন্দ্র } $(\alpha+a,\beta)$\B{, অক্ষ } $y=\beta$\B{, নিয়ামক } $x=\alpha-a$\B{{\bn ।}}
\sub{ii} $(x-\alpha)^2=4a(y-\beta)$\B{: শীর্ষ } $(\alpha,\beta)$\B{, উপকেন্দ্র } $(\alpha,\beta+a)$\B{, অক্ষ } $x=\alpha$\B{, নিয়ামক } $y=\beta-a$\B{{\bn ।}}

\clearpage
\chsec{অধ্যায়-৬: কণিক — উপবৃত্ত (Ellipse)}
\footnotesize
\begin{center}
\begin{tikzpicture}[x=1.0cm,y=1.0cm,every node/.style={font=\scriptsize}]
\fill[softgreen] (0,0) ellipse (4.15 and 2.35);
\draw[->,axisgray,thick] (-5.35,0)--(5.35,0) node[right]{$x$};
\draw[->,axisgray,thick] (0,-3.0)--(0,3.0) node[above]{$y$};
\draw[very thick,parablue] (0,0) ellipse (4.15 and 2.35);
\draw[directgreen,very thick,dashed] (-5.05,-2.85)--(-5.05,2.85) node[above]{$x=-a/e$};
\draw[directgreen,very thick,dashed] (5.05,-2.85)--(5.05,2.85) node[above]{$x=a/e$};
\draw[guideorange,thick] (-3.4,-1.35)--(-3.4,1.35);
\draw[guideorange,thick] (3.4,-1.35)--(3.4,1.35);
\fill[focusred] (-3.4,0) circle (2pt) node[below left,xshift=-6pt,yshift=-1pt]{$S'(-ae,0)$};
\fill[focusred] (3.4,0) circle (2pt) node[below right,xshift=-6pt,yshift=-1pt]{$S(ae,0)$};
\fill[axisgray] (-4.15,0) circle (1.7pt) node[above left]{$A'(-a,0)$};
\fill[axisgray] (4.15,0) circle (1.7pt) node[above right]{$A(a,0)$};
\fill[axisgray] (0,2.35) circle (1.7pt) node[above right]{$B(0,b)$};
\fill[axisgray] (0,-2.35) circle (1.7pt) node[right,xshift=1pt]{$B'(0,-b)$};
\coordinate (P) at (2.2,1.99);
\fill[focusred] (P) circle (1.8pt) node[above right]{$P$};
\draw[focusred,thick] (-3.4,0)--(P) node[midway,above,sloped]{$S'P$};
\draw[guideorange,thick] (3.4,0)--(P) node[midway,below,sloped]{$SP$};
\draw[directgreen,densely dotted,thick] (P)--(5.05,1.99) node[midway,above]{$PM$};
\draw[<->,axisgray] (-4.15,-2.78)--(4.15,-2.78) node[pos=.28,below]{\B{বৃহৎ অক্ষ }$2a$};
\node[parablue] at (0,0.6) {$\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$};
\end{tikzpicture}
\end{center}
\B{এখানে } $a>b>0$\B{, } $c=ae=\sqrt{a^2-b^2}$\B{ এবং } $b^2=a^2(1-e^2)$\B{{\bn ।} উল্লম্ব বৃহৎ অক্ষের ক্ষেত্রে $a,b$-এর ভূমিকা বিনিময় হবে{\bn ।}}
\fulltablebegin
\begin{tabularx}{1.32\textwidth}{|L|Y|Y|}
\hline
\B{বৈশিষ্ট্য} & $a>b$ & $b>a$ \\
\hline
\B{কেন্দ্র} & $(0,0)$ & $(0,0)$ \\
\hline
\B{উৎকেন্দ্রিকতা} & $e=\sqrt{1-\dfrac{b^2}{a^2}}$ & $e=\sqrt{1-\dfrac{a^2}{b^2}}$ \\
\hline
\B{উপকেন্দ্রদ্বয়} & $(\pm ae,0)$ & $(0,\pm be)$ \\
\hline
\B{প্রধান শীর্ষবিন্দু} & $(\pm a,0)$ & $(0,\pm b)$ \\
\hline
\B{সহ-শীর্ষবিন্দু} & $(0,\pm b)$ & $(\pm a,0)$ \\
\hline
\B{বৃহৎ অক্ষ: সমীকরণ ও দৈর্ঘ্য} & $y=0,\ 2a$ & $x=0,\ 2b$ \\
\hline
\B{ক্ষুদ্র অক্ষ: সমীকরণ ও দৈর্ঘ্য} & $x=0,\ 2b$ & $y=0,\ 2a$ \\
\hline
\B{নিয়ামকদ্বয়} & $x=\pm\dfrac{a}{e}$ & $y=\pm\dfrac{b}{e}$ \\
\hline
\B{উপকেন্দ্রিক লম্বের সমীকরণ ও দৈর্ঘ্য} & $x=\pm ae,\ \dfrac{2b^2}{a}$ & $y=\pm be,\ \dfrac{2a^2}{b}$ \\
\hline
\B{উপকেন্দ্রদ্বয় ও নিয়ামকদ্বয়ের দূরত্ব} & $2ae,\ \dfrac{2a}{e}$ & $2be,\ \dfrac{2b}{e}$ \\
\hline
\B{কেন্দ্র থেকে উপকেন্দ্র, শীর্ষ ও নিয়ামক} & $ae,\ a,\ \dfrac{a}{e}$ & $be,\ b,\ \dfrac{b}{e}$ \\
\hline
\B{উপকেন্দ্র থেকে নিকটবর্তী শীর্ষ} & $a-ae=a(1-e)$ & $b-be=b(1-e)$ \\
\hline
\B{উপকেন্দ্র থেকে দূরবর্তী শীর্ষ} & $a+ae=a(1+e)$ & $b+be=b(1+e)$ \\
\hline
\B{উপকেন্দ্র থেকে নিকট ও বিপরীত নিয়ামক} & $\dfrac{a}{e}-ae,\ \dfrac{a}{e}+ae$ & $\dfrac{b}{e}-be,\ \dfrac{b}{e}+be$ \\
\hline
\B{শীর্ষ থেকে নিকট ও বিপরীত নিয়ামক} & $\dfrac{a}{e}-a,\ \dfrac{a}{e}+a$ & $\dfrac{b}{e}-b,\ \dfrac{b}{e}+b$ \\
\hline
\B{উপকেন্দ্রিক দূরত্বের সমষ্টি} & $SP+S'P=2a$ & $SP+S'P=2b$ \\
\hline
\B{প্যারামেট্রিক বিন্দু} & $(a\cos\theta,b\sin\theta)$ & $(a\cos\theta,b\sin\theta)$ \\
\hline
\end{tabularx}
\fulltableend

\clearpage
\chsec{অধ্যায়-৬: কণিক — অধিবৃত্ত (Hyperbola)}
\footnotesize
\begin{center}
\begin{tikzpicture}[x=1.0cm,y=0.92cm,every node/.style={font=\scriptsize}]
\fill[softorange,opacity=.75] (-5.0,-3.15) rectangle (5.0,3.15);
\fill[white] (-3.95,-2.25) rectangle (3.95,2.25);
\draw[->,axisgray,thick] (-5.45,0)--(5.45,0) node[right]{$x$};
\draw[->,axisgray,thick] (0,-3.35)--(0,3.35) node[above]{$y$};
\draw[guideorange,dashed,very thick] (-5.15,-3.09)--(5.15,3.09) node[above right]{$y=\frac{b}{a}x$};
\draw[guideorange,dashed,very thick] (-5.15,3.09)--(5.15,-3.09) node[below right]{$y=-\frac{b}{a}x$};
\draw[axisgray,densely dotted] (-2.6,-1.56) rectangle (2.6,1.56);
\draw[very thick,parablue,smooth,domain=-1.2:1.2,samples=100] plot ({2.6*cosh(\x)},{1.56*sinh(\x)});
\draw[very thick,parablue,smooth,domain=-1.2:1.2,samples=100] plot ({-2.6*cosh(\x)},{1.56*sinh(\x)});
\draw[directgreen,very thick,dashed] (-1.63,-3.05)--(-1.63,3.05) node[above]{$x=-a/e$};
\draw[directgreen,very thick,dashed] (1.63,-3.05)--(1.63,3.05) node[above]{$x=a/e$};
\draw[guideorange,very thick] (-4.15,-1.1)--(-4.15,1.1);
\draw[guideorange,very thick] (4.15,-1.1)--(4.15,1.1);
\fill[focusred] (-4.15,0) circle (2.1pt) node[below left,xshift=-8pt,yshift=-1pt]{$S'(-ae,0)$};
\fill[focusred] (4.15,0) circle (2.1pt) node[below right,xshift=-8pt,yshift=-1pt]{$S(ae,0)$};
\fill[axisgray] (-2.6,0) circle (1.8pt) node[below left,xshift=-4pt,yshift=-1pt]{$A'(-a,0)$};
\fill[axisgray] (2.6,0) circle (1.8pt) node[below right,xshift=-4pt,yshift=-1pt]{$A(a,0)$};
\coordinate (P) at (3.4,1.31);
\fill[focusred] (P) circle (1.8pt) node[above right]{$P$};
\draw[focusred,thick] (-4.15,0)--(P) node[pos=.42,above,sloped]{$S'P$};
\draw[guideorange,thick] (4.15,0)--(P) node[midway,right]{$SP$};
\draw[directgreen,densely dotted,thick] (P)--(1.63,1.31) node[midway,below=1pt]{$PM$};
\node[parablue] at (0,0.65) {$\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$};
\node[axisgray] at (0,-1.83){\B{সহায়ক আয়তক্ষেত্র}};
\end{tikzpicture}
\end{center}
\B{এখানে } $c=ae=\sqrt{a^2+b^2}$\B{, } $e=\sqrt{1+\dfrac{b^2}{a^2}}>1$\B{ এবং } $b^2=a^2(e^2-1)$\B{{\bn ।}}
\fulltablebegin
\begin{tabularx}{1.32\textwidth}{|L|Y|Y|}
\hline
\B{বৈশিষ্ট্য} & $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ & $\dfrac{y^2}{b^2}-\dfrac{x^2}{a^2}=1$ \\
\hline
\B{কেন্দ্র ও উৎকেন্দ্রিকতা} & $(0,0),\ \sqrt{1+\dfrac{b^2}{a^2}}$ & $(0,0),\ \sqrt{1+\dfrac{a^2}{b^2}}$ \\
\hline
\B{উপকেন্দ্রদ্বয় ও শীর্ষবিন্দুদ্বয়} & $(\pm ae,0),\ (\pm a,0)$ & $(0,\pm be),\ (0,\pm b)$ \\
\hline
\B{আড় অক্ষ: সমীকরণ ও দৈর্ঘ্য} & $y=0,\ 2a$ & $x=0,\ 2b$ \\
\hline
\B{অনুবন্ধী অক্ষ: সমীকরণ ও দৈর্ঘ্য} & $x=0,\ 2b$ & $y=0,\ 2a$ \\
\hline
\B{নিয়ামকদ্বয়} & $x=\pm\dfrac{a}{e}$ & $y=\pm\dfrac{b}{e}$ \\
\hline
\B{উপকেন্দ্রিক লম্বের সমীকরণ ও দৈর্ঘ্য} & $x=\pm ae,\ \dfrac{2b^2}{a}$ & $y=\pm be,\ \dfrac{2a^2}{b}$ \\
\hline
\B{অসীমতটদ্বয়} & $y=\pm\dfrac{b}{a}x$ & $y=\pm\dfrac{b}{a}x$ \\
\hline
\B{কেন্দ্র থেকে উপকেন্দ্র, শীর্ষ ও নিয়ামক} & $ae,\ a,\ \dfrac{a}{e}$ & $be,\ b,\ \dfrac{b}{e}$ \\
\hline
\B{উপকেন্দ্র থেকে নিকটবর্তী শীর্ষ} & $ae-a=a(e-1)$ & $be-b=b(e-1)$ \\
\hline
\B{উপকেন্দ্র থেকে দূরবর্তী শীর্ষ} & $ae+a=a(e+1)$ & $be+b=b(e+1)$ \\
\hline
\B{উপকেন্দ্র থেকে নিকট ও বিপরীত নিয়ামক} & $ae-\dfrac{a}{e},\ ae+\dfrac{a}{e}$ & $be-\dfrac{b}{e},\ be+\dfrac{b}{e}$ \\
\hline
\B{শীর্ষ থেকে নিকট ও বিপরীত নিয়ামক} & $a-\dfrac{a}{e},\ a+\dfrac{a}{e}$ & $b-\dfrac{b}{e},\ b+\dfrac{b}{e}$ \\
\hline
\B{উপকেন্দ্র, শীর্ষ ও নিয়ামকদ্বয়ের দূরত্ব} & $2ae,\ 2a,\ \dfrac{2a}{e}$ & $2be,\ 2b,\ \dfrac{2b}{e}$ \\
\hline
\B{উপকেন্দ্রিক দূরত্বের অন্তর} & $|SP-S'P|=2a$ & $|SP-S'P|=2b$ \\
\hline
\B{প্যারামেট্রিক বিন্দু} & $(a\sec\theta,b\tan\theta)$ & $(a\tan\theta,b\sec\theta)$ \\
\hline
\end{tabularx}
\fulltableend

\itm{5} \B{স্পর্শক ও অভিলম্ব সংক্রান্ত সমীকরণ}
\sub{A} \B{পরাবৃত্ত } $y^2=4ax$\B{: } $c=\dfrac{a}{m}$\B{; স্পর্শবিন্দু } $\left(\dfrac{a}{m^2},\dfrac{2a}{m}\right)$\B{; স্পর্শক } $yy_1=2a(x+x_1)$\B{; অভিলম্ব } $y-y_1=-\dfrac{y_1}{2a}(x-x_1)$\B{{\bn ।}}
\sub{B} \B{উপবৃত্ত } $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$\B{: } $c=\pm\sqrt{a^2m^2+b^2}$\B{; স্পর্শক } $\dfrac{xx_1}{a^2}+\dfrac{yy_1}{b^2}=1$\B{; অভিলম্ব } $\dfrac{a^2x}{x_1}-\dfrac{b^2y}{y_1}=a^2-b^2$\B{{\bn ।}}
\sub{C} \B{অধিবৃত্ত } $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$\B{: } $c=\pm\sqrt{a^2m^2-b^2}$\B{; স্পর্শক } $\dfrac{xx_1}{a^2}-\dfrac{yy_1}{b^2}=1$\B{; অভিলম্ব } $\dfrac{a^2x}{x_1}+\dfrac{b^2y}{y_1}=a^2+b^2$\B{{\bn ।}}
\itm{6} \B{উপবৃত্তের ক্ষেত্রফল } $\pi ab$\B{; উপবৃত্তের নিয়ামক বৃত্ত } $x^2+y^2=a^2+b^2$\B{; অধিবৃত্তের নিয়ামক বৃত্ত } $x^2+y^2=a^2-b^2$\B{; আয়তাকার অধিবৃত্তে } $a=b,\ e=\sqrt2$ \B{ এবং অসীমতটদ্বয় পরস্পর লম্ব{\bn ।}}

\clearpage
\begin{multicols}{2}\footnotesize
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
\end{document}
'
)

workdir = pathlib.Path(__file__).resolve().parent
os.chdir(workdir)
pathlib.Path("fonts").mkdir(exist_ok=True)
font_path = pathlib.Path("fonts/NotoSerifBengali.ttf")
if not font_path.exists():
    candidates = [
        "/usr/share/fonts/truetype/noto/NotoSerifBengali-Regular.ttf",
        "/usr/share/fonts/opentype/noto/NotoSerifBengali-Regular.otf",
    ]
    copied = False
    for candidate in candidates:
        p = pathlib.Path(candidate)
        if p.exists():
            shutil.copyfile(p, font_path)
            copied = True
            break
    if not copied:
        url = "https://github.com/google/fonts/raw/main/ofl/notoserifbengali/NotoSerifBengali%5Bwdth%2Cwght%5D.ttf"
        urllib.request.urlretrieve(url, font_path)

tex_file = pathlib.Path("highermath_fixed.tex")
tex_file.write_text(tex_content, encoding="utf-8")

engines = [
    ["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex_file.name],
    ["tectonic", "--keep-intermediates", "--reruns", "2", tex_file.name],
]
last_error = None
for engine in engines:
    if shutil.which(engine[0]) is None:
        continue
    try:
        for _ in range(2 if engine[0] == "xelatex" else 1):
            result = subprocess.run(engine, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            if result.returncode != 0:
                last_error = result.stdout
                raise RuntimeError(result.stdout)
        break
    except RuntimeError:
        continue
else:
    if last_error:
        print(last_error)
    raise SystemExit("No working LaTeX engine found. Install xelatex or tectonic and run this script again.")

pdf = pathlib.Path("highermath_fixed.pdf")
if not pdf.exists():
    alt = tex_file.with_suffix(".pdf")
    if alt.exists():
        alt.rename(pdf)
if not pdf.exists():
    raise SystemExit("PDF build failed: output file was not created.")
print(f"PDF ready: {pdf.resolve()}")
