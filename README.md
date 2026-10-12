# 1. sabse phele terminal par ye karo

git pull origin main

# fir ye command run karna jisme 'chnaged-message' ki jaga kuch bhi likh sakte ho jo tumare timeline ka name hoga. iska matlab kaam karne se phele new timeline banane lo. example- new timeline banane ke liye 'git checkout -b ' use karte hai

git checkout -b changed-message

# 2. fir jo bhi kaam karna hai kar lena for eg. backend/main.py me message change kar dena.

git add .

# message me kuch bhi lik sakte ho describe karte hue jo tumne kiya

git commit -m "Change message from backend to x"

# jo git checkout ke time timeline ka name likha tha eg. changed-message wahi likhna

git push -u origin changed-message

# 3. time line change karne ke liye 'git checkout ' use kaete hai. (example - 'git checkout main' ya fir git checkout changed-message) jo timline bane hui hai usse par change kar sakte hai.

git checkout main

# NEXT DAY

# 4. Fir jab kabhi kaam karna hoga tab. jisse latest updated code jo mene ya kisse ne likha ho vo mil jaye

git checkout main

git pull origin main

# 5. dusra timeline banaoge jisme 'second-task' ke jage kuch bhi name dal do timeline ka

git checkout -b second-task

# fir wahi kaam karne ke badd git add . git commit wala sab jo upar likha tha

# YOU can write git branch to show all git branches/timelines and the green highlited one will be the current branch\timeline that you are in. use git checkout name-of-branch to chnage branch.

git branch
