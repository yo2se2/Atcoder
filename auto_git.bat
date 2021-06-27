cd C:\Users\yonezawa\github\atcoder
git init
git config --global user.name "yo2se2"
git config --global user.email "yo2se2@gmail.com"
git clone https://github.com/yo2se2/atcoder C:\Users\yonezawa\github\atcoder\atcoder
xcopy /d C:\Users\yonezawa\desktop\atcoder C:\Users\yonezawa\github\atcoder\atcoder
cd atcoder
git add --all
git commit -m "auto commit"
git push -f
exit