Git and GitHub
Created a repo, made a commit, pushed main.
Created branch-55503, edited app.py, committed, pushed.
Still to do: open the pull request on GitHub.
Fix needed: the compose file was committed as docker-compose.yml). Rename it, commit, push.
Don’t commit the symlink on Windows.
3. Docker image and Docker Hub
Built saira102/app-55503:v1 from the Dockerfile.
Pushed it to Docker Hub. The first pushes failed because the image name must start with your Docker Hub username (saira102).
4. Running a container
Ran with -p 8003:5000 and -e REDIS_HOST=....
Read the output with docker logs.
5. Docker Compose
Two services: web (your Flask app) and redis.
Named volume redis-data for persistence.
Fixed errors: wrong filename and a malformed volumes: section.
Proved persistence: the visit counter continued after down and up.
Missing: a custom network. I gave you the corrected file with mynet.
6. Linux commands
grep, awk, sort, uniq for filtering and counting.
chmod 755, hard link (ln) and soft link (ln -s), and reading ls -l.
Issues: run grep -c for the line count, run the pipeline in one WSL command, and work in the WSL home folder so permissions show correctly.
7. Review of your work
Compared your terminal log against the requirements and listed what worked and what was missing.
Read your code files (app.py, Dockerfile, compose file) and gave the corrected compose file.
8. Full exam flow
Wrote the whole sequence of commands in order, with your names filled in (55503saira, saira102, roll 55503, port 8003).
9. README
Wrote a README for the repo describing the project, how to run it, and the Git workflow.
Add it with git add, commit and push.
Remaining checklist
Update the compose file (custom network) and the Dockerfile ENV.
Fix the filename in Git, then commit and push.
Open the pull request.
Run grep -c and the Linux commands inside WSL.
Add and push the README