#Copyright @ISmartCoder 2026-Present
#Updates Channel @abirxdhackz 
import subprocess, os

tex_content = r"""
\documentclass[9pt,a4paper]{extarticle}
\usepackage{fontspec}
\usepackage{amsmath,amssymb}
\usepackage[margin=1.0cm, top=1.2cm, bottom=1.0cm]{geometry}
\usepackage{multicol}
\usepackage{xcolor}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{microtype}
\pagestyle{empty}
\setlength{\emergencystretch}{10pt}
\hbadness=10000
\setmainfont{Latin Modern Roman}
\newfontfamily\bn{Noto Serif Bengali}[Script=Bengali, BoldFont=Noto Serif Bengali Bold]
\definecolor{sectionbg}{RGB}{65,65,65}

\newcommand{\B}[1]{{\bn #1}}

\newcommand{\chsec}[1]{%
  \vspace{3pt}%
  \noindent\colorbox{sectionbg}{\parbox{\dimexpr\linewidth\relax}{%
    \centering\bfseries\small\color{white}\B{#1}%
  }}%
  \vspace{1pt}\par
}

\setlength{\columnseprule}{0.3pt}
\setlength{\columnsep}{8pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{1pt}

\setlist[enumerate]{nosep, leftmargin=*, topsep=0pt}
\newcommand{\itm}[1]{\textbf{#1.}\;}
\newcommand{\sub}[1]{\textbf{(#1)}\;}

\begin{document}

\begin{center}
\noindent
{\bn\Large\bfseries একনজরে প্রয়োজনীয় সূত্রাবলি — প্রথম ও দ্বিতীয় পত্র}\hfill
\textnormal{\small By \textbf{Abir Arafat Chawdhury} [Introvert's Area]}
\vspace{3pt}
\end{center}

\vspace{2pt}

\begin{multicols}{2}

\noindent\colorbox{black}{\parbox{\dimexpr\linewidth\relax}{\centering\bfseries\large\color{white}{\bn প্রথম পত্র}}}
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

\B{এবং} $x=\dfrac{D_x}{D},\quad y=\dfrac{D_y}{D},\quad z=\dfrac{D_z}{D}$

\chsec{অধ্যায়-২: ভেক্টর}

\itm{1} $\vec{A}=A_x\hat{i}+A_y\hat{j}+A_z\hat{k}$ \B{ভেক্টরের মান,} $|\vec{A}|=\sqrt{A_x^2+A_y^2+A_z^2}$

\itm{2} $\vec{A}$ \B{ভেক্টরের দিকে একক ভেক্টর,} $\hat{\eta}=\dfrac{\vec{A}}{|\vec{A}|}$

\itm{3} \B{দুইটি ভেক্টর} $\vec{A}$ \B{ও} $\vec{B}$ \B{হলে, স্কেলার গুণন,}

$\vec{A}\cdot\vec{B}=|\vec{A}||\vec{B}|\cos\theta$\B{; $\theta$ ভেক্টর দুইটির মধ্যবর্তী কোণ।}

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

\chsec{অধ্যায়-৩: সরলরেখা}

\itm{1} \B{কার্তেসীয় স্থানাঙ্ক} $(x,y)$ \B{এবং পোলার স্থানাঙ্ক} $(r,\theta)$ \B{হলে,}

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

\sub{iii} \B{বিন্দুত্রয় সমরেখ হলে, ত্রিভুজের ক্ষেত্রফল শূন্য হবে এবং বিপরীতক্রমে সত্য।}

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

\itm{9} $y$\B{-অক্ষকে ছেদ করে এরূপ সরলরেখার সমীকরণ,} $y=mx+c$\B{; একে ঢাল আকার সমীকরণও বলা হয়।}

\itm{10} \B{মূলবিন্দু ও} $(x_1,y_1)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$y=\dfrac{y_1}{x_1}x$

\itm{11} \B{ঢাল} $m$ \B{এবং} $(x_1,y_1)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$y-y_1=m(x-x_1)$

\itm{12} $x$\B{-অক্ষ ও} $y$\B{-অক্ষের ছেদক রেখার সমীকরণ,} $\dfrac{x}{a}+\dfrac{y}{b}=1$\B{; যেখানে,} $x$ \B{ও} $y$ \B{অক্ষের ছেদিতাংশ যথাক্রমে} $a$ \B{ও} $b$\B{; রেখাটি} $x$\B{-অক্ষকে} $(a,0)$ \B{এবং} $y$\B{-অক্ষকে} $(0,b)$ \B{বিন্দুতে ছেদ করে।}

\itm{13} $(x_1,y_1)$ \B{ও} $(x_2,y_2)$ \B{বিন্দুগামী সরলরেখার সমীকরণ,}

$\dfrac{y-y_1}{y_1-y_2}=\dfrac{x-x_1}{x_1-x_2}$

\B{বা} $y-y_1=\dfrac{y_2-y_1}{x_2-x_1}(x-x_1)$

\B{এবং ঢাল} $=\dfrac{\text{\B{কোটিদ্বয়ের অন্তর}}}{\text{\B{ভুজদ্বয়ের অন্তর}}}=\dfrac{y_2-y_1}{x_2-x_1}$

\itm{14} \B{মূলবিন্দু হতে একটি সরলরেখার উপর অঙ্কিত লম্বের দৈর্ঘ্য} $p$ \B{এবং} $x$\B{-অক্ষের সাথে উক্ত লম্বের অন্তর্ভুক্ত কোণ} $\alpha$ \B{হলে, সরলরেখার সমীকরণ,}

$x\cos\alpha+y\sin\alpha=p$

\itm{15} $ax+by+c=0$ \B{রেখার সমান্তরাল ও লম্ব যেকোনো রেখার সমীকরণ যথাক্রমে,}

$ax+by+k=0$ \B{ও} $bx-ay+k=0$\B{; যেখানে,} $k$ \B{ইচ্ছাধীন ধ্রুবক।}

\itm{16} \B{দুইটি রেখার ছেদবিন্দুগামী সরলরেখার সমীকরণ, (একটি সরলরেখা)} $+k$ \B{(অপর সরলরেখা)} $=0$\B{; যেখানে} $k$ \B{ইচ্ছাধীন ধ্রুবক।}

\itm{17} $a_1x+b_1y+c_1=0$, $a_2x+b_2y+c_2=0$ \B{ও} $a_3x+b_3y+c_3=0$ \B{সরলরেখা তিনটি সমবিন্দু হওয়ার শর্ত:}

$\begin{vmatrix}a_1&b_1&c_1\\a_2&b_2&c_2\\a_3&b_3&c_3\end{vmatrix}=0$ \B{এবং বিপরীতক্রমে সত্য।}

\itm{18} $y=m_1x+c_1$ \B{ও} $y=m_2x+c_2$ \B{বা দুইটি সরলরেখার অন্তর্ভুক্ত কোণ} $\varphi$ \B{হলে,}

$\tan\varphi=\pm\dfrac{m_1-m_2}{1+m_1m_2}$

\B{[}$\because\; m_1=\tan\theta_1,\; m_2=\tan\theta_2$\B{]}

\itm{19} $m_1$ \B{ও} $m_2$ \B{ঢালবিশিষ্ট দুইটি সরলরেখা পরস্পর সমান্তরাল ও লম্ব হলে যথাক্রমে,}

$m_1=m_2$ \B{ও} $m_1m_2=-1$

\itm{20} $P(x_1,y_1)$ \B{বিন্দু হতে} $ax+by+c=0$ \B{সরলরেখার উপর অঙ্কিত লম্বের দৈর্ঘ্য বা লম্বদূরত্ব}

$=\dfrac{|ax_1+by_1+c|}{\sqrt{a^2+b^2}}$

\itm{21} $ax+by+c_1=0$ \B{এবং} $ax+by+c_2=0$ \B{সমান্তরাল সরলরেখা দুইটির মধ্যবর্তী দূরত্ব}

$=\dfrac{|c_1-c_2|}{\sqrt{a^2+b^2}}$

\itm{22} $a_1x+b_1y+c_1=0$ \B{এবং} $a_2x+b_2y+c_2=0$ \B{রেখাদ্বয়ের অন্তর্ভুক্ত কোণের সমদ্বিখণ্ডকের সমীকরণ}

\[
\frac{a_1x+b_1y+c_1}{\sqrt{a_1^2+b_1^2}}=\pm\frac{a_2x+b_2y+c_2}{\sqrt{a_2^2+b_2^2}}
\]

\chsec{অধ্যায়-৪: বৃত্ত}

\itm{1} \sub{i} $(0,0)$ \B{কেন্দ্র এবং} $a$ \B{ব্যাসার্ধবিশিষ্ট বৃত্তের সমীকরণ,} $x^2+y^2=a^2$

\sub{ii} $(h,k)$ \B{কেন্দ্র এবং} $r$ \B{ব্যাসার্ধবিশিষ্ট বৃত্তের সমীকরণ,} $(x-h)^2+(y-k)^2=r^2$

\itm{2} \B{বৃত্তের সাধারণ সমীকরণ,} $x^2+y^2+2gx+2fy+c=0$ \B{যার--}

\sub{i} \B{কেন্দ্র} $(-g,-f)$ \B{এবং ব্যাসার্ধ} $=\sqrt{g^2+f^2-c}$

\sub{ii} $x$\B{-অক্ষের খণ্ডিতাংশ} $=2\sqrt{g^2-c}$ \B{এবং} $y$\B{-অক্ষের খণ্ডিতাংশ} $=2\sqrt{f^2-c}$

\sub{iii} $x$\B{-অক্ষকে স্পর্শ করলে} $g^2=c$\B{;} $y$\B{-অক্ষকে স্পর্শ করলে} $f^2=c$ \B{এবং উভয় অক্ষকে স্পর্শ করলে} $g^2=f^2=c$.

\sub{iv} $-g=0$ \B{বা,} $g=0$ \B{হলে বৃত্তের কেন্দ্র} $y$\B{-অক্ষের উপর অবস্থিত এবং} $-f=0$ \B{বা} $f=0$ \B{হলে বৃত্তের কেন্দ্র} $x$\B{-অক্ষের উপর অবস্থিত।}

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

\itm{6} \sub{i} \B{দুইটি বৃত্ত পরস্পর বহিঃস্থভাবে স্পর্শ করলে, কেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব} $=$ \B{ব্যাসার্ধদ্বয়ের যোগফল।}

\sub{ii} \B{দুইটি বৃত্ত পরস্পরকে অন্তঃস্থভাবে স্পর্শ করলে, কেন্দ্রদ্বয়ের মধ্যবর্তী দূরত্ব} $=$ \B{ব্যাসার্ধদ্বয়ের অন্তর।}

\itm{7} $S_1=0$ \B{এবং} $S_2=0$ \B{দুইটি বৃত্তের ছেদবিন্দুগামী যেকোনো বৃত্তের সমীকরণ,}

$S_1+kS_2=0$\B{; যেখানে} $k$ \B{একটি অশূন্য ধ্রুবক।}

\itm{8} $S_1=0$ \B{বৃত্ত এবং} $L=0$ \B{সরলরেখা হলে, এদের ছেদবিন্দুগামী যেকোনো বৃত্তের সমীকরণ,}

$S_1+kL=0$\B{; যেখানে} $k$ \B{একটি অশূন্য ধ্রুবক।}

\itm{9} $(x_1,y_1)$ \B{ও} $(x_2,y_2)$ \B{বিন্দুগামী বৃত্তের সমীকরণ}

$(x-x_1)(x-x_2)+(y-y_1)(y-y_2)+k\{(x-x_1)(y_1-y_2)-(y-y_1)(x_1-x_2)\}=0$\B{; যেখানে,} $k$ \B{একটি ইচ্ছামূলক ধ্রুবক।}

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

\chsec{অধ্যায়-৫: বিন্যাস ও সমাবেশ}

\itm{1} \sub{i} $n$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিস থেকে} $r$ \B{সংখ্যক জিনিসের বিন্যাস}

${}^nP_r=\dfrac{n!}{(n-r)!}$\B{;} $n\geq r$

\sub{ii} $n!=n(n-1)!=n(n-1)(n-2)!=n(n-1)(n-2)\cdots3\cdot2\cdot1$\B{;} ${}^nP_n=n!$, $0!=1$

\sub{iii} $p$ \B{সংখ্যক এক প্রকার,} $q$ \B{সংখ্যক অন্য এক প্রকার, $r$ সংখ্যক অন্য আর এক প্রকার বাকিগুলি ভিন্ন ভিন্ন এরূপ} $n$ \B{সংখ্যক বস্তুর বিন্যাস সংখ্যা} $=\dfrac{n!}{p!\,q!\,r!}$

\sub{iv} $n$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিস থেকে প্রতিবার} $r$ \B{সংখ্যক জিনিস নিয়ে বিন্যাস সংখ্যা (যেখানে, যেকোনো জিনিসের} $r$ \B{সংখ্যক বার পুনরাবৃত্তি ঘটতে পারে)} $=n^r$

\itm{2} \sub{i} ${}^nC_r=\dfrac{n!}{r!\,(n-r)!}={}^nC_{n-r}$ \B{(সম্পূরক সমাবেশ)}

\sub{ii} ${}^nC_r+{}^nC_{r-1}={}^{n+1}C_r$

\sub{iii} ${}^nC_x={}^nC_y$ \B{হলে,} $x+y=n$

\itm{3} \sub{i} \B{১ম প্রকারের} $p$ \B{সংখ্যক ২য় প্রকারের} $q$ \B{সংখ্যক ও ৩য় প্রকারের} $r$ \B{সংখ্যক থেকে যেকোনো সংখ্যক জিনিস নিয়ে মোট সমাবেশ} $(p+1)(q+1)(r+1)-1$

\sub{ii} \B{১ম প্রকারের} $p$ \B{সংখ্যক ২য় প্রকারের} $q$ \B{সংখ্যক ও} $r$ \B{সংখ্যক ভিন্ন ভিন্ন জিনিসের সমাবেশ} $(p+1)(q+1)2^r-1$

\sub{iii} $n$ \B{সংখ্যক জিনিস থেকে প্রত্যেক বার অন্তত একটি জিনিস নিয়ে গঠিত সমাবেশ} $2^n-1$

\itm{4} $p_1+p_2+\cdots+p_n$ \B{সংখ্যক জিনিসকে} $n$ \B{সংখ্যক ভাগে বিভক্ত করার সমাবেশ যেন ভাগগুলিতে যথাক্রমে} $p_1,p_2,\ldots,p_n$ \B{জিনিস থাকে,}

$\dfrac{(p_1+p_2+\cdots+p_n)!}{p_1!\,p_2!\cdots p_n!}$

\chsec{অধ্যায়-৬: ত্রিকোণমিতিক অনুপাত}

\itm{1} $1^\circ=\dfrac{\pi}{180}$ \B{রেডিয়ান; 1 রেডিয়ান} $=\dfrac{180^\circ}{\pi}$

\itm{2} \sub{i} \B{বৃত্তচাপের দৈর্ঘ্য,} $s=r\theta$ \B{একক; যেখানে,} $r$ \B{ব্যাসার্ধ ও} $\theta$ \B{রেডিয়ান কোণ}

\sub{ii} \B{বৃত্তকলার ক্ষেত্রফল} $A=\dfrac{1}{2}r^2\theta$ \B{বর্গ একক}

\chsec{অধ্যায়-৭: সংযুক্ত কোণের ত্রিকোণমিতিক অনুপাত}

\itm{1} \sub{i} $\sin(A\pm B)=\sin A\cos B\pm\cos A\sin B$

\sub{ii} $\cos(A\pm B)=\cos A\cos B\mp\sin A\sin B$

\itm{2} \sub{i} $\tan(A\pm B)=\dfrac{\tan A\pm\tan B}{1\mp\tan A\tan B}$

\sub{ii} $\cot(A\pm B)=\dfrac{\cot A\cot B\mp1}{\cot B\pm\cot A}$

\itm{3} \sub{i} $2\sin A\cos B=\sin(A+B)+\sin(A-B)$

\sub{ii} $2\cos A\sin B=\sin(A+B)-\sin(A-B)$

\sub{iii} $2\cos A\cos B=\cos(A+B)+\cos(A-B)$

\sub{iv} $2\sin A\sin B=\cos(A-B)-\cos(A+B)$

\itm{4} \sub{i} $\sin(A+B)\sin(A-B)=\sin^2\!A-\sin^2\!B=\cos^2\!B-\cos^2\!A$

\sub{ii} $\cos(A+B)\cos(A-B)=\cos^2\!A-\sin^2\!B=\cos^2\!B-\sin^2\!A$

\itm{5} \sub{i} $\sin C+\sin D=2\sin\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$

\sub{ii} $\sin C-\sin D=2\cos\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$

\sub{iii} $\cos C+\cos D=2\cos\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$

\sub{iv} $\cos C-\cos D=2\sin\dfrac{C+D}{2}\sin\dfrac{D-C}{2}$

\itm{6} \sub{i} $\sin2A=2\sin A\cos A=\dfrac{2\tan A}{1+\tan^2\!A}$

\sub{ii} $\cos2A=\cos^2\!A-\sin^2\!A=1-2\sin^2\!A=2\cos^2\!A-1=\dfrac{1-\tan^2\!A}{1+\tan^2\!A}$

\sub{iii} $\tan2A=\dfrac{2\tan A}{1-\tan^2\!A}$

\sub{iv} $1-\cos2A=2\sin^2\!A$

\sub{v} $1+\cos2A=2\cos^2\!A$

\itm{7} \sub{i} $\sin3A=3\sin A-4\sin^3\!A$

\sub{ii} $\cos3A=4\cos^3\!A-3\cos A$

\sub{iii} $\tan3A=\dfrac{3\tan A-\tan^3\!A}{1-3\tan^2\!A}$

\itm{8} $\dfrac{a}{\sin A}=\dfrac{b}{\sin B}=\dfrac{c}{\sin C}=2R$\B{; যেখানে,} $R$ \B{হলো পরিবৃত্তের ব্যাসার্ধ।}

\itm{9} \B{যেকোনো ত্রিভুজের ক্ষেত্রে:}

$\cos A=\dfrac{b^2+c^2-a^2}{2bc}$,\; $\cos B=\dfrac{c^2+a^2-b^2}{2ca}$,\; $\cos C=\dfrac{a^2+b^2-c^2}{2ab}$

\itm{10} \B{যেকোনো ত্রিভুজের ক্ষেত্রে:}

$a=b\cos C+c\cos B,\; b=c\cos A+a\cos C,\; c=a\cos B+b\cos A$

\itm{11} \B{ত্রিভুজের ক্ষেত্রফল:}

$\Delta=\dfrac{1}{2}bc\sin A=\dfrac{1}{2}ca\sin B=\dfrac{1}{2}ab\sin C=\sqrt{s(s-a)(s-b)(s-c)}$\B{; যেখানে} $s=\dfrac{a+b+c}{2}=$ \B{অর্ধপরিসীমা।}

\chsec{অধ্যায়-৯: অন্তরীকরণ}

\itm{1} \B{কোনো ফাংশনের বিপরীত ফাংশন পাওয়া যাবে যদি এবং কেবল যদি ফাংশনটি এক-এক ও সার্বিক হয়।}

\itm{2} $\displaystyle\lim_{x\to a}[f(x)g(x)]=\lim_{x\to a}f(x)\times\lim_{x\to a}g(x)$\B{;}

$\displaystyle\lim_{x\to a}\frac{f(x)}{g(x)}=\frac{\displaystyle\lim_{x\to a}f(x)}{\displaystyle\lim_{x\to a}g(x)}$

\itm{3}

$\displaystyle\lim_{\theta\to0}\frac{\sin\theta}{\theta}=1$\B{;}
$\displaystyle\lim_{\theta\to0}\frac{\theta}{\sin\theta}=1$\B{;}
$\displaystyle\lim_{\theta\to0}\frac{\tan\theta}{\theta}=1$\B{;}
$\displaystyle\lim_{\theta\to0}\frac{\theta}{\tan\theta}=1$\B{;}
$\displaystyle\lim_{x\to0}\frac{\sin^{-1}x}{x}=1$\B{;}
$\displaystyle\lim_{x\to0}\frac{\tan^{-1}x}{x}=1$\B{;}
$\displaystyle\lim_{x\to0}\frac{e^x-1}{x}=1$\B{;}
$\displaystyle\lim_{x\to0}\frac{\ln(1+x)}{x}=1$\B{;}
$\displaystyle\lim_{x\to0}(1+x)^{\frac{1}{x}}=e$\B{;}
$\displaystyle\lim_{x\to\infty}\!\left(1+\frac{1}{x}\right)^{\!x}=e$\B{;}
$\displaystyle\lim_{x\to0}\frac{(1+x)^n-1}{x}=n$

\itm{4} $\displaystyle\lim_{x\to a}\frac{x^n-a^n}{x-a}=na^{n-1}$

\itm{5} \sub{i} $f'(x)$ \B{বা} $\dfrac{d}{dx}\{f(x)\}=\displaystyle\lim_{h\to0}\dfrac{f(x+h)-f(x)}{h}$

\sub{ii} $\dfrac{d}{dx}(c)=0$ \B{[যখন,} $c$ \B{ধ্রুবক]}

\sub{iii} $\dfrac{d}{dx}\{cf(x)\}=c\dfrac{d}{dx}\{f(x)\}$ \B{[যখন,} $c$ \B{ধ্রুবক]}

\sub{iv} $\dfrac{d}{dx}(uv)=v\dfrac{du}{dx}+u\dfrac{dv}{dx}$

\sub{v} $\dfrac{d}{dx}\!\left(\dfrac{u}{v}\right)=\dfrac{v\dfrac{du}{dx}-u\dfrac{dv}{dx}}{v^2}$

\B{[$u,v$ উভয়ই $x$-এর ফাংশন]}

\sub{vi} $y=f(z)$ \B{এবং} $z=f(x)$ \B{হলে,} $\dfrac{dy}{dx}=\dfrac{dy}{dz}\times\dfrac{dz}{dx}$

\itm{6}

\sub{i} $\dfrac{d}{dx}(x^n)=nx^{n-1}$

\sub{ii} $\dfrac{d}{dx}(e^x)=e^x$

\sub{iii} $\dfrac{d}{dx}(\sin x)=\cos x$

\sub{iv} $\dfrac{d}{dx}(\cos x)=-\sin x$

\sub{v} $\dfrac{d}{dx}(\tan x)=\sec^2 x$

\sub{vi} $\dfrac{d}{dx}(\cot x)=-\csc^2 x$

\sub{vii} $\dfrac{d}{dx}(\sec x)=\sec x\tan x$

\sub{viii} $\dfrac{d}{dx}(\csc x)=-\csc x\cot x$

\sub{ix} $\dfrac{d}{dx}(\ln x)=\dfrac{1}{x}$

\sub{x} $\dfrac{d}{dx}(a^x)=a^x\ln a$

\sub{xi} $\dfrac{d}{dx}(\log_a x)=\dfrac{1}{x}\log_a e$

\sub{xii} $\dfrac{d}{dx}(\sqrt{x})=\dfrac{1}{2\sqrt{x}}$

\sub{xiii} $\dfrac{d}{dx}(\sin^{-1}x)=\dfrac{1}{\sqrt{1-x^2}}$

\sub{xiv} $\dfrac{d}{dx}(\cos^{-1}x)=\dfrac{-1}{\sqrt{1-x^2}}$

\sub{xv} $\dfrac{d}{dx}(\tan^{-1}x)=\dfrac{1}{1+x^2}$

\sub{xvi} $\dfrac{d}{dx}(\cot^{-1}x)=\dfrac{-1}{1+x^2}$

\sub{xvii} $\dfrac{d}{dx}(\sec^{-1}x)=\dfrac{1}{x\sqrt{x^2-1}}$

\sub{xviii} $\dfrac{d}{dx}(\csc^{-1}x)=\dfrac{-1}{x\sqrt{x^2-1}}$

\medskip

\noindent\small\B{বিপরীত ত্রিকোণমিতিক ফাংশনের অন্তরীকরণ করার জন্য নিম্নলিখিত সূত্রগুলো প্রয়োজন যা দ্বিতীয় পত্রে বিস্তারিত আলোচনা করা হয়েছে।}\normalsize

\itm{7} \sub{a}

\sub{i} $\sin(\sin^{-1}x)=x$\B{;}

\sub{ii} $\cos(\cos^{-1}x)=x$\B{;}

\sub{iii} $\tan(\tan^{-1}x)=x$

\sub{b}

\sub{i} $\sin^{-1}x=\csc^{-1}\!\left(\dfrac{1}{x}\right)$\B{;}

\sub{ii} $\cot^{-1}x=\tan^{-1}\!\left(\dfrac{1}{x}\right)$ \B{ইত্যাদি।}

\sub{iv} $\sin^{-1}(\sin x)=x$\B{;} \sub{v} $\cos^{-1}(\cos x)=x$

\sub{c}

\sub{i} $2\tan^{-1}x=\tan^{-1}\!\dfrac{2x}{1-x^2}=\sin^{-1}\!\dfrac{2x}{1+x^2}=\cos^{-1}\!\dfrac{1-x^2}{1+x^2}$

\sub{ii} $\tan^{-1}x\pm\tan^{-1}y=\tan^{-1}\!\dfrac{x\pm y}{1\mp xy}$

\itm{8} \B{ম্যাকলরিনের ধারা,}

$f(x)=f(0)+xf'(0)+\dfrac{x^2}{2!}f''(0)+\dfrac{x^3}{3!}f'''(0)+\cdots+\dfrac{x^n}{n!}f^{(n)}(0)+\cdots$

\itm{9} $y=f(x)$ \B{বক্ররেখার} $(x_1,y_1)$ \B{বিন্দুতে স্পর্শকের সমীকরণ,}

$y-y_1=\dfrac{dy}{dx}(x-x_1)$\B{; যেখানে, ঢাল} $=\dfrac{dy}{dx}$

\itm{10} $y=f(x)$ \B{বক্ররেখার} $(x_1,y_1)$ \B{বিন্দুতে অভিলম্বের সমীকরণ,}

$(x-x_1)+\dfrac{dy}{dx}(y-y_1)=0$\B{; যেখানে, ঢাল} $=-\dfrac{1}{\,dy/dx\,}$

\itm{11} $y=f(x)$ \B{বক্ররেখার স্পর্শক}

\sub{i} $y$\B{-অক্ষের সমান্তরাল অথবা} $x$\B{-অক্ষের উপর লম্ব হলে,} $\dfrac{dx}{dy}=0$

\sub{ii} $x$\B{-অক্ষের সমান্তরাল অথবা} $y$\B{-অক্ষের উপর লম্ব হলে,} $\dfrac{dy}{dx}=0$

\sub{iii} \B{স্পর্শক} $x$\B{-অক্ষের সাথে} $45^\circ$ \B{কোণ উৎপন্ন করলে,} $\dfrac{dy}{dx}=1$

\sub{iv} \B{স্পর্শক উভয় অক্ষের সাথে সমান কোণ উৎপন্ন করলে,} $\dfrac{dy}{dx}=\pm1$

\itm{12} $x=c$ \B{বিন্দুতে ফাংশনটির সর্বোচ্চ মান অথবা সর্বনিম্ন মান এবং} $f'(c)$ \B{এর অস্তিত্ব থাকলে} $f'(c)=0$ \B{হবে।}

\sub{i} $f''(c)<0$ \B{হলে,} $x=c$ \B{বিন্দুতে} $f(x)$ \B{ফাংশনের সর্বোচ্চ মান বিদ্যমান।}

\sub{ii} $f''(c)>0$ \B{হলে,} $x=c$ \B{বিন্দুতে} $f(x)$ \B{ফাংশনের সর্বনিম্ন মান বিদ্যমান।}

\itm{13} \B{যদি} $x=c$ \B{বিন্দুতে} $f'(x)$ \B{ফাংশনের মান শূন্য না হয়, অর্থাৎ} $f'(c)\neq0$ \B{অথবা} $f''(x)=0$ \B{হয়, তবে} $f(x)$ \B{ফাংশনটির সর্বোচ্চ মান বা সর্বনিম্ন মান নেই।}

\itm{14} \B{তিনটি ফাংশনের গুণনফলের অন্তরক,}

$\dfrac{d}{dx}(uvw)=vw\dfrac{du}{dx}+uw\dfrac{dv}{dx}+uv\dfrac{dw}{dx}$

\itm{15} \B{যদি} $f(x,y)=0$ \B{হয় অর্থাৎ অব্যক্ত ফাংশন তাহলে,}

$\dfrac{dy}{dx}=-\dfrac{f_x}{f_y}=-\dfrac{y\text{\B{ এর সাপেক্ষে }} x\text{\B{ এর অন্তরীকরণ}}}{x\text{\B{ ধ্রুবরেখে }} y\text{\B{ এর সাপেক্ষে অন্তরীকরণ}}}$

\itm{16} $\dfrac{d}{dx}(u^v)=u^v\!\left[v\cdot\dfrac{d}{dx}(\ln u)+\ln u\cdot\dfrac{dv}{dx}\right]$

\itm{17} \B{বেগ,} $v=\dfrac{ds}{dt}$\B{; ত্বরণ,} $a=\dfrac{dv}{dt}=\dfrac{d^2s}{dt^2}$

\chsec{অধ্যায়-১০: যোগজীকরণ}

\itm{1}

\sub{i} $\int\!\{f(x)\pm\varphi(x)\}\,dx=\int\!f(x)\,dx\pm\int\!\varphi(x)\,dx$

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

\itm{2}

\sub{i} $\displaystyle\int\!\frac{dx}{x^2+a^2}=\frac{1}{a}\tan^{-1}\!\frac{x}{a}+c$

\sub{ii} $\displaystyle\int\!\frac{dx}{\sqrt{a^2-x^2}}=\sin^{-1}\!\frac{x}{a}+c$

\sub{iii} $\displaystyle\int\!\frac{dx}{x^2-a^2}=\frac{1}{2a}\ln\!\left|\frac{x-a}{x+a}\right|+c$

\sub{iv} $\displaystyle\int\!\frac{dx}{a^2-x^2}=\frac{1}{2a}\ln\!\left|\frac{a+x}{a-x}\right|+c$

\sub{v} $\displaystyle\int\!\frac{dx}{\sqrt{x^2-a^2}}=\ln\!\left|x+\sqrt{x^2-a^2}\right|+c$

\sub{vi} $\displaystyle\int\!\frac{dx}{\sqrt{x^2+a^2}}=\ln\!\left|x+\sqrt{x^2+a^2}\right|+c$

\sub{vii} $\displaystyle\int\!\sqrt{a^2-x^2}\,dx=\frac{x\sqrt{a^2-x^2}}{2}+\frac{a^2}{2}\sin^{-1}\!\frac{x}{a}+c$

\itm{3} \sub{i} $\displaystyle\int\!uv\,dx=u\int\!v\,dx-\int\!\left\{\frac{du}{dx}\int\!v\,dx\right\}dx$

\sub{ii} $\int\!e^x\{f(x)+f'(x)\}\,dx=e^x f(x)+c$\B{ এবং} $\int\!e^{ax}\{af(x)+f'(x)\}\,dx=e^{ax}f(x)+c$

\sub{iii} $\displaystyle\int\!\tan x\,dx=-\ln|\cos x|+c=\ln|\sec x|+c$

\sub{iv} $\displaystyle\int\!\ln x\,dx=x\ln x-x+c$

\itm{4} \B{প্রতিস্থাপন কৌশল:}

\sub{i} \B{যদি কোনো যোগজ} $\displaystyle\int\!\frac{a+bx^l}{p+qx^n}\,dx$ \B{আকারে থাকে, যেখানে} $l$ \B{ও} $m$ \B{উভয়ে ভগ্নাংশ এবং তাদের হরের ল.সা.গু} $n$ \B{হয়, তবে} $x=z^n$ \B{ধরতে হয়।}

\sub{ii} $\displaystyle\int\!\frac{dx}{x(a+bx^n)}$ \B{আকারের যোগজের জন্য,} $x^n=\dfrac{1}{z}$ \B{ধরতে হয়।}

\sub{iii} $\displaystyle\int\!\frac{dx}{x\sqrt{a+bx^n}}$ \B{আকারের যোগজের জন্য,} $x^n=\dfrac{1}{z}$ \B{ধরতে হয়।}

\sub{iv} $\displaystyle\int\!\frac{dx}{x^m(a+bx)^n}$ \B{আকারের যোগজের জন্য,} $a+bx=zx$ \B{ধরতে হয়।}

\sub{v} $\displaystyle\int\!\frac{dx}{(x-a)^m(x-b)^n}$ \B{আকারের যোগজের জন্য,} $z=\dfrac{x-b}{x-a}$ \B{ধরতে হয়।}

\itm{5}

\sub{i} $\displaystyle\int_a^b\!f'(x)\,dx=\bigl[f(x)\bigr]_a^b=f(b)-f(a)$

\sub{ii} $\displaystyle\int_a^b\!f(x)\,dx=-\int_b^a\!f(x)\,dx$

\sub{iii} $\displaystyle\int_0^a\!f(x)\,dx=\int_0^a\!f(a-x)\,dx$

\sub{iv} $\displaystyle\int_a^b\!f(x)\,dx=\int_a^b\!f(a+b-x)\,dx$

\vspace{4pt}
\noindent\colorbox{black}{\parbox{\dimexpr\linewidth\relax}{\centering\bfseries\large\color{white}{\bn দ্বিতীয় পত্র}}}
\vspace{2pt}\par

\chsec{অধ্যায়-১: বাস্তব সংখ্যা ও অসমতা}

\itm{1} \B{সকল} $a, b \in \mathbb{R}$ \B{এর জন্য,}

\sub{i} $|a|\geq a$ \quad
\sub{ii} $|a|^2=|-a|^2=a^2$

\sub{iii} $|ab|=|a||b|$ \quad
\sub{iv} $|a+b|\leq|a|+|b|$

\sub{v} $|a-b|\leq|a|+|b|$ \quad
\sub{vi} $|a-b|\geq\bigl||a|-|b|\bigr|$

\sub{vii} $|ab|\geq ab$ \quad
\sub{viii} $\left|\dfrac{a}{b}\right|=\dfrac{|a|}{|b|}$

\itm{2} $|x|=\begin{cases}x, & \B{যখন } x>0\\0, & \B{যখন } x=0\\-x, & \B{যখন } x<0\end{cases}$

\chsec{অধ্যায়-৩: জটিল সংখ্যা}

\itm{1} \B{জটিল সংখ্যা,} $z=x+iy$ \B{এর ক্ষেত্রে, মডুলাস,} $r=\sqrt{x^2+y^2}$\B{, আর্গুমেন্ট,} $\theta=\tan^{-1}\!\left(\dfrac{y}{x}\right)$

\itm{2} \B{যদি} $a+ib=x+iy$ \B{হয়, তবে} $a=x,\,b=y$\B{; যেখানে} $i=\sqrt{-1}$\B{, সুতরাং} $i^2=-1,\,i^3=-i$ \B{এবং} $i^4=1$

\itm{3} \B{একেকের জটিল ঘনমূল দুইটির একটি} $\omega$ \B{হলে, অপরটি} $\omega^2$

\B{এবং} $\omega^3=1,\;1+\omega+\omega^2=0$\B{;} $\omega=\dfrac{1}{2}(-1+\sqrt{3}),\;\omega^2=\dfrac{1}{2}(-1-\sqrt{3})$

\chsec{অধ্যায়-৪: বহুপদী ও বহুপদী সমীকরণ}

\itm{1} \B{দ্বিঘাত সমীকরণ,} $ax^2+bx+c=0$ \B{(যেখানে,} $a\neq0$\B{) এর ক্ষেত্রে,}

\sub{i} \B{মূলদ্বয়} $\alpha,\beta$ \B{হলে,} $\alpha+\beta=-\dfrac{b}{a}$ \B{এবং} $\alpha\beta=\dfrac{c}{a}$

\sub{ii} \B{উপরি-উক্ত সমীকরণের সমাধান,} $x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}$

\sub{iii} \B{দ্বিঘাত সমীকরণের নিষ্কায়ক} $=b^2-4ac$ \B{যেখানে,}

$b^2-4ac=0$ \B{হলে, মূলদ্বয় বাস্তব ও সমান;}\quad $b^2-4ac>0$ \B{হলে, মূলদ্বয় বাস্তব ও অসমান।}

$b^2-4ac<0$ \B{হলে, মূলদ্বয় জটিল ও অসমান;}\quad $b^2-4ac>0$ \B{এবং পূর্ণবর্গ সংখ্যা হলে, মূলদ্বয় মূলদ ও অসমান।}

$b^2-4ac>0$ \B{এবং পূর্ণবর্গ সংখ্যা না হয়, তবে মূলদ্বয় অমূলদ ও অসমান।}

\itm{2} \B{ত্রিঘাত সমীকরণ,} $ax^3+bx^2+cx+d=0$ \B{(যেখানে,} $a\neq0$\B{) এর ক্ষেত্রে}

\sub{i} \B{মূলত্রয়,} $\alpha,\beta,\gamma$ \B{হলে,} $\Sigma\alpha=\alpha+\beta+\gamma=-\dfrac{b}{a}$\B{,} $\Sigma\alpha\beta=\alpha\beta+\alpha\gamma+\beta\gamma=\dfrac{c}{a}$ \B{এবং} $\alpha\beta\gamma=-\dfrac{d}{a}$

\sub{ii} \B{মূলত্রয় সমান্তর প্রগমনে থাকলে তাদের সাধারণ আকার,} $\alpha-\beta,\;\alpha,\;\alpha+\beta$

\sub{iii} \B{মূলত্রয় গুণোত্তর প্রগমনে থাকলে তাদের সাধারণ আকার,} $\dfrac{\alpha}{r},\;\alpha,\;\alpha r$

\sub{iv} \B{মূলত্রয় ভাজিত }\textnormal{(Harmonic)}\B{ প্রগমনে থাকলে তাদের সাধারণ আকার,} $\dfrac{1}{\alpha-\beta},\;\dfrac{1}{\alpha},\;\dfrac{1}{\alpha+\beta}$

\itm{3} \sub{i} $\alpha,\beta$ \B{মূলদ্বয় বিশিষ্ট দ্বিঘাত সমীকরণ} $x^2-(\alpha+\beta)x+\alpha\beta=0$

\sub{ii} \B{ত্রিঘাত সমীকরণের মূলত্রয়} $\alpha,\beta$ \B{ও} $\gamma$ \B{হলে, সমীকরণ}

$x^3-(\alpha+\beta+\gamma)x^2+(\alpha\beta+\beta\gamma+\gamma\alpha)x-\alpha\beta\gamma=0$

\chsec{অধ্যায়-৫: দ্বিপদী বিস্তৃতি}

\itm{1} \sub{i} $(a+x)^n=a^n+{}^nC_1 a^{n-1}x+{}^nC_2 a^{n-2}x^2+\cdots+{}^nC_r a^{n-r}x^r+\cdots+x^n$\B{; যেখানে,} $n\in\mathbb{N}$

\sub{ii} $(a+x)^n$ \B{এর বিস্তৃতির সাধারণ পদ অর্থাৎ} $(r+1)$ \B{তম পদ,} $T_{r+1}={}^nC_r a^{n-r}x^r$

\itm{2} \sub{i} $n$ \B{ঋণাত্মক পূর্ণসংখ্যা অথবা ভগ্নাংশ এবং} $|x|<1$ \B{হলে,}

$(1+x)^n=1+nx+\dfrac{n(n-1)}{2!}x^2+\dfrac{n(n-1)(n-2)}{3!}x^3+\cdots+\dfrac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r+\cdots$

\sub{ii} $(1+x)^n$ \B{এর বিস্তৃতির সাধারণ পদ অর্থাৎ} $(r+1)$ \B{তম পদ,} $T_{r+1}=\dfrac{n(n-1)(n-2)\cdots(n-r+1)}{r!}x^r$

\sub{iii} $(ax^p+bx^q)^n$ \B{এর বিস্তৃতিতে} $(r+1)$ \B{তম পদে} $x^m$ \B{সম্বলিত হলে,} $r=\dfrac{np-m}{p-q}$ \B{এবং} $x^m$ \B{এর সহগ} $={}^nC_r a^{n-r}b^r$\B{; যেখানে,} $m,n\in\mathbb{N}$

\sub{iv} $(a+x)^n$ \B{এর বিস্তৃতিতে,}

\sub{a} $n$ \B{জোড় সংখ্যা হলে, মধ্যপদ একটি এবং তা} $\left(\dfrac{n}{2}+1\right)$ \B{তম পদ।}

\sub{b} $n$ \B{বিজোড় সংখ্যা হলে, মধ্যপদ দুইটি এবং তা} $\left(\dfrac{n-1}{2}+1\right)$ \B{এবং} $\left(\dfrac{n+1}{2}+1\right)$ \B{তম পদদ্বয়।}

\itm{3} $|x|<1$ \B{হলে,}

\sub{i} $(1-x)^{-1}=1+x+x^2+x^3+\cdots+x^r+\cdots$

\sub{ii} $(1+x)^{-1}=1-x+x^2-x^3+\cdots+(-1)^rx^r+\cdots$

\sub{iii} $(1-x)^{-2}=1+2x+3x^2+4x^3+\cdots+(r+1)x^r+\cdots$

\sub{iv} $(1+x)^{-2}=1-2x+3x^2-4x^3+\cdots+(-1)^r(r+1)x^r+\cdots$

\sub{v} $(1-x)^{-3}=1+3x+6x^2+10x^3+\cdots+\dfrac{1}{2}(r+1)(r+2)x^r+\cdots$

\sub{vi} $(1+x)^{-3}=1-3x+6x^2-10x^3+\cdots+(-1)^r\dfrac{1}{2}(r+1)(r+2)x^r+\cdots$

\itm{4} \B{যদি} $\displaystyle\lim_{n\to\infty}\dfrac{U_{n+1}}{U_n}<1$ \B{হয়, তাহলে ধারাটি অভিসৃত }\textnormal{(Convergent)}\B{ হবে।}

\chsec{অধ্যায়-৬: কণিক}

\itm{1} \B{পরাবৃত্তের সমীকরণ} $y^2=4ax$ \B{হলে,}

\sub{i} \B{শীর্ষবিন্দুর স্থানাঙ্ক} $(0,0)$
\sub{ii} \B{উপকেন্দ্রের স্থানাঙ্ক} $(a,0)$
\sub{iii} \B{নিয়ামক রেখার সমীকরণ,} $x=-a$
\sub{iv} \B{অক্ষরেখার সমীকরণ,} $y=0$
\sub{v} \B{উপকেন্দ্রিক লম্বের দৈর্ঘ্য} $=4a$
\sub{vi} \B{উপকেন্দ্রিক লম্বের সমীকরণ,} $x=a$
\sub{vii} \B{উপকেন্দ্রিক দূরত্ব} $=a+x$

\sub{viii} $(\alpha,\beta)$ \B{উপকেন্দ্র এবং} $ax+by+c=0$ \B{নিয়ামক বিশিষ্ট পরাবৃত্তের সমীকরণ,}

$(x-\alpha)^2+(y-\beta)^2=\dfrac{(ax+by+c)^2}{a^2+b^2}$

\sub{ix} $y=mx+c$ \B{রেখাটি} $y^2=4ax$ \B{পরাবৃত্তকে স্পর্শ করবে যদি,} $c=\dfrac{a}{m}$ \B{হয় এবং স্পর্শ বিন্দু} $\left(\dfrac{a}{m^2},\dfrac{2a}{m}\right)$

\sub{x} $y^2=4ax$ \B{পরাবৃত্তের} $(x_1,y_1)$ \B{বিন্দুতে স্পর্শকের সমীকরণ,} $yy_1=2a(x+x_1)$

\sub{xi} $x^2=4ay$ \B{পরাবৃত্তের} $(x_1,y_1)$ \B{বিন্দুতে স্পর্শকের সমীকরণ,} $xx_1=2a(y+y_1)$

\itm{2} \B{উপবৃত্তের সমীকরণ} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$\B{;} $a>b$ \B{হলে,}

\sub{i} \B{উপবৃত্তের কেন্দ্রের স্থানাঙ্ক} $(0,0)$
\sub{ii} \B{বৃহৎ অক্ষের দৈর্ঘ্য} $=2a$
\sub{iii} \B{ক্ষুদ্র অক্ষের দৈর্ঘ্য} $=2b$
\sub{iv} \B{উপকেন্দ্রের স্থানাঙ্ক} $(\pm ae,0)$
\sub{v} \B{বৃহৎ অক্ষের সমীকরণ} $y=0$
\sub{vi} \B{ক্ষুদ্র অক্ষের সমীকরণ,} $x=0$
\sub{vii} \B{নিয়ামক রেখার সমীকরণ,} $x=\pm\dfrac{a}{e}$
\sub{viii} \B{উৎকেন্দ্রিকতা,} $e=\sqrt{\dfrac{a^2-b^2}{a^2}}$
\sub{ix} \B{উপকেন্দ্রিক লম্ব} $=\dfrac{2b^2}{a}$
\sub{x} \B{উপকেন্দ্রিক লম্বের সমীকরণ,} $x=\pm ae$
\sub{xi} \B{উপকেন্দ্রদ্বয়ের দূরত্ব} $=2ae$
\sub{xii} \B{নিয়ামক রেখাদ্বয়ের দূরত্ব} $=\dfrac{2a}{e}$

\sub{xiii} $(\alpha,\beta)$ \B{উপকেন্দ্র এবং} $ax+by+c=0$ \B{নিয়ামক বিশিষ্ট উপবৃত্তের সমীকরণ,}

$(x-\alpha)^2+(y-\beta)^2=e^2\!\left(\dfrac{(ax+by+c)^2}{a^2+b^2}\right)$\B{; যেখানে,} $e=$ \B{উৎকেন্দ্রিকতা।}

\sub{xiv} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{উপবৃত্তের} $(x_1,y_1)$ \B{বিন্দুতে স্পর্শকের সমীকরণ,} $\dfrac{xx_1}{a^2}+\dfrac{yy_1}{b^2}=1$

\sub{xv} $y=mx+c$ \B{রেখাটি} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{উপবৃত্তকে স্পর্শ করবে যদি} $c=\pm\sqrt{a^2m^2+b^2}$ \B{হয়}

\B{এবং স্পর্শবিন্দু} $\left(\pm\dfrac{a^2m}{\sqrt{a^2m^2+b^2}},\;\pm\dfrac{b^2}{\sqrt{a^2m^2+b^2}}\right)$

\sub{xvi} $\dfrac{x^2}{a^2}+\dfrac{y^2}{b^2}=1$ \B{উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল} $=\pi ab$ \B{বর্গ একক।}

\itm{3} \B{অধিবৃত্তের সমীকরণ} $\dfrac{x^2}{a^2}-\dfrac{y^2}{b^2}=1$ \B{হলে,}

\sub{i} \B{কেন্দ্রের স্থানাঙ্ক} $(0,0)$
\sub{ii} \B{উপকেন্দ্র দুইটির স্থানাঙ্ক} $(\pm ae,0)$
\sub{iii} \B{শীর্ষবিন্দুর স্থানাঙ্ক} $(\pm a,0)$
\sub{iv} \B{আড় অক্ষের সমীকরণ,} $y=0$
\sub{v} \B{অনুবন্ধী অক্ষের সমীকরণ,} $x=0$
\sub{vi} \B{নিয়ামক রেখার সমীকরণ,} $x=\pm\dfrac{a}{e}$
\sub{vii} \B{উৎকেন্দ্রিকতা} $e=\sqrt{\dfrac{a^2+b^2}{a^2}}$
\sub{viii} \B{উপকেন্দ্রিক লম্ব} $=\dfrac{2b^2}{a}$
\sub{ix} \B{অক্ষ দুইটির দৈর্ঘ্য} $2a$ \B{ও} $2b$
\sub{x} \B{উপকেন্দ্রদ্বয়ের দূরত্ব} $=2ae$
\sub{xi} \B{নিয়ামক রেখাদ্বয়ের দূরত্ব} $=\dfrac{2a}{e}$
\sub{xii} \B{অসীমতটের সমীকরণ,} $y=\pm\dfrac{b}{a}x$

\chsec{অধ্যায়-৭: বিপরীত ত্রিকোণমিতিক ফাংশন ও ত্রিকোণমিতিক সমীকরণ}

\itm{1} \sub{i} $\sin(A+B)=\sin A\cos B+\cos A\sin B$
\sub{ii} $\sin(A-B)=\sin A\cos B-\cos A\sin B$
\sub{iii} $\cos(A+B)=\cos A\cos B-\sin A\sin B$
\sub{iv} $\cos(A-B)=\cos A\cos B+\sin A\sin B$
\sub{v} $\tan(A+B)=\dfrac{\tan A+\tan B}{1-\tan A\tan B}$
\sub{vi} $\tan(A-B)=\dfrac{\tan A-\tan B}{1+\tan A\tan B}$
\sub{vii} $\cot(A+B)=\dfrac{\cot A\cot B-1}{\cot B+\cot A}$
\sub{viii} $\cot(A-B)=\dfrac{\cot A\cot B+1}{\cot B-\cot A}$

\itm{2} \sub{i} $2\sin A\cos B=\sin(A+B)+\sin(A-B)$
\sub{ii} $2\cos A\sin B=\sin(A+B)-\sin(A-B)$
\sub{iii} $2\cos A\cos B=\cos(A+B)+\cos(A-B)$
\sub{iv} $2\sin A\sin B=\cos(A-B)-\cos(A+B)$

\itm{3} \sub{i} $\sin C+\sin D=2\sin\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{ii} $\sin C-\sin D=2\cos\dfrac{C+D}{2}\sin\dfrac{C-D}{2}$
\sub{iii} $\cos C+\cos D=2\cos\dfrac{C+D}{2}\cos\dfrac{C-D}{2}$
\sub{iv} $\cos C-\cos D=2\sin\dfrac{C+D}{2}\sin\dfrac{D-C}{2}$

\itm{4} \sub{i} $\sin 2A=2\sin A\cos A=\dfrac{2\tan A}{1+\tan^2\!A}$
\sub{ii} $\tan 2A=\dfrac{2\tan A}{1-\tan^2\!A}$
\sub{iii} $\cos 2A=\cos^2\!A-\sin^2\!A=1-2\sin^2\!A=2\cos^2\!A-1=\dfrac{1-\tan^2\!A}{1+\tan^2\!A}$
\sub{iv} $\sin 3A=3\sin A-4\sin^3\!A$
\sub{v} $\cos 3A=4\cos^3\!A-3\cos A$
\sub{vi} $\tan 3A=\dfrac{3\tan A-\tan^3\!A}{1-3\tan^2\!A}$

\itm{5} \sub{i} $\sin\theta=0$ \B{বা} $\tan\theta=0$ \B{হলে,} $\theta=n\pi$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{ii} $\cos\theta=0$ \B{বা} $\cot\theta=0$ \B{হলে,} $\theta=(2n+1)\dfrac{\pi}{2}$\B{, যেখানে,} $n\in\mathbb{Z}$

\sub{iii} $\sin\theta=1$ \B{হলে,} $\theta=(4n+1)\dfrac{\pi}{2}$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{iv} $\cos\theta=1$ \B{হলে,} $\theta=2n\pi$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{v} $\sin\theta=-1$ \B{হলে,} $\theta=(4n-1)\dfrac{\pi}{2}$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{vi} $\cos\theta=-1$ \B{হলে,} $\theta=(2n+1)\pi$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{vii} $\sin\theta=\sin\alpha$ \B{হলে,} $\theta=n\pi+(-1)^n\alpha$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{viii} $\cos\theta=\cos\alpha$ \B{হলে,} $\theta=2n\pi\pm\alpha$\B{; যেখানে,} $n\in\mathbb{Z}$

\sub{ix} $\tan\theta=\tan\alpha$ \B{হলে,} $\theta=n\pi+\alpha$\B{; যেখানে,} $n\in\mathbb{Z}$

\itm{6} $\sin^{-1}x=\csc^{-1}\!\dfrac{1}{x}=\cos^{-1}\!\sqrt{1-x^2}=\sec^{-1}\!\dfrac{1}{\sqrt{1-x^2}}=\cot^{-1}\!\dfrac{\sqrt{1-x^2}}{x}=\tan^{-1}\!\dfrac{x}{\sqrt{1-x^2}}$

\itm{7} \sub{i} $\sin^{-1}x+\cos^{-1}x=\dfrac{\pi}{2}$\B{;}
\sub{ii} $\tan^{-1}x+\cot^{-1}x=\dfrac{\pi}{2}$\B{;}
\sub{iii} $\csc^{-1}x+\sec^{-1}x=\dfrac{\pi}{2}$

\itm{8} \sub{i} $\tan^{-1}x+\tan^{-1}y=\tan^{-1}\!\dfrac{x+y}{1-xy}$

\sub{ii} $\tan^{-1}x-\tan^{-1}y=\tan^{-1}\!\dfrac{x-y}{1+xy}$

\sub{iii} $\tan^{-1}x+\tan^{-1}y+\tan^{-1}z=\tan^{-1}\!\dfrac{x+y+z-xyz}{1-yz-zx-xy}$

\sub{iv} $\sin^{-1}x+\sin^{-1}y=\sin^{-1}\!\left\{x\sqrt{1-y^2}+y\sqrt{1-x^2}\right\}$\B{; যখন} $x^2+y^2\leq1$

\sub{v} $\sin^{-1}x-\sin^{-1}y=\sin^{-1}\!\left\{x\sqrt{1-y^2}-y\sqrt{1-x^2}\right\}$

\sub{vi} $\cos^{-1}x+\cos^{-1}y=\cos^{-1}\!\left\{xy-\sqrt{(1-x^2)(1-y^2)}\right\}$\B{; যখন} $x+y\geq0$

\sub{vii} $\cos^{-1}x-\cos^{-1}y=\cos^{-1}\!\left\{xy+\sqrt{(1-x^2)(1-y^2)}\right\}$

\sub{viii} $2\tan^{-1}x=\tan^{-1}\!\dfrac{2x}{1-x^2}=\sin^{-1}\!\dfrac{2x}{1+x^2}=\cos^{-1}\!\dfrac{1-x^2}{1+x^2}$

\chsec{অধ্যায়-৮: স্থিতিবিদ্যা}

\itm{1} $P$ \B{ও} $Q$ \B{বলদ্বয়ের মধ্যবর্তী কোণ} $\alpha$ \B{এবং লব্ধি} $R$ \B{হলে,} $R=\sqrt{P^2+Q^2+2PQ\cos\alpha}$

\itm{2} $P$ \B{বল এবং লব্ধিবল} $R$ \B{এর মধ্যবর্তী কোণ} $\theta$ \B{হলে,} $\tan\theta=\dfrac{Q\sin\alpha}{P+Q\cos\alpha}$

\itm{3} \B{বল বিভাজন:}

\sub{i} $\dfrac{P}{\sin\beta}=\dfrac{Q}{\sin\alpha}=\dfrac{F}{\sin(\alpha+\beta)}$

\sub{ii} $P,Q$ \B{ও তাদের লব্ধি} $F$ \B{বলত্রয়} $OX$ \B{এর সাথে যথাক্রমে} $\alpha,\beta,\theta$ \B{কোণ উৎপন্ন করলে উপরোক্ত সূত্রটি হবে} $P\cos\alpha+Q\cos\beta=F\cos\theta$

\itm{4} $P,Q$ \B{সদৃশ সমান্তরাল বলের ক্ষেত্রে লব্ধি,} $R=P+Q$ \B{এবং} $P.AC=Q.BC$

\itm{5} $P,Q\;(P>Q)$ \B{অসদৃশ সমান্তরাল বলের ক্ষেত্রে লব্ধি,} $R=P-Q$ \B{এবং} $P.AC=Q.BC$

\chsec{অধ্যায়-৯: সমতলে বস্তুকণার গতি}

\itm{1} \B{কোনো বিন্দুতে কার্যরত} $u$ \B{ও} $v$ \B{বেগদ্বয়ের মধ্যবর্তী কোণ} $\alpha$ \B{হলে,}

\B{লব্ধি বেগ,} $w=\sqrt{u^2+v^2+2uv\cos\alpha}$ \B{এবং} $u$ \B{বেগের সাথে উৎপন্ন কোণ,} $\theta=\tan^{-1}\!\dfrac{v\sin\alpha}{u+v\cos\alpha}$

\itm{2} \B{বিভিন্ন ক্ষেত্রে একবিন্দুগামী,} $u$ \B{ও} $v$ \B{বেগদ্বয়ের লব্ধির মান,}

\sub{i} \B{বৃহত্তম লব্ধি} $w_{\max}=u+v$

\sub{ii} \B{ক্ষুদ্রতম লব্ধি} $w_{\min}=u-v$ \B{[}$u>v$\B{]}

\sub{iii} \B{সমকোণে ক্রিয়ারত বেগদ্বয়ের লব্ধি} $w=\sqrt{u^2+v^2}$

\itm{3} \B{সমত্বরণে চলন্ত কণার গতির সমীকরণ}

\sub{i} $v=u+ft$ \quad
\sub{ii} $s=ut+\dfrac{1}{2}ft^2$ \quad
\sub{iii} $v^2=u^2+2fs$

\sub{iv} $t$\B{-তম সেকেন্ডে অতিক্রান্ত দূরত্ব} $=u+\dfrac{1}{2}f(2t-1)$

\itm{4} \sub{i} $h$ \B{উচ্চতায় অবস্থিত কোন বিন্দু হতে} $u$ \B{আদিবেগে খাড়া উপরে নিক্ষিপ্ত বস্তুকণা} $t$ \B{সময়ে} $v$ \B{বেগে ভূমিতে আঘাত করলে:}

\sub{a} $v=-u+gt$ \qquad \sub{b} $h=-ut+\dfrac{1}{2}gt^2$

\sub{ii} $h$ \B{উচ্চতা হতে পতনশীল বস্তুকণাটি} $\sqrt{\dfrac{2h}{g}}$ \B{সময় পরে} $\sqrt{2gh}$ \B{বেগে ভূমিতে পতিত হবে।}

\itm{5} \B{উর্ধ্বমুখী কণার}

\sub{i} \B{উথানকাল} $=\dfrac{u}{g}=$ \B{পতনকাল}

\sub{ii} \B{বৃহত্তম উচ্চতা,} $H=\dfrac{u^2}{2g}$

\sub{iii} \B{বিচরণকাল} $=\dfrac{2u}{g}$

\itm{6} $u$ \B{বেগে আনুভূমিকের সাথে} $\alpha$ \B{কোণে প্রক্ষিপ্ত কণার,}

\sub{i} \B{বৃহত্তম উচ্চতা,} $H=\dfrac{u^2\sin^2\alpha}{2g}$

\sub{ii} \B{বৃহত্তম উচ্চতায় পৌঁছাতে সময়,} $t=\dfrac{u\sin\alpha}{g}$

\sub{iii} \B{বিচরণকাল,} $T=\dfrac{2u\sin\alpha}{g}$

\sub{iv} \B{আনুভূমিক পাল্লা} $R=\dfrac{u^2\sin 2\alpha}{g}$

\sub{v} \B{বৃহত্তম আনুভূমিক পাল্লা} $=\dfrac{u^2}{g}$

\sub{vi} $t$ \B{সময়ে আনুভূমিক সরণ,} $x=u\cos\alpha\cdot t$

\sub{vii} $t$ \B{সময়ে উলম্ব সরণ,} $y=u\sin\alpha\cdot t-\dfrac{1}{2}gt^2$

\chsec{অধ্যায়-১০: বিস্তার পরিমাপ ও সম্ভাবনা}

\itm{1} $x_1,x_2,\ldots,x_n$ \B{কোনো তথ্যসেটের} $n$ \B{সংখ্যক তথ্যমান এবং গাণিতিক গড়} $\bar{x}$ \B{হলে,}

\B{গড় ব্যবধান} $=\dfrac{\sum|x-\bar{x}|}{n}$\B{, ভেদাঙ্ক,} $\sigma^2=\dfrac{\sum(x_i-\bar{x})^2}{n}=\dfrac{\sum x_i^2}{n}-\left(\dfrac{\sum x_i}{n}\right)^2$

\B{এবং পরিমিত ব্যবধান,} $\sigma=\sqrt{\dfrac{\sum(x_i-\bar{x})^2}{n}}=\sqrt{\dfrac{\sum x_i^2}{n}-\left(\dfrac{\sum x_i}{n}\right)^2}$

\itm{2} \B{কোনো গণসংখ্যা নিবেশনের শ্রেণিমানগুলি} $x_1,x_2,\ldots,x_n$ \B{এবং এদের গণসংখ্যা যথাক্রমে} $f_1,f_2,\ldots,f_n$ \B{হলে,}

\B{গড় ব্যবধান} $=\dfrac{\sum f_i|x-\bar{x}|}{N}$\B{, ভেদাঙ্ক,} $\sigma^2=\dfrac{\sum f_i(x_i-\bar{x})^2}{N}=\dfrac{\sum f_ix_i^2}{N}-\left(\dfrac{\sum f_ix_i}{N}\right)^2$

\B{এবং পরিমিত ব্যবধান,} $\sigma=\sqrt{\dfrac{\sum f_i(x_i-\bar{x})^2}{N}}=\sqrt{\dfrac{\sum f_ix_i^2}{N}-\left(\dfrac{\sum f_ix_i}{N}\right)^2}$

\itm{3} \sub{i} $A$ \B{ও} $B$ \B{বর্জনশীল ঘটনা হলে,} $P(A\cup B)=P(A)+P(B)$

\sub{ii} $A$ \B{ও} $B$ \B{অবর্জনশীল ঘটনা হলে,} $P(A\cup B)=P(A)+P(B)-P(A\cap B)$

\sub{iii} $A$ \B{ও} $B$ \B{স্বাধীন ঘটনা হলে,} $P(A\cap B)=P(A)\times P(B)$

\sub{iv} $A$ \B{ও} $B$ \B{অধীন ঘটনা হলে,} $P(A\cap B)=P(A)\times P(B|A)=P(B)\times P(A|B)$

\sub{v} $A$ \B{ও} $B$ \B{সম্পূর্ণ ঘটনা হলে,} $P(A\cup B)=P(S)=1$

\end{multicols}

\end{document}
"""

with open("maxdoc.tex", "w", encoding="utf-8") as f:
    f.write(tex_content)

def run(cmd):
    result = subprocess.run(cmd, shell=True)
    return result.returncode

run("apt update -qq --allow-unauthenticated 2>/dev/null; apt install -y texlive-xetex texlive-fonts-recommended texlive-latex-extra texlive-lang-other fonts-noto-core fonts-noto-extra 2>/dev/null")
run("fc-cache -fv 2>/dev/null")
run("xelatex -interaction=nonstopmode maxdoc.tex")
run("xelatex -interaction=nonstopmode maxdoc.tex")
print("PDF ready:", os.path.exists("maxdoc.pdf"))
