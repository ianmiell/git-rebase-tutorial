FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject && touch /root/.bash_history
# Step 3 done
WORKDIR /myproject
# Step 4 done
RUN git init && echo 'git init' >> /root/.bash_history
# Step 5 done
RUN echo Line1 > afile && echo 'echo Line1' >> /root/.bash_history
# Step 6 done
RUN git add afile && echo 'git add afile' >> /root/.bash_history
# Step 7 done
RUN git commit -am Line1 && echo 'git commit -am Line1' >> /root/.bash_history
# Step 8 done
RUN echo Line2 >> afile  && echo 'echo Line2 >> afile' >> /root/.bash_history
# Step 9 done
RUN git commit -am Line2 && echo 'git commit -am Line2' >> /root/.bash_history
# Step 10 done
RUN git branch feature_1 && echo 'git branch feature_1' >> /root/.bash_history
# Step 11 done
RUN echo Line3 >> afile && echo 'echo Line3' >> /root/.bash_history
# Step 12 done
RUN git commit -am Line3 && echo 'git commit -am Line3' >> /root/.bash_history
# Step 13 done
RUN git checkout feature_1 && echo 'git checkout feature_1' >> /root/.bash_history
# Step 14 done
RUN echo FeatureLine1 >> afile && echo 'echo FeatureLine1' >> /root/.bash_history
# Step 15 done
RUN git commit -am FeatureLine1 && echo 'git commit -am FeatureLine1' >> /root/.bash_history
# Step 16 done
RUN git checkout master && echo 'git checkout master' >> /root/.bash_history
# Step 17 done
RUN git merge feature_1 || /bin/true && echo 'git merge feature_1' >> /root/.bash_history
# Step 18 done
RUN /bin/bash -c 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile' && echo 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile' >> /root/.bash_history
# Step 19 done
RUN git commit -am Merged && echo 'git commit -am merged' >> /root/.bash_history
# Step 20 done
RUN git checkout HEAD^ && echo 'git checkout HEAD^' >> /root/.bash_history
# Step 21 done
RUN git branch -f master && echo 'git branch -f master' >> /root/.bash_history
# Step 22 done
RUN git checkout feature_1 && echo 'git checkout feature_1' >> /root/.bash_history
# Step 23 done
RUN git rebase master || /bin/true && echo 'git rebase master' >> /root/.bash_history
# Step 24 done
RUN /bin/bash -c 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile' && echo 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile' >> /root/.bash_history
# Step 25 done
RUN git add afile && echo 'git add afile' >> /root/.bash_history
# Step 26 done
RUN git rebase --continue && echo 'git rebase' >> /root/.bash_history
# Step 27 done
RUN git checkout master && echo 'git checkout master' >> /root/.bash_history
# Step 28 done
RUN git merge feature_1 && echo 'git merge feature_1' >> /root/.bash_history
# Step 29 done
CMD /bin/bash
