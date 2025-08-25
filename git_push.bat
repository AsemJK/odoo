@echo off
echo Adding all changes...
git config --global --add safe.directory .
rm .git/index.lock
git add .
echo Committing changes...
git commit -m "save"
echo Pushing to remote repository...
git push origin main
echo Done!
exit