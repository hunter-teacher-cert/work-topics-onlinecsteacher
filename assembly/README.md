* Last Name: Wingreen
* First Name: Emma

**Homework (buggy):** \
INP \
STA 99 \
INP \
ADD 99 \
STA 99 \
INP \
SUB 99 \
OUT \
HLT


**Homework (debugged):** \
INP \
STA 99 \
INP \
ADD 99 \
STA 99 \
INP \
STA 98 \
LDA 99 \
SUB 98 \
OUT \
HLT


**Mild:** \
INP \
STA 99 \
INP \
STA 98 \
SUB 99 \
BRP 10 \
LDA 99 \
OUT \
HLT \
HLT \
LDA 98 \
OUT


**Spicy:** \
INP \
SUB b \
STA 91 \
LDA 91 \
BRP 8 \
LDA 40 \
OUT \
HLT \
SUB b \
STA 91 \
INP \
ADD 40 \
STA 40 \
BRA 3 \
b DAT 1

