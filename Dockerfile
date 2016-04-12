FROM alpine
RUN apk update && apk add git
RUN git config --global user.email "you@example.com"
RUN git config --global user.name "Your Name"
RUN git init
RUN echo Line1 > afile
RUN git add afile
RUN git commit -am Line1
RUN echo Line2 >> afile
RUN git commit -am Line2
RUN git branch feature_1
RUN echo Line3 >> afile
RUN git commit -am Line3
RUN git checkout feature_1
RUN echo FeatureLine1 >> afile
RUN git commit -am FeatureLine1
RUN git checkout master
RUN git merge feature_1 || /bin/true
RUN echo "Line1\nLine2\nLine3\nFeatureLine1\n" > afile
RUN git commit -am Merged
RUN git checkout HEAD^
RUN git branch -f master
RUN git checkout feature_1
RUN git rebase master || /bin/true
RUN echo "Line1\nLine2\nLine3\nFeatureLine1\n" > afile
RUN git add afile
RUN git rebase --continue
RUN git checkout master
RUN git merge feature_1


