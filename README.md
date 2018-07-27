# Face Recognition With Python
or
### "Who Watches the Project Managers"

Table of Contents
- [Understanding the basics of face recognition](#basics)
- [Why Python is used](#language)
- [Setting up a simple Python face recognition library](#setup)
- Identifying people in photos
- Idenetifying people in real-time using your webcam

# Basics
There are many approaches used to accurately recognize faces in photos, but they all follow relatively similar steps.

Most face recognition libraries are built using machine learning. The libraries are trained by having users identify faces in batches of pictures until a pattern is learned.

Usually a library will identify face "landmarks" such as eyes, nose, mouth and chin. These landmarks are used to locate all the faces in a photo, then used for comparison with existing "known" photos that have been positively identified.

One of the most recognized benchmarks for facial recognition success is the [Labeled Faces in the Wild](http://vis-www.cs.umass.edu/lfw/) test. This test contains 13,000 identified photos of people's faces with a wide range of cameras angles, lighting and quality. These images are used as reference points to test accurate identification of the same subjects in other pictures.

# Language
We're going to use the Python library [Face Recognition](https://github.com/ageitgey/face_recognition) because it provides a much nicer wrapper around a C++ library that has a 99.38% accuracy using images from "Labeled Faces in the Wild". Mainly because no one has time for C++, and Python is typically the go-to language for machine-learning and data sciences.

# Setup
Enough theory, let's set things up.

I'd recommend using [Pipenv](https://docs.pipenv.org/) to set up your environment. Detailed instructions [are here](https://docs.pipenv.org/install/#installing-pipenv), but if you're using a Mac you can use `brew install pipenv` to get it set up.

Then run:
```
pipenv install
pipenv shell
pip install face_recognition
pip install Pillow
pip install opencv-python
```