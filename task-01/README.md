BANDIT TASKS

task0->As I'm not aware of ssh.I struggled initially.But it was fine after.password:bandit0

task0–1>just usage of ls and cat to read the file.password:ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If

task1–2>usage of ls and cat ./- to read file named -.password:263JGJPfgU6LtdEvgfWU1XP5yac29mFx

task2–3>used cat ./ - spaces\ in\ this\ filename - command read the file.password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx

task3–4>used ls -a to show hidden files then cat ./…Hiding-From-You to read the file.password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

take4–5>used file ./* to find the readable file.password:4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

task5–6>used find -size 1033c to return the file size of 1033bytes then used cat maybehere07/.file2 to read the file.password:HWasnPhtq9AVKe0dmk45nxy20cvUa6EG

task6–7>used find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null to get the path to password and cat /var/lib/dpkg/info/bandit7.password for getting password.password:morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj

task7–8>used grep "millionth" data.txt.password:dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc

task8–9>used sort data.txt|uniq -u to get the only once occured line.password:4CKMh1JI91bUIZZPXDqGanal4xvAg0JM

task9–10>used strings data.txt | grep "=" to get the password for this level.password:FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey

task10–11>used cat data.txt to get base64 line then changed the format.password:dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

task11–12>used cat data.txt to get Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4 and changed it from ROT13 to text.password:7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

task12–13>I've used /tmp/om to create temporary directory and cp data.txt /tmp/om to copy the file then xxd -r data.txt to retrive data in /tmp/om then used  gunzip,bunzip2,tar xf, to decompress the specified file.password:FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

task13–14>I've used ssh -i sshkey.private -p 2220 bandit14@localhost to tell ssh to use private key file in port 2220 from bandit14 as username and localhost as host.then cat /etc/bandit_pass/bandit14 to read this which is mentioned in levelgoal.password:MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

task14–15>i've used echo "MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS"| nc localhost 30000 to give input to localhost by using pipes.password:8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo.

task15–16>I've used openssl s_client -connect localhost:30001 to connect to port 30001 of localhost then gave level15 password as input.password:kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx.

GIT EXERCISES

##Exercise-01: master

→ Created a brand-new file and made an initial commit.
Commands used:

git start → Similar to git init; it runs the start.sh script located in the repository.

git verify → Used to check and submit when an exercise is completed.

Exercise-02: Commit a file

→ Made a new file called A.txt.
Commands used:

git add A.txt

git commit -m "Add A.txt file"

git verify

Exercise-03: commit-one-file-staged

→ Practiced the process of unstaging a file.
Commands used:

git reset -- B.txt

git add A.txt

git commit -m "Committed only A.txt"

Exercise-04: ignore-them

→ Created a .gitignore file to make Git skip unnecessary files.

The .gitignore file lists files or folders that Git should ignore — often temporary files, editor backups, or sensitive data.
Commands used:

git add .

git commit -m "Add only needed files"

git verify

Exercise-05: chase-branch

→ Learned to combine two branches into one using git merge.

This is helpful when different features are developed independently and need to be merged onto the main branch.
Commands used:

git checkout chase-branch

git merge escaped

git verify

Exercise-06: merge-conflict

→ Practiced resolving merge conflicts.

A conflict occurs when two branches alter the same part of a file differently.
Commands used:

git checkout merge-conflict

git merge another-piece-of-work

nano equation.txt

git add equation.txt

git commit -m "Fixed merge conflict"

git verify

Exercise-07: bugfix

→ Checked out the bugfix branch, removed the problematic line in bug.txt, and committed the fix.
Afterwards, switched back to the main branch and added an extra newline to the file.
Commands used:

git switch main

nano bug.txt

git add bug.txt

git commit -m "Inserted newline in bug.txt"


