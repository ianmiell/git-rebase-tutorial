FROM debian
# Step 2 done
RUN apt-get update && apt-get install -y git lsb-release vim bsdmainutils man-db manpages && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject
# Step 3 done
WORKDIR /myproject
# Step 4 done
RUN git init 
# Step 5 done
RUN echo Line1 > afile
# Step 6 done
RUN git add afile
# Step 7 done
RUN git commit -am Line1
# Step 8 done
RUN echo Line2 >> afile 
# Step 9 done
RUN git commit -am Line2
# Step 10 done
RUN git branch feature_1
# Step 11 done
RUN echo Line3 >> afile
# Step 12 done
RUN git commit -am Line3
# Step 13 done
RUN git checkout feature_1
# Step 14 done
RUN echo FeatureLine1 >> afile
# Step 15 done
RUN git commit -am FeatureLine1
# Step 16 done
RUN git checkout master
# Step 17 done
RUN git merge feature_1 || /bin/true
# Step 18 done
RUN /bin/bash -c 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile'
# Step 19 done
RUN git commit -am Merged
# Step 20 done
RUN git checkout HEAD^
# Step 21 done
RUN git branch -f master
# Step 22 done
RUN git checkout feature_1
# Step 23 done
RUN git rebase master || /bin/true
# Step 24 done
RUN /bin/bash -c 'echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile'
# Step 25 done
RUN git add afile
# Step 26 done
RUN git rebase --continue
# Step 27 done
RUN git checkout master
# Step 28 done
RUN git merge feature_1
# Step 29 done
CMD /bin/bash
