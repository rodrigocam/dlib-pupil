import dlib

options = dlib.simple_object_detector_training_options()
options.C = 1.0
options.num_threads = 8
options.be_verbose = True
dlib.train_simple_object_detector('/home/shammyz/repos/dlib-pupil/annotations.xml', '/home/shammyz/repos/dlib-pupil/detector.svm', options)

print("[INFO] training accuracy: {}".format(
    dlib.test_simple_object_detector('/home/shammyz/repos/dlib-pupil/annotations.xml', '/home/shammyz/repos/dlib-pupil/detector.svm')))

