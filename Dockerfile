FROM debian
# Step 1 done
RUN apt-get update && apt-get install -y git lsb-release vim && git config --global user.email "you@example.com" && git config --global user.name "Your Name" && mkdir -p myproject
# Step 2 done
WORKDIR /myproject
# Step 3 done
RUN git init 
# Step 4 done
RUN echo Line1 > afile
# Step 5 done
RUN git add afile
# Step 6 done
RUN git commit -am Line1
# Step 7 done
RUN echo Line2 >> afile 
# Step 8 done
RUN git commit -am Line2
# Step 9 done
RUN git branch feature_1
# Step 10 done
RUN echo Line3 >> afile
# Step 11 done
RUN git commit -am Line3
# Step 12 done
RUN git checkout feature_1
# Step 13 done
RUN echo FeatureLine1 >> afile
# Step 14 done
RUN git commit -am FeatureLine1
# Step 15 done
RUN git checkout master
# Step 16 done
RUN git merge feature_1 || /bin/true
# Step 17 done
RUN echo -e -n "Line1\nLine2\nLine3\nFeatureLine1" > afile
# Step 18 done
RUN git commit -am Merged
# Step 19 done
RUN git checkout HEAD^
# Step 20 done
RUN git branch -f master
# Step 21 done
RUN git checkout feature_1
# Step 22 done
RUN git rebase master || /bin/true
# Step 23 done
RUN echo -e -n "Line1\nLine2\nLine3\nFeatureLine1\n" > afile
# Step 24 done
RUN git add afile
# Step 25 done
RUN git rebase --continue
# Step 26 done
RUN git checkout master
# Step 27 done
RUN git merge feature_1
# Step 28 done
CMD /bin/bash
